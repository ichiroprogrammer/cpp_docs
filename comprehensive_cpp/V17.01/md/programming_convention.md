<!-- ./md/programming_convention.md -->
# 3 プログラミング規約 <a id="SS_3"></a>
組織に秩序を与える法、道徳、慣習等をここではルールと呼ぶことにする。
当然ながら、秩序ある組織には良いルールがあり、混沌とした組織には悪いルールがあるか、
ルールはあっても守られていないか、そもそもルールが存在しない。

秩序あるソースコードとは、

* 可読性が高い。
    * 簡潔に記述されている。
    * 記述スタイルが統一されている(「[コーディングスタイル](coding_style.md#SS_5)」参照)。
    * ファイルや識別子の名前に規則性があり、適切に命名されている
      (「[Name and Conquer](software_practice.md#SS_2_5)」、「[命名規則](naming_practice.md#SS_6)」参照)。 
    * コメントの記法が統一されており、内容が適切である(「[コメント](comment.md#SS_7)」参照)。 
* 保守、テスト、移植等が容易である。
* 型安全性が配慮されている。
* コンパイル警告レベルが高く、かつ指摘がない(「[g++の警告機能](code_analysis.md#SS_4_1_1)」参照)。

のような特性を満たすものであるが、そうあるためには秩序ある組織と同様に良いルールが必要である。
本章の目的は、C++プログラミングにおけるそのようなルール(=プログラミング規約)を示すことである。

なお、型安全性とは、「正しく型付けされたソースコードは未定義動作をしない」
ことが保証されるという言語の特性である。
配列のオーバランが未定義動作を引き起こすことを考えれば明らかである通り、
C++は型安全性を保証しない。このことは、C++の劣等性を意味しないが、
それに配慮したプログラミング(型システムの最大限の利用等)が必要となることは事実である。

## 3.1 型とインスタンス <a id="SS_3_1"></a>

### 3.1.1 算術型 <a id="SS_3_1_1"></a>

#### 3.1.1.1 整数型 <a id="SS_3_1_1_1"></a>
* [整数型](term_explanation.md#SS_18_1_3)には、整数の基本型(intやlong等)を直接使わずに、
  [cstdint](https://cpprefjp.github.io/reference/cstdint.html)
  で定義されている型エイリアスを使用する。
    * STLやPOSIX等の標準クラスや関数のインターフェースが基本型を直接使用している場合は、
      その型に合わせるために基本型を直接使用する。
* 整数型には、特に理由がない限りに、int32\_tを使用する。
* 整数型の変数が負にならないのであれば、uint32\_tを使用する。
    * 符号あり型との演算がある場合は、その変数が負にならなくともint32\_tを使用する。
    * 符号あり型と符号なし型との比較をしない。
* sizeofの値や配列の長さの保持等には、size\_tを使用する。
* int32_tからint16_tや、int32_tからuint32_t等の値が変わる可能性がある代入を避ける。
  やむを得ずそのような代入をする場合、下記のようなnarrow_castを使いこのような問題を緩和する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 9

    template <typename DST, typename SRC>
    DST narrow_cast(SRC v)
    {
        static_assert(std::is_integral_v<DST> && std::is_integral_v<DST>,
                      "DST, SRC shoud be integral-type.");
        auto r = static_cast<DST>(v);

        assert((r < 0) == (v < 0));        // 符号が変わっていないことの確認
        assert(static_cast<SRC>(r) == v);  // bit落ちしていないことの確認

        return r;
    }
```

```cpp
    // @@@ example/programming_convention/type_ut.cpp 28

    auto ui32 = narrow_cast<uint32_t>(128);                // 安全なint32_t -> uint32_t
    ASSERT_EQ(ui32, 128);                                  //
    ASSERT_DEATH(ui32 = narrow_cast<uint32_t>(-128), "");  // 危険なint32_t -> uint32_t

    auto i8 = narrow_cast<int8_t>(127);                    // 安全なint32_t -> int8_t
    ASSERT_EQ(i8, 127);                                    //
    ASSERT_DEATH(i8 = narrow_cast<int8_t>(128), "");       // 危険なint32_t -> int8_t

    i8 = narrow_cast<int8_t>(-1);                          // 安全なint32_t -> int8_t
    ASSERT_EQ(i8, -1);                                     //
    ASSERT_DEATH(i8 = narrow_cast<int8_t>(-129), "");      // 危険なint32_t -> int8_t
```

* [演習-汎整数型の選択](exercise_q.md#SS_19_1_1)

#### 3.1.1.2 char型 <a id="SS_3_1_1_2"></a>
* charはascii文字の保持のみに使用する。
* char\*をvoid\*の代わりに使わない。
* charがsingedかunsignedかは処理系に依存するため、char型を[汎整数型](term_explanation.md#SS_18_1_2)として扱わない。
  8ビット整数には、int8\_tまたは、uint8\_tを使用する。
    * バイトストリームを表現する場合、int8_t\*、int8_t[]、uint8_t\*、uint8_t[]のいずれかを使う。

* [演習-汎整数型の演算](exercise_q.md#SS_19_1_2)

#### 3.1.1.3 std::byte型 <a id="SS_3_1_1_3"></a>
* intよりもビット幅の小さい組み込み型の演算の結果は[汎整数拡張](term_explanation.md#SS_18_1_5)によりint型になるため、
  uint8_tのビット演算の型もintとなる。
  intへの拡張が意図したものかどうかの判別は困難であるため、
  uint8_tインスタンスにビット演算が必要な場合、
  uint8_tの代わりに下記のようにstd::byte(「[BitmaskType](design_pattern.md#SS_9_2)」参照)を用いる。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 50
    // uint8_tのビット演算例

    auto u    = uint8_t{0b1000'0001};
    auto ret0 = u << 1;
    // uint8_t ret1{u << 1};  // 縮小型変換のため、コンパイルエラー
    uint8_t ret1 = u << 1;

    static_assert(std::is_same_v<decltype(ret0), int>);  // u << 1はintになる
    ASSERT_EQ(0b1'0000'0010, ret0);
    ASSERT_EQ(0b0000'0010, ret1);
```

```cpp
    // @@@ example/programming_convention/type_ut.cpp 64
    // uint8_tに代わりstd::byteを使用したビット演算例

    auto b    = std::byte{0b1000'0001};
    auto ret0 = b << 1;
    auto ret1 = std::byte{b << 1};

    static_assert(std::is_same_v<decltype(ret0), std::byte>);  // b << 1はstd::byteになる
    ASSERT_EQ(std::byte{0b0000'0010}, ret0);
    ASSERT_EQ(std::byte{0b0000'0010}, ret1);
```

* std::byteの初期化には{}を用いる(static_castを使用しない)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 77

    std::byte b0{0b1000'0001};                           // OK
    auto      b1 = std::byte{0b1000'0001};               // OK
    std::byte b2 = static_cast<std::byte>(0b1000'0001);  // NG
    // std::byte b3 = 0b1000'0001;                       // NG コンパイルエラー
```

#### 3.1.1.4 bool型 <a id="SS_3_1_1_4"></a>
* bool型は、bool型リテラル(true/false)やbool型オブジェクトの保持のみに使用する。
* bool型を[汎整数型](term_explanation.md#SS_18_1_2)として扱わない。bool型に++を使用しない(--はコンパイルできない)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 95

    #if __cplusplus < 201703L  // 以下のコードはC++14以前ではコンパイルできるが、
                               // C++17以降ではコンパイルエラー

        auto b = false;

        ASSERT_EQ(1, ++b);  // NG 予想通り動作するが、boolの目的外使用
        ASSERT_EQ(1, ++b);  // NG bは2ではなく1
        // ASSERT_EQ(1, --b);  // NG コンパイルエラー
    #endif
```

* ポインタ型やboolを除く汎整数型のインスタンスをbool値として使用しない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 111

    void g(int32_t* ptr0, int32_t* ptr1) noexcept
    {
        if (ptr0) {  // NG ポインタ型をbool値として使用
            return;
        }

        if (ptr1 == nullptr) {  // OK
            return;
        }

        ...
    }
```

#### 3.1.1.5 浮動小数点型 <a id="SS_3_1_1_5"></a>
* floatやdoubleのダイナミックレンジが必要な場合のみに、これらの型を使用する。
  ちなみに銀河系の直径は1e+21メートル程度、プランク長は1.616229e-35メートルであるため、
  銀河から素粒子までのサイズを一つの基本型で表す場合においても、
  floatのダイナミックレンジに収まる。
  従って、floatやdoubleが必要になる場合は極めて限られる。


|                |正の最小値              |正の最大値                |
|:---------------|:----------------------:|:------------------------:|
| floatの範囲    |1.175494351 e-38        |3.402823466 e+38          |
| doubleの範囲   |2.2250738585072014 e-308|1.7976931348623158 e+308  |
| uint32_tの範囲 |0                       |4.294967295 e+9           |
| uint64_tの範囲 |0                       |1.8446744073709551615 e+19|

* 演算順序等により誤差が生じることがあるため、floatやdoubleのインスタンスを、
  ==、!=、>、<等で比較しない。

```cpp
    // @@@ example/programming_convention/float_ut.cpp 11

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    //  ASSERT_EQ(0.05F, a + b);  // NG  a + b == 0.05Fは一般には成立しない。
    ASSERT_NE(0.05F, a + b);
```
```cpp
    // @@@ example/programming_convention/float_ut.cpp 22

    /// @fn bool is_equal_f(float lhs, float rhs) noexcept
    /// @brief float比較用関数
    bool is_equal_f(float lhs, float rhs) noexcept
    {
        return std::abs(lhs - rhs) <= std::numeric_limits<float>::epsilon();
    }
```
```cpp
    // @@@ example/programming_convention/float_ut.cpp 34

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    // floatの比較はis_equal_fのような関数を使う。
    ASSERT_TRUE(is_equal_f(0.05F, a + b));  // OK
```

* 一つの式にfloatとdoubleを混在させない。

```cpp
    // @@@ example/programming_convention/float_ut.cpp 46

    // 上記例と似たソースコードであるが、下記のような問題が起こる
    /// @fn bool is_equal_d(double lhs, double rhs) noexcept
    /// @brief double比較用関数
    bool is_equal_d(double lhs, double rhs) noexcept
    {
        return std::abs(lhs - rhs) <= std::numeric_limits<double>::epsilon();
    }
```
```cpp
    // @@@ example/programming_convention/float_ut.cpp 59

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    // a + bはfloatの精度のまま、is_equal_dの引数の型であるdoubleに昇格される。
    // 一方、0.05はdoubleであるため(循環小数をdoubleの精度で切り捨てた値であるため)、
    // a + b(floatの精度の値)と0.05の差はdoubleのepsilonを超える。
    //  ASSERT_TRUE(is_equal_d(0.05, a + b));  // NG
    ASSERT_FALSE(is_equal_d(0.05, a + b));
```
```cpp
    // @@@ example/programming_convention/float_ut.cpp 73

    // is_equal_dを改良して、引数の型が統一されていない呼び出しをコンパイルエラーにできるようにした。
    /// @fn bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    /// @brief 浮動小数点比較用関数
    template <typename FLOAT_0, typename FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        static_assert(std::is_floating_point_v<FLOAT_0>, "FLOAT_0 shoud be float or double.");
        static_assert(std::is_same_v<FLOAT_0, FLOAT_1>, "FLOAT_0 and FLOAT_1 shoud be a same type.");

        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }
```
```cpp
    // @@@ example/programming_convention/float_ut.cpp 90

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    // a + bはfloatであり、0.05はdoubleであるため、下記コードはコンパイルできない。
    // ASSERT_TRUE(is_equal(0.05, a + b));
    ASSERT_TRUE(is_equal(0.05F, a + b));  // OK リテラルに型を指定して、引数の型を統一
```

* INFや、NANを演算で使用しない。
* [汎整数型](term_explanation.md#SS_18_1_2)の演算とは違い、0除算等の浮動小数点演算のエラーは、
  通常、プログラム終了シグナルを発生させないため、
  浮動小数点演算のエラーを捕捉する必要がある場合(ほとんどの場合、そうなる)は、
  std::fetestexcept()、std::isnan()、std::isinf()等を使用してエラーを捕捉する。

```cpp
    // @@@ example/programming_convention/float_ut.cpp 102

    int   global_zero{0};
    float div(float a, float b) noexcept { return a / b; }
```
```cpp
    // @@@ example/programming_convention/float_ut.cpp 110

    std::feclearexcept(FE_ALL_EXCEPT);  // エラーをクリア

    div(1.0F, 0.0F);  // 関数の中で0除算するが、終了シグナルは発生しない
    ASSERT_TRUE(std::fetestexcept(FE_ALL_EXCEPT) & FE_DIVBYZERO);  // 0除算

    std::feclearexcept(FE_ALL_EXCEPT);  // エラーをクリア

    div(std::numeric_limits<double>::max(), 1);

    auto const excepts = std::fetestexcept(FE_ALL_EXCEPT);

    ASSERT_FALSE(excepts & FE_DIVBYZERO);  // 0除算
    ASSERT_TRUE(excepts & FE_INEXACT);     // 演算が不正確
    ASSERT_FALSE(excepts & FE_INVALID);    // 不正な操作
    ASSERT_TRUE(excepts & FE_OVERFLOW);    // 演算がオーバーフローを起こした
    ASSERT_FALSE(excepts & FE_UNDERFLOW);  // 演算がアンダーフローを起こした

    std::feclearexcept(FE_ALL_EXCEPT);  // エラーをクリア

    auto const a = 1.0F / global_zero;  // global_zero == 0
    ASSERT_TRUE(std::isinf(a));

    auto const b = std::sqrt(-1);
    auto const c = std::sqrt(-1);
    ASSERT_TRUE(std::isnan(b));
    ASSERT_FALSE(b == c);  // NaN == NaNは常にfalse
```

* できる限り浮動小数点の代わりに固定小数点を使用する
  (全ソースコードは「"[example/programming_convention/fixed_point.h](sample_code.md#SS_23_2_37)"」に掲載)。

```cpp
    // @@@ example/programming_convention/fixed_point.h 6

    /// @class FixedPoint
    /// @brief BASIC_TYPEで指定する基本型のビット長を持つ固定小数点を扱うためのクラス
    /// @tparam BASIC_TYPE       全体のビット長や、符号を指定するための整数型
    /// @tparam FRACTION_BIT_NUM 小数点保持のためのビット長
    template <typename BASIC_TYPE, uint32_t FRACTION_BIT_NUM>
    class FixedPoint {
    public:
        FixedPoint(BASIC_TYPE                                integer  = 0,
                   typename std::make_unsigned_t<BASIC_TYPE> fraction = 0) noexcept
            : value_{get_init_value(integer, fraction)}
        {
            ...
        }

        ...
        FixedPoint& operator+=(FixedPoint rhs) noexcept
        ...
        FixedPoint& operator-=(FixedPoint rhs) noexcept
        ...
        FixedPoint& operator*=(FixedPoint rhs) noexcept
        ...
        FixedPoint& operator/=(FixedPoint rhs) noexcept
        ...
    private:
        BASIC_TYPE value_;
        ...

        friend bool operator==(FixedPoint lhs, FixedPoint rhs) noexcept
        ...

        // FixedPoint() + intのようなオーバーロードを作るためにあえてfriend
        friend FixedPoint operator+(FixedPoint lhs, FixedPoint rhs) noexcept
        ...
    };
```
```cpp
    // @@@ example/programming_convention/fixed_point_ut.cpp 19

    // 以下は、FixedPoint<>の使用例である。
    {
        using FP4 = FixedPoint<uint8_t, 4>;  // 基本型uint8_t、小数点4ビット
        auto fp0  = FP4{};

        ...
        fp0 = 7;    ASSERT_EQ(7, fp0);
        fp0 = 7;    ASSERT_NE(6, fp0);
        fp0 += 2;   ASSERT_EQ(FP4{9}, fp0);         
                    ASSERT_TRUE(is_equal(9.0, fp0.ToFloatPoint()));
        fp0 /= 2;   ASSERT_EQ((FP4{4, 8}), fp0);    
                    ASSERT_TRUE(is_equal(4.5, fp0.ToFloatPoint()));
        fp0 /= 2;   ASSERT_EQ((FP4{2, 4}), fp0);    
                    ASSERT_TRUE(is_equal(2.25, fp0.ToFloatPoint()));
        fp0 *= 4;   ASSERT_EQ(FP4{9}, fp0);
        fp0 += 7;   ASSERT_EQ(FP4{0}, fp0);
    }
    ...
    {
        using FP8 = FixedPoint<int32_t, 8>;  // 基本型int32_t、小数点8ビット

        auto fp0 = FP8{};
        ...
        fp0 = 3;            ASSERT_EQ((FP8{3, 0}), fp0);
        fp0 += 3;           ASSERT_EQ((FP8{6, 0}), fp0);
        fp0 -= 3;           ASSERT_EQ((FP8{3, 0}), fp0);
        ...
        fp0 = 3;
        fp0 *= 5;           ASSERT_EQ((FP8{15, 0}), fp0);
        fp0 /= 5;           ASSERT_EQ((FP8{3, 0}), fp0);
        fp0 = fp0 / 2;      ASSERT_EQ((FP8{1, 0x80}), fp0);
        ...
    }
```

* [演習-浮動小数点型](exercise_q.md#SS_19_1_3)

### 3.1.2 enum <a id="SS_3_1_2"></a>
* C++の強力な型システムや、コンパイラの静的解析機能(switchでのcase抜け)を効果的に使用するために、
  一連の定数の列挙にはenumを使用する。
* 使用範囲や方法が明示しづらく、且つ整数型への[算術変換](term_explanation.md#SS_18_1_4)が行われてしまう旧来のenum
  (非スコープドenum)は、一部の例外を除き定義しない。
  代わりに、より型安全なスコープドenumを使用する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 133

    enum CarLight { CL_Red, CL_Yellow, CL_Blue };
    enum WalkerLight { WL_Red, WL_Yellow, WL_Blue };

    bool f(CarLight cl) noexcept
    {
        switch (cl) {
        // 非スコープドenumは下記のようなコードを許容する(if文でも同様)。
        // スコープドenumであればこのような間違いはコンパイルエラーで発見できる。
        case WL_Red:  // CL_Regの間違い?
            ...
            break;
        case CL_Yellow:  // これは正しい
        case CL_Blue:
        default:
            ...
            break;
        }

        ...
    }
```

* 列挙子に値を設定する必要がない場合（具体的な値に意味を持たない場合）には、値を設定しない。
  値を設定する場合にはそれらを最初に書き、同じ値を設定しない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 163

    enum Colour {   // NG スコープドになっていない。
        Red   = 0,  // NG 配列インデックスでない場合、0を定義する必要はない。
        Green = 1,  // NG 連続値を定義する必要はない。
        Blue  = 2
    };

    ...

    enum class Colour {  // OK
        Red,             // OK 不要な記述がない。
        Green,
        Blue
    };
```

* enumを配列のインデックスとして使う場合は以下のようにする。
    * スコープドenumの代わりに、旧来のenumをstruct内で定義する。
    * 最初に定義されるenumメンバは0で初期化する。
    * 最後の要素のシンボル名はMaxで終わることにより、
      その要素が最大値であることを示す。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 185

    enum class Foo { FooA = 0, FooB, FooMAX };

    struct Hoo  // structによるスコーピング
    {
        enum {
            HooA = 0,  // OK
            HooB,      // OK 値は暗黙に定義
            HooMAX     // OK
        };
    };

    void f() noexcept
    {
    //  int32_t a0[Foo::FooMAX];                       // NG コンパイルエラー
        int32_t a1[static_cast<size_t>(Foo::FooMAX)];  // NG castが必要になる
        int32_t a2[Hoo::HooMAX];                       // OK
        ...
    }
```

* enumはC++11から前方宣言できるようになったため、
  この機能を使用して、不要なヘッダファイルの依存関係を作らないようにする。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 211

    enum class IncompleteEnum;
    enum class IncompleteEnum2 : uint64_t;

    // このファイルから可視である範囲にIncompleteEnum、IncompleteEnum2の定義はないが、
    // 前方宣言することで以下の関数宣言をすることができる。
    extern void g(IncompleteEnum);
    extern void g(IncompleteEnum2);
```

* アプリケーションの設定ファイルに保存された情報を復元させるような場合や、
  「[BitmaskType](design_pattern.md#SS_9_2)」を使用する場合を除き、enumへのキャストをしない。
* クラスのstatic constの整数定数の代わりにenumを使うことは、
  C++言語仕様やコンパイラの機能が不十分だった頃のテクニックであり、もはや不要である。
  代わりにstatic constexprインスタンス(「[constexprインスタンスと関数](term_explanation.md#SS_18_1_15)」参照)を使用する。
  こうすることで定数の型を明示できる。

* [演習-定数列挙](exercise_q.md#SS_19_1_4)
* [演習-enum](exercise_q.md#SS_19_1_5)

### 3.1.3 bit field <a id="SS_3_1_3"></a>
* ハードウエアレジスタにアクセスをする目的でのみ使用する。
* bit fieldの型は、unsigned intにする。

### 3.1.4 class <a id="SS_3_1_4"></a>
* 「[クラスとインスタンス](programming_convention.md#SS_3_2)」を参照せよ。

### 3.1.5 struct <a id="SS_3_1_5"></a>
* メンバ変数を持つ構造体は、[POD](term_explanation.md#SS_18_1_6)としてのみ使用する。
* メンバ変数を持つ構造体を基底クラスとした継承をしない。
  従ってそのような構造体は常にfinalであるが、finalの明示はしない。
* メンバ変数(static constやstatic constexprメンバは定数とする)を持たない構造体は、
  templateや非スコープドenumのスコーピング(「[enum](programming_convention.md#SS_3_1_2)」参照)等に使用しても良い。
* コンストラクタ以外のメンバ関数を定義しない。
    * [ディープコピー](term_explanation.md#SS_18_3_2)(「[コンストラクタ](programming_convention.md#SS_3_3_2_2)」参照)が必要な型は、structでなくclassで表す。
    * デフォルトコンストラクタを除く[特殊メンバ関数](programming_convention.md#SS_3_3_2_1)に対して、
      = defaultの明示をしない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 224

    struct Pod final {                        // NG finalは不要
        Pod()                     = default;  // OK
        ~Pod()                    = default;  // NG = defaultは不要
        Pod(Pod const&)           = delete;   // OK copyを禁止する場合
        Pod operator=(Pod const&) = delete;   // OK copyを禁止する場合

        int32_t x;
        int32_t y;
    };
```

* Cとシェアしない構造体を無名構造体とそのtypedefで定義しない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 237

    typedef struct {  // NG   無名構造体
        int32_t x;
        int32_t y;
    } StructNG;  // NG   無名構造体をtypedef

    typedef struct StructOK_C_Share {  // Cとシェアする場合OK
        int32_t x;
        int32_t y;
    } StructOK_C_Share;

    struct StructOK {  // OK   Cとシェアしない場合このように書く
        int32_t x;
        int32_t y;
    };
```

### 3.1.6 union <a id="SS_3_1_6"></a>
* ハードウエアレジスタにアクセスをする目的以外で使用しない(以下のような使い方のみ認められる)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 258

    union XXX_REG {
        uint8_t  bytes[4];
        uint32_t word32;
    };

    uint8_t f() noexcept
    {
        // 0x14000000はハードウェアレジスタのアドレスとする
        auto& XXX_REG_INST = *reinterpret_cast<XXX_REG*>(0x14000000);
        auto  byte_1       = XXX_REG_INST.bytes[1];

        return byte_1;
    }
```

* 上記のようなunionはランタイム依存性が強いため、それへの依存を最小にする。
  従って、unionの定義を外部パッケージに公開(「[パッケージの実装と公開](programming_convention.md#SS_3_7_1)」参照)しない。

* 上記以外でunionのような機能が必要な場合、
  std::variant(「[std::variantとジェネリックラムダ](template_meta_programming.md#SS_13_6_2_2)」参照)を使用する
  (std::anyはunionの代替えにはならないので、このような場合には使用しない)。

### 3.1.7 配列 <a id="SS_3_1_7"></a>
* 配列をnew[]により生成しない。
  可変長配列が必要な場合は、std::vectorを使用する(「[new](programming_convention.md#SS_3_5_6_1)」参照)。
  固定長配列を動的に確保する場合は、std::arrayをnewする。
* 配列からポインタへの暗黙の型変換をしない(「[キャスト、暗黙の型変換](programming_convention.md#SS_3_5_10)」参照)。
  特に、オブジェクトの配列をそのオブジェクトの基底クラスへのポインタに代入しないことは重要である
  (「[スライシング](programming_convention.md#SS_3_2_8)」参照)。
* 関数の仮引数を一見、配列に見える型にしない
  (「[実引数/仮引数](programming_convention.md#SS_3_3_3_5)」参照)。
* char型の配列を文字列リテラルで初期化する場合、配列の長さを指定しない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 279

    #if 0
        // g++では通常コンパイルエラーとなるが、-fpermissiveを付ければコンパイルできてしまう。
        char a[3]{"abc"};  // NG aはヌル終端されない
    #else
        char a[]{"abc"};  // OK
    #endif
```

* 配列の全要素にアクセスするような繰り返し処理には[範囲for文](programming_convention.md#SS_3_4_4)を使用する。

* [演習-配列の範囲for文](exercise_q.md#SS_19_1_6)

### 3.1.8 型エイリアス <a id="SS_3_1_8"></a>
* Cとシェアされる型エイリアスを除き、typedefではなくusingを使用する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 296

    // C90スタイル
    typedef unsigned int uint;                 // NG
    typedef void (*void_func_int32)(int32_t);  // NG

    ...

    // C++11スタイル
    using uint            = unsigned int;       // OK
    using void_func_int32 = void (*)(int32_t);  // OK

    template <class T>  // templateで型エイリアスを作ることもできる。
    using Dict = std::map<std::string, T>;  // OK
```

* 型へのポインタのエイリアスは、それを使用してconstポインタが定義できないため、
  型へのポインタ(関数ポインタを除く)のエイリアスを作らない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 320

    using pint32_t = int32_t*;  // pint32_tにはconstポインタを代入できない。

    pint32_t const pint32_0_c = nullptr;  // 一見pint32_0_cはconstポインタに見えるが。
    int32_t const* pint32_1_c = nullptr;

    // pint32_0_cの型とpint32_1_cの型が同じであれば問題ないのだが、
    // エイリアスのため結合順が変わった影響でそうはならない。
    // *pint32_0_cはconstではなく、pint32_0_cがconstとなる。
    static_assert(std::is_same_v<decltype(pint32_0_c),  int32_t* const>);
    static_assert(std::is_same_v<decltype(*pint32_0_c), int32_t&>);
    static_assert(std::is_same_v<decltype(pint32_1_c),  int32_t const*>);
    static_assert(std::is_same_v<decltype(*pint32_1_c), int32_t const&>);
```

* [演習-エイリアス](exercise_q.md#SS_19_1_7)

### 3.1.9 const/constexprインスタンス <a id="SS_3_1_9"></a>
* インスタンス、インスタンスへのポインタ、インスタンスへのリファレンス等に対して、
    * constexpr(「[constexprインスタンスと関数](term_explanation.md#SS_18_1_15)」参照)にできる場合、constexprにする。
    * constexprにはできないが、const(「[constインスタンス](term_explanation.md#SS_18_1_14)」にはできる場合、constにする。
      関数の仮引数になっているリファレンスやポインタをconstにすることは特に重要である
      (「[実引数/仮引数](programming_convention.md#SS_3_3_3_5)」、「[三項演算子](programming_convention.md#SS_3_5_5)」参照)。
    * 文字列リテラルのアドレスを非constポインタ型変数に代入しない(「[リテラル](programming_convention.md#SS_3_1_10)」参照)。
    * イテレータにおいても、可能な場合は、イテレータをconstするか、const_iteratorを使う。

```cpp
    // @@@ example/programming_convention/type_const_ut.cpp 13

    // name0は文字列リテラルを指すポインタなのでconstでなければならない。
    char const* name0 = "hoge";

    // name1は文字列リテラルでないのでconstでなくてよい。
    char name1[] = "hoge";

    char const* get_str();
    // 左側のconstはname2の指す先をconstにする。
    // 右側のconstはname2自体をconstにする。
    char const* const name2 = get_str();

    // name2の右辺がリテラルならば、下記のようにするべきである。
    constexpr char const* name3 = "hoge";

    void f(std::vector<int32_t>& vec)
    {
        std::vector<int32_t>::iterator const iter = vec.begin();  // iter自体がconst

        *iter = 10;
        // ++iter;      // 意図的にコンパイルエラー

        std::vector<int32_t>::const_iterator const_iter_0 = vec.begin();   // *const_iter_0がconst
        auto                                 const_iter_1 = vec.cbegin();  // *const_iter_1がconst
        static_assert(std::is_same_v<std::vector<int32_t>::const_iterator, decltype(const_iter_1)>);

        // *const_iter_0 = 10;   // 意図的にコンパイルエラー
        ++const_iter_0;

        // *const_iter_1 = 10;   // 意図的にコンパイルエラー
        ++const_iter_1;

        ...
    }
```

* constは、意味が変わらない範囲で出来るだけ右側に書く。

```cpp
    // @@@ example/programming_convention/type_const_ut.cpp 52

    const std::string s;  // NG
    std::string const t;  // OK

    const std::string* s_ptr;  // NG
    std::string const* t_ptr;  // OK

    const std::string& f();  // NG 関数の宣言
    std::string const& g();  // OK 関数の宣言

    char        abc[]{"abc"};
    const char* a = abc;  // NG *aはconst
    char const* b = abc;  // OK *aはconst
    char* const c = abc;  // NG *aではなく、aがconstになり、意味が変わる

    const char* const d = abc;  // NG
    char const* const e = abc;  // OK
```

* [演習-constの意味](exercise_q.md#SS_19_1_8)
* [演習-const/constexpr](exercise_q.md#SS_19_1_9)

### 3.1.10 リテラル <a id="SS_3_1_10"></a>
* ヌルポインタを表すポインタリテラルとして、nullptrを使用する(0やNULLを使用しない)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 343

    int32_t* a{0};        // NG   オールドスタイル
    int32_t* b{NULL};     // NG   C90の書き方
    int32_t* c{nullptr};  // OK   C++11
```
```cpp
    // @@@ example/programming_convention/type_ut.cpp 362

    extern int g(long a) noexcept;
    extern int g(int* a) noexcept;

    // NULLを使ったことで、わかりづらいバグが発生する例
    g(NULL);  // NG NULLはポインタではないため、この呼び出しはg(long)を呼び出す
    static_assert(std::is_same_v<long, decltype(NULL)>);

    g(nullptr);  // OK 意図通り、g(int*)を呼び出す。
    static_assert(std::is_same_v<std::nullptr_t, decltype(nullptr)>);

```

* 文字列リテラル("xxx")はconstオブジェクトとして扱う
  (「[const/constexprインスタンス](programming_convention.md#SS_3_1_9)」、「[std::string型リテラル](term_explanation.md#SS_18_1_17)」参照)。
* 長い[汎整数型](term_explanation.md#SS_18_1_2)リテラルを使用する場合は、適切に区切りを入れる(C++14)。
* ビットマスク等2進数を使用した方が直感的な場合には2進数リテラルを使用する(C++14)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 384

    auto a = 123'456'789U;       // = 123456789
    auto b = 0x123'456'789U;     // = 0x123456789
    auto c = 0b1001'0001'0101U;  // = 0x915
```

* bool型を表すリテラルにはtrue、falseを使用する。代わりに0、1、!0等を使わない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 395

    bool a{0};          // NG
    bool b{!0};         // NG
    bool c{false};      // OK
    auto d = bool{0};   // NG
    auto e = bool{!0};  // NG
    auto f = true;      // OK
```

* long値リテラルを表す文字には"l"ではなく、"L"を使う。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 408

    auto a = 432l;  // NG 4321と区別が難しい
    auto b = 432L;  // OK
```

* [演習-危険なconst_cast](exercise_q.md#SS_19_1_10)
* [演習-リテラル](exercise_q.md#SS_19_1_11)

### 3.1.11 型推論 <a id="SS_3_1_11"></a>
#### 3.1.11.1 auto <a id="SS_3_1_11_1"></a>
* [AAAスタイル](term_explanation.md#SS_18_2_8)に従い適切にautoを使用する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 422

    void f(std::vector<std::string> const& strs)
    {
        auto s0 = std::string{"hehe"};  // OK
        auto s1{std::string{"hehe"}};   // OKだが、通常は代入を使用する
        auto s2 = s0;                   // OK
        auto s3 = get_name();           // NG get_name()の戻り値を見ないとs3の型が不明

        for (auto const& str : strs) {  // OK strsの型が明らかであるため、strの型も明らか
            ...
        }
    }
```

* autoを使用する場合、&、\*、const等の付け忘れに注意する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 442

    class A {
    public:
        A() = default;

    #if 0  // NG この関数を呼び出すとクラッシュ
        std::string const& Get(char first_byte) const noexcept
        {
            static std::string const empty;
            for (auto const str : strs) {       // NG &の付け忘れのため、スタック上の
                if (str.at(0) == first_byte) {  //    オブジェクトのリファレンスをreturnする。
                    return str;
                }
            }
            return empty;
        }

    #else  // OK 上のGetの修正。
        std::string const& Get(char first_byte) const noexcept
        {
            static std::string const empty;
            for (auto const& str : strs) {      // OK &を付けて、インスタンスのオブジェクトの
                if (str.at(0) == first_byte) {  //    リファレンスを返せるようになった。
                    return str;
                }
            }
            return empty;
        }
    #endif

    private:
        std::vector<std::string> strs{"aha", "ihi", "uhu"};
    };
```

* autoと= {}を使用した変数の宣言には以下のような紛らわしさがあるため、
  そのような記述を行わない(「[インスタンスの初期化](programming_convention.md#SS_3_1_12)」参照)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 493

    auto a = 1;       // OK aの型はint
    auto b(1);        // 別の規制でNG ()より{}を優先的に使うべき
    auto c{1};        // OK cの型はint
    auto d = {1};     // NG dの型はstd::initializer_list<int>
    auto e = {1, 2};  // NG eの型はstd::initializer_list<int>
    auto f = std::initializer_list<int>{1, 2};  // OK

    static_assert(std::is_same_v<decltype(a), int>, "type not same");
    static_assert(std::is_same_v<decltype(b), int>, "type not same");
    static_assert(std::is_same_v<decltype(c), int>, "type not same");
    static_assert(std::is_same_v<decltype(d), std::initializer_list<int>>, "type not same");
    static_assert(std::is_same_v<decltype(e), std::initializer_list<int>>, "type not same");
    static_assert(std::is_same_v<decltype(f), std::initializer_list<int>>, "type not same");
```

* auto、[decltype](term_explanation.md#SS_18_5_7), decltype(auto)の微妙な違いに気を付ける。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 515

    short  s0{0};
    short& s0_ref{s0};

    {  // autoとdecltypeが同じ動作をするパターン
        auto a = s0;
        static_assert(std::is_same_v<decltype(a), short>);

        decltype(s0) d = s0;
        static_assert(std::is_same_v<decltype(d), short>);

        decltype(auto) da = s0;
        static_assert(std::is_same_v<decltype(da), short>);
    }
    {  // autoとdecltypeに違いが出るパターン
        auto a = s0_ref;
        static_assert(std::is_same_v<decltype(a), short>);

        decltype(s0_ref) d = s0_ref;  // dはリファレンス
        static_assert(std::is_same_v<decltype(d), short&>);

        decltype(auto) da = s0_ref;  // daはリファレンス
        static_assert(std::is_same_v<decltype(da), short&>);
    }

    short s1{0};
    {  // 微妙な違いで出るパターン
        auto a = s0 + s1;
        static_assert(std::is_same_v<decltype(a), int>);

        decltype(s0) d = s0 + s1;  // これが意図的ならよいが
        static_assert(std::is_same_v<decltype(d), short>);

        decltype(s0 + s1) d2 = s0 + s1;  // int&&にはならない
        static_assert(std::is_same_v<decltype(d2), int>);

        decltype(auto) da = s0 + s1;  // この方がクローンがないため上よりも良い
        static_assert(std::is_same_v<decltype(da), int>);
    }
```

* [演習-適切なautoの使い方](exercise_q.md#SS_19_1_12)

### 3.1.12 インスタンスの初期化 <a id="SS_3_1_12"></a>
* 関数内のオブジェクトは、出来る限り[AAAスタイル](term_explanation.md#SS_18_2_8)を用いて宣言し、同時に初期化する。
* [算術型](term_explanation.md#SS_18_1_1)の宣言に[AAAスタイル](term_explanation.md#SS_18_2_8)が使えない場合、
  「代入演算子を伴わない[一様初期化](term_explanation.md#SS_18_2_7)」を使用する。
  「代入演算子を伴う一様初期化」、「()、=による初期化」を使用しない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 572

    int32_t a0(0);            // NG
    int32_t a1 = 0;           // NG
    int32_t a2{0};            // OK 一様初期化
    int32_t a3 = {0};         // NG 代入演算子を伴う一様初期化
    auto    a4 = 0;           // OK AAAの場合は一様初期を使わなくても問題ない
    auto    a5 = int32_t{0};  // OK AAA且つ一様初期
```

* リファレンスやポインタの宣言に[AAAスタイル](term_explanation.md#SS_18_2_8)が使えない場合、
  「代入演算子を伴わない[一様初期化](term_explanation.md#SS_18_2_7)」か「=による初期化」を使用する。
  「代入演算子を伴う一様初期化」、「()による初期化」を使用しない。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 581

    int32_t& r0(a0);     // NG
    int32_t& r1 = a0;    // OK
    int32_t& r2{a0};     // OK 一様初期化
    int32_t& r3 = {a0};  // NG 代入演算子を伴う一様初期化
    auto&    r4 = a0;  // OK AAAの場合は一様初期を使わなくても問題ないが、&の付け忘れに気を付ける

    int32_t* p0(&a0);     // NG
    int32_t* p1 = &a0;    // OK
    int32_t* p2{&a0};     // OK 一様初期化
    int32_t* p3 = {&a0};  // NG 代入演算子を伴う一様初期化
    auto     p4 = &a0;    // OK AAAの場合は一様初期を使わなくても問題ない
    auto*    p5 = &a0;    // OK AAAの場合は一様初期を使わなくても問題ない
```

* 構造体やクラス型オブジェクトの宣言に[AAAスタイル](term_explanation.md#SS_18_2_8)が使えない場合、
    * 「代入演算子を伴わない[一様初期化](term_explanation.md#SS_18_2_7)」を使用する。
    * 上記では意図したコンストラクタが呼び出せない場合にのみ「()による初期化」を使用する。
  ただし、std::string、std::string_viewに関しては「 = "xxx"」を使用しても良い。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 609

    // 構造体の初期化
    struct Struct {
        int32_t     a;
        char const* str;
    };

    Struct s0{1, "1"};           // OK 代入演算子を伴わない一様初期化
    Struct s1 = {2, "2"};        // NG 代入演算子による一様初期化
    Struct s2{};                 // OK s2.aは0、s2.strはnullptrに初期化される。
    Struct s3;                   // NG s3は未初期化
    auto   s4 = Struct{1, "1"};  // OK AAAスタイル
    auto   s5 = Struct{};        // OK AAAスタイル

    // クラスの初期化
    std::unique_ptr<Widget> a{std::make_unique<Widget>()};   // OK
    std::unique_ptr<Widget> b(std::make_unique<Widget>());   // NG {}を使うべき
    auto                    c{std::make_unique<Widget>()};   // OK
    auto                    d = std::make_unique<Widget>();  // OK
    // このような場合、重複を避けるため、変数宣言の型はautoが良い

    // std::string、std::string_viewの初期化
    std::string str0{"222"};     // OK
    std::string str1 = {"222"};  // NG = は不要
    std::string str2("222");     // NG {}で初期化できない時のみ、()を使う。
    std::string str3(3, '2');    // OK {}では初期化できない。str3 == "222"
    std::string str4 = "222";    // OK 例外的に認める
    auto        str5 = std::string{"222"};  // OK AAAスタイル

    std::string_view sv0 = "222";                    // OK 例外的に認める
    auto             sv1 = std::string_view{"222"};  // OK AAAスタイル

    // {}、()による初期化の違い
    std::vector<int32_t> vec0_i{1, 2, 3};  // OK vec0_i.size() == 3 && vec0_i[0] == 1 ...
    std::vector<int32_t> vec1_i{10};       // OK vec1_i.size() == 1 && vec1_i[0] == 10
    std::vector<int32_t> vec2_i(10);       // OK vec1_i.size() == 10
    auto                 vec3_i = std::vector{1, 2, 3};  // OK vec0_iと同じ

    std::vector<std::string> vec1_s{10};  // OK vec1_s.size() == 10
    std::vector<std::string> vec2_s(10);  // NG vec2_s.size() == 10  {}を優先するべき
    auto                     vec3_s = std::vector<std::string>{10};  // OK vec1_sと同じ

    // vec1_i、vec2_i、vec1_sの初期化は似ているが、結果は全く異なる。
    // vec1_iは、vector(initializer_list<>)を呼び出す。
    // vec2_iは、vector(int)を呼び出す。
    // vec1_sは、vector(int)を呼び出す。

    ASSERT_EQ(3, vec0_i.size());
    ASSERT_EQ(1, vec1_i.size());
    ASSERT_EQ(10, vec2_i.size());
    ASSERT_EQ(vec0_i, vec3_i);
    ASSERT_EQ(10, vec1_s.size());  // vec1_iと同じ形式で初期化したが結果は全く異なる。
    ASSERT_EQ(10, vec2_s.size());
    ASSERT_EQ(10, vec3_s.size());
```

* decltypeによるオブジェクトの宣言は、[AAAスタイル](term_explanation.md#SS_18_2_8)と同様に行う。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 677

    auto  a = 0;
    auto& b = a;

    decltype(a)    c = a;    // OKがautoの方が良い
    decltype(a)    d = {a};  // NG
    decltype(b)    e = a;    // OK
    decltype(auto) f = b;    // OK

    static_assert(std::is_same_v<decltype(c), int>);
    static_assert(std::is_same_v<decltype(d), int>);
    static_assert(std::is_same_v<decltype(e), int&>);
    static_assert(std::is_same_v<decltype(f), int&>);
```

* 配列の宣言には、「代入演算子を伴わない[一様初期化](term_explanation.md#SS_18_2_7)」を使用する。
  char[]に関しては、「代入演算子を伴わない一様初期化」か「 = "xxx"」を使用する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 700

    int32_t array0[3]{1, 2, 3};     // OK 代入演算子を伴わない一様初期化
    int32_t array1[3] = {1, 2, 3};  // NG 代入演算子による一様初期化
    int32_t array2[3]{};            // OK 代入演算子を伴わない一様初期化
    int32_t array3[3] = {};         // NG 代入演算子による一様初期化

    char c_str0[]{'1', '2', '\0'};     // OKだが、非推奨
    char c_str1[] = {'1', '2', '\0'};  // NG 代入演算子による一様初期化
    char c_str2[] = {"12"};            // NG 代入演算子による一様初期化
    char c_str3[]{"12"};               // OK
    char c_str4[] = "12";              // OK
```

* 宣言時にポインタ変数の初期値が決まらない場合、nullptrで初期化する(「[リテラル](programming_convention.md#SS_3_1_10)」参照)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 723

    int32_t*       ptr1 = nullptr;  // OK
    int32_t*       ptr2{nullptr};   // OK
    char const*    pchar0 = 0;      // NG
    char*          pchar1 = NULL;   // NG
    int32_t const* ptr0(nullptr);   // NG {}か=で初期化する
```

* 初期化順序が不定になるため、
  別のコンパイル単位で定義された静的なオブジェクトに依存した静的オブジェクトの初期化を行わない
  (同じファイルの上方にある静的なオブジェクトや、
  [Singleton](design_pattern.md#SS_9_12)に依存した初期化を行うことには問題はない)。
* コンパイル時に値が確定する「基本型」や「コンストラクタがconstexprであるクラス」のインスタンスは、
  constexpr(「[const/constexprインスタンス](programming_convention.md#SS_3_1_9)」参照)と宣言する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 735

    constexpr int32_t f_constexpr(int32_t a) noexcept { return a * 3; }
    int32_t           f_normal(int32_t a) noexcept { return a * 3; }
```
```cpp
    // @@@ example/programming_convention/type_ut.cpp 743

    constexpr auto a = f_constexpr(3);  // OK
    auto const     b = f_constexpr(3);  // NG constexprにできる
    // constexpr auto c = f_normal(3);  // NG コンパイルエラー
    auto const d = f_normal(3);  // OK

```

* constなオブジェクトが複雑な初期化を必要とする場合、その初期化にはラムダ式を使用する。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 756

    int32_t len{10};  // ここではlenは固定だが、関数引数等で外部から与えられるとする

    auto vc0 = std::vector<int32_t>(len);  // vc0が初期化以外で変更されないのであれば、NG
    std::iota(vc0.begin(), vc0.end(), 1);  // vc0の初期化

    auto const vc1 = [len]() {  // OK vc1の初期化
        std::vector<int32_t> ret(len);
        std::iota(ret.begin(), ret.end(), 1);
        return ret;
    }();  // ラムダ式の生成と呼び出し
```


* [演習-インスタンスの初期化](exercise_q.md#SS_19_1_15)
* [演習-vector初期化](exercise_q.md#SS_19_1_14)
* [演習-ポインタの初期化](exercise_q.md#SS_19_1_13)


### 3.1.13 rvalue <a id="SS_3_1_13"></a>
* 関数の仮引数以外のリファレンスで[rvalue](term_explanation.md#SS_18_5_3)をバインドしない
  (「[オブジェクトのライフタイム](programming_convention.md#SS_3_2_10)」参照)。
* rvalueの内部ハンドルを使用しない(「[std::string_viewの使用制限](programming_convention.md#SS_3_10_1_4)」参照)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 790

    char const* str = std::string{"str"}.c_str();
    // strが指すポインタはこの行では解放済

    ASSERT_STREQ(str, "str");  //    strは無効なポインタを保持であるため、未定義動作
```

* 非constなリファレンスでrvalueをバインドしない。


## 3.2 クラスとインスタンス <a id="SS_3_2"></a>
### 3.2.1 ファイルの使用方法 <a id="SS_3_2_1"></a>
* 下記の例外を除き、一つのクラスはそれを宣言、定義する1つのヘッダファイルと、
  一つの.cppファイルによって構成する。
    * ファイル外部から使用されないクラスは、一つの.cppファイルの無名名前空間で宣言、定義する。
    * ファイル外部から使用されるインラインクラス(クラステンプレート等)は、
      一つのヘッダファイルで宣言、定義する。
    * 「一つのヘッダファイル(a.h)と、一つの.cpp(a.cpp)で構成されたクラスA」のみをサポートするクラス
      (Aのインターフェースや実装専用に定義されたクラス(「[Pimpl](design_pattern.md#SS_9_3)」参照))は、
      a.h、a.cppで宣言、定義する。

### 3.2.2 クラスの規模 <a id="SS_3_2_2"></a>
#### 3.2.2.1 行数 <a id="SS_3_2_2_1"></a>
* それ以外に方法がない場合を除き、ヘッダファイル内のクラスの定義、
  宣言はコメントを含め200行程度に収める。
* クラス内定義関数が大きくなると下記のような問題が発生しやすくなるため、
  10行を超える関数はクラス内で定義しない。
    * 関数のインポートする外部シンボルが多くなり、
      このクラスを使用する別のクラスに不要な依存関係を作ってしまう
      (「[インターフェース分離の原則(ISP)](solid.md#SS_8_4)」参照)。
    * クラスの定義が間延びして、クラスの全体構造を把握することが困難になる。

#### 3.2.2.2 メンバの数 <a id="SS_3_2_2_2"></a>
* それ以外に方法がない場合を除き、publicメンバ関数の数は、最大7個程度に収める
  (ただし、オーバーロードにより同じ名前を持つ関数群は、全部で1個とカウントする)。
* オブジェクトの状態を保持するメンバ変数の数は、最大4個程度に留める。
  constやconstexprメンバ・インスタンスは定数(状態を保持するメンバ変数ではない)であるため、
  この数に含めない。

#### 3.2.2.3 凝集度 <a id="SS_3_2_2_3"></a>
* 単なるデータホルダー(アプリケーションの設定データを保持するようなクラス等)や、
  ほとんどの振る舞いを他のクラスに委譲するようなクラスを除き、
  [凝集度](term_explanation.md#SS_18_11_1)が高くなるように設計する。

* [演習-凝集度の意味](exercise_q.md#SS_19_2_1)
* [演習-凝集度の向上](exercise_q.md#SS_19_2_2)

### 3.2.3 アクセスレベルと隠蔽化 <a id="SS_3_2_3"></a>
* アクセスレベルは、特別な理由がない限り、上からpublic、protected、privateの順番で明示する。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 12

    class A {
        void f0();  // NG デフォルト private を使用しない。
    public:
        void f1();  // OK
    private:
        void f2();  // OK
    protected:
        void f3();  // NG privateの前に定義すべき。
    };
```

* 全てのメンバ変数はprivateにする。
    * メンバ変数にアクセスしたい場合は、Accessorメンバ関数を経由させる
      (「[Accessor](design_pattern.md#SS_9_4)」参照)。その場合でもsetterは控えめに使用する。
    * 派生クラスから基底クラスの変数の値が必要になる場合は、protectedなAccessorを定義する。
    * 単体テスト用クラスでは、protectedメンバ変数を定義してよい。
* アクセスレベルによるカプセル化が破壊されるため、
  メンバ変数のハンドル(リファレンスやポインタ)を返さない。
  それが避けがたい場合においては、constハンドルを返す。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 28

    class B {
    public:
        ...

        void* f0() noexcept  // NG メンバ変数が保持するポインタを返している
        {
            return v_ptr_;
        }

        std::string* f1() noexcept  // NG メンバ変数へのポインタを返している
        {
            return &str_;
        }

        std::string& f2() noexcept  // NG メンバ変数へのリファレンスを返している
        {
            return str_;
        }

        std::string f3() const noexcept  // OK ただし、パフォーマンスに注意
        {
            return str_;
        }

        std::string const& f4() const noexcept  // OK
        {
            return str_;
        }

    private:
        void*       v_ptr_ = nullptr;
        std::string str_{};
    };
```

* 以下のような場合を除き、friendを使用しない。
    * 単体テスト用クラス
    * 二項演算子をオーバーロードした関数

```cpp
    // @@@ example/programming_convention/class_ut.cpp 68

    class Integer {
    public:
        Integer(int32_t integer) noexcept : integer_{integer} {}

        // メンバ関数に見えるが、非メンバ関数
        friend bool operator==(Integer lhs, Integer rhs) noexcept  // OK
        {
            return lhs.integer_ == rhs.integer_;
        }

    private:
        int32_t const integer_;
    };

    bool operator!=(Integer lhs, Integer rhs) noexcept { return !(lhs == rhs); }
```

* [NVI(non virtual interface)](design_pattern.md#SS_9_8)に従う。従って、
  virtualな関数はprivateかprotectedと宣言し、それをpublicな非仮想メンバ関数から呼び出す。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 86

    class Widget {
    public:
        virtual int32_t DoSomething() noexcept  // NG virtualでpublic
        {
            ...
        }

        int32_t DoSomething(bool b) noexcept  // OK non-virtualでpublic
        {
            return do_something(b);
        }
        ...
    private:
        virtual int32_t do_something(bool b) noexcept  // OK virtualでprivate
        {
            ...
        }
        ...
    };
```

### 3.2.4 継承/派生 <a id="SS_3_2_4"></a>
* 派生は最大2回程度までに留める。やむを得ず階層が深くなる場合、
  コードの静的解析等を使用し派生関係を明確にする(「[クラスのレイアウト](term_explanation.md#SS_18_2_11)」参照)。
* 実装の継承よりも、包含、委譲を優先的に使用する。やむを得ず実装の継承を行う場合は、
  private継承を使用する。 実装の継承をしたクラスがfinalでないならば、protected継承を使用する
  ([CRTP(curiously recurring template pattern)](design_pattern.md#SS_9_21)等は例外的に認められる)。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 124

    // private継承。非推奨
    class StringWrapper0 final : private std::string {
    public:
        explicit StringWrapper0(char const* str) : std::string{str} {}

        void AddStr(char const* str) { *this += str; }

        using std::string::c_str;
    };

    // 移譲。こちらを優先する
    class StringWrapper1 final {
    public:
        explicit StringWrapper1(char const* str) : str_{str} {}

        void AddStr(char const* str) { str_ += str; }

        char const* c_str() const noexcept { return str_.c_str(); }

    private:
        std::string str_;
    };
```

* 派生させないクラスは、finalと宣言する。ほとんどのクラスは派生しないはずなので、
  ほとんどのクラスはfinalになる。
* リソースリークの原因になり得るため、非virtualなデストラクタをもつクラスを継承しない。
  ただし、継承したクラスが基底クラスのメンバ変数以外のメンバ変数を持たないならば、継承しても良い。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 149

    class A {  // デストラクタの呼び出しチェック用のクラス
    public:
        A(bool& destructed) noexcept : destructed_{destructed} { destructed_ = false; }
        ~A() { destructed_ = true; }

    private:
        bool& destructed_;
    };

    class BaseNG {  // NG デストラクタが非virtual
    public:
        BaseNG() = default;
    };

    class DerivedNG : public BaseNG {
    public:
        DerivedNG(bool& destructed) : a_{std::make_unique<A>(destructed)} {}

    private:
        std::unique_ptr<A> a_;
    };
```
```cpp
    // @@@ example/programming_convention/class_ut.cpp 183

    auto a_destructed = false;
    {
        std::unique_ptr<DerivedNG> d{std::make_unique<DerivedNG>(a_destructed)};
        ASSERT_FALSE(a_destructed);
    }
    ASSERT_TRUE(a_destructed);  // OK A::~A()が呼ばれたため問題ないが、、、

    {
        std::unique_ptr<BaseNG> d{std::make_unique<DerivedNG>(a_destructed)};
        ASSERT_FALSE(a_destructed);
    }
    ASSERT_FALSE(a_destructed);  // NG A::~A()が呼ばれないため、メモリリークする
```
```cpp
    // @@@ example/programming_convention/class_ut.cpp 201

    class BaseOK {  // OK デストラクタがvirtual
    public:
        BaseOK()          = default;
        virtual ~BaseOK() = default;
    };

    class DerivedOK : public BaseOK {
    public:
        DerivedOK(bool& destructed) : a_{std::make_unique<A>(destructed)} {}

    private:
        std::unique_ptr<A> a_;
    };
```
```cpp
    // @@@ example/programming_convention/class_ut.cpp 221

    auto a_destructed = false;
    {
        std::unique_ptr<DerivedOK> d{std::make_unique<DerivedOK>(a_destructed)};
        ASSERT_FALSE(a_destructed);
    }
    ASSERT_TRUE(a_destructed);  // OK A::~A()が呼ばれたため問題ない

    {
        std::unique_ptr<BaseOK> d{std::make_unique<DerivedOK>(a_destructed)};
        ASSERT_FALSE(a_destructed);
    }
    ASSERT_TRUE(a_destructed);  // OK A::~A()が呼ばれたため問題ない
```

#### 3.2.4.1 インターフェースの継承 <a id="SS_3_2_4_1"></a>
* クラス間に「Is-a」の関係が成り立つときに限りpublic継承を行う。
    * public継承を行う場合、[リスコフの置換原則(LSP)](solid.md#SS_8_3)を守る。
    * インターフェースを継承しない場合、public継承をしない。
* C#やJavaのinterfaceが必要ならば(インタフェースと実装の完全分離をしたい場合等)、
  pure-virtualなメンバ関数のみを宣言したクラス
  (もしくはそのクラスに[NVI(non virtual interface)](design_pattern.md#SS_9_8)を適用したクラス)
  を定義する。

#### 3.2.4.2 多重継承 <a id="SS_3_2_4_2"></a>
* それが不可避でない限り、多重継承は使用しない。
* 多重継承を使用する場合、複数個の基底クラスのうち、一つを除きメンバ変数を持ってはならない。
* 多重継承を使用する場合、継承階層内に同じ基底クラスが複数回出てきてはならない
  (ダイヤモンド継承をしない)。
* やむを得ずダイヤモンド継承をせざるを得ない場合、
  継承階層内に複数回出現する基底クラスにはvirtual継承を行う。
* virtual継承を行ったクラスのコンストラクタからは、
  virtual基底クラスのコンストラクタを呼び出すようにする
  (こうしないとvirtual基底クラスは初期化されない)。

### 3.2.5 非静的なメンバ変数/定数の初期化 <a id="SS_3_2_5"></a>
* [定義] 非静的なメンバ変数の初期化には下記の3つの方法がある。
    * 初期化方法０: 非静的メンバ変数の初期化子による初期化([NSDMI](term_explanation.md#SS_18_2_6))
    * 初期化方法１: コンストラクタの非静的メンバ初期化子による初期化
    * 初期化方法２: コンストラクタ内での非静的なメンバ変数の初期値の代入

```cpp
    // @@@ example/programming_convention/class_ut.cpp 243

    class A0 {
    public:
        A0() noexcept : b_{0}    // 初期化方法１
        {
            c_ = 0;     // 初期化方法２
        }

    private:
        int32_t a_{0}; // 初期化方法０
        int32_t b_;
        int32_t c_;
    };
```

* [注意] 初期化方法０と、初期化方法１が同一変数に行われた場合、初期化方法０は実行されない。
* すべての非静的なメンバ変数は、コンストラクタ終了時までに明示的に初期化する。
* 多くのコンパイラや静的解析ツールは、
  初期化方法０、１による初期化の漏れについては容易に発見、指摘できるが、
  初期化方法２による初期化の漏れについては、発見が難しい場合がある。
  また、constメンバ変数は、初期化方法２では初期化できないため、
  それ以外に方法がない場合を除き、初期化方法２の使用を避ける。
* 非静的なメンバ変数はクラス内で定義された順序に従い初期化されるため、
  初期化方法１で羅列される初期化の順序を定義順序と同じにする
  (初期化方法１での初期化の順序は、実際の初期化の順序とは関係がない)。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 262

    class A_NG {
    public:
        A_NG(int32_t x, int32_t y) noexcept
            : b_{x + y}, a_{x}, c_{y} // NG メンバ変数定義と初期化の順序が違う
        {
        }

    private:
        int32_t a_;
        int32_t b_;
        int32_t c_;
    };

    class A_OK {
    public:
        A_OK(int32_t x, int32_t y) noexcept : a_{x}, b_{x + y}, c_{x}  // OK
        {
        }

    private:
        int32_t a_;
        int32_t b_;
        int32_t c_;
    };
```

* クラスがただ一つのコンストラクタを持つ場合、初期化方法０と初期化方法１を混在させない。
  従って、初期化方法１を必要とするメンバ変数が一つでもある場合は、
  すべての変数の初期化を初期化方法１で行う。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 291

    class A1 {
    public:
        A1() noexcept {}  // OK 初期化方法０に統一

    private:
        int32_t const a_{1};  // OK 初期化方法０による初期化。
                              //    ただし、static constexprにすべき。
        int32_t b_[2]{0, 1};  // OK 初期化方法０による初期化
        int32_t c_{5};        // OK 初期化方法０による初期化
    };

    class A2 {
    public:
        explicit A2(int a) noexcept   // OK 初期化方法１に統一
            : a_{a}, b_{0, 1}, c_{5}  // OK 初期化方法１による初期化
        {
        }

    private:
        int32_t const a_;
        int32_t       b_[2];
        int32_t       c_;
    };

    class A3 {
    public:
        explicit A3(int a) noexcept : a_{a}  // NG 初期化方法の混在
        {
            c_ = 5;  // NG 初期化方法０、１使用可能にもかかわらず初期化方法２を使用している
        }

    private:
        int32_t const a_;
        int32_t       b_[2]{0, 1};  // NG 初期化方法の混在
        int32_t       c_;
    };
```

* クラスが複数のコンストラクタを持つ場合、すべてのメンバ変数に対して初期化方法０を行い(デフォルト値の設定)、
  デフォルト値とは異なる初期値を持つ変数に対してのみ、コンストラクタ毎に初期化方法１を行う。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 331

    class A4 {
    public:
        A4() noexcept {}  // OK 初期化方法０

        A4(int32_t e) noexcept : e_{e} {}  // OK 初期化方法１によるe_の上書き
        // 注) A4()とA4(int32_t)はデフォルト引数を使用すれば統一できるが、
        // 例の単純化のためにあえてそれぞれを定義している。

    private:
        int32_t d_{5};  // OK 初期化方法０による初期化
        int32_t e_{0};  // OK 初期化方法０による初期化
    };
```

* [演習-メンバ変数の初期化方法の選択](exercise_q.md#SS_19_2_3)
* [演習-メンバの型](exercise_q.md#SS_19_2_4)
* [演習-メンバ変数の初期化](exercise_q.md#SS_19_2_5)

### 3.2.6 静的なメンバ変数/定数の初期化 <a id="SS_3_2_6"></a>
* 静的な(且つconstexprでない)メンバ変数は、ヘッダファイルで宣言し、.cppで定義、初期化する。
* クラス宣言内で初期化される基本型のstatic constメンバ定数を定義しない。
  代わりに、static constexprメンバ定数として定義、初期化する
  (クラス宣言外で初期化されるメンバ定数はstatic constにする)。
* privateなstatic constexprメンバ定数は、
  そのクラスが宣言されているヘッダファイル内で依存されている場合のみ使用する。
* privateなstatic constexprメンバ定数がヘッダファイル内で依存されていない場合は、
  .cppの無名名前空間内で定義、初期化する
  (つまり、クラスのメンバとして定義しない。こうすることで不要なコンパイルが防げる)。

```cpp
    // @@@ example/programming_convention/class.h 5

    class StaticConstexprVar {
    public:
        StaticConstexprVar() = default;

        uint32_t MultiplyBy2(uint32_t a) noexcept;
        uint32_t MultiplyBy3(uint32_t a) noexcept { return static_constexpr_var_3 * a; }
        uint32_t MultiplyBy4(uint32_t a) noexcept;

    private:
        static constexpr uint32_t static_constexpr_var_2{2};  // NG クラス内で定義する必要なし
        static constexpr uint32_t static_constexpr_var_3{3};  // OK クラス内で定義する必要あり
    };
```

```cpp
    // @@@ example/programming_convention/class_ut.cpp 351
    //
    uint32_t StaticConstexprVar::MultiplyBy2(uint32_t a) noexcept { return static_constexpr_var_2 * a; }

    namespace {
    constexpr uint32_t static_constexpr_var_4{4};  // OK クラス内で定義する必要なし
    }

    uint32_t StaticConstexprVar::MultiplyBy4(uint32_t a) noexcept { return static_constexpr_var_4 * a; }
```

### 3.2.7 mutableなメンバ変数 <a id="SS_3_2_7"></a>
* 排他制御用(std::mutex等)や計算データのキャッシュ用等のメンバ変数を除き、
  メンバ変数をmutableと宣言しない。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 365

    class A {
    public:
        A() = default;

        uint32_t GetValue() const  // OK GetValue()をconstにするためにmutex_はmutable
        {
            auto lock = std::lock_guard{mutex_};  // constでない関数std::mutex::lock()の呼び出し

            return v_;
        }

        void AddValue(uint32_t v) noexcept
        {
            auto lock = std::lock_guard{mutex_};

            v_ += v;
        }

    private:
        mutable std::mutex mutex_;  // OK
        uint32_t           v_{0};
    };
```

### 3.2.8 スライシング <a id="SS_3_2_8"></a>
* オブジェクトの[スライシング](term_explanation.md#SS_18_3_3)には以下のいずれかで対処する。
    * [Clone(仮想コンストラクタ)](design_pattern.md#SS_9_7)を使用する。
    * copy代入演算子を= deleteする。

* [スライシング](term_explanation.md#SS_18_3_3)と類似の問題が起こるため、
  オブジェクトの配列をそのオブジェクトの基底クラスへのポインタに代入しない。

* [演習-スライシング](exercise_q.md#SS_19_2_6)

### 3.2.9 オブジェクトの所有権 <a id="SS_3_2_9"></a>
* オブジェクトaの所有権
  (「[オブジェクトの所有権](term_explanation.md#SS_18_2_9)」参照)を持つオブジェクトもしくは関数は、
  オブジェクトaの解放責務を持つ。
* オブジェクトaの所有権を持たないオブジェクトは、
  オブジェクトaのハンドルをメンバ変数で保持することを出来る限り避ける
  ([Observer](design_pattern.md#SS_9_22)パターン等、このルール順守が困難な場合は多い)。
* オブジェクトaがオブジェクトbにnewで生成された(もしくはstd::make_unique()で生成された)とすると、
    * オブジェクトaのポインタはstd::unique_ptr<>(「[RAII(scoped guard)](design_pattern.md#SS_9_9)」参照)で保持する。
    * オブジェクトa(正確にはオブジェクトaを管理するstd::unique_ptr<>オブジェクト)の所有権は、
      オブジェクトbが保持する。
    * オブジェクトbはオブジェクトaの解放責務を持つ(std::unique_ptr<>による自動解放)。
    * オブジェクトaの所有権を保持していないオブジェクトは、オブジェクトaを解放してはならない。
    * オブジェクトaの所有権を別のオブジェクトxへ移動させる場合、
      std::unique_ptr<>とstd::move()を使用する。

* [演習-オブジェクトの所有権](exercise_q.md#SS_19_2_7)

### 3.2.10 オブジェクトのライフタイム <a id="SS_3_2_10"></a>
* [オブジェクトのライフタイム](term_explanation.md#SS_18_2_10)開始前、
  もしくは終了後のオブジェクトにアクセスしない。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 419

    // 初期化前にオブジェクトにアクセスしてしまう例
    B& getB() noexcept;

    // bが初期される前に(ライフタイム開始前)に、a.A::A()が呼び出される。
    // a.A::A()が呼び出される前に、getB()が呼び出される。
    // 従って、bが初期化される前にgetB()が未初期化のbのリファレンスを返してしまう。
    A a{getB()};

    B  b;
    B& getB() noexcept { return b; }
```

* オブジェクトaが所有権を持たないオブジェクトbへのハンドルをa自体のメンバ変数で保持する場合、
  オブジェクトbのライフタイムが終了する前に、
  オブジェクトaがオブジェクトbにアクセスできないようにする(Observerパターンのdetachメンバ関数等)。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 435

    // ライフタイムが終了したオブジェクトにアクセスしてしまう例
    auto a = A{};
    {
        auto b = B{};
        a.SetB(&b);  // NG aのメンバ変数へ&bを代入。
    }                //    この行でbのライフタイム終了。

    a.DoSomething();  // NG bのポインタを使用して何かすると不定動作。
```

* スタック上のオブジェクトのハンドルをその関数外部へ開示しない
  (そのハンドルは、ライフタイムが終了したオブジェクトを指している)。
* thread_localオブジェクトは、ログやデバッグ用途のみで使用する。
* [rvalue](term_explanation.md#SS_18_5_3)はライフタイム終了間際のオブジェクトであるため、
  関数の仮引数以外のリファレンスでrvalueをバインドしない
  (特にリファレンス型のメンバ変数でrvalueをバインドしないことは重要である)。
  rvalueをリファレンス型の引数で受け取る場合はconstリファレンス、
  もしくはrvalueリファレンス(T&&)を使用する(「[rvalue](programming_convention.md#SS_3_1_13)」参照)。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 466

    void f0(E&) noexcept;
    void f1(E const&) noexcept;
    void f2(E&&) noexcept;
```
```cpp
    // @@@ example/programming_convention/class_ut.cpp 475

    // f0(E{});  NG ほとんどのコンパイラではエラー
    f1(E{});  // OK rvalueはconstリファレンスにバインド可
    f2(E{});  // OK rvalueはrvalueリファレンス

    E const& a0 = E{"4"};  // NG rvalueを引数以外のconstリファレンスに代入
    E&&      a1 = E{"5"};  // NG rvalueを引数以外のrvalueリファレンスに代入
```


## 3.3 非メンバ関数/メンバ関数 <a id="SS_3_3"></a>

### 3.3.1 非メンバ関数 <a id="SS_3_3_1"></a>
* 下記のような関数を除き、グローバル名前空間に非メンバ関数を定義しない。
    * C言語から呼び出される関数
    * アセンブラ関数

* .cppファイルから、そのファイルの外部で定義された関数を呼び出す場合、
  その.cppファイル内での局所的な関数宣言をしない
  (関数が宣言、定義されているヘッダファイルをインクルードする)。
* コンパイル時に戻り値が確定する関数はconstexprと宣言する。

* [演習-非メンバ関数の宣言](exercise_q.md#SS_19_3_1)

### 3.3.2 メンバ関数 <a id="SS_3_3_2"></a>
* 可能な場合(メンバに直接アクセスしない場合)、メンバ関数をstaticにする。
* コンパイル時に戻り値が確定するメンバ関数はconstexprと宣言する。
* オブジェクトの状態を変えないメンバ関数は、constと宣言する。
    * getter(下記の例ではGetString)はconstと宣言する。
    * 下記のSetPtrのような関数はconstにしない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 19

    class A {
    public:
        A() : s_ptr_{std::make_unique<std::string>("haha")}, s_inst_{"hihi"} {}

        std::string const& GetString() const noexcept  // OK 必ずconst
        {
            return s_inst_;
        }

        // SetPtrと、SetInstは実質的には同じことを行っている。
        // SetInstはconstと宣言できない(コンパイルエラー)。
        // 従ってSetPtrもconstと宣言してはならない。
        // なお、この問題はstd::experimental::propagate_constを使用することで解決できるが、
        // 名前空間からわかるように、このライブラリが将来にわたって有効かどうかは不明である。
        void SetPtr(std::string_view name) const  // NG このconstはつけてはならない。
        {
            *s_ptr_ = name;
        }

        void SetInst(std::string_view name)  // OK
        {
            s_inst_ = name;
        }

    private:
        std::unique_ptr<std::string> s_ptr_;
        std::string                  s_inst_;
    };

    void f()
    {
        A const a;

        a.SetPtr("0");  // constオブジェクトaを変更できてしまう。
    //  a.SetInst("1"); // constオブジェクトaを変更しようとしたため、
                        // 正しく(constの目的通り)コンパイルエラー。
    }
```

* クラス内部のハンドル（ポインタやリファレンス）を戻り値に使用しない。
    * それが避けがたい場合は、戻り値のハンドルをconstにする。
    * ハンドルがconstにできない場合(関数が非constなハンドルを返す場合)、
      そのハンドル経由でクラスの状態を変更できるため、その関数をconstにしない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 62

    class B {
    public:
        B() noexcept {}

        // GetStringsは、避けがたい理由で、strings_のリファレンスを返さざるを得ないとする。
        // この場合、GetStringsはconstにしてはならない。
        std::vector<std::string>& GetStrings() noexcept { return strings_; }

    private:
        std::vector<std::string> strings_{};
    };
```

* 非静的メンバのハンドルを返すメンバ関数を持つオブジェクトが
  [rvalue](term_explanation.md#SS_18_5_3)である場合、
  そのオブジェクトからその関数を呼び出した戻り値(メンバへのハンドル)を変数で保持しない
  (そのハンドルは無効なオブジェクトを指している)。
  そういった使用方法が必要ならばlvalue修飾、[rvalue修飾](term_explanation.md#SS_18_5_4)を用いたオーバーロード関数を定義する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 82

    char const* s = std::string{"hehe"}.c_str();  // std::string{"hehe"}はrvalue

    std::cout << s << std::endl;  // この時点ではsは解放されている。
```

* [演習-メンバ関数の修飾](exercise_q.md#SS_19_3_2)

#### 3.3.2.1 特殊メンバ関数 <a id="SS_3_3_2_1"></a>
* [特殊メンバ関数](term_explanation.md#SS_18_2_1)
    * デフォルトコンストラクタ
    * copyコンストラクタ
    * copy代入演算子(operator =)
    * moveコンストラクタ
    * move代入演算子
    * デストラクタ

  について、デフォルトコンストラクタ以外を定義する場合、
  その他の関数には以下のいずれかを選択する(不要な代入演算子を= deleteすることは特に重要である)。

|コンパイラ生成関数を |定義方法                      |
|:-------------------:|------------------------------|
|使用する             | = default                    |
|使用しない           | = delete、もしくは自分で実装 |

* クラスを宣言、定義する場合、下記のClassStationery(クラスのひな形)を参考にし、
  不要なコンパイラ生成関数が作られないようにする。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 489

    /// @class ClassStationery
    /// @brief クラスのひな形。クラスを定義、宣言するときには、このクラスの下記6関数を適切に
    ///        定義、宣言すること。
    class ClassStationery final {
    public:
        ClassStationery()  = delete;
        ~ClassStationery() = delete;

        ClassStationery(ClassStationery const&)                = delete;
        ClassStationery& operator=(ClassStationery const&)     = delete;
        ClassStationery(ClassStationery&&) noexcept            = delete;
        ClassStationery& operator=(ClassStationery&&) noexcept = delete;
    };
```

* リソース管理等の都合からコンパイラが生成するデストラクタでは機能が不十分な場合、
  プログラマがそのクラスのデストラクタを定義する。
  この場合、コンパイラが生成するcopyコンストラクタ、copy代入演算子、moveコンストラクタ、
  move代入演算子では機能が不十分であることが予測されるため、
  これらを使用しない(「[Copy-And-Swap](design_pattern.md#SS_9_5)」参照)。

* [演習-特殊メンバ関数の削除](exercise_q.md#SS_19_3_3)

#### 3.3.2.2 コンストラクタ <a id="SS_3_3_2_2"></a>
* クラスが複数の初期化方法を提供する場合でも、
  デフォルト引数を使用し、できる限りコンストラクタを一つに集約する。
* 一つのコンストラクタに集約できない場合、[委譲コンストラクタ](term_explanation.md#SS_18_2_4)等により処理の重複を防ぐ。
  [非静的なメンバ変数/定数の初期化](programming_convention.md#SS_3_2_5)処理の重複を避けることは特に重要である。
* オブジェクトの初期化が完了するまでは派生クラスの仮想関数呼び出し等の
  [RTTI](programming_convention.md#SS_3_5_9)機能を使うことはできないため(「[クラスのレイアウト](term_explanation.md#SS_18_2_11)」参照)、
  コンストラクタの中でRTTI機能を使わない(デストラクタでも同様)。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 95

    class Base {
    public:
        Base(std::ostream& os) : os_{os} { os_ << __func__ << "-" << Name() << " -> "; }

        virtual ~Base() { os_ << __func__ << "-" << Name(); }

        virtual std::string_view Name() const { return "Base"; }

    protected:
        std::ostream& os_;  // protectedなメンバ変数を定義すべきではないが、コードの動作例示のため
    };

    class Derived : public Base {
    public:
        Derived(std::ostream& os) : Base{os} { os_ << __func__ << "-" << Name() << " -> "; }

        virtual ~Derived() { os_ << __func__ << "-" << Name() << " -> "; }

        virtual std::string_view Name() const override { return "Derived"; }
    };
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 122

    auto oss = std::ostringstream{};

    {
        auto d = Derived{oss};
    }

    ASSERT_EQ("Base-Base -> Derived-Derived -> ~Derived-Derived -> ~Base-Base", oss.str());
    // つまり、
    //          Base::Base()とBase::~Base()からは、Base::Name()が
    //          Derived::Derived()とDerived::~Derived()からは、Derived::Name()
    // が呼び出される。
```

* クラスが解放責務を持つポインタ型メンバ変数を持つならば、copyコンストラクタ、
  copy代入演算子に対して以下のいずれかを行い、[シャローコピー](term_explanation.md#SS_18_3_1)が行われないようにする
  (このルールはファイルディスクリプタ等のリソース管理をするクラス全般に当てはまる)。
    * [ディープコピー](term_explanation.md#SS_18_3_2)をさせる。
    * = deleteする(「[特殊メンバ関数](programming_convention.md#SS_3_3_2_1)」参照)。

  またこの場合、moveコンストラクタ、move代入演算子の定義を検討する(「[Copy-And-Swap](design_pattern.md#SS_9_5)」参照)。

* [非explitなコンストラクタによる暗黙の型変換](term_explanation.md#SS_18_2_5)
  が不要なクラスのコンストラクタに関しては、下記の目的のためにexplicitと宣言する。

    * 仮引数一つのコンストラクタに関しては、暗黙の型変換が行われないようにする。
    * 仮引数二つ以上のコンストラクタに関しては、
      代入演算子での[一様初期化](term_explanation.md#SS_18_2_7)ができないようにする。  

```cpp
    // @@@ example/programming_convention/func_ut.cpp 144

    class A0 {
    public:
        // NG int32_tからA0への暗黙の型変換が起こる。
        A0(int32_t a) noexcept : a_{a} {}
        ...
    };

    class A1 {
    public:
        // OK int32_tからA1への暗黙の型変換をさせない。
        explicit A1(int32_t a) noexcept : a_{a} {}
        ...
    };

    class A2 {
    public:
        // NG 代入演算子でのリスト初期化ができてしまう。
        A2(int32_t a, int32_t* b) noexcept : a_{a}, b_{b} {}
        ...
    };

    class A3 {
    public:
        // OK 代入演算子でのリスト初期化をさせない。
        explicit A3(int32_t a, int32_t* b) noexcept : a_{a}, b_{b} {}
        ...
    };

    void f_A0(A0) noexcept {}
    void f_A1(A1) noexcept {}
    void f_A2(A2) noexcept {}
    void f_A3(A3) noexcept {}
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 198

        A0 a0 = 1;           // NG 1からA0への暗黙の型変換。
                             //    このような変換はセマンティクス的不整合につながる場合がある。
    //  A1 a1 = 1;           // OK explicitの効果で、意図通りコンパイルエラー。

        f_A0(1);             // NG 1からA0への暗黙の型変換のためf_A0が呼び出せてしまう。
    #if 0
        f_A1(1);             // OK explicitの効果で、意図通り以下のようなコンパイルエラー。
                             //    error: could not convert ‘1’ from ‘int’ to ‘A1’
    #else
        f_A1(A1{1});         // OK f_A1の呼び出し
    #endif

        auto i = 3;
        A2  a2 = {i, &i};    // NG 代入演算子でのリスト初期化をしている。

    //  A3 a3 = { i, &i };   // OK explicitの効果で、意図通りコンパイルエラー。
        A3 a3{i, &i};        // OK リスト初期化
        auto a4 = A3{i, &i}; // OK AAA

        f_A2({i, &i});       // NG { i, &i }からA2への暗黙の型変換のためf_A2が呼び出せてしまう。
    #if 0
        f_A3({i, &i});       // OK explicitの効果で、意図通り以下のようなコンパイルエラー。
                             //    error: converting to A3 from initializer list would use explicit 
                             //           constructor A3::A3(int32_t, int32_t*)’
    #else
        f_A3(A3{i, &i});     // OK f_A3の呼び出し
    #endif
```

* 派生クラスが基底クラスの全コンストラクタを必要とする場合、
  [継承コンストラクタ](term_explanation.md#SS_18_2_3)を使用する。

* デフォルト引数はインターフェース関数の呼び出しを簡略化する目的で使用するべきであるため、
  private関数にデフォルト引数を持たさない。

* [演習-委譲コンストラクタ](exercise_q.md#SS_19_3_4)

#### 3.3.2.3 copyコンストラクタ、copy代入演算子 <a id="SS_3_3_2_3"></a>
* copyコンストラクタ、copy代入演算子は[copyセマンティクス](term_explanation.md#SS_18_8_2)に従わせる。
* copyコンストラクタ、copy代入演算子の引数はconstリファレンスにする。
* [RVO(Return Value Optimization)](term_explanation.md#SS_18_10_12)により、
  copyコンストラクタの呼び出しは省略されることがあるため、
  copyコンストラクタ、copy代入演算子はコピー以外のことをしない。
* copy代入演算子は[lvalue修飾](term_explanation.md#SS_18_5_5)をする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 239

    class Widget {
    public:
        Widget& operator=(Widget const& rhs)  // NG lvalue修飾無し
        {
            // 何らかの処理
            return *this;
        }

        Widget& operator=(Widget&& rhs) noexcept  // NG lvalue修飾無し
        {
            // 何らかの処理
            return *this;
        }
        ...
    };
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 268

    Widget w0{1};
    Widget w1{2};

    w0 = w1;         // これには問題ない
    w1 = Widget{3};  // これにも問題ない

    Widget{2} = w0;  // NG lvalue修飾無しのcopy代入演算子であるため、コンパイルできる
    Widget{3} = Widget{4};  // NG lvalue修飾無しのmove代入演算子であるため、コンパイルできる
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 287

    class Widget {  // 上記の修正
    public:
        Widget& operator=(Widget const& rhs) &  // OK lvalue修飾
        {
            // 何らかの処理
            return *this;
        }

        Widget& operator=(Widget&& rhs) & noexcept  // OK lvalue修飾
        {
            // 何らかの処理
            return *this;
        }
        ...
    };
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 316

    Widget w0{1};
    Widget w1{2};

    // Widget{2} = w0;          lvalue修飾の効果でコンパイルエラー
    // Widget{3} = Widget{4};   lvalue修飾の効果でコンパイルエラー
```

* [演習-copyコンストラクタ](exercise_q.md#SS_19_3_5)

#### 3.3.2.4 moveコンストラクタ、move代入演算子 <a id="SS_3_3_2_4"></a>
* moveコンストラクタ、move代入演算子は[moveセマンティクス](term_explanation.md#SS_18_8_3)に従わせ、
  エクセプションをthrowさせない(「[エクセプション処理](programming_convention.md#SS_3_3_3_10)」参照)。
* [注意] noexceptでないmoveコンストラクタ、
  move代入演算子を持つクラスをSTLコンテナのtemplate引数として使用した場合、
  moveコンストラクタ、move代入演算子の代わりに、 
  copyコンストラクタ、copy代入演算子が使用され、パフォーマンス問題を引き起こす場合がある。
* move代入演算子はlvalue修飾(「[copyコンストラクタ、copy代入演算子](programming_convention.md#SS_3_3_2_3)」参照)をする。

* [演習-moveコンストラクタ](exercise_q.md#SS_19_3_6)  

#### 3.3.2.5 初期化子リストコンストラクタ <a id="SS_3_3_2_5"></a>
* [初期化子リストコンストラクタ](term_explanation.md#SS_18_2_2)は、コンテナクラスの初期化のためのみに定義する。
* 初期化子リストコンストラクタと同じ仮引数を取り得るコンストラクタを定義しない。

#### 3.3.2.6 デストラクタ <a id="SS_3_3_2_6"></a>
* デストラクタの中でRTTI機能を使わない(「[コンストラクタ](programming_convention.md#SS_3_3_2_2)」参照)。
* デストラクタはnoexceptであり、throwするとプログラムが終了するため、デストラクタでthrowしない。

#### 3.3.2.7 オーバーライド <a id="SS_3_3_2_7"></a>
* [オーバーライドとオーバーロードの違い](term_explanation.md#SS_18_10_1)に注意する。
* オーバーライドしたメンバ関数には、オーバーライドされたメンバ関数の機能の意味を踏襲させる。
* オーバーライドする/される一連の仮想関数(デストラクタを含む)について、
    * 全ての宣言にはvirtualを付ける。
    * 一連の仮想関数の最初でも最後でもないものの宣言には、overrideを付ける。
    * 一連の仮想関数の最後のものの宣言には、overrideを付けず、finalを付ける。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 334

    class Base {
    public:
        virtual ~Base();                   // OK
        virtual void f(int32_t) noexcept;  // OK
        virtual void g() noexcept;         // OK
    };

    // Derived_0::fは、Base::fのオーバーライドのつもりであったが、タイポのため新たな関数の宣言、
    // 定義になってしまった。この手のミスは、自分で気づくのは難しい
    class Derived_0 : public Base {
    public:
        virtual ~Derived_0();               // NG overrideが必要
        virtual void f(uint32_t) noexcept;  // NG Derived_0:fはBase:fのオーバーライドではない
        virtual void g() noexcept override;  // OK
    };

    class Derived_1 : public Base {
    public:
        // NG 下記が必要
        // virtual ~Derived_1() override;
        virtual void f(uint32_t) override;  // OK overrideと書いたことで、
                                            //    コンパイルできないため、タイポに気づく
    };

    class Derived_2 : public Base {
    public:
        virtual ~Derived_2() override;                    // OK Derived_2はfinalではない
        virtual void f(int32_t) noexcept override final;  // NG overrideは不要
        virtual void g() noexcept final;  // OK これ以上オーバーライドしない
    };
```

* オーバーライド元の関数とそのオーバーライド関数のデフォルト引数の値は一致させる。
  オーバーライド元の関数にデフォルト引数を持たせないのであれば、
  そのオーバーライド関数にもデフォルト引数を持たせない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 373

    class Base {
    public:
        virtual int32_t GetArg(int32_t a = 0) const noexcept { return a; }
        ...
    };

    class Derived : public Base {
    public:
        // NG Base::GetArgのデフォルト引数と違う
        virtual int32_t GetArg(int32_t a = 1) const noexcept override { return a; }

        ...
    };
```

```cpp
    // @@@ example/programming_convention/func_ut.cpp 397

    auto  d = Derived{};
    Base& b{d};

    // 同じオブジェクトであるにもかかわらず、その表層型でデフォルト引数の値が変わってしまう。
    ASSERT_EQ(0, b.GetArg());
    ASSERT_EQ(1, d.GetArg());
```

* privateやprotectedなオーバーライド関数にはデフォルト引数を持たさない
  (「[実引数/仮引数](programming_convention.md#SS_3_3_3_5)」参照)。
  さらに[NVI(non virtual interface)](design_pattern.md#SS_9_8)にも従うことにより、
  上の条項の示した一連のオーバーライド関数のデフォルト引数の一致について考慮の必要がなくなり、
  且つこのクラスのユーザはデフォルト引数が使用できるようになる。

* [演習-オーバーライド関数の修飾](exercise_q.md#SS_19_3_8)  

### 3.3.3 非メンバ関数/メンバ関数共通 <a id="SS_3_3_3"></a>

#### 3.3.3.1 サイクロマティック複雑度 <a id="SS_3_3_3_1"></a>
* [サイクロマティック複雑度](term_explanation.md#SS_18_11_2)は15以下が好ましい。
* 特別な理由がない限り、サイクロマティック複雑度は20以下にする。

#### 3.3.3.2 行数 <a id="SS_3_3_3_2"></a>
* 10行程度が好ましい。
* 特別な理由がない限り、30行以下で記述する。
* [注意] C++の創始者であるビャーネ・ストラウストラップ氏は、
  [プログラミング言語C++ 第4版](https://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9EC-%E7%AC%AC4%E7%89%88-%E3%83%93%E3%83%A3%E3%83%BC%E3%83%8D%E3%83%BB%E3%82%B9%E3%83%88%E3%83%A9%E3%82%A6%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97-ebook/dp/B01BGEO9MS)
  の中で、下記のように述べている。

```
    約 40 行を関数の上限にすればよい。 
    私自身は、もっと小さい平均 7 行程度を理想としている。 
```

* [演習-関数分割](exercise_q.md#SS_19_3_7)  

#### 3.3.3.3 オーバーロード <a id="SS_3_3_3_3"></a>
* [オーバーライドとオーバーロードの違い](term_explanation.md#SS_18_10_1)に注意する。
* オーバーロードされた関数は実行目的を同じにする。
  異なる目的のためには異なる名前の関数を用意する。
* [オーバーライド](programming_convention.md#SS_3_3_2_7)を除き、基底クラスのメンバ関数と同じ名前を持つメンバ関数を派生クラスで宣言、
  定義しない。
  これに反すると[name-hiding](term_explanation.md#SS_18_4_8)のため、基底クラスのメンバ関数の可視範囲を縮小させてしまう。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 411

    // NGな例
    class Base {
    public:
        virtual ~Base() = default;
        void f() noexcept
        {
            ...
        }
    };

    class DerivedNG : public Base {
    public:
        void f(int32_t a) noexcept  // NG DerivedNG::f(int32_t)がBase::fを隠す(可視範囲の縮小)
        {
            ...
        }
    };

    void f() noexcept
    {
        auto d = DerivedNG{};

        d.f(0);
    #if 0
        d.f(); // NG DerivedNG::f(int32_t)がBase::fを隠す(可視範囲の縮小)ためコンパイルエラー
    #endif
    }

    // DerivedNGの修正
    class DerivedOK : public Base {
    public:
        void f(int32_t a) noexcept
        {
            ...
        }
        using Base::f;  // OK Base::fをDerivedOKに導入。
    };

    void g() noexcept
    {
        auto d = DerivedOK{};

        d.f(0);
        d.f();  // OK usingにより、Base::fが見える
    }
```

* 仮引数の型が互いに暗黙に変換できるオーバーロード関数の定義、使用には気を付ける。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 468

    int32_t f(int32_t) { return 0; }
    int32_t f(int16_t) { return 1; }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 476

    auto i16 = int16_t{1};

    ASSERT_EQ(1, f(i16));        // f(int16_t)が呼ばれる
    ASSERT_EQ(0, f(i16 + i16));  // f(int32_t)が呼ばれる
```

* 暗黙の型変換による関数の使用範囲の拡張を防ぐには、オーバーロード関数を= deleteする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 488

    // 実引数がdoubleを認めないパターン
    int32_t f0(double) = delete;
    int32_t f0(int32_t a) noexcept { return a / 2; }

    // 実引数がint32_t以外を認めないパターン
    template <typename T>
    int32_t f1(T) = delete;
    int32_t f1(int32_t a) noexcept { return a / 2; }

    // 実引数がunsigned以外を認めないパターン
    template <typename T, std::enable_if_t<!std::is_unsigned_v<T>>* = nullptr>
    uint64_t f2(T) = delete;

    template <typename T, std::enable_if_t<std::is_unsigned_v<T>>* = nullptr>
    uint64_t f2(T t) noexcept
    {
        uint64_t f2_impl(uint64_t) noexcept;

        // Tがsignedで、tが-1のような値の場合、f2_impl(uint64_t)の呼び出しによる算術変換により、
        // tは巨大な値に変換されるが、
        // Tがunsignedならば、f2_impl(uint64_t)の呼び出しによる算術変換は安全

        return f2_impl(t);
    }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 518

    char     c{'c'};
    int8_t   i8{1};
    int32_t  i32{1};
    uint32_t ui32{1};
    uint64_t ui64{1};
    double   d{1.0};

    f0(c);
    f0(i8);
    f0(i32);
    // f0(d);    呼び出そうとしたf0(double)はdeleteされているので意図通りエラー

    f1(i32);
    // f1(u32);  呼び出そうとしたf1<uint32_t>(uint32_t)はdeleteされているので意図通りエラー

    f2(ui32);
    f2(ui64);
    // f2(c);    呼び出そうとしたf2<char>(char)はdeleteされているので意図通りエラー
    // f2(i32);  呼び出そうとしたf2<int32_t>(int32_t)はdeleteされているので意図通りエラー
```

* [演習-オーバーライド/オーバーロード](exercise_q.md#SS_19_3_9)  
* [演習-オーバーロードによる誤用防止](exercise_q.md#SS_19_3_10)  

#### 3.3.3.4 演算子オーバーロード <a id="SS_3_3_3_4"></a>
* 演算子をオーバーロードする場合、
    * 単項演算子はメンバ関数で定義する。
    * 二項演算子は非メンバ関数で定義する。
* &&, ||, カンマ(,)をオーバーロードしない。
* 型変換オペレータの宣言、定義を多用しない。
* boolへの型変換オペレータは、explicit付きで定義する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 547

    class A0 {
    public:
        operator bool() const noexcept  // NG intへの型変換が可能
        {
            return state_;
        }

    private:
        bool state_{true};
    };

    class A1 {
    public:
        explicit operator bool() const noexcept  // OK explicitすることで誤使用を避ける。
        {
            return state_;
        }

    private:
        bool state_{true};
    };

    void f()
    {
        auto a0 = A0{};
        auto a1 = A1{};

        std::cout << a0 + 1;  // NG コンパイルできてしまう。
    #if 0
        std::cout << a1 + 1;  // OK 意図通りコンパイルエラー
    #endif

        ...
    }
```

* 演算子をオーバーロードする場合、それが自然に使えるようにする。
    * operator == を定義するならば、operator != も定義する（<, >等のその他の例も同様）。
    * operator+ を定義するならば、operator += も定義する(+以外も同様)。
    * copy(またはmove)代入演算子を定義する場合、copy(またはmove)コンストラクタも定義する
      (その際、コードクローンを作りがちなので注意する(「[Copy-And-Swap](design_pattern.md#SS_9_5)」参照))。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 586

    class Integer {
    public:
        Integer(int32_t integer) noexcept
            : integer_{integer} {}  // int32_tの暗黙の型変換が必要なのでexplicitしない

        // copyコンストラクタ、copy代入演算子の定義
        Integer(Integer const&)            = default;
        Integer& operator=(Integer const&) = default;

        friend bool operator==(Integer lhs, Integer rhs) noexcept
        {
            return lhs.integer_ == rhs.integer_;
        }

        Integer& operator+=(Integer rhs) noexcept
        {
            integer_ += rhs.integer_;
            return *this;
        }

    private:
        int32_t integer_;
    };

    inline bool operator!=(Integer lhs, Integer rhs) noexcept
    {
        return !(lhs == rhs);  // operator==の活用
    }

    inline Integer operator+(Integer lhs, Integer rhs) noexcept
    {
        lhs += rhs;  // operator+=の活用
        return lhs;
    }

```

* [ユーザ定義リテラル演算子](term_explanation.md#SS_18_1_16)のサフィックスには、
  アンダーバーから始まる3文字以上の文字列を使用する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 628

    constexpr int32_t one_km{1000};

    // ユーザ定義リテラル演算子の定義
    constexpr int32_t operator""_kilo_meter(unsigned long long num_by_mk)  // OK
    {
        return num_by_mk * one_km;
    }

    constexpr int32_t operator"" km(unsigned long long num_by_mk)  // NG STDでリザーブ
    {
        return num_by_mk * one_km;
    }

    constexpr int32_t operator""_meter(unsigned long long num_by_m)  // OK
    {
        return num_by_m;
    }

    constexpr int32_t operator""_m(unsigned long long num_by_m)  // NG 短すぎる
    {
        return num_by_m;
    }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 656

    auto km = int32_t{3_kilo_meter};  // ユーザ定義リテラル演算子の利用
    auto m  = int32_t{3000_meter};    // ユーザ定義リテラル演算子の利用

    ASSERT_EQ(m, km);
```

#### 3.3.3.5 実引数/仮引数 <a id="SS_3_3_3_5"></a>
* 仮引数(「[実引数/仮引数](term_explanation.md#SS_18_10_2)」参照)の数は、4個程度を上限とする。
* 仮引数を関数の戻り値として利用しない場合
  (且つ仮引数が関数テンプレートの[ユニバーサルリファレンス](term_explanation.md#SS_18_6_1)でない場合)、
    * 基本型やその型のエイリアス、enumは値渡しにする。
    * それ以外のオブジェクトはconstリファレンス渡しにする
      (「[const/constexprインスタンス](programming_convention.md#SS_3_1_9)」参照)。
      ただし、数バイトの小さいオブジェクトは値渡ししても良い。
    * 「引数がnullptrである場合の処理をその関数が行う」場合、constポインタ渡しにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 674

    void f(int32_t a, enum EnumArg b, NotSmall const& c, Small d, NotSmall const* e) noexcept
    {
        // a : 基本型
        // b : enum
        // c : サイズが小さくないオブジェクトで、nullptrでないことが前提
        // d : サイズ小さいオブジェクト
        // e : サイズが小さくないオブジェクトを指すが、nullptrである場合も処理の対象

        if (e == nullptr) {
            ...
        }
        else {
            ...
        }

        ...
    }
```

* [注意] 仮引数をconstリファレンス渡しやconstポインタ渡しにすることで、
    * 値渡しに比べて、ランタイムでの処理が速くなる。
    * リファレンスやポインタ経由で引数に使用されたオブジェクトが変更されるのを防ぐ
      (値渡しであれば引数に使用されたオブジェクトが変更されることはない)。

* 仮引数を関数の戻り値として利用する場合、
    * 「関数が、仮引数がnullptrである場合の処理を行う」場合、ポインタ渡しにする。
    * 「関数が、仮引数がnullptrでないことを前提している」場合、リファレンス渡しにする。

* [ユニバーサルリファレンス](term_explanation.md#SS_18_6_1)を仮引数とする関数テンプレートでは、
  仮引数を関数の戻り値として利用しない場合でも、仮引数は非constにする
  (ユニバーサルリファレンスはrvalueにもバインドできるためconstにすることはできない)。

* 継承の都合等で、使用しないにもかかわらず定義しなければならない仮引数には名前を付けない。
* 関数f()の仮引数が2つ以上であり、f()に渡す引数をそれぞれに生成する関数があった場合、
  引数を生成する関数の戻り値を直接f()に渡さない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 698

    class A {
    public:
        int32_t f0() noexcept { return a_++; }

        int32_t f1() noexcept { return a_--; }
        ...
    };

    void f(int32_t a0, int32_t a1) noexcept
    {
        ...
    }

    void g(A& a) noexcept
    {
        f(a.f0(), a.f1());  // NG f0()、f1()が呼ばれる順番は未定義。

        auto a0 = a.f0();
        auto a1 = a.f1();
        f(a0, a1);          // OK f0()はf1()よりも先に呼ばれる。
    }
```

* copyコンストラクタ、copy代入演算子、moveコンストラクタ、
  move代入演算子の仮引数名はrhs(「[略語リスト](naming_practice.md#SS_6_1_1)」参照)にする。
* 二項演算子の仮引数名は、左側をlhs、右側をrhsにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 731

    class B {
    public:
        B(A const& rhs);
        B& operator=(A const& rhs);

    private:
        int32_t b_{0};

        friend bool operator==(B const& lhs, B const& rhs) noexcept { return lhs.b_ == rhs.b_; }
    };
```

* 仮引数の意味を明示するために、関数宣言の仮引数の名前は省略しない。
* 仮引数がない関数の()の中には何も書かない。
  Cからリンクされる場合に限り、関数の()の中にはvoidと書く。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 747

    class C {
    public:
        void SetValue(int32_t number_of_peaple);  // OK
    //  void SetValue(int32_t);                   // NG 仮引数名を書く
        void SetValue(D const& d);                // OK
    //  void SetValue(D const&);                  // NG 仮引数名を書く
    //  int32_t GetValue(void) const;             // NG void不要
        int32_t GetValue() const;                 // OK
    };

    extern "C" int32_t XxxGetValue(void);  // OK Cからリンクされる
```

* 実引数として使用される配列がポインタ型へ暗黙に変換されることを前提に、
  仮引数をポインタ型にしない。また、仮引数を一見、配列に見えるポインタ型にしない
  (「[スライシング](term_explanation.md#SS_18_3_3)」で述べたように、
  特に基底クラスを配列にすることは危険である)。
  代わりに配列へのリファレンスを使用する。 

```cpp
    // @@@ example/programming_convention/func_ut.cpp 770

    class Base {
    public:
        Base(char const* name) noexcept : name0_{name} {}
        char const* Name0() const noexcept { return name0_; }

        ...
    private:
        char const* name0_;
    };

    class Derived final : public Base {
    public:
        Derived(char const* name0, char const* name1) noexcept : Base{name0}, name1_{name1} {}
        char const* Name1() const noexcept { return name1_; }

        ...
    private:
        char const* name1_;
    };

    std::vector<std::string> f(Base const* array, uint32_t n)  // NG 誤用しやすいシグネチャ
    {
        auto ret = std::vector<std::string>{n};

        std::transform(array, array + n, ret.begin(), [](Base const& b) noexcept { return b.Name0(); });

        return ret;
    }

    std::vector<std::string> g(Base const array[10], uint32_t n)  // NG 誤用しやすいシグネチャ
    {
        // str_arrayは一見、配列に見えるが、実際はポインタであるため、
        // この関数のシグネチャはf(Base const* str_array, uint32_t n)と同じ。
        // 配列の長さに見える10はシンタックス上の意味を持たない。
        auto ret = std::vector<std::string>{n};

        std::transform(array, array + n, ret.begin(), [](Base const& b) noexcept { return b.Name0(); });

        return ret;
    }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 821

    TEST(ProgrammingConvention, use_convert_to_ptr)
    {
        Base    b[]{"0", "0"};
        Derived d[]{{"0", "1"}, {"2", "3"}};

        ASSERT_EQ((std::vector<std::string>{"0", "0"}), f(b, array_length(b)));  // OK これは良いが
        ASSERT_EQ((std::vector<std::string>{"0", "0"}), g(b, array_length(b)));  // OK これは良いが

    #if 0  // 本来なら、下記のようになるべきだが、
        ASSERT_EQ((std::vector<std::string>{"0", "2"}), f(d, array_length(d)));  // NG
        ASSERT_EQ((std::vector<std::string>{"0", "2"}), g(d, array_length(d)));  // NG
    #else  // レイアウトずれにより、下記のようになる
        ASSERT_EQ((std::vector<std::string>{"0", "1"}), f(d, array_length(d)));  // NG
        ASSERT_EQ((std::vector<std::string>{"0", "1"}), g(d, array_length(d)));  // NG
    #endif
    }
```

```cpp
    // @@@ example/programming_convention/func_ut.cpp 842

    // ポインタではなく、配列へのリファレンスを使用することで、
    // 上記のようなバグを避けることができる

    std::vector<std::string> f_ref_2(Base const (&array)[2])  // OK
    {
        auto ret = std::vector<std::string>{array_length(array)};

        // arrayの型はポインタではなく、リファレンスなのでstd::endが使える
        std::transform(array, std::end(array), ret.begin(),
                       [](Base const& b) noexcept { return b.Name0(); });

        return ret;
    }

    template <uint32_t N>
    std::vector<std::string> f_ref_n(Base const (&array)[N])  // OK
    {
        auto ret = std::vector<std::string>{N};

        std::transform(array, std::end(array), ret.begin(), [](auto& b) noexcept { return b.Name0(); });

        return ret;
    }

    template <typename T, uint32_t N>
    std::vector<std::string> g_ref(T const (&array)[N])  // OK
    {
        auto ret = std::vector<std::string>{N};

        std::transform(array, std::end(array), ret.begin(), [](auto& b) noexcept { return b.Name0(); });

        return ret;
    }

    // NULLを渡す必要がある場合、配列へのリファレンスの代わりに、
    // 配列へのポインタを使うことができる

    template <typename T, uint32_t N>
    std::vector<std::string> g_ptr(T const (*array)[N])  // OK
    {
        if (array == nullptr) {
            return std::vector<std::string>{};
        }

        auto ret = std::vector<std::string>{N};

        std::transform(*array, std::end(*array), ret.begin(),
                       [](auto& b) noexcept { return b.Name0(); });

        return ret;
    }

```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 899

    TEST(ProgrammingConvention, not_use_convert_to_ptr)
    {
        Base    b[]{"0", "0"};
        Derived d[]{{"0", "1"}, {"2", "3"}};

        ASSERT_EQ((std::vector<std::string>{"0", "0"}), f_ref_2(b));  // OK
        ASSERT_EQ((std::vector<std::string>{"0", "0"}), f_ref_n(b));  // OK
        ASSERT_EQ((std::vector<std::string>{"0", "0"}), g_ref(b));    // OK

        // ASSERT_EQ((std::vector<std::string>{"0", "2"}), f_ref_2(d));  OK 誤用なのでコンパイルエラー
        ASSERT_EQ((std::vector<std::string>{"0", "2"}), g_ref(d));  // OK

        // 配列へのポインタを使う場合
        ASSERT_EQ((std::vector<std::string>{"0", "0"}), g_ptr(&b));  // OK

        Derived(*d_null)[3]{nullptr};
        ASSERT_EQ((std::vector<std::string>{}), g_ptr(d_null));  // OK
    }
```

* デフォルト引数は関数のプロトタイプ宣言もしくはクラス宣言内のメンバ関数宣言のみに記述する
  (「[オーバーライド](programming_convention.md#SS_3_3_2_7)」参照)。
* メンバ関数のデフォルト引数は、
  そのクラス外部からのメンバ関数呼び出しを簡潔に記述するための記法であるため、
  非publicなメンバ関数にデフォルト引数を持たさない。
* デフォルト引数の初期化オブジェクトは定数、もしくは常に等価なオブジェクトにする。
  デフォルト引数の初期化オブジェクトは関数呼出し時に評価されるため、
  引数の初期化オブジェクトが等価でない場合、
  関数の処理が初期化オブジェクトの現在の状態に依存してしまう。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 921

    int32_t default_arg{0};
    int32_t get_default_arg(int32_t a = default_arg) noexcept { return a; }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 930

    ASSERT_EQ(0, get_default_arg());  // default_arg == 0

    default_arg = 2;

    ASSERT_EQ(2, get_default_arg());  // default_arg == 2
```

* std::unique_ptr\<T> const&を引数とする関数は、
  その引数が指すオブジェクトが保持しているT型オブジェクトを書き換えることができるため、
  そのような記述をしない。
  関数がそのT型オブジェクトを書き換える必要があるのであれば引数をT&とする。
  書き換える必要がないのであれば引数をT const&とする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 942

    void f0(std::unique_ptr<std::string> const& str)  // NG *strは書き換え可能
    {
        *str = "it can be changed";

    #if 0  // strはconstなので以下はできない
        str = std::make_unique<std::string>("haha");
    #endif
    }

    void f1(std::string& str)  // OK
    {
        str = "it can be changed";
    }

    void f2(std::string const& str)  // OK
    {
    #if 0  // strは変更できない
        str = "it can NOT be changed";
    #endif
    }

    void g()
    {
        auto s = std::make_unique<std::string>("hehe");

        f0(s);   // sは変更されないが、sが保持しているstd::stringオブジェクトは変更できる
        f1(*s);  // sは変更されないが、sが保持しているstd::stringオブジェクトは変更できる
        f2(*s);  // sも、sが指しているstd::stringオブジェクトも変更されない
    }
```

* [演習-仮引数の修飾](exercise_q.md#SS_19_3_11)  

#### 3.3.3.6 自動変数 <a id="SS_3_3_3_6"></a>
* 一つの文で複数の変数の宣言をしない。
* 自動変数は、それを使う直前に定義することでスコープを最小化する。
* 自動変数は、定義と同時に初期化する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1008

    int32_t a, b;  // NG 一度に2つの変数定義
    int32_t index;

    // Do something
    ...

    index = get_index();                    // NG 定義と使用箇所が離れている
    int32_t index2{get_index()};            // OK
    auto    index3 = get_index();           // OK AAA
    auto    index4 = int32_t{get_index()};  // OK 型を明示したAAA

    int32_t i;

    for (i = 0; i < max; ++i) {  // NG 定義と使用箇所が離れている
        // Do something
    }

    for (int32_t i{0}; i < max; ++i) {  // OK
        // Do something
        ...
    }

    for (auto i = 0; i < max; ++i) {  // OK AAAスタイル
        // Do something
        ...
    }

    ...

    auto& w0 = Widget::Inst();  // if文後にはw0を使用しないならばNG
    if (w0.GetStatus() == Widget::Success) {
        w0.DoSomething();
    }
    else {
        w0.DoSomething(Widget::None);
    }
    // この後w0を使用しない

    ...

    if (auto& w1 = Widget::Inst(); w1.GetStatus() == Widget::Success) {  // OK C++17より使用可能
        w1.DoSomething();
    }
    else {
        w1.DoSomething(Widget::None);
    }

    ...

    auto const& w2 = Widget::InstConst();  // switch文後にw2を使用しないならばNG
    switch (w2.GetStatus()) {
    case Widget::Success:
        // Do something
        break;
        ...
    default:
        // Do something
        break;
    }
    // この後w2を使用しない

    ...

    switch (auto const& w3 = Widget::InstConst(); w3.GetStatus()) {  // OK C++17より使用可能
    case Widget::Success:
        // Do something
        break;
        ...
    default:
        // Do something
        break;
    }
```

#### 3.3.3.7 戻り値型 <a id="SS_3_3_3_7"></a>
* メモリアロケータ以外の関数の戻り値をvoid\*にしない。
* 避けがたい理由なしに「戻り値の型を後置する関数宣言構文」を使用しない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1111

    auto f(int32_t a, int32_t b) noexcept -> decltype(a + b)  // NG
    {
        return a + b;
    }

    template <typename T>
    auto f(T a, T b) noexcept -> decltype(a + b)  // OK 後置構文以外に方法がない
    {
        return a + b;  // T = uint8_tとすると、a + bの型はint32_t
    }
```

* 戻り値を比較的大きなオブジェクトにする場合、パフォーマンスに注意する
  (「[関数の戻り値オブジェクト](programming_convention.md#SS_3_9_3)」参照)。

* 関数が複数の値を返す場合、std::pair、std::tupple、構造体オブジェクトを戻り値にして返す。
  パフォーマンスに著しい悪影響がない限り、その値をリファレンス引数で返さない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1124

    void g0(int32_t a, int32_t b, int32_t& quotient, int32_t& remainder)  // NG
    {
        quotient  = a / b;
        remainder = a % b;
    }

    int32_t g1(int32_t a, int32_t b, int32_t& remainder)  // NG
    {
        remainder = a % b;
        return a / b;
    }

    std::pair<int32_t, int32_t> g_pair(int32_t a, int32_t b)  // OK
    {
        return {a / b, a % b};
    }

    struct Result {
        int32_t quotient;
        int32_t remainder;
    };

    Result g_struct(int32_t a, int32_t b)  // OK
    {
        return {a / b, a % b};
    }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 1157

    {
        int32_t quotient;
        int32_t remainder;
        g0(7, 3, quotient, remainder);  // NG quotient、remainderが戻り値かどうかわかりづらい
        ASSERT_EQ(2, quotient);
        ASSERT_EQ(1, remainder);
    }
    {
        int32_t remainder;
        int32_t quotient{g1(7, 3, remainder)};  // NG remainderが戻り値かどうかわかりづらい
        ASSERT_EQ(2, quotient);
        ASSERT_EQ(1, remainder);
    }
    {
        auto ret = g_pair(7, 3);  // OK
        ASSERT_EQ(2, ret.first);
        ASSERT_EQ(1, ret.second);
    }
    {
        auto [quotient, remainder] = g_struct(7, 3);  // OK C++17 構造化束縛
        ASSERT_EQ(2, quotient);
        ASSERT_EQ(1, remainder);
    }
    {
        auto ret = g_struct(7, 3);  // OK
        ASSERT_EQ(2, ret.quotient);
        ASSERT_EQ(1, ret.remainder);
    }
```

* 処理の成否をbool等で通知し、成功時の戻り値をリファレンス引数で戻す関数や、
  処理の成功時の値と、失敗時の外れ値を戻り値で返す関数を作らない。
  代わりにC++17で導入されたstd::optionalを使用する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1215

    bool h0(int32_t a, int32_t b, int32_t& remainder)  // NG
    {
        if (b == 0) {
            return false;
        }

        remainder = a % b;

        return true;
    }

    int32_t h1(uint32_t a, uint32_t b)  // NG 余りが-1になる場合(外れ値)、エラー通知
    {
        if (b == 0) {
            return -1;
        }

        return a % b;
    }

    std::pair<bool, int32_t> h_pair(int32_t a, int32_t b)  // NG
    {
        if (b == 0) {
            return {false, 0};
        }

        return {true, a % b};
    }

    struct Result2 {
        bool    is_success;
        int32_t remainder;
    };

    Result2 h_struct(int32_t a, int32_t b)  // NG
    {
        if (b == 0) {
            return {false, 0};
        }

        return {true, a % b};
    }

    std::optional<int32_t> h_optional(int32_t a, int32_t b)  // OK
    {
        if (b == 0) {
            return std::nullopt;
        }

        return a % b;
    }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 1272

    {
        int32_t remainder;

        auto result = h0(7, 0, remainder);
        ASSERT_FALSE(result);  // エラー時にremainderが有効か否かわからない
    }
    {
        auto remainder = h1(7, 0);
        ASSERT_EQ(-1, remainder);  // エラー通知がわかりづらい
    }
    {
        auto [result, remainder] = h_pair(7, 0);
        ASSERT_FALSE(result);  // エラー時にremainderが有効か否かわからない
    }
    {
        auto [result, remainder] = h_struct(7, 0);
        ASSERT_FALSE(result);  // エラー時にremainderが有効か否かわからない
    }
    {
        auto result = h_optional(7, 0);
        ASSERT_FALSE(result);

        result = h_optional(7, 4);
        ASSERT_TRUE(result);
        ASSERT_EQ(3, *result);  // 成功時の値取り出し
    }
```


#### 3.3.3.8 constexpr関数 <a id="SS_3_3_3_8"></a>
* 多くの使用箇所で戻り値がコンパイル時に確定する関数テンプレートもしくはinline関数は、
  constexprと宣言する(「[constexprインスタンスと関数](term_explanation.md#SS_18_1_15)」参照)。

* コンパイル時に値が確定する[ラムダ式](programming_convention.md#SS_3_4_8)を戻り値に持つ関数はconstexprと宣言する。

* [演習-constexpr関数](exercise_q.md#SS_19_3_12)  

#### 3.3.3.9 リエントラント性 <a id="SS_3_3_3_9"></a>
* 関数、メンバ関数はなるべくリエントラントに実装する。
* 複数のスレッドから呼び出される関数は必ずリエントラントにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1328

    int32_t var{0};

    int32_t f() noexcept  // リエントラントでない関数f()
    {
        return ++var;
    }

    int32_t f(int32_t& i) noexcept  // リエントラントな関数f()
    {
        return ++i;
    }
```

#### 3.3.3.10 エクセプション処理 <a id="SS_3_3_3_10"></a>
* 関数はそれが不可避でない限り、[no-fail保証](term_explanation.md#SS_18_7_1)をする。
* throwをせざるを得ない場合、最低でも[基本保証](term_explanation.md#SS_18_7_3)をする。
* STLコンテナ(std::string, std::vector等)が発生させるエクセプションはtry-catchせず
  (catchしてデバッグ情報を保存するような場合を除く)、
  プログラムをクラッシュさせる。try-catchしてもできることはない。
* 特別な理由がない限り、コンストラクタ呼び出しはnoexceptと宣言する。
  ネットワーク接続等、簡単にエラーすることをコンストラクタ内で行わない。
* [オープン・クローズドの原則(OCP)](solid.md#SS_8_2)、[リスコフの置換原則(LSP)](solid.md#SS_8_3)に違反する場合が多いため、
  「throwキーワードによるエクセプション仕様」を使用しない(C++17で廃止)。
* エクセプションをthrowしないことが確定している関数は、noexceptと宣言する。
  move代入演算子をnoexceptと宣言することは特に重要である。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1359

    int32_t f() noexcept;  // OK fはno-fail保証

    class Derived : public Base {
        ...
        // オブジェクトの状態を変えず(const)、エクセプションを発生させず(noexcept)
        // f()の最後(final)のoverride
        virtual int32_t f() const noexcept final
        {
            ...
        }
    };
```

* try-catchが不可避である場合、以下の理由によりconstリファレンスで受け取る。
    * 実態で受け取るとオブジェクトの[スライシング](term_explanation.md#SS_18_3_3)が起こる場合がある。
    * 受け取ったエクセプションオブジェクトを書き換えるべきではない。

* エクセプションによるリソースリークを避けるため[RAII(scoped guard)](design_pattern.md#SS_9_9)でリソースを管理する。
* 一連のcatch節では、catchするエクセプションの型の最もマッチ率の高いcatch節で処理されるのではなく、
  マッチした最上位のcatch節で処理されるため、
  catchするエクセプションの型に継承関係があるのであれば、継承順位が低い順番にcatchする。
  また、catch(...)は一番最後に書く(関数tryブロックの場合も同様にする)。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1379

    struct ExceptionA : std::exception {};
    struct ExceptionB : ExceptionA {};
    struct ExceptionX : std::exception {};

    void order_of_catch() noexcept
    {
        try {
            ...
        }
        catch (ExceptionB const& e) {  // ExceptionAの前に書く。
            ...
        }
        catch (ExceptionA const& e) {  // std::exceptionの前に書く。
            ...
        }
        catch (ExceptionX const& e) {  // std::exceptionの前に書く。
            ...
        }
        catch (std::exception const& e) {  // catch(...)の前に書く。
            ...
        }
        catch (...) {  // 必ず一番最後に書く。
            ...
        }
    }

    void order_of_catch_with_try() noexcept
    try {  // 関数tryブロック
        ...
    }
    catch (ExceptionB const& e) {  // ExceptionAの前に書く。
        ...
    }
    catch (ExceptionA const& e) {  // std::exceptionの前に書く。
        ...
    }
    catch (ExceptionX const& e) {  // std::exceptionの前に書く。
        ...
    }
    catch (std::exception const& e) {  // catch(...)の前に書く。
        ...
    }
    catch (...) {  // 必ず一番最後に書く。
        ...
    }
```

* エクセプションをthrowする場合、独自定義したオブジェクトを使用しない。
  代わりにstd::exceptionか、これから派生したクラスを使用する。
  また、throwされたオブジェクトのwhat()から、throwされたファイル位置が特定できるようにする
  (「[ファイル位置を静的に保持したエクセプションクラスの開発](template_meta_programming.md#SS_13_6_7_4)」参照)。


* noexceptと宣言された関数へのポインタへ、noexceptでない関数のポインタを代入しない
  (C++17では[ill-formed](term_explanation.md#SS_18_10_8)になる)。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1442

    int32_t f0()  // noexceptではないため、エクセプションを発生させることがある。
    {
        ...
    }

    int32_t f1() noexcept
    {
        ...
    }

    #if __cplusplus < 201703L  // 以下のコードはC++14以前ではコンパイルできるが、
                               // C++17以降ではコンパイルエラー
    int32_t (*f_ptr0)() noexcept = &f0;  // NG f_ptr0()はnoexceptだが、
                                         //    f0はエクセプションを発生させる可能性がある。
    #endif
    int32_t (*f_ptr1)() noexcept = &f1;  // OK
    int32_t (*f_ptr2)()          = &f0;  // OK
    int32_t (*f_ptr3)()          = &f1;  // OK f1はエクセプションを発生させない。

    class A {
    public:
        int32_t f0()  // noexceptではないため、エクセプションを発生させることがある。
        {
            ...
        }

        int32_t f1() noexcept
        {
            ...
        }
    };

    #if __cplusplus < 201703L  // 以下のコードはC++14以前ではコンパイルできるが、
                               // C++17以降ではコンパイルエラー
    int32_t (A::*mf_ptr0)() noexcept = &A::f0;  // NG mf_ptr0()はnoexceptだが、
                                                //    f0はエクセプションを発生させる可能性がある。
    #endif
    int32_t (A::*mf_ptr1)() noexcept = &A::f1;  // OK
    int32_t (A::*mf_ptr2)()          = &A::f0;  // OK
    int32_t (A::*mf_ptr3)()          = &A::f1;  // OK f1はエクセプションを発生させない。

```

* [演習-エクセプションの型](exercise_q.md#SS_19_3_13)  

#### 3.3.3.11 ビジーループ <a id="SS_3_3_3_11"></a>
* 待ち合わせにビジーループを使わない。イベントドリブンにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1504

    // NG イベントドリブンにするべき
    void wait_busily() noexcept
    {
        while (1) {
            sleep(1);
            if (xxx_flag) {
                ...
                break;
            }
        }

        ...
    }

    // OK selectでイベント発生を待つ。
    void wait_event(fd_set const& rfds, uint32_t wait_sec) noexcept
    {
        while (1) {
            auto rfds2 = rfds;
            auto tv    = timeval{wait_sec, 0};

            auto retval = select(1, &rfds2, 0, 0, &tv);

            ...
        }

        ...
    }
```

* [注意] C++11からイベント通知のためにstd::condition_variable
  (「[並行処理](concurrency.md#SS_12)」参照)が導入された。

## 3.4 構文 <a id="SS_3_4"></a>

### 3.4.1 複合文 <a id="SS_3_4_1"></a>
* if, else, for, while, do後には複合文を使う。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 22

    if (a == 0) {
        b = 0;  // OK
    }

    if (a == 0)
        b = 0;                      // NG 複合文でない

    if (a == 0) {
        b = 0;                      // OK
    }
    else                            // NG 複合文でない
        b = 1;

    for (auto i = 0; i < a; ++i) {  // OK
        c[i] = i;
    }

    for (auto i = 0; i < a; ++i)    // NG
        c[i] = i;
```

* 空の複合文には、何もすることがないという意図を表現するため、";"だけの文を置き、
  空の複合文である事を明示する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 53

    while (volatile_flag) {
    }  // NG ;が無い

    while (volatile_flag) {
        ;  // OK
    }

    while (volatile_flag)
        ;  // NG whileの文が複合文でない
```

### 3.4.2 switch文 <a id="SS_3_4_2"></a>
* caseラベル、defaultラベルに関連付けられた一連の文はできだけフォールスルーさせない。
  実装がシンプルになる等の理由からフォールスルーさせる場合、
  それが意図であることを明示するため以下のような記述する。

    // fallthrough          // C++14以前

    [[fallthrough]];        // C++17以降

* defaultラベルは省略せず、switch文の末尾に書く。
    * defaultラベルに関連付けられた処理がない場合は、breakのみを記述する。
    * 論理的にdefaultラベルに到達しないのであれば、
      defaultラベルに続いてassert(false)を実行することで、
      そこを通過してはならないことを明示する(「[assertion](programming_convention.md#SS_3_11_1)」参照)。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 79

    switch (a) {
    case 0:
        b = 0;
        break;  // OK
    case 1:
        e = 2;  // NG break無しで抜けているのにコメントが無い
    case 2:
        c = 1;
        // fallthrough  C++14以前であればOK
    case 3:
        e += 2;
        [[fallthrough]];  // OK C++17
    case 4:
        d = 1;
        break;  // OK
    default:
        assert(false);  // OK 論理的にここには来ないのならば、defaultを省略せずにassert
    }
```

### 3.4.3 if文 <a id="SS_3_4_3"></a>
* if-else-ifと連続する場合は、else文で終了させる。
  最後のelseのブロックでやるべき処理がないのであれば、そのブロックに;のみを記述する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 111

    if (a == 1) {
        ...
    }
    else if (a == 2) {
        ...
    }  // NG elseで終了していない

    if (a == 1) {
        ...
    }
    else if (a == 2) {
        ...
    }
    else {  // OK else文でやることがない場合は、;のみ記述
        ;
    }
```

* if-else-ifの最後のelseのブロックに論理的に到達しないのであれば、
  そのブロックでassert(false)を実行する(「[assertion](programming_convention.md#SS_3_11_1)」参照)。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 134

    if (a == 1) {
        ...
    }
    else if (a == 2) {
        ...
    }
    else {              // OK
        assert(false);  //    ここに来るのはバグの場合。
    }
```

* 条件が2つ以上且つ、switchで表現できる条件文には、ifではなくswitchを使用する。
* ifの条件式が、コンパイル時に定まるのであれば、[constexpr if文](template_meta_programming.md#SS_13_6_4)を使用する。

### 3.4.4 範囲for文 <a id="SS_3_4_4"></a>
* 配列やコンテナの全要素にアクセスするような繰り返し処理には、
  [off-by-oneエラー](https://ja.wikipedia.org/wiki/Off-by-one%E3%82%A8%E3%83%A9%E3%83%BC)
  が避けられ、従来よりもシンプルに記述できる[範囲for文](term_explanation.md#SS_18_10_3)を使用する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 155

    auto vect = std::vector<uint32_t>{0, 1, 2, 3, 4};

    // NG oldスタイル
    for (auto i = 0U; i < vect.size(); ++i) {
        std::cout << vect[i] << " ";
    }
    ...

    // NG C++03スタイル
    for (std::vector<uint32_t>::iterator it = vect.begin(); it != vect.end(); ++it) {
        *it = 3;
    }

    for (std::vector<uint32_t>::const_iterator it = vect.cbegin(); it != vect.cend(); ++it) {
        std::cout << *it << " ";
    }
    ...

    // OK C++11スタイル
    for (auto const& a : vect) {
        std::cout << a << " ";
    }
    ...
```

* 独自のコンテナクラスを定義する場合、STLコンテナと同様の要件を満たすbegin()、end()や、
  cbegin()、cend()も定義し、そのコンテナに[範囲for文](term_explanation.md#SS_18_10_3)を適用できるようにする
  (「[デバッグ用イテレータ](dynamic_memory_allocation.md#SS_14_2_4)」参照)。

* [演習-コンテナの範囲for文](exercise_q.md#SS_19_4_1)  

### 3.4.5 制御文のネスト <a id="SS_3_4_5"></a>
* breakとの関係がわかりづらい、ブロックが巨大になる等の問題があるため、
  if, for, while, do-while, switch文に付随するブロックの中にswitch文を書かない。

### 3.4.6 return文 <a id="SS_3_4_6"></a>
* returnの後に括弧をつけない。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 194

    ...

    if (xxx) {
        // decltype(retval)は、int32_t
        // decltype((retval))は、(retval)がlvalueであるためint32_t&
        // この違いは通常問題にはならないが、関数の戻り値を型推測させると問題になる。
        return (retval);  // NG ()は不要
    }
    else {
        return retval2;  // OK
    }
```

* 下記のようなreturnしない関数には、[[noreturn]]をつけて宣言、定義する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 215
    // @fn terminate(char const* message)
    // @brief メッセージを出力してプログラムを終了させる。
    // @param const char* message 上記メッセージ
    [[noreturn]] void terminate(char const* message)
    {
        auto const str = std::string{"unrecoverable error"} + message;

        ...

        throw std::runtime_error{str};
    }
```

### 3.4.7 goto文 <a id="SS_3_4_7"></a>
* 二重以上のループを抜ける目的以外でgotoを使用しない。
* 二重以上のループを抜ける目的でgotoを使用する場合、gotoのジャンプ先ラベルはそのループの直後に置く。

### 3.4.8 ラムダ式 <a id="SS_3_4_8"></a>
* [ラムダ式](term_explanation.md#SS_18_10_4)を複雑にしない。
    * できるだけワンライナーにする。
    * 必ず10行以下にする。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 235

    // ラムダ式はワンライナーが基本
    auto itr = std::find_if(strs.begin(), strs.end(), [](auto const& n) noexcept {
        return (n.at(0) == 'n') && (n.size() > 5);
    });
```

* デフォルトのキャプチャ方式は、ローカル変数を無限定にキャプチャしてしまうため使用しない。
    * C++11では、キャプチャする変数ごとに代入キャプチャか参照キャプチャを使用する。
    * C++14以降では、初期化キャプチャを使用する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 260

    // NG デフォルトのキャプチャ方式
    class A {
    public:
        ...
        std::vector<std::string> GetNameLessThan(uint32_t length) const
        {
            auto ret = std::vector<std::string>{};

    #if 1  // 手が滑って、strをstrs_としてしまったバグ([=]によってthisが導入されている)。

            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [=](auto const& str) noexcept { return (strs_.size() < length); });

    #else  // 本来は下記のように書きたかったが、
           // キャプチャ範囲が大きすぎるため上記バグを生み出してしまった。

            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [=](auto const& str) noexcept { return (str.size() < length); });
    #endif
            return ret;
        }

    private:
        std::vector<std::string> strs_;
    };
```

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 295

    // OK 限定したキャプチャにより、ラムダ式から可視である変数が限定された
    class A {
    public:
        ...
        std::vector<std::string> GetNameLessThan(uint32_t length) const
        {
            auto ret = std::vector<std::string>{};

    #if CPP_VER == 11  // c++11
                       // [length]を代入キャプチャと呼ぶ。

            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [length](std::string const& str) noexcept { return (str.size() < length); });

    #elif CPP_VER == 14  // c++14以降
            // [length = length]を初期化キャプチャと呼ぶ。
            // 左のlengthのスコープはラムダ式内。右のlengthのスコープはGetNameLessThan内。

            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [length = length](auto const& str) noexcept { return (str.size() < length); });
    #else
            static_assert(false, "CPP_VER should be 11 or 14");
    #endif
            return ret;
        }
        ...
    };
```

* 外部のオブジェクトを参照キャプチャしたクロージャを、
  その外部オブジェクトのライフタイムを超えて使用しない。
    * 関数で作られたクロージャがその関数のローカル変数のハンドルを使用するのであれば、
      そのクロージャをその関数外で使用しない。
    * オブジェクトで作られたクロージャがそのメンバ変数のハンドルを使用するのであれば、
      そのオブジェクトの終了後にそのクロージャを使用しない。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 331

    class B {
    public:
        ...
        std::function<bool(int)> GenLambda(int max)
        {
            // NG
            // この関数が返すはクロージャがリファレンスしているmaxはこの関数が終了すると無効になる。
            return [&max](int n) noexcept { return n < max; };
        }

        std::function<bool(int)> GenLambda()
        {
            // NG
            // この関数が返すクロージャがリファレンスしているmin_はBオブジェクトが終了すると無効になる。
            return [&min = min_](int n) noexcept { return n > min; };
        }

    private:
        int min_;
    };
```

* C++17以降では、 コンパイル時に戻り値が確定するラムダ式の呼び出し式はリテラルにできるため、
  そのようなラムダ式を戻り値に持つ関数はconstexprと宣言する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 369

    auto square1 = [](int32_t n) { return n * n; };

    static_assert(square1(2) == 4);  // C++17以降、square1(2)はリテラル

    auto i = 2;
    // static_assert(square1(i) == 2);  // iはconstexprではないので、コンパイルエラー

    constexpr auto j       = 2;
    constexpr auto square2 = [n = j]() { return n * n; };  // constexprの宣言が必要

    static_assert(square2() == 4);  // C++17以降、square2()はリテラル

    auto square3 = [n = j]() { return n * n; };

    // static_assert(square3() == 4);  // square3()はリテラルではないので、コンパイルエラー
```
```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 390

    constexpr int32_t square4(int32_t n)  // OK nがconstexprであれば、ラムダはconstexpr
    {
        return [n] { return n * n; }();
    }

    static_assert(square4(2) == 4);  // C++17以降、square4(2)はリテラル

    constexpr auto square5(int32_t n)  //  OK nがconstexprであれば、ラムダはconstexpr
    {
        // nがconstexprならば、ラムダ式はリテラル
        auto f = [n] { return n * n; };

        // fの戻り値がリテラルならば、gもリテラル
        auto g = [f] { return f(); };
        return g;
    }

    static_assert(square5(2)() == 4);  // C++17以降、square5(2)はリテラル
```

* [演習-ラムダ式](exercise_q.md#SS_19_4_2)  
* [演習-ラムダ式のキャプチャ](exercise_q.md#SS_19_4_3)  

### 3.4.9 マクロの中の文 <a id="SS_3_4_9"></a>
* マクロの中に文がある場合、do-while(0)イデオムを使用する(「[関数型マクロ](programming_convention.md#SS_3_6_1)」参照)。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 418

    // do-while(0)イデオムによる関数型マクロ
    #define INIT_ARRAY(array_, x_)      \
        do {                            \
            for (auto& a_ : (array_)) { \
                a_ = (x_);              \
            }                           \
        } while (0)

    void f(uint32_t (&a)[10])
    {
        // INIT_ARRAYがdo-whileではなく、単なるブロックで囲むと、";"が余計になる。
        INIT_ARRAY(a, 3);
    }
```

## 3.5 演算子 <a id="SS_3_5"></a>

### 3.5.1 優先順位 <a id="SS_3_5_1"></a>
* 優先順位が分かりづらい式では、順序を明示するために丸括弧を使う。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 20

    // 論理演算子例
    if (a < b && c < d || e < f)  // NG 優先順位がわからない
    {
        ...
    }

    if (((a < b) && (c < d)) || (e < f))  // OK
    {
        ...
    }

    // シフト演算子例
    auto a0 = b << 16 + 1;    // NG
    auto a1 = b << (16 + 1);  // OK
    auto a2 = (b << 16) + 1;  // OK

    // ビット演算ではないが
    std::cout << a0 + 1;    // NG
    std::cout << (a1 + 1);  // OK

    // 三項演算子例
    auto e0 = a ? b : c = d;      // NG
    auto e1 = ((a ? b : c) = d);  // OK
    auto e2 = (a ? b : (c = d));  // OK 上記NG式と同じ意味
```

* [注意] 複合代入式と、それと等価に見える式での演算順序の違いに気を付ける。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 62
    {
        auto a = 4;

        a = a * 3 / 2;
        ASSERT_EQ(6, a);
    }
    {
        auto a = 4;

        a *= 3 / 2;  // この式は、a = a * 3 / 2と等価ではない
        ASSERT_EQ(4, a);
    }
```

### 3.5.2 代入演算 <a id="SS_3_5_2"></a>
* [単純代入](term_explanation.md#SS_18_10_7)のみからなる文を除き、1つの文で複数の代入を行わない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 89

    a = b = 0;              // OK
    b     = (a += 1) + 2;   // NG
    b     = (a++) + (c++);  // NG

    b = b++;  // NG unary operators assign itself.

    ++a;         // OK
    auto i = a;  // OK

    a = 0;  // OK
```

* 一部の例外を除き、ifの条件文の中で代入しない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 105

    if (c = b) {  // NG ifの条件文の中で代入
        return 0;
    }

    if ((fd1 = socket(AF_INET, SOCK_STREAM, 0)) < 0) {  // OK このような場合は代入していることが明確
        return false;
    }

    if (auto fd2 = socket(AF_INET, SOCK_STREAM, 0); fd2 < 0) {  // OK C++17
        return false;
    }
    else {
        // fd2を使った処理
        ...
    }
```

### 3.5.3 ビット演算 <a id="SS_3_5_3"></a>
* オーバーフロー、アンダーフローしたときの符号の扱い方が未定義であるため、
  signed変数へのビット演算を使用しない。
  (「2の階乗での除算は、ビット演算に置き換えることで実行速度が速くなる」というのは都市伝説である)。
* [注意] ビット演算にはstd::bitsetや[BitmaskType](design_pattern.md#SS_9_2)を使用することもできる。

### 3.5.4 論理演算 <a id="SS_3_5_4"></a>
* &&や||の論理演算子の右オペランドで[副作用](term_explanation.md#SS_18_11_4)のある処理をしない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 136

    if (a == 0 && ++b > 3) {  // NG ++bが上記の副作用
        ...
    }

    // ↑のような記述は、↓とは意味が違う
    ++b;
    if (a == 0 && b > 3) {  // OK
        ...
    }

    if (a == 0) {  // OK 上記NGのif文と同じ意味
        ++b;
        if (b > 3) {
            ...
        }
    }
```

### 3.5.5 三項演算子 <a id="SS_3_5_5"></a>
* 単純なif文よりも、三項演算子を優先して使用する
  (const変数の条件付き初期化は三項演算子でのみ可能である)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 168

    int const a0{xxx ? 3 : 4};  // OK constで定義、初期化

    int a1;  // NG a1をconstにできない
             //    定義と初期が分離してしまう
    if (xxx) {
        a1 = 3;
    }
    else {
        a1 = 4;
    }
```

* [演習-三項演算子](exercise_q.md#SS_19_5_1)  

### 3.5.6 メモリアロケーション <a id="SS_3_5_6"></a>
#### 3.5.6.1 new <a id="SS_3_5_6_1"></a>
* オブジェクトのダイナミックな生成には、特別な理由がない限りnewを使用せず、
  std::make_unique<>やstd::make_shared<>を使用する。
  また、特別な理由でnewした場合、そのポインタはstd::unique_ptr<>やstd::shared_ptr<>で管理する。
* new(nothrow)、プレースメントnewは使用しない。
* 配列型オブジェクトのダイナミックな生成を避け、
  代わりにstd::arrayをダイナミックに生成するか、std::vectorを使用する。
* newの戻り値がnullptrであることはない、
  もしくはnewがnullptrを返してきた場合、リカバリーすることはできないため、
  new演算子の返り値をnullptrと比較しない。
    * operator newを独自に実装した場合でも、newはnullptrを返してはならない。
      メモリが不足した場合、assert(false)させるかstd::bad_allocをthrowする。
* スタック上で生成しても差し支えないオブジェクトをダイナミックに生成しない。
* newを禁止したいクラスには、privateなoperator new()を宣言する(定義は不要)か、= deleteする。

#### 3.5.6.2 delete <a id="SS_3_5_6_2"></a>
* [不完全型](term_explanation.md#SS_18_1_10)のオブジェクトへのポインタをdeleteしない。
  特に「[Pimpl](design_pattern.md#SS_9_3)」を使用する場合には注意が必要である。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 202

    void deleteA(A* a_ptr) noexcept
    {
        // Aが不完全型だった場合、deleteAは、A::~A()にアクセスできないため、A::~A()は呼び出されない
        // これはリソースリークにつながる
        delete a_ptr;
    }

    // やむを得ず、deleteAのような関数を作る場合、下記のようにstatic_assertをdelete行の直前に書く
    // こうすることによりAが不完全型であった場合、コンパイルエラーとなる
    void deleteA2(A* a_ptr) noexcept
    {
        static_assert(sizeof(*a_ptr) != 0, "incomplete type");
        delete a_ptr;
    }

    // やむを得ず、deleteAのような関数を作る場合、std::unique_ptr<>を使用することもできる
    // こうすることによりAが不完全型であった場合、コンパイルエラーとなる
    void deleteA3(A* a_ptr) noexcept { std::unique_ptr<A> a(a_ptr); }
```

* 不完全型と同じような不具合が起こるためvoid\*をdeleteしない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 224

    void delete_ptr(void* v_ptr) noexcept
    {
        // NG
        // 任意の型のポインタは、キャストすること無しでこの関数に渡すことができる
        // そのポインタがクラス型であった場合でも、void*として扱われるため、
        // そのクラスのデストラクタは呼び出されない
        delete v_ptr;
    }

    void deleteA4(A* ptr) noexcept
    {
        delete_ptr(ptr);  // NG ptrはvoid*へ暗黙のキャストが行われる
                          //    delete_ptrでは、A::~A()は呼び出されない
    }
```

* deleteはオペランドがnullptrであった場合、何もしないため、delete対象ポインタをnullptrと比較しない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 244

    if (ptr != nullptr) {  // NG nullptrとの比較は不要
        delete ptr;
    }

    ...

    delete ptr;  // OK ptrがnullptrでも問題ない
```

* [演習-delete](exercise_q.md#SS_19_5_2)  

#### 3.5.6.3 メモリ制約が強いシステムでの::operator new <a id="SS_3_5_6_3"></a>
* [注意]このルールは以下のようなソフトウェアを対象とする。  
    * 使用できるメモリが少なく、且つほとんど再起動されない。
    * メモリリークの可能性を否定できない3rdパーティライブラリを使っている。
    * MISRA/AUTOSAR C++等のヒープの使用制限が強い規約を守る必要がある
      (ヒープを使った場合の最長処理時間の決定が難しいためリアルタイム性に問題がある)。

  このようなソフトウェア開発においてはこのルールは重要であるが、
  逆にそのような制限のないソフトウェア開発においては不要である。

* デフォルトのグローバルnewを使用しない。
    * リアルタイム性に制約のあるシステムでは、
      「[グローバルnew/deleteのオーバーロード](dynamic_memory_allocation.md#SS_14_2)」で述べたようなnewを実装する。
    * メモリ制限が強いシステムでは、ダイナミックなオブジェクト生成を避け、
      やむを得ない場合、「[クラスnew/deleteのオーバーロード](dynamic_memory_allocation.md#SS_14_3)」
      で述べたようなクラス毎のnewを実装する。

* エクセプションの送出にダイナミックなメモリアロケーションを使用している場合
  (多くのコンパイラはmalloc/newを用いてエクセプション送出を行っている)、
  エクセプションの送出をしない(「[エクセプション処理機構の変更](dynamic_memory_allocation.md#SS_14_4_4)」参照)。


### 3.5.7 sizeof <a id="SS_3_5_7"></a>
* sizeof(型名)とsizeof(インスタンス名)の両方が使える場合、sizeof(インスタンス名)を優先的に使用する。
* ポインタ型変数に関して、それが指しているインスタンスのサイズを獲得する場合は、
  sizeof(\*ポインタ型変数名)を使用する
  (そのポインタがnullptrであってもデリファレンスされないので問題ない)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 270

    uint8_t  a = 0;
    uint8_t* b = &a;

    auto s_0 = sizeof(uint8_t);  // NG aのサイズをs_0に代入したい場合
    auto s_1 = sizeof(a);        // OK aのサイズをs_1に代入したい場合
    auto s_2 = sizeof(*b);       // OK *bのサイズをs_2に代入したい場合
```

* 上記例を除き、sizeof演算子のオペランドは一見[副作用](term_explanation.md#SS_18_11_4)を持っているような式を含んではならない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 282

    a = 0;

    auto size_3 = sizeof(++a);  // NG  おそらく意図通りには動かない
                                // この行でもa == 0(++aは効果がない)
```

* C++03のテンプレートの実装でよく使われたsizeofによるディスパッチを行わない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 295

    // 下記のようなsizeofディスパッチはC++03ではよく使われたが、
    // C++11ではtype_traitsを使えば、もっとスマートに実装できる
    struct True {
        uint8_t temp[2];
    };
    struct False {
        uint8_t temp[1];
    };

    constexpr True  sizeof_dispatch(int32_t);
    constexpr False sizeof_dispatch(...);
```
```cpp
    // @@@ example/programming_convention/operator_ut.cpp 312

    static_assert(sizeof(sizeof_dispatch(int{})) == sizeof(True), "int32_t is int");
    static_assert(sizeof(sizeof_dispatch(std::string{})) != sizeof(True), "int32_t is not string");

    // 上記はC++11では下記のように実装すべき
    static_assert(std::is_same_v<int, int32_t>, "int32_t is int");
    static_assert(!std::is_same_v<std::string, int32_t>, "int32_t is not string");

```

* 一見、配列に見えるポインタをsizeofのオペランドにしない。
  (「[実引数/仮引数](programming_convention.md#SS_3_3_3_5)」参照)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 327

    void f(int8_t arg_array0[5], int8_t arg_array1[], int8_t (&arg_array2)[5]) noexcept
    {
        int8_t* ptr;
        int8_t  array[5];

        // arg_array0、arg_array1の型は、int8_t*
        // 従って、sizeof(arg_array0)の値は、sizeof(int8_t) * 5ではなく、sizeof(int8_t*)である

        // 64bit環境でコンパイルポインタサイズは8バイト
        static_assert(8 == sizeof(arg_array0), "arg_array0 is a pointer but an array");
        static_assert(8 == sizeof(arg_array1), "arg_array1 is a pointer but an array");
        static_assert(5 == sizeof(arg_array2), "arg_array2 is an array");
        static_assert(8 == sizeof(ptr), "ptr must be 8 bytes on 64bit environment");
        static_assert(5 == sizeof(array), "int8_t[5] is 5 bytes");
    }
```

* [演習-sizeof](exercise_q.md#SS_19_5_3)  

### 3.5.8 ポインタ間の演算 <a id="SS_3_5_8"></a>
* 同一オブジェクト(配列等)の要素を指さないポインタ間の除算や比較をしない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 363

    int8_t  a0[5];
    int8_t  a1[5];
    int8_t* end0{&a0[5]};
    int8_t* end1{&a1[5]};

    for (int8_t* curr{a0}; curr < end0;  // OK currもend0もa0のどこかを指している
         ++curr) {
        *curr = 0;
    }

    for (int8_t* curr{a0}; curr < end1;  // NG currとend1は別々のオブジェクトを指している
         ++curr) {
        *curr = 0;
    }
```

### 3.5.9 RTTI <a id="SS_3_5_9"></a>
* [注意] [RAII(scoped guard)](design_pattern.md#SS_9_9)との混乱に気を付ける。
* [Run-time Type Information](term_explanation.md#SS_18_10_16)を使用したラインタイム時の型による場合分けは、
  それ以外に解決方法がない場合や、実装が大幅にシンプルになる場合を除き行わない
  (「[等価性のセマンティクス](term_explanation.md#SS_18_8_1)」参照)。
    * 単体テストやロギングのでtypeidの使用は問題ない。
    * 派生クラスの型によって異なる動作にしたい場合には、仮想関数を使うか、
      [Visitor](design_pattern.md#SS_9_20)パターン等により実現できる。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 383

    class Base {
    public:
        virtual ~Base() = default;
        ...
    };

    class Derived_0 : public Base {
        ...
    };

    class Derived_1 : public Base {
        ...
    };

    ...

    // NGの例
    void b_do_something(Base const& b) noexcept
    {
        auto name = std::string_view{typeid(b).name()};

        // bの実際の型を使った場合分けによる最悪のコード
        // dynamic_castによる場合分けも、下記のコードより大きく改善するわけではない
        if (name == "4Base") {  // マングリングされたBase
            ...
        }
        else if (name == "9Derived_0") {  // マングリングされたDerived_0
            ...
        }
        else if (name == "9Derived_1") {  // マングリングされたDerived_1
            ...
        }
        else {
            assert(false);
        }
    }
```

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 471

    // OKの例
    // 上記のb_do_somethingにポリモーフィズムを適用しリファクタリング
    class Base {
    public:
        void DoSomething() noexcept { do_something(); }
        ...
    private:
        virtual void do_something() noexcept
        {
            ...
        }
    };

    class Derived_0 : public Base {
    private:
        virtual void do_something() noexcept override
        {
            ...
        }
        ...
    };

    class Derived_1 : public Base {
    public:
        virtual void do_something() noexcept override
        {
            ...
        }
        ...
    };

    // virtual Base::do_something()により醜悪なswitchが消えた
    void b_do_something(Base& b) noexcept { b.DoSomething(); }
```

* コンストラクタやデストラクタ内でRTTIの機能を使わない
  (「[コンストラクタ](programming_convention.md#SS_3_3_2_2)」、「[デストラクタ](programming_convention.md#SS_3_3_2_6)」参照)

* [演習-dynamic_castの削除](exercise_q.md#SS_19_5_4)  

### 3.5.10 キャスト、暗黙の型変換 <a id="SS_3_5_10"></a>
* キャストが必要な式等は、設計レベルの問題を内包していることがほとんどであるため、設計を見直す。
* Cタイプキャストは使用しない。
* const_cast、 dynamic_castはそれ以外に解決方法がない場合や、
  実装が大幅にシンプルになる場合を除き使用しない。
* reinterpret_castはハードウエアレジスタ等のアドレスを表す目的以外で使用しない。
* ダウンキャストを行う目的でstatic_castを使用しない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 524
    class Base {
        ...
    };

    class Derived : public Base {
        ...
    };

    void f() noexcept
    {
        auto  d     = Derived{};
        Base* b_ptr = &d;  // ここまでは良い

        auto d_ptr = static_cast<Derived*>(b_ptr);  // ダウンキャスト、動作保証はない

    }
```

* strnlenや、memcpyのような例を除き、void\*への暗黙の型変換を行わない
  (これをすると、後にダウンキャストが必要になる)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 548

    class A {
    public:
        A() : str_{std::make_unique<std::string>("sample")}
        {
            ...
        }

        ~A()
        {
            ...
        }

    private:
        std::unique_ptr<std::string> str_;  // ~unique_ptr()は~A()から呼ばれる
    };

    class B;
```

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 576

    void* v = new A;  // 暗黙の型変換
                      // これ自体は問題ないが、vをdeleteすると
                      // A::~A()が呼び出されないためメモリリークする

    B* b = static_cast<B*>(v);  // ダウンキャストの一種で、極めて悪質なことが多い
                                // 実際、このコードの中にクラスBの定義はないが
                                // このようなことができてしまう

    delete v;          // このdeleleは、A::~A()を呼び出さない
```

* strnlenや、memcpyのような例を除き、配列からポインタへの暗黙の型変換をしない。
  配列を関数の仮引数にしたい場合は、配列へのリファレンスを使う。
  これにより、その関数内でも配列の長さが使用できる
  (「[実引数/仮引数](programming_convention.md#SS_3_3_3_5)」、
  「[sizeof](programming_convention.md#SS_3_5_7)」、「[関数型マクロ](programming_convention.md#SS_3_6_1)」参照)。

* [演習-キャスト](exercise_q.md#SS_19_5_5)  

## 3.6 プリプロセッサ命令 <a id="SS_3_6"></a>
* ソースコードの可読性劣化や単体テストの阻害要因となるため、.cpp内での#if/#ifdef等を使用しない。

```cpp
    // @@@ example/programming_convention/preprocessor_ut.cpp 14

    bool f() noexcept
    {
    #ifdef DEBUG  // NG
        std::cout << __func__ << ":" << __LINE__ << std::endl;
    #endif

        ...

    #if 0  // NG
        return true;
    #else  // NG
        return false;
    #endif
    }

    // やむを得ず条件付きコンパイルが必要な場合、下記のように書き、関数ブロックの中に
    // #ifdefは書かない。

    #ifdef DEBUG
    #define DEBUG_COUT() std::cout << __func__ << ":" << __LINE__ << std::endl
    #else
    #define DEBUG_COUT()
    #endif

    bool g() noexcept
    {
        DEBUG_COUT();

        ...

        return false;
    }

```

* ヘッダファイル内での#if/#ifdef/#ifndefに関しては、以下の用途以外では使わない。
    * 二重インクルードガード(「[二重読み込みの防御](programming_convention.md#SS_3_7_4)」参照)
    * Cとシェアするヘッダファイルでの下記例


```cpp
    // @@@ example/programming_convention/preprocessor.h 3

    #ifdef __cplusplus
    extern "C" {
    #endif  // __cplusplus

    extern bool func_shared_c();

    #ifdef __cplusplus
    }
    #endif  // __cplusplus
```

* ##によるシンボルの生成を使用しない。

```cpp
    // @@@ example/programming_convention/preprocessor_ut.cpp 53

    #define GEN_SYMBOL(x_, y_) x_##y_

    int32_t h() noexcept
    {
        int32_t GEN_SYMBOL(a, b);  // int ab;と同じ

        ab = 3;

        return ab;
    }
```

* 出荷仕向け等の理由から、やむを得ずプリプロセッサ命令を使わざるを得ない場合、
  #if等で囲まれて区間をなるべく短くする。
  これによりより多くのコードがコンパイルされるようにできる
  (「[using宣言/usingディレクティブ](programming_convention.md#SS_3_8_3)」参照)。

```cpp
    // @@@ example/programming_convention/preprocessor_ut.cpp 72
    //
    // ヘッダファイルでの宣言(NGのパターン)
    //

    enum class ShippingRegions { Japan, US, EU };

    struct ShippingData {
        // 何らかの宣言
    };

    void ShippingDoSomething(ShippingData const& region_data);

    #if defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // NG

    constexpr ShippingRegions shipping_region = ShippingRegions::Japan;

    ShippingData const region_data{
        // 何らかのデータ
    };

    #elif !defined(SHIP_TO_JAPAN) && defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // NG

    constexpr ShippingRegions shipping_region = ShippingRegions::US;
    ShippingData const region_data{
        // 何らかのデータ
    };

    #elif !defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && defined(SHIP_TO_EU)  // NG

    constexpr ShippingRegions shipping_region = ShippingRegions::EU;
    ShippingData const        region_data{
        // 何らかのデータ
    };

    #else
    static_assert(false, "SHIP_TO_JAPAN/US/EU must be defined");
    #endif

    //
    // .cppファイルでの定義(NGのパターン)
    //
    void ShippingDoSomething(ShippingData const& region_data)
    {
    #if defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // NG
        // 何らかの処理
    #elif !defined(SHIP_TO_JAPAN) && defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // NG
        // 何らかの処理
    #elif !defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && defined(SHIP_TO_EU)  // NG
        // 何らかの処理
    #else
        static_assert(false, "SHIP_TO_JAPAN/US/EU must be defined");
    #endif
    }
```
```cpp
    // @@@ example/programming_convention/preprocessor_ut.cpp 140
    //
    // ヘッダファイルでの宣言(OKのパターン)
    //

    enum class ShippingRegions { Japan, US, EU };

    struct ShippingData {
        // 何らかの宣言
    };
    void ShippingDoSomething(ShippingData const& region_data);

    extern ShippingData const& region_data;

    #if defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // OK

    constexpr ShippingRegions shipping_region = ShippingRegions::Japan;

    #elif !defined(SHIP_TO_JAPAN) && defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // OK

    constexpr ShippingRegions shipping_region = ShippingRegions::US;

    #elif !defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && defined(SHIP_TO_EU)  // OK

    constexpr ShippingRegions shipping_region = ShippingRegions::EU;

    #else
    static_assert(false, "SHIP_TO_JAPAN/US/EU must be defined");
    #endif

    //
    // .cppファイルでの定義(OKのパターン、以下にはプリプロセッサ命令は出てこない)
    //

    void ShippingDoSomething(ShippingData const& region_data)
    {
        if constexpr (shipping_region == ShippingRegions::Japan) {
            // 何らかの処理
        }
        else if constexpr (shipping_region == ShippingRegions::US) {
            // 何らかの処理
        }
        else if constexpr (shipping_region == ShippingRegions::EU) {
            // 何らかの処理
        }
        else {
            static_assert(shipping_region == ShippingRegions::Japan
                          || shipping_region == ShippingRegions::US
                          || shipping_region == ShippingRegions::EU);
        }
    }

    template <ShippingRegions sr>
    ShippingData const& gen_shipping_data()
    {
        if constexpr (sr == ShippingRegions::Japan) {
            static ShippingData const region_data{
                // 何らかのデータ
            };
            return region_data;
        }
        else if constexpr (sr == ShippingRegions::US) {
            static ShippingData const region_data{
                // 何らかのデータ
            };
            return region_data;
        }
        else if constexpr (sr == ShippingRegions::EU) {
            static ShippingData const region_data{
                // 何らかのデータ
            };
            return region_data;
        }
        else {
            static_assert(sr == ShippingRegions::Japan || sr == ShippingRegions::US
                          || sr == ShippingRegions::EU);
        }
    }

    ShippingData const& region_data = gen_shipping_data<shipping_region>();
```


### 3.6.1 関数型マクロ <a id="SS_3_6_1"></a>
* 関数型マクロ以外に方法がない場合を除き、関数型マクロを定義しない。
  その代わりに関数テンプレートを定義する。こうすることで下記のような誤用を防ぐことができる。

```cpp
    // @@@ example/programming_convention/preprocessor_ut.cpp 242

    #define ARRAY_LENGTH(array_) (sizeof(array_) / sizeof(array_[0]))  // NG

    template <typename T, size_t N>  // OK
    constexpr size_t array_length(T const (&)[N]) noexcept
    {
        return N;
    }

    // arrayは配列へのリファレンスだが関数中では配列
    size_t f0(bool use_macro, int32_t (&array)[5]) noexcept
    {
        if (use_macro) {
            return ARRAY_LENGTH(array);  // この場合は、関数型マクロでも正しく処理できるが好ましくない
        }
        else {
            return array_length(array);  // OK
        }
    }

    // fake_arrayは配列に見えるが実際にはポインタ
    size_t f1(bool use_macro, int32_t fake_array[5]) noexcept
    {
        if (use_macro) {
            return ARRAY_LENGTH(fake_array);  // NG 誤用でもコンパイルできてしまい不正値を返す
        }
        else {
            // return  array_length(fake_array); // OK 誤用のためコンパイルエラー
            auto array = reinterpret_cast<int32_t(*)[5]>(fake_array);  // 無理やりコンパイル
            return array_length(*array);
        }
    }
```

* 関数型マクロの中に文がある場合、do-while(0)イデオムを使用する
  (「[マクロの中の文](programming_convention.md#SS_3_4_9)」参照)。

### 3.6.2 マクロ定数 <a id="SS_3_6_2"></a>
* マクロ定数以外に方法がない場合を除き、マクロ定数を定義しない。
  その代わりにconstexpr uint32\_t等や、enumを定義する。

```cpp
    // @@@ example/programming_convention/preprocessor_ut.cpp 293

    #define XXX_LENGHT 5  // NG

    constexpr uint32_t YyyLenght{5};  // OK

    #define XXX_TYPE_A 0  // NG
    #define XXX_TYPE_B 1  // NG
    #define XXX_TYPE_C 2  // NG

    enum class XxxType {  // OK
        A = 0,            //      Aの値が必要だと前提
        B,
        C
    };
```

## 3.7 パッケージとその構成ファイル <a id="SS_3_7"></a>

### 3.7.1 パッケージの実装と公開 <a id="SS_3_7_1"></a>
* パッケージに関して、以下の構造を持つようにソースコードを構成する
  (「[アーキテクチャとファイル構造](architecture.md#SS_10_3)」参照)。
    * ソフトウェアはパッケージに分割される。
    * パッケージは、複数のヘッダファイルと複数の.cppファイルから作られる。
    * パッケージを構成するファイルは、このパッケージ専用ディレクトリに保存される。
    * パッケージは他のパッケージとは排他的な[名前空間](programming_convention.md#SS_3_8_2)を持ち、
      パッケージ内で宣言、定義され、外部パッケージに公開される修飾子はその名前空間に包含される。
      外部パッケージに公開されない修飾子は、そのパッケージでのみ使用される名前空間か、
      無名名前空間に包含されるようにする。
    * パッケージは、サブパッケージを内包する場合がある。
      サブパッケージは、パッケージの要件を満たす。

* 上記前提のもと、パッケージが外部にサービスを提供する場合、
  そのパッケージで定義されるヘッダファイルは以下のどちらかのみを行うように構成する。
    * 外部へ提供するクラス等を公開する(外部公開ヘッダファイル)。
    * パッケージ内部のみで使用するクラス等の宣言、定義を行う(外部非公開ヘッダファイル)。

<p><img src="data:image/png;base64,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" /></p>

* 外部公開ヘッダファイルは、ビルド時に他のパッケージから参照できるディレクトリに配置する。
    * 外部公開ヘッダファイルは、外部非公開ヘッダファイルをインクルードしない。
    * 外部非公開ヘッダファイルは、ビルド時に他のパッケージから参照できるディレクトリに配置しない。

### 3.7.2 識別子の宣言、定義 <a id="SS_3_7_2"></a>
* [ODR](https://en.cppreference.com/w/cpp/language/definition)を守る。
  つまり、一つの識別子は全ソースコード内にただ一つの定義を持つようにする。
* 一つの.cppファイル内のみで使用される識別子は、
  その.cppファイル内の無名名前空間にその定義や宣言を持つ。
* ヘッダファイルで宣言された識別子が.cppファイル内に定義をもつ場合、
  その.cppファイルにそのヘッダファイルをインクルードさせる。
  特に、非メンバ関数や変数の宣言と定義を矛盾させないために、このルールは特に重要である
  (「[非メンバ関数](programming_convention.md#SS_3_3_1)」参照)。

### 3.7.3 依存関係 <a id="SS_3_7_3"></a>
* 不要/不適切な依存関係(「[インターフェース分離の原則(ISP)](solid.md#SS_8_4)」や
  「[依存関係逆転の原則(DIP)](solid.md#SS_8_5)」への違反)を作らない。
    * 依存関係を最小にとどめるために、前方宣言を適切に使用する。
        * STLクラス(やクラスのエイリアス)の前方宣言をしない
          (例えば、「std::stringをクラス宣言することでstringヘッダファイルへの依存関係を作らない」
          といった方法は、std::stringがクラスでないため想定通りに働かない)。
    * SOLIDの原則やデザインパターン、イデオム等を適切に使用することにより、依存関係を適切に保つ。
        * 依存関係の伝搬を回避したい場合、[Pimpl](design_pattern.md#SS_9_3)イデオムを使い実装の詳細を隠蔽する。
        * 上位概念が下位概念に依存することを避ける場合、
          「[依存関係逆転の原則(DIP)](solid.md#SS_8_5)」での例や[Observer](design_pattern.md#SS_9_22)等を適用する。
    * パッケージ間の相互、循環依存関係を作らない。

<p><img src="data:image/png;base64,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" /></p>

### 3.7.4 二重読み込みの防御 <a id="SS_3_7_4"></a>
* 二重インクルードを防ぐため、 ヘッダファイルには#includeガードを付ける。
  ガード用のマクロは、<パス名>\_<ファイル名>\_H\_とする。

```cpp
    // @@@ example/programming_convention/lib/inc/xxx.h 1

    // lib/inc/xxx.hでの#includeガード

    #ifndef LIB_INC_XXX_H_
    #define LIB_INC_XXX_H_

    extern void XxxInitialize();

    ...

    #endif  // LIB_INC_XXX_H_
```

* コンパイラが#pragma onceをサポートしている場合は、
  上記方法ではなく下記をヘッダファイル先頭に記述する。

```cpp
    // @@@ example/programming_convention/lib/inc/xxx.h 16

    #pragma once
```

### 3.7.5 ヘッダファイル内の#include <a id="SS_3_7_5"></a>
* 不要な依存関係を作らないようにするため、
  ヘッダファイルは、そのコンパイルに不要なヘッダファイルをインクルードしない。
* ヘッダファイルが外部からインポートする型(class、struct、enum)
  のデリファレンスがそのヘッダファイル内で不要な場合、前方宣言を使い依存関係を小さくする。 

```cpp
    // @@@ example/programming_convention/header.h 3

    // Pod0, Pod1の定義は別ファイルでされていると前提。
    struct Pod0;
    struct Pod1;

    // 下記関数宣言のコンパイルには、Pod0、Pod1の完全な定義は必要ない。
    extern void forward_decl(Pod0 const* pod_0, Pod1* pod_1) noexcept;
    extern Pod1 forward_decl(Pod0 const* pod_0) noexcept;
    extern void forward_decl(Pod0 pod_0) noexcept;
```

```cpp
    // @@@ example/programming_convention/header_ut.cpp 12

    // Pod0, Pod1の定義がなくても宣言があるためコンパイルできる
    forward_decl(nullptr, nullptr);

    // 下記のソースコードのコンパイルには、Pod0の定義が必要なのでコンパイルできない
    // forward_decl(nullptr);
```

### 3.7.6 #includeするファイルの順番 <a id="SS_3_7_6"></a>
* ユーザ定義ヘッダファイルより、システムヘッダファイルの#includeを先に行う。
* システムヘッダファイルは、アルファベット順に#includeを行う。
* ユーザ定義ヘッダファイルは、アルファベット順に#includeを行う。

### 3.7.7 #includeで指定するパス名 <a id="SS_3_7_7"></a>
* ユーザ定義のヘッダファイルは""で囲み、システムヘッダファイルは、<>で囲む。
* 他のパッケージの外部非公開ヘッダファイルを読み込まないようにするために、
  #includeのパス指定に"../"(ディレクトリ上方向への移動)を使用しない。

```cpp
    // @@@ example/programming_convention/lib/header.cpp 1

    #include <string>  // OK

    #include "../h/suppress_warning.h"  // NG   上方向へのファイルパスは禁止

    #include "../header.h"  // NG   上方向へのファイルパスは禁止
    #include "inc/xxx.h"    // OK
```

* ヘッダファイル以外のファイル(.cppファイル等)をインクルードしない。

## 3.8 スコープ <a id="SS_3_8"></a>
### 3.8.1 スコープの定義と原則 <a id="SS_3_8_1"></a>
この章で扱うスコープを下記のように定義する(「[パッケージの実装と公開](programming_convention.md#SS_3_7_1)」参照)。

1. グローバル
2. パッケージ外部公開名前空間
3. パッケージ外部非公開名前空間
4. ファイル(無名名前空間と関数外static)
5. クラス内
6. 関数内
7. ブロック内

リンクの観点からは、2と3の識別子は同じスコープを持つが、
その識別子はパッケージ外部非公開なヘッダファイルに宣言、定義されているため、
パッケージ外から(まともな方法では)アクセスできない。

* 識別子のスコープは最小になるように配置する。
    * 1のスコープを持つ識別子を宣言しない(特にグローバルなスコープ内のオブジェクトは定義しない)。
    * 2、3のスコープを持つ静的な変数を宣言しない。
    * パッケージ外部公開ヘッダファイルでの識別子の宣言、定義を最小にする。
    * クラス内部でのみ使用される識別子は、privateもしくはprotectedで宣言する。
    * 一つの.cppファイルのみで使用する識別子は、
      その.cppファイル内の無名名前空間で宣言、定義する(staticを使用しない)。
    * 単一関数のみで使用する変数は、その関数内で定義する。
    * 自動変数は、使用直前に定義する。

* スコープが重複する「名前のない名前空間内」(例えば、ブロックとそれを内包するブロック)
  にある「同一名を持つ識別子」を宣言、定義しない(「[name-hiding](term_explanation.md#SS_18_4_8)」参照)。

```cpp
    // @@@ example/programming_convention/scope.h 7

    extern uint32_t xxx;  // NG 外部から参照可能な静的変数
    extern uint64_t yyy;  // NG 同上
```

```cpp
    // @@@ example/programming_convention/scope_ut.cpp 18

    uint32_t xxx;  // NG 外部から参照可能な静的変数
    uint32_t yyy;  // NG 同上

    uint32_t f(uint32_t yyy) noexcept
    {
        auto xxx = 0;  // NG 関数外xxxと関数内xxxのスコープが重なっており区別が付きづらい

        return xxx + yyy;
    }
    // なお、
    //  scope.h内では、  uint64_t yyy;
    //  scope.cpp内では、uint32_t yyy;
    //  となっており、宣言と定義が矛盾している。
    //  この問題は、このファイルからscope.hをインクルードすれば防げる。
```

### 3.8.2 名前空間 <a id="SS_3_8_2"></a>
* グローバル名前空間には下記以外の識別子を定義、宣言しない。
    * main関数
    * グローバルnewのオーバーロード
    * Cとシェアする識別子
* パッケージ毎に名前空間を定義する
  (「[パッケージの実装と公開](programming_convention.md#SS_3_7_1)」、[名前空間名](naming_practice.md#SS_6_3_8)」参照)。
* 外部リンケージの不要な識別子は.cpp内の無名名前空間で宣言、定義する。
* 名前空間Xxx内で定義されたテンプレートやinline関数から参照されるため、
  外部公開用ではないにもかかわらずヘッダファイル内に定義が必要な識別子は、
  名前空間Xxx::Inner\_内で定義する。
  名前空間Xxx::Inner\_内の識別子は、単体テストを除き他のファイルから参照しない。

```cpp
    // @@@ example/programming_convention/scope2.h 9

    template <size_t N>
    class StaticString {  // StaticStringは外部公開
        ...
    };

    namespace Inner_ {  // equal_nは外部非公開
    template <size_t N>
    constexpr bool equal_n(size_t n, StaticString<N> const& lhs, StaticString<N> const& rhs) noexcept
    {
        if (n == N) {
            return true;
        }
        else {
            return lhs.String()[n] != rhs.String()[n] ? false : equal_n(n + 1, lhs, rhs);
        }
    }
    }  // namespace Inner_

    template <size_t N1, size_t N2>  // operator==は外部公開
    constexpr bool operator==(StaticString<N1> const&, StaticString<N2> const&) noexcept
    {
        return false;
    }

    template <size_t N>  // operator==は外部公開
    constexpr bool operator==(StaticString<N> const& lhs, StaticString<N> const& rhs) noexcept
    {
        return Inner_::equal_n(0, lhs, rhs);
    }
```

### 3.8.3 using宣言/usingディレクティブ <a id="SS_3_8_3"></a>
* 識別子のインポートのための[using宣言](term_explanation.md#SS_18_4_13)は下記のような場合のみに使用する
  (「[継承コンストラクタ](term_explanation.md#SS_18_2_3)」、「[オーバーライドとオーバーロードの違い](term_explanation.md#SS_18_10_1)」参照)。

```cpp
    // @@@ example/programming_convention/scope_ut.cpp 55

    using std::string;  // NG この関数内でのstd::stringの使用箇所が少ないのであれば、
                        //    using宣言ではなく、名前修飾する
    auto s_0 = string{"str"};       // NG
    auto s_1 = std::string{"str"};  // OK

    // 大量のstd::stringリテラルを使用する場合
    using std::literals::string_literals::operator""s;  // OK

    auto s_2 = "str"s;  // OK
    // ...
    auto s_N = "str"s;  // OK

    // クラス内でのusing宣言
    struct Base {
        void f(){};
    };

    struct Derived : Base {
        using Base::Base;  // OK 継承コンストラクタ
        using Base::f;     // OK B::fのインポート
        void f(int){};
    };
```

* 下記のような場合を除き、[usingディレクティブ](term_explanation.md#SS_18_4_14)は使用しない。

```cpp
    // @@@ example/programming_convention/scope_ut.cpp 84

    using namespace std;  // NG

    auto s0 = string{"str"};

    auto s1 = std::literals::string_literals::operator""s("str", 3);  // NG
    static_assert(std::is_same_v<std::string, decltype(s1)>);

    using namespace std::literals::string_literals;  // OK 例外的にOK

    auto s2 = "str"s;
    static_assert(std::is_same_v<std::string, decltype(s2)>);
```

* 出荷仕向け等の理由を除き、inline namespaceを使用しない(「[プリプロセッサ命令](programming_convention.md#SS_3_6)」参照)。

```cpp
    // @@@ example/programming_convention/scope_ut.cpp 106

    namespace XxxLib {
    namespace OldVersion {
    int32_t f() noexcept
    {
        ...
    }
    }  // namespace OldVersion

    inline namespace NewVersion {  // NG inline
    int32_t f() noexcept
    {
        ...
    }
    }  // namespace NewVersion

    int32_t g() noexcept
    {
        return f();  // NG NewVersion::f()が呼ばれる。
    }
```
```cpp
    // @@@ example/programming_convention/scope_ut.cpp 141
    // 例外的にOKな例

    #if defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // OK
    #define INLINE_JAPAN inline                                                 // OK
    #define INLINE_US
    #define INLINE_EU

    #elif !defined(SHIP_TO_JAPAN) && defined(SHIP_TO_US) && !defined(SHIP_TO_EU)  // OK
    #define INLINE_JAPAN
    #define INLINE_US inline  // OK
    #define INLINE_EU

    #elif !defined(SHIP_TO_JAPAN) && !defined(SHIP_TO_US) && defined(SHIP_TO_EU)  // OK
    #define INLINE_JAPAN
    #define INLINE_US
    #define INLINE_EU inline  // OK

    #else
    static_assert(false, "SHIP_TO_JAPAN/US/EU must be defined");
    #endif

    namespace Shipping {
    INLINE_JAPAN namespace Japan  // OK
    {
        int32_t DoSomething() { return 0; }
    }

    INLINE_US namespace US  // OK
    {
        int32_t DoSomething() { return 1; }
    }

    INLINE_EU namespace EU  // OK
    {
        int32_t DoSomething() { return 2; }
    }
    }  // namespace Shipping
```
```cpp
    // @@@ example/programming_convention/scope_ut.cpp 183

    // SHIP_TO_JAPAN/US/EUを切り替えることで、対応したDoSomethingが呼ばれる
    // この例ではSHIP_TO_JAPANが定義されているため、Shipping::Japan::DoSomethingが呼ばれる
    ASSERT_EQ(0, Shipping::DoSomething());

    // 名前修飾することで、すべてのDoSomethingにアクセスできるため、単体テストも容易
    ASSERT_EQ(0, Shipping::Japan::DoSomething());
    ASSERT_EQ(1, Shipping::US::DoSomething());
    ASSERT_EQ(2, Shipping::EU::DoSomething());
```

* [演習-usingディレクティブ](exercise_q.md#SS_19_6_1)  

### 3.8.4 ADLと名前空間による修飾の省略 <a id="SS_3_8_4"></a>
* 名前空間の修飾を省略した識別子のアクセスには、
  下記のような副作用があるため、[ADL](term_explanation.md#SS_18_4_5)を使用する目的以外で使用しない
  (「[識別子の命名](naming_practice.md#SS_6_3)」を順守することで、識別子の偶然の一致を避けることも必要)。

```cpp
    // @@@ example/programming_convention/scope_ut.cpp 200

    namespace NS_0 {
    class X {};

    std::string f(X, int32_t)  // 第2引数int32_t
    {
        return "in NS_0";
    }
    }  // namespace NS_0

    namespace NS_1 {

    std::string f(NS_0::X, uint32_t)  // 第2引数uint32_t
    {
        return "in NS_1";
    }

    TEST(ProgrammingConvention, adl)
    {
        // in NS_1
        // 下記関数fの探索名前空間には、
        //  * 第1引数の名前空間がNS_0であるため、ADLにより、
        //  * この関数の宣言がNS_1で行われているため、
        // NS_0、NS_1が含まれる。
        // これにより、下記fの候補は、NS_0::f、NS_1::fになるが、第2引数1がint32_t型であるため、
        // 下記は、NS_0::fの呼び出しになる。

        ASSERT_EQ("in NS_0", f(NS_0::X(), 1));  // NS_0::fが呼ばれる。

        ASSERT_EQ("in NS_1", NS_1::f(NS_0::X(), 1));  // NS_1::fの呼び出しには名前修飾が必要
    }
    }  // namespace NS_1
```


### 3.8.5 名前空間のエイリアス <a id="SS_3_8_5"></a>
* ネストされた長い名前空間を短く簡潔に書くための名前空間エイリアスは、関数スコープで宣言する。
* 名前空間のエイリアスを[using宣言/usingディレクティブ](programming_convention.md#SS_3_8_3)で使用しない。

```cpp
    // @@@ example/programming_convention/scope_ut.cpp 238

    std::vector<std::string> find_files_recursively(
        std::string const& path, std::function<bool(std::filesystem::path const&)> condition)
    {
        namespace fs = std::filesystem;  // OK 長い名前を短く

        auto files  = std::vector<std::string>{};
        auto parent = fs::path{path.c_str()};

        using namespace fs;  // NG エイリアスをusing namespaceで使用しない

        std::for_each(fs::recursive_directory_iterator{parent},  // OK namespaceエイリアス
                      fs::recursive_directory_iterator{},        // OK namespaceエイリアス
                      ...
        );

        using fs::recursive_directory_iterator;  // NG エイリアスをusing宣言で使用しない

        std::for_each(recursive_directory_iterator{parent},  // NG
                      recursive_directory_iterator{},        // NG
                      ...
        );

        return files;
    }
```

## 3.9 ランタイムの効率 <a id="SS_3_9"></a>
* ランタイム効率と、可読性のトレードオフが発生する場合、可読性を優先させる。
* やむを得ず可読性を落とすコードオプティマイゼーションを行う場合は、
  プロファイリング等を行い、ボトルネックを確定させ、必要最低限に留める。
  また、開発早期での可読性を落とすコードオプティマイゼーションは行わない。

### 3.9.1 前置/後置演算子の選択 <a id="SS_3_9_1"></a>
* 後置演算子の一般的な動作は、下記のようになるため前置演算子の実行に比べて処理が多い。
  どちらを使用してもよい場合は前置演算子を使う。
    1. 自分(オブジェクト)をコピーする。
    2. 自分に前置演算子を実行する。
    3. コピーされたオブジェクトを返す。

```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 14

    class A {
    public:
        A& operator++() noexcept  // 前置++
        {
            ++a_;  // メンバ変数のインクリメント
            return *this;
        }

        A operator++(int) noexcept  // 後置++
        {
            A old{*this};  // リターンするためのオブジェクト
            ++(*this);     // 前置++
            return old;    // oldオブジェクトのリターン(オブジェクトのコピー)
        }

        operator int() const noexcept { return a_; }

    private:
        int32_t a_{0};
    };
```
```cpp
    // @@@ example/h/measure_performance.h 4

    // パフォーマンス測定用
    template <typename FUNC>
    std::chrono::milliseconds MeasurePerformance(uint32_t count, FUNC f)
    {
        auto const start = std::chrono::system_clock::now();

        for (auto i = 0U; i < count; ++i) {
            f();
        }

        auto const stop = std::chrono::system_clock::now();

        return std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    }
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 41

    constexpr auto count = 10000000U;

    auto a_post = A{};
    auto post   = MeasurePerformance(count, [&a_post] {
        a_post++;  // NG 効率が悪い。
    });

    auto a_pre = A{};
    auto pre   = MeasurePerformance(count, [&a_pre] {
        ++a_pre;  // OK 上記に比べると効率が良い。
    });

    ASSERT_GT(post, pre);  // 前置++の処理は後置++より効率が良い。
```

* ソースコードの統一性のため、このオーバーヘッドがない基本型についても、同じルールを適用する。

### 3.9.2 operator X、operator x=の選択 <a id="SS_3_9_2"></a>
* 前置/後置演算子と同じような問題が発生するため、どちらを使っても問題ない場合は、
  operator Xではなく、operator X=を使う。

```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 68

    class A {
    public:
        explicit A(int32_t a) noexcept : a_{a} {}

        A& operator+=(A const& rhs) noexcept
        {
            a_ += rhs.a_;
            return *this;
        }
        ...
        friend A operator+(A const& lhs, A const& rhs) noexcept  // メンバ関数に見えるが、非メンバ関数
        {
            A tmp{lhs};  // operator +=に対して、
            tmp += rhs;  // 「tmpを作り、それを返す]をしなければならない。
            return tmp;
        }
    };

    void f() noexcept
    {
        auto a = A{1};
        auto b = A{2};

        a = a + b;                                   // NG 無駄な動作が多い。
        std::cout << "a:" << a.GetA() << std::endl;  // a:3と表示

        a += b;                                      // OK
        std::cout << "a:" << a.GetA() << std::endl;  // a:5と表示
    }
```

* ソースコードの統一性のため、このオーバーヘッドがない基本型についても、同じルー ルを適用する。

### 3.9.3 関数の戻り値オブジェクト <a id="SS_3_9_3"></a>
* 基本型やenum、
  std::unique_ptr<>、std::optional<>
  等のサイズの小さいクラス以外のオブジェクトを関数の戻り値にしない。
* [注意] ローカルオブジェクトに対して[RVO(Return Value Optimization)](term_explanation.md#SS_18_10_12)が有効であれば、
  そのオブジェクトを戻り値にしても良い。
* [注意] stdのコンテナは、RVOが有効でなくてもmoveが行われるため、関数の戻り値として使用しても良い。
* [注意] std::stringについては、RVOに加えて、
  [SSO(Small String Optimization)](term_explanation.md#SS_18_10_13)が使用されていることが多い。
  そのようなコンパイラを使用している場合、std::stringは小さいオブジェクトとして扱って良い。

```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 115

    struct HugeClass {
        int32_t a{0};
        int32_t array[100000]{};
    };

    HugeClass f() noexcept  // NG 巨大なオブジェクトのリターン
    {
        auto obj = HugeClass{};

        ...

        return obj;  // RVOが使えない場合パフォーマンス問題を引き起こす可能性がある。
    }

    class A {
    public:
        // RVO、SSOをサポートしているコンパイラを使用している場合、下記の2つのGetNameの
        // パフォーマンスに大差はない(ほとんどのC++コンパイラはRVO、SSOをサポートしている)。
        // 使い勝手は、std::string GetName()の方が良い。
        static std::string GetName()  // OK この程度なら問題はない
        {
            return "sample";
        }

        static void GetName(std::string& s)  // OK
        {
            s = "sample";
        }
    };
```

### 3.9.4 move処理 <a id="SS_3_9_4"></a>
* [ディープコピー](term_explanation.md#SS_18_3_2)の実装を持つクラスへのcopy代入の多くがrvalueから行われるのであれば、
  moveコンストラクタや、move代入演算子も実装する。
* 関数の戻り値にローカルオブジェクトを使用する場合、
  [RVO(Return Value Optimization)](term_explanation.md#SS_18_10_12)の阻害になるため、そのオブジェクトをstd::moveしない。

```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 150

    std::string MakeString(int a, int b)
    {
        auto ret = std::string{};

        ...
        // 文字列操作
        ...

    #if 0
        // NG
        // std::moveのため、RVOが抑止される。
        // -Wpessimizing-moveを指定してg++/clang++でコンパイルすれば、
        // "moving a local object in a return statement prevents copy elision"
        // という警告が出る。

        return std::move(ret);
    #else
        // OK
        // ローカルオブジェクトには通常RVOが行われるため、std::moveするよりも無駄が少ない。

        return ret;
    #endif
    }
```

### 3.9.5 std::string vs std::string const& vs std::string_view <a id="SS_3_9_5"></a>
* 文字列を受け取る関数の仮引数の型に関しては下記のような観点に気を付ける。
  以下に示す通り、このような仮引数の型をstd::string const&にすることが最適であるとは限らない。

```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 184
    // テスト０用関数

    void f0([[maybe_unused]] std::string const& str) {}
    void f1([[maybe_unused]] std::string str) {}
    void f2([[maybe_unused]] std::string_view str) {}
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 195
    // テスト０―０

    auto str     = std::string{__func__};
    auto f0_msec = MeasurePerformance(10000000, [&str] { f0(str); });
    auto f1_msec = MeasurePerformance(10000000, [&str] { f1(str); });
    auto f2_msec = MeasurePerformance(10000000, [&str] { f2(str); });

    // このドキュメントを開発しているPCでは上記の結果は以下の様になる。
    // f0 : 50 msec
    // f1 :222 msec
    // f2 : 55 msec
    // つまり、f0 < f2 < f1であり、f0とf2は大差がなく、f1は極めて非効率である。
    // 従って、文字列を関数に渡す場合の引数の型は、
    // std::string const&か、std::string_viewとするのが効率的である。
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 219
    // テスト０―１

    auto f0_msec = MeasurePerformance(10000000, [] { f0(__func__); });
    auto f1_msec = MeasurePerformance(10000000, [] { f1(__func__); });
    auto f2_msec = MeasurePerformance(10000000, [] { f2(__func__); });

    // このドキュメントを開発しているPCでは上記の結果は以下の様になる。
    // f0 :674 msec
    // f1 :662 msec
    // f2 :115 msec
    // つまり、f2 < f1 < f0であり、f0、f1は極めて非効率である。
    // 従って、文字列を関数に渡す場合の引数の型は、std::string_viewとするのが効率的である。
    //
    // テスト０―０、テスト０―１の結果から、
    //   * 文字列リテラルからstd::string型テンポラリオブジェクトを作るような呼び出しが多い場合、
    //     std::string_view
    //   * 上記のような呼び出しがほとんどない場合、std::string const&
    // を引数型とすべきである。
    // 使用方法が想定できない場合、極めて非効率なテスト０－１のf0のパターンを避けるため、
    // std::string_viewを選択すべきだろう。
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 248
    // テスト１用クラス

    class A0 {
    public:
        A0(std::string const& str) : str_{str} {}

    private:
        std::string str_;
    };

    class A1 {
    public:
        A1(std::string str) : str_{std::move(str)} {}

    private:
        std::string str_;
    };

    class A2 {
    public:
        A2(std::string_view str) : str_{str} {}

    private:
        std::string str_;
    };
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 303
    // テスト１―１

    auto a0_msec = MeasurePerformance(10000000, [] { A0 a{__func__}; });
    auto a1_msec = MeasurePerformance(10000000, [] { A1 a{__func__}; });
    auto a2_msec = MeasurePerformance(10000000, [] { A2 a{__func__}; });

    // このドキュメントを開発しているPCでは上記の結果は以下の様になる。
    // A0 :834 msec
    // A1 :774 msec
    // A2 :704 msec
    // つまり、A2 < A1 < A0であり、A0の効率がやや悪い。
    // 従って、文字列を関数に渡す場合の引数の型は、
    // std::stringか、std::string_viewとするのが効率的である。
    //
    // コンストラクタのインターフェースとしては、
    // 実引数オブジェクトのライフタイムを考慮しなくて良いため、A0よりもA1の方が優れている。
    // この観点と、テスト１－０、テスト１－１の結果を総合的に考えれば、
    // このような場合の引数の型は、std::stringを選択すべきだろう。
```

### 3.9.6 extern template <a id="SS_3_9_6"></a>
* 何度もインスタンス化が行われ、
  それによりROMの肥大化やビルドの長時間化を引き起こすようなクラステンプレートに対しては、
  extern templateを使う。

```cpp
    // @@@ example/programming_convention/string_vector.h 4

    // このファイルをインクルードすると、
    // そのファイルでのstd::vector<std::string>のインスタンス化は抑止される。
    extern template class std::vector<std::string>;
```
```cpp
    // @@@ example/programming_convention/string_vector.cpp 3

    // std::vector<std::string>はこのファイルでインスタンス化される。
    template class std::vector<std::string>;
```

## 3.10 標準クラス、関数の使用制限 <a id="SS_3_10"></a>
### 3.10.1 STL <a id="SS_3_10_1"></a>
* C++のバージョン毎に定められた非推奨の機能、関数、クラスを使わない。
  これらについては、[C++日本語リファレンス](https://cpprefjp.github.io/)の
  * [C++11の機能変更](https://cpprefjp.github.io/lang/cpp11.html)
  * [C++14の機能変更](https://cpprefjp.github.io/lang/cpp14.html)
  * [C++17の機能変更](https://cpprefjp.github.io/lang/cpp17.html)
  に詳細が書かれている。

* [g++](term_explanation.md#SS_18_9_1)/[clang++](term_explanation.md#SS_18_9_2)等の優れたコンパイラを適切なオプションで使用することで、
  非推奨の機能、関数、クラスの使用を防ぐ。

#### 3.10.1.1 スマートポインタの使用制限 <a id="SS_3_10_1_1"></a>
* std::auto_ptrを使用しない(C++17で廃止)。
* ダイナミックに生成したオブジェクトの管理にはstd::unique_ptr<>を使用する。
  std::unique_ptr<>では機能が足りない場合のみ、std::shared_ptr<>を使用する。

#### 3.10.1.2 配列系コンテナクラスの使用制限 <a id="SS_3_10_1_2"></a>
* 配列系のコンテナを使用する場合、コンパイル時に要素数の上限が
    * 定まるのであれば、std::arrayを使用する。
    * 未定ならば、std::vectorを使用する。
* std::vector\<bool\>は、std::vectorの特殊化であり、通常のstd::vectorと同じようには扱えない。
  std::vector\<bool\>を使用する場合、その要素へのハンドルがbool&やbool\*でないことに注意する。
* std::arrayを除くコンテナクラスは、
  それ自体でメモリリソースの[RAII(scoped guard)](design_pattern.md#SS_9_9)を実現しているため、newしない。

#### 3.10.1.3 std::stringの使用制限 <a id="SS_3_10_1_3"></a>
* std::stringは、
  それ自体でメモリリソースの[RAII(scoped guard)](design_pattern.md#SS_9_9)を実現しているため、newしない。
* std::stringの添字演算子[]は領域外アクセスを通知しない
  ([std::out_of_range](https://cpprefjp.github.io/reference/stdexcept.html)
  エクセプションを発生させない)ため、std::string::at() を使用する
  (「[安全な配列型コンテナ](template_meta_programming.md#SS_13_2_3)」参照)。
* std::string.data()は、C++のバージョンによってはNULLターミネイトが保証されていないため、
  std::string.c_str() を使用する。

#### 3.10.1.4 std::string_viewの使用制限 <a id="SS_3_10_1_4"></a>
* std::string_viewが保持するポインタが指す文字列の所有権は、他のオブジェクトが保持しているため、
  std::string_viewの初期化や、copy代入の右辺にrvalueを使用しない。

```cpp
    // @@@ example/programming_convention/string_view_ut.cpp 11

    auto str = std::string{"abc"};
    auto sv  = std::string_view{str};  // OK lvalueからの初期化

    ASSERT_EQ(sv, std::string_view{"abc"});
```
```cpp
    // @@@ example/programming_convention/string_view_ut.cpp 31

    std::string_view sv = std::string{"abc"};  // NG rvalueからの初期化
                                               //    この行でstd::string{"abc"}が解放
    ASSERT_EQ(sv, std::string_view{"abc"});    //    svは無効なポインタを保持
```

* 文字列リテラルで初期化されたstd::string_viewと文字列リテラルとの微妙な違いに気を付ける。

```cpp
    // @@@ example/programming_convention/string_view_ut.cpp 43

    {  // 文字列リテラルを範囲として使用すると、ヌル文字が要素に含まれる
        auto oss = std::ostringstream{};

        for (char c : "abc") {
            oss << c;
        }

        ASSERT_EQ((std::string{'a', 'b', 'c', '\0'}), oss.str());  // ヌル文字が入る
    }
    {  // string_viewを使用すると、ヌル文字が要素に含まれない
        auto oss = std::ostringstream{};

        for (char c : std::string_view{"abc"}) {
            oss << c;
        }

        ASSERT_EQ((std::string{'a', 'b', 'c'}), oss.str());  // ヌル文字は入らない
    }
```
```cpp
    // @@@ example/programming_convention/string_view_ut.cpp 65

    char const a[]{"123"};
    auto       b = std::string_view{"01234"}.substr(1, 3);  // インデックス1 - 3

    ASSERT_EQ(a, b);  // a == bが成り立つ

    auto oss_a = std::ostringstream{};
    oss_a << a;

    auto oss_b = std::ostringstream{};
    oss_b << b;

    ASSERT_EQ(oss_a.str(), oss_b.str());  // ここまでは予想通り

    // bをインデックスアクセスすると以下のようになる。
    ASSERT_EQ('0', b[-1]); ASSERT_EQ('1', b[0]); ASSERT_EQ('2',  b[1]);
    ASSERT_EQ('3',  b[2]); ASSERT_EQ('4', b[3]); ASSERT_EQ('\0', b[4]);

    // 上記の結果から、以下の結果になることには注意が必要
    auto oss_b_cstr = std::ostringstream{};
    oss_b_cstr << b.data();  // data()は文字列リテラルへのポインタを指す。

    ASSERT_NE(oss_a.str(), oss_b_cstr.str());
    ASSERT_EQ("123", oss_a.str());
    ASSERT_EQ("1234", oss_b_cstr.str());
```


### 3.10.2 POSIX系関数 <a id="SS_3_10_2"></a>
#### 3.10.2.1 使用禁止関数一覧 <a id="SS_3_10_2_1"></a>

| 禁止関数                                      | 代替え                                        |
|:----------------------------------------------|:----------------------------------------------|
| alloca()                                      | コンテナ                                      |
| asctime()                                     | strftime()                                    |
| asctime_r()                                   | strftime()                                    |
| bcmp()                                        |                                               |
| bcopy()                                       |                                               |
| brk()                                         |                                               |
| bzero()                                       |                                               |
| ctermid()                                     |                                               |
| ctime()                                       | strftime()                                    |
| ctime\_r()                                    | strftime()                                    |
| cuserid()                                     |                                               |
| ecvt()                                        |                                               |
| execl()                                       | execle(), execve()                            |
| execlp()                                      | execle(), execve()                            |
| execv()                                       | execle(), execve()                            |
| execvp()                                      | execle(), execve()                            |
| fattach()                                     |                                               |
| fcvt()                                        |                                               |
| fdetach()                                     |                                               |
| ftw()                                         |                                               |
| gcvt()                                        |                                               |
| getc()                                        |                                               |
| getchar()                                     |                                               |
| getgrgid()                                    | getgrgir\_r()                                 |
| getgrnam()                                    | getgrnam\_r()                                 |
| getitimer()                                   |                                               |
| getlogin()                                    | getlogin\_r()                                 |
| getmsg()                                      |                                               |
| getopt()                                      |                                               |
| getpmsg()                                     |                                               |
| getpwuid()                                    | getpwuid\_r()                                 |
| getpwnam()                                    | getpwnam\_r()                                 |
| gets()                                        | fgets()                                       |
| getitimer()                                   | timer\_gettime()                              |
| gettimeofday()                                | clock\_gettime()（戻り値を確認すること）      |
| getw()                                        |                                               |
| getwd()                                       |                                               |
| gmtime()                                      | gmtime\_r()                                   |
| index()                                       |                                               |
| ioctl() （stropts.hに定義されているもの）     |                                               |
| isascii()                                     |                                               |
| isastream()                                   |                                               |
| localtime()                                   | localtime\_r()                                |
| \_longjmp()                                   |                                               |
| mktemp()                                      |                                               |
| popen()                                       | execle(), execve()                            |
| pthread\_getconsurrency()                     |                                               |
| pthread\_setconcurrency()                     |                                               |
| putc()                                        |                                               |
| putchar()                                     |                                               |
| putenv() に autoな変数のポインタ              | setenv()                                      |
| putmsg()                                      |                                               |
| putpmsg()                                     |                                               |
| rand()                                        | srand()                                       |
| rand\_r()                                     | srand()                                       |
| readdir()                                     | readdir\_r()                                  |
| rindex()                                      |                                               |
| sbrk()                                        |                                               |
| scanf()                                       | sscanf()                                      |
| \_setjmp()                                    |                                               |
| setpgrp()                                     |                                               |
| settimer()                                    | timer\_settimer()                             |
| sighold()                                     | pthread\_sigmask() または sigprocmask()       |
| sigignore()                                   |                                               |
| siginterrupt()                                |                                               |
| signal()                                      | signalfd()                                    |
| sigpause()                                    | sigsuspend()                                  |
| sigrelse()                                    | pthread\_sigmask() または sigprocmask()       |
| sigset()                                      | sigaction()                                   |
| sigstack()                                    |                                               |
| strcpy()                                      | strncpy()                                     |
| strcat()                                      | strncat()                                     |
| strlen()                                      | strnlen()                                     |
| strtok()                                      |                                               |
| sprintf()                                     | snprintf()                                    |
| system()                                      | execle(), execve()                            |
| tempnam()                                     | tmpfile(), mkdtemp(), mkstemp()               |
| tmpnam()                                      | tmpfile(), mkdtemp(), mkstemp()               |
| toascii()                                     |                                               |
| \_tolower()                                   | tolower()                                     |
| \_toupper()                                   | toupper()                                     |
| ttyname()                                     | ttyname\_r()                                  |
| ttyslot()                                     |                                               |
| ulimit()                                      | getrlimit(), setrlimit()                      |
| utime()                                       | utimensat()                                   |
| utimes()                                      |                                               |
| valloc()                                      |                                               |
| vfork()                                       | fork()                                        |
| vsprintf()                                    | vsnprintf()                                   |
| wcscat()                                      | wcsncat()                                     |
| wcscpy()                                      | wcsncpy()                                     |

#### 3.10.2.2 使用禁止関数の理由や注意点 <a id="SS_3_10_2_2"></a>
##### 3.10.2.2.1 バッファオーバーランを引き起こしやすい関数 <a id="SS_3_10_2_2_1"></a>
* 以下の関数は、バッファオーバーフロー等のバグを引き起こしやすい。

```
    gets(), scanf(), strcpy(), strcat(), sprintf(), vsprintf(), wcscat(), wcscpy()
```

##### 3.10.2.2.2 コマンドインジェクション防止 <a id="SS_3_10_2_2_2"></a>
* 以下の関数は、外部コマンドの実行時に環境変数に依存してしまう。

```
    execl(), execlp(), execv(), execvp(), popen(), system()
```

##### 3.10.2.2.3 obsolete関数 <a id="SS_3_10_2_2_3"></a>
* 以下の関数は、すでにメンテナンスがされなくなった(obsolete)。

```
    asc_time(), asctime_r(), ctime(), ctime_r(), fattach(), fdetach(), ftw(), getitimer(),
    getmsg(), getpmsg(), gets(), settimer(), gettimeofday(), ioctl() in stropts.h for stream,
    isascii(), isastream(), _longjmp(),
    pthread_getconsurrency(), pthread_setconcurrency(), putmsg(), putpmsg(), rand_r(),
    _setjmp(), settimer(),
    setpgrp(), sighold(), sigignore(), siginterrupt(), sigpause(), sigrelse(), sigset(),
    strlen(), _tolower(), _toupper(), tempnam(), tmpnam(), toascii(), ulimit(), utime()
```

##### 3.10.2.2.4 LEGACY関数 <a id="SS_3_10_2_2_4"></a>
* 以下の関数は、すでに役目を終えた。

```
    sigstack(), cuserid(), getopt(), getw(), ttyslot(), valloc(), ecvt(), fcvt(), 
    gcvt(), mktemp(), bcmp(), bcopy(), bzero(), index(), rindex(), utimes(), getwd(),
    brk(), sbrk(), rand()
```

##### 3.10.2.2.5 スレッドセーフでない関数 <a id="SS_3_10_2_2_5"></a>
* 以下の関数は、スレッドセーフでない。

```
    asctime(), ctime(), getgrgid(), getgrnam(), getlogin(), getpwuid(), getpwnam(), gmtime(),
    localtime(), ttyname(), 
    ctermid(), tmpnam() (引数がNULLのとき、非リエントラントになる)
```

##### 3.10.2.2.6 標準外関数等 <a id="SS_3_10_2_2_6"></a>
* 可変長配列や、alloca()は、標準外である。

##### 3.10.2.2.7 扱いが難しい関数 <a id="SS_3_10_2_2_7"></a>
* signalの扱いは極めて難しく、安定動作をさせるのは困難である。
  「シグナルのリエントラント問題を解決でき、使用できる関数に制限がない」という利点があるため、
   signal()の代わりに、 signalfd() を使用する。 
* 排他的にファイルをオープンできないため、tmpfile()を使用しない。代わりにmkstemp()を使用する。

#### 3.10.2.3 典型的な注意点 <a id="SS_3_10_2_3"></a>
##### 3.10.2.3.1 リソースリークを引き起こしやすい関数 <a id="SS_3_10_2_3_1"></a>
* open()/close()、fopen()/fclose()はリソースリークを引き起こしやすい。
  「[RAII(scoped guard)](#8.9)」で例示したコードやstd::fstreamを使うことでその問題を回避する。

##### 3.10.2.3.2 シンボリックリンクの検査 <a id="SS_3_10_2_3_2"></a>
* シンボリックリンクはlstat()のみで検査せず、以下のように検査する。

    1.	ファイル名をlstat()
    2.	ファイルをopen()
    3.	2で取得したファイル記述子に対してfstat()
    4.	1, 3の情報を照合して同一ファイルであることを確認

##### 3.10.2.3.3 strncpy(), strncat()の終端 <a id="SS_3_10_2_3_3"></a>
* 下記のような問題を回避するために文字列操作にはstd::stringを使用する。
    * sizeof(dst) <= strlen(src) の場合、strncpy(dst, src, sizeof(dst) - 1)の呼び出しは、
      dstの文字列を'\0'終端しない。
    * コピーすべきデータが無くなると、dstの残りを'\0'で埋めるので性能上の問題がある。
    * strncpy(), strncat()ともに、
      sizeof(dst) < strlen(src) のときにsrcの文字列が切り捨てられたことを判別できない。

##### 3.10.2.3.4 TOCTOU (Time Of Check, Time Of Use) <a id="SS_3_10_2_3_4"></a>
* open()前にaccess()でファイルの存在を確認する等、チェックして使用するパターンでは、
  この動作がアトミックに行われないため問題が発生する。
  この問題回避の一般解はないが「ファイルの存在確認後、read-open」のような場合では、
  「いきなりread-openし、エラーした場合に対処」することでアトミックな処理にできる。

##### 3.10.2.3.5 メモリアロケーション <a id="SS_3_10_2_3_5"></a>
* new/deleteとmalloc/freeの混在を避けるため下記の使用をしない。
  newしたオブジェクトのポインタをfreeした場合、そのオブジェクトのデストラクタが呼び出されず、
  リソースリークしてしまうことがある。

```
    malloc(), realloc(), free()
```

##### 3.10.2.3.6 非同期シグナル <a id="SS_3_10_2_3_6"></a>
* プロセス監視のSIGCHLDや、accept()でのブロッキングの中断等、シグナルでしか処理できない場合を除き、
  非同期シグナルを使用しない。
* 使用してもよいシグナルは、以下に限られる。
    * SIGHUP : デーモン制御
    * SIGINT : 端末の割り込みキー
    * SIGILL : 不正なハードウェア命令
    * SIGBUS : ハードウェアフォルト
    * SIGFPE : 算術演算例外
    * SIGSEGV : 不正なメモリ参照
    * SIGALRM : タイムアウト検知
    * SIGTERM : killで送られるデフォルト終了シグナル
    * SIGCHLD : プロセス監視

* 上記シグナルを扱う場合であっても、シグナル処理専用スレッドでsigwait()を用いることで、
  非同期シグナルを同期的に扱うようにする。

## 3.11 その他 <a id="SS_3_11"></a>
### 3.11.1 assertion <a id="SS_3_11_1"></a>
* 論理的にありえない状態(特に論理的に到達しないはずの条件文への到達)を検出するために、
  assert()を使用する(「[switch文](programming_convention.md#SS_3_4_2)」、「[if文](programming_convention.md#SS_3_4_3)」参照)。
* assert()はコンパイルオプションにより無効化されることがあるため、
  assert()の引数に[副作用](term_explanation.md#SS_18_11_4)のある式を入れない。
* ランタイムでなく、コンパイル時に判断できる論理矛盾や使用制限には、static\_assertを使用する。

```cpp
    // @@@ example/programming_convention/etc.cpp 12

    template <uint32_t SIZE>
    struct POD {
        POD() noexcept
        {  // 何らかの理由で、10を超えるSIZEをサポートしたくない。
            static_assert(SIZE < 10, "too big");
        }

        uint32_t mem[SIZE];
    };

    void f() noexcept
    {
        POD<3> p3;             // コンパイル可能
        auto   p4 = POD<4>{};  // コンパイル可能
        // POD<10> p10;        // static assertion failed: too big でコンパイルエラー
        // POD<11> p11;        // static assertion failed: too big でコンパイルエラー
    }
```

* static\_assert、assert両方が使える場合には、static\_assertを優先して使用する。

* [演習-アサーションの選択](exercise_q.md#SS_19_7_1)  
* [演習-assert/static_assert](exercise_q.md#SS_19_7_2)  

### 3.11.2 アセンブラ <a id="SS_3_11_2"></a>
* アセンブラ関数は、.asm等で定義し、ヘッダファイルでCの関数として宣言する。
* アセンブラ関数も、関数/メンバ関数のルールに従う(「[非メンバ関数/メンバ関数](programming_convention.md#SS_3_3)」参照)。
* インラインアセンブラや、それを含む[関数型マクロ](programming_convention.md#SS_3_6_1)がソースコード全域に広がらないようにする。

### 3.11.3 言語拡張機能 <a id="SS_3_11_3"></a>
* #pragma once以外で、且つそれ以外に実装方法がない場合を除き、
  コンパイラ独自の言語拡張機能を使用しない。
* オブジェクトのアライメントが必要な場合、
    * alignas、alignofを使用する(「[固定長メモリプール](dynamic_memory_allocation.md#SS_14_2_1)」参照)。
    * コンパイラ独自のアライメント機能(#pragma等)の使用を避ける。
* 繰り返し使用する#pragmaに関しては、\_Pragma演算子とマクロを組み合わせて使用する。
  コンパイラの警告には従うべきであるが、ごく稀に無視せざるを得ない場合がある。
  そういった場合、その警告は下記例のような方法で抑止する。

```cpp
    // @@@ example/programming_convention/etc.cpp 38

    #if defined(__clang__)
    #define SUPPRESS_WARN_CLANG_UNUSED_PRIVATE_FIELD \
        _Pragma("clang diagnostic ignored \"-Wunused-private-field\"")
    #else
    #define SUPPRESS_WARN_CLANG_UNUSED_PRIVATE_FIELD
    #endif

    #define SUPPRESS_WARN_GCC_BEGIN _Pragma("GCC diagnostic push")
    #define SUPPRESS_WARN_GCC_END _Pragma("GCC diagnostic pop")
    #define SUPPRESS_WARN_GCC_NOT_EFF_CPP _Pragma("GCC diagnostic ignored \"-Weffc++\"")
    #define SUPPRESS_WARN_GCC_UNUSED_VAR _Pragma("GCC diagnostic ignored \"-Wunused-variable\"")

    //
    // ...
    //

    SUPPRESS_WARN_GCC_BEGIN;
    SUPPRESS_WARN_GCC_UNUSED_VAR;
    SUPPRESS_WARN_GCC_NOT_EFF_CPP;
    SUPPRESS_WARN_CLANG_UNUSED_PRIVATE_FIELD;

    class A {
    public:
        A() noexcept
        {
            // 警告: 'PragmaSample::A::b_' should be initialized in
            //       the member initialization list [-Weffc++]
            // 警告: unused variable 'c' [-Wunused-variable]
            // のようなワーニングが出力される。

            int32_t c;
            b_ = 0;
        }

    private:
        int32_t a_{0};
        int32_t b_;
    };

    SUPPRESS_WARN_GCC_END;
```

## 3.12 特に重要なプログラミング規約 <a id="SS_3_12"></a>
本章で取り上げた規約は、重要度という観点で様々なレベルのものが混在するため量も多く、
すぐに実践することが難しいかもしれない。
そういった場合には、まずは特に重要な下記リストを守ることから始めるのが良いだろう。

* 浮動小数点型をなるべく使わない([浮動小数点型](programming_convention.md#SS_3_1_1_5))。
* const/constexprを積極的に使用する([const/constexprインスタンス](programming_convention.md#SS_3_1_9), [メンバ関数](programming_convention.md#SS_3_3_2))。
* すべてのインスタンスは定義と同時に初期化する([インスタンスの初期化](programming_convention.md#SS_3_1_12))。
* クラスのpublicメンバ関数は最大7個([メンバの数](programming_convention.md#SS_3_2_2_2))。
* クラスのメンバ変数は最大4個([メンバの数](programming_convention.md#SS_3_2_2_2))。
* クラスのメンバ変数はprivateのみ([アクセスレベルと隠蔽化](programming_convention.md#SS_3_2_3))。
* クラスのメンバ変数はコンストラクタ終了時までに初期化する([非静的なメンバ変数/定数の初期化](programming_convention.md#SS_3_2_5))。
* friendは使用しない([アクセスレベルと隠蔽化](programming_convention.md#SS_3_2_3))。
* 派生は最大2回([継承/派生](programming_convention.md#SS_3_2_4))。
* 関数は小さくする([サイクロマティック複雑度](programming_convention.md#SS_3_3_3_1))。
* 関数の仮引数は最大4個([実引数/仮引数](programming_convention.md#SS_3_3_3_5))。
* グローバルなインスタンスは使わない([スコープ](programming_convention.md#SS_3_8))。
* throw, try-catchは控えめに使用する([エクセプション処理](programming_convention.md#SS_3_3_3_10))。
* 構文に関しては以下に気を付ける。
    * if, else, for, while, do後には{}を使う([複合文](programming_convention.md#SS_3_4_1))。
    * switchでのフォールスルーをしない([switch文](programming_convention.md#SS_3_4_2))。
    * switchにはdefaultラベルを入れる([switch文](programming_convention.md#SS_3_4_2))。
    * 範囲for文を積極的に使う([範囲for文](programming_convention.md#SS_3_4_4))。
    * gotoを使用しない([goto文](programming_convention.md#SS_3_4_7))。
* オブジェクトのダイナミックな生成にはstd::make_unique<>を使用する
  ([メモリアロケーション](programming_convention.md#SS_3_5_6))。
* Cタイプのキャストは使用しない([キャスト、暗黙の型変換](programming_convention.md#SS_3_5_10))。


