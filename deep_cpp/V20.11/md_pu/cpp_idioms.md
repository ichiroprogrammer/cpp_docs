<!-- essential/md/cpp_idioms.md -->
# C++慣用語句 <a id="SS_8"></a>
この章では、C++慣用言句ついて解説を行う。

___

__この章の構成__

&emsp;&emsp; [オブジェクト指向](cpp_idioms.md#SS_8_1)  
&emsp;&emsp;&emsp; [is-a](cpp_idioms.md#SS_8_1_1)  
&emsp;&emsp;&emsp; [has-a](cpp_idioms.md#SS_8_1_2)  
&emsp;&emsp;&emsp; [is-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3)  
&emsp;&emsp;&emsp;&emsp; [public継承によるis-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_1)  
&emsp;&emsp;&emsp;&emsp; [private継承によるis-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_2)  
&emsp;&emsp;&emsp;&emsp; [コンポジションによる(has-a)is-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_3)  

&emsp;&emsp; [オブジェクトの所有権](cpp_idioms.md#SS_8_2)  
&emsp;&emsp;&emsp; [オブジェクトの排他所有](cpp_idioms.md#SS_8_2_1)  
&emsp;&emsp;&emsp; [オブジェクトの共有所有](cpp_idioms.md#SS_8_2_2)  
&emsp;&emsp;&emsp; [オブジェクトの循環所有](cpp_idioms.md#SS_8_2_3)  

&emsp;&emsp; [copy/moveと等価性のセマンティクス](cpp_idioms.md#SS_8_3)  
&emsp;&emsp;&emsp; [等価性のセマンティクス](cpp_idioms.md#SS_8_3_1)  
&emsp;&emsp;&emsp; [copyセマンティクス](cpp_idioms.md#SS_8_3_2)  
&emsp;&emsp;&emsp; [moveセマンティクス](cpp_idioms.md#SS_8_3_3)  
&emsp;&emsp;&emsp; [MoveAssignable要件](cpp_idioms.md#SS_8_3_4)  
&emsp;&emsp;&emsp; [CopyAssignable要件](cpp_idioms.md#SS_8_3_5)  

&emsp;&emsp; [関数設計のガイドライン](cpp_idioms.md#SS_8_4)  
&emsp;&emsp;&emsp; [関数の引数と戻り値の型](cpp_idioms.md#SS_8_4_1)  
&emsp;&emsp;&emsp; [サイクロマティック複雑度のクライテリア](cpp_idioms.md#SS_8_4_2)  
&emsp;&emsp;&emsp; [関数の行数のクライテリア](cpp_idioms.md#SS_8_4_3)  

&emsp;&emsp; [クラス設計のガイドライン](cpp_idioms.md#SS_8_5)  
&emsp;&emsp;&emsp; [ゼロの原則(Rule of Zero)](cpp_idioms.md#SS_8_5_1)  
&emsp;&emsp;&emsp; [五の原則(Rule of Five)](cpp_idioms.md#SS_8_5_2)  
&emsp;&emsp;&emsp; [クラス凝集性のクライテリア](cpp_idioms.md#SS_8_5_3)  

&emsp;&emsp; [コーディングスタイル](cpp_idioms.md#SS_8_6)  
&emsp;&emsp;&emsp; [AAAスタイル](cpp_idioms.md#SS_8_6_1)  
&emsp;&emsp;&emsp; [east-const](cpp_idioms.md#SS_8_6_2)  
&emsp;&emsp;&emsp; [west-const](cpp_idioms.md#SS_8_6_3)  

&emsp;&emsp; [オブジェクトのコピー](cpp_idioms.md#SS_8_7)  
&emsp;&emsp;&emsp; [シャローコピー](cpp_idioms.md#SS_8_7_1)  
&emsp;&emsp;&emsp; [ディープコピー](cpp_idioms.md#SS_8_7_2)  
&emsp;&emsp;&emsp; [スライシング](cpp_idioms.md#SS_8_7_3)  

&emsp;&emsp; [C++注意点](cpp_idioms.md#SS_8_8)  
&emsp;&emsp;&emsp; [オーバーライドとオーバーロードの違い](cpp_idioms.md#SS_8_8_1)  
&emsp;&emsp;&emsp; [danglingリファレンス](cpp_idioms.md#SS_8_8_2)  
&emsp;&emsp;&emsp; [danglingポインタ](cpp_idioms.md#SS_8_8_3)  
&emsp;&emsp;&emsp; [Most Vexing Parse](cpp_idioms.md#SS_8_8_4)  

&emsp;&emsp; [ソフトウェア一般](cpp_idioms.md#SS_8_9)  
&emsp;&emsp;&emsp; [ヒープ](cpp_idioms.md#SS_8_9_1)  
&emsp;&emsp;&emsp; [スレッドセーフ](cpp_idioms.md#SS_8_9_2)  
&emsp;&emsp;&emsp; [リエントラント](cpp_idioms.md#SS_8_9_3)  
&emsp;&emsp;&emsp; [クリティカルセクション](cpp_idioms.md#SS_8_9_4)  
&emsp;&emsp;&emsp; [スピンロック](cpp_idioms.md#SS_8_9_5)  
&emsp;&emsp;&emsp; [ハンドル](cpp_idioms.md#SS_8_9_6)  
&emsp;&emsp;&emsp; [フリースタンディング環境](cpp_idioms.md#SS_8_9_7)  
&emsp;&emsp;&emsp; [サイクロマティック複雑度](cpp_idioms.md#SS_8_9_8)  
&emsp;&emsp;&emsp; [凝集性](cpp_idioms.md#SS_8_9_9)  
&emsp;&emsp;&emsp;&emsp; [凝集性の欠如](cpp_idioms.md#SS_8_9_9_1)  
&emsp;&emsp;&emsp;&emsp; [LCOM](cpp_idioms.md#SS_8_9_9_2)  

&emsp;&emsp;&emsp; [Spurious Wakeup](cpp_idioms.md#SS_8_9_10)  
&emsp;&emsp;&emsp; [Static Initialization Order Fiasco(静的初期化順序問題)](cpp_idioms.md#SS_8_9_11)  
&emsp;&emsp;&emsp; [副作用](cpp_idioms.md#SS_8_9_12)  
&emsp;&emsp;&emsp; [Itanium C++ ABI](cpp_idioms.md#SS_8_9_13)  

&emsp;&emsp; [C++コンパイラ](cpp_idioms.md#SS_8_10)  
&emsp;&emsp;&emsp; [g++](cpp_idioms.md#SS_8_10_1)  
&emsp;&emsp;&emsp; [clang++](cpp_idioms.md#SS_8_10_2)  

&emsp;&emsp; [非ソフトウェア用語](cpp_idioms.md#SS_8_11)  
&emsp;&emsp;&emsp; [セマンティクス](cpp_idioms.md#SS_8_11_1)  
&emsp;&emsp;&emsp; [割れ窓理論](cpp_idioms.md#SS_8_11_2)  
&emsp;&emsp;&emsp; [車輪の再発明](cpp_idioms.md#SS_8_11_3)  
  
  

[インデックス](deep_intro.md#SS_1_2)に戻る。  

___

## オブジェクト指向 <a id="SS_8_1"></a>
### is-a <a id="SS_8_1_1"></a>
「is-a」の関係は、オブジェクト指向プログラミング（OOP）
においてクラス間の継承関係を説明する際に使われる概念である。
クラスDerivedとBaseが「is-a」の関係である場合、
DerivedがBaseの派生クラスであり、Baseの特性をDerivedが引き継いでいることを意味する。
C++でのOOPでは、DerivedはBaseのpublic継承として定義される。
通常DerivedやBaseは以下の条件を満たす必要がある。

* Baseはvirtualメンバ関数(Base::f)を持つ。
* DerivedはBase::fのオーバーライド関数を持つ。
* DerivedはBaseに対して
  [リスコフの置換原則](https://ja.wikipedia.org/wiki/%E3%83%AA%E3%82%B9%E3%82%B3%E3%83%95%E3%81%AE%E7%BD%AE%E6%8F%9B%E5%8E%9F%E5%89%87)
  を守る必要がある。
  この原則を簡単に説明すると、
  「派生クラスのオブジェクトは、
  いつでもその基底クラスのオブジェクトと置き換えても、
  プログラムの動作に悪影響を与えずに問題が発生してはならない」という設計の制約である。

 「is-a」の関係とは「一種の～」と言い換えることができることが多い.
ペンギンや九官鳥 は一種の鳥であるため、この関係を使用したコード例を次に示す。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 11

    class bird {
    public:
        //  事前条件: altitude  > 0 でなければならない
        //  事後条件: 呼び出しが成功した場合、is_flyingがtrueを返すことである
        virtual void fly(int altitude)
        {
            if (not(altitude > 0)) {  // 高度(altitude)は0より大きくなければ、飛べない
                throw std::invalid_argument{"altitude error"};
            }
            altitude_ = altitude;
        }

        bool is_flying() const noexcept
        {
            return altitude_ != 0;  // 高度が0でなければ、飛んでいると判断
        }

        virtual ~bird() = default;

    private:
        int altitude_ = 0;
    };

    class kyukancho : public bird {
    public:
        void speak()
        {
            // しゃべるため処理
        }

        // このクラスにget_nameを追加した理由はこの後を読めばわかる
        virtual std::string get_name() const  // その個体の名前を返す
        {
            return "no name";
        }
    };
```

bird::flyのオーバーライド関数(penguin::fly)について、[リスコフの置換原則(LSP)](solid.md#SS_2_3)に反した例を下記する。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 50

    class penguin : public bird {
    public:
        void fly(int altitude) override
        {
            if (altitude != 0) {
                throw std::invalid_argument{"altitude error"};
            }
        }
    };

    // 単体テストを行うためのラムダ
    auto let_it_fly = [](bird& b, int altitude) {
        try {
            b.fly(altitude);
        }
        catch (std::exception const&) {
            return 0;  // エクセプションが発生した
        }

        return b.is_flying() ? 2 : 1;  // is_flyingがfalseなら1を返す
    };

    bird    b;
    penguin p;
    ASSERT_EQ(let_it_fly(p, 0), 1);  // パスする
    // リスコフ置換原則が満たされていれば、派生クラス(penguin)
    // を基底クラス(bird)で置き換えても同じ結果になるはずだが、
    // 実際には逆に下記テストがパスしてしまう
    ASSERT_NE(let_it_fly(b, 0), 1);  // let_it_fly(b, 0) != 1　であることに注意
    // このことからpenguinへの派生はリスコフ置換の原則を満たさない

```

birdからpenguinへの派生がリスコフ置換の原則に反してしまった原因は以下のように考えることができる。

* bird::flyの事前条件penguin::flyが強めた
* bird::flyの事後条件をpenguin::flyが弱めた

penguinとbirdの関係はis-aの関係ではあるが、
上記コードの問題によって不適切なis-aの関係と言わざるを得ない。

上記の例では鳥全般と鳥の種類のis-a関係をpublic継承を使用して表した(一部不適切であるもの)。
さらにis-aの誤った適用例を示す。
自身が飼っている九官鳥に"キューちゃん"と名付けることはよくあることである。
キューちゃんという名前の九官鳥は一種の九官鳥であることは間違いのないことであるが、
このis-aの関係を表すためにpublic継承を使用するのは、is-aの関係の誤用になることが多い。
実際のコード例を以下に示す。この場合、型とインスタンスの概念の混乱が原因だと思われる。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 91

    class q_chan : public kyukancho {
    public:
        std::string get_name() const override { return "キューちゃん"; }
    };
```

この誤用を改めた例を以下に示す。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 113

    class kyukancho {
    public:
        kyukancho(std::string name) : name_{std::move(name)} {}

        std::string const& get_name() const  // 名称をメンバ変数で保持するため、virtualである必要はない
        {
            return name_;
        }

        virtual ~kyukancho() = default;

    private:
        std::string const name_;  // 名称の保持
    };

    // ...

    kyukancho q{"キューちゃん"};

    ASSERT_EQ("キューちゃん", q.get_name());
```

修正されたKyukancho はstd::string インスタンスをメンバ変数として持ち、
kyukanchoとstd::stringの関係を[has-a](cpp_idioms.md#SS_8_1_2)の関係と呼ぶ。


### has-a <a id="SS_8_1_2"></a>
「has-a」の関係は、
あるクラスのインスタンスが別のクラスのインスタンスを構成要素として含む関係を指す。
つまり、あるクラスのオブジェクトが別のクラスのオブジェクトを保持している関係である。

例えば、CarクラスとEngineクラスがあるとする。CarクラスはEngineクラスのインスタンスを含むので、
CarはEngineを「has-a」の関係にあると言える。
通常、has-aの関係はクラス内でメンバ変数またはメンバオブジェクトとして実装される。
Carクラスの例ではCarクラスにはEngine型のメンバ変数が存在する。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 144

    class Engine {
    public:
        void start() {}  // エンジンを始動するための処理
        void stop() {}   // エンジンを停止するための処理

    private:
        // ...
    };

    class Car {
    public:
        Car() : engine_{} {}
        void start() { engine_.start(); }
        void stop() { engine_.stop(); }

    private:
        Engine engine_;  // Car は Engine を持っている（has-a）
    };
```

### is-implemented-in-terms-of <a id="SS_8_1_3"></a>
「is-implemented-in-terms-of」の関係は、
オブジェクト指向プログラミング（OOP）において、
あるクラスが別のクラスの機能を内部的に利用して実装されていることを示す概念である。
これは、あるクラスが他のクラスのインターフェースやメンバ関数を用いて、
自身の機能を提供する場合に使われる。
[has-a](cpp_idioms.md#SS_8_1_2)の関係は、is-implemented-in-terms-of の関係の一種である。

is-implemented-in-terms-ofは下記の手段1-3に示した方法がある。

* 手段1.[public継承によるis-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_1)  
* 手段2.[private継承によるis-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_2)  
* 手段3.[コンポジションによる(has-a)is-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_3)  

手段1-3にはそれぞれ、長所、短所があるため、必要に応じて手段を選択する必要がある。
以下の議論を単純にするため、下記のようにクラスS、C、CCを定める。

* S(サーバー): 実装を提供するクラス
* C(クライアント): Sの実装を利用するクラス
* CC(クライアントのクライアント): Cのメンバを使用するクラス

コード量の観点から考えた場合、手段1が最も優れていることが多い。
依存関係の複雑さから考えた場合、CはSに強く依存する。
場合によっては、この依存はCCからSへの依存間にも影響をあたえる。
従って、手段3が依存関係を単純にしやすい。
手段1は[is-a](cpp_idioms.md#SS_8_1_1)に見え、以下に示すような問題も考慮する必要があるため、
可読性、保守性を劣化させる可能性がある。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 260

    class MyString : public std::string {  // 手段1
    };

    // ...
    std::string* m_str = new MyString{"str"};

    // このようなpublic継承を行う場合、基底クラスのデストラクタは非virtualであるため、
    // 以下のコードではｈmy_stringのデストラクタは呼び出されない。
    // この問題はリソースリークを発生させる場合がある。
    delete m_str;
```

以上述べたように問題の多い手段1であるが、実践的には有用なパターンであり、
[CRTP(curiously recurring template pattern)](https://ja.wikibooks.org/wiki/More_C%2B%2B_Idioms/%E5%A5%87%E5%A6%99%E3%81%AB%E5%86%8D%E5%B8%B0%E3%81%97%E3%81%9F%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3(Curiously_Recurring_Template_Pattern))
の実現手段でもあるため、一概にコーディング規約などで排除することもできない。


#### public継承によるis-implemented-in-terms-of <a id="SS_8_1_3_1"></a>
public継承によるis-implemented-in-terms-ofの実装例を以下に示す。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 282

    class MyString : public std::string {};

    // ...
    MyString str{"str"};

    ASSERT_EQ(str[0], 's');
    ASSERT_STREQ(str.c_str(), "str");

    str.clear();
    ASSERT_EQ(str.size(), 0);
```

すでに述べたようにこの方法は、
[private継承によるis-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_2)や、
[コンポジションによる(has-a)is-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_3)
と比べコードがシンプルになる。 

#### private継承によるis-implemented-in-terms-of <a id="SS_8_1_3_2"></a>
private継承によるis-implemented-in-terms-ofの実装例を以下に示す。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 179

    class MyString : std::string {
    public:
        using std::string::string;
        using std::string::operator[];
        using std::string::c_str;
        using std::string::clear;
        using std::string::size;
    };

    // ...
    MyString str{"str"};

    ASSERT_EQ(str[0], 's');
    ASSERT_STREQ(str.c_str(), "str");

    str.clear();
    ASSERT_EQ(str.size(), 0);
```

この方法は、[public継承によるis-implemented-in-terms-of](cpp_idioms.md#SS_8_1_3_1)が持つデストラクタ問題は発生せす、
[is-a](cpp_idioms.md#SS_8_1_1)と誤解してしまう問題も発生しない。


#### コンポジションによる(has-a)is-implemented-in-terms-of <a id="SS_8_1_3_3"></a>
コンポジションによる(has-a)is-implemented-in-terms-ofの実装例を示す。

```cpp
    //  example/cpp_idioms/class_relation_ut.cpp 207

    namespace is_implemented_in_terms_of_1 {
    class MyString {
    public:
        // コンストラクタ
        MyString() = default;
        MyString(const std::string& str) : str_(str) {}
        MyString(const char* cstr) : str_(cstr) {}

        // 文字列へのアクセス
        const char* c_str() const { return str_.c_str(); }

        using reference = std::string::reference;
        using size_type = std::string::size_type;

        reference operator[](size_type pos) { return str_[pos]; }

        // その他のメソッドも必要に応じて追加する
        // 以下は例
        std::size_t size() const { return str_.size(); }

        void clear() { str_.clear(); }

        MyString& operator+=(const MyString& rhs)
        {
            str_ += rhs.str_;
            return *this;
        }

    private:
        std::string str_;
    };

    // ...
    MyString str{"str"};

    ASSERT_EQ(str[0], 's');
    ASSERT_STREQ(str.c_str(), "str");

    str.clear();
    ASSERT_EQ(str.size(), 0);
```

この方は実装を利用するクラストの依存関係を他の2つに比べるとシンプルにできるが、
逆に実装例から昭なとおり、コード量が増えてしまう。

## オブジェクトの所有権 <a id="SS_8_2"></a>
### オブジェクトの排他所有 <a id="SS_8_2_1"></a>
オブジェクトの排他所有や、それを容易に実現するための
[std::unique_ptr](https://cpprefjp.github.io/reference/memory/unique_ptr.html)
の仕様を説明するために、下記のようにクラスA、Xを定義する。

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 7

    class A final {
    public:
        explicit A(int32_t n) noexcept : num_{n} { last_constructed_num_ = num_; }
        ~A() { last_destructed_num_ = num_; }

        int32_t GetNum() const noexcept { return num_; }

        static int32_t LastConstructedNum() noexcept { return last_constructed_num_; }
        static int32_t LastDestructedNum() noexcept { return last_destructed_num_; }

    private:
        int32_t const  num_;
        static int32_t last_constructed_num_;
        static int32_t last_destructed_num_;
    };

    int32_t A::last_constructed_num_ = -1;
    int32_t A::last_destructed_num_  = -1;

    class X final {
    public:
        // Xオブジェクトの生成と、ptrからptr_へ所有権の移動
        explicit X(std::unique_ptr<A>&& ptr) : ptr_{std::move(ptr)} {}

        // ptrからptr_へ所有権の移動
        void MoveFrom(std::unique_ptr<A>&& ptr) noexcept { ptr_ = std::move(ptr); }

        // ptr_から外部への所有権の移動
        std::unique_ptr<A> Release() noexcept { return std::move(ptr_); }

        A const* GetA() const noexcept { return ptr_ ? ptr_.get() : nullptr; }

    private:
        std::unique_ptr<A> ptr_{};
    };
```

下記に示した上記クラスの単体テストにより、
オブジェクトの所有権やその移動、
std::unique_ptr、std::move()、[rvalue](core_lang_spec.md#SS_6_7_1_2)の関係を解説する。

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 48

    // ステップ0
    // まだ、クラスAオブジェクトは生成されていないため、
    // A::LastConstructedNum()、A::LastDestructedNum()は初期値である-1である。
    ASSERT_EQ(-1, A::LastConstructedNum());     // まだ、A::A()は呼ばれてない
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 57

    // ステップ1
    // a0、a1がそれぞれ初期化される。
    auto a0 = std::make_unique<A>(0);           // a0はA{0}を所有
    auto a1 = std::make_unique<A>(1);           // a1はA{1}を所有

    ASSERT_EQ(1,  A::LastConstructedNum());     // A{1}は生成された
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

```essential/plant_uml/unique_ownership_1.pu
@startditaa
    ステップ1
    +------------------+ +------------------+
    |std꞉꞉unique_ptr＜A＞| |std꞉꞉unique_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             V                    v
             +------+             +------+
             | A{0} |             | A{1} |
             | cBLU |             | cGRE |
             +------+             +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|cPNK  1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |     -1|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 67

    // ステップ2
    // xが生成され、オブジェクトA{0}の所有がa0からxへ移動する。
    ASSERT_EQ(0, a0->GetNum());                 // a0はA{0}を所有
    auto x = X{std::move(a0)};                  // xの生成と、a0からxへA{0}の所有権の移動
    ASSERT_FALSE(a0);                           // a0は何も所有していない
```

```essential/plant_uml/unique_ownership_2.pu
@startditaa
    ステップ2
    +------------------+ +------------------+
    |std꞉꞉unique_ptr＜A＞| |std꞉꞉unique_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             V                    v
             nullptr              +------+
             |                    | A{1} |
             |                    | cGRE |
             :                    +------+
    +-----+  |
    |  x  |  |
    +--+--+  | x ＝ X{a0}
       |     |
       V     v
       +------+
       | A{0} |
       | cBLU |
       +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |     -1|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 75

    // ステップ3
    // オブジェクトA{1}の所有がa1からxへ移動する。
    // xは以前保持していたA{0}オブジェクトへのポインタをdeleteするため
    // (std::unique_ptrによる自動delete)、A::LastDestructedNum()の値が0になる。
    ASSERT_EQ(1, a1->GetNum());                 // a1はA{1}を所有
    x.MoveFrom(std::move(a1));                  // xによるA{0}の解放
                                                // a1からxへA{1}の所有権の移動
                                                // MoveFromの処理は ptr_ = std::move(a1)
    ASSERT_EQ(0, A::LastDestructedNum());       // A{0}は解放された
    ASSERT_FALSE(a1);                           // a1は何も所有していない
    ASSERT_EQ(1, x.GetA()->GetNum());           // xはA{1}を所有
```
```essential/plant_uml/unique_ownership_3.pu
@startditaa
    ステップ3
    +------------------+ +------------------+
    |std꞉꞉unique_ptr＜A＞| |std꞉꞉unique_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             V                    v
             nllptr               nullptr
    +-----+                             :
    |  x  |                             |
    +--+--+                             | x.Move(a1)
       |                                |
       +------------------+             |
                          |             v
       +-=----+           +-----> +------+
       | A{0} | delete            | A{1} |
       | cGRE |                   | cGRE |
       +------+                   +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |cPNK  0|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 89

    // ステップ4
    // x.ptr_はstd::unique_ptr<A>であるため、ステップ3の状態では、
    // x.ptr_はA{1}オブジェクトのポインタを保持しているが、
    // x.Release()はそれをrvalueに変換し戻り値にする。
    // その戻り値をa2で受け取るため、A{1}の所有はxからa2に移動する。
    std::unique_ptr<A> a2{x.Release()};         // xからa2へA{1}の所有権の移動
    ASSERT_EQ(nullptr, x.GetA());               // xは何も所有していない
    ASSERT_EQ(1, a2->GetNum());                 // a2はA{1}を所有
```

```essential/plant_uml/unique_ownership_4.pu
@startditaa
    ステップ4
    +-----+
    |  x  |
    +--+--+
       |
       +------------------------> nullptr
                                  |
    +------------------+          :
    |std꞉꞉unique_ptr＜A＞|          |
    |        a2        |          |
    +--------+---------+          |
             |                    |
             V                    |
             +------+             | x.Release()
             | A{1} | <-----------+ return rvalue
             | cGRE |
             +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |      0|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 100

    // ステップ5
    // a2をstd::move()によりrvalueに変換し、ブロック内のa3に渡すことで、
    // A{1}の所有はa2からa3に移動する。
    {
        std::unique_ptr<A> a3{std::move(a2)};
        ASSERT_FALSE(a2);                       // a2は何も所有していない
        ASSERT_EQ(1, a3->GetNum());             // a3はA{1}を所有
```

```essential/plant_uml/unique_ownership_5.pu
@startditaa
    ステップ5
    +------------------+ +------------------+
    |std꞉꞉unique_ptr＜A＞| |std꞉꞉unique_ptr＜A＞|
    |        a2        | |        a3        |
    +--------+---------+ +--------+---------+
             |                    |
             V                    v
             nullptr              +------+
               -=---------------> | A{1} |
                 std꞉꞉move(a2)    | cGRE |
                 return rvalue    +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |      0|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 110

        // ステップ6
        // このブロックが終了することで、std::unique_ptrであるa3のデストラクタが呼び出される。
        // これはA{1}オブジェクトへのポインタをdeleteする。
    }                                      // a3によるA{1}の解放
    ASSERT_EQ(1, A::LastDestructedNum());  // A{1}が解放されたことの確認
```

```essential/plant_uml/unique_ownership_6.pu
@startditaa
    ステップ6
    +------------------+ +-=----------------+
    |std꞉꞉unique_ptr＜A＞| |std꞉꞉unique_ptr＜A＞|
    |        a2        | |        a3        |
    +--------+---------+ +--------+---------+
             |                    |
             V                    v
             nullptr              nullptr
                                  +-=----+
                                  | A{1} | delete
                                  | cGRE |
                                  +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |cPNK  1|
      +-----------------------+-------+
@endditaa
```


また、以下に見るようにstd::unique_ptrはcopy生成やcopy代入を許可しない。

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 124

    auto a0 = std::make_unique<A>(0);

    // auto a1 = a0;                            // 下記のようなメッセージでコンパイルエラー
    //      unique_ptr_ownership_ut.cpp:125:15: error: use of deleted function ‘std::unique_ptr ...

    auto a1 = std::move(a0);                    // すでに示したようにmove生成は可能
    
    auto a2 = std::unique_ptr<A>{};

    // a2 = a1;                                 // 下記のようなメッセージでコンパイルエラー
    //      unique_ptr_ownership_ut.cpp:131:10: error: use of deleted function ‘std::unique_ptr ...

    a2 = std::move(a1);                         // すでに示したようにmove代入は可能

    //
    auto x0 = X{std::make_unique<A>(0)};

    // auto x1 = x0;                            // Xはstd::unique_ptrをメンバとするため、
                                                // デフォルトのcopyコンストラクタによる生成は
                                                // コンパイルエラー
    auto x1 = std::move(x0);                    // デフォルトのmove生成は可能

    auto x2 = X{std::make_unique<A>(0)};

    // x2 = x1;                                 // Xはstd::unique_ptrをメンバとするため、
                                                // デフォルトのcopy代入子の呼び出しは
                                                // コンパイルエラー
    x2 = std::move(x1);                         // デフォルトのmove代入は可能
```

以上で示したstd::unique_ptrの仕様の要点をまとめると、以下のようになる。

* std::unique_ptrはダイナミックに生成されたオブジェクトを保持する。
* ダイナミックに生成されたオブジェクトを保持するstd::unique_ptrがスコープアウトすると、
  保持中のオブジェクトは自動的にdeleteされる。
* 保持中のオブジェクトを他のstd::unique_ptrにmoveすることはできるが、
  copyすることはできない。このため、下記に示すような不正な方法以外で、
  複数のstd::unique_ptrが1つのオブジェクトを共有することはできない。

```cpp
    //  example/cpp_idioms/unique_ptr_ownership_ut.cpp 162

    // 以下のようなコードを書いてはならない

    auto a0 = std::make_unique<A>(0);
    auto a1 = std::unique_ptr<A>{a0.get()};  // a1もa0が保持するオブジェクトを保持するが、
                                             // 保持されたオブジェクトは二重解放される

    auto a_ptr = new A{0};

    auto a2 = std::unique_ptr<A>{a_ptr};
    auto a3 = std::unique_ptr<A>{a_ptr};  // a3もa2が保持するオブジェクトを保持するが、
                                          // 保持されたオブジェクトは二重解放される
```

こういった機能によりstd::unique_ptrはオブジェクトの排他所有を実現している。

### オブジェクトの共有所有 <a id="SS_8_2_2"></a>
オブジェクトの共有所有や、それを容易に実現するための
[std::shared_ptr](https://cpprefjp.github.io/reference/memory/shared_ptr.html)
の仕様を説明するために、下記のようにクラスA、Xを定義する。

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 7

    class A final {
    public:
        explicit A(int32_t n) noexcept : num_{n} { last_constructed_num_ = num_; }
        ~A() { last_destructed_num_ = num_; }

        int32_t GetNum() const noexcept { return num_; }

        static int32_t LastConstructedNum() noexcept { return last_constructed_num_; }
        static int32_t LastDestructedNum() noexcept { return last_destructed_num_; }

    private:
        int32_t const  num_;
        static int32_t last_constructed_num_;
        static int32_t last_destructed_num_;
    };

    int32_t A::last_constructed_num_ = -1;
    int32_t A::last_destructed_num_  = -1;

    class X final {
    public:
        // Xオブジェクトの生成と、ptrからptr_へ所有権の移動もしくは共有
        explicit X(std::shared_ptr<A> ptr) : ptr_{std::move(ptr)} {}

        // ptrからptr_へ所有権の移動
        void Move(std::shared_ptr<A>&& ptr) noexcept { ptr_ = std::move(ptr); }

        int32_t UseCount() const noexcept { return ptr_.use_count(); }

        A const* GetA() const noexcept { return ptr_ ? ptr_.get() : nullptr; }

    private:
        std::shared_ptr<A> ptr_{};
    };
```

下記に示した上記クラスの単体テストにより、
オブジェクトの所有権やその移動、共有、
std::shared_ptr、std::move()、[rvalue](core_lang_spec.md#SS_6_7_1_2)の関係を解説する。

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 47

    // ステップ0
    // まだ、クラスAオブジェクトは生成されていないため、
    // A::LastConstructedNum()、A::LastDestructedNum()は初期値である-1である。
    ASSERT_EQ(-1, A::LastConstructedNum());     // まだ、A::A()は呼ばれてない
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 56

    // ステップ1
    // a0、a1がそれぞれ初期化される。
    auto a0 = std::make_shared<A>(0);           // a0はA{0}を所有
    auto a1 = std::make_shared<A>(1);           // a1はA{1}を所有
    ASSERT_EQ(1, a0.use_count());               // A{0}の共有所有カウント数は1
    ASSERT_EQ(1, a1.use_count());               // A{1}の共有所有カウント数は1

    ASSERT_EQ(1,  A::LastConstructedNum());     // A{1}は生成された
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

```essential/plant_uml/shared_ownership_1.pu
@startditaa
    ステップ1
    +------------------+ +------------------+
    |std꞉꞉shared_ptr＜A＞| |std꞉꞉shared_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             V                    v
             +------+             +------+
             | A{0} |             | A{1} |
             | cBLU |             | cGRE |
             +------+             +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|cPNK  1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |     -1|
      +-----------------------+-------+
@endditaa
```


```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 68

    // ステップ2
    // x0が生成され、オブジェクトA{0}がa0とx0に共同所有される。
    ASSERT_EQ(0, a0->GetNum());                 // a0はA{0}を所有
    ASSERT_EQ(1, a0.use_count());               // A{0}の共有所有カウントは1
    auto x0 = X{a0};                            // x0の生成と、a0とx0によるA{0}の共有所有
    ASSERT_EQ(2, a0.use_count());               // A{0}の共有所有カウント数は2
    ASSERT_EQ(2, x0.UseCount());
    ASSERT_EQ(x0.GetA(), a0.get());
```

```essential/plant_uml/shared_ownership_2.pu
@startditaa
    ステップ2
    +------------------+ +------------------+
    |std꞉꞉shared_ptr＜A＞| |std꞉꞉shared_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             |                    v
             |                    +------+
             |                    | A{1} |
             |                    | cGRE |
             |                    +------+
    +------+ |
    |  x0  | | x0 ＝ X{a0}
    +--+---+ |
       |     |
       V     v
       +------+
       | A{0} |
       | cBLU |
       +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |     -1|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 79

    // ステップ３
    // x1が生成され、オブジェクトA{0}の所有がa0からx1へ移動する。
    auto x1 = X{std::move(a0)};                 // x1の生成と、a0からx1へA{0}の所有権の移動
    ASSERT_EQ(x1.GetA(), x1.GetA());            // x0、x1がA{0}を共有所有
    ASSERT_EQ(2, x0.UseCount());                // A{0}の共有所有カウント数は2
    ASSERT_EQ(2, x1.UseCount());
    ASSERT_FALSE(a0);                           // a0は何も所有していない
```

```essential/plant_uml/shared_ownership_3.pu
@startditaa
    ステップ3
    +------------------+ +------------------+
    |std꞉꞉shared_ptr＜A＞| |std꞉꞉shared_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             v                    v
             nullptr              +------+
             |                    | A{1} |
             :                    | cGRE |
             |                    +------+
             |
             | x1 ＝ X{std꞉꞉move(a0)}
    +------+ |           +------+   
    |  x0  | |           |  x1  |   
    +--+---+ |           +--+---+   
       |     |              |
       V     v              |
       +------+<------------+
       | A{0} |
       | cBLU |
       +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |     -1|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 89

    // ステップ４
    // オブジェクトA{1}の所有がa1からx1へ移動する。
    // この時、x1::ptr_は下記のような手順で以前保持していたA{0}オブジェクトへの所有を放棄する。
    //  1. x1::ptr_の共有所有カウント(ptr_.use_count()の戻り値)をデクリメント
    //  2. 共有所有カウントが0ならば、ptr_で保持しているオブジェクト(この場合、A{0})をdelete
    //  3. x1::ptr_の管理対象をに新規オブジェクト(この場合、A{1})に変更
    //
    // ここでは、x0::ptr_がA{0}を所有しているため、共有所有カウントは1であり、
    // 従って、A{0}はdeleteされず、A::LastDestructedNum()の値は-1のまま。
    ASSERT_EQ(1, a1->GetNum());                 // a1はA{1}を所有
    ASSERT_EQ(0, x1.GetA()->GetNum());          // x1はA{0}を所有
    ASSERT_EQ(2, x1.UseCount());                // A{0}の共有所有カウント数は２
    x1.Move(std::move(a1));                     // x1はA{0}の代わりに、A{1}を所有
                                                // a1からx1へA{1}の所有権の移動
    ASSERT_EQ(-1, A::LastDestructedNum());      // x0がA{0}を所有するため、A{0}は未解放
    ASSERT_FALSE(a1);                           // a1は何も所有していない
    ASSERT_EQ(1, x1.GetA()->GetNum());          // x1はA{1}を所有
    ASSERT_EQ(1, x1.UseCount());                // A{1}の共有所有カウント数は1
```

```essential/plant_uml/shared_ownership_4.pu
@startditaa
    ステップ4
    +------------------+ +------------------+
    |std꞉꞉shared_ptr＜A＞| |std꞉꞉shared_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             v                    v
             nullptr              nullptr 
                                  |            
                                  :
                                  | x1.Move(a1)
    +------+             +------+ | 
    |  x0  |             |  x1  | | 
    +--+---+             +--+---+ | 
       |                    |     |
       V                    V     v
       +------+             +------+ 
       | A{0} |             | A{1} |
       | cBLU |             | cGRE |
       +------+             +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |     -1|
      +-----------------------+-------+
@endditaa
```

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 110

    // ステップ５
    // 現時点でx1はA{1}オブジェクトを保持している。
    // x1::Moveに空のstd::shared_ptrを渡すことにより、A{1}を解放する。
    x1.Move(std::shared_ptr<A>{});              // x1に空のstd::shared_ptr<A>を代入することで、
                                                // A{1}を解放
    ASSERT_EQ(nullptr, x1.GetA());              // x1は何も保持していない
    ASSERT_EQ(1, A::LastDestructedNum());       // A{1}が解放された
```

```essential/plant_uml/shared_ownership_5.pu
@startditaa
    ステップ5
    +------------------+ +------------------+
    |std꞉꞉shared_ptr＜A＞| |std꞉꞉shared_ptr＜A＞|
    |        a0        | |        a1        |
    +--------+---------+ +--------+---------+
             |                    |
             v                    v
             nullptr              nullptr 


    +------+             +------+
    |  x0  |             |  x1  |
    +--+---+             +--+---+
       |                    |
       |                    | x1.Move(std꞉꞉shared_ptr＜A＞{})
       |                    |
       |                    V
       V                    nullptr
       +------+             +-=----+  delete
       | A{0} |             | A{1} |
       | cBLU |             | cGRE |
       +------+             +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |cPNK  1|
      +-----------------------+-------+
@endditaa
```


```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 120

    // ステップ６
    // 現時点でx0はA{0}オブジェクトを保持している。
    //
    // ここでは、x0からx2、x3をそれぞれcopy、move生成し、
    // この次のステップ７では、x2、x3がスコープアウトすることでA{0}を解放する。
    {
        ASSERT_EQ(0, x0.GetA()->GetNum());      // x0はA{0}を所有
        ASSERT_EQ(1, x0.UseCount());            // A{0}の共有所有カウント数は1
        auto x2 = x0;                           // x0からx2をcopy生成
        ASSERT_EQ(x0.GetA(), x2.GetA());
        ASSERT_EQ(2, x0.UseCount());            // A{0}の共有所有カウント数は２

        auto x3 = std::move(x0);                // x0からx2をmove生成、x0はA{0}の所有を放棄
        ASSERT_EQ(nullptr, x0.GetA());
        ASSERT_EQ(0, x2.GetA()->GetNum());      // x2はA{0}を保有
        ASSERT_EQ(x2.GetA(), x3.GetA());        // x2、x3はA{0}を共有保有
        ASSERT_EQ(2, x2.UseCount());            // A{1}の共有所有カウント数は２
```

```essential/plant_uml/shared_ownership_6.pu
@startditaa
    ステップ6
    +------+
    |  x0  |
    +--+---+
       |
       V
       nullptr 
             | 
             | 
    x2 ＝ x0  :           x3 ＝ std꞉꞉move(x0)
    +------+ |           +------+
    |  x2  | |           |  x3  |
    +--+---+ |           +--+---+
       |     |              |
       V     V              |
       +------+<------------+
       | A{0} |
       | cBLU |
       +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |      1|
      +-----------------------+-------+
@endditaa
```


```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 142

        // ステップ７
        // このブロックが終了することで、x2、x3はスコープアウトする。
        // デストラクタ呼び出しの順序はコンストラクタ呼び出しの逆になるため、
        // 最初にx3::~X()が呼び出され、この延長でx3::ptr_のデストラクタが呼び出される。
        // これによりA{0}のの共有所有カウントは1になる。
        // 次にx2::~X()が呼び出され、この延長でx2::ptr_のデストラクタが呼び出される。
        // これによりA{0}のの共有所有カウントは0になり、A{0}はdeleteされる。
        // 
    }   // x2、x3のスコープアウト
    ASSERT_EQ(0, A::LastDestructedNum());  // A{0}が解放された
    
```

```essential/plant_uml/shared_ownership_7.pu
@startditaa
    ステップ7
    +------+
    |  x0  |
    +--+---+
       |
       V
       nullptr

    x0からのcopy生成          x0からのmove生成  
    +------+             +------+
    |  x2  |             |  x3  |
    +--+---+             +--+---+
       |                    |
       V                    v
       nullptr              nullptr
       +-=----+
       | A{0} | delete
       |      |
       +------+

    -=-----------------------------------
      +-----------------------+-------+
      |A꞉꞉LastConstructedNum()|      1|
      +-----------------------+-------+
      |A꞉꞉LastDestructedNum() |cPNK  0|
      +-----------------------+-------+
@endditaa
```

以上で示したstd::shared_ptrの仕様の要点をまとめると、以下のようになる。

* std::shared_ptrはダイナミックに生成されたオブジェクトを保持する。
* ダイナミックに生成されたオブジェクトを保持するstd::shared_ptrがスコープアウトすると、
  共有所有カウントはデクリメントされ、その値が0ならば保持しているオブジェクトはdeleteされる。
* std::shared_ptrを他のstd::shared_ptrに、
    * moveすることことで、保持中のオブジェクトの所有権を移動できる。
    * copyすることことで、保持中のオブジェクトの所有権を共有できる。
* 下記のようなコードはstd::shared_ptrの仕様が想定する[セマンティクス](cpp_idioms.md#SS_8_11_1)に沿っておらず、
  [未定義動作](core_lang_spec.md#SS_6_14_3)に繋がる。

```cpp
    //  example/cpp_idioms/shared_ptr_ownership_ut.cpp 162

    // 以下のようなコードを書いてはならない

    auto a0 = std::make_shared<A>(0);
    auto a1 = std::shared_ptr<A>{a0.get()};  // a1もa0が保持するオブジェクトを保持するが、
                                             // 保持されたオブジェクトは二重解放される

    auto a_ptr = new A{0};

    auto a2 = std::shared_ptr<A>{a_ptr};
    auto a3 = std::shared_ptr<A>{a_ptr};  // a3もa2が保持するオブジェクトを保持するが、
                                          // 保持されたオブジェクトは二重解放される
```

こういった機能によりstd::shared_ptrはオブジェクトの共有所有を実現している。


### オブジェクトの循環所有 <a id="SS_8_2_3"></a>
[std::shared_ptr](https://cpprefjp.github.io/reference/memory/shared_ptr.html)の使い方を誤ると、
以下のコード例が示すようにメモリーリークが発生する。

なお、この節の題名である「オブジェクトの循環所有」という用語は、
この前後の節がダイナミックに確保されたオブジェクトの所有の概念についての解説しているため、
この用語を選択したが、文脈によっては、「オブジェクトの循環参照」といった方がふさわしい場合もある。

---

まずは、**メモリリークが発生しない**`std::shared_ptr`の正しい使用例を示す。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 8

    class Y;
    class X final {
    public:
        explicit X() noexcept { ++constructed_counter; }
        ~X() { --constructed_counter; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<Y> y_{};  // 初期化状態では、y_はオブジェクトの所有しない(use_count()==0)
    };
    uint32_t X::constructed_counter;

    class Y final {
    public:
        explicit Y() noexcept { ++constructed_counter; }
        ~Y() { --constructed_counter; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<X> x_{};  // 初期化状態では、x_はオブジェクトの所有しない(use_count()==0)
    };
    uint32_t Y::constructed_counter;
```

上記のクラスの使用例を示す。下記をステップ1とする。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 39

    {  // ステップ1
        ASSERT_EQ(X::constructed_counter, 0);
        ASSERT_EQ(Y::constructed_counter, 0);

        auto x0 = std::make_shared<X>();
        auto y0 = std::make_shared<Y>();

        ASSERT_EQ(x0.use_count(), 1);

        ASSERT_EQ(y0.use_count(), 1);

        ASSERT_EQ(X::constructed_counter, 1);
        ASSERT_EQ(Y::constructed_counter, 1);
```

```essential/plant_uml/shared_each_1.pu
@startditaa
    ステップ1
    +-----+
    |  x0 | use_count꞉1（参照しているXオブジェクトの数）
    +--+--+
       |
       V
       +-------+
       |Xオブジェクト|
       |cGRE   |
       +-------+

    +-----+
    |  y0 | use_count꞉1（参照しているYオブジェクトの数）
    +--+--+
       |
       V
       +-------+
       |Yオブジェクト|
       |cBLU   |
       +-------+

@endditaa

```


上記の続きを以下に示し、ステップ2とする。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 55
        // ステップ2

        auto x1 = x0;  // x0が保有するオブジェクトをx1にも所有させる
        auto y1 = y0;  // y0が保有するオブジェクトをy1にも所有させる

        ASSERT_EQ(X::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない
        ASSERT_EQ(Y::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない

        ASSERT_EQ(x1.use_count(), 2);  // コピーしたため、参照カウントが増えた
        ASSERT_EQ(y1.use_count(), 2);  // コピーしたため、参照カウントが増えた
```

```essential/plant_uml/shared_each_2.pu
@startditaa
    ステップ2
    +------+   +------+
    |  x0  |   |  x1  | use_count꞉2（参照しているXオブジェクトの数）
    +--+---+   +--+---+ 
       |          |
       +----------+
       | 
       V 
       +-------+
       |Xオブジェクト|
       |cGRE   |
       +-------+

    +------+   +------+
    |  y0  |   |  y1  | use_count꞉2（参照しているYオブジェクトの数）
    +--+---+   +--+---+ 
       |          |
       +----------+
       | 
       V 
       +-------+
       |Yオブジェクト|
       |cBLU   |
       +-------+

@endditaa


```


上記の続きを以下に示し、ステップ3とする。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 67
        // ステップ3

        auto x2 = std::move(x1);  // x1が保持する所有権をx2に移動(この後x1はオブジェクトを所有しない)
        auto y2 = std::move(y1);  // y1が保持する所有権をy2に移動(この後y1はオブジェクトを所有しない)

        ASSERT_EQ(x1.use_count(), 0);  // ムーブしたため、参照カウントが0に
        ASSERT_EQ(y1.use_count(), 0);  // ムーブしたため、参照カウントが0に

        ASSERT_EQ(x0.use_count(), 2);  // x0からムーブしていないので参照カウントは不変
        ASSERT_EQ(y0.use_count(), 2);  // y0からムーブしていないので参照カウントは不変
```

```essential/plant_uml/shared_each_3.pu
@startditaa
    ステップ3

    use_count꞉2
    +------+   +------+             +------+  
    |  x0  |   |  x2  |  <-- Move --+  x1  | use_count꞉0
    +--+---+   +--+---+             +--+---+   
       |          |                    |           
       +----------+                    V           
       |                              nullptr
       V                    
       +-------+
       |Xオブジェクト|
       |cGRE   |
       +-------+

    use_count꞉2
    +------+   +------+             +------+        
    |  y0  |   |  y2  |  <-- Move --+  y1  |  use_count꞉0       
    +--+---+   +--+---+             +--+---+         
       |          |                    |            
       +----------+                    V            
       |                              nullptr       
       V 
       +-------+
       |Yオブジェクト|
       |cBLU   |
       +-------+

@endditaa



```


上記の続きを以下に示し、ステップ4とする。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 79

    }  // この次の行で、x0、x2、y0、y2はスコープアウトし、X、Yオブジェクトは解放される

    ASSERT_EQ(X::constructed_counter, 0);  // Xオブジェクトの解放の確認
    ASSERT_EQ(Y::constructed_counter, 0);  // Yオブジェクトの解放の確認
```

```essential/plant_uml/shared_each_4.pu
@startditaa
    ステップ4
    +-=----+   +-=----+
    |  x0  |   |  x2  | use_count꞉0（参照しているXオブジェクトの数）
    +--+---+   +--+---+ 
       |          |
       V          V
     nullptr    nullptr

    +-=----+   +-=----+
    |  y0  |   |  y2  | use_count꞉0（参照しているYオブジェクトの数）
    +--+---+   +--+---+ 
       |          |
       V          V
     nullptr    nullptr


@endditaa



```


このような動作により、`std::make_shared<>`で生成されたX、Yオブジェクトは解放される。

---

次は**メモリリークが発生する**`std::shared_ptr`の誤用を示す。まずはクラスの定義から。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 91

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

        std::shared_ptr<X> const& ref_x() const noexcept { return x_; }

        // 自身の状態を返す ("Y alone" または "Y with X")
        std::string WhoYouAre() const;

        // x_が保持するオブジェクトの状態を返す ("None" またはY::WhoYouAre()に委譲)
        std::string WhoIsWith() const;

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<X> x_{};  // 初期化状態では、x_はオブジェクトを所有しない(use_count()==0)
    };

    // Xのメンバ定義
    std::string X::WhoYouAre() const { return y_ ? "X with Y" : "X alone"; }
    std::string X::WhoIsWith() const { return y_ ? y_->WhoYouAre() : std::string{"None"}; }
    uint32_t    X::constructed_counter;

    // Yのメンバ定義
    std::string Y::WhoYouAre() const { return x_ ? "Y with X" : "Y alone"; }
    std::string Y::WhoIsWith() const { return x_ ? x_->WhoYouAre() : std::string{"None"}; }
    uint32_t    Y::constructed_counter;
```

上記のクラスの動作を以下に示したコードで示す。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 151

    {
        ASSERT_EQ(X::constructed_counter, 0);
        ASSERT_EQ(Y::constructed_counter, 0);

        auto x0 = std::make_shared<X>();       // Xオブジェクトを持つshared_ptrの生成
        ASSERT_EQ(X::constructed_counter, 1);  // Xオブジェクトは1つ生成された

        ASSERT_EQ(x0.use_count(), 1);
        ASSERT_EQ(x0->WhoIsWith(), "None");     // x0.y_は何も保持していないので、"None"
        ASSERT_EQ(x0->ref_y().use_count(), 0);  // X::y_は何も持っていない

```

x0のライフタイムに差を作るために新しいスコープを導入し、そのスコープ内で、y0を生成し、
`X::Register`、`Y::Register`を用いて、循環を作ってしまう例(メモリーリークを起こすバグ)を示す。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 165

        {
            auto y0 = std::make_shared<Y>();

            ASSERT_EQ(Y::constructed_counter, 1);   // Yオブジェクトは1つ生成された
            ASSERT_EQ(y0.use_count(), 1);
            ASSERT_EQ(y0->ref_x().use_count(), 0);  // y0.x_は何も持っていない
            ASSERT_EQ(y0->WhoYouAre(), "Y alone");  // y0.x_は何も持っていないので、"Y alone"

            x0->Register(y0);                       // これによりx0.y_はy0と同じYオブジェクトを持つ
            ASSERT_EQ(x0->WhoIsWith(), "Y alone");  // x0が持つYオブジェクトはまだXを持っていない状態

            y0->Register(x0);                       // これによりy0.y_はx0と同じオブジェクトを持つ
            // 上記で生成されたXオブジェクト、Yオブジェクトは、x0->Register(y0), y0->Register(x0)により
            // 相互に参照しあう状態になる
            ASSERT_EQ(X::constructed_counter, 1);   // 新しいオブジェクトが生成されるわけではない
            ASSERT_EQ(Y::constructed_counter, 1);   // 新しいオブジェクトが生成されるわけではない

            ASSERT_EQ(y0->WhoYouAre(), "Y with X"); // y0.x_はXオブジェクトを持っている
            ASSERT_EQ(x0->WhoYouAre(), "X with Y"); // x0.y_はYオブジェクトを持っている

            ASSERT_EQ(y0->WhoIsWith(), "X with Y"); // y0.x_はXオブジェクトを持っている
            ASSERT_EQ(x0->WhoIsWith(), "Y with X"); // x0.y_はYオブジェクトを持っている

            // 現時点で、x0とy0がお互いを持ち合う状態であることが確認できた
```

```essential/plant_uml/shared_cyclic.pu
@startditaa
  
         +------+
         |  x0  |
         +---+--+
             |
             V
   +-------->+-------+
   |         |Xオブジェクト|
   |         |cGRE y_+---+ y_꞉꞉use_count꞉2
   |         +-------+   |
   |                     |
   |     +------+        |
   |  +--+  y0  |        |
   |  |  +------+        |
   |  |                  |
   |  |      +-----------+
   |  |      |
   |  |      V                  
   |  +----->+-------+
   |         |Yオブジェクト|
   +---------+cBLU x_| x_꞉꞉use_count꞉2
             +-------+

@endditaa

```

下記のコードでは、y0がスコープアウトするが、そのタイミングでは、x0はまだ健在であるため、
Yオブジェクトの参照カウントは1になる(x0::y_が存在するため0にならない)。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 192

            ASSERT_EQ(x0.use_count(), 2);           // x0、y0が相互に参照するので参照カウントが2に
            ASSERT_EQ(y0.use_count(), 2);           // x0、y0が相互に参照するので参照カウントが2に
            ASSERT_EQ(y0->ref_x().use_count(), 2);  // y0.x_の参照カウントは2
            ASSERT_EQ(x0->ref_y().use_count(), 2);  // x0.y_の参照カウントは2
        }  //ここでy0がスコープアウトするため、y0にはアクセスできないが、
           //x0を介して、y0が持っていたYオブジェクトにはアクセスできる

        ASSERT_EQ(x0->ref_y().use_count(), 1);  // y0がスコープアウトしたため、Yオブジェクトの参照カウントが減った
        ASSERT_EQ(x0->ref_y()->WhoYouAre(), "Y with X");  // x0.y_はXオブジェクトを持っている
```

```essential/plant_uml/shared_cyclic_2.pu
@startditaa
  
         +------+
         |  x0  |
         +---+--+
             |
             V
   +-------->+-------+
   |         |Xオブジェクト|
   |         |cGRE y_+---+ y_꞉꞉use_count꞉1 y0がスコープアウトしたため
   |         +-------+   |
   |                     |
   |     +-=----+        |
   |  +--+  y0  |        |
   |  |  +------+        |
   |  |                  |
   |  |      +-----------+
   |  |      |
   |  |      V                  
   |  +----->+-------+
   |         |Yオブジェクト|
   +---------+cBLU x_| x_꞉꞉use_count꞉2
             +-------+

@endditaa


```

ここでの状態をまとめると、

- y0がもともと持っていたXオブジェクトは健在(このオブジェクトはx0が持っているものでもあるため、use_countは2のまま)
- x0が宣言されたスコープが残っているため、当然ながらx0は健在
- x0はYオブジェクトを持ったままではあるが、y0がスコープアウトしたため、Yオブジェクトのuse_countは1に減った

  
次のコードでは、x0がスコープアウトし、y0がもともと持っていたXオブジェクトは健在であるため、
Xオブジェクトの参照カウントも1になる。このため、x0、y0がスコープアウトした状態でも、
X、Yオブジェクトの参照カウントは0にならず、従ってこれらのオブジェクトは解放されない
(shared_ptrは参照カウントが1->0に変化するタイミングで保持するオブジェクトを解放する)。

```cpp
    //  example/cpp_idioms/shared_ptr_cycle_ut.cpp 204
    }  // この次の行で、x0はスコープアウトするため、x0にはアクセスできず、すでにy0にもアクセスできない
    // ここではx0、y0がもともと持っていたXオブジェクト、Yオブジェクトへのポインタを完全に失ってしまった状態

    ASSERT_EQ(X::constructed_counter, 1);  // Xオブジェクトは未開放であり、リークが発生
    ASSERT_EQ(Y::constructed_counter, 1);  // Yオブジェクトは未開放であり、リークが発生
```

```essential/plant_uml/shared_cyclic_3.pu
@startditaa
  
         +-=----+
         |  x0  |
         +---+--+
             |
             V
   +-------->+-------+
   |         |Xオブジェクト|
   |         |cGRE y_+---+ y_꞉꞉use_count꞉1 y0がスコープアウトしたため
   |         +-------+   |
   |                     |
   |     +-=----+        |
   |  +--+  y0  |        |
   |  |  +------+        |
   |  |                  |
   |  |      +-----------+
   |  |      |
   |  |      V                  
   |  +----->+-------+
   |         |Yオブジェクト|
   +---------+cBLU x_| x_꞉꞉use_count꞉1 x0がスコープアウトしたため
             +-------+

@endditaa



```

X、Yオブジェクトへの[ハンドル](cpp_idioms.md#SS_8_9_6)を完全に失った状態であり、X、Yオブジェクトを解放する手段はない。

## copy/moveと等価性のセマンティクス <a id="SS_8_3"></a>
### 等価性のセマンティクス <a id="SS_8_3_1"></a>
純粋数学での実数の等号(=)は、任意の実数x、y、zに対して、

| 律   |意味                     |
|------|-------------------------|
|反射律|x = x                    |
|対称律|x = yならばy = x         |
|推移律|x = y且つy = zならばx = z|

を満たしている。x = yが成立する場合、「xはyと等しい」もしくは「xはyと同一」であると言う。

C++における組み込みの==も純粋数学の等号と同じ性質を満たしている。
下記のコードは、その性質を表している。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 13

    auto  a = 0;
    auto& b = a;

    ASSERT_TRUE(a == b);
    ASSERT_TRUE(&a == &b);  // aとbは同一
```

しかし、下記のコード内のa、bは同じ値を持つが、
アドレスが異なるため同一のオブジェクトではないにもかかわらず、組み込みの==の値はtrueとなる。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 23

    auto a = 0;
    auto b = 0;

    ASSERT_TRUE(a == b);
    ASSERT_FALSE(&a == &b);  // aとbは同一ではない
```

このような場合、aとbは等価であるという。同一ならば等価であるが、等価であっても同一とは限らない。

ポインタや配列をオペランドとする場合を除き、C++における組み込みの==は、
数学の等号とは違い、等価を表していると考えられるが、
上記した3つの律を守っている。従ってオーバーロードoperator==も同じ性質を守る必要がある。

組み込みの==やオーバーロード[==演算子](core_lang_spec.md#SS_6_6_3)のこのような性質をここでは「等価性のセマンティクス」と呼ぶ。

クラスAを下記のように定義し、

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 34

    class A {
    public:
        explicit A(int num, char const* name) noexcept : num_{num}, name_{name} {}

        int         GetNum() const noexcept { return num_; }
        char const* GetName() const noexcept { return name_; }

    private:
        int const   num_;
        char const* name_;
    };
```

そのoperator==を下記のように定義した場合、

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 51

    inline bool operator==(A const& lhs, A const& rhs) noexcept
    {
        return std::tuple(lhs.GetNum(), lhs.GetName()) == std::tuple(rhs.GetNum(), rhs.GetName());
    }
```

単体テストは下記のように書けるだろう。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 62

    auto a0 = A{0, "a"};
    auto a1 = A{0, "a"};

    ASSERT_TRUE(a0 == a1);
```

これは、一応パスするが(処理系定義の動作を前提とするため、必ず動作する保証はない)、
下記のようにすると、パスしなくなる。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 72

    char a0_name[] = "a";
    auto a0        = A{0, a0_name};

    char a1_name[] = "a";
    auto a1        = A{0, a1_name};

    ASSERT_TRUE(a0 == a1);  // テストが失敗する
```

一般にポインタの等価性は、その値の同一性ではなく、
そのポインタが指すオブジェクトの等価性で判断されるべきであるが、
先に示したoperator==はその考慮をしていないため、このような結果になった。

次に、これを修正した例を示す。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 91

    inline bool operator==(A const& lhs, A const& rhs) noexcept
    {
        return std::tuple(lhs.GetNum(), std::string_view{lhs.GetName()})
               == std::tuple(rhs.GetNum(), std::string_view{rhs.GetName()});
    }
```

ポインタをメンバに持つクラスのoperator==については、上記したような処理が必要となる。

次に示す例は、基底クラスBaseとそのoperator==である。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 114

    class Base {
    public:
        explicit Base(int b) noexcept : b_{b} {}
        virtual ~Base() = default;
        int GetB() const noexcept { return b_; }

    private:
        int b_;
    };

    inline bool operator==(Base const& lhs, Base const& rhs) noexcept { return lhs.GetB() == rhs.GetB(); }
```

次の単体テストが示す通り、これ自体には問題がないように見える。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 131

    auto b0 = Base{0};
    auto b1 = Base{0};
    auto b2 = Base{1};

    ASSERT_TRUE(b0 == b0);
    ASSERT_TRUE(b0 == b1);
    ASSERT_FALSE(b0 == b2);
```

しかし、Baseから派生したクラスDerivedを

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 143

    class Derived : public Base {
    public:
        explicit Derived(int d) noexcept : Base{0}, d_{d} {}
        int GetD() const noexcept { return d_; }

    private:
        int d_;
    };
```

のように定義すると、下記の単体テストで示す通り、等価性のセマンティクスが破壊される。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 157

    {
        auto b = Base{0};
        auto d = Derived{1};

        ASSERT_TRUE(b == d);  // NG bとdは明らかに等価でない
    }
    {
        auto d0 = Derived{0};
        auto d1 = Derived{1};

        ASSERT_TRUE(d0 == d1);  // NG d0とd1は明らかに等価ではない
    }
```

Derived用のoperator==を

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 174

    bool operator==(Derived const& lhs, Derived const& rhs) noexcept
    {
        return std::tuple(lhs.GetB(), lhs.GetD()) == std::tuple(rhs.GetB(), rhs.GetD());
    }
```

と定義しても、下記に示す通り部分的な効果しかない。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 184

    auto d0 = Derived{0};
    auto d1 = Derived{1};

    ASSERT_FALSE(d0 == d1);  // OK operator==(Derived const&, Derived const&)の効果で正しい判定

    Base& d0_b_ref = d0;

    ASSERT_TRUE(d0_b_ref == d1);  // NG d0_b_refの実態はd0なのでd1と等価でない
```

この問題は、「[RTTI](core_lang_spec.md#SS_6_4_9)」使った下記のようなコードで対処できる。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 200

    class Base {
    public:
        explicit Base(int b) noexcept : b_{b} {}
        virtual ~Base() = default;
        int GetB() const noexcept { return b_; }

    protected:
        virtual bool is_equal(Base const& rhs) const noexcept { return b_ == rhs.b_; }

    private:
        int b_;

        friend inline bool operator==(Base const& lhs, Base const& rhs) noexcept
        {
            if (typeid(lhs) != typeid(rhs)) {
                return false;
            }

            return lhs.is_equal(rhs);
        }
    };

    class Derived : public Base {
    public:
        explicit Derived(int d) : Base{0}, d_{d} {}
        int GetD() const noexcept { return d_; }

    protected:
        virtual bool is_equal(Base const& rhs) const noexcept
        {
            // operator==によりrhsの型はDerivedであるため、下記のキャストは安全
            auto const& rhs_d = static_cast<Derived const&>(rhs);

            return Base::is_equal(rhs) && d_ == rhs_d.d_;
        }

    private:
        int d_;
    };
```

下記に示す通り、このコードは、
[オープン・クローズドの原則(OCP)](solid.md#SS_2_2)にも対応した柔軟な構造を実現している。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 267

    class DerivedDerived : public Derived {
    public:
        explicit DerivedDerived(int dd) noexcept : Derived{0}, dd_{dd} {}
        int GetDD() const noexcept { return dd_; }

    protected:
        virtual bool is_equal(Base const& rhs) const noexcept
        {
            // operator==によりrhsの型はDerivedDerivedであるため、下記のキャストは安全
            auto const& rhs_d = static_cast<DerivedDerived const&>(rhs);

            return Derived::is_equal(rhs) && dd_ == rhs_d.dd_;
        }

    private:
        int dd_;
    };
```

前例では「両辺の型が等しいこと」が「等価であること」の必要条件となるが、
この要件が、すべてのoperator==に求められるわけではない。

次に示すのは、一見すると両辺の型が違うにもかかわらず、
等価性のセマンティクスを満たしている例である。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 317

    auto abc = std::string{"abc"};

    ASSERT_TRUE("abc" == abc);
    ASSERT_TRUE(abc == "abc");
```

これは、文字列リテラルを第1引数に取るstd::stringのコンストラクタが非explicitであることによって、
文字列リテラルからstd::stringへの[暗黙の型変換](core_lang_spec.md#SS_6_6_2_2)が起こるために成立する。

以上で見てきたように、等価性のセマンティクスを守ったoperator==の実装には多くの観点が必要になる。

### copyセマンティクス <a id="SS_8_3_2"></a>
copyセマンティクスとは以下を満たすようなセマンティクスである。

* a = bが行われた後に、aとbが等価である。
* a = bが行われた前後でbの値が変わっていない。

従って、これらのオブジェクトに対して[等価性のセマンティクス](cpp_idioms.md#SS_8_3_1)
を満たすoperator==が定義されている場合、
以下を満たすようなセマンティクスであると言い換えることができる。

* a = bが行われた後に、a == bがtrueになる。
* b == b_preがtrueの時に、a = bが行われた後でもb == b_preがtrueとなる。

下記に示す通り、std::stringはcopyセマンティクスを満たしている。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 331

    auto c_str = "string";
    auto str   = std::string{};

    str = c_str;
    ASSERT_TRUE(c_str == str);      // = 後には == が成立している
    ASSERT_STREQ("string", c_str);  // c_strの値は変わっていない
```

一方で、std::auto_ptrはcopyセマンティクスを満たしていない。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 344

    std::auto_ptr<std::string> str0{new std::string{"string"}};
    std::auto_ptr<std::string> str0_pre{new std::string{"string"}};

    ASSERT_TRUE(*str0 == *str0_pre);  // 前提は成立

    std::auto_ptr<std::string> str1;

    str1 = str0;

    // ASSERT_TRUE(*str0 == *str0_pre);  // これをするとクラッシュする
    ASSERT_TRUE(str0.get() == nullptr);  // str0の値がoperator ==で変わってしまった

    ASSERT_TRUE(*str1 == *str0_pre);  // これは成立

```

この仕様は極めて不自然であり、std::auto_ptrはC++11で非推奨となり、C++17で規格から排除された。

下記の単体テストから明らかな通り、
「[等価性のセマンティクス](cpp_idioms.md#SS_8_3_1)」で示した最後の例も、copyセマンティクスを満たしていない。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 364

    auto b = Base{1};
    auto d = Derived{1};

    b = d;  // スライシングが起こる

    ASSERT_FALSE(b == d);  // copyセマンティクスを満たしていない
```

原因は、copy代入で[スライシング](cpp_idioms.md#SS_8_7_3)が起こるためである。


### moveセマンティクス <a id="SS_8_3_3"></a>
moveセマンティクスとは以下を満たすようなセマンティクスである(operator==が定義されていると前提)。

* パフォーマンス要件  
    move代入の実行コスト <= copy代入の実行コスト(通常はmove代入の方が高速)

* 意味的要件  
    a == b が true の時に、c = std::move(a) を実行すると、  
    * b == c が true になる（値が保存される）
    * a == c は true にならなくても良い（aはmove後に不定状態になり得る）

* リソース管理   
    必須ではないが、aがポインタ等のリソースを保有している場合、
     move代入後にはそのリソースはcに移動していることが一般的である(「[rvalue](core_lang_spec.md#SS_6_7_1_2)」参照)

* エクセプション安全性  
    [no-fail保証](core_lang_spec.md#SS_6_13_1)をする(noexceptと宣言し、エクセプションをthrowしない)

moveセマンティクスは、使用後に破棄されるオブジェクト(主にrvalue)からの代入処理の実行コストを削減するために導入された。

下記のクラスのmove代入の内部処理はcopy代入が行われており、
moveセマンティクスの目的である「パフォーマンスの向上」が達成されない。

そのため、このようなmove代入は避けるべきである。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 379

    class IneffcientMove {
    public:
        IneffcientMove(char const* name) : name_{name} {}
        std::string const& Name() const noexcept { return name_; }

        IneffcientMove& operator=(IneffcientMove&& rhs)  // move代入、noexceptなし(非推奨)
        {
            name_ = rhs.name_;  // NG: rhs.name_をcopy代入している
                                //     std::move(rhs.name_)を使うべき
            return *this;
        }

    private:
        std::string name_;
    };

    bool operator==(IneffcientMove const& lhs, IneffcientMove const& rhs) noexcept { return lhs.Name() == rhs.Name(); }

    TEST(Semantics, move1)
    {
        auto a = IneffcientMove{"a"};
        auto b = IneffcientMove{"a"};

        ASSERT_EQ("a", a.Name());
        ASSERT_TRUE(a == b);

        auto c = IneffcientMove{"c"};
        ASSERT_EQ("c", c.Name());

        c = std::move(a);
        ASSERT_TRUE(b == c);  // 意味的には正しいが、内部でcopyが発生している(非効率)
    }

```

下記のコードのようにメンバの代入もできる限りmove代入を使うことで、
パフォーマンスの良い代入ができる。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 415

    class EfficientMove {
    public:
        EfficientMove(char const* name) : name_{name} {}
        std::string const& Name() const noexcept { return name_; }

        EfficientMove& operator=(EfficientMove&& rhs) noexcept  // move代入、no-fail保証
        {
            name_ = std::move(rhs.name_);  // OK: rhs.name_からname_へのmove代入
                                           //     リソース(文字列バッファ)をmove
            return *this;
        }

    private:
        std::string name_;
    };

    bool operator==(EfficientMove const& lhs, EfficientMove const& rhs) noexcept { return lhs.Name() == rhs.Name(); }

    TEST(Semantics, move2)
    {
        auto a = EfficientMove{"a"};
        auto b = EfficientMove{"a"};

        ASSERT_EQ("a", a.Name());
        ASSERT_TRUE(a == b);

        auto c = EfficientMove{"c"};
        ASSERT_EQ("c", c.Name());

        c = std::move(a);     // これ以降aは使ってはならない（aは不定状態）
        ASSERT_TRUE(b == c);  // moveセマンティクスを正しく守り、かつ効率的
    }

```

### MoveAssignable要件 <a id="SS_8_3_4"></a>
MoveAssignable要件は、C++において型がmove代入をサポートするために満たすべき条件を指す。
move代入はリソースを効率的に転送する操作であり、以下の条件を満たす必要がある。

1. リソースの移動  
   move代入では、リソース(動的メモリ等)が代入元から代入先へ効率的に転送される。

2. 有効だが未定義の状態  
   move代入後、代入元のオブジェクトは有効ではあるが未定義の状態となる。
   未定義の状態とは、破棄や再代入が可能である状態を指し、それ以外の操作は保証されない。

3. 自己代入の安全性  
   同一のオブジェクトをmove代入する場合でも、未定義動作やリソースリークを引き起こしてはならない。

4. 効率性  
   move代入は通常、copy代入よりも効率的であることが求められる。
   これは、リソースの複製を避けることで達成される(「[moveセマンティクス](cpp_idioms.md#SS_8_3_3)」参照)。

5. デフォルト実装  
   move代入演算子が明示的に定義されていない場合でも、
   クラスが一定の条件(例: move不可能なメンバが存在しないこと)を満たしていれば、
   コンパイラがデフォルトの実装(「[特殊メンバ関数](core_lang_spec.md#SS_6_6_1)」参照)を生成する。

### CopyAssignable要件 <a id="SS_8_3_5"></a>
CopyAssignable要件は、C++において型がcopy代入をサポートするために満たすべき条件を指す。

1. 動作が定義されていること  
   代入操作は未定義動作を引き起こしてはならない。自己代入（同じオブジェクトを代入する場合）においても正しく動作し、
   リソースリークを引き起こさないことが求められる。

2. 値の保持  
   代入後、代入先のオブジェクトの値は代入元のオブジェクトの値と一致していなければならない。

3. 正しいセマンティクス  
   copy代入によって代入元のオブジェクトが変更されてはならない(「[copyセマンティクス](cpp_idioms.md#SS_8_3_2)」参照)。
   代入先のオブジェクトが保持していたリソース(例: メモリ)は適切に解放される必要がある。

4. デフォルト実装  
   copy代入演算子が明示的に定義されていない場合でも、
   クラスが一定の条件(例: copy不可能なメンバが存在しないこと)を満たしていれば、
   コンパイラがデフォルトの実装(「[特殊メンバ関数](core_lang_spec.md#SS_6_6_1)」参照)を生成する。

## 関数設計のガイドライン <a id="SS_8_4"></a>
### 関数の引数と戻り値の型 <a id="SS_8_4_1"></a>
関数の引数型および戻り値型に関するガイドラインを以下の表で表す。

<table>
  <tr bgcolor="#cccccc">
    <th style="text-align: center;"> </th>
    <th style="text-align: center;">copy/moveが低コスト</th>
    <th style="text-align: center;">copyが高コスト/moveが低コスト</th>
    <th style="text-align: center;">moveが高コスト</th>
    <th style="text-align: center;">fがヌルを扱う</th>
  </tr>
  <tr>
    <td style="text-align: center;">in</td>
    <td style="text-align: center;"><code>f(X)</code></td>
    <td colspan="2" style="text-align: center;"><code>f(X const&)</code></td>
    <td style="text-align: center;"><code>f(X const\*)</code></td>
  </tr>
  <tr>
    <td style="text-align: center;">in/out</td>
    <td colspan="3" style="text-align: center;"><code>f(X&)</code></td>
    <td style="text-align: center;"><code>f(X\*)</code></td>
  </tr>
  <tr>
    <td style="text-align: center;">out</td>
    <td colspan="2" style="text-align: center;"><code>X f()</code></td>
    <td style="text-align: center;"><code>f(X&)</code></td>
    <td style="text-align: center;"><code>f(X\*)</code></td>
  </tr>
  <tr>
    <td style="text-align: center;">move</td>
    <td colspan="3" style="text-align: center;"><code>f(X&&)</code></td>
    <td style="text-align: center;">-</td>
  </tr>
  <tr>
    <td style="text-align: center;">forward</td>
    <td colspan="3" style="text-align: center;"><code>template&lt;typename T&gt; f(T&&)</code></td>
    <td style="text-align: center;">-</td>
  </tr>
</table>

[注] Xは任意の型  

[注] `templat<typename T> f(T&&)`の`T&&`は[forwardingリファレンス](core_lang_spec.md#SS_6_8_3)である。  

[注] 以下のような引数型は避けるべきである。  

* `X const*`
* `X*`
* `X&`


### サイクロマティック複雑度のクライテリア <a id="SS_8_4_2"></a>
関数構造の適・不適については、[サイクロマティック複雑度](cpp_idioms.md#SS_8_9_8)によって下記テーブルのように定義する。

| サイクロマティック複雑度(CC) | 複雑さの状態                                     |
| :--------------------------: | :----------------------------------------------- |
|            CC <= 10          | 非常に良い構造(適)                               |
|       11 < CC <  30          | やや複雑(概ね適)                                 |
|       31 < CC <  50          | 構造的なリスクあり(場合により不適)               |
|       51 < CC                | テスト不可能、デグレードリスクが非常に高い(不適) |

### 関数の行数のクライテリア <a id="SS_8_4_3"></a>
C++の創始者であるビャーネ・ストラウストラップ氏は、
  [プログラミング言語C++ 第4版](https://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9EC-%E7%AC%AC4%E7%89%88-%E3%83%93%E3%83%A3%E3%83%BC%E3%83%8D%E3%83%BB%E3%82%B9%E3%83%88%E3%83%A9%E3%82%A6%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97-ebook/dp/B01BGEO9MS)
  の中で、下記のように述べている。

```
    約 40 行を関数の上限にすればよい。 
    私自身は、もっと小さい平均 7 行程度を理想としている。 
```

## クラス設計のガイドライン <a id="SS_8_5"></a>
### ゼロの原則(Rule of Zero) <a id="SS_8_5_1"></a>
「ゼロの原則」は、リソース管理を直接クラスで行わず、
リソース管理を専門とするクラス
(例: 標準ライブラリの[RAII(scoped guard)](design_pattern.md#SS_3_10)クラス)に任せる設計ガイドラインを指す。
この法則に従うと、自身で特殊メンバ関数を定義する必要がなくなる。

```cpp
    //  example/cpp_idioms/rule_of_zero_ut.cpp 9

    class RuleZero {
    public:
        RuleZero(std::list<std::string> const& strs, std::string const& s) : strs_{strs}, s_{s} {}
        std::list<std::string> const& GetStrs() const noexcept { return strs_; }
        std::string const&            GetStr() const noexcept { return s_; }

        // 特殊メンバ関数は、メンバの特殊メンバ関数に任せる
    private:
        std::list<std::string> strs_{};
        std::string            s_{};
    };
```
```cpp
    //  example/cpp_idioms/rule_of_zero_ut.cpp 26

    auto z = RuleZero(std::list<std::string>{"1", "2", "3"}, "str");

    auto copied = z;             // コピーは自動生成に任せる(ゼロの原則)
    auto moved  = std::move(z);  // ムーブも自動生成に任せる(ゼロの原則)

    ASSERT_EQ(copied.GetStr(), moved.GetStr());
    ASSERT_EQ(copied.GetStrs(), moved.GetStrs());
```

クラスがリソースを直接管理する場合、メモリリークや二重解放などのリスクを伴う。
上記のように信頼性の高いクラスに特殊メンバ関数の処理を任せることにより、
クラス自体にリソース管理の責任を持たせる必要がなくなる。

### 五の原則(Rule of Five) <a id="SS_8_5_2"></a>
「五の原則」は、
クラスがリソース(例: 動的メモリやファイルハンドルなど)を管理する場合、
デフォルトコンストラクタを除く[特殊メンバ関数](core_lang_spec.md#SS_6_6_1)、
つまり以下の5つの関数をすべて適切に定義する必要があるという設計ガイドラインを指す。

* デストラクタ
* コピーコンストラクタ
* コピー代入演算子
* ムーブコンストラクタ
* ムーブ代入演算子

特殊メンバ関数の挙動を正しく定義しないと、
リソースの不適切な管理(例: メモリリーク、リソースの二重解放)を招く可能性がある。
自動生成されるメンバ関数では、
複雑なリソース管理の要件を満たせないことがある(「[シャローコピー](cpp_idioms.md#SS_8_7_1)」参照)。

なお、「五の原則」は、「六の原則」と呼ばれることもある。
その場合、この原則が対象とする関数は、
[特殊メンバ関数](core_lang_spec.md#SS_6_6_1)のすべてとなる。

このガイドラインに従って、コピーやムーブを実装する場合、

* [等価性のセマンティクス](cpp_idioms.md#SS_8_3_1)
* [copyセマンティクス](cpp_idioms.md#SS_8_3_2)
* [moveセマンティクス](cpp_idioms.md#SS_8_3_3)

に従わなけならない。

### クラス凝集性のクライテリア <a id="SS_8_5_3"></a>
クラス構造の適・不適については、[LCOM](cpp_idioms.md#SS_8_9_9_2)によって下記テーブルのように定義する。

| 凝集性の欠如(LCOM)  |  クラスの状態              |
|:-------------------:|:--------------------------:|
|       `LCOM <= 0.4` | 理想的な状態(適)           |
|`0.4 <  LCOM <  0.6` | 要注意状態(場合により不適) |
|`0.6 <= LCOM`        | 改善必須状態(不適)         |


* `LCOM <= 0.4`  
  クラスが非常に凝集しており、[単一責任の原則(SRP)](solid.md#SS_2_1)を強く遵守している状態であるため、
  通常、デザインの見直しは不要である。

* `0.4 < LCOM < 0.6`  
  クラスの凝集性がやや弱くなり始めている。
  デザイン見直しの必要な時期が迫りつつあると考えるべきだろう。
  このタイミングであればリファクタリングは低コストで完了できるだろう。

* `0.6 <= LCOM`  
  クラス内のメンバ関数間の関連性が低く、凝集性が不十分である。
  メンバ関数が異なる責務にまたがっている可能性が高いため、
  一刻も早くデザインの見直しを行うべきだろう。


## コーディングスタイル <a id="SS_8_6"></a>
### AAAスタイル <a id="SS_8_6_1"></a>
このドキュメントでのAAAとは、単体テストのパターンarrange-act-assertではなく、
almost always autoを指し、
AAAスタイルとは、「可能な場合、型を左辺に明示して変数を宣言する代わりに、autoを使用する」
というコーディングスタイルである。
この用語は、Andrei Alexandrescuによって造られ、Herb Sutterによって広く推奨されている。

特定の型を明示して使用する必要がない場合、下記のように書く。

```cpp
    //  example/cpp_idioms/aaa.cpp 11

    auto i  = 1;
    auto ui = 1U;
    auto d  = 1.0;
    auto s  = "str";
    auto v  = {0, 1, 2};

    for (auto i : v) {
        // 何らかの処理
    }

    auto add = [](auto lhs, auto rhs) {  // -> return_typeのような記述は不要
        return lhs + rhs;                // addの型もautoで良い
    };

    // 上記変数の型の確認
    static_assert(std::is_same_v<decltype(i), int>);
    static_assert(std::is_same_v<decltype(ui), unsigned int>);
    static_assert(std::is_same_v<decltype(d), double>);
    static_assert(std::is_same_v<decltype(s), char const*>);
    static_assert(std::is_same_v<decltype(v), std::initializer_list<int>>);

    char s2[] = "str";  // 配列の宣言には、AAAは使えない
    static_assert(std::is_same_v<decltype(s2), char[4]>);

    int* p0 = nullptr;  // 初期値がnullptrであるポインタの初期化には、AAAは使うべきではない
    auto p1 = static_cast<int*>(nullptr);  // NG
    auto p2 = p0;                          // OK
    auto p3 = nullptr;                     // NG 通常、想定通りにならない
    static_assert(std::is_same_v<decltype(p3), std::nullptr_t>);
```

特定の型を明示して使用する必要がある場合、下記のように書く。

```cpp
    //  example/cpp_idioms/aaa.cpp 51

    auto b  = new char[10]{0};
    auto v  = std::vector<int>{0, 1, 2};
    auto s  = std::string{"str"};
    auto sv = std::string_view{"str"};

    static_assert(std::is_same_v<decltype(b), char*>);
    static_assert(std::is_same_v<decltype(v), std::vector<int>>);
    static_assert(std::is_same_v<decltype(s), std::string>);
    static_assert(std::is_same_v<decltype(sv), std::string_view>);

    // 大量のstd::stringオブジェクトを定義する場合
    using std::literals::string_literals::operator""s;

    auto s_0 = "222"s;  // OK
    // ...
    auto s_N = "222"s;  // OK

    static_assert(std::is_same_v<decltype(s_0), std::string>);
    static_assert(std::is_same_v<decltype(s_N), std::string>);

    // 大量のstd::string_viewオブジェクトを定義する場合
    using std::literals::string_view_literals::operator""sv;

    auto sv_0 = "222"sv;  // OK
    // ...
    auto sv_N = "222"sv;  // OK

    static_assert(std::is_same_v<decltype(sv_0), std::string_view>);
    static_assert(std::is_same_v<decltype(sv_N), std::string_view>);

    std::mutex mtx;  // std::mutexはmove出来ないので、AAAスタイル不可
    auto       lock = std::lock_guard{mtx};

    static_assert(std::is_same_v<decltype(lock), std::lock_guard<std::mutex>>);
```

関数の戻り値を受け取る変数を宣言する場合、下記のように書く。

```cpp
    //  example/cpp_idioms/aaa.cpp 94

    auto v = std::vector<int>{0, 1, 2};

    // AAAを使わない例
    std::vector<int>::size_type t0{v.size()};      // 正確に書くとこうなる
    std::vector<int>::iterator  itr0 = v.begin();  // 正確に書くとこうなる

    std::unique_ptr<int> p0 = std::make_unique<int>(3);

    // 上記をAAAにした例
    auto t1   = v.size();   // size()の戻りは算術型であると推測できる
    auto itr1 = v.begin();  // begin()の戻りはイテレータであると推測できる

    auto p1 = std::make_unique<int>(3);  // make_uniqueの戻りはstd::unique_ptrであると推測できる
```

ただし、関数の戻り値型が容易に推測しがたい下記のような場合、
型を明示しないAAAスタイルは使うべきではない。

```cpp
    //  example/cpp_idioms/aaa.cpp 118

    extern std::map<std::string, int> gen_map();

    // 上記のような複雑な型を戻す関数の場合、AAAを使うと可読性が落ちる
    auto map0 = gen_map();

    for (auto [str, i] : gen_map()) {
        // 何らかの処理
    }

    // 上記のような複雑な型を戻す関数の場合、AAAを使うと可読性が落ちるため、AAAにしない
    std::map<std::string, int> map1 = gen_map();  // 型がコメントとして役に立つ

    for (std::pair<std::string, int> str_i : gen_map()) {
        // 何らかの処理
    }

    // 型を明示したAAAスタイルでも良い
    auto map2 = std::map<std::string, int>{gen_map()};  // 型がコメントとして役に立つ
```

インライン関数や関数テンプレートの宣言は、下記のように書く。

```cpp
    //  example/cpp_idioms/aaa.cpp 145

    template <typename F, typename T>
    auto apply_0(F&& f, T value)
    {
        return f(value);
    }
```

ただし、インライン関数や関数テンプレートが複雑な下記のような場合、
AAAスタイルは出来る限り避けるべきである。

```cpp
    //  example/cpp_idioms/aaa.cpp 153

    template <typename F, typename T>
    auto apply_1(F&& f, T value) -> decltype(f(std::declval<T>()))  // autoを使用しているが、AAAではない
    {
        auto cond  = false;
        auto param = value;

        // 複雑な処理

        if (cond) {
            return f(param);
        }
        else {
            return f(value);
        }
    }
```

このスタイルには下記のような狙いがある。

* コードの安全性の向上  
  autoで宣言された変数は未初期化にすることができないため、未初期化変数によるバグを防げる。
  また、下記のように縮小型変換(下記では、unsignedからsignedの変換)を防ぐこともできる。

```cpp
    //  example/cpp_idioms/aaa.cpp 180

    auto v = std::vector<int>{0, 1, 2};

    int t0 = v.size();  // 縮小型変換されるため、バグが発生する可能性がある
    // int t1{v.size()};   縮小型変換のため、コンパイルエラー
    auto t2 = v.size();  // t2は正確な型
```

* コードの可読性の向上  
  冗長なコードを排除することで、可読性の向上が見込める。

* コードの保守性の向上  
  「変数宣言時での左辺と右辺を同一の型にする」非AAAスタイルは
  [DRYの原則](https://ja.wikipedia.org/wiki/Don%27t_repeat_yourself#:~:text=Don't%20repeat%20yourself%EF%BC%88DRY,%E3%81%A7%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8%E3%82%92%E5%BC%B7%E8%AA%BF%E3%81%99%E3%82%8B%E3%80%82)
  に反するが、この観点において、AAAスタイルはDRYの原則に沿うため、
  コード修正時に型の変更があった場合でも、それに付随したコード修正を最小限に留められる。


AAAスタイルでは、以下のような場合に注意が必要である。

* 関数の戻り値をautoで宣言された変数で受ける場合  
  上記で述べた通り、AAAの過剰な仕様は、可読性を下げてしまう。

* autoで推論された型が直感に反する場合  
  下記のような型推論は、直感に反する場合があるため、autoの使い方に対する習熟が必要である。

```cpp
    //  example/cpp_idioms/aaa.cpp 194

    auto str0 = "str";
    static_assert(std::is_same_v<char const*, decltype(str0)>);  // str0はchar[4]ではない

    // char[]が必要ならば、AAAを使わずに下記のように書く
    char str1[] = "str";
    static_assert(std::is_same_v<char[4], decltype(str1)>);

    // &が必要になるパターン
    class X {
    public:
        explicit X(int32_t a) : a_{a} {}
        int32_t& Get() { return a_; }

    private:
        int32_t a_;
    };

    X x{3};

    auto a0 = x.Get();
    ASSERT_EQ(3, a0);

    a0 = 4;
    ASSERT_EQ(4, a0);
    ASSERT_EQ(3, x.Get());  // a0はリファレンスではないため、このような結果になる

    // X::a_のリファレンスが必要ならば、下記のように書く
    auto& a1 = x.Get();
    a1       = 4;
    ASSERT_EQ(4, a1);
    ASSERT_EQ(4, x.Get());  // a1はリファレンスであるため、このような結果になる

    // constが必要になるパターン
    class Y {
    public:
        std::string&       Name() { return name_; }
        std::string const& Name() const { return name_; }

    private:
        std::string name_{"str"};
    };

    auto const y = Y{};

    auto        name0 = y.Name();  // std::stringがコピーされる
    auto&       name1 = y.Name();  // name1はconstに見えない
    auto const& name2 = y.Name();  // このように書くべき

    static_assert(std::is_same_v<std::string, decltype(name0)>);
    static_assert(std::is_same_v<std::string const&, decltype(name1)>);
    static_assert(std::is_same_v<std::string const&, decltype(name2)>);

    // 範囲for文でのauto const&
    auto const v = std::vector<std::string>{"0", "1", "2"};

    for (auto s : v) {  // sはコピー生成される
        static_assert(std::is_same_v<std::string, decltype(s)>);
    }

    for (auto& s : v) {  // sはconstに見えない
        static_assert(std::is_same_v<std::string const&, decltype(s)>);
    }

    for (auto const& s : v) {  // このように書くべき
        static_assert(std::is_same_v<std::string const&, decltype(s)>);
    }
```
 
### east-const <a id="SS_8_6_2"></a>
east-constとは、`const`修飾子を修飾する型要素の右側(east＝右)に置くコーディングスタイルのこと。
つまり「`const`はどの対象を修飾するか」を明確にするため、被修飾対象の直後に const を書くのが特徴である。

このスタイルは、C言語由来の「`const`を左に置く」スタイル([west-const](cpp_idioms.md#SS_8_6_3))に比べ、
テンプレート展開や型推論の際に一貫性があり、C++コミュニティではしばしば論理的・直感的と評価されている。

```cpp
    //  example/cpp_idioms/east_west_const.cpp 11

    char              str[] = "hehe";  // 配列strに書き込み可能
    char const*       str0  = str;  // str0が指すオブジェクトはconstなので、*str0への書き込み不可
    char* const       str1  = str;  // str1がconstなので、str1への代入不可
    char const* const str2  = str;  // *str2への書き込み不可、str2への代入不可

    auto lamda = [](char const(&str_ref)[5]) {  // str_refは配列へのconstリファレンス
        int ret = 0;

        for (char const& a : str_ref) {  // aはchar constリファレンス
            ret += a;
        }
        return ret;
    };
```

このスタイルは 「east constスタイル」 または 「右側const」と呼ばれ、
typeid のデマングル結果や Itanium C++ ABI でもこの形式が採用されている。

### west-const <a id="SS_8_6_3"></a>
west-constとは、`const`修飾子を型の左側(west＝左)に置くコーディングスタイルのこと。
C言語からの伝統的な表記法であり、多くの標準ライブラリや教科書でも依然としてこの書き方が用いられている。

可読性は慣れに依存するが、`const`の位置が一貫しないケース(`T* const`など)では理解しづらくなることもある。

```cpp
    //  example/cpp_idioms/east_west_const.cpp 34

    char              str[] = "hehe";  // 配列strに書き込み可能
    const char*       str0  = str;  // str0が指すオブジェクトはconstなので、*str0への書き込み不可
    char* const       str1  = str;  // str1がconstなので、str1への代入不可
    const char* const str2  = str;  // *str2への書き込み不可、str2への代入不可

    auto lamda = [](const char(&str_ref)[5]) {  // str_refは配列へのconstリファレンス
        int ret = 0;

        for (const char& a : str_ref) {  // aはchar constリファレンス
            ret += a;
        }
        return ret;
    };
```

このスタイルは「west constスタイル」または「左側const」と呼ばれ、
C言語文化圏での可読性・慣習を重視する場合に採用されることが多い。

## オブジェクトのコピー <a id="SS_8_7"></a>
### シャローコピー <a id="SS_8_7_1"></a>
シャローコピー(浅いコピー)とは、暗黙的、
もしくは=defaultによってコンパイラが生成するようなcopyコンストラクタ、
copy代入演算子が行うコピーであり、[ディープコピー](cpp_idioms.md#SS_8_7_2)と対比的に使われる概念である。

以下のクラスShallowOKには、コンパイラが生成するcopyコンストラクタ、
copy代入演算子と同等なものを定義したが、これは問題のないシャローコピーである
(が、正しく自動生成される関数を実装すると、メンバ変数が増えた際にバグを生み出すことがあるため、
実践的にはこのようなことはすべきではない)。

```cpp
    //  example/cpp_idioms/deep_shallow_copy_ut.cpp 7

    class ShallowOK {
    public:
        explicit ShallowOK(char const* str = "") : str_{std::string{str}} {}
        std::string const& GetString() const noexcept { return str_; }

        // 下記2関数を定義しなければ、以下と同等なcopyコンストラクタ、copy代入演算子が定義される。
        ShallowOK(ShallowOK const& rhs) : str_{rhs.str_} {}

        ShallowOK& operator=(ShallowOK const& rhs)
        {
            str_ = rhs.str_;
            return *this;
        }

    private:
        std::string str_;
    };
```

コンストラクタでポインタのようなリソースを確保し、
デストラクタでそれらを解放するようなクラスの場合、シャローコピーは良く知られた問題を起こす。

下記のShallowNGはその例である。

```cpp
    //  example/cpp_idioms/deep_shallow_copy_ut.cpp 43

    class ShallowNG {
    public:
        explicit ShallowNG(char const* str = "") : str_{new std::string{str}} {}
        ~ShallowNG() { delete str_; }
        std::string const& GetString() const noexcept { return *str_; }

    private:
        std::string* str_;
    };
```

シャローコピーにより、メンバで保持していたポインタ(ポインタが指しているオブジェクトではない)
がコピーされてしまうため、下記のコード内のコメントで示した通り、
メモリリークや2重解放を起こしてしまう。

```cpp
    //  example/cpp_idioms/deep_shallow_copy_ut.cpp 60

    auto const s0 = ShallowNG{"s0"};

    // NG s0.str_とs1.str_は同じメモリを指すため~ShallowNG()に2重解放される。
    auto const s1 = ShallowNG{s0};

    auto s2 = ShallowNG{"s2"};

    // NG s2.str_が元々保持していたメモリは、解放できなくなる。
    s2 = s0;

    // NG s0.str_とs2.str_は同じメモリを指すため、
    //    s0、s2のスコープアウト時に、~ShallowNG()により、2重解放される。
```

### ディープコピー <a id="SS_8_7_2"></a>
ディープコピーとは、[シャローコピー](cpp_idioms.md#SS_8_7_1)が発生させる問題を回避したコピーである。

以下に例を示す。

```cpp
    //  example/cpp_idioms/deep_shallow_copy_ut.cpp 79

    class Deep {
    public:
        explicit Deep(char const* str = "") : str_{new std::string{str}} {}
        ~Deep() { delete str_; }
        std::string const& GetString() const noexcept { return *str_; }

        // copyコンストラクタの実装例
        Deep(Deep const& rhs) : str_{new std::string{*rhs.str_}} {}

        // copy代入演算子の実装例
        Deep& operator=(Deep const& rhs)
        {
            *str_ = *(rhs.str_);
            return *this;
        }

    private:
        std::string* str_;
    };

    class Deep2 {  // std::unique_ptrを使いDeepをリファクタリング
    public:
        explicit Deep2(char const* str = "") : str_{std::make_unique<std::string>(str)} {}
        std::string const& GetString() const { return *str_; }

        // copyコンストラクタの実装例
        Deep2(Deep2 const& rhs) : str_{std::make_unique<std::string>(*rhs.str_)} {}

        // copy代入演算子の実装例
        Deep2& operator=(Deep2 const& rhs)
        {
            *str_ = *(rhs.str_);
            return *this;
        }

    private:
        std::unique_ptr<std::string> str_;
    };
```

上記クラスのDeepは、copyコンストラクタ、copy代入演算子でポインタをコピーするのではなく、
ポインタが指しているオブジェクトを複製することにより、シャローコピーの問題を防ぐ。


### スライシング <a id="SS_8_7_3"></a>
オブジェクトのスライシングとは、

* クラスBaseとその派生クラスDerived
* クラスDerivedのインスタンスd1、d2(解説のために下記例ではd0も定義)
* d2により初期化されたBase&型のd2_ref(クラスBase型のリファレンス)

が宣言されたとした場合、 

```cpp
    d2_ref = d1;    // オブジェクトの代入
```

を実行した時に発生するようなオブジェクトの部分コピーのことである
(この問題はリファレンスをポインタに代えた場合にも起こる)。

以下のクラスと単体テストはこの現象を表している。

```cpp
    //  example/cpp_idioms/slice_ut.cpp 10

    class Base {
    public:
        explicit Base(char const* name) noexcept : name0_{name} {}
        char const* Name0() const noexcept { return name0_; }

        // ...
    private:
        char const* name0_;
    };

    class Derived final : public Base {
    public:
        Derived(char const* name0, char const* name1) noexcept : Base{name0}, name1_{name1} {}
        char const* Name1() const noexcept { return name1_; }

        // ...
    private:
        char const* name1_;
    };
```

```cpp
    //  example/cpp_idioms/slice_ut.cpp 41

    auto const d0     = Derived{"d0", "d0"};
    auto const d1     = Derived{"d1", "d1"};
    auto       d2     = Derived{"d2", "d2"};
    Base&      d2_ref = d2;

    ASSERT_STREQ("d2", d2.Name0());  // OK
    ASSERT_STREQ("d2", d2.Name1());  // OK

    d2 = d0;
    ASSERT_STREQ("d0", d2.Name0());  // OK
    ASSERT_STREQ("d0", d2.Name1());  // OK

    d2_ref = d1;                     // d2_refはBase&型で、d2へのリファレンス
    ASSERT_STREQ("d1", d2.Name0());  // OK
    /*  本来なら↓が成立してほしいが.、、、
    ASSERT_STREQ("d1", d2.Name1()); */
    ASSERT_STREQ("d0", d2.Name1());  // スライシングの影響でDerived::name1_はコピーされない
```

copy代入演算子(=)によりコピーが行われた場合、=の両辺のオブジェクトは等価になるべきだが
(copy代入演算子をオーバーロードした場合も、そうなるように定義すべきである)、
スライシングが起こった場合、そうならないことが問題である(「[等価性のセマンティクス](cpp_idioms.md#SS_8_3_1)」参照)。

下記にこの現象の発生メカニズムについて解説する。

1. 上記クラスBase、Derivedのメモリ上のレイアウトは下記のようになる。

```essential/plant_uml/slicing_class.pu
@startditaa

    +---------------+--------+
    |               | cBLU   |
    | class Base    | name0_ |
    |               |        |
    +---------------+--------+   

    ---

    +---------------+--------+--------+
    |               | cBLU   | cGRE   |
    | class Derived | name0_ | name1_ |
    |               |        |        |
    +---------------+--------+--------+   
 
@endditaa
```

2. 上記インスタンスd0、d1、d2、d2_refのメモリ上のレイアウトは下記のようになる。

```essential/plant_uml/slicing_init.pu
@startditaa
    +---------------+--------+--------+
    |               | cBLU   | cGRE   |
    | instance d0   | name0_ | name1_ |
    |               |  "d0"  |  "d0"  |
    +---------------+--------+--------+
         
    ---

    +---------------+--------+--------+
    |               | cBLU   | cGRE   | 
    | instance d1   | name0_ | name1_ |
    |               |  "d1"  |  "d1"  |
    +---------------+--------+--------+   
         
    ---

    +---------------+--------+--------+
    |               | cBLU   | cGRE   | 
    | instance d2   | name0_ | name1_ |
    |               |  "d2"  |  "d2"  |
    +---------------+--------+--------+   
                    ^
                    |
     d2_ref --------+
@endditaa
```

3. d2 = d0をした場合の状態は下記のようになる。

```essential/plant_uml/slicing_normal.pu
@startditaa
    +---------------+--------+--------+
    |               | cBLU   | cGRE   | 
    | instance d0   | name0_ | name1_ |
    |               |  "d0"  |  "d0"  |
    +---------------+--------+--------+   
                        |        |
    ---                 |        |
                        v        v
    +---------------+--------+--------+
    |               | cBLU   | cGRE   | 
    | instance d2   | name0_ | name1_ |
    |               |  "d0"  |  "d0"  |
    +---------------+--------+--------+ 
                    ^
                    |
     d2_ref --------+
@endditaa
```

4. 上記の状態でd2_ref = d1をした場合の状態は下記のようになる。

```essential/plant_uml/slicing_slicing.pu
@startditaa
    +---------------+--------+--------+
    |               | cBLU   | cGRE   | 
    | instance d1   | name0_ | name1_ |
    |               |  "d1"  |  "d1"  |
    +---------------+--------+--------+   
                        |
    ---                 |
                        v
    +---------------+--------+--------+
    |               | cBLU   | cRED   |
    | instance d2   | name0_ | name1_ |
    |               |  "d1"  |  "d0"  |
    +---------------+--------+--------+
                    ^             ^
                    |             |
     d2_ref --------+             +-=- コピーされないため、"d0"のまま
@endditaa
```

d2.name1\_の値が元のままであるが(これがスライシングである)、その理由は下記の疑似コードが示す通り、
「d2_refの表層型がクラスBaseであるためd1もクラスBase(正確にはBase型へのリファレンス)へ変換された後、
d2_refが指しているオブジェクト(d2)へコピーされた」からである。

```cpp
    d2_ref.Base::operator=(d1);   // Base::operator=(Base const&)が呼び出される
                                  // 関数Base::operator=(Base const&)の中では、
                                  // d1の型はBase型のリファレンスとなる
```

次に示すのは、
「オブジェクトの配列をその基底クラスへのポインタに代入し、
そのポインタを配列のように使用した場合に発生する」スライシングと類似の現象である。

```cpp
    //  example/cpp_idioms/slice_ut.cpp 64

    Derived d_array[]{{"0", "1"}, {"2", "3"}};
    Base*   b_ptr = d_array;  // この代入までは問題ないが、b_ptr[1]でのアクセスで問題が起こる

    ASSERT_STREQ("0", d_array[0].Name0());  // OK
    ASSERT_STREQ("0", b_ptr[0].Name0());    // OK

    ASSERT_STREQ("2", d_array[1].Name0());  // OK
    /* スライシングに類似した問題で、以下のテストは失敗する。
    ASSERT_STREQ("2", b_ptr[1].Name0());    NG */
    // こうすればテストは通るが、、、
    ASSERT_STREQ("1", b_ptr[1].Name0());  // NG
```

```essential/plant_uml/slicing_array.pu
@startditaa

               +----d_array[0]---+----d_array[1]---+
               |                 |                 |
        
    +----------+--------+--------+--------+--------+
    |          | cBLU   | cGRE   | cBLU   | cGRE   |
    | d_array  | name0_ | name1_ | name0_ | name1_ |
    |          |  "0"   |  "1"   |  "2"   |  "3"   |
    +----------+--------+--------+--------+--------+
               ^        ^
               |        |
               &b_ptr[0]|
                        &b_ptr[1]
 
@endditaa
```


## C++注意点 <a id="SS_8_8"></a>
### オーバーライドとオーバーロードの違い <a id="SS_8_8_1"></a>
下記例では、Base::g()がオーバーロードで、Derived::f()がオーバーライドである
(Derived::g()はオーバーロードでもオーバーライドでもない(「[name-hiding](core_lang_spec.md#SS_6_12_9)」参照))。


```cpp
    //  example/cpp_idioms/override_overload_ut.cpp 5

    class Base {
    public:
        virtual ~Base() = default;
        virtual std::string f() { return "Base::f"; }
        std::string         g() { return "Base::g"; }

        // g()のオーバーロード
        std::string g(int) { return "Base::g(int)"; }
    };

    class Derived : public Base {
    public:
        // Base::fのオーバーライド
        virtual std::string f() override { return "Derived::f"; }

        // Base::gのname-hiding
        std::string g() { return "Derived::g"; }
    };
```

下記図の通り、

* BaseのインスタンスはBase用のvtblへのポインタを内部に持ち、
  そのvtblでBase::f()のアドレスを保持する。
* DerivedのインスタンスはDerived用のvtblへのポインタを内部に持ち、
  そのvtblでDerived::f()のアドレスを保持する。
* Base::g()、Base::g(int)、
  Derived::g()のアドレスはBaseやDerivedのインスタンスから辿ることはできない。

```essential/plant_uml/vtbl.pu
@startditaa
                                    +---------------------
                                    : インストラクション領域
                                    |     関数はリンク後に
+---------------+                   |     インストラクション
|class Base     +---->+---------+   |     領域に配置される
+---------------+     |vtbl cPNK|   |                  
                      | for     |   |
                      | Base    +----->+--------------+
                      +---------+   |  |Base꞉꞉f()     |
                                    :  |  ... cGRE {d}|
                                    |  +--------------+
                                    |                  
                                    |  +--------------+
                                    |  |Base꞉꞉g()     |
                                    |  |  ... cBLU {d}|
                                    |  +--------------+
                                    |                  
                                    |  +--------------+
                                    |  |Base꞉꞉g(int)  |
                                    |  |  ... cBLU {d}|
                                    |  +--------------+
                                    |
+---------------+                   |
|class Derived  |                   |                  
|  ꞉public Base +---->+---------+   |                  
+---------------+     |vtbl cPNK|   |                  
                      | for     |   |
                      | Derived +----->+--------------+
                      +---------+   |  |Derived꞉꞉f()  |
                                    :  |  ... cGRE {d}|
                                    |  +--------------+
                                    |                  
                                    |  +--------------+
                                    |  |Derived꞉꞉g()  |
                                    |  |  ... cRED {d}|
                                    |  +--------------+
                                    |
+----+---------------------------=-+
|cGRE| override                    |
+----+---------------------------=-+
|cBLU| overload                    |
+----+---------------------------=-+
|cRED|not override and not overload|
+----+-----------------------------+
                            
@endditaa
```

vtblとは仮想関数テーブルとも呼ばれる、仮想関数ポインタを保持するための上記のようなテーブルである
(「[ポリモーフィックなクラス](core_lang_spec.md#SS_6_4_8)」参照)。

Base::f()、Derived::f()の呼び出し選択は、オブジェクトの表層の型ではなく、実際の型により決定される。
Base::g()、Derived::g()の呼び出し選択は、オブジェクトの表層の型により決定される。

```cpp
    //  example/cpp_idioms/override_overload_ut.cpp 29

    auto  ret   = std::string{};
    auto  b     = Base{};
    auto  d     = Derived{};
    Base& d_ref = d;

    ret = b.f();  // Base::f()呼び出し
    ASSERT_EQ("Base::f", ret);

    ret = d.f();  // Derived::f()呼び出し
    ASSERT_EQ("Derived::f", ret);

    ret = b.g();  // Base::g()呼び出し
    ASSERT_EQ("Base::g", ret);

    ret = d.g();  // Derived::g()呼び出し
    ASSERT_EQ("Derived::g", ret);
    // ret = d.g(int{});   // Derived::gによって、Base::gが隠されるのでコンパイルエラー

    ret = d_ref.f();  // Base::fはDerived::fによってオーバーライドされたので、Derived::f()呼び出し
    ASSERT_EQ("Derived::f", ret);

    ret = d_ref.g();  // d_refの表層型はBaseなので、Base::g()呼び出し
    ASSERT_EQ("Base::g", ret);

    ret = d_ref.g(int{});  // d_refの表層型はBaseなので、Base::g(int)呼び出し
    ASSERT_EQ("Base::g(int)", ret);
```

上記のメンバ関数呼び出し

```cpp
    d_ref.f() 
```

がどのように解釈され、Derived::f()が選択されるかを以下に疑似コードで例示する。

```cpp
    vtbl = d_ref.vtbl             // d_refの実態はDerivedなのでvtblはDerivedのvtbl

    member_func = vtbl->f         // vtbl->fはDerived::f()のアドレス

    (d_ref.*member_func)(&d_ref)  // member_func()の呼び出し
```

このようなメカニズムにより仮想関数呼び出しが行われる。

### danglingリファレンス <a id="SS_8_8_2"></a>
Dangling リファレンスとは、破棄後のオブジェクトを指しているリファレンスを指す。
このようなリファレンスにアクセスすると、[未定義動作](core_lang_spec.md#SS_6_14_3)に繋がるに繋がる。

```cpp
    //  example/cpp_idioms/dangling_ut.cpp 9

    bool X_destructed;
    class X {
    public:
        X() { X_destructed = false; }
        ~X() { X_destructed = true; }
    };

    bool A_destructed;
    class A {
    public:
        A() { A_destructed = false; }
        ~A() { A_destructed = true; }

        X const& GetX() const noexcept { return x_; }

    private:
        X x_;
    };

    //  example/cpp_idioms/dangling_ut.cpp 34

    auto a = A{};

    auto const& x_safe = a.GetX();  // x_safeはダングリングリファレンスではない
    ASSERT_FALSE(A_destructed || X_destructed);

    auto const& x_dangling = A{}.GetX();  // 次の行でxが指すオブジェクトは解放される
    // この行ではxはdangngling リファレンスになる。
    ASSERT_TRUE(A_destructed && X_destructed);

    auto const* x_ptr_dangling = &A{}.GetX();  // 次の行でxが指すオブジェクトは解放される
    // この行ではxはdangngling ポインタになる。
    ASSERT_TRUE(A_destructed && X_destructed);
```

### danglingポインタ <a id="SS_8_8_3"></a>
danglingポインタとは、[danglingリファレンス](cpp_idioms.md#SS_8_8_2)と同じような状態になったポインタを指す。


### Most Vexing Parse <a id="SS_8_8_4"></a>
Most Vexing Parse(最も困惑させる構文解析)とは、C++の文法に関連する問題で、
Scott Meyersが彼の著書"Effective STL"の中でこの現象に名前をつけたことに由来する。

この問題はC++の文法が関数の宣言と変数の定義とを曖昧に扱うことによって生じる。
特にオブジェクトの初期化の文脈で発生し、意図に反して、その行は関数宣言になってしまう。

```cpp
    //  example/cpp_idioms/most_vexing_parse_ut.cpp 6

    class Vexing {
    public:
        Vexing(int) {}
        Vexing() {}
    };

    //  example/cpp_idioms/most_vexing_parse_ut.cpp 21

    Vexing obj1();        // はローカルオブジェクトobj1の定義ではない
    Vexing obj2(Vexing);  // はローカルオブジェクトobj2の定義ではない
    Vexing(obj3);         // はローカルオブジェクトobj3の定義

    ASSERT_EQ("Vexing ()", Nstd::Type2Str<decltype(obj1)>());
    ASSERT_EQ("Vexing (Vexing)", Nstd::Type2Str<decltype(obj2)>());
    ASSERT_EQ("Vexing", Nstd::Type2Str<decltype(obj3)>());
    // 上記単体テストが示すように、
    //   * obj1はVexingを返す関数
    //   * obj2はVexingを引数に取りVexingを返す関数
    //   * obj3はVexing型のオブジェクト
    // となる。
```

[初期化子リストコンストラクタ](core_lang_spec.md#SS_6_6_1_1)の呼び出しでオブジェクトの初期化を行うことで、
このような問題を回避できる。

## ソフトウェア一般 <a id="SS_8_9"></a>
### ヒープ <a id="SS_8_9_1"></a>
ヒープとは、プログラム実行時に動的メモリ割り当てを行うためのメモリ領域である。
malloc、calloc、reallocといった関数を使用して必要なサイズのメモリを確保し、freeで解放する。
スタックとは異なり、プログラマが明示的にメモリ管理を行う必要があり、解放漏れはメモリリークを引き起こす。
ヒープ領域はスタックよりも大きく、動的なサイズのデータ構造や長寿命のオブジェクトに適しているが、
アクセス速度はスタックより遅い。また、断片化（フラグメンテーション）が発生しやすく、
連続的な割り当てと解放により利用可能なメモリが分散する課題がある。適切なヒープ管理は、
C/C++プログラミングにおける重要なスキルの一つである。

### スレッドセーフ <a id="SS_8_9_2"></a>
スレッドセーフとは「複数のスレッドから同時にアクセスされても、
排他制御などの機構([std::mutex](stdlib_and_concepts.md#SS_7_3_2))により共有データの整合性が保たれ、正しく動作する性質」である。

### リエントラント <a id="SS_8_9_3"></a>
リエントラントとは「実行中に同じ関数が再度呼び出されても、グローバル変数や静的変数に依存せず、
ローカル変数のみで動作するため正しく動作する性質」である。

一般に、リエントラントな関数は[スレッドセーフ](cpp_idioms.md#SS_8_9_2)であるが、逆は成り立たない。


### クリティカルセクション <a id="SS_8_9_4"></a>
複数のスレッドから同時にアクセスされると競合状態を引き起こす可能性があるコード領域をクリティカルセクションと呼ぶ。
典型的には、共有変数や共有データ構造を読み書きするコード部分がこれに該当する。
クリティカルセクションは、[std::mutex](stdlib_and_concepts.md#SS_7_3_2)等の排他制御機構によって保護し、
一度に一つのスレッドのみが実行できるようにする必要がある。

### スピンロック <a id="SS_8_9_5"></a>
スピンロックとは、
スレッドがロックを取得できるまでCPUを占有したままビジーループで待機する排他制御方式である。
スリープを伴わずカーネルを呼び出さないため、短時間の競合では高速に動作するが、
長時間の待機ではCPUを浪費しやすい。リアルタイム処理や割り込み制御に適する。

C++11では、スピンロックは[std::atomic](stdlib_and_concepts.md#SS_7_3_3)を使用して以下のように定義できる。

```cpp
    //  h/spin_lock.h 3

    #include <atomic>

    class SpinLock {
    public:
        void lock() noexcept
        {
            while (state_.exchange(state::locked, std::memory_order_acquire) == state::locked) {
                ;  // busy wait
            }
        }

        void unlock() noexcept { state_.store(state::unlocked, std::memory_order_release); }

    private:
        enum class state { locked, unlocked };
        std::atomic<state> state_{state::unlocked};
    };
```

以下の単体テスト(「[std::mutex](stdlib_and_concepts.md#SS_7_3_2)」の単体テストを参照)
に示したように[std::scoped_lock](stdlib_and_concepts.md#SS_7_4_3)のテンプレートパラメータとして使用できる。

```cpp
    //  example/cpp_idioms/spin_lock_ut.cpp 11

    struct Conflict {
        void increment()
        {
            std::lock_guard<SpinLock> lock{spin_lock_};  // スピンロックのロックガードオブジェクト生成
            ++count_;
        }

        SpinLock spin_lock_{};
        uint32_t count_ = 0;
    };
```
```cpp
    //  example/cpp_idioms/spin_lock_ut.cpp 27

    Conflict c{};

    constexpr uint32_t inc_per_thread = 5'000'000;
    constexpr uint32_t expected       = 2 * inc_per_thread;
    auto               thread_body    = [&c] {
        for (uint32_t i = 0; i < inc_per_thread; ++i) {
            c.increment();
        }
    };

    std::thread t1{thread_body};
    std::thread t2{thread_body};

    t1.join();  // スレッドの終了待ち
    t2.join();  // スレッドの終了待ち
                // 注意: join()もdetach()も呼ばずにスレッドオブジェクトが
                // デストラクトされると、std::terminateが呼ばれる

    ASSERT_EQ(c.count_, expected);
```

### ハンドル <a id="SS_8_9_6"></a>
CやC++の文脈でのハンドルとは、ポインタかリファレンスを指す。

### フリースタンディング環境 <a id="SS_8_9_7"></a>
[フリースタンディング環境](https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AA%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E7%92%B0%E5%A2%83)
とは、組み込みソフトウェアやOSのように、その実行にOSの補助を受けられないソフトウエアを指す。

### サイクロマティック複雑度 <a id="SS_8_9_8"></a>
[サイクロマティック複雑度](https://ja.wikipedia.org/wiki/%E5%BE%AA%E7%92%B0%E7%9A%84%E8%A4%87%E9%9B%91%E5%BA%A6)
とは関数の複雑さを表すメトリクスである。


### 凝集性 <a id="SS_8_9_9"></a>
[凝集性(凝集度)](https://ja.wikipedia.org/wiki/%E5%87%9D%E9%9B%86%E5%BA%A6)
とはクラス設計の妥当性を表す尺度の一種であり、
「[凝集性の欠如](cpp_idioms.md#SS_8_9_9_1)(LCOM)」というメトリクスで計測される。

* [凝集性の欠如](cpp_idioms.md#SS_8_9_9_1)メトリクスの値が1に近ければ凝集性は低く、この値が0に近ければ凝集性は高い。
* メンバ変数やメンバ関数が多くなれば、凝集性は低くなりやすい。
* 凝集性は、クラスのメンバがどれだけ一貫した責任を持つかを示す。
* 「[単一責任の原則(SRP)](solid.md#SS_2_1)」を守ると凝集性は高くなりやすい。
* 「[Accessor](design_pattern.md#SS_3_5)」を多用すれば、振る舞いが分散しがちになるため、通常、凝集性は低くなる。
   従って、下記のようなクラスは凝集性が低い。言い換えれば、凝集性を下げることなく、
   より小さいクラスに分割できる。
   なお、以下のクラスでは、LCOMが位置にに近い値となっており、凝集性が欠如していることがわかる。

```cpp
    //  example/cpp_idioms/lack_of_cohesion_ut.cpp 7

    class ABC {
    public:
        explicit ABC(int32_t a, int32_t b, int32_t c) noexcept : a_{a}, b_{b}, c_{c} {}

        int32_t GetA() const noexcept { return a_; }
        int32_t GetB() const noexcept { return b_; }
        int32_t GetC() const noexcept { return c_; }
        void    SetA(int32_t a) noexcept { a_ = a; }
        void    SetB(int32_t b) noexcept { b_ = b; }
        void    SetC(int32_t c) noexcept { c_ = c; }

    private:
        int32_t a_;
        int32_t b_;
        int32_t c_;
    };
```

良く設計されたクラスは、下記のようにメンバが結合しあっているため凝集性が高い
(ただし、「[Immutable](design_pattern.md#SS_3_7)」の観点からは、QuadraticEquation::Set()がない方が良い)。
言い換えれば、凝集性を落とさずにクラスを分割することは難しい。
なお、上記の凝集性を欠くクラスを凝集性が高くなるように修正した例を以下に示す。

```cpp
    //  example/cpp_idioms/lack_of_cohesion_ut.cpp 26

    class QuadraticEquation {  // 2次方程式
    public:
        explicit QuadraticEquation(int32_t a, int32_t b, int32_t c) noexcept : a_{a}, b_{b}, c_{c} {}

        void Set(int32_t a, int32_t b, int32_t c) noexcept
        {
            a_ = a;
            b_ = b;
            c_ = c;
        }

        int32_t Discriminant() const noexcept  // 判定式
        {
            return b_ * b_ - 4 * a_ * c_;
        }

        bool HasRealNumberSolution() const noexcept { return 0 <= Discriminant(); }

        std::pair<int32_t, int32_t> Solution() const;

    private:
        int32_t a_;
        int32_t b_;
        int32_t c_;
    };

    std::pair<int32_t, int32_t> QuadraticEquation::Solution() const
    {
        if (!HasRealNumberSolution()) {
            throw std::invalid_argument{"solution is an imaginary number"};
        }

        auto a0 = static_cast<int32_t>((-b_ - std::sqrt(Discriminant())) / 2);
        auto a1 = static_cast<int32_t>((-b_ + std::sqrt(Discriminant())) / 2);

        return {a0, a1};
    }
```

#### 凝集性の欠如 <a id="SS_8_9_9_1"></a>
[凝集性](cpp_idioms.md#SS_8_9_9)の欠如(Lack of Cohesion in Methods/LCOM)とは、
クラス設計の妥当性を表す尺度の一種であり、`0 ～ 1`の値で表すメトリクスである。

LCOMの値が大きい(1か1に近い値)場合、「クラス内のメンバ関数が互いに関連性を持たず、
それぞれが独立した責務やデータに依存するため、クラス全体の統一性が欠けている」ことを表す。

クラスデザイン見直しの基準値としてLCOMを活用する場合、[クラス凝集性のクライテリア](cpp_idioms.md#SS_8_5_3)に具体的な推奨値を示す。

#### LCOM <a id="SS_8_9_9_2"></a>
[凝集性の欠如](cpp_idioms.md#SS_8_9_9_1)とはLack of Cohesion in Methodsの和訳であり、LCOMと呼ばれる。

### Spurious Wakeup <a id="SS_8_9_10"></a>
[Spurious Wakeup](https://en.wikipedia.org/wiki/Spurious_wakeup)とは、
条件変数に対する通知待ちの状態であるスレッドが、その通知がされていないにもかかわらず、
起き上がってしまう現象のことを指す。

下記のようなstd::condition_variableの使用で起こり得る。

```cpp
    //  example/cpp_idioms/spurious_wakeup_ut.cpp 8

    namespace {
    std::mutex              mutex;
    std::condition_variable cond_var;
    }  // namespace

    void notify_wrong()  // 通知を行うスレッドが呼び出す関数
    {
        auto lock = std::lock_guard{mutex};

        cond_var.notify_all();  // wait()で待ち状態のスレッドを起こす。
    }

    void wait_wrong()  // 通知待ちスレッドが呼び出す関数
    {
        auto lock = std::unique_lock{mutex};

        // notifyされるのを待つ。
        cond_var.wait(lock);  // notify_allされなくても起き上がってしまうことがある。

        // do something
    }
```

std::condition_variable::wait()の第2引数を下記のようにすることでこの現象を回避できる。

```cpp
    //  example/cpp_idioms/spurious_wakeup_ut.cpp 34

    namespace {
    bool                    event_occured{false};
    std::mutex              mutex;
    std::condition_variable cond_var;
    }  // namespace

    void notify_right()  // 通知を行うスレッドが呼び出す関数
    {
        auto lock = std::lock_guard{mutex};

        event_occured = true;

        cond_var.notify_all();  // wait()で待ち状態のスレッドを起こす。
    }

    void wait_right()  // 通知待ちスレッドが呼び出す関数
    {
        auto lock = std::unique_lock{mutex};

        // notifyされるのを待つ。
        cond_var.wait(lock, []() noexcept { return event_occured; });  // Spurious Wakeup対策

        event_occured = false;

        // do something
    }
```

### Static Initialization Order Fiasco(静的初期化順序問題) <a id="SS_8_9_11"></a>
静的初期化順序問題とは、
グローバルや名前空間スコープの静的オブジェクトの初期化順序が翻訳単位間で未定義であることに起因する不具合である。
あるオブジェクトAが初期化時に別のオブジェクトBに依存していても、Bがまだ初期化されていない場合、
Aの初期化は未定義の状態となり、不正アクセスやクラッシュを引き起こす可能性がある。

原因は、C++標準が同じ翻訳単位内の静的オブジェクトの初期化順序は保証するが、
異なる翻訳単位間の順序は保証しないことにある。さらに、動的初期化を必要とするオブジェクトでは、
初期化順序の依存関係が問題を起こす。

C++20からこの問題の対策として、[constinit](core_lang_spec.md#SS_6_5_8)が導入された。

### 副作用 <a id="SS_8_9_12"></a>
プログラミングにおいて、式の評価による作用には、
主たる作用とそれ以外の
[副作用](https://ja.wikipedia.org/wiki/%E5%89%AF%E4%BD%9C%E7%94%A8_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0))
(side effect)とがある。
式は、評価値を得ること(関数では「引数を受け取り値を返す」と表現する)が主たる作用とされ、
それ以外のコンピュータの論理的状態(ローカル環境以外の状態変数の値)を変化させる作用を副作用という。
副作用の例としては、グローバル変数や静的ローカル変数の変更、
ファイルの読み書き等のI/O実行、等がある。


### Itanium C++ ABI <a id="SS_8_9_13"></a>
ItaniumC++ABIとは、C++コンパイラ間でバイナリ互換性を確保するための規約である。
関数呼び出し規約、クラスレイアウト、仮想関数テーブル、例外処理、
名前修飾(マングリング)などC++のオブジェクト表現と呼び出し方法に関する標準ルールを定めている。

もともとはIntelItanium(IA-64)プロセッサ向けに策定されたが、
[g++](cpp_idioms.md#SS_8_10_1)や[clang++](cpp_idioms.md#SS_8_10_2)はx86/x86-64やARM64など多くのプラットフォームでもItaniumC++ABI準拠の規約を採用している。
そのため異なるコンパイラ間でもオブジェクトファイルやライブラリのリンクが可能である。
また、typeid(...).name()をデマングルした場合、
constがeast-const形式(T const)で表示されるのもこのABIの規約によるものである。

| ABI               | 主な対象プラットフォーム  | マングリング規則    | クラスレイアウト  | 例外処理    |
| ----------------- | ------------------------- | ------------------- | ----------------- | ----------- |
| **ItaniumC++ABI** | IA-64, x86, x86-64, ARM64 | east-const形式      | Itanium規則       | Itanium規則 |
| **MSVC C++ABI**   | Windows x86/x64           | 独自形式            | 独自規則          | 独自規則    |
| **ARM C++ABI**    | AArch32, AArch64          | 基本的にItanium準拠だが例外あり         | ARM規則     |


## C++コンパイラ <a id="SS_8_10"></a>
本ドキュメントで使用するg++/clang++のバージョンは以下のとおりである。

### g++ <a id="SS_8_10_1"></a>
```
    g++ (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
    Copyright (C) 2021 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### clang++ <a id="SS_8_10_2"></a>
```
    Ubuntu clang version 14.0.0-1ubuntu1
    Target: x86_64-pc-linux-gnu
    Thread model: posix
    InstalledDir: /usr/bin
```

## 非ソフトウェア用語 <a id="SS_8_11"></a>
### セマンティクス <a id="SS_8_11_1"></a>
シンタックスとは構文論のことであり、セマンティクスとは意味論のことである。
セマンティクス、シンタックスの違いをはっきりと際立たせる以下の有名な例文により、
セマンティクスの意味を直感的に理解することができる。

```
    Colorless green ideas sleep furiously(直訳:無色の緑の考えが猛烈に眠る)
```

この文は文法的には正しい(シンタックス的に成立している)が、意味的には不自然で理解不能である
(セマンティクス的には破綻している)。ノーム・チョムスキーによって提示されたこの例文は、
構文が正しくても意味が成立しないことがあるという事実を示しており、構文と意味の違いを鮮やかに浮かび上がらせる。


### 割れ窓理論 <a id="SS_8_11_2"></a>
[割れ窓理論](https://ja.wikipedia.org/wiki/%E5%89%B2%E3%82%8C%E7%AA%93%E7%90%86%E8%AB%96)とは、
軽微な犯罪も徹底的に取り締まることで、凶悪犯罪を含めた犯罪を抑止できるとする環境犯罪学上の理論。
アメリカの犯罪学者ジョージ・ケリングが考案した。
「建物の窓が壊れているのを放置すると、誰も注意を払っていないという象徴になり、
やがて他の窓もまもなく全て壊される」との考え方からこの名がある。

ソフトウェア開発での割れ窓とは、「朝会に数分遅刻する」、「プログラミング規約を守らない」
等の軽微なルール違反を指し、この理論の実践には、このような問題を放置しないことによって、

* チームのモラルハザードを防ぐ
* コードの品質を高く保つ

等の重要な狙いがある。


### 車輪の再発明 <a id="SS_8_11_3"></a>
[車輪の再発明](https://ja.wikipedia.org/wiki/%E8%BB%8A%E8%BC%AA%E3%81%AE%E5%86%8D%E7%99%BA%E6%98%8E)
とは、広く受け入れられ確立されている技術や解決法を（知らずに、または意図的に無視して）
再び一から作ること」を指すための慣用句である。
ソフトウェア開発では、STLのような優れたライブラリを使わずに、
それと同様なライブラリを自分たちで実装するような非効率な様を指すことが多い。



