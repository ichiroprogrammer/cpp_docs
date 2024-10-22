<!-- ./md/programming_convention.md -->
# プログラミング規約 <a id="SS_3"></a>
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

___

__この章の構成__

&emsp;&emsp; [型とインスタンス](programming_convention.md#SS_3_1)  
&emsp;&emsp;&emsp; [算術型](programming_convention.md#SS_3_1_1)  
&emsp;&emsp;&emsp;&emsp; [整数型](programming_convention.md#SS_3_1_1_1)  
&emsp;&emsp;&emsp;&emsp; [char型](programming_convention.md#SS_3_1_1_2)  
&emsp;&emsp;&emsp;&emsp; [std::byte型](programming_convention.md#SS_3_1_1_3)  
&emsp;&emsp;&emsp;&emsp; [bool型](programming_convention.md#SS_3_1_1_4)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点型](programming_convention.md#SS_3_1_1_5)  

&emsp;&emsp;&emsp; [enum](programming_convention.md#SS_3_1_2)  
&emsp;&emsp;&emsp; [bit field](programming_convention.md#SS_3_1_3)  
&emsp;&emsp;&emsp; [class](programming_convention.md#SS_3_1_4)  
&emsp;&emsp;&emsp; [struct](programming_convention.md#SS_3_1_5)  
&emsp;&emsp;&emsp; [union](programming_convention.md#SS_3_1_6)  
&emsp;&emsp;&emsp; [配列](programming_convention.md#SS_3_1_7)  
&emsp;&emsp;&emsp; [型エイリアス](programming_convention.md#SS_3_1_8)  
&emsp;&emsp;&emsp; [const/constexprインスタンス](programming_convention.md#SS_3_1_9)  
&emsp;&emsp;&emsp; [リテラル](programming_convention.md#SS_3_1_10)  
&emsp;&emsp;&emsp;&emsp; [生文字列リテラル](programming_convention.md#SS_3_1_10_1)  

&emsp;&emsp;&emsp; [型推論](programming_convention.md#SS_3_1_11)  
&emsp;&emsp;&emsp;&emsp; [auto](programming_convention.md#SS_3_1_11_1)  

&emsp;&emsp;&emsp; [インスタンスの初期化](programming_convention.md#SS_3_1_12)  
&emsp;&emsp;&emsp; [rvalue](programming_convention.md#SS_3_1_13)  

&emsp;&emsp; [クラスとインスタンス](programming_convention.md#SS_3_2)  
&emsp;&emsp;&emsp; [ファイルの使用方法](programming_convention.md#SS_3_2_1)  
&emsp;&emsp;&emsp; [クラスの規模](programming_convention.md#SS_3_2_2)  
&emsp;&emsp;&emsp;&emsp; [行数](programming_convention.md#SS_3_2_2_1)  
&emsp;&emsp;&emsp;&emsp; [メンバの数](programming_convention.md#SS_3_2_2_2)  
&emsp;&emsp;&emsp;&emsp; [凝集度](programming_convention.md#SS_3_2_2_3)  

&emsp;&emsp;&emsp; [アクセスレベルと隠蔽化](programming_convention.md#SS_3_2_3)  
&emsp;&emsp;&emsp; [継承/派生](programming_convention.md#SS_3_2_4)  
&emsp;&emsp;&emsp;&emsp; [インターフェースの継承](programming_convention.md#SS_3_2_4_1)  
&emsp;&emsp;&emsp;&emsp; [多重継承](programming_convention.md#SS_3_2_4_2)  

&emsp;&emsp;&emsp; [非静的なメンバ変数](programming_convention.md#SS_3_2_5)  
&emsp;&emsp;&emsp; [静的なメンバ変数/定数の初期化](programming_convention.md#SS_3_2_6)  
&emsp;&emsp;&emsp; [mutableなメンバ変数](programming_convention.md#SS_3_2_7)  
&emsp;&emsp;&emsp; [スライシング](programming_convention.md#SS_3_2_8)  
&emsp;&emsp;&emsp; [オブジェクトの所有権](programming_convention.md#SS_3_2_9)  
&emsp;&emsp;&emsp; [オブジェクトのライフタイム](programming_convention.md#SS_3_2_10)  

&emsp;&emsp; [非メンバ関数/メンバ関数](programming_convention.md#SS_3_3)  
&emsp;&emsp;&emsp; [非メンバ関数](programming_convention.md#SS_3_3_1)  
&emsp;&emsp;&emsp; [メンバ関数](programming_convention.md#SS_3_3_2)  
&emsp;&emsp;&emsp;&emsp; [特殊メンバ関数](programming_convention.md#SS_3_3_2_1)  
&emsp;&emsp;&emsp;&emsp; [コンストラクタ](programming_convention.md#SS_3_3_2_2)  
&emsp;&emsp;&emsp;&emsp; [copyコンストラクタ、copy代入演算子](programming_convention.md#SS_3_3_2_3)  
&emsp;&emsp;&emsp;&emsp; [moveコンストラクタ、move代入演算子](programming_convention.md#SS_3_3_2_4)  
&emsp;&emsp;&emsp;&emsp; [初期化子リストコンストラクタ](programming_convention.md#SS_3_3_2_5)  
&emsp;&emsp;&emsp;&emsp; [デストラクタ](programming_convention.md#SS_3_3_2_6)  
&emsp;&emsp;&emsp;&emsp; [オーバーライド](programming_convention.md#SS_3_3_2_7)  

&emsp;&emsp;&emsp; [非メンバ関数/メンバ関数共通](programming_convention.md#SS_3_3_3)  
&emsp;&emsp;&emsp;&emsp; [サイクロマティック複雑度](programming_convention.md#SS_3_3_3_1)  
&emsp;&emsp;&emsp;&emsp; [行数](programming_convention.md#SS_3_3_3_2)  
&emsp;&emsp;&emsp;&emsp; [オーバーロード](programming_convention.md#SS_3_3_3_3)  
&emsp;&emsp;&emsp;&emsp; [演算子オーバーロード](programming_convention.md#SS_3_3_3_4)  
&emsp;&emsp;&emsp;&emsp; [実引数/仮引数](programming_convention.md#SS_3_3_3_5)  
&emsp;&emsp;&emsp;&emsp; [自動変数](programming_convention.md#SS_3_3_3_6)  
&emsp;&emsp;&emsp;&emsp; [戻り値型](programming_convention.md#SS_3_3_3_7)  
&emsp;&emsp;&emsp;&emsp; [constexpr関数](programming_convention.md#SS_3_3_3_8)  
&emsp;&emsp;&emsp;&emsp; [リエントラント性](programming_convention.md#SS_3_3_3_9)  
&emsp;&emsp;&emsp;&emsp; [エクセプション処理](programming_convention.md#SS_3_3_3_10)  
&emsp;&emsp;&emsp;&emsp; [ビジーループ](programming_convention.md#SS_3_3_3_11)  

&emsp;&emsp; [構文](programming_convention.md#SS_3_4)  
&emsp;&emsp;&emsp; [複合文](programming_convention.md#SS_3_4_1)  
&emsp;&emsp;&emsp; [switch文](programming_convention.md#SS_3_4_2)  
&emsp;&emsp;&emsp; [if文](programming_convention.md#SS_3_4_3)  
&emsp;&emsp;&emsp; [while文](programming_convention.md#SS_3_4_4)  
&emsp;&emsp;&emsp; [範囲for文](programming_convention.md#SS_3_4_5)  
&emsp;&emsp;&emsp; [制御文のネスト](programming_convention.md#SS_3_4_6)  
&emsp;&emsp;&emsp; [return文](programming_convention.md#SS_3_4_7)  
&emsp;&emsp;&emsp; [goto文](programming_convention.md#SS_3_4_8)  
&emsp;&emsp;&emsp; [ラムダ式](programming_convention.md#SS_3_4_9)  
&emsp;&emsp;&emsp; [マクロの中の文](programming_convention.md#SS_3_4_10)  

&emsp;&emsp; [演算子](programming_convention.md#SS_3_5)  
&emsp;&emsp;&emsp; [優先順位](programming_convention.md#SS_3_5_1)  
&emsp;&emsp;&emsp; [代入演算](programming_convention.md#SS_3_5_2)  
&emsp;&emsp;&emsp; [ビット演算](programming_convention.md#SS_3_5_3)  
&emsp;&emsp;&emsp; [論理演算](programming_convention.md#SS_3_5_4)  
&emsp;&emsp;&emsp; [条件演算子](programming_convention.md#SS_3_5_5)  
&emsp;&emsp;&emsp; [メモリアロケーション](programming_convention.md#SS_3_5_6)  
&emsp;&emsp;&emsp;&emsp; [new](programming_convention.md#SS_3_5_6_1)  
&emsp;&emsp;&emsp;&emsp; [delete](programming_convention.md#SS_3_5_6_2)  
&emsp;&emsp;&emsp;&emsp; [メモリ制約が強いシステムでの::operator new](programming_convention.md#SS_3_5_6_3)  

&emsp;&emsp;&emsp; [sizeof](programming_convention.md#SS_3_5_7)  
&emsp;&emsp;&emsp; [ポインタ間の演算](programming_convention.md#SS_3_5_8)  
&emsp;&emsp;&emsp; [RTTI](programming_convention.md#SS_3_5_9)  
&emsp;&emsp;&emsp; [キャスト、暗黙の型変換](programming_convention.md#SS_3_5_10)  

&emsp;&emsp; [プリプロセッサ命令](programming_convention.md#SS_3_6)  
&emsp;&emsp;&emsp; [関数型マクロ](programming_convention.md#SS_3_6_1)  
&emsp;&emsp;&emsp; [マクロ定数](programming_convention.md#SS_3_6_2)  

&emsp;&emsp; [パッケージとその構成ファイル](programming_convention.md#SS_3_7)  
&emsp;&emsp;&emsp; [パッケージの実装と公開](programming_convention.md#SS_3_7_1)  
&emsp;&emsp;&emsp; [識別子の宣言、定義](programming_convention.md#SS_3_7_2)  
&emsp;&emsp;&emsp; [依存関係](programming_convention.md#SS_3_7_3)  
&emsp;&emsp;&emsp; [二重読み込みの防御](programming_convention.md#SS_3_7_4)  
&emsp;&emsp;&emsp; [ヘッダファイル内の#include](programming_convention.md#SS_3_7_5)  
&emsp;&emsp;&emsp; [#includeするファイルの順番](programming_convention.md#SS_3_7_6)  
&emsp;&emsp;&emsp; [#includeで指定するパス名](programming_convention.md#SS_3_7_7)  

&emsp;&emsp; [スコープ](programming_convention.md#SS_3_8)  
&emsp;&emsp;&emsp; [スコープの定義と原則](programming_convention.md#SS_3_8_1)  
&emsp;&emsp;&emsp; [名前空間](programming_convention.md#SS_3_8_2)  
&emsp;&emsp;&emsp; [using宣言/usingディレクティブ](programming_convention.md#SS_3_8_3)  
&emsp;&emsp;&emsp; [ADLと名前空間による修飾の省略](programming_convention.md#SS_3_8_4)  
&emsp;&emsp;&emsp; [名前空間のエイリアス](programming_convention.md#SS_3_8_5)  

&emsp;&emsp; [ランタイムの効率](programming_convention.md#SS_3_9)  
&emsp;&emsp;&emsp; [前置/後置演算子の選択](programming_convention.md#SS_3_9_1)  
&emsp;&emsp;&emsp; [operator X、operator x=の選択](programming_convention.md#SS_3_9_2)  
&emsp;&emsp;&emsp; [関数の戻り値オブジェクト](programming_convention.md#SS_3_9_3)  
&emsp;&emsp;&emsp; [move処理](programming_convention.md#SS_3_9_4)  
&emsp;&emsp;&emsp; [std::string vs std::string const& vs std::string_view](programming_convention.md#SS_3_9_5)  
&emsp;&emsp;&emsp; [extern template](programming_convention.md#SS_3_9_6)  

&emsp;&emsp; [標準クラス、関数の使用制限](programming_convention.md#SS_3_10)  
&emsp;&emsp;&emsp; [STL](programming_convention.md#SS_3_10_1)  
&emsp;&emsp;&emsp;&emsp; [スマートポインタの使用制限](programming_convention.md#SS_3_10_1_1)  
&emsp;&emsp;&emsp;&emsp; [配列系コンテナクラスの使用制限](programming_convention.md#SS_3_10_1_2)  
&emsp;&emsp;&emsp;&emsp; [std::stringの使用制限](programming_convention.md#SS_3_10_1_3)  
&emsp;&emsp;&emsp;&emsp; [std::string_viewの使用制限](programming_convention.md#SS_3_10_1_4)  

&emsp;&emsp;&emsp; [POSIX系関数](programming_convention.md#SS_3_10_2)  
&emsp;&emsp;&emsp;&emsp; [使用禁止関数一覧](programming_convention.md#SS_3_10_2_1)  
&emsp;&emsp;&emsp;&emsp; [使用禁止関数の理由や注意点](programming_convention.md#SS_3_10_2_2)  
&emsp;&emsp;&emsp;&emsp; [典型的な注意点](programming_convention.md#SS_3_10_2_3)  

&emsp;&emsp; [その他](programming_convention.md#SS_3_11)  
&emsp;&emsp;&emsp; [assertion](programming_convention.md#SS_3_11_1)  
&emsp;&emsp;&emsp; [アセンブラ](programming_convention.md#SS_3_11_2)  
&emsp;&emsp;&emsp; [言語拡張機能](programming_convention.md#SS_3_11_3)  

&emsp;&emsp; [特に重要なプログラミング規約](programming_convention.md#SS_3_12)  
  
  

[このドキュメントの構成](introduction.md#SS_1_7)に戻る。  

___

## 型とインスタンス <a id="SS_3_1"></a>

### 算術型 <a id="SS_3_1_1"></a>

#### 整数型 <a id="SS_3_1_1_1"></a>
* [整数型](term_explanation.md#SS_19_1_3)には、整数の基本型(intやlong等)を直接使わずに、
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

* [演習-汎整数型の選択](exercise_q.md#SS_20_1_1)

#### char型 <a id="SS_3_1_1_2"></a>
* charはascii文字の保持のみに使用する。
* char\*をvoid\*の代わりに使わない。
* charがsingedかunsignedかは処理系に依存するため、char型を[汎整数型](term_explanation.md#SS_19_1_2)として扱わない。
  8ビット整数には、int8\_tまたは、uint8\_tを使用する。
    * バイトストリームを表現する場合、int8_t\*、int8_t[]、uint8_t\*、uint8_t[]のいずれかを使う。

* [演習-汎整数型の演算](exercise_q.md#SS_20_1_2)

#### std::byte型 <a id="SS_3_1_1_3"></a>
* intよりもビット幅の小さい組み込み型の演算の結果は[汎整数拡張](term_explanation.md#SS_19_1_5)によりint型になるため、
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

#### bool型 <a id="SS_3_1_1_4"></a>
* bool型は、bool型リテラル(true/false)やbool型オブジェクトの保持のみに使用する。
* bool型を[汎整数型](term_explanation.md#SS_19_1_2)として扱わない。bool型に++を使用しない(--はコンパイルできない)。

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

#### 浮動小数点型 <a id="SS_3_1_1_5"></a>
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
* [汎整数型](term_explanation.md#SS_19_1_2)の演算とは違い、0除算等の浮動小数点演算のエラーは、
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

* 扱うダイナミックレンジに収まる限り、安易に浮動小数点を使わず、
  代わりに[固定小数点クラス](template_meta_programming.md#SS_13_5_2)を使用する

* [演習-浮動小数点型](exercise_q.md#SS_20_1_3)

### enum <a id="SS_3_1_2"></a>
* C++の強力な型システムや、コンパイラの静的解析機能(switchでのcase抜け)を効果的に使用するために、
  一連の定数の列挙にはenumを使用する。
* 使用範囲や方法が明示しづらく、且つ整数型への[算術変換](term_explanation.md#SS_19_1_4)が行われてしまう旧来のenum
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
        case WL_Red:  // CL_Redの間違い?
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
  代わりにstatic constexprインスタンス(「[constexpr関数](term_explanation.md#SS_19_4_2)」参照)を使用する。
  こうすることで定数の型を明示できる。

* [演習-定数列挙](exercise_q.md#SS_20_1_4)
* [演習-enum](exercise_q.md#SS_20_1_5)

### bit field <a id="SS_3_1_3"></a>
* ハードウエアレジスタにアクセスをする目的でのみ使用する。
* bit fieldの型は、unsigned intにする。

### class <a id="SS_3_1_4"></a>
* 「[クラスとインスタンス](programming_convention.md#SS_3_2)」を参照せよ。

### struct <a id="SS_3_1_5"></a>
* メンバ変数を持つ構造体は、[POD](term_explanation.md#SS_19_3_5)としてのみ使用する。
* メンバ変数を持つ構造体を基底クラスとした継承をしない。
  従ってそのような構造体は常にfinalであるが、finalの明示はしない。
* メンバ変数(static constやstatic constexprメンバは定数とする)を持たない構造体は、
  templateや非スコープドenumのスコーピング(「[enum](term_explanation.md#SS_19_2)」参照)等に使用しても良い。
* コンストラクタ以外のメンバ関数を定義しない。
    * [ディープコピー](term_explanation.md#SS_19_5_9_2)(「[コンストラクタ](programming_convention.md#SS_3_3_2_2)」参照)が必要な型は、structでなくclassで表す。
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

### union <a id="SS_3_1_6"></a>
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
  std::variant(「[std::variantとジェネリックラムダ](template_meta_programming.md#SS_13_7_2_2)」参照)を使用する
  (std::anyはunionの代替えにはならないので、このような場合には使用しない)。

### 配列 <a id="SS_3_1_7"></a>
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

* 配列の全要素にアクセスするような繰り返し処理には[範囲for文](term_explanation.md#SS_19_7_3)を使用する。

* [演習-配列の範囲for文](exercise_q.md#SS_20_1_6)

### 型エイリアス <a id="SS_3_1_8"></a>
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

* [演習-エイリアス](exercise_q.md#SS_20_1_7)

### const/constexprインスタンス <a id="SS_3_1_9"></a>
* インスタンス、インスタンスへのポインタ、インスタンスへのリファレンス等に対して、
    * [constexpr定数](term_explanation.md#SS_19_4_1)をパラメータにした場合、コンパイル時に定数として評価できる関数は、
      [constexpr関数](term_explanation.md#SS_19_4_2)として宣言する。
    * コンパイル時に必ず定数として評価したい[constexpr関数](term_explanation.md#SS_19_4_2)には[consteval](term_explanation.md#SS_19_4_5)を使用する。
    * constexprにはできないが、const(「[constインスタンス](term_explanation.md#SS_19_3_12)」にはできるインスタンスは、
      constとして定義する。関数の仮引数になっているリファレンスやポインタをconstにすることは特に重要である
    * 文字列リテラルのアドレスを非constポインタ型変数に代入しない(「[リテラル](term_explanation.md#SS_19_6)」参照)。
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

* [演習-constの意味](exercise_q.md#SS_20_1_8)
* [演習-const/constexpr](exercise_q.md#SS_20_1_9)

### リテラル <a id="SS_3_1_10"></a>
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
  (「[const/constexprインスタンス](programming_convention.md#SS_3_1_9)」、「[std::string型リテラル](term_explanation.md#SS_19_6_6_2)」参照)。
* 長い[汎整数型](term_explanation.md#SS_19_1_2)リテラルを使用する場合は、適切に区切りを入れる(C++14)。
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

#### 生文字列リテラル <a id="SS_3_1_10_1"></a>
* 正規表現を表す文字列リテラルを使用する場合、文字列内のエスケープシーケンスをエスケープするのでなく、
  には[生文字列リテラル](term_explanation.md#SS_19_6_1)を使用する。これにより正規表現の可読性が向上する。

```cpp
    // @@@ example/programming_convention/raw_literal_ut.cpp 9

    std::pair<std::string, std::string> url2addr(std::string const& url)
    {
    #if 0  // 正規表現のエスケープ
        std::regex re("^(https?|ftp):\\/\\/([^\\/\\s]+)(\\/.*)?$");
    #else
        std::regex re(R"(^(https?|ftp)://([^/\s]+)(/.*)?$)");  // 生文字リテラル
    #endif
        std::smatch match;

        if (std::regex_search(url, match, re) && match.size() > 3) {
            std::string host = match.str(2);
            std::string path = match.str(3);
            return {host, path};
        }
        else {
            return {"", ""};
        }
    }

    // @@@ example/programming_convention/raw_literal_ut.cpp 33

    std::string const url = "https://www.example.com/path/to/resource";

    auto [host, path] = url2addr(url);
    ASSERT_EQ("www.example.com", host);
    ASSERT_EQ("/path/to/resource", path);
```

* [演習-危険なconst_cast](exercise_q.md#SS_20_1_10)
* [演習-リテラル](exercise_q.md#SS_20_1_11)

### 型推論 <a id="SS_3_1_11"></a>
#### auto <a id="SS_3_1_11_1"></a>
* [AAAスタイル](term_explanation.md#SS_19_11_1)に従い適切にautoを使用する。

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

* auto、[decltype](term_explanation.md#SS_19_11_2), decltype(auto)の微妙な違いに気を付ける。

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

* 通常の関数の定義に「[autoパラメータによる関数テンプレートの簡易定義](term_explanation.md#SS_19_10_9)」の使用を避ける。
  [autoパラメータによる関数テンプレートの簡易定義](term_explanation.md#SS_19_10_9)を使ったインライン関数は柔軟すぎる。

* [演習-適切なautoの使い方](exercise_q.md#SS_20_1_12)

### インスタンスの初期化 <a id="SS_3_1_12"></a>
* 関数内のオブジェクトは、出来る限り[AAAスタイル](term_explanation.md#SS_19_11_1)を用いて宣言し、同時に初期化する。
* [算術型](term_explanation.md#SS_19_1_1)の宣言に[AAAスタイル](term_explanation.md#SS_19_11_1)が使えない場合、
  「代入演算子を伴わない[一様初期化](term_explanation.md#SS_19_5_6)」を使用する。
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

* リファレンスやポインタの宣言に[AAAスタイル](term_explanation.md#SS_19_11_1)が使えない場合、
  「代入演算子を伴わない[一様初期化](term_explanation.md#SS_19_5_6)」か「=による初期化」を使用する。
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

* 構造体やクラス型オブジェクトの宣言に[AAAスタイル](term_explanation.md#SS_19_11_1)が使えない場合、
    * 「代入演算子を伴わない[一様初期化](term_explanation.md#SS_19_5_6)」を使用する。
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

* decltypeによるオブジェクトの宣言は、[AAAスタイル](term_explanation.md#SS_19_11_1)と同様に行う。

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

* 配列の宣言には、「代入演算子を伴わない[一様初期化](term_explanation.md#SS_19_5_6)」を使用する。
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

* 宣言時にポインタ変数の初期値が決まらない場合、nullptrで初期化する(「[リテラル](term_explanation.md#SS_19_6)」参照)。

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


* [演習-インスタンスの初期化](exercise_q.md#SS_20_1_15)
* [演習-vector初期化](exercise_q.md#SS_20_1_14)
* [演習-ポインタの初期化](exercise_q.md#SS_20_1_13)


### rvalue <a id="SS_3_1_13"></a>
* 関数の仮引数以外のリファレンスで[rvalue](term_explanation.md#SS_19_13_3)をバインドしない
  (「[オブジェクトのライフタイム](programming_convention.md#SS_3_2_10)」参照)。
* rvalueの内部ハンドルを使用しない(「[std::string_viewの使用制限](programming_convention.md#SS_3_10_1_4)」参照)。

```cpp
    // @@@ example/programming_convention/type_ut.cpp 790

    char const* str = std::string{"str"}.c_str();
    // strが指すポインタはこの行では解放済

    ASSERT_STREQ(str, "str");  //    strは無効なポインタを保持であるため、未定義動作
```

* 非constなリファレンスでrvalueをバインドしない。


## クラスとインスタンス <a id="SS_3_2"></a>
### ファイルの使用方法 <a id="SS_3_2_1"></a>
* 下記の例外を除き、一つのクラスはそれを宣言、定義する1つのヘッダファイルと、
  一つの.cppファイルによって構成する。
    * ファイル外部から使用されないクラスは、一つの.cppファイルの無名名前空間で宣言、定義する。
    * ファイル外部から使用されるインラインクラス(クラステンプレート等)は、
      一つのヘッダファイルで宣言、定義する。
    * 「一つのヘッダファイル(a.h)と、一つの.cpp(a.cpp)で構成されたクラスA」のみをサポートするクラス
      (Aのインターフェースや実装専用に定義されたクラス(「[Pimpl](design_pattern.md#SS_9_3)」参照))は、
      a.h、a.cppで宣言、定義する。

### クラスの規模 <a id="SS_3_2_2"></a>
#### 行数 <a id="SS_3_2_2_1"></a>
* それ以外に方法がない場合を除き、ヘッダファイル内のクラスの定義、
  宣言はコメントを含め200行程度に収める。
* クラス内定義関数が大きくなると下記のような問題が発生しやすくなるため、
  10行を超える関数はクラス内で定義しない。
    * 関数のインポートする外部シンボルが多くなり、
      このクラスを使用する別のクラスに不要な依存関係を作ってしまう
      (「[インターフェース分離の原則(ISP)](solid.md#SS_8_4)」参照)。
    * クラスの定義が間延びして、クラスの全体構造を把握することが困難になる。

#### メンバの数 <a id="SS_3_2_2_2"></a>
* それ以外に方法がない場合を除き、publicメンバ関数の数は、最大7個程度に収める
  (ただし、オーバーロードにより同じ名前を持つ関数群は、全部で1個とカウントする)。
* オブジェクトの状態を保持するメンバ変数の数は、最大4個程度に留める。
  constやconstexprメンバ・インスタンスは定数(状態を保持するメンバ変数ではない)であるため、
  この数に含めない。

#### 凝集度 <a id="SS_3_2_2_3"></a>
* 単なるデータホルダー(アプリケーションの設定データを保持するようなクラス等)や、
  ほとんどの振る舞いを他のクラスに委譲するようなクラスを除き、
  [凝集度](term_explanation.md#SS_19_19_2)が高くなるように設計する。

* [演習-凝集度の意味](exercise_q.md#SS_20_2_1)
* [演習-凝集度の向上](exercise_q.md#SS_20_2_2)

### アクセスレベルと隠蔽化 <a id="SS_3_2_3"></a>
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

### 継承/派生 <a id="SS_3_2_4"></a>
* 派生は最大2回程度までに留める。やむを得ず階層が深くなる場合、
  コードの静的解析等を使用し派生関係を明確にする(「[クラスのレイアウト](term_explanation.md#SS_19_3_8)」参照)。
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

#### インターフェースの継承 <a id="SS_3_2_4_1"></a>
* クラス間に「Is-a」の関係が成り立つときに限りpublic継承を行う。
    * public継承を行う場合、[リスコフの置換原則(LSP)](solid.md#SS_8_3)を守る。
    * インターフェースを継承しない場合、public継承をしない。
* C#やJavaのinterfaceが必要ならば(インタフェースと実装の完全分離をしたい場合等)、
  pure-virtualなメンバ関数のみを宣言したクラス
  (もしくはそのクラスに[NVI(non virtual interface)](design_pattern.md#SS_9_8)を適用したクラス)
  を定義する。

#### 多重継承 <a id="SS_3_2_4_2"></a>
* それが不可避でない限り、多重継承は使用しない。
* 多重継承を使用する場合、複数個の基底クラスのうち、一つを除きメンバ変数を持ってはならない。
* 多重継承を使用する場合、継承階層内に同じ基底クラスが複数回出てきてはならない
  (ダイヤモンド継承をしない)。
* やむを得ずダイヤモンド継承をせざるを得ない場合、
  継承階層内に複数回出現する基底クラスにはvirtual継承を行う。
* virtual継承を行ったクラスのコンストラクタからは、
  virtual基底クラスのコンストラクタを呼び出すようにする
  (こうしないとvirtual基底クラスは初期化されない)。

### 非静的なメンバ変数 <a id="SS_3_2_5"></a>
* すべての非静的なメンバ変数は、コンストラクタ終了時までに明示的に初期化する。
* 多くのコンパイラや静的解析ツールはインスペクタは、
  [NSDMI](term_explanation.md#SS_19_5_5_1)、[初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)による初期化の漏れについては容易に発見、
  指摘できることが多い。
* constメンバ変数は、[NSDMI](term_explanation.md#SS_19_5_5_1)、
  [初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)でなければ初期化できないため、それ以外に方法がない場合を除き、
  [コンストラクタ内での非静的なメンバ変数の初期値の代入](term_explanation.md#SS_19_5_5_3)の使用を避ける。
* 非静的なメンバ変数はクラス内で定義された順序に従い初期化されるため、
  [初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)の順序を定義順序と同じにすることで可読性を向上させる。
* クラスがただ一つのコンストラクタを持つ場合、
  [NSDMI](term_explanation.md#SS_19_5_5_1)と[初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)を混在させない。
  従って、[初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)を必要とするメンバ変数が一つでもある場合は、
  すべての変数の初期化を[初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)で行う。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 257

    class A1 {
    public:
        A1() noexcept {}  // OK NSDMIに統一

    private:
        int32_t const a_{1};  // OK NSDMIによる初期化。
                              //    ただし、static constexprにすべき。
        int32_t b_[2]{0, 1};  // OK NSDMIによる初期化
        int32_t c_{5};        // OK NSDMIによる初期化
    };

    class A2 {
    public:
        explicit A2(int a) noexcept   // OK 初期化子リストに統一
            : a_{a}, b_{0, 1}, c_{5}  // OK 初期化子リストによる初期化
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
            c_ = 5;  // NG NSDMIか初期化子リストを使用するべき
        }

    private:
        int32_t const a_;
        int32_t       b_[2]{0, 1};  // NG 初期化方法の混在
        int32_t       c_;
    };
```

* クラスが複数のコンストラクタを持つ場合、
  すべてのメンバ変数に対して[NSDMI](term_explanation.md#SS_19_5_5_1)を行い(デフォルト値の設定)、
  デフォルト値とは異なる初期値を持つ変数に対してのみ、
  コンストラクタ毎に[初期化子リストでの初期化](term_explanation.md#SS_19_5_5_2)を行う。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 297

    class A4 {
    public:
        A4() noexcept {}  // OK

        A4(int32_t e) noexcept : e_{e} {}  // OK 初期化子リストによるe_の上書き
        // 注) A4()とA4(int32_t)はデフォルト引数を使用すれば統一できるが、
        // 例の単純化のためにあえてそれぞれを定義している。

    private:
        int32_t d_{5};  // OK NSDMIによる初期化
        int32_t e_{0};  // OK NSDMIによる初期化
    };
```

* [演習-メンバ変数の初期化方法の選択](exercise_q.md#SS_20_2_3)
* [演習-メンバの型](exercise_q.md#SS_20_2_4)
* [演習-メンバ変数の初期化](exercise_q.md#SS_20_2_5)

### 静的なメンバ変数/定数の初期化 <a id="SS_3_2_6"></a>
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
    // @@@ example/programming_convention/class_ut.cpp 317
    //
    uint32_t StaticConstexprVar::MultiplyBy2(uint32_t a) noexcept { return static_constexpr_var_2 * a; }

    namespace {
    constexpr uint32_t static_constexpr_var_4{4};  // OK クラス内で定義する必要なし
    }

    uint32_t StaticConstexprVar::MultiplyBy4(uint32_t a) noexcept { return static_constexpr_var_4 * a; }
```

### mutableなメンバ変数 <a id="SS_3_2_7"></a>
* 排他制御用(std::mutex等)や計算データのキャッシュ用等のメンバ変数を除き、
  メンバ変数をmutableと宣言しない。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 331

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

### スライシング <a id="SS_3_2_8"></a>
* オブジェクトの[スライシング](term_explanation.md#SS_19_5_9_3)には以下のいずれかで対処する。
    * [Clone(仮想コンストラクタ)](design_pattern.md#SS_9_7)を使用する。
    * copy代入演算子を= deleteする。

* [スライシング](term_explanation.md#SS_19_5_9_3)と類似の問題が起こるため、
  オブジェクトの配列をそのオブジェクトの基底クラスへのポインタに代入しない。

* [演習-スライシング](exercise_q.md#SS_20_2_6)

### オブジェクトの所有権 <a id="SS_3_2_9"></a>
* オブジェクトaの所有権
  (「[オブジェクトの所有権](term_explanation.md#SS_19_5_7)」参照)を持つオブジェクトもしくは関数は、
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

* [演習-オブジェクトの所有権](exercise_q.md#SS_20_2_7)

### オブジェクトのライフタイム <a id="SS_3_2_10"></a>
* [オブジェクトのライフタイム](term_explanation.md#SS_19_5_8)開始前、
  もしくは終了後のオブジェクトにアクセスしない。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 385

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
    // @@@ example/programming_convention/class_ut.cpp 401

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
* [rvalue](term_explanation.md#SS_19_13_3)はライフタイム終了間際のオブジェクトであるため、
  関数の仮引数以外のリファレンスでrvalueをバインドしない
  (特にリファレンス型のメンバ変数でrvalueをバインドしないことは重要である)。
  rvalueをリファレンス型の引数で受け取る場合はconstリファレンス、
  もしくはrvalueリファレンス(T&&)を使用する(「[rvalue](programming_convention.md#SS_3_1_13)」参照)。

```cpp
    // @@@ example/programming_convention/class_ut.cpp 432

    void f0(E&) noexcept;
    void f1(E const&) noexcept;
    void f2(E&&) noexcept;
```
```cpp
    // @@@ example/programming_convention/class_ut.cpp 441

    // f0(E{});  NG ほとんどのコンパイラではエラー
    f1(E{});  // OK rvalueはconstリファレンスにバインド可
    f2(E{});  // OK rvalueはrvalueリファレンス

    E const& a0 = E{"4"};  // NG rvalueを引数以外のconstリファレンスに代入
    E&&      a1 = E{"5"};  // NG rvalueを引数以外のrvalueリファレンスに代入
```


## 非メンバ関数/メンバ関数 <a id="SS_3_3"></a>

### 非メンバ関数 <a id="SS_3_3_1"></a>
* 下記のような関数を除き、グローバル名前空間に非メンバ関数を定義しない。
    * C言語から呼び出される関数
    * アセンブラ関数

* .cppファイルから、そのファイルの外部で定義された関数を呼び出す場合、
  その.cppファイル内での局所的な関数宣言をしない
  (関数が宣言、定義されているヘッダファイルをインクルードする)。
* コンパイル時に戻り値が確定する関数は[constexpr関数](term_explanation.md#SS_19_4_2)として宣言する。

* [演習-非メンバ関数の宣言](exercise_q.md#SS_20_3_1)

### メンバ関数 <a id="SS_3_3_2"></a>
* 可能な場合(メンバに直接アクセスしない場合)、メンバ関数をstaticにする。
* コンパイル時に戻り値が確定するメンバ関数は[constexpr関数](term_explanation.md#SS_19_4_2)と宣言する。
* オブジェクトの状態を変えないメンバ関数は、constと宣言する。
    * getter(下記の例ではGetString)はconstと宣言する。
    * 下記のSetPtrのような関数はconstにしない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 21

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
    // @@@ example/programming_convention/func_ut.cpp 64

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
  [rvalue](term_explanation.md#SS_19_13_3)である場合、
  そのオブジェクトからその関数を呼び出した戻り値(メンバへのハンドル)を変数で保持しない
  (そのハンドルは[danglingリファレンス](term_explanation.md#SS_19_14_5)/[danglingポインタ](term_explanation.md#SS_19_14_6)になっている)。
  そういった使用方法が必要ならばlvalue修飾、[rvalue修飾](term_explanation.md#SS_19_13_4)を用いたオーバーロード関数を定義する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 84

    char const* s = std::string{"hehe"}.c_str();  // std::string{"hehe"}はrvalue

    std::cout << s << std::endl;  // この時点ではsは解放されている。
```

* [演習-メンバ関数の修飾](exercise_q.md#SS_20_3_2)

#### 特殊メンバ関数 <a id="SS_3_3_2_1"></a>
* [特殊メンバ関数](term_explanation.md#SS_19_3_1)
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
    // @@@ example/programming_convention/class_ut.cpp 455

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

* [演習-特殊メンバ関数の削除](exercise_q.md#SS_20_3_3)

#### コンストラクタ <a id="SS_3_3_2_2"></a>
* クラスが複数の初期化方法を提供する場合でも、
  デフォルト引数を使用し、できる限りコンストラクタを一つに集約する。
* 一つのコンストラクタに集約できない場合、[委譲コンストラクタ](term_explanation.md#SS_19_5_3)等により処理の重複を防ぐ。
  [非静的なメンバ変数](programming_convention.md#SS_3_2_5)処理の重複を避けることは特に重要である。
* オブジェクトの初期化が完了するまでは派生クラスの仮想関数呼び出し等の
  [RTTI](programming_convention.md#SS_3_5_9)機能を使うことはできないため(「[クラスのレイアウト](term_explanation.md#SS_19_3_8)」参照)、
  コンストラクタの中でRTTI機能を使わない(デストラクタでも同様)。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 97

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
    // @@@ example/programming_convention/func_ut.cpp 124

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
  copy代入演算子に対して以下のいずれかを行い、[シャローコピー](term_explanation.md#SS_19_5_9_1)が行われないようにする
  (このルールはファイルディスクリプタ等のリソース管理をするクラス全般に当てはまる)。
    * [ディープコピー](term_explanation.md#SS_19_5_9_2)をさせる。
    * = deleteする(「[特殊メンバ関数](programming_convention.md#SS_3_3_2_1)」参照)。

  またこの場合、moveコンストラクタ、move代入演算子の定義を検討する(「[Copy-And-Swap](design_pattern.md#SS_9_5)」参照)。

* [非explicitなコンストラクタによる暗黙の型変換](term_explanation.md#SS_19_5_4)
  が不要なクラスのコンストラクタに関しては、下記の目的のためにexplicitと宣言する。

    * 仮引数一つのコンストラクタに関しては、[暗黙の型変換抑止](term_explanation.md#SS_19_12_1)する。
    * 仮引数二つ以上のコンストラクタに関しては、
      代入演算子での[一様初期化](term_explanation.md#SS_19_5_6)ができないようにする。  

```cpp
    // @@@ example/programming_convention/func_ut.cpp 146

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
    // @@@ example/programming_convention/func_ut.cpp 200

    A0 a0 = 1;           // NG 1からA0への暗黙の型変換。
                         //    このような変換はセマンティクス的不整合につながる場合がある
    // A1 a1 = 1;        // OK explicitの効果で、意図通りコンパイルエラー

    f_A0(1);             // NG 1からA0への暗黙の型変換のためf_A0が呼び出せてしまう
    // f_A1(1);          // OK explicitの効果で、意図通り以下のようなコンパイルエラー
                         //    error: could not convert ‘1’ from ‘int’ to ‘A1’
    f_A1(A1{1});         // OK f_A1の呼び出し

    auto i = 3;
    A2  a2 = {i, &i};    // NG 代入演算子でのリスト初期化をしている

    // A3 a3 = { i, &i };// OK explicitの効果で、意図通りコンパイルエラー
    A3 a3{i, &i};        // OK リスト初期化
    auto a4 = A3{i, &i}; // OK AAA

    f_A2({i, &i});       // NG { i, &i }からA2への暗黙の型変換のためf_A2が呼び出せてしまう
    // f_A3({i, &i});    // OK explicitの効果で、意図通り以下のようなコンパイルエラー
                         //    error: converting to A3 from initializer list would use explicit 
                         //           constructor A3::A3(int32_t, int32_t*)’
    f_A3(A3{i, &i});     // OK f_A3の呼び出し
```

* 派生クラスが基底クラスの全コンストラクタを必要とする場合、
  [継承コンストラクタ](term_explanation.md#SS_19_5_2)を使用する。

* デフォルト引数はインターフェース関数の呼び出しを簡略化する目的で使用するべきであるため、
  private関数にデフォルト引数を持たせない。

* [演習-委譲コンストラクタ](exercise_q.md#SS_20_3_4)

#### copyコンストラクタ、copy代入演算子 <a id="SS_3_3_2_3"></a>
* copyコンストラクタ、copy代入演算子は[copyセマンティクス](term_explanation.md#SS_19_16_2)に従わせる。
* copyコンストラクタ、copy代入演算子の引数はconstリファレンスにする。
* [RVO(Return Value Optimization)](term_explanation.md#SS_19_17_8)により、
  copyコンストラクタの呼び出しは省略されることがあるため、
  copyコンストラクタ、copy代入演算子はコピー以外のことをしない。
* copy代入演算子は[lvalue修飾](term_explanation.md#SS_19_13_5)をする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 235

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
    // @@@ example/programming_convention/func_ut.cpp 264

    Widget w0{1};
    Widget w1{2};

    w0 = w1;         // これには問題ない
    w1 = Widget{3};  // これにも問題ない

    Widget{2} = w0;  // NG lvalue修飾無しのcopy代入演算子であるため、コンパイルできる
    Widget{3} = Widget{4};  // NG lvalue修飾無しのmove代入演算子であるため、コンパイルできる
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 283

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
    // @@@ example/programming_convention/func_ut.cpp 312

    Widget w0{1};
    Widget w1{2};

    // Widget{2} = w0;          lvalue修飾の効果でコンパイルエラー
    // Widget{3} = Widget{4};   lvalue修飾の効果でコンパイルエラー
```

* [演習-copyコンストラクタ](exercise_q.md#SS_20_3_5)

#### moveコンストラクタ、move代入演算子 <a id="SS_3_3_2_4"></a>
* moveコンストラクタ、move代入演算子は[moveセマンティクス](term_explanation.md#SS_19_16_3)に従わせる。
* moveコンストラクタ、move代入演算子はnoexceptをつけて宣言し、エクセプションを発生させない。
  noexceptでないmoveコンストラクタ、
  move代入演算子を持つクラスをSTLコンテナのtemplate引数として使用した場合、
  moveの代わりにcopyが使用され、パフォーマンス問題を引き起こす場合がある。
* move代入演算子はlvalue修飾(「[copyコンストラクタ、copy代入演算子](programming_convention.md#SS_3_3_2_3)」参照)をする。


* [演習-moveコンストラクタ](exercise_q.md#SS_20_3_6)  

#### 初期化子リストコンストラクタ <a id="SS_3_3_2_5"></a>
* [初期化子リストコンストラクタ](term_explanation.md#SS_19_5_1)は、コンテナクラスの初期化のためのみに定義する。
* 初期化子リストコンストラクタと同じ仮引数を取り得るコンストラクタを定義しない。

#### デストラクタ <a id="SS_3_3_2_6"></a>
* デストラクタの中で[RTTI](programming_convention.md#SS_3_5_9)機能を使わない(「[コンストラクタ](programming_convention.md#SS_3_3_2_2)」参照)。
* デストラクタはnoexceptであり、throwするとプログラムが終了するため、デストラクタでthrowしない。

#### オーバーライド <a id="SS_3_3_2_7"></a>
* [オーバーライドとオーバーロードの違い](term_explanation.md#SS_19_3_9)に注意する。
* オーバーライドしたメンバ関数には、オーバーライドされたメンバ関数の機能の意味を踏襲させる。
* オーバーライドする/される一連の仮想関数(デストラクタを含む)について、
    * 全ての宣言にはvirtualを付ける。
    * 一連の仮想関数の最初でも最後でもないものの宣言には、overrideを付ける。
    * 一連の仮想関数の最後のものの宣言には、overrideを付けず、finalを付ける。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 330

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
    // @@@ example/programming_convention/func_ut.cpp 369

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
    // @@@ example/programming_convention/func_ut.cpp 393

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

* [演習-オーバーライド関数の修飾](exercise_q.md#SS_20_3_8)  

### 非メンバ関数/メンバ関数共通 <a id="SS_3_3_3"></a>

#### サイクロマティック複雑度 <a id="SS_3_3_3_1"></a>
* [サイクロマティック複雑度](term_explanation.md#SS_19_19_3)は15以下が好ましい。
* 特別な理由がない限り、サイクロマティック複雑度は20以下にする。

#### 行数 <a id="SS_3_3_3_2"></a>
* 10行程度が好ましい。
* 特別な理由がない限り、40行以下で記述する。
* [注意] C++の創始者であるビャーネ・ストラウストラップ氏は、
  [プログラミング言語C++ 第4版](https://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9EC-%E7%AC%AC4%E7%89%88-%E3%83%93%E3%83%A3%E3%83%BC%E3%83%8D%E3%83%BB%E3%82%B9%E3%83%88%E3%83%A9%E3%82%A6%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97-ebook/dp/B01BGEO9MS)
  の中で、下記のように述べている。

```
    約 40 行を関数の上限にすればよい。 
    私自身は、もっと小さい平均 7 行程度を理想としている。 
```

* [演習-関数分割](exercise_q.md#SS_20_3_7)  

#### オーバーロード <a id="SS_3_3_3_3"></a>
* [オーバーライドとオーバーロードの違い](term_explanation.md#SS_19_3_9)に注意する。
* オーバーロードされた関数は実行目的を同じにする。
  異なる目的のためには異なる名前の関数を用意する。
* [オーバーライド](programming_convention.md#SS_3_3_2_7)を除き、基底クラスのメンバ関数と同じ名前を持つメンバ関数を派生クラスで宣言、
  定義しない。
  これに反すると[name-hiding](term_explanation.md#SS_19_9_7)のため、基底クラスのメンバ関数の可視範囲を縮小させてしまう。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 407

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
    // @@@ example/programming_convention/func_ut.cpp 464

    int32_t f(int32_t) { return 0; }
    int32_t f(int16_t) { return 1; }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 472

    auto i16 = int16_t{1};

    ASSERT_EQ(1, f(i16));        // f(int16_t)が呼ばれる
    ASSERT_EQ(0, f(i16 + i16));  // f(int32_t)が呼ばれる
```

* 暗黙の型変換による関数の使用範囲の拡張を防ぐには、オーバーロード関数を= deleteする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 484

    // 実引数がdoubleを認めないパターン
    int32_t f0(double) = delete;
    int32_t f0(int32_t a) noexcept { return a / 2; }

    // 実引数がint32_t以外を認めないパターン
    template <typename T>
    int32_t f1(T) = delete;
    int32_t f1(int32_t a) noexcept { return a / 2; }

    // 実引数がunsigned以外を認めないパターン
    template <typename T, std::enable_if_t<!std::is_unsigned_v<T>>* = nullptr>  // C++17スタイル
    uint64_t f2(T) = delete;

    template <typename T, std::enable_if_t<std::is_unsigned_v<T>>* = nullptr>  // C++17スタイル
    uint64_t f2(T t) noexcept
    {
        uint64_t f2_impl(uint64_t) noexcept;

        // Tがsignedで、tが-1のような値の場合、f2_impl(uint64_t)の呼び出しによる算術変換により、
        // tは巨大な値に変換されるが、
        // Tがunsignedならば、f2_impl(uint64_t)の呼び出しによる算術変換は安全

        return f2_impl(t);
    }

    template <typename T>
    uint64_t f3(T) = delete;

    template <std::unsigned_integral T>  // C++20スタイル
    uint64_t f3(T t) noexcept
    {
        uint64_t ret = t;
        // 何らかの処理

        return ret;
    }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 526

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
    // f3(i8);   呼び出そうとしたf3<int8_t>(int8_t)はdeleteされているので意図通りエラー
    f3(ui32);
```

* [演習-オーバーライド/オーバーロード](exercise_q.md#SS_20_3_9)  
* [演習-オーバーロードによる誤用防止](exercise_q.md#SS_20_3_10)  

#### 演算子オーバーロード <a id="SS_3_3_3_4"></a>
* 演算子をオーバーロードする場合、
    * 単項演算子はメンバ関数で定義する。
    * 二項演算子は非メンバ関数で定義する。
* &&, ||, カンマ(,)をオーバーロードしない。
* 型変換オペレータの宣言、定義を多用しない。
* boolへの型変換オペレータは、explicit付きで定義する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 557

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
    // @@@ example/programming_convention/func_ut.cpp 596

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

* 比較演算子のオーバーロードする場合、
    * C++20であれば、[<=>演算子](term_explanation.md#SS_19_6_8_3)を定義する。
    * C++17以下であれば、`operator==`と`operator<`の2つの演算子がを定義し、
      [std::rel_ops](term_explanation.md#SS_19_6_8_1)を使用する。

* [ユーザ定義リテラル演算子](term_explanation.md#SS_19_6_6_1)のサフィックスには、
  アンダーバーから始まる3文字以上の文字列を使用する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 638

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
    // @@@ example/programming_convention/func_ut.cpp 666

    auto km = int32_t{3_kilo_meter};  // ユーザ定義リテラル演算子の利用
    auto m  = int32_t{3000_meter};    // ユーザ定義リテラル演算子の利用

    ASSERT_EQ(m, km);
```

#### 実引数/仮引数 <a id="SS_3_3_3_5"></a>
* 仮引数(「[実引数/仮引数](term_explanation.md#SS_19_17_2)」参照)の数は、4個程度を上限とする。
* 仮引数を関数の戻り値として利用しない場合
  (且つ仮引数が関数テンプレートの[ユニバーサルリファレンス](term_explanation.md#SS_19_14_1)でない場合)、
    * 基本型やその型のエイリアス、enumは値渡しにする。
    * それ以外のオブジェクトはconstリファレンス渡しにする
      (「[const/constexprインスタンス](programming_convention.md#SS_3_1_9)」参照)。
      ただし、数バイトの小さいオブジェクトは値渡ししても良い。
    * 「引数がnullptrである場合の処理をその関数が行う」場合、constポインタ渡しにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 684

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

* [ユニバーサルリファレンス](term_explanation.md#SS_19_14_1)を仮引数とする関数テンプレートでは、仮引数は非constにする。

* 継承の都合等で、使用しないにもかかわらず定義しなければならない仮引数には名前を付けない。
  仮引数が使用されていない警告の抑止のために[属性構文](term_explanation.md#SS_19_7_1)を使わない。
  
* 関数f()の仮引数が2つ以上であり、f()に渡す引数をそれぞれに生成する関数があった場合、
  引数を生成する関数の戻り値を直接f()に渡さない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 708

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
    // @@@ example/programming_convention/func_ut.cpp 741

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
    // @@@ example/programming_convention/func_ut.cpp 757

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
  (「[スライシング](term_explanation.md#SS_19_5_9_3)」で述べたように、
  特に基底クラスを配列にすることは危険である)。
  代わりに配列へのリファレンスもしくはstd::arrayを使用する。 

```cpp
    // @@@ example/programming_convention/func_ut.cpp 780

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
    // @@@ example/programming_convention/func_ut.cpp 835

    Base    b[]{"0", "0"};
    Derived d[]{{"0", "1"}, {"2", "3"}};

    ASSERT_EQ((std::vector<std::string>{"0", "0"}), f(b, array_length(b)));  // OK これは良いが
    ASSERT_EQ((std::vector<std::string>{"0", "0"}), g(b, array_length(b)));  // OK これは良いが

    // 本来なら、下記のようになるべきだが、
    // ASSERT_EQ((std::vector<std::string>{"0", "2"}), f(d, array_length(d)));  // NG
    // ASSERT_EQ((std::vector<std::string>{"0", "2"}), g(d, array_length(d)));  // NG

    // レイアウトずれにより、下記のようになる
    ASSERT_EQ((std::vector<std::string>{"0", "1"}), f(d, array_length(d)));  // NG
    ASSERT_EQ((std::vector<std::string>{"0", "1"}), g(d, array_length(d)));  // NG
```

```cpp
    // @@@ example/programming_convention/func_ut.cpp 855

    // ポインタではなく、配列へのリファレンスを使用することで、
    // 上記のようなバグを避けることができる

    std::vector<std::string> f_ref_2(Base const (&array)[2])  // OK 配列へのリファレンス
    {
        auto ret = std::vector<std::string>{array_length(array)};

        // arrayの型はポインタではなく、リファレンスなのでstd::endが使える
        std::transform(array, std::end(array), ret.begin(),
                       [](Base const& b) noexcept { return b.Name0(); });

        return ret;
    }

    template <size_t N>                                       // 配列の長さの型はsize_t
    std::vector<std::string> f_ref_n(Base const (&array)[N])  // OK 配列へのリファレンス
    {
        auto ret = std::vector<std::string>{N};

        std::transform(array, std::end(array), ret.begin(), [](auto& b) noexcept { return b.Name0(); });

        return ret;
    }

    template <typename T, size_t N>                      // 配列の長さの型はsize_t
    std::vector<std::string> g_ref(T const (&array)[N])  // OK 配列へのリファレンス
    {
        auto ret = std::vector<std::string>{N};

        std::transform(array, std::end(array), ret.begin(), [](auto& b) noexcept { return b.Name0(); });

        return ret;
    }

    template <typename T, size_t N>  // std::arrayの第2パラメータの型はsize_t
    std::vector<std::string> h_ref(std::array<T, N> const& array)  // OK std::arrayへのリファレンス
    {
        auto ret = std::vector<std::string>{N};

        std::transform(std::begin(array), std::end(array), ret.begin(),
                       [](auto& b) noexcept { return b.Name0(); });

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
    // @@@ example/programming_convention/func_ut.cpp 924
    Base    b[]{"0", "0"};
    Derived d[]{{"0", "1"}, {"2", "3"}};
    auto    d2 = std::array<Derived, 2>{Derived{"0", "1"}, Derived{"2", "3"}};

    ASSERT_EQ((std::vector<std::string>{"0", "0"}), f_ref_2(b));  // OK
    ASSERT_EQ((std::vector<std::string>{"0", "0"}), f_ref_n(b));  // OK
    ASSERT_EQ((std::vector<std::string>{"0", "0"}), g_ref(b));    // OK

    // ASSERT_EQ((std::vector<std::string>{"0", "2"}), f_ref_2(d));  OK 誤用なのでコンパイルエラー
    ASSERT_EQ((std::vector<std::string>{"0", "2"}), g_ref(d));   // OK
    ASSERT_EQ((std::vector<std::string>{"0", "2"}), h_ref(d2));  // OK

    // 配列へのポインタを使う場合
    ASSERT_EQ((std::vector<std::string>{"0", "0"}), g_ptr(&b));  // OK

    Derived(*d_null)[3]{nullptr};
    ASSERT_EQ((std::vector<std::string>{}), g_ptr(d_null));  // OK
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
    // @@@ example/programming_convention/func_ut.cpp 945

    int32_t default_arg{0};
    int32_t get_default_arg(int32_t a = default_arg) noexcept { return a; }
```
```cpp
    // @@@ example/programming_convention/func_ut.cpp 954

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
    // @@@ example/programming_convention/func_ut.cpp 966

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

* [演習-仮引数の修飾](exercise_q.md#SS_20_3_11)  

#### 自動変数 <a id="SS_3_3_3_6"></a>
* 一つの文で複数の変数の宣言をしない。
* 自動変数は、それを使う直前に定義することでスコープを最小化する。
* 自動変数は、定義と同時に初期化する。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1032

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

#### 戻り値型 <a id="SS_3_3_3_7"></a>
* メモリアロケータ以外の関数の戻り値をvoid\*にしない。
* 避けがたい理由なしに以下のシンタックスを使用しない。
    * [戻り値型を後置する関数宣言](term_explanation.md#SS_19_11_4)
    * [関数の戻り値型auto](term_explanation.md#SS_19_11_5)
    * [後置戻り値型auto](term_explanation.md#SS_19_11_6)

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1135

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
  パフォーマンスに著しい悪影響がない限り、リファレンス引数で戻り値を返さない。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1148

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
    // @@@ example/programming_convention/func_ut.cpp 1181

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
    // @@@ example/programming_convention/func_ut.cpp 1239

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
    // @@@ example/programming_convention/func_ut.cpp 1296

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


#### constexpr関数 <a id="SS_3_3_3_8"></a>
* 引数が[constexpr](term_explanation.md#SS_19_4)の場合、コンパイル時に評価が確定する関数テンプレートもしくはinline関数は、
  [constexpr関数](term_explanation.md#SS_19_4_2)として宣言する。
* [constexpr関数](term_explanation.md#SS_19_4_2)がコンパイル時に評価される必要がある場合、
  [constexpr](term_explanation.md#SS_19_4)の代わりに[consteval](term_explanation.md#SS_19_4_5)を使用する。

* [演習-constexpr関数](exercise_q.md#SS_20_3_12)  

#### リエントラント性 <a id="SS_3_3_3_9"></a>
* 関数、メンバ関数はなるべくリエントラントに実装する。
* 複数のスレッドから呼び出される関数は必ずリエントラントにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1352

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

#### エクセプション処理 <a id="SS_3_3_3_10"></a>
* 関数はそれが不可避でない限り、[no-fail保証](term_explanation.md#SS_19_15_1)をする。
  [no-fail保証](term_explanation.md#SS_19_15_1)関数は[noexcept](term_explanation.md#SS_19_15_4)を使用してそのことを明示する。
* throwをせざるを得ない場合、最低でも[基本保証](term_explanation.md#SS_19_15_3)をする。
* STLコンテナ(std::string, std::vector等)が発生させるエクセプションはtry-catchせず
  (catchしてデバッグ情報を保存するような場合を除く)、
  プログラムをクラッシュさせる。try-catchしてもできることはない。
* 特別な理由がない限り、コンストラクタ呼び出しは[noexcept](term_explanation.md#SS_19_15_4)と宣言する。
  ネットワーク接続等、簡単にエラーすることをコンストラクタ内で行わない。
* [オープン・クローズドの原則(OCP)](solid.md#SS_8_2)、[リスコフの置換原則(LSP)](solid.md#SS_8_3)に違反する場合が多いため、
  「throwキーワードによるエクセプション仕様」を使用しない(C++17で廃止)。
* エクセプションをthrowしないことが確定している関数は、[noexcept](term_explanation.md#SS_19_15_4)と宣言する。
  move代入演算子を[noexcept](term_explanation.md#SS_19_15_4)と宣言することは特に重要である。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1383

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
    * 実態で受け取るとオブジェクトの[スライシング](term_explanation.md#SS_19_5_9_3)が起こる場合がある。
    * 受け取ったエクセプションオブジェクトを書き換えるべきではない。

* エクセプションによるリソースリークを避けるため[RAII(scoped guard)](design_pattern.md#SS_9_9)でリソースを管理する。
* 一連のcatch節では、catchするエクセプションの型の最もマッチ率の高いcatch節で処理されるのではなく、
  マッチした最上位のcatch節で処理されるため、
  catchするエクセプションの型に継承関係があるのであれば、継承順位が低い順番にcatchする。
  また、catch(...)は一番最後に書く(関数tryブロックの場合も同様にする)。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1403

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
  (「[ファイル位置を静的に保持したエクセプションクラスの開発](template_meta_programming.md#SS_13_7_6_4)」参照)。


* noexceptと宣言された関数へのポインタへ、noexceptでない関数のポインタを代入しない
  (C++17では[ill-formed](term_explanation.md#SS_19_17_4)になる)。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1466

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

* [演習-エクセプションの型](exercise_q.md#SS_20_3_13)  

#### ビジーループ <a id="SS_3_3_3_11"></a>
* 待ち合わせにビジーループを使わない。イベントドリブンにする。

```cpp
    // @@@ example/programming_convention/func_ut.cpp 1528

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

## 構文 <a id="SS_3_4"></a>

### 複合文 <a id="SS_3_4_1"></a>
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

### switch文 <a id="SS_3_4_2"></a>
* caseラベル、defaultラベルに関連付けられた一連の文はできだけフォールスルーさせない。
  実装がシンプルになる等の理由からフォールスルーさせる場合、
  [属性構文](term_explanation.md#SS_19_7_1)を使用しそれが意図的であることを明示するため以下のような記述する。

```cpp
    // fallthrough          // C++14以前

    [[fallthrough]];        // C++17以降
```

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

* switch文のオペランド変数を生成する場合、
  できるだけ[初期化付きswitch文](term_explanation.md#SS_19_7_5_3)を使用し、その変数のスコープを最小に留める。

### if文 <a id="SS_3_4_3"></a>
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
* ifの条件式が、コンパイル時に定まるのであれば、[constexpr if文](term_explanation.md#SS_19_10_8)を使用する。

* if文のオペランド変数を生成する場合、
  できるだけ[初期化付きif文](term_explanation.md#SS_19_7_5_2)を使用し、その変数のスコープを最小に留める。

### while文 <a id="SS_3_4_4"></a>
* while文には、[初期化付きif文](term_explanation.md#SS_19_7_5_2)/[初期化付きswitch文](term_explanation.md#SS_19_7_5_3)のような構文は存在しないが、
  while文のオペランド変数を生成するする場合、
  [初期化付きfor文(従来のfor文)](term_explanation.md#SS_19_7_5_1)を使用し、その変数のスコープを最小に留める。

### 範囲for文 <a id="SS_3_4_5"></a>
* 配列やコンテナの全要素にアクセスするような繰り返し処理には、
  [off-by-oneエラー](https://ja.wikipedia.org/wiki/Off-by-one%E3%82%A8%E3%83%A9%E3%83%BC)
  が避けられ、従来よりもシンプルに記述できる[範囲for文](term_explanation.md#SS_19_7_3)を使用する。

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
  cbegin()、cend()も定義し、そのコンテナに[範囲for文](term_explanation.md#SS_19_7_3)を適用できるようにする
  (「[デバッグ用イテレータ](dynamic_memory_allocation.md#SS_14_2_4)」参照)。

* [演習-コンテナの範囲for文](exercise_q.md#SS_20_4_1)  

### 制御文のネスト <a id="SS_3_4_6"></a>
* breakとの関係がわかりづらい、ブロックが巨大になる等の問題があるため、
  if, for, while, do-while, switch文に付随するブロックの中にswitch文を書かない。

### return文 <a id="SS_3_4_7"></a>
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

### goto文 <a id="SS_3_4_8"></a>
* 二重以上のループを抜ける目的以外でgotoを使用しない。
* 二重以上のループを抜ける目的でgotoを使用する場合、gotoのジャンプ先ラベルはそのループの直後に置く。

### ラムダ式 <a id="SS_3_4_9"></a>
* [ラムダ式](term_explanation.md#SS_19_8_3)を複雑にしない。
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

    #if __cplusplus == 201703L  // =でのキャプチャは範囲は大きすぎるため、C++20から非推奨
            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [=](auto const& str) noexcept { return (strs_.size() < length); });

    #elif __cplusplus == 202002L
            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [&strs = strs_, length = length](auto const& str) noexcept {
                             return (strs.size() < length);
                         });
    #else
            static_assert(false, "C++ version not supported!");
    #endif

            return ret;
        }

    private:
        std::vector<std::string> strs_;
    };
```

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 297

    // OK 限定したキャプチャにより、ラムダ式から可視である変数が限定された
    class A {
    public:
        ...
        std::vector<std::string> GetNameLessThan(uint32_t length) const
        {
            auto ret = std::vector<std::string>{};

    #if __cplusplus == 201103L  // c++11
                                // [length]を代入キャプチャと呼ぶ。

            std::copy_if(strs_.cbegin(), strs_.cend(), std::back_inserter(ret),
                         [length](std::string const& str) noexcept { return (str.size() < length); });

    #elif __cplusplus >= 201402L  // c++14以降
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
    // @@@ example/programming_convention/syntax_ut.cpp 333

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

* C++17以降では、 コンパイル時に戻り値が確定するラムダ式の呼び出し式は定数にできるため、
  そのようなラムダ式は[constexprラムダ](term_explanation.md#SS_19_4_6)として宣言する。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 371

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
    // @@@ example/programming_convention/syntax_ut.cpp 392

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

* [演習-ラムダ式](exercise_q.md#SS_20_4_2)  
* [演習-ラムダ式のキャプチャ](exercise_q.md#SS_20_4_3)  

### マクロの中の文 <a id="SS_3_4_10"></a>
* マクロの中に文がある場合、do-while(0)イデオムを使用する(「[関数型マクロ](programming_convention.md#SS_3_6_1)」参照)。

```cpp
    // @@@ example/programming_convention/syntax_ut.cpp 420

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

## 演算子 <a id="SS_3_5"></a>

### 優先順位 <a id="SS_3_5_1"></a>
* [厳密な式の評価順](cpp_improve.md#SS_18_3_2_1)で評価順位が決まっていても、一見優先順位が分かりづらい式では、
  順序を明示するために丸括弧を使う。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 18

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
    // @@@ example/programming_convention/operator_ut.cpp 60
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

### 代入演算 <a id="SS_3_5_2"></a>
* [単純代入](term_explanation.md#SS_19_17_3)のみからなる文を除き、1つの文で複数の代入を行わない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 87

    a = b = 0;              // OK
    b     = (a += 1) + 2;   // NG
    b     = (a++) + (c++);  // NG

    b = b++;  // NG unary operators assign itself.

    ++a;         // OK
    auto i = a;  // OK

    a = 0;                 // OK
```

* 一部の例外を除き、ifの条件文の中で代入しない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 104

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

### ビット演算 <a id="SS_3_5_3"></a>
* オーバーフロー、アンダーフローしたときの符号の扱い方が未定義であるため、
  signed変数へのビット演算を使用しない。
  (「2の階乗での除算は、ビット演算に置き換えることで実行速度が速くなる」というのは都市伝説である)。
* [注意] ビット演算にはstd::bitsetや[BitmaskType](design_pattern.md#SS_9_2)を使用することもできる。

### 論理演算 <a id="SS_3_5_4"></a>
* &&や||の論理演算子の右オペランドで[副作用](term_explanation.md#SS_19_19_5)のある処理をしない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 138

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

### 条件演算子 <a id="SS_3_5_5"></a>
* 単純なif文よりも、条件演算子を優先して使用する
  (const変数の条件付き初期化は条件演算子でのみ可能である)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 170

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

* [演習-条件演算子](exercise_q.md#SS_20_5_1)  

### メモリアロケーション <a id="SS_3_5_6"></a>
#### new <a id="SS_3_5_6_1"></a>
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

#### delete <a id="SS_3_5_6_2"></a>
* [不完全型](term_explanation.md#SS_19_3_6)のオブジェクトへのポインタをdeleteしない。
  特に「[Pimpl](design_pattern.md#SS_9_3)」を使用する場合には注意が必要である。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 204

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
    // @@@ example/programming_convention/operator_ut.cpp 226

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
    // @@@ example/programming_convention/operator_ut.cpp 246

    if (ptr != nullptr) {  // NG nullptrとの比較は不要
        delete ptr;
    }

    ...

    delete ptr;  // OK ptrがnullptrでも問題ない
```

* [演習-delete](exercise_q.md#SS_20_5_2)  

#### メモリ制約が強いシステムでの::operator new <a id="SS_3_5_6_3"></a>
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


### sizeof <a id="SS_3_5_7"></a>
* sizeof(型名)とsizeof(インスタンス名)の両方が使える場合、sizeof(インスタンス名)を優先的に使用する。
* ポインタ型変数に関して、それが指しているインスタンスのサイズを獲得する場合は、
  sizeof(\*ポインタ型変数名)を使用する
  (そのポインタがnullptrであってもデリファレンスされないので問題ない)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 272

    uint8_t  a = 0;
    uint8_t* b = &a;

    auto s_0 = sizeof(uint8_t);  // NG aのサイズをs_0に代入したい場合
    auto s_1 = sizeof(a);        // OK aのサイズをs_1に代入したい場合
    auto s_2 = sizeof(*b);       // OK *bのサイズをs_2に代入したい場合
```

* 上記例を除き、sizeof演算子のオペランドは一見[副作用](term_explanation.md#SS_19_19_5)を持っているような式を含んではならない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 284

    a = 0;

    auto size_3 = sizeof(++a);  // NG  おそらく意図通りには動かない
                                // この行でもa == 0(++aは効果がない)
```

* C++03のテンプレートの実装でよく使われたsizeofによるディスパッチを行わない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 297

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
    // @@@ example/programming_convention/operator_ut.cpp 314

    static_assert(sizeof(sizeof_dispatch(int{})) == sizeof(True), "int32_t is int");
    static_assert(sizeof(sizeof_dispatch(std::string{})) != sizeof(True), "int32_t is not string");

    // 上記はC++11では下記のように実装すべき
    static_assert(std::is_same_v<int, int32_t>, "int32_t is int");
    static_assert(!std::is_same_v<std::string, int32_t>, "int32_t is not string");

```

* 一見、配列に見えるポインタをsizeofのオペランドにしない。
  (「[実引数/仮引数](programming_convention.md#SS_3_3_3_5)」参照)。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 329

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

* [演習-sizeof](exercise_q.md#SS_20_5_3)  

### ポインタ間の演算 <a id="SS_3_5_8"></a>
* 同一オブジェクト(配列等)の要素を指さないポインタ間の除算や比較をしない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 365

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

### RTTI <a id="SS_3_5_9"></a>
* [注意] [RAII(scoped guard)](design_pattern.md#SS_9_9)との混乱に気を付ける。
* [Run-time Type Information](term_explanation.md#SS_19_17_13)を使用したラインタイム時の型による場合分けは、
  それ以外に解決方法がない場合や、実装が大幅にシンプルになる場合を除き行わない
  (「[等価性のセマンティクス](term_explanation.md#SS_19_16_1)」参照)。
    * 単体テストやロギングのでtypeidの使用は問題ない。
    * 派生クラスの型によって異なる動作にしたい場合には、仮想関数を使うか、
      [Visitor](design_pattern.md#SS_9_20)パターン等により実現できる。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 385

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
    // @@@ example/programming_convention/operator_ut.cpp 473

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

* [演習-dynamic_castの削除](exercise_q.md#SS_20_5_4)  

### キャスト、暗黙の型変換 <a id="SS_3_5_10"></a>
* キャストが必要な式等は、設計レベルの問題を内包していることがほとんどであるため、設計を見直す。
* Cタイプキャストは使用しない。
* const_cast、 dynamic_castはそれ以外に解決方法がない場合や、
  実装が大幅にシンプルになる場合を除き使用しない。
* reinterpret_castはハードウエアレジスタ等のアドレスを表す目的以外で使用しない。
* ダウンキャストを行う目的でstatic_castを使用しない。

```cpp
    // @@@ example/programming_convention/operator_ut.cpp 526
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
    // @@@ example/programming_convention/operator_ut.cpp 550

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
    // @@@ example/programming_convention/operator_ut.cpp 578

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

* [演習-キャスト](exercise_q.md#SS_20_5_5)  

## プリプロセッサ命令 <a id="SS_3_6"></a>
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
  #if等で囲まれた区間をなるべく短くする。
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


### 関数型マクロ <a id="SS_3_6_1"></a>
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
  (「[マクロの中の文](programming_convention.md#SS_3_4_10)」参照)。

### マクロ定数 <a id="SS_3_6_2"></a>
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

## パッケージとその構成ファイル <a id="SS_3_7"></a>

### パッケージの実装と公開 <a id="SS_3_7_1"></a>
* パッケージに関して、以下の構造を持つようにソースコードを構成する
  (「[アーキテクチャとファイル構造](architecture.md#SS_10_3)」参照)。
    * ソフトウェアはパッケージに分割される。
    * パッケージは、複数のヘッダファイルと複数の.cppファイルから作られる。
    * パッケージを構成するファイルは、このパッケージ専用ディレクトリに保存される。
    * パッケージは他のパッケージとは排他的な[名前空間](programming_convention.md#SS_3_8_2)を持ち、
      パッケージ内で宣言、定義され、外部パッケージに公開される識別子はその名前空間に包含される。
      外部パッケージに公開されない識別子は、そのパッケージでのみ使用される名前空間か、
      無名名前空間に包含されるようにする。
    * パッケージは、サブパッケージを内包する場合がある。
      サブパッケージは、パッケージの要件を満たす。

* 上記前提のもと、パッケージが外部にサービスを提供する場合、
  そのパッケージで定義されるヘッダファイルは以下のどちらかのみを行うように構成する。
    * 外部へ提供するクラス等を公開する(外部公開ヘッダファイル)。
    * パッケージ内部のみで使用するクラス等の宣言、定義を行う(外部非公開ヘッダファイル)。

<!-- pu:plant_uml/package.pu--><p><img src="data:image/png;base64,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" /></p>

* h/PackageBのディレクトリPackageBは冗長に見えるが、
  h配下にそれを保持するディレクトリ名と同じ名前のディレクトリを持つことは、
  可読性の観点から重要である。
  このディレクトリため、他のパッケージから識別子をインポートするためのインクルードディレクティブは
  以下のように記述されることになる。
  このような記述を可能とするために、
  PackageBがエクスポートするヘッダを使用するコードのコンパイルに
 「インクルールパスにPackageB/hを指定する」オプションを使用する。

```cpp
    // @@@ example/programming_convention/pkg.cpp 1

    // PackageC内の*.cppファイルの内部とする
    #include <memory>  // システムヘッダ
    #include <mutex>   // システムヘッダ
    #include <string>  // システムヘッダ

    // PackageBがエクスポートするするヘッダを使用するために、
    // 以下のようなコンパイルオプションが必要になる
    //      -I<DIR>/PackageA/h
    // <DIR>はコンパイラが実行されるディレクトリ
    //
    #include "PackageA/xxx.h"  // PackageAのインクルード
    #include "PackageB/b0.h"   // PackageBのインクルード
    #include "PackageB/b3.h"   // PackageBのインクルード
    #include "internal.h"      // パッケージ外部非公開ヘッダのインクルード
```

* 外部公開ヘッダファイルは、ビルド時に他のパッケージから参照できるディレクトリに配置する。
    * 外部公開ヘッダファイルは、外部非公開ヘッダファイルをインクルードしない。
    * 外部非公開ヘッダファイルは、ビルド時に他のパッケージから参照できるディレクトリに配置しない。

### 識別子の宣言、定義 <a id="SS_3_7_2"></a>
* [ODR](https://en.cppreference.com/w/cpp/language/definition)を守る。
  つまり、一つの識別子は全ソースコード内にただ一つの定義を持つようにする。
* 一つの.cppファイル内のみで使用される識別子は、
  その.cppファイル内の無名名前空間にその定義や宣言を持つ。
* ヘッダファイルで宣言された識別子が.cppファイル内に定義をもつ場合、
  その.cppファイルにそのヘッダファイルをインクルードさせる。
  特に、非メンバ関数や変数の宣言と定義を矛盾させないために、このルールは特に重要である
  (「[非メンバ関数](programming_convention.md#SS_3_3_1)」参照)。

### 依存関係 <a id="SS_3_7_3"></a>
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

<!-- pu:plant_uml/package_ng.pu--><p><img src="data:image/png;base64,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" /></p>

### 二重読み込みの防御 <a id="SS_3_7_4"></a>
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

### ヘッダファイル内の#include <a id="SS_3_7_5"></a>
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

### #includeするファイルの順番 <a id="SS_3_7_6"></a>
* ユーザ定義ヘッダファイルより、システムヘッダファイルの#includeを先に行う。
* システムヘッダファイルは、アルファベット順に#includeを行う。
* ユーザ定義ヘッダファイルは、アルファベット順に#includeを行う。

### #includeで指定するパス名 <a id="SS_3_7_7"></a>
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

## スコープ <a id="SS_3_8"></a>
### スコープの定義と原則 <a id="SS_3_8_1"></a>
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

* このドキュメント執筆時のコンパイラ/ビルダのC++20での[モジュール](term_explanation.md#SS_19_8_2)のサポート状況が
  万全ではないため、
    * モジュールを定義するためのmoduleを使用しない。
    * モジュール外に公開する識別子を定義するexport使用しない。
    * exportされた識別子を使用するためにimportを使用しない。

* [name-hiding](term_explanation.md#SS_19_9_7)を起こすとコードの可読性が著しく低下するため、
  スコープが重複する「名前のない名前空間内」(例えば、ブロックとそれを内包するブロック)
  にある「同一名を持つ識別子」を宣言、定義しない。

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

### 名前空間 <a id="SS_3_8_2"></a>
* グローバル名前空間には下記以外の識別子を定義、宣言しない。
    * main関数
    * グローバルnewのオーバーロード
    * Cとシェアする識別子
* パッケージ毎に名前空間を定義する
  (「[パッケージの実装と公開](programming_convention.md#SS_3_7_1)」、[名前空間名](naming_practice.md#SS_6_2_11)」参照)。
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

### using宣言/usingディレクティブ <a id="SS_3_8_3"></a>
* 識別子のインポートのための[using宣言](term_explanation.md#SS_19_9_12)は下記のような場合のみに使用する
  (「[継承コンストラクタ](term_explanation.md#SS_19_5_2)」、「[オーバーライドとオーバーロードの違い](term_explanation.md#SS_19_3_9)」参照)。

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

* 下記のような場合を除き、[usingディレクティブ](term_explanation.md#SS_19_9_13)は使用しない。
  使用する場合でもその効果をブロックスコープ内のみに留める。

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

* [演習-usingディレクティブ](exercise_q.md#SS_20_6_1)  

### ADLと名前空間による修飾の省略 <a id="SS_3_8_4"></a>
* 名前空間の修飾を省略した識別子のアクセスには、
  下記のような副作用があるため、[ADL](term_explanation.md#SS_19_9_5)を使用する目的以外で使用しない
  (「[識別子の命名](naming_practice.md#SS_6_2)」を順守することで、識別子の偶然の一致を避けることも必要)。

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


### 名前空間のエイリアス <a id="SS_3_8_5"></a>
* ネストされた長い名前空間を短く簡潔に書くための名前空間エイリアスは、
  その効果をブロックスコープ内のみに留める。
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

## ランタイムの効率 <a id="SS_3_9"></a>
* ランタイム効率と、可読性のトレードオフが発生する場合、可読性を優先させる。
* やむを得ず可読性を落とすコードオプティマイゼーションを行う場合は、
  プロファイリング等を行い、ボトルネックを確定させ、必要最低限に留める。
  また、開発早期での可読性を落とすコードオプティマイゼーションは行わない。

### 前置/後置演算子の選択 <a id="SS_3_9_1"></a>
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

### operator X、operator x=の選択 <a id="SS_3_9_2"></a>
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

```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 99

    auto a = A{1};
    auto b = A{2};

    a = a + b;  // NG 無駄なコピーが発生する
    ASSERT_EQ(a.Value(), 3);

    a += b;  // OK 無駄なコピーが発生しない
    ASSERT_EQ(a.Value(), 5);
```

* ソースコードの統一性のため、このオーバーヘッドがない基本型についても、同じルー ルを適用する。

### 関数の戻り値オブジェクト <a id="SS_3_9_3"></a>
* 基本型やenum、
  std::unique_ptr<>、std::optional<>
  等のサイズの小さいクラス以外のオブジェクトを関数の戻り値にしない。
* [注意] ローカルオブジェクトに対して[RVO(Return Value Optimization)](term_explanation.md#SS_19_17_8)が有効であれば、
  そのオブジェクトを戻り値にしても良い。
* [注意] stdのコンテナは、RVOが有効でなくてもmoveが行われるため、関数の戻り値として使用しても良い。
* [注意] std::stringについては、RVOに加えて、
  [SSO(Small String Optimization)](term_explanation.md#SS_19_17_9)が使用されていることが多い。
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

### move処理 <a id="SS_3_9_4"></a>
* [ディープコピー](term_explanation.md#SS_19_5_9_2)の実装を持つクラスへのcopy代入の多くがrvalueから行われるのであれば、
  moveコンストラクタや、move代入演算子も実装する。
* 関数の戻り値にローカルオブジェクトを使用する場合、
  [RVO(Return Value Optimization)](term_explanation.md#SS_19_17_8)の阻害になるため、そのオブジェクトをstd::moveしない。

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

### std::string vs std::string const& vs std::string_view <a id="SS_3_9_5"></a>
* 文字列を受け取る関数の仮引数の型に関しては下記のような観点に気を付ける。
  以下に示す通り、このような仮引数の型をstd::string const&にすることが最適であるとは限らない。

```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 187
    // テスト０用関数

    void f0(std::string const& str) { /* strを使用した何らかの処理 */ }
    void f1(std::string str)        { /* strを使用した何らかの処理 */ }
    void f2(std::string_view str)   { /* strを使用した何らかの処理 */ }
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 200
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
    // 従って、文字列リテラルを関数に渡す場合の引数の型は、
    // std::string const&か、std::string_viewとするのが効率的である。
```
```cpp
    // @@@ example/programming_convention/runtime_ut.cpp 224
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
    // @@@ example/programming_convention/runtime_ut.cpp 253
    // テスト１用クラス

    class A0 {
    public:
        A0(std::string const& str) : str_{str} {}

    private:
        std::string str_;
    };

    class A1 {
    public:
        A1(std::string str) : str_{std::move(str)} {}  // strの一時オブジェクトをmoveで利用

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
    // @@@ example/programming_convention/runtime_ut.cpp 308
    // テスト１―１

    auto a0_msec = MeasurePerformance(10000000, [] { A0 a{__func__}; });
    auto a1_msec = MeasurePerformance(10000000, [] { A1 a{__func__}; });
    auto a2_msec = MeasurePerformance(10000000, [] { A2 a{__func__}; });

    // このドキュメントを開発しているPCでは上記の結果は以下の様になる。
    // A0 :834 msec
    // A1 :774 msec
    // A2 :704 msec
    // つまり、A2 < A1 < A0であり、A0の効率がやや悪い。
    // 従って、文字列リテラルを関数に渡す場合の引数の型は、
    // std::stringか、std::string_viewとするのが効率的である。
    //
    // コンストラクタのインターフェースとしては、
    // 実引数オブジェクトのライフタイムを考慮しなくて良いため、A0よりもA1の方が優れている。
    // この観点と、テスト１－０、テスト１－１の結果を総合的に考えれば、
    // このような場合の引数の型は、std::stringを選択すべきだろう。
```

### extern template <a id="SS_3_9_6"></a>
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

## 標準クラス、関数の使用制限 <a id="SS_3_10"></a>
### STL <a id="SS_3_10_1"></a>
* C++のバージョン毎に定められた非推奨の機能、関数、クラスを使わない。
  これらについては、[C++日本語リファレンス](https://cpprefjp.github.io/)の
  * [C++11の機能変更](https://cpprefjp.github.io/lang/cpp11.html)
  * [C++14の機能変更](https://cpprefjp.github.io/lang/cpp14.html)
  * [C++17の機能変更](https://cpprefjp.github.io/lang/cpp17.html)
  に詳細が書かれている。

* [g++](term_explanation.md#SS_19_18_1)/[clang++](term_explanation.md#SS_19_18_2)等の優れたコンパイラを適切なオプションで使用することで、
  非推奨の機能、関数、クラスの使用を防ぐ。

#### スマートポインタの使用制限 <a id="SS_3_10_1_1"></a>
* std::auto_ptrを使用しない(C++17で廃止)。
* ダイナミックに生成したオブジェクトの管理にはstd::unique_ptr<>を使用する。
  std::unique_ptr<>では機能が足りない場合のみ、std::shared_ptr<>を使用する。

#### 配列系コンテナクラスの使用制限 <a id="SS_3_10_1_2"></a>
* 配列系のコンテナを使用する場合、コンパイル時に要素数の上限が
    * 定まるのであれば、std::arrayを使用する。
    * 未定ならば、std::vectorを使用する。
* std::vector\<bool\>は、std::vectorの特殊化であり、通常のstd::vectorと同じようには扱えない。
  std::vector\<bool\>を使用する場合、その要素へのハンドルがbool&やbool\*でないことに注意する。
* std::arrayを除くコンテナクラスは、
  それ自体でメモリリソースの[RAII(scoped guard)](design_pattern.md#SS_9_9)を実現しているため、newしない。

#### std::stringの使用制限 <a id="SS_3_10_1_3"></a>
* std::stringは、
  それ自体でメモリリソースの[RAII(scoped guard)](design_pattern.md#SS_9_9)を実現しているため、newしない。
* std::stringの添字演算子[]は領域外アクセスを通知しない
  ([std::out_of_range](https://cpprefjp.github.io/reference/stdexcept.html)
  エクセプションを発生させない)ため、std::string::at() を使用する
  (「[安全な配列型コンテナ](template_meta_programming.md#SS_13_2_3)」参照)。
* std::string.data()は、C++のバージョンによってはNULLターミネイトが保証されていないため、
  std::string.c_str() を使用する。

#### std::string_viewの使用制限 <a id="SS_3_10_1_4"></a>
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


### POSIX系関数 <a id="SS_3_10_2"></a>
#### 使用禁止関数一覧 <a id="SS_3_10_2_1"></a>

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

#### 使用禁止関数の理由や注意点 <a id="SS_3_10_2_2"></a>
##### バッファオーバーランを引き起こしやすい関数 <a id="SS_3_10_2_2_1"></a>
* 以下の関数は、バッファオーバーフロー等のバグを引き起こしやすい。

```
    gets(), scanf(), strcpy(), strcat(), sprintf(), vsprintf(), wcscat(), wcscpy()
```

##### コマンドインジェクション防止 <a id="SS_3_10_2_2_2"></a>
* 以下の関数は、外部コマンドの実行時に環境変数に依存してしまう。

```
    execl(), execlp(), execv(), execvp(), popen(), system()
```

##### obsolete関数 <a id="SS_3_10_2_2_3"></a>
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

##### LEGACY関数 <a id="SS_3_10_2_2_4"></a>
* 以下の関数は、すでに役目を終えた。

```
    sigstack(), cuserid(), getopt(), getw(), ttyslot(), valloc(), ecvt(), fcvt(), 
    gcvt(), mktemp(), bcmp(), bcopy(), bzero(), index(), rindex(), utimes(), getwd(),
    brk(), sbrk(), rand()
```

##### スレッドセーフでない関数 <a id="SS_3_10_2_2_5"></a>
* 以下の関数は、スレッドセーフでない。

```
    asctime(), ctime(), getgrgid(), getgrnam(), getlogin(), getpwuid(), getpwnam(), gmtime(),
    localtime(), ttyname(), 
    ctermid(), tmpnam() (引数がNULLのとき、非リエントラントになる)
```

##### 標準外関数等 <a id="SS_3_10_2_2_6"></a>
* 可変長配列や、alloca()は、標準外である。

##### 扱いが難しい関数 <a id="SS_3_10_2_2_7"></a>
* signalの扱いは極めて難しく、安定動作をさせるのは困難である。
  「シグナルのリエントラント問題を解決でき、使用できる関数に制限がない」という利点があるため、
   signal()の代わりに、 signalfd() を使用する。 
* 排他的にファイルをオープンできないため、tmpfile()を使用しない。代わりにmkstemp()を使用する。

#### 典型的な注意点 <a id="SS_3_10_2_3"></a>
##### リソースリークを引き起こしやすい関数 <a id="SS_3_10_2_3_1"></a>
* open()/close()、fopen()/fclose()はリソースリークを引き起こしやすい。
  「[RAII(scoped guard)](#8.9)」で例示したコードやstd::fstreamを使うことでその問題を回避する。

##### シンボリックリンクの検査 <a id="SS_3_10_2_3_2"></a>
* シンボリックリンクはlstat()のみで検査せず、以下のように検査する。

    1.	ファイル名をlstat()
    2.	ファイルをopen()
    3.	2で取得したファイル記述子に対してfstat()
    4.	1, 3の情報を照合して同一ファイルであることを確認

##### strncpy(), strncat()の終端 <a id="SS_3_10_2_3_3"></a>
* 下記のような問題を回避するために文字列操作にはstd::stringを使用する。
    * sizeof(dst) <= strlen(src) の場合、strncpy(dst, src, sizeof(dst) - 1)の呼び出しは、
      dstの文字列を'\0'終端しない。
    * コピーすべきデータが無くなると、dstの残りを'\0'で埋めるので性能上の問題がある。
    * strncpy(), strncat()ともに、
      sizeof(dst) < strlen(src) のときにsrcの文字列が切り捨てられたことを判別できない。

##### TOCTOU (Time Of Check, Time Of Use) <a id="SS_3_10_2_3_4"></a>
* open()前にaccess()でファイルの存在を確認する等、チェックして使用するパターンでは、
  この動作がアトミックに行われないため問題が発生する。
  この問題回避の一般解はないが「ファイルの存在確認後、read-open」のような場合では、
  「いきなりread-openし、エラーした場合に対処」することでアトミックな処理にできる。

##### メモリアロケーション <a id="SS_3_10_2_3_5"></a>
* new/deleteとmalloc/freeの混在を避けるため下記の使用をしない。
  newしたオブジェクトのポインタをfreeした場合、そのオブジェクトのデストラクタが呼び出されず、
  リソースリークしてしまうことがある。

```
    malloc(), realloc(), free()
```

##### 非同期シグナル <a id="SS_3_10_2_3_6"></a>
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

## その他 <a id="SS_3_11"></a>
### assertion <a id="SS_3_11_1"></a>
* 論理的にありえない状態(特に論理的に到達しないはずの条件文への到達)を検出するために、
  assert()を使用する(「[switch文](programming_convention.md#SS_3_4_2)」、「[if文](programming_convention.md#SS_3_4_3)」参照)。
* assert()はコンパイルオプションにより無効化されることがあるため、
  assert()の引数に[副作用](term_explanation.md#SS_19_19_5)のある式を入れない。
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

* [演習-アサーションの選択](exercise_q.md#SS_20_7_1)  
* [演習-assert/static_assert](exercise_q.md#SS_20_7_2)  

### アセンブラ <a id="SS_3_11_2"></a>
* アセンブラ関数は、.asm等で定義し、ヘッダファイルでCの関数として宣言する。
* アセンブラ関数も、関数/メンバ関数のルールに従う(「[非メンバ関数/メンバ関数](programming_convention.md#SS_3_3)」参照)。
* インラインアセンブラや、それを含む[関数型マクロ](programming_convention.md#SS_3_6_1)がソースコード全域に広がらないようにする。

### 言語拡張機能 <a id="SS_3_11_3"></a>
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

## 特に重要なプログラミング規約 <a id="SS_3_12"></a>
本章で取り上げた規約は、重要度という観点で様々なレベルのものが混在するため量も多く、
すぐに実践することが難しいかもしれない。
そういった場合には、まずは特に重要な下記リストを守ることから始めるのが良いだろう。

* 浮動小数点型をなるべく使わない([浮動小数点型](programming_convention.md#SS_3_1_1_5))。
* const/constexprを積極的に使用する([const/constexprインスタンス](programming_convention.md#SS_3_1_9), [メンバ関数](programming_convention.md#SS_3_3_2))。
* すべてのインスタンスは定義と同時に初期化する([インスタンスの初期化](programming_convention.md#SS_3_1_12))。
* クラスのpublicメンバ関数は最大7個([メンバの数](programming_convention.md#SS_3_2_2_2))。
* クラスのメンバ変数は最大4個([メンバの数](programming_convention.md#SS_3_2_2_2))。
* クラスのメンバ変数はprivateのみ([アクセスレベルと隠蔽化](programming_convention.md#SS_3_2_3))。
* クラスのメンバ変数はコンストラクタ終了時までに初期化する([非静的なメンバ変数](programming_convention.md#SS_3_2_5))。
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
    * 範囲for文を積極的に使う([範囲for文](term_explanation.md#SS_19_7_3))。
    * gotoを使用しない([goto文](programming_convention.md#SS_3_4_8))。
* オブジェクトのダイナミックな生成にはstd::make_unique<>を使用する
  ([メモリアロケーション](programming_convention.md#SS_3_5_6))。
* Cタイプのキャストは使用しない([キャスト、暗黙の型変換](programming_convention.md#SS_3_5_10))。


