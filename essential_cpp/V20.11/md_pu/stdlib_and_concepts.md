<!-- ./md/stdlib_and_concepts.md -->
# 標準ライブラリとプログラミングの概念 <a id="SS_3"></a>
この章では、C++標準ライブラリやそれによって導入されたプログラミングの概念等の紹介を行う。

___

__この章の構成__

&emsp;&emsp; [ユーティリティ](stdlib_and_concepts.md#SS_3_1)  
&emsp;&emsp;&emsp; [std::move](stdlib_and_concepts.md#SS_3_1_1)  
&emsp;&emsp;&emsp; [std::forward](stdlib_and_concepts.md#SS_3_1_2)  

&emsp;&emsp; [type_traits](stdlib_and_concepts.md#SS_3_2)  
&emsp;&emsp;&emsp; [std::integral_constant](stdlib_and_concepts.md#SS_3_2_1)  
&emsp;&emsp;&emsp; [std::true_type](stdlib_and_concepts.md#SS_3_2_2)  
&emsp;&emsp;&emsp; [std::false_type](stdlib_and_concepts.md#SS_3_2_3)  
&emsp;&emsp;&emsp; [std::is_same](stdlib_and_concepts.md#SS_3_2_4)  
&emsp;&emsp;&emsp; [std::enable_if](stdlib_and_concepts.md#SS_3_2_5)  
&emsp;&emsp;&emsp; [std::conditional](stdlib_and_concepts.md#SS_3_2_6)  
&emsp;&emsp;&emsp; [std::is_void](stdlib_and_concepts.md#SS_3_2_7)  
&emsp;&emsp;&emsp; [std::is_copy_assignable](stdlib_and_concepts.md#SS_3_2_8)  
&emsp;&emsp;&emsp; [std::is_move_assignable](stdlib_and_concepts.md#SS_3_2_9)  

&emsp;&emsp; [並列処理](stdlib_and_concepts.md#SS_3_3)  
&emsp;&emsp;&emsp; [std::thread](stdlib_and_concepts.md#SS_3_3_1)  
&emsp;&emsp;&emsp; [std::mutex](stdlib_and_concepts.md#SS_3_3_2)  
&emsp;&emsp;&emsp; [std::atomic](stdlib_and_concepts.md#SS_3_3_3)  
&emsp;&emsp;&emsp; [std::condition_variable](stdlib_and_concepts.md#SS_3_3_4)  

&emsp;&emsp; [ロック所有ラッパー](stdlib_and_concepts.md#SS_3_4)  
&emsp;&emsp;&emsp; [std::lock_guard](stdlib_and_concepts.md#SS_3_4_1)  
&emsp;&emsp;&emsp; [std::unique_lock](stdlib_and_concepts.md#SS_3_4_2)  
&emsp;&emsp;&emsp; [std::scoped_lock](stdlib_and_concepts.md#SS_3_4_3)  

&emsp;&emsp; [スマートポインタ](stdlib_and_concepts.md#SS_3_5)  
&emsp;&emsp;&emsp; [std::unique_ptr](stdlib_and_concepts.md#SS_3_5_1)  
&emsp;&emsp;&emsp; [std::shared_ptr](stdlib_and_concepts.md#SS_3_5_2)  
&emsp;&emsp;&emsp; [std::weak_ptr](stdlib_and_concepts.md#SS_3_5_3)  
&emsp;&emsp;&emsp; [std::auto_ptr](stdlib_and_concepts.md#SS_3_5_4)  

&emsp;&emsp; [Polymorphic Memory Resource(pmr)](stdlib_and_concepts.md#SS_3_6)  
&emsp;&emsp;&emsp; [std::pmr::memory_resource](stdlib_and_concepts.md#SS_3_6_1)  
&emsp;&emsp;&emsp; [std::pmr::polymorphic_allocator](stdlib_and_concepts.md#SS_3_6_2)  
&emsp;&emsp;&emsp; [pool_resource](stdlib_and_concepts.md#SS_3_6_3)  

&emsp;&emsp; [コンテナ](stdlib_and_concepts.md#SS_3_7)  
&emsp;&emsp;&emsp; [シーケンスコンテナ(Sequence Containers)](stdlib_and_concepts.md#SS_3_7_1)  
&emsp;&emsp;&emsp;&emsp; [std::forward_list](stdlib_and_concepts.md#SS_3_7_1_1)  

&emsp;&emsp;&emsp; [連想コンテナ(Associative Containers)](stdlib_and_concepts.md#SS_3_7_2)  
&emsp;&emsp;&emsp; [無順序連想コンテナ(Unordered Associative Containers)](stdlib_and_concepts.md#SS_3_7_3)  
&emsp;&emsp;&emsp;&emsp; [std::unordered_set](stdlib_and_concepts.md#SS_3_7_3_1)  
&emsp;&emsp;&emsp;&emsp; [std::unordered_map](stdlib_and_concepts.md#SS_3_7_3_2)  
&emsp;&emsp;&emsp;&emsp; [std::type_index](stdlib_and_concepts.md#SS_3_7_3_3)  

&emsp;&emsp;&emsp; [コンテナアダプタ(Container Adapters)](stdlib_and_concepts.md#SS_3_7_4)  
&emsp;&emsp;&emsp; [特殊なコンテナ](stdlib_and_concepts.md#SS_3_7_5)  

&emsp;&emsp; [std::optional](stdlib_and_concepts.md#SS_3_8)  
&emsp;&emsp;&emsp; [戻り値の無効表現](stdlib_and_concepts.md#SS_3_8_1)  
&emsp;&emsp;&emsp; [オブジェクトの遅延初期化](stdlib_and_concepts.md#SS_3_8_2)  

&emsp;&emsp; [std::variant](stdlib_and_concepts.md#SS_3_9)  
&emsp;&emsp; [オブジェクトの比較](stdlib_and_concepts.md#SS_3_10)  
&emsp;&emsp;&emsp; [std::rel_ops](stdlib_and_concepts.md#SS_3_10_1)  
&emsp;&emsp;&emsp; [std::tuppleを使用した比較演算子の実装方法](stdlib_and_concepts.md#SS_3_10_2)  

&emsp;&emsp; [その他](stdlib_and_concepts.md#SS_3_11)  
&emsp;&emsp;&emsp; [SSO(Small String Optimization)](stdlib_and_concepts.md#SS_3_11_1)  
&emsp;&emsp;&emsp; [heap allocation elision](stdlib_and_concepts.md#SS_3_11_2)  
  
  

[インデックス](essential_intro.md#SS_1_2)に戻る。  

___


## ユーティリティ <a id="SS_3_1"></a>
### std::move <a id="SS_3_1_1"></a>
std::moveは引数を[rvalueリファレンス](core_lang_spec.md#SS_2_8_2)に変換する関数テンプレートである。

|引数                 |std::moveの動作                                    |
|---------------------|---------------------------------------------------|
|非const [lvalue](core_lang_spec.md#SS_2_7_1_1)|引数を[rvalueリファレンス](core_lang_spec.md#SS_2_8_2)にキャストする      |
|const [lvalue](core_lang_spec.md#SS_2_7_1_1)  |引数をconst [rvalueリファレンス](core_lang_spec.md#SS_2_8_2)にキャストする|

この表の動作仕様を下記ののコードで示す。

```cpp
    //  example/stdlib_and__concepts/utility_ut.cpp 10

    uint32_t f(std::string&) { return 0; }         // f-0
    uint32_t f(std::string&&) { return 1; }        // f-1
    uint32_t f(std::string const&) { return 2; }   // f-2
    uint32_t f(std::string const&&) { return 3; }  // f-3
```
```cpp
    //  example/stdlib_and__concepts/utility_ut.cpp 21

    std::string       str{};
    std::string const cstr{};

    ASSERT_EQ(0, f(str));               // strはlvalue → f(std::string&)
    ASSERT_EQ(1, f(std::string{}));     // 一時オブジェクトはrvalue → f(std::string&&)
    ASSERT_EQ(1, f(std::move(str)));    // std::moveでrvalueに変換 → f(std::string&&)
    ASSERT_EQ(2, f(cstr));              // cstrはconst lvalue → f(std::string const&)
    ASSERT_EQ(3, f(std::move(cstr)));   // std::moveでconst rvalueに変換 → f(std::string const&&)
```

std::moveは以下の２つの概念ときわめて密接に関連しており、

* [rvalueリファレンス](core_lang_spec.md#SS_2_8_2)
* [moveセマンティクス](cpp_idioms.md#SS_4_3_3)

これら3つが組み合わさることで、不要なコピーを避けた高効率なリソース管理が実現される。

### std::forward <a id="SS_3_1_2"></a>
std::forwardは、下記の２つの概念を実現するための関数テンプレートである。

* [forwardingリファレンス](core_lang_spec.md#SS_2_8_3)
* [perfect forwarding](core_lang_spec.md#SS_2_8_5)

std::forwardを適切に使用することで、引数の値カテゴリを保持したまま転送でき、
move可能なオブジェクトの不要なコピーを避けることができる。

## type_traits <a id="SS_3_2"></a>
type_traitsは、型に関する情報をコンパイル時に取得・変換するためのメタ関数群で、
型特性の判定や型操作を静的に行うために用いられる。

以下に代表的なものをいくつか説明する。

- [std::integral_constant](stdlib_and_concepts.md#SS_3_2_1)
- [std::true_type](stdlib_and_concepts.md#SS_3_2_2)/[std::false_type](stdlib_and_concepts.md#SS_3_2_3)
- [std::is_same](stdlib_and_concepts.md#SS_3_2_4)
- [std::enable_if](stdlib_and_concepts.md#SS_3_2_5)
- [std::conditional](stdlib_and_concepts.md#SS_3_2_6)
- [std::is_void](stdlib_and_concepts.md#SS_3_2_7)
- [std::is_copy_assignable](stdlib_and_concepts.md#SS_3_2_8)
- [std::is_move_assignable](stdlib_and_concepts.md#SS_3_2_9)

### std::integral_constant <a id="SS_3_2_1"></a>
std::integral_constantは「テンプレートパラメータとして与えられた型とその定数から新たな型を定義する」
クラステンプレートである。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 13

    using int3 = std::integral_constant<int, 3>;

    // std::is_same_vの2パラメータが同一であれば、std::is_same_v<> == true
    static_assert(std::is_same_v<int, int3::value_type>);
    static_assert(std::is_same_v<std::integral_constant<int, 3>, int3::type>);
    static_assert(int3::value == 3);

    using bool_true = std::integral_constant<bool, true>;

    static_assert(std::is_same_v<bool, bool_true::value_type>);
    static_assert(std::is_same_v<std::integral_constant<bool, true>, bool_true::type>);
    static_assert(bool_true::value == true);
```

また、すでに示したようにstd::true_type/std::false_typeを実装するためのクラステンプレートでもある。


### std::true_type <a id="SS_3_2_2"></a>
`std::true_type`(と`std::false_type`)は真/偽を返す標準ライブラリの[メタ関数](core_lang_spec.md#SS_2_11_2)群の戻り型となる型エイリアスであるため、
最も使われるテンプレートの一つである。

これらは、下記で確かめられる通り、後述する[std::integral_constant](stdlib_and_concepts.md#SS_3_2_1)を使い定義されている。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 32

    // std::is_same_vの2パラメータが同一であれば、std::is_same_v<> == true
    static_assert(std::is_same_v<std::integral_constant<bool, true>, std::true_type>);
    static_assert(std::is_same_v<std::integral_constant<bool, false>, std::false_type>);
```

それぞれの型が持つvalue定数は、下記のように定義されている。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 39

    static_assert(std::true_type::value, "must be true");
    static_assert(!std::false_type::value, "must be false");
```

これらが何の役に立つのか直ちに理解することは難しいが、
true/falseのメタ関数版と考えれば、追々理解できるだろう。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 48

    // 引数の型がintに変換できるかどうかを判定する関数
    // decltypeの中でのみ使用されるため、定義は不要
    constexpr std::true_type  IsCovertibleToInt(int);  // intに変換できる型はこちら
    constexpr std::false_type IsCovertibleToInt(...);  // それ以外はこちら
```

上記の単体テストは下記のようになる。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 59

    static_assert(decltype(IsCovertibleToInt(1))::value);
    static_assert(decltype(IsCovertibleToInt(1u))::value);
    static_assert(!decltype(IsCovertibleToInt(""))::value);  // ポインタはintに変換不可

    struct ConvertibleToInt {
        operator int();
    };

    struct NotConvertibleToInt {};

    static_assert(decltype(IsCovertibleToInt(ConvertibleToInt{}))::value);
    static_assert(!decltype(IsCovertibleToInt(NotConvertibleToInt{}))::value);

    // なお、IsCovertibleToInt()やConvertibleToInt::operator int()は実際に呼び出されるわけでは
    // ないため、定義は必要なく宣言のみがあれば良い。
```

IsCovertibleToIntの呼び出しをdecltypeのオペランドにすることで、
std::true_typeかstd::false_typeを受け取ることができる。

### std::false_type <a id="SS_3_2_3"></a>
[std::true_type](stdlib_and_concepts.md#SS_3_2_2)を参照せよ。

### std::is_same <a id="SS_3_2_4"></a>

すでに上記の例でも使用したが、std::is_sameは2つのテンプレートパラメータが

* 同じ型である場合、std::true_type
* 違う型である場合、std::false_type

から派生した型となる。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 99

    static_assert(std::is_same<int, int>::value);
    static_assert(std::is_same<int, int32_t>::value);   // 64ビットg++/clang++
    static_assert(!std::is_same<int, int64_t>::value);  // 64ビットg++/clang++
    static_assert(std::is_same<std::string, std::basic_string<char>>::value);
    static_assert(std::is_same<typename std::vector<int>::reference, int&>::value);
```

また、 C++17で導入されたstd::is_same_vは、定数テンプレートを使用し、
下記のように定義されている。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 90

    template <typename T, typename U>
    constexpr bool is_same_v{std::is_same<T, U>::value};
```

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 108

    static_assert(is_same_v<int, int>);
    static_assert(is_same_v<int, int32_t>);   // 64ビットg++/clang++
    static_assert(!is_same_v<int, int64_t>);  // 64ビットg++/clang++
    static_assert(is_same_v<std::string, std::basic_string<char>>);
    static_assert(is_same_v<typename std::vector<int>::reference, int&>);
```

このような簡潔な記述の一般形式は、

```
   T::value  -> T_v
   T::type   -> T_t
```

のように定義されている(このドキュメントのほとんど場所では、簡潔な形式を用いる)。

第1テンプレートパラメータが第2テンプレートパラメータの基底クラスかどうかを判断する
std::is_base_ofを使うことで下記のようにstd::is_sameの基底クラス確認することもできる。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 117

    static_assert(std::is_base_of_v<std::true_type, std::is_same<int, int>>);
    static_assert(std::is_base_of_v<std::false_type, std::is_same<int, char>>);
```

### std::enable_if <a id="SS_3_2_5"></a>
std::enable_ifは、bool値である第1テンプレートパラメータが

* trueである場合、型である第2テンプレートパラメータをメンバ型typeとして宣言する。
* falseである場合、メンバ型typeを持たない。

下記のコードはクラステンプレートの特殊化を用いたstd::enable_ifの実装例である。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 124

    template <bool T_F, typename T = void>
    struct enable_if;

    template <typename T>
    struct enable_if<true, T> {
        using type = T;
    };

    template <typename T>
    struct enable_if<false, T> {  // メンバエイリアスtypeを持たない
    };

    template <bool COND, typename T = void>
    using enable_if_t = typename enable_if<COND, T>::type;
```

std::enable_ifの使用例を下記に示す。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 148

    static_assert(std::is_same_v<void, std::enable_if_t<true>>);
    static_assert(std::is_same_v<int, std::enable_if_t<true, int>>);
```

実装例から明らかなように

* std::enable_if\<true>::typeは[well-formed](core_lang_spec.md#SS_2_14_2)
* std::enable_if\<false>::typeは[ill-formed](core_lang_spec.md#SS_2_14_1)

となるため、下記のコードはコンパイルできない。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 155

    // 下記はill-formedとなるため、コンパイルできない。
    static_assert(std::is_same_v<void, std::enable_if_t<false>>);
    static_assert(std::is_same_v<int, std::enable_if_t<false, int>>);
```

std::enable_ifのこの特性と後述する[SFINAE](core_lang_spec.md#SS_2_11_1)により、
様々な静的ディスパッチを行うことができる。


### std::conditional <a id="SS_3_2_6"></a>

std::conditionalは、bool値である第1テンプレートパラメータが

* trueである場合、第2テンプレートパラメータ
* falseである場合、第3テンプレートパラメータ

をメンバ型typeとして宣言する。

下記のコードはクラステンプレートの特殊化を用いたstd::conditionalの実装例である。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 164

    template <bool T_F, typename, typename>
    struct conditional;

    template <typename T, typename U>
    struct conditional<true, T, U> {
        using type = T;
    };

    template <typename T, typename U>
    struct conditional<false, T, U> {
        using type = U;
    };

    template <bool COND, typename T, typename U>
    using conditional_t = typename conditional<COND, T, U>::type;
```

std::conditionalの使用例を下記に示す。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 189

    static_assert(std::is_same_v<int, std::conditional_t<true, int, char>>);
    static_assert(std::is_same_v<char, std::conditional_t<false, int, char>>);
```

### std::is_void <a id="SS_3_2_7"></a>
std::is_voidはテンプレートパラメータの型が

* voidである場合、std::true_type
* voidでない場合、std::false_type

から派生した型となる。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and__concepts/type_traits_ut.cpp 82

    static_assert(std::is_void<void>::value);
    static_assert(!std::is_void<int>::value);
    static_assert(!std::is_void<std::string>::value);
```

### std::is_copy_assignable <a id="SS_3_2_8"></a>
std::is_copy_assignableはテンプレートパラメータの型(T)がcopy代入可能かを調べる。
Tが[CopyAssignable要件](cpp_idioms.md#SS_4_3_5)を満たすためには`std::is_copy_assignable<T>`がtrueでなければならないが、
その逆が成立するとは限らない。


### std::is_move_assignable <a id="SS_3_2_9"></a>
std::is_move_assignableはテンプレートパラメータの型(T)がmove代入可能かを調べる。
Tが[MoveAssignable要件](cpp_idioms.md#SS_4_3_4)を満たすためには`std::is_move_assignable<T>`がtrueでなければならないが、
その逆が成立するとは限らない。


## 並列処理 <a id="SS_3_3"></a>

### std::thread <a id="SS_3_3_1"></a>
クラスthread は、新しい実行のスレッドの作成/待機/その他を行う機構を提供する。

```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 9

    struct Conflict {
        void     increment() { ++count_; }  // 非アトミック（データレースの原因）
        uint32_t count_ = 0;
    };
```
```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 19

    Conflict c;

    constexpr uint32_t inc_per_thread = 5'000'000;
    constexpr uint32_t expected       = 2 * inc_per_thread;

    auto worker = [&c] {  // スレッドのボディとなるラムダの定義
        for (uint32_t i = 0; i < inc_per_thread; ++i) {
            c.increment();
        }
    };

    std::thread t1{worker};  // ラムダworker関数を使用したスレッドの起動
    std::thread t2{worker};

    t1.join();  // スレッドの終了待ち
    t2.join();  // スレッドの終了待ち
                // 注意: join()もdetach()も呼ばずにスレッドオブジェクトが
                // デストラクトされると、std::terminateが呼ばれる

    // ASSERT_EQ(c.count_, expected);  t1とt2が++count_が競合するためこのテストは成立しないため、
    //                                 一例では次のようになる  c.count_: 6825610 expected: 10000000
    ASSERT_NE(c.count_, expected);
```

### std::mutex <a id="SS_3_3_2"></a>
mutex は、スレッド間で使用する共有リソースを排他制御するためのクラスである。 

| メンバ関数 | 動作説明                                                                                    |
|:-----------|---------------------------------------------------------------------------------------------|
| lock()     | lock()が即時リターンするスレッドはただ一つ。そうでない場合、unlock()が呼ばれるまでブロック  |
| unlock()   | lock()でブロックされていたスレッドの中から一つが動き出す                                    |


以下のコード例では、メンバ変数のインクリメントがスレッド間の競合を引き起こす(こういったコード領域を
[クリティカルセクション](cpp_idioms.md#SS_4_9_4)と呼ぶ)が、std::mutexによりこの問題を回避している。

```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 48

    struct Conflict {
        void increment()
        {
            mtx_.lock();  // クリティカルセクションの保護開始

            ++count_;

            mtx_.unlock();  // クリティカルセクションの保護終了
        }
        uint32_t   count_ = 0;
        std::mutex mtx_{};
    };
```
```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 66

    Conflict c;

    constexpr uint32_t inc_per_thread = 5'000'000;
    constexpr uint32_t expected       = 2 * inc_per_thread;

    auto worker = [&c] {  // スレッドのボディとなるラムダの定義
        for (uint32_t i = 0; i < inc_per_thread; ++i) {
            c.increment();
        }
    };

    std::thread t1{worker};  // ラムダworker関数を使用したスレッドの起動
    std::thread t2{worker};

    t1.join();  // スレッドの終了待ち
    t2.join();  // スレッドの終了待ち
                // 注意: join()もdetach()も呼ばずにスレッドオブジェクトが
                // デストラクトされると、std::terminateが呼ばれる

    ASSERT_EQ(c.count_, expected);
```

lock()を呼び出した状態で、unlock()を呼び出さなかった場合、デッドロックを引き起こしてしまうため、
永久に処理が完了しないバグの元となり得る。このような問題を避けるために、
mutexは通常、[std::lock_guard](stdlib_and_concepts.md#SS_3_4_1)と組み合わせて使われる。

### std::atomic <a id="SS_3_3_3"></a>
atomicクラステンプレートは、型Tをアトミック操作するためのものである。
[組み込み型](core_lang_spec.md#SS_2_1_2)に対する特殊化が提供されており、それぞれに特化した演算が用意されている。
[std::mutex](stdlib_and_concepts.md#SS_3_3_2)で示したような単純なコードではstd::atomicを使用して下記のように書く方が一般的である。

```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 92

    struct Conflict {
        void increment()
        {
            ++count_;  // ++count_は「count_の値の呼び出し -> その値のインクリメント、その値のcount_への書き戻し」である
                       // この一連の操作は排他的(アトミック)に行われる

        }  // lockオブジェクトのデストラクタでmtx_.unlock()が呼ばれる
        std::atomic<uint32_t> count_ = 0;
    };
```
```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 107

    Conflict c;

    constexpr uint32_t inc_per_thread = 5'000'000;
    constexpr uint32_t expected       = 2 * inc_per_thread;

    auto worker = [&c] {  // スレッドのボディとなるラムダの定義
        for (uint32_t i = 0; i < inc_per_thread; ++i) {
            c.increment();
        }
    };

    std::thread t1{worker};  // ラムダworker関数を使用したスレッドの起動
    std::thread t2{worker};

    t1.join();  // スレッドの終了待ち
    t2.join();  // スレッドの終了待ち
                // 注意: join()もdetach()も呼ばずにスレッドオブジェクトが
                // デストラクトされると、std::terminateが呼ばれる

    ASSERT_EQ(c.count_, expected);
```

### std::condition_variable <a id="SS_3_3_4"></a>
condition_variable は、特定のイベントが発生するまでスレッドの待ち合わせを行うためのクラスである。
最も単純な使用例を以下に示す(「[Spurious Wakeup](cpp_idioms.md#SS_4_9_10)」参照)。
```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 135

    std::mutex              mutex;
    std::condition_variable cond_var;
    bool                    event_occured = false;

    void notify()  // 通知を行うスレッドが呼び出す関数
    {
        auto lock = std::lock_guard{mutex};

        event_occured = true;

        cond_var.notify_all();  // wait()で待ち状態のすべてのスレッドを起こす
    }

    void wait()
    {
        auto lock = std::unique_lock{mutex};

        // notifyされるのを待つ。
        cond_var.wait(lock, []() noexcept { return event_occured; });  // Spurious Wakeup対策
    }
```
```cpp
    //  example/stdlib_and__concepts/thread_ut.cpp 162

    std::thread t1{[]() { wait(); /* 通知待ち */ }};
    std::thread t2{[]() { wait(); /* 通知待ち */ }};

    notify();  // 通知待ちのスレッドに通知

    t1.join();
    t2.join();
```

## ロック所有ラッパー <a id="SS_3_4"></a>
ロック所有ラッパーとはミューテックスのロックおよびアンロックを管理するための以下のクラスを指す。

- [std::lock_guard](stdlib_and_concepts.md#SS_3_4_1)
- [std::unique_lock](stdlib_and_concepts.md#SS_3_4_2)
- [std::scoped_lock](stdlib_and_concepts.md#SS_3_4_3)


### std::lock_guard <a id="SS_3_4_1"></a>
std::lock_guardを使わない問題のあるコードを以下に示す。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 14

    struct Conflict {
        void increment()
        {
            mtx_.lock();  // ++count_の排他のためのロック

            ++count_;

            mtx_.unlock();  // 上記のアンロック
        }

        uint32_t   count_ = 0;
        std::mutex mtx_{};
    };
```

上記で示したConflict::increment()には以下のようなリスクが存在する。

1. 関数が複雑化してエクセプションを投げる可能性がある場合、
    - エクセプションをこの関数内で捕捉し、ロック解除 (mtx_.unlock()) を行った上で再スローしなければならない。
    - ロック解除を忘れるとデッドロックにつながる。

2. 複数の return 文を持つように関数が拡張された場合、
    - すべての return の前で mtx_.unlock() を呼び出さなければならない。

これらを正しく管理するためには、重複コードが増え、関数の保守性が著しく低下する。

std::lock_guardを使用して、このような問題に対処したコードを以下に示す。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 63

    struct Conflict {
        void increment()
        {
            std::lock_guard<std::mutex> lock{mtx_};  // lockオブジェクトのコンストラクタでmtx_.lock()が呼ばれる
                                                     // ++count_の排他
            ++count_;

        }  // lockオブジェクトのデストラクタでmtx_.unlock()が呼ばれる
        uint32_t   count_ = 0;
        std::mutex mtx_{};
    };
```

オリジナルの単純な以下のincrement()と改善版を比較すると、大差ないように見えるが、

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 19
    {
        mtx_.lock();  // ++count_の排他のためのロック

        ++count_;

        mtx_.unlock();  // 上記のアンロック
    }
```

オリジナルのコードで指摘したすべてのリスクが、わずか一行の変更で解決されている。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 68
    {
        std::lock_guard<std::mutex> lock{mtx_};  // lockオブジェクトのコンストラクタでmtx_.lock()が呼ばれる
                                                 // ++count_の排他
        ++count_;

    }  // lockオブジェクトのデストラクタでmtx_.unlock()が呼ばれる
```

### std::unique_lock <a id="SS_3_4_2"></a>
std::unique_lockとは、ミューテックスのロック管理を柔軟に行えるロックオブジェクトである。
std::lock_guardと異なり、ロックの手動解放や再取得が可能であり、特にcondition_variable::wait()と組み合わせて使用される。
wait()は内部でロックを一時的に解放し、通知受信後に再取得する。

下記の例では、IntQueue::push()、 IntQueue::pop_ng()、
IntQueue::pop_ok()の中で行われるIntQueue::q_へのアクセスで発生する競合を回避するためにIntQueue::mtx_を使用する。

下記のコード例では、[std::lock_guard](stdlib_and_concepts.md#SS_3_4_1)の説明で述べたようにmutex::lock()、mutex::unlock()を直接呼び出すのではなく、
std::unique_lockやstd::lock_guardによりmutexを使用する。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 112

    class IntQueue {
    public:
        void push(int v)
        {
            {
                std::lock_guard<std::mutex> lg{mtx_};  // ロック取得
                q_.push(v);
            }  // ロック解放

            cv_.notify_one();  // 待機中のスレッドを1つ起床
                               // 注: ロック解放後に呼び出すことで、起床したスレッドがすぐにロックを取得できる
        }

        int pop_ng()
        {
            std::unique_lock<std::mutex> lock{mtx_};
            cv_.wait(lock);  // NG: Spurious Wakeup対策なし
                             // 起床時に条件を再確認しないため、
                             // q_.empty() が true のまま起床する可能性がある
            int v = q_.front();
            q_.pop();  // 条件未確認アクセス（危険）

            return v;
        }

        int pop_ok()
        {
            std::unique_lock<std::mutex> lock{mtx_};
            cv_.wait(lock, [&q_ = q_] { return !q_.empty(); });  // waitの述語が true になるまで待機(Spurious Wakeup対策)
            // wait()の動作:
            // 1. 述語を評価してtrueならすぐreturn
            // 2. falseなら: unlock() → 通知待機 → 通知受信 → lock() → 述語再評価
            // 3. 述語がtrueになるまで2を繰り返す

            int v = q_.front();
            q_.pop();  // ここでは、q_.empty()は必ずfalse
            return v;
        }
    private:
        std::mutex              mtx_{};
        std::condition_variable cv_{};
        std::queue<int>         q_{};
    };
```
```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 168

    IntQueue           iq;
    constexpr int      end_data       = -1;
    constexpr uint32_t push_count_max = 10;

    // Producer
    std::thread t1([&iq] {
        for (uint32_t i = 0; i < push_count_max; ++i) {
            iq.push(100 + i);
        }

        iq.push(end_data);  // t2が-1を受信したらt2のループ終了
    });

    uint32_t pop_count = 0;

    std::thread t2([&iq, &pop_count] {
        for (;;) {
            if (int v = iq.pop_ok(); v == -1) {
                break;
            }
            else {
                ++pop_count;
            }
        }
    });

    t1.join();  // スレッドの終了待ち
    t2.join();  // スレッドの終了待ち

    ASSERT_EQ(push_count_max, pop_count);
```

一般に条件変数には、[Spurious Wakeup](cpp_idioms.md#SS_4_9_10)という問題があり、std::condition_variableも同様である。

上記の抜粋である下記のコード例では[Spurious Wakeup](cpp_idioms.md#SS_4_9_10)の対策が行われていないため、
意図通り動作しない可能性がある。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 127

    int pop_ng()
    {
        std::unique_lock<std::mutex> lock{mtx_};
        cv_.wait(lock);  // NG: Spurious Wakeup対策なし
                         // 起床時に条件を再確認しないため、
                         // q_.empty() が true のまま起床する可能性がある
        int v = q_.front();
        q_.pop();  // 条件未確認アクセス（危険）

        return v;
    }
```

下記のIntQueue::pop_ok()は、pop_ng()にSpurious Wakeupの対策を施したものである。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 141

    int pop_ok()
    {
        std::unique_lock<std::mutex> lock{mtx_};
        cv_.wait(lock, [&q_ = q_] { return !q_.empty(); });  // waitの述語が true になるまで待機(Spurious Wakeup対策)
        // wait()の動作:
        // 1. 述語を評価してtrueならすぐreturn
        // 2. falseなら: unlock() → 通知待機 → 通知受信 → lock() → 述語再評価
        // 3. 述語がtrueになるまで2を繰り返す

        int v = q_.front();
        q_.pop();  // ここでは、q_.empty()は必ずfalse
        return v;
    }
```

### std::scoped_lock <a id="SS_3_4_3"></a>
std::scoped_lockとは、複数のミューテックスを同時にロックするためのロックオブジェクトである。
C++17で導入され、デッドロックを回避しながら複数のミューテックスを安全にロックできる。

複数のミューテックスを扱う際、異なるスレッドが異なる順序でロックを取得しようとすると、
デッドロックが発生する可能性がある。下記の例では、2つの銀行口座間で送金を行う際に、
両方の口座を同時にロックする必要がある。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 205

    class BankAccount {
    public:
        explicit BankAccount(int balance) : balance_{balance} {}

        void transfer_ng(BankAccount& to, int amount)
        {
            std::lock_guard<std::mutex> lock1{mtx_};     // 自分のアカウントをロック
            std::lock_guard<std::mutex> lock2{to.mtx_};  // 相手のアカウントをロック
            // NG: 異なるスレッドが異なる順序でロックを取得するとデッドロックの可能性

            if (balance_ >= amount) {
                balance_ -= amount;
                to.balance_ += amount;
            }
        }

        void transfer_ok(BankAccount& to, int amount)
        {
            std::scoped_lock lock{mtx_, to.mtx_};  // 複数のmutexを安全にロック
            // デッドロック回避アルゴリズムにより、常に同じ順序でロックを取得

            if (balance_ >= amount) {
                balance_ -= amount;
                to.balance_ += amount;
            }
        }

        int balance() const
        {
            std::lock_guard<std::mutex> lock{mtx_};
            return balance_;
        }

    private:
        mutable std::mutex mtx_{};
        int                balance_;
    };
```
下記の例では、2つのスレッドがそれぞれ逆方向の送金を同時に行う。
transfer_ok()の代わりにtransfer_ng()を使用した場合、デッドロックが発生する可能性がある。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 254

    BankAccount acc1{1000};
    BankAccount acc2{1000};

    constexpr int transfer_amount = 100;
    constexpr int transfer_count  = 10;

    // スレッド1: acc1 → acc2 へ送金
    std::thread t1([&acc1, &acc2] {
        for (int i = 0; i < transfer_count; ++i) {
            acc1.transfer_ok(acc2, transfer_amount);
        }
    });

    // スレッド2: acc2 → acc1 へ送金
    std::thread t2([&acc2, &acc1] {
        for (int i = 0; i < transfer_count; ++i) {
            acc2.transfer_ok(acc1, transfer_amount);
        }
    });

    t1.join();
    t2.join();

    // 総額は変わらない
    ASSERT_EQ(acc1.balance() + acc2.balance(), 2000);
```

transfer_ng()がデッドロックを引き起こすシナリオは、以下のようなものである。

1. スレッド1が acc1.transfer_ng(acc2, 100) を呼び出し、acc1.mtx_ をロック
2. スレッド2が acc2.transfer_ng(acc1, 100) を呼び出し、acc2.mtx_ をロック
3. スレッド1が acc2.mtx_ のロックを試みるが、スレッド2が保持しているため待機
4. スレッド2が acc1.mtx_ のロックを試みるが、スレッド1が保持しているため待機
5. 互いに相手のロック解放を待ち続け、永遠に進まない（デッドロック）

```plant_uml/mutex_deadlock.pu
@startuml
!theme plain
title デッドロック発生のシナリオ

participant "Thread 1" as T1
participant "acc1.mtx_" as M1
participant "acc2.mtx_" as M2
participant "Thread 2" as T2

== 初期状態 ==
note over T1, T2
  両スレッドが同時に送金処理を開始
end note

== ロック取得フェーズ ==
T1 -> M1: lock() ✓
activate M1
note right of T1
  acc1.transfer_ng(acc2, 100)
  acc1.mtx_ のロック成功
end note

T2 -> M2: lock() ✓
activate M2
note left of T2
  acc2.transfer_ng(acc1, 100)
  acc2.mtx_ のロック成功
end note

== デッドロック発生 ==
T1 -x M2: lock() ✗
note right of T1
  acc2.mtx_ のロック待機中...
  (Thread 2が保持中)
end note

T2 -x M1: lock() ✗
note left of T2
  acc1.mtx_ のロック待機中...
  (Thread 1が保持中)
end note

note over T1, T2 #FF6B6B
  **デッドロック発生**
  互いに相手のロック解放を待ち続ける
  
  Thread 1: acc1.mtx_ を保持、acc2.mtx_ を待機
  Thread 2: acc2.mtx_ を保持、acc1.mtx_ を待機
  
  → プログラムが停止（永遠に進まない）
end note

@enduml
```


下記のBankAccount::transfer_ok()は、std::scoped_lockを使用して前述したデッドロックを回避したものである。

```cpp
    //  example/stdlib_and__concepts/lock_ownership_wrapper_ut.cpp 225

    void transfer_ok(BankAccount& to, int amount)
    {
        std::scoped_lock lock{mtx_, to.mtx_};  // 複数のmutexを安全にロック
        // デッドロック回避アルゴリズムにより、常に同じ順序でロックを取得

        if (balance_ >= amount) {
            balance_ -= amount;
            to.balance_ += amount;
        }
    }
```

## スマートポインタ <a id="SS_3_5"></a>
スマートポインタは、C++標準ライブラリが提供するメモリ管理クラス群を指す。
生のポインタの代わりに使用され、リソース管理を容易にし、
メモリリークや二重解放といった問題を防ぐことを目的としている。

スマートポインタは通常、所有権とスコープに基づいてメモリの解放を自動的に行う。
C++標準ライブラリでは、主に以下の3種類のスマートポインタが提供されている。

* [std::unique_ptr](stdlib_and_concepts.md#SS_3_5_1)
* [std::shared_ptr](stdlib_and_concepts.md#SS_3_5_2)
* [std::weak_ptr](stdlib_and_concepts.md#SS_3_5_3)
* [std::auto_ptr](stdlib_and_concepts.md#SS_3_5_4)

### std::unique_ptr <a id="SS_3_5_1"></a>
std::unique_ptrは、C++11で導入されたスマートポインタの一種であり、std::shared_ptrとは異なり、
[オブジェクトの排他所有](cpp_idioms.md#SS_4_2_1)を表すために用いられる。所有権は一つのunique_ptrインスタンスに限定され、
他のポインタと共有することはできない。ムーブ操作によってのみ所有権を移譲でき、
スコープを抜けると自動的にリソースが解放されるため、メモリ管理の安全性と効率性が向上する。

### std::shared_ptr <a id="SS_3_5_2"></a>
std::shared_ptrは、同じくC++11で導入されたスマートポインタであり、[オブジェクトの共有所有](cpp_idioms.md#SS_4_2_2)を表すために用いられる。
複数のshared_ptrインスタンスが同じリソースを参照でき、
内部の参照カウントによって最後の所有者が破棄された時点でリソースが解放される。
[std::weak_ptr](stdlib_and_concepts.md#SS_3_5_3)は、shared_ptrと連携して使用されるスマートポインタであり、オブジェクトの非所有参照を表す。
参照カウントには影響せず、循環参照を防ぐために用いられる。weak_ptrから一時的にshared_ptrを取得するにはlock()を使用する。

### std::weak_ptr <a id="SS_3_5_3"></a>
std::weak_ptrは、スマートポインタの一種である。

std::weak_ptrは参照カウントに影響を与えず、[std::shared_ptr](stdlib_and_concepts.md#SS_3_5_2)とオブジェクトを共有所有するのではなく、
その`shared_ptr`インスタンスとの関連のみを保持するのため、[オブジェクトの循環所有](cpp_idioms.md#SS_4_2_3)の問題を解決できる。

[オブジェクトの循環所有](cpp_idioms.md#SS_4_2_3)で示した問題のあるクラスの修正版を以下に示す
(以下の例では、Xは前のままで、Yのみ修正した)。

```cpp
    //  example/stdlib_and__concepts/weak_ptr_ut.cpp 9

    class Y;
    class X final {
    public:
        explicit X() noexcept { ++constructed_counter; }
        ~X() { --constructed_counter; }

        void Register(std::shared_ptr<Y> y) { y_ = y; }

        std::shared_ptr<Y> const& ref_y() const noexcept { return y_; }

        // 自身の状態を返す ("X alone" または "X with Y")
        std::string WhoYouAre() const;

        // y_が保持するオブジェクトの状態を返す ("None" またはY::WhoYouAre()に委譲)
        std::string WhoIsWith() const;

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<Y> y_{};  // 初期化状態では、y_はオブジェクトを所有しない(use_count()==0)
    };

    class Y final {
    public:
        explicit Y() noexcept { ++constructed_counter; }
        ~Y() { --constructed_counter; }

        void Register(std::shared_ptr<X> x) { x_ = x; }

        std::weak_ptr<X> const& ref_x() const noexcept { return x_; }

        // 自身の状態を返す ("Y alone" または "Y with X")
        std::string WhoYouAre() const;

        // x_が保持するオブジェクトの状態を返す ("None" またはY::WhoYouAre()に委譲)
        std::string WhoIsWith() const;

        static uint32_t constructed_counter;

    private:
        std::weak_ptr<X> x_{};
    };

    // Xのメンバ定義
    std::string X::WhoYouAre() const { return y_ ? "X with Y" : "X alone"; }
    std::string X::WhoIsWith() const { return y_ ? y_->WhoYouAre() : std::string{"None"}; }
    uint32_t    X::constructed_counter;

    // Yのメンバ定義
    std::string Y::WhoYouAre() const { return x_.use_count() != 0 ? "Y with X" : "Y alone"; }
    // 注: weak_ptrはbool変換をサポートしないため、use_count() != 0 で有効性を判定
    std::string Y::WhoIsWith() const  // 修正版Y::WhoIsWithの定義
    {
        if (auto x = x_.lock(); x) {  // Xオブジェクトが解放されていた場合、xはstd::shared_ptr<X>{}となり、falseと評価される
            return x->WhoYouAre();
        }
        else {
            return "None";
        }
    }
    uint32_t Y::constructed_counter;
```

このコードからわかるように修正版YはXオブジェクトを参照するために、
`std::shared_ptr<X>`の代わりに`std::weak_ptr<X>`を使用する。
Xオブジェクトにアクセスする必要があるときに、
下記のY::WhoIsWith()関数の内部処理のようにすることで、`std::weak_ptr<X>`オブジェクトから、
それと紐づいた`std::shared_ptr<X>`オブジェクトを生成できる。

なお、上記コードは[初期化付きif文](core_lang_spec.md#SS_2_9_5_3)を使うことで、
生成した`std::shared_ptr<X>`オブジェクトのスコープを最小に留めている。

```cpp
    //  example/stdlib_and__concepts/weak_ptr_ut.cpp 63
    std::string Y::WhoIsWith() const  // 修正版Y::WhoIsWithの定義
    {
        if (auto x = x_.lock(); x) {  // Xオブジェクトが解放されていた場合、xはstd::shared_ptr<X>{}となり、falseと評価される
            return x->WhoYouAre();
        }
        else {
            return "None";
        }
    }
```

Xと修正版Yの単体テストによりメモリーリークが修正されたことを以下に示す。

```cpp
    //  example/stdlib_and__concepts/weak_ptr_ut.cpp 82

    {
        ASSERT_EQ(X::constructed_counter, 0);
        ASSERT_EQ(Y::constructed_counter, 0);

        auto x0 = std::make_shared<X>();       // Xオブジェクトを持つshared_ptrの生成
        ASSERT_EQ(X::constructed_counter, 1);  // Xオブジェクトは1つ生成された

        ASSERT_EQ(x0.use_count(), 1);
        ASSERT_EQ(x0->WhoYouAre(), "X alone");  // x0.y_は何も保持していないので、"X alone"
        ASSERT_EQ(x0->ref_y().use_count(), 0);  // X::y_は何も持っていない

        {
            auto y0 = std::make_shared<Y>();

            ASSERT_EQ(Y::constructed_counter, 1);       // Yオブジェクトは1つ生成された
            ASSERT_EQ(y0.use_count(), 1);
            ASSERT_EQ(y0->ref_x().use_count(), 0);      // y0.x_は何も持っていない
            ASSERT_EQ(y0->WhoYouAre(), "Y alone");      // y0.x_は何も持っていないので、"Y alone"

            x0->Register(y0);                           // これによりx0.y_はy0と同じオブジェクトを持つ
            ASSERT_EQ(x0->WhoYouAre(), "X with Y");     // x0.y_はYオブジェクトを持っている

            y0->Register(x0);  // これによりy0.x_はx0と同じXオブジェクトを持つことができる
            ASSERT_EQ(y0->WhoIsWith(), "X with Y");     // y0.x_が持っているXオブジェクトはYを持っている
            
            // x0->Register(y0), y0->Register(x0)により Xオブジェクト、Yオブジェクトは相互参照できる状態となった
            ASSERT_EQ(X::constructed_counter, 1);       // 新しいオブジェクトが生成されるわけではない
            ASSERT_EQ(Y::constructed_counter, 1);       // 新しいオブジェクトが生成されるわけではない

            ASSERT_EQ(y0->WhoYouAre(), "Y with X");     // y0.x_はXオブジェクトを持っている
            ASSERT_EQ(x0->WhoYouAre(), "X with Y");     // x0.y_はYオブジェクトを持っている(再確認)
            ASSERT_EQ(y0->WhoIsWith(), "X with Y");     // y0が参照するXオブジェクトはYを持っている
            // 現時点で、x0とy0がお互いを相互参照できることが確認できた

            // weak_ptrを使用した効果によりXオブジェクトの参照カウントは増加しない
            ASSERT_EQ(x0.use_count(), 1);               // y0.x_はweak_ptrなので参照カウントに影響しない
            ASSERT_EQ(y0.use_count(), 2);               // x0.y_はshared_ptrなので参照カウントが2
            ASSERT_EQ(y0->ref_x().use_count(), 1);      // y0.x_の参照カウントは1
            ASSERT_EQ(x0->ref_y().use_count(), 2);      // x0.y_の参照カウントは2
        }  //ここでy0がスコープアウトするため、y0にはアクセスできないが、
           // x0を介して、y0が持っていたYオブジェクトにはアクセスできる

        ASSERT_EQ(x0->ref_y().use_count(), 1);  // y0がスコープアウトしたため、Yオブジェクトの参照カウントが減った
        ASSERT_EQ(x0->ref_y()->WhoYouAre(), "Y with X");  // x0.y_はXオブジェクトを持っている
    }  // この次の行で、x0はスコープアウトし、以下の処理が実行される:
       //   1. x0のデストラクタが呼ばれ、x0.y_の参照カウントがデクリメント
       //   2. x0.y_の参照カウントが1→0になり、保持していたYオブジェクトを解放する
       //   3. Yオブジェクトのデストラクタ内でy_.x_(weak_ptr)が破棄されるが、weak_ptrなのでXオブジェクトの参照カウントには影響しない
       //   4. x0本体のデストラクタが完了し、Xオブジェクトの参照カウントが1→0になり、Xオブジェクトも解放される

    // 上記1-4によりダイナミックに生成されたオブジェクトは解放されたため、下記のテストが成立する
    ASSERT_EQ(X::constructed_counter, 0);
    ASSERT_EQ(Y::constructed_counter, 0);
```

上記コード例で見てきたように`std::weak_ptr`を使用することで:

- 循環参照によるメモリリークを防ぐことができる
- 必要に応じて`lock()`でオブジェクトにアクセスできる
- オブジェクトが既に解放されている場合は`lock()`が空の`shared_ptr`を返すため、安全に処理できる

### std::auto_ptr <a id="SS_3_5_4"></a>
`std::auto_ptr`はC++11以前に導入された初期のスマートポインタであるが、異常な[copyセマンティクス](cpp_idioms.md#SS_4_3_2)を持つため、
多くの誤用を生み出し、C++11から非推奨とされ、C++17から規格から排除された。


## Polymorphic Memory Resource(pmr) <a id="SS_3_6"></a>
Polymorphic Memory Resource(pmr)は、
動的メモリ管理の柔軟性と効率性を向上させるための、C++17から導入された仕組みである。

[std::pmr::polymorphic_allocator](stdlib_and_concepts.md#SS_3_6_2)はC++17で導入された標準ライブラリのクラスで、
C++のメモリリソース管理を抽象化するための機能を提供する。

例えば、std::vectorは以下のように宣言されていた。

```cpp
namespace std {
  template <class T, class Allocator = allocator<T>>
  class vector;
}
```

C++17では以下のエイリアスが追加された。

```cpp
namespace std::pmr {
  template <class T>
  using vector = std::vector<T, polymorphic_allocator<T>>;
}
```

他のコンテナに関してもほぼ同様のエイリアスが追加された。

C++17で導入されたstd::pmr名前空間は、カスタマイズ可能なメモリ管理を提供し、
特に標準ライブラリのコンテナと連携して効率化を図るための統一フレームワークを提供する。
std::pmrは、
カスタマイズ可能なメモリ管理を標準ライブラリのデータ構造に統合するための統一的なフレームワークであり、
特に標準ライブラリのコンテナと連携して、動的メモリ管理を効率化することができる。

std::pmrは以下のようなメモリ管理のカスタマイズを可能にする。

* メモリアロケータをポリモーフィック(動的に選択可能)にする。
* メモリ管理ポリシーをstd::pmr::memory_resourceで定義する。
* メモリリソースを再利用して効率的な動的メモリ管理を実現する。

std::pmrの主要なコンポーネントは以下の通りである。

* [std::pmr::memory_resource](stdlib_and_concepts.md#SS_3_6_1)  
* [std::pmr::polymorphic_allocator](stdlib_and_concepts.md#SS_3_6_2)  
* [pool_resource](stdlib_and_concepts.md#SS_3_6_3)

### std::pmr::memory_resource <a id="SS_3_6_1"></a>
std::pmr::memory_resourceは、
ユーザー定義のメモリリソースをカスタマイズし、
[std::pmr::polymorphic_allocator](stdlib_and_concepts.md#SS_3_6_2)を通じて利用可能にする[インターフェースクラス](core_lang_spec.md#SS_2_4_11)である。

std::pmr::memory_resourceから派生した具象クラスの実装を以下に示す。

```cpp
    //  example/stdlib_and__concepts/pmr_memory_resource_ut.cpp 64

    template <uint32_t MEM_SIZE>
    class memory_resource_variable final : public std::pmr::memory_resource {
    public:
        memory_resource_variable() noexcept
        {
            header_->next    = nullptr;
            header_->n_units = sizeof(buff_) / Inner_::unit_size;
        }

        size_t get_count() const noexcept { return unit_count_ * Inner_::unit_size; }
        bool   is_valid(void const* mem) const noexcept
        {
            return (&buff_ < mem) && (mem < &buff_.buffer[ArrayLength(buff_.buffer)]);
        }

        // ...

    private:
        using header_t = Inner_::header_t;

        Inner_::buffer_t<MEM_SIZE> buff_{};
        header_t*                  header_{reinterpret_cast<header_t*>(buff_.buffer)};
        mutable SpinLock           spin_lock_{};
        size_t                     unit_count_{sizeof(buff_) / Inner_::unit_size};
        size_t                     unit_count_min_{sizeof(buff_) / Inner_::unit_size};

        void* do_allocate(size_t size, size_t) override
        {
            auto n_units = (Roundup(Inner_::unit_size, size) / Inner_::unit_size) + 1;

            auto lock = std::lock_guard{spin_lock_};

            auto curr = header_;

            for (header_t* prev{nullptr}; curr != nullptr; prev = curr, curr = curr->next) {
                auto opt_next = std::optional<header_t*>{sprit(curr, n_units)};

                if (!opt_next) {
                    continue;
                }

                auto next = *opt_next;
                if (prev == nullptr) {
                    header_ = next;
                }
                else {
                    prev->next = next;
                }
                break;
            }

            if (curr != nullptr) {
                unit_count_ -= curr->n_units;
                unit_count_min_ = std::min(unit_count_, unit_count_min_);
                ++curr;
            }

            if (curr == nullptr) {
                throw std::bad_alloc{};
            }

            return curr;
        }

        void do_deallocate(void* mem, size_t, size_t) noexcept override
        {
            header_t* to_free = Inner_::set_back(mem);

            to_free->next = nullptr;

            auto lock = std::lock_guard{spin_lock_};

            unit_count_ += to_free->n_units;
            unit_count_min_ = std::min(unit_count_, unit_count_min_);

            if (header_ == nullptr) {
                header_ = to_free;
                return;
            }

            if (to_free < header_) {
                concat(to_free, header_);
                header_ = to_free;
                return;
            }

            header_t* curr = header_;

            for (; curr->next != nullptr; curr = curr->next) {
                if (to_free < curr->next) {  // 常に curr < to_free
                    concat(to_free, curr->next);
                    concat(curr, to_free);
                    return;
                }
            }

            concat(curr, to_free);
        }

        bool do_is_equal(const memory_resource& other) const noexcept override { return this == &other; }
    };
```

### std::pmr::polymorphic_allocator <a id="SS_3_6_2"></a>
std::pmr::polymorphic_allocatorはC++17で導入された標準ライブラリのクラスで、
C++のメモリリソース管理を抽象化するための機能を提供する。
[std::pmr::memory_resource](stdlib_and_concepts.md#SS_3_6_1)を基盤とし、
コンテナやアルゴリズムにカスタムメモリアロケーション戦略を容易に適用可能にする。
std::allocatorと異なり、型に依存せず、
ポリモーフィズムを活用してメモリリソースを切り替えられる点が特徴である。

すでに示したmemory_resource_variable([std::pmr::memory_resource](stdlib_and_concepts.md#SS_3_6_1))の単体テストを以下に示すことにより、
polymorphic_allocatorの使用例とする。

```cpp
    //  example/stdlib_and__concepts/pmr_memory_resource_ut.cpp 208

    constexpr uint32_t            max = 1024;
    memory_resource_variable<max> mrv;
    memory_resource_variable<max> mrv2;

    ASSERT_EQ(mrv, mrv);
    ASSERT_NE(mrv, mrv2);

    {
        auto remaings1 = mrv.get_count();

        ASSERT_GE(max, remaings1);

        // std::basic_stringにカスタムアロケータを適用
        using pmr_string = std::basic_string<char, std::char_traits<char>, std::pmr::polymorphic_allocator<char>>;
        std::pmr::polymorphic_allocator<char> allocator(&mrv);

        // カスタムアロケータを使って文字列を作成
        pmr_string str("custom allocator!", allocator);
        auto       remaings2 = mrv.get_count();
        // アサーション: 文字列の内容を確認

        ASSERT_GT(remaings1, remaings2);
        ASSERT_EQ("custom allocator!", str);

        ASSERT_TRUE(mrv.is_valid(str.c_str()));  // strの内部メモリがmrvの内部であることの確認

        auto str3 = str + str + str;
        ASSERT_EQ(str.size() * 3 + 1, str3.size() + 1);
        ASSERT_THROW(str3 = pmr_string(2000, 'a'), std::bad_alloc);  // メモリの枯渇テスト
    }

    ASSERT_GE(max, mrv.get_count());  // 解放後のメモリの回復のテスト
```

### pool_resource <a id="SS_3_6_3"></a>
pool_resourceは[std::pmr::memory_resource](stdlib_and_concepts.md#SS_3_6_1)を基底とする下記の2つの具象クラスである。

* std::pmr::synchronized_pool_resourceは下記のような特徴を持つメモリプールである。
    * 非同期のメモリプールリソース
    * シングルスレッド環境での高速なメモリ割り当てに適する
    * 排他制御のオーバーヘッドがない
    * 以下に使用例を示す。

```cpp
    //  example/stdlib_and__concepts/pool_resource_ut.cpp 10

    std::pmr::unsynchronized_pool_resource pool_resource(
        std::pmr::pool_options{
            .max_blocks_per_chunk        = 10,   // チャンクあたりの最大ブロック数
            .largest_required_pool_block = 1024  // 最大ブロックサイズ
        },
        std::pmr::new_delete_resource()  // フォールバックリソース
    );

    // vectorを使用したメモリ割り当てのテスト
    {
        std::pmr::vector<int> vec{&pool_resource};

        // ベクターへの要素追加
        vec.push_back(42);
        vec.push_back(100);

        // メモリ割り当てと要素の検証
        ASSERT_EQ(vec.size(), 2);
        ASSERT_EQ(vec[0], 42);
        ASSERT_EQ(vec[1], 100);
    }
```

* std::pmr::unsynchronized_pool_resource は下記のような特徴を持つメモリプールである。
    * スレッドセーフなメモリプールリソース
    * 複数のスレッドから同時にアクセス可能
    * 内部で排他制御を行う
    * 以下に使用例を示す。

```cpp
    //  example/stdlib_and__concepts/pool_resource_ut.cpp 38

    std::pmr::synchronized_pool_resource shared_pool;

    auto thread_func = [&shared_pool](int thread_id) {
        std::pmr::vector<int> local_vec{&shared_pool};

        // スレッドごとに異なる要素を追加
        local_vec.push_back(thread_id * 10);
        local_vec.push_back(thread_id * 20);

        ASSERT_EQ(local_vec.size(), 2);
    };

    // 複数スレッドでの同時使用
    std::thread t1(thread_func, 1);
    std::thread t2(thread_func, 2);

    t1.join();
    t2.join();
```


## コンテナ <a id="SS_3_7"></a>
データを格納し、
効率的に操作するための汎用的なデータ構造を提供するC++標準ライブラリの下記のようなクラス群である。

* [シーケンスコンテナ(Sequence Containers)](stdlib_and_concepts.md#SS_3_7_1)
* [連想コンテナ(Associative Containers)(---)
* [無順序連想コンテナ(Unordered Associative Containers)](stdlib_and_concepts.md#SS_3_7_3)
* [コンテナアダプタ(Container Adapters)](stdlib_and_concepts.md#SS_3_7_4)
* [特殊なコンテナ](stdlib_and_concepts.md#SS_3_7_5)

### シーケンスコンテナ(Sequence Containers) <a id="SS_3_7_1"></a>
データが挿入順に保持され、順序が重要な場合に使用する。

| コンテナ                 | 説明                                                                |
|--------------------------|---------------------------------------------------------------------|
| `std::vector`            | 動的な配列で、ランダムアクセスが高速。末尾への挿入/削除が効率的     |
| `std::deque`             | 両端に効率的な挿入/削除が可能な動的配列                             |
| `std::list`              | 双方向リスト。要素の順序を維持し、中間の挿入/削除が効率的           |
| [std::forward_list](stdlib_and_concepts.md#SS_3_7_1_1) | 単方向リスト。軽量だが、双方向の操作はできない                      |
| `std::array`             | 固定長配列で、サイズがコンパイル時に決まる                          |
| `std::string`            | 可変長の文字列を管理するクラス(厳密には`std::basic_string`の特殊化) |

#### std::forward_list <a id="SS_3_7_1_1"></a>

```cpp
    //  example/stdlib_and__concepts/container_ut.cpp 14

    std::forward_list<int> fl{1, 2, 3};

    // 要素の挿入
    EXPECT_EQ(fl.front(), 1);
    fl.push_front(0);
    EXPECT_EQ(fl.front(), 0);

    auto it = fl.begin();
    EXPECT_EQ(*++it, 1);
    EXPECT_EQ(*++it, 2);
    EXPECT_EQ(*++it, 3);
```

### 連想コンテナ(Associative Containers) <a id="SS_3_7_2"></a>
データがキーに基づいて自動的にソートされ、検索が高速である。

| コンテナ           | 説明                                             |
|--------------------|--------------------------------------------------|
| `std::set`         | 要素がソートされ、重複が許されない集合           |
| `std::multiset`    | ソートされるが、重複が許される集合               |
| `std::map`         | ソートされたキーと値のペアを保持。キーは一意     |
| `std::multimap`    | ソートされたキーと値のペアを保持。キーは重複可能 |

### 無順序連想コンテナ(Unordered Associative Containers) <a id="SS_3_7_3"></a>
ハッシュテーブルを基盤としたコンテナで、順序を保証しないが高速な検索を提供する。

| コンテナ                  | 説明                                                   |
|---------------------------|--------------------------------------------------------|
| [std::unordered_set](stdlib_and_concepts.md#SS_3_7_3_1) | ハッシュテーブルベースの集合。重複は許されない         |
| `std::unordered_multiset` | ハッシュテーブルベースの集合。重複が許される           |
| [std::unordered_map](stdlib_and_concepts.md#SS_3_7_3_2) | ハッシュテーブルベースのキーと値のペア。キーは一意     |
| `std::unordered_multimap` | ハッシュテーブルベースのキーと値のペア。キーは重複可能 |
| [std::type_index](stdlib_and_concepts.md#SS_3_7_3_3)    | 型情報型を連想コンテナのキーとして使用するためのクラス |

#### std::unordered_set <a id="SS_3_7_3_1"></a>

```cpp
    //  example/stdlib_and__concepts/container_ut.cpp 32

    std::unordered_set<int> uset{1, 2, 3};

    // 要素の挿入
    uset.insert(4);
    uset.insert(5);

    // 存在確認
    EXPECT_NE(uset.find(1), uset.end());
    EXPECT_NE(uset.find(4), uset.end());
    EXPECT_EQ(uset.find(6), uset.end());

    // サイズの確認
    EXPECT_EQ(uset.size(), 5);
```

#### std::unordered_map <a id="SS_3_7_3_2"></a>

```cpp
    //  example/stdlib_and__concepts/container_ut.cpp 52

    std::unordered_map<int, std::string> umap;

    // 要素の挿入
    umap[1] = "one";
    umap[2] = "two";
    umap[3] = "three";

    // 要素の確認
    EXPECT_EQ(umap[1], "one");
    EXPECT_EQ(umap[2], "two");
    EXPECT_EQ(umap[3], "three");

    // 存在確認
    EXPECT_NE(umap.find(1), umap.end());
    EXPECT_EQ(umap.find(4), umap.end());
```

#### std::type_index <a id="SS_3_7_3_3"></a>
std::type_indexはコンテナではないが、
型情報型を連想コンテナのキーとして使用するためのクラスであるため、この場所に掲載する。

```cpp
    //  example/stdlib_and__concepts/container_ut.cpp 74

    std::unordered_map<std::type_index, std::string> type_map;

    // std::type_indexを使って型をキーとしてマッピング
    type_map[typeid(int)]         = "int";
    type_map[typeid(double)]      = "double";
    type_map[typeid(std::string)] = "string";

    // マッピングの確認
    EXPECT_EQ(type_map[typeid(int)], "int");
    EXPECT_EQ(type_map[typeid(double)], "double");
    EXPECT_EQ(type_map[typeid(std::string)], "string");

    // 存在しない型の確認
    EXPECT_EQ(type_map.find(typeid(float)), type_map.end());
```


### コンテナアダプタ(Container Adapters) <a id="SS_3_7_4"></a>
特定の操作のみを公開するためのラッパーコンテナ。

| コンテナ              | 説明                                     |
|-----------------------|------------------------------------------|
| `std::stack`          | LIFO(後入れ先出し)操作を提供するアダプタ |
| `std::queue`          | FIFO(先入れ先出し)操作を提供するアダプタ |
| `std::priority_queue` | 優先度に基づく操作を提供するアダプタ     |

### 特殊なコンテナ <a id="SS_3_7_5"></a>
上記したようなコンテナとは一線を画すが、特定の用途や目的のために設計された一種のコンテナ。

| コンテナ             | 説明                                                       |
|----------------------|------------------------------------------------------------|
| `std::span`          | 生ポインタや配列を抽象化し、安全に操作するための軽量ビュー |
| `std::bitset`        | 固定長のビット集合を管理するクラス                         |
| `std::basic_string`  | カスタム文字型をサポートする文字列コンテナ                 |

## std::optional <a id="SS_3_8"></a>
C++17から導入されたstd::optionalには、以下のような2つの用途がある。
以下の用途2から、
このクラスがオブジェクトのダイナミックなメモリアロケーションを行うような印象を受けるが、
そのようなことは行わない。
このクラスがオブジェクトのダイナミックな生成が必要になった場合、プレースメントnewを実行する。
ただし、std::optionalが保持する型自身がnewを実行する場合は、この限りではない。

1. 関数の任意の型の[戻り値の無効表現](stdlib_and_concepts.md#SS_3_8_1)を持たせる
2. [オブジェクトの遅延初期化](stdlib_and_concepts.md#SS_3_8_2)する(初期化処理が重く、
   条件によってはそれが無駄になる場合にこの機能を使う)

### 戻り値の無効表現 <a id="SS_3_8_1"></a>
```cpp
    //  example/stdlib_and__concepts/optional_ut.cpp 11

    /// @brief 指定されたファイル名から拡張子を取得する。
    /// @param filename ファイル名（パスを含む場合も可）
    /// @return 拡張子を文字列として返す。拡張子がない場合は std::nullopt を返す。
    std::optional<std::string> file_extension(std::string const& filename)
    {
        size_t pos = filename.rfind('.');
        if (pos == std::string::npos || pos == filename.length() - 1) {
            return std::nullopt;  // 値が存在しない
        }
        return filename.substr(pos + 1);
    }
```
```cpp
    //  example/stdlib_and__concepts/optional_ut.cpp 28

    auto ret0 = file_extension("xxx.yyy");

    ASSERT_TRUE(ret0);  // 値を保持している
    ASSERT_EQ("yyy", *ret0);

    auto ret1 = file_extension("xxx");

    ASSERT_FALSE(ret1);  // 値を保持していない
    // ASSERT_THROW(*ret1, std::exception);  // 未定義動作(エクセプションは発生しない)
    ASSERT_THROW(ret1.value(), std::bad_optional_access);  // 値非保持の場合、エクセプション発生
```

### オブジェクトの遅延初期化 <a id="SS_3_8_2"></a>
```cpp
    //  example/stdlib_and__concepts/optional_ut.cpp 43

    class HeavyResource {
    public:
        HeavyResource() : large_erea_{0xdeadbeaf}
        {  // large_erea_[0]を44にする
            initialied = true;
        }
        bool     is_ready() const noexcept { return large_erea_[0] == 0xdeadbeaf; }
        uint32_t operator[](size_t index) const noexcept { return large_erea_[index]; }

        static bool initialied;

    private:
        uint32_t large_erea_[1024];
    };
    bool HeavyResource::initialied;
```
```cpp
    //  example/stdlib_and__concepts/optional_ut.cpp 64

    std::optional<HeavyResource> resource;

    // resourceの内部のHeavyResourceは未初期化
    ASSERT_FALSE(resource.has_value());
    ASSERT_FALSE(HeavyResource::initialied);
    ASSERT_NE(0xdeadbeaf, (*resource)[0]);  // 未定義動作

    // resourceの内部のHeavyResourceの遅延初期化
    resource.emplace();  // std::optionalの内部でplacement newが実行される

    // ここから下は定義動作
    ASSERT_TRUE(HeavyResource::initialied);  // resourceの内部のHeavyResourceは初期化済み
    ASSERT_TRUE(resource.has_value());

    ASSERT_TRUE(resource->is_ready());
    ASSERT_EQ(0xdeadbeaf, (*resource)[0]);
```

## std::variant <a id="SS_3_9"></a>
std::variantは、C++17で導入された型安全なunionである。
このクラスは複数の型のうち1つの値を保持することができ、
従来のunionに伴う低レベルな操作の安全性の問題を解消するために設計された。

std::variant自身では、オブジェクトのダイナミックな生成が必要な場合でも通常のnewを実行せず、
代わりにプレースメントnewを用いる
(以下のコード例のようにstd::variantが保持する型自身がnewを実行する場合は、この限りではない)。

以下にstd::variantの典型的な使用例を示す。

```cpp
    //  example/stdlib_and__concepts/variant_ut.cpp 13

    std::variant<int, std::string, double> var  = 10;
    auto                                   var2 = var;  // コピーコンストラクタの呼び出し

    ASSERT_EQ(std::get<int>(var), 10);  // 型intの値を取り出す

    // 型std::stringの値を取り出すが、その値は持っていないのでエクセプション発生
    ASSERT_THROW(std::get<std::string>(var), std::bad_variant_access);

    var = "variant";  // "variant"はstd::stringに変更され、varにムーブされる
    ASSERT_EQ(std::get<std::string>(var), "variant");

    ASSERT_NE(var, var2);  // 保持している値の型が違う

    var2.emplace<std::string>("variant");  // "variant"からvar2の値を直接生成するため、
                                           // 文字列代入より若干効率的
    ASSERT_EQ(var, var2);

    var = 1.0;
    ASSERT_FLOAT_EQ(std::get<2>(var), 1.0);  // 2番目の型の値を取得
```

std::variantとstd::visit([Visitor](design_pattern.md#SS_6_21)パターンの実装の一種)を組み合わせた場合の使用例を以下に示す。

```cpp
    //  example/stdlib_and__concepts/variant_ut.cpp 37

    void output_from_variant(std::variant<int, double, std::string> const& var, std::ostringstream& oss)
    {
        std::visit([&oss](auto&& arg) { oss.str().empty() ? oss << arg : oss << "|" << arg; }, var);
    }
```
```cpp
    //  example/stdlib_and__concepts/variant_ut.cpp 47

    std::ostringstream                     oss;
    std::variant<int, double, std::string> var = 42;

    output_from_variant(var, oss);
    ASSERT_EQ("42", oss.str());

    var = 3.14;
    output_from_variant(var, oss);
    ASSERT_EQ("42|3.14", oss.str());

    var = "Hello, world!";
    output_from_variant(var, oss);
    ASSERT_EQ("42|3.14|Hello, world!", oss.str());
```

## オブジェクトの比較 <a id="SS_3_10"></a>
### std::rel_ops <a id="SS_3_10_1"></a>
クラスに`operator==`と`operator<`の2つの演算子が定義されていれば、
それがメンバか否かにかかわらず、他の比較演算子 !=、<=、>、>= はこれらを基に自動的に導出できる。
std::rel_opsでは`operator==`と`operator<=` を基に他の比較演算子を機械的に生成する仕組みが提供されている。

次の例では、std::rel_opsを利用して、少ないコードで全ての比較演算子をサポートする例を示す。

```cpp
    //  example/stdlib_and__concepts/comparison_stdlib_ut.cpp 12

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        // operator==とoperator<だけを定義
        int get() const noexcept { return x_; }

        // メンバ関数の比較演算子
        bool operator==(const Integer& other) const noexcept { return x_ == other.x_; }
        bool operator<(const Integer& other) const noexcept { return x_ < other.x_; }

    private:
        int x_;
    };
```

```cpp
    //  example/stdlib_and__concepts/comparison_stdlib_ut.cpp 32

    using namespace std::rel_ops;  // std::rel_opsを使うために名前空間を追加

    auto a = Integer{5};
    auto b = Integer{10};
    auto c = Integer{5};

    // std::rel_opsとは無関係に直接定義
    ASSERT_TRUE(a == c);   // a == c
    ASSERT_FALSE(a == b);  // !(a == b)
    ASSERT_TRUE(a < b);    // aはbより小さい
    ASSERT_FALSE(b < a);   // bはaより小さくない

    // std::rel_ops による!=, <=, >, >=の定義
    ASSERT_TRUE(a != b);   // aとbは異なる
    ASSERT_TRUE(a <= b);   // aはb以下
    ASSERT_TRUE(b > a);    // bはaより大きい
    ASSERT_FALSE(a >= b);  // aはb以上ではない
```

なお、std::rel_opsはC++20から導入された[<=>演算子](core_lang_spec.md#SS_2_6_4_1)により不要になったため、
非推奨とされた。

### std::tuppleを使用した比較演算子の実装方法 <a id="SS_3_10_2"></a>
クラスのメンバが多い場合、[==演算子](core_lang_spec.md#SS_2_6_3)で示したような方法は、
可読性、保守性の問題が発生する場合が多い。下記に示す方法はこの問題を幾分緩和する。

```cpp
    //  example/stdlib_and__concepts/comparison_stdlib_ut.cpp 56

    struct Point {
        int x;
        int y;

        bool operator==(const Point& other) const noexcept { return std::tie(x, y) == std::tie(other.x, other.y); }

        bool operator<(const Point& other) const noexcept { return std::tie(x, y) < std::tie(other.x, other.y); }
    };
```
```cpp
    //  example/stdlib_and__concepts/comparison_stdlib_ut.cpp 70

    auto a = Point{1, 2};
    auto b = Point{1, 3};
    auto c = Point{1, 2};

    using namespace std::rel_ops;  // std::rel_opsを使うために名前空間を追加

    ASSERT_TRUE(a == c);
    ASSERT_TRUE(a != b);
    ASSERT_TRUE(a < b);
    ASSERT_FALSE(a > b);
```

## その他 <a id="SS_3_11"></a>
### SSO(Small String Optimization) <a id="SS_3_11_1"></a>
一般にstd::stringで文字列を保持する場合、newしたメモリが使用される。
64ビット環境であれば、newしたメモリのアドレスを保持する領域は8バイトになる。
std::stringで保持する文字列が終端の'\0'も含め8バイト以下である場合、
アドレスを保持する領域をその文字列の格納に使用すれば、newする必要がない(当然deleteも不要)。
こうすることで、短い文字列を保持するstd::stringオブジェクトは効率的に動作できる。

SOOとはこのような最適化を指す。

### heap allocation elision <a id="SS_3_11_2"></a>
C++11までの仕様では、new式によるダイナミックメモリアロケーションはコードに書かれた通りに、
実行されなければならず、ひとまとめにしたり省略したりすることはできなかった。
つまり、ヒープ割り当てに対する最適化は認められなかった。
ダイナミックメモリアロケーションの最適化のため、この制限は緩和され、
new/deleteの呼び出しをまとめたり省略したりすることができるようになった。

```cpp
    //  example/stdlib_and__concepts/heap_allocation_elision_ut.cpp 4

    void lump()  // 実装によっては、ダイナミックメモリアロケーションをまとめらる場合がある
    {
        int* p1 = new int{1};
        int* p2 = new int{2};
        int* p3 = new int{3};

        // 何らかの処理

        delete p1;
        delete p2;
        delete p3;

        // 上記のメモリアロケーションは、実装によっては下記のように最適化される場合がある

        int* p = new int[3]{1, 2, 3};
        // 何らかの処理

        delete[] p;
    }

    int emit()  // ダイナミックメモリアロケーションの省略
    {
        int* p = new int{10};
        delete p;

        // 上記のメモリアロケーションは、下記の用にスタックの変数に置き換える最適化が許される

        int n = 10;

        return n;
    }
```

この最適化により、std::make_sharedのようにstd::shared_ptrの参照カウントを管理するメモリブロックと、
オブジェクトの実体を1つのヒープ領域に割り当てることができ、
ダイナミックメモリアロケーションが1回に抑えられるため、メモリアクセスが高速化される。



