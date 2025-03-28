<!-- ./md/design_pattern.md -->
# デザインパターン <a id="SS_3"></a>
ソースコードを劣化させるアンチパターンには、

* 大きすぎる関数、クラス、ファイル等のソフトウェア構成物
* 複雑怪奇な依存関係
* コードクローン

等があるだろう。
こういった問題は、ひどいソースコードを書かないという強い意志を持ったプログラマの不断の努力と、
そのプログラマを支えるソフトウェア工学に基づいた知識によって回避可能である。
本章ではその知識の一翼をになうデザインパターン、イデオム等を解説、例示する。

なお、ここに挙げるデザインパターン、イデオム等は「適切な場所に適用される場合、
ソースコードをよりシンプルに記述できる」というメリットがある一方で、
「不適切な場所に適用される場合、ソースコードの複雑度を不要に上げてしまう」
という負の一面を持つ。

また、デザインパターン、イデオム等を覚えたてのプログラマは、
自分のスキルが上がったという一種の高揚感や顕示欲を持つため、
それをむやみやたらに多用してしまう状態に陥ることある。このようなプログラマの状態を 

* パターン病に罹患した
* パターン猿になった、もしくは単に、猿になった  

と呼ぶ。
猿になり不要に複雑なソースコードを書かないために、デザインパターン、イデオム等を使用する場合、
本当にそれが必要か吟味し、不要な場所への適用を避けなければならない。

---
__この章の構成__

&emsp;&emsp; [ガード節](design_pattern.md#SS_3_1)  
&emsp;&emsp; [BitmaskType](design_pattern.md#SS_3_2)  
&emsp;&emsp; [Pimpl](design_pattern.md#SS_3_3)  
&emsp;&emsp; [Accessor](design_pattern.md#SS_3_4)  
&emsp;&emsp; [Copy-And-Swap](design_pattern.md#SS_3_5)  
&emsp;&emsp; [Immutable](design_pattern.md#SS_3_6)  
&emsp;&emsp; [Clone(仮想コンストラクタ)](design_pattern.md#SS_3_7)  
&emsp;&emsp; [NVI(non virtual interface)](design_pattern.md#SS_3_8)  
&emsp;&emsp; [RAII(scoped guard)](design_pattern.md#SS_3_9)  
&emsp;&emsp; [Future](design_pattern.md#SS_3_10)  
&emsp;&emsp; [DI(dependency injection)](design_pattern.md#SS_3_11)  
&emsp;&emsp; [Singleton](design_pattern.md#SS_3_12)  
&emsp;&emsp; [State](design_pattern.md#SS_3_13)  
&emsp;&emsp; [Null Object](design_pattern.md#SS_3_14)  
&emsp;&emsp; [Templateメソッド](design_pattern.md#SS_3_15)  
&emsp;&emsp; [Factory](design_pattern.md#SS_3_16)  
&emsp;&emsp; [Named Constructor](design_pattern.md#SS_3_17)  
&emsp;&emsp; [Proxy](design_pattern.md#SS_3_18)  
&emsp;&emsp; [Strategy](design_pattern.md#SS_3_19)  
&emsp;&emsp; [Visitor](design_pattern.md#SS_3_20)  
&emsp;&emsp; [CRTP(curiously recurring template pattern)](design_pattern.md#SS_3_21)  
&emsp;&emsp; [Observer](design_pattern.md#SS_3_22)  
&emsp;&emsp; [MVC](design_pattern.md#SS_3_23)  
&emsp;&emsp; [Cでのクラス表現](design_pattern.md#SS_3_24)  
  
  

## ガード節 <a id="SS_3_1"></a>
ガード節とは、
「可能な場合、処理を早期に打ち切るために関数やループの先頭に配置される短い条件文(通常はif文)」
であり、以下のような利点がある。

* 処理の打ち切り条件が明確になる。
* 関数やループのネストが少なくなる。

まずは、ガード節を使っていない例を上げる。

```cpp
    // @@@ example/design_pattern/guard_ut.cpp 24

    /// @fn int32_t SequentialA(char const (&a)[3])
    /// @brief a(配列へのリファレンス)の要素について、先頭から'a'が続く数を返す
    /// @param 配列へのリファレンス
    int32_t SequentialA(char const (&a)[3]) noexcept
    {
        if (a[0] == 'a') {
            if (a[1] == 'a') {
                if (a[2] == 'a') {
                    return 3;
                }
                else {
                    return 2;
                }
            }
            else {
                return 1;
            }
        }
        else {
            return 0;
        }
    }
```

上記の例を読んで一目で何が行われているか、理解できる人は稀である。
一方で、上記と同じロジックである下記関数を一目で理解できない人も稀である。

```cpp
    // @@@ example/design_pattern/guard_ut.cpp 78

    int32_t SequentialA(char const (&a)[3]) noexcept
    {
        if (a[0] != 'a') {  // ガード節
            return 0;
        }
        if (a[1] != 'a') {  // ガード節
            return 1;
        }
        if (a[2] != 'a') {  // ガード節
            return 2;
        }

        return 3;
    }
```

ここまで効果的な例はあまりない。

もう一例、(ガード節導入の効果が前例ほど明確でない)ガード節を使っていないコードを示す。

```cpp
    // @@@ example/design_pattern/guard_ut.cpp 49

    std::optional<std::vector<uint32_t>> PrimeNumbers(uint32_t max_num)
    {
        auto result = std::vector<uint32_t>{};

        if (max_num < 65536) {  // 演算コストが高いためエラーにする
            if (max_num >= 2) {
                auto is_num_prime = std::vector<bool>(max_num + 1, true);  // falseなら素数でない
                is_num_prime[0] = is_num_prime[1] = false;
                auto prime_num                    = 2U;  // 最初の素数

                do {
                    result.emplace_back(prime_num);
                    prime_num = next_prime_num(prime_num, is_num_prime);
                } while (prime_num < is_num_prime.size());
            }

            return result;
        }

        return std::nullopt;
    }
```

上記にガード節を適用した例を下記する。

```cpp
    // @@@ example/design_pattern/guard_ut.cpp 95

    std::optional<std::vector<uint32_t>> PrimeNumbers(uint32_t max_num)
    {
        if (max_num >= 65536) {  // ガード節。演算コストが高いためエラーにする。
            return std::nullopt;
        }

        auto result = std::vector<uint32_t>{};

        if (max_num < 2) {  // ガード節。2未満の素数はない。
            return result;
        }

        auto is_num_prime = std::vector<bool>(max_num + 1, true);  // falseなら素数でない。
        is_num_prime[0] = is_num_prime[1] = false;
        auto prime_num                    = 2U;  // 最初の素数

        do {
            result.emplace_back(prime_num);
            prime_num = next_prime_num(prime_num, is_num_prime);
        } while (prime_num < is_num_prime.size());

        return result;
    }
```

ガード節を使っていない例に比べて、

* ネストが減って読みやすくなった
* max_numが1, 2, 65535, 65536である場合がロジックの境界値であることが一目でわかるようになった

といった改善はされたものの、最初の例ほどのレベル差はない。
しかし、ソースコードの改善やリファクタリングのほとんどは、このようなものであり、
この少しのレベルアップが数か月後、数年後に大きな差を生み出すことを忘れてはならない。


## BitmaskType <a id="SS_3_2"></a>
下記のようなビットマスク表現は誤用しやすいインターフェースである。
修正や拡張等に関しても脆弱であるため、避けるべきである。

```cpp
    // @@@ example/design_pattern/enum_operator.h 6

    class Animal {
    public:
        struct PhisicalAbility {  // オブジェクトの状態を表すためのビットマスク
            static constexpr auto Run  = 0b0001U;
            static constexpr auto Fly  = 0b0010U;
            static constexpr auto Swim = 0b0100U;
        };

        // paにはPhisicalAbilityのみを受け入れたいが、実際にはすべてのuint32_tを受け入れる。
        explicit Animal(uint32_t pa) noexcept : phisical_ability_{pa} {}

        uint32_t GetPhisicalAbility() const noexcept { return phisical_ability_; }
        ...
    };
```

```cpp
    // @@@ example/design_pattern/enum_operator_ut.cpp 13

    Animal dolphin{Animal::PhisicalAbility::Swim};  // OK
    ASSERT_EQ(Animal::PhisicalAbility::Swim, dolphin.GetPhisicalAbility());

    Animal uma{0xff};  // NG 誤用だが、コンストラクタの仮引数の型がuint32_tなのでコンパイル可能
```

上記のような誤用を防ぐために、
enumによるビットマスク表現を使用して型チェックを強化した例を以下に示す。
このテクニックは、STLのインターフェースとしても使用されている強力なイデオムである。

```cpp
    // @@@ example/design_pattern/enum_operator.h 30

    class Animal {
    public:
        enum class PhisicalAbility : uint32_t {
            Run  = 0b0001,
            Fly  = 0b0010,
            Swim = 0b0100,
        };

        explicit Animal(PhisicalAbility pa) noexcept : phisical_ability_{pa} {}

        PhisicalAbility GetPhisicalAbility() const noexcept { return phisical_ability_; }

    private:
        PhisicalAbility const phisical_ability_;
    };

    // &, | &=, |=, IsTrue, IsFalseの定義
    constexpr Animal::PhisicalAbility operator&(Animal::PhisicalAbility x,
                                                Animal::PhisicalAbility y) noexcept
    {
        return static_cast<Animal::PhisicalAbility>(static_cast<uint32_t>(x)
                                                    & static_cast<uint32_t>(y));
    }

    constexpr Animal::PhisicalAbility operator|(Animal::PhisicalAbility x,
                                                Animal::PhisicalAbility y) noexcept
    {
        return static_cast<Animal::PhisicalAbility>(static_cast<uint32_t>(x)
                                                    | static_cast<uint32_t>(y));
    }

    inline Animal::PhisicalAbility& operator&=(Animal::PhisicalAbility& x,
                                               Animal::PhisicalAbility  y) noexcept
    {
        return x = x & y;
    }

    ...
```

```cpp
    // @@@ example/design_pattern/enum_operator_ut.cpp 28

    // コンストラクタの仮引数の型が厳密になったためコンパイル不可
    // これにより誤用を防ぐ
    // Animal uma{0xff};

    // C++17から下記はコンパイル可能となったが、アクシデントでこのようなミスはしないだろう
    auto uma = Animal{Animal::PhisicalAbility{0xff}};

    auto dolphin = Animal{Animal::PhisicalAbility::Swim};
    ASSERT_EQ(Animal::PhisicalAbility::Swim, dolphin.GetPhisicalAbility());

    auto pa = Animal::PhisicalAbility{Animal::PhisicalAbility::Run};
    pa |= Animal::PhisicalAbility::Swim;

    auto human = Animal{pa};
    ASSERT_TRUE(IsTrue(Animal::PhisicalAbility::Run & human.GetPhisicalAbility()));
```

この改善により、Animalのコンストラクタに域値外の値を渡すことは困難になった
(少なくとも不注意で間違うことはないだろう)。
この修正の延長で、Animal::GetPhisicalAbility()の戻り値もenumになり、これも誤用が難しくなった。


## Pimpl <a id="SS_3_3"></a>
このパターンは、「クラスA(a.cpp、a.hで宣言、定義)を使用するクラスにAの実装の詳細を伝搬させたくない」
ような場合に使用する。
そのため[オープン・クローズドの原則(OCP)](solid.md#SS_2_2)の実装方法としても有用である。

一般的に、STLライブラリのパースは多くのCPUタイムを消費する。
クラスAがSTLクラスをメンバに使用し、a.hにそのSTLヘッダファイルがインクルードされた場合、
a.hをインクルードするファイルをコンパイルする度にそのSTLヘッダファイルはパースされる。
これはさらに多くのCPUタイムの消費につながり、ソースコード全体のビルドは遅くなる。
こういった問題をあらかじめ避けるためにも有効な手段ではあるが、
そのトレードオフとして実行速度は若干遅くなる。

下記は、Pimplイデオム未使用の、std::stringに依存したクラスStringHolderOldの例である。

```cpp
    // @@@ example/design_pattern/string_holder_old.h 3
    // このファイルには<string>が必要

    #include <memory>
    #include <string>

    class StringHolderOld final {
    public:
        StringHolderOld();

        void        Add(char const* str);
        char const* GetStr() const;

    private:
        std::unique_ptr<std::string> str_;
    };
```

```cpp
    // @@@ example/design_pattern/string_holder_old.cpp 1

    #include "string_holder_old.h"

    StringHolderOld::StringHolderOld() : str_{std::make_unique<std::string>()} {}

    void StringHolderOld::Add(char const* str) { *str_ += str; }

    char const* StringHolderOld::GetStr() const { return str_->c_str(); }
```


下記は、上記クラスStringHolderOldにPimplイデオムを適用したクラスStringHolderNewの例である。

```cpp
    // @@@ example/design_pattern/string_holder_new.h 3
    // このファイルには<string>は不要

    #include <memory>

    class StringHolderNew final {
    public:
        StringHolderNew();

        void        Add(char const* str);
        char const* GetStr() const;
        ~StringHolderNew();  // デストラクタは.cppで=defaultで定義

    private:
        class StringHolderNewCore;  // StringHolderNewの振る舞いは、StringHolderNewCoreに移譲
        std::unique_ptr<StringHolderNewCore> core_;
    };
```

```cpp
    // @@@ example/design_pattern/string_holder_new.cpp 1
    // このファイルには<string>が必要

    #include <string>

    #include "string_holder_new.h"

    class StringHolderNew::StringHolderNewCore final {
    public:
        StringHolderNewCore() = default;
        void Add(char const* str) { str_ += str; }

        char const* GetStr() const noexcept { return str_.c_str(); }

    private:
        std::string str_{};
    };

    StringHolderNew::StringHolderNew() : core_{std::make_unique<StringHolderNewCore>()} {}

    void StringHolderNew::Add(char const* str) { core_->Add(str); }

    char const* StringHolderNew::GetStr() const { return core_->GetStr(); }

    // この宣言、定義をしないと、StringHolderNewをインスタンス化した場所では、
    // StringHolderNewCoreが不完全型であるため、std::unique_ptrが実体化できず、コンパイルエラーとなる。
    // この場所であれば、StringHolderNewCoreは完全型であるためstd::unique_ptrが実体化できる。
    StringHolderNew::~StringHolderNew() = default;
```

下記図は、上記ファイルやそれらを使用するファイルの依存関係である。
string_holder_old.hは、std::stringに依存しているが、string_holder_new.hは、
std::stringに依存していないこと、
それによってStringHolderNewを使用するファイルから、std::stringへの依存を排除できていることがわかる。

<!-- pu:plant_uml/pimpl_pattern.pu--><p><img src="data:image/png;base64,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" /></p>

このパターンを使用して問題のある依存関係をリファクタリングする例を示す。

まずは、リファクタリング前のコードを下記する。

```cpp
    // in lib/h/widget.h

    #include "gtest/gtest.h"

    class Widget {
    public:
        void     DoSomething();
        uint32_t GetValue() const;
        // 何らかの宣言

    private:
        uint32_t gen_xxx_data(uint32_t a);
        uint32_t xxx_data_{1};
        FRIEND_TEST(Pimpl, widget_ng);  // 単体テストをfriendにする
    };
```
```cpp
    // in lib/src/widget.cpp

    #include "widget.h"

    void Widget::DoSomething()
    {
        // 何らかの処理
        xxx_data_ = gen_xxx_data(xxx_data_);
    }

    uint32_t Widget::GetValue() const { return xxx_data_; }

    uint32_t WidgetNG::Widget::gen_xxx_data(uint32_t a) { return a * 3; }
```
```cpp
    // in lib/ut/widget_ut.cpp

    #include "widget.h"

    TEST(Pimpl, widget_ng)
    {
        Widget w;

        ASSERT_EQ(1, w.xxx_data_);  // privateのテスト
        w.DoSomething();
        ASSERT_EQ(3, w.xxx_data_);        // privateのテスト
        ASSERT_EQ(9, w.gen_xxx_data(3));  // privateのテスト

        ASSERT_EQ(3, w.GetValue());
    }
```

何らかの事情により、単体テストでprivateなメンバにアクセスする必要があったため、
単体テストクラスをテスト対象クラスのfriendすることで、それを実現している。

単体テストクラスをテスト対象クラスのfriendにするためには、
上記コードの抜粋である下記を記述する必要がある。

```cpp
        FRIEND_TEST(Pimpl, widget_ng);  // 単体テストをfriendにする
```

このマクロは、gtest.h内で定義されているため、widget.hからgtest.hをインクルードしている。

このため、ファイルの依存関係は下記のようになる。

<!-- pu:plant_uml/widget_ng.pu--><p><img src="data:image/png;base64,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" /></p>

この依存関係は、Widgetのクライアントに不要な依存関係を強要してしまう問題のある構造を作り出す。

この問題をPimplによるリファクタリングで解決したコードを以下に示す
(コンパイラのインクルードパスにはlib/hのみが入っていることを前提とする)。

```cpp
    // in lib/h/widget.h

    #include <memory>

    class Widget {
    public:
        Widget();   // widget_pimplは不完全型であるため、コンストラクタ、
        ~Widget();  // デストラクタはインラインにできない
        void     DoSomething();
        uint32_t GetValue() const;
        // 何らかの宣言

        struct widget_pimpl;  // 単体テストのため、publicとするが、実装はsrc/の下に置くため、
                              // 単体テスト以外の外部からのアクセスはできない

    private:
        std::unique_ptr<widget_pimpl> widget_pimpl_;
    };
```
```cpp
    // in lib/src/widget.cpp

    #include "widget_internal.h"

    // widget_pimpl
    void Widget::widget_pimpl::DoSomething()
    {
        // 何らかの処理
        xxx_data_ = gen_xxx_data(xxx_data_);
    }

    uint32_t Widget::widget_pimpl::gen_xxx_data(uint32_t a) { return a * 3; }

    // Widget
    void     Widget::DoSomething() { widget_pimpl_->DoSomething(); }
    uint32_t Widget::GetValue() const { return widget_pimpl_->xxx_data_; }

    // ヘッダファイルの中では、widget_pimplは不完全型であるため、コンストラクタ、
    // デストラクタは下記に定義する
    Widget::Widget() : widget_pimpl_{std::make_unique<Widget::widget_pimpl>()} {}
    Widget::~Widget() = default;
```
```cpp
    // in lib/src/widget_internal.h

    #include "widget.h"

    struct Widget::widget_pimpl {
        void     DoSomething();
        uint32_t gen_xxx_data(uint32_t a);
        uint32_t xxx_data_{1};
    };
```
```cpp
    // in lib/ut/widget_ut.cpp

    #include "../src/widget_internal.h"  // 単体テストのみに、このようなインクルードを認める
    #include "gtest/gtest.h"

    TEST(Pimpl, widget_ok)
    {
        Widget::widget_pimpl wi;

        ASSERT_EQ(1, wi.xxx_data_);
        wi.DoSomething();
        ASSERT_EQ(3, wi.xxx_data_);
        ASSERT_EQ(9, wi.gen_xxx_data(3));

        Widget w;

        w.DoSomething();
        ASSERT_EQ(3, w.GetValue());
    }
```

このリファクタリングにより、ファイルの依存は下記のようになり、
問題のある構造は解消された。

<!-- pu:plant_uml/widget_ok.pu--><p><img src="data:image/png;base64,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" /></p>


## Accessor <a id="SS_3_4"></a>
publicメンバ変数とそれにアクセスするソースコードは典型的なアンチパターンであるため、
このようなコードを禁じるのが一般的なプラクティスである。

```cpp
    // @@@ example/design_pattern/accessor_ut.cpp 8

    class A {  // アンチパターン
    public:
        int32_t a_{0};
    };

    void f(A& a) noexcept
    {
        a.a_ = 3;

        // Do something
        ...
    }
```

とはいえ、ソフトウェアのプラクティスには必ずといってほど例外があり、
製品開発の現場において、オブジェクトのメンバ変数にアクセスせざるを得ないような場面は、
稀にではあるが発生する。
このような場合に適用するがのこのイデオムである。

```cpp
    // @@@ example/design_pattern/accessor_ut.cpp 28

    class A {  // Accessorの実装例
    public:
        void SetA(int32_t a) noexcept  // setter
        {
            a_ = a;
        }

        int32_t GetA() const noexcept  // getter
        {
            return a_;
        }

    private:
        int32_t a_{0};
        ...
    };

    void f(A& a) noexcept
    {
        a.SetA(3);

        // Do something
        ...
    }
```

メンバ変数への直接のアクセスに比べ、以下のようなメリットがある。

* アクセスのログを入れることができる。
* メンバ変数へのアクセスをデバッガで捕捉しやすくなる。
* setterに都合の悪い値が渡された場合、何らかの手段を取ることができる(assertや、エラー処理)。
* リファクタリングや機能修正により対象のメンバ変数がなくなった場合においても、
  クラスのインターフェースの変更を回避できる(修正箇所を局所化できる)。

一方で、クラスに対するこのような細かい制御は、カプセル化に対して問題を起こしやすい。
下記はその典型的なアンチパターンである。

```cpp
    // @@@ example/design_pattern/accessor_ut.cpp 62

    class A {  // Accessorを使用して細かすぎる制御をしてしまうアンチパターン
    public:
        void SetA(int32_t a) noexcept  // setter
        {
            a_ = a;
        }

        int32_t GetA() const noexcept  // getter
        {
            return a_;
        }

        void Change(bool is_changed) noexcept  // setter
        {
            is_changed_ = is_changed;
        }

        bool IsChanged() const noexcept  // getter
        {
            return is_changed_;
        }

        void DoSomething() noexcept  // is_changed_がtrueの時に、呼び出してほしい
        {
            // Do something
            ...
        }
        ...
    };

    void f(A& a) noexcept
    {
        if (a.GetA() != 3) {
            a.SetA(3);
            a.Change(true);
        }

        ...
    }

    void g(A& a) noexcept
    {
        if (!a.IsChanged()) {
            return;
        }

        a.Change(false);
        a.DoSomething();  // a.IsChanged()がtrueの時に実行する。

        ...
    }
```

上記ソースコードは、オブジェクトaのA::a\_が変更された場合、
その後、それをもとに何らかの動作を行うこと(a.DoSomething)を表しているが、
本来オブジェクトaの状態が変わったかどうかはオブジェクトa自体が判断すべきであり、
a.DoSomething()の実行においても、それが必要かどうかはオブジェクトaが判断すべきである。
この考えに基づいた修正ソースコードを下記に示す。

```cpp
    // @@@ example/design_pattern/accessor_ut.cpp 130

    class A {  // 上記アンチパターンからChange()とIsChanged()を削除し、状態の隠蔽レベルを強化
    public:
        void SetA(int32_t a) noexcept  // setter
        {
            if (a_ == a) {
                return;
            }

            a_          = a;
            is_changed_ = true;
        }

        void DoSomething() noexcept
        {
            if (!is_changed_) {
                return;
            }

            // Do something
            ...

            is_changed_ = false;  // 状態変更の取り消し
        }
        ...
    };

    void f(A& a) noexcept
    {
        a.SetA(3);

        ...
    }

    void g(A& a) noexcept
    {
        a.DoSomething();  // DoSomethingは無条件で呼び出す。
                          // 実際に何かをするかどうかは、オブジェクトaが決める。
        ...
    }
```

setterを使用する場合、上記のように処理の隠蔽化には特に気を付ける必要がある。


## Copy-And-Swap <a id="SS_3_5"></a>
メンバ変数にポインタやスマートポインタを持つクラスに

* copyコンストラクタ
* copy代入演算子
* moveコンストラクタ
* move代入演算子

が必要になった場合、コンパイラが生成するデフォルトの
[特殊メンバ関数](term_explanation.md#SS_6_2_1)では機能が不十分であることが多い。

下記に示すコードは、そのような場合の上記4関数の実装例である。

```cpp
    // @@@ example/design_pattern/no_copy_and_swap_ut.cpp 8

    class NoCopyAndSwap final {
    public:
        explicit NoCopyAndSwap(char const* name0, char const* name1)
            : name0_{name0 == nullptr ? "" : name0}, name1_{name1 == nullptr ? "" : name1}
        {
        }

        NoCopyAndSwap(NoCopyAndSwap const& rhs) : name0_{rhs.name0_}, name1_{rhs.name1_} {}

        NoCopyAndSwap(NoCopyAndSwap&& rhs) noexcept
            : name0_{std::exchange(rhs.name0_, nullptr)}, name1_{std::move(rhs.name1_)}
        {
            // move後には、
            //  * name0_はnullptr
            //  * name1_はnullptrを保持したunique_ptr
            // となる。
        }

        NoCopyAndSwap& operator=(NoCopyAndSwap const& rhs)
        {
            if (this == &rhs) {
                return *this;
            }

            // copyコンストラクタのコードクローン
            name0_ = rhs.name0_;
            name1_ = rhs.name1_;  // ここでエクセプションが発生すると*thisが壊れる

            return *this;
        }

        NoCopyAndSwap& operator=(NoCopyAndSwap&& rhs) noexcept
        {
            if (this == &rhs) {
                return *this;
            }

            // moveコンストラクタのコードクローン
            name0_ = std::exchange(rhs.name0_, nullptr);
            name1_ = std::string{};  // これがないと、name1_の値がrhs.name1_にスワップされる
            name1_ = std::move(rhs.name1_);

            return *this;
        }

        char const*        GetName0() const noexcept { return name0_; }
        std::string const& GetName1() const noexcept { return name1_; }
        ~NoCopyAndSwap() = default;

    private:
        char const* name0_;  // 問題やその改善を明示するために、敢えてname0_をchar const*としたが、
                             // 本来ならば、std::stringかstd::string_viewを使うべき
        std::string name1_;
    };
```

コード内のコメントで示したように、このコードには以下のような問題がある。

* copy代入演算子には、[エクセプション安全性の保証](term_explanation.md#SS_6_7)がない。
* 上記4関数は似ているにも関わらず、微妙な違いがあるためコードクローンとなっている。

ここで紹介するCopy-And-Swapはこのような問題を解決するためのイデオムである。

実装例を以下に示す。

```cpp
    // @@@ example/design_pattern/copy_and_swap_ut.cpp 6

    class CopyAndSwap final {
    public:
        explicit CopyAndSwap(char const* name0, char const* name1)
            : name0_{name0 == nullptr ? "" : name0}, name1_{name1 == nullptr ? "" : name1}
        {
        }

        CopyAndSwap(CopyAndSwap const& rhs) : name0_{rhs.name0_}, name1_{rhs.name1_} {}

        CopyAndSwap(CopyAndSwap&& rhs) noexcept
            : name0_{std::exchange(rhs.name0_, nullptr)}, name1_{std::move(rhs.name1_)}
        {
            // move後には、
            //  * name0_はnullptr
            //  * name1_は""を保持したstd::string
            // となる。
        }

        CopyAndSwap& operator=(CopyAndSwap const& rhs)
        {
            if (this == &rhs) {
                return *this;
            }

            // copyコンストラクタの使用
            CopyAndSwap tmp{rhs};  // ここでエクセプションが発生しても、tmp以外、壊れない

            Swap(tmp);

            return *this;
        }

        CopyAndSwap& operator=(CopyAndSwap&& rhs) noexcept
        {
            if (this == &rhs) {
                return *this;
            }

            CopyAndSwap tmp{std::move(rhs)};  // moveコンストラクタ

            Swap(tmp);

            return *this;
        }

        void Swap(CopyAndSwap& rhs) noexcept
        {
            std::swap(name0_, rhs.name0_);
            std::swap(name1_, rhs.name1_);
        }

        char const*        GetName0() const noexcept { return name0_; }
        std::string const& GetName1() const noexcept { return name1_; }
        ~CopyAndSwap() = default;

    private:
        char const* name0_;  // 問題やその改善を明示するために、敢えてname0_をchar const*としたが、
                             // 本来ならば、std::stringかstd::string_viewを使うべき
        std::string name1_;
    };
```

上記CopyAndSwapのcopyコンストラクタ、moveコンストラクタに変更はない。
また、CopyAndSwap::Swapに関してもstd::vector等が持つswapと同様のものである。
このイデオムの特徴は、copy代入演算子、
move代入演算子が各コンストラクタとSwap関数により実装されている所にある。
これにより[エクセプション安全性の保証](term_explanation.md#SS_6_7)を持つ4関数をコードクローンすることなく実装できる。


## Immutable <a id="SS_3_6"></a>
クラスに対するimmutable、immutabilityの定義を以下のように定める。

* immutable(不変な)なクラスとは、初期化後、状態の変更ができないクラスを指す。
* immutability(不変性)が高いクラスとは、
  状態を変更するメンバ関数(非constなメンバ関数)が少ないクラスを指す。

immutabilityが高いほど、そのクラスの使用方法は制限される。
これにより、そのクラスやそのクラスを使用しているソースコードの可読性やデバッグ容易性が向上する。
また、クラスがimmutableでなくても、そのクラスのオブジェクトをconstハンドル経由でアクセスすることで、
immutableとして扱うことができる。

一方で、「[Accessor](design_pattern.md#SS_3_4)」で紹介したsetterは、クラスのimmutabilityを下げる。
いつでも状態が変更できるため、ソースコードの可読性やデバッグ容易性が低下する。
また、マルチスレッド環境においてはこのことが競合問題や、
それを回避するためのロックがパフォーマンス問題やデッドロックを引き起こしてしまう。

従って、クラスを宣言、定義する場合、immutabilityを出来るだけ高くするべきであり、
そのクラスのオブジェクトを使う側は、
可能な限りimmutableオブジェクト(constオブジェクト)として扱うべきである。


## Clone(仮想コンストラクタ) <a id="SS_3_7"></a>
オブジェクトコピーによる[スライシング](term_explanation.md#SS_6_3_3)を回避するためのイデオムである。

下記は、オブジェクトコピーによるスライシングを起こしてしまう例である。

```cpp
    // @@@ example/design_pattern/clone_ut.cpp 8

    class BaseSlicing {
    public:
        ...
        virtual char const* Name() const noexcept { return "BaseSlicing"; }
    };

    class DerivedSlicing final : public BaseSlicing {
    public:
        ...
        virtual char const* Name() const noexcept override { return "DerivedSlicing"; }
    };

    TEST(Clone, object_slicing)
    {
        auto b = BaseSlicing{};
        auto d = DerivedSlicing{};

        BaseSlicing* b_ptr   = &b;
        BaseSlicing* b_ptr_d = &d;

        ASSERT_STREQ("BaseSlicing", b_ptr->Name());
        ASSERT_STREQ("DerivedSlicing", b_ptr_d->Name());

        *b_ptr = *b_ptr_d;  // コピーしたつもりだがスライシングにより、*b_ptrは、
                            // DerivedSlicingのインスタンスではなく、BaseSlicingのインスタンス

    #if 0
        ASSERT_STREQ("DerivedSlicing", b_ptr->Name());
    #else
        ASSERT_STREQ("BaseSlicing", b_ptr->Name());  // "DerivedSlicing"が返るはずだが、
                                                     // スライシングにより"BaseSlicing"が返る
    #endif
    }
```

下記は、上記にcloneイデオムを適用した例である。

```cpp
    // @@@ example/design_pattern/clone_ut.cpp 50

    // スライシングを起こさないようにコピー演算子の代わりにClone()を実装。
    class BaseNoSlicing {
    public:
        ...
        virtual char const* Name() const noexcept { return "BaseNoSlicing"; }

        virtual std::unique_ptr<BaseNoSlicing> Clone() { return std::make_unique<BaseNoSlicing>(); }

        BaseNoSlicing(BaseNoSlicing const&)            = delete;  // copy生成の禁止
        BaseNoSlicing& operator=(BaseNoSlicing const&) = delete;  // copy代入の禁止
    };

    class DerivedNoSlicing final : public BaseNoSlicing {
    public:
        ...
        virtual char const* Name() const noexcept override { return "DerivedNoSlicing"; }

        std::unique_ptr<DerivedNoSlicing> CloneOwn() { return std::make_unique<DerivedNoSlicing>(); }

        // DerivedNoSlicingはBaseNoSlicingの派生クラスであるため、
        // std::unique_ptr<DerivedNoSlicing>オブジェクトから
        // std::unique_ptr<BaseNoSlicing>オブジェクトへのmove代入可能
        virtual std::unique_ptr<BaseNoSlicing> Clone() override { return CloneOwn(); }
    };

    TEST(Clone, object_slicing_avoidance)
    {
        auto b = BaseNoSlicing{};
        auto d = DerivedNoSlicing{};

        BaseNoSlicing* b_ptr   = &b;
        BaseNoSlicing* b_ptr_d = &d;

        ASSERT_STREQ("BaseNoSlicing", b_ptr->Name());
        ASSERT_STREQ("DerivedNoSlicing", b_ptr_d->Name());

    #if 0
        *b_ptr = *b_ptr_d;                // コピー演算子をdeleteしたのでコンパイルエラー
    #else
        auto b_uptr = b_ptr_d->Clone();  // コピー演算子の代わりにClone()を使う。
    #endif

        ASSERT_STREQ("DerivedNoSlicing", b_uptr->Name());  // 意図通り"DerivedNoSlicing"が返る。
    }
```

B1::Clone()やそのオーバーライドであるD1::Clone()を使うことで、
スライシングを起こすことなくオブジェクトのコピーを行うことができるようになった。


## NVI(non virtual interface) <a id="SS_3_8"></a>
NVIとは、「virtualなメンバ関数をpublicにしない」という実装上の制約である。

下記のようにクラスBaseが定義されているとする。

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 7

    class Base {
    public:
        virtual bool DoSomething(int something) const noexcept
        {
            ...
        }

        virtual ~Base() = default;

    private:
        ...
    };
```

これを使うクラスはBase::DoSomething()に依存する。
また、このクラスから派生した下記のクラスDerivedもBase::DoSomething()に依存する。

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 26

    class Derived : public Base {
    public:
        virtual bool DoSomething(int something) const noexcept override
        {
            ...
        }

    private:
        ...
    };
```

この条件下ではBase::DoSomething()へ依存が集中し、この関数の修正や機能追加の作業コストが高くなる。
このイデオムは、この問題を軽減する。

これを用いた上記2クラスのリファクタリング例を以下に示す。

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 57

    class Base {
    public:
        bool DoSomething(int something) const noexcept { return do_something(something); }
        virtual ~Base() = default;

    private:
        virtual bool do_something(int something) const noexcept
        {
            ...
        }

        ...
    };

    class Derived : public Base {
    private:
        virtual bool do_something(int something) const noexcept override
        {
            ...
        }

        ...
    };
```

オーバーライド元の関数とそのオーバーライドのデフォルト引数の値は一致させる必要がある。

それに従わない下記のようなクラスとその派生クラス

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 105

    class NotNviBase {
    public:
        virtual std::string Name(bool mangled = false) const
        {
            return mangled ? typeid(*this).name() : "NotNviBase";
        }

        virtual ~NotNviBase() = default;
    };

    class NotNviDerived : public NotNviBase {
    public:
        virtual std::string Name(bool mangled = true) const override  // NG デフォルト値が違う
        {
            return mangled ? typeid(*this).name() : "NotNviDerived";
        }
    };
```

には下記の単体テストで示したような、
メンバ関数の振る舞いがその表層型に依存してしまう問題を持つことになる。

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 129

    NotNviDerived const d;
    NotNviBase const&   d_ref = d;

    ASSERT_EQ("NotNviDerived", d.Name(false));   // OK
    ASSERT_EQ("13NotNviDerived", d.Name(true));  // OK

    ASSERT_EQ("NotNviDerived", d_ref.Name(false));   // OK
    ASSERT_EQ("13NotNviDerived", d_ref.Name(true));  // OK

    ASSERT_EQ("13NotNviDerived", d.Name());    // mangled == false
    ASSERT_EQ("NotNviDerived", d_ref.Name());  // mangled == true

    ASSERT_NE(d.Name(), d_ref.Name());  // NG d_refの実態はdであるが、d.Name()と動きが違う
```

この例のように継承階層が浅く、デフォルト引数の数も少ない場合、
この値を一致させることは難しくないが、
これよりも遥かに複雑な実際のコードではこの一致の維持は困難になる。

下記のようにNVIに従わせることでこのような問題に対処できる。

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 148
    class NviBase {
    public:
        std::string Name(bool mangled = false) const { return name(mangled); }
        virtual ~NviBase() = default;

    private:
        virtual std::string name(bool mangled) const
        {
            return mangled ? typeid(*this).name() : "NviBase";
        }
    };

    class NviDerived : public NviBase {
    private:
        virtual std::string name(bool mangled) const override  // OK デフォルト値を持たない
        {
            return mangled ? typeid(*this).name() : "NviDerived";
        }
    };
```

下記の単体テストにより、この問題の解消が確認できる。

```cpp
    // @@@ example/design_pattern/nvi_ut.cpp 173

    NviBase const    b;
    NviDerived const d;
    NviBase const&   d_ref = d;

    ASSERT_EQ("NviDerived", d.Name(false));   // OK
    ASSERT_EQ("10NviDerived", d.Name(true));  // OK

    ASSERT_EQ("NviDerived", d_ref.Name(false));   // OK
    ASSERT_EQ("10NviDerived", d_ref.Name(true));  // OK

    ASSERT_EQ("NviDerived", d.Name());      // mangled == false
    ASSERT_EQ("NviDerived", d_ref.Name());  // mangled == false

    ASSERT_EQ(d.Name(), d_ref.Name());  // OK
```

なお、メンバ関数のデフォルト引数は、
そのクラス外部からのメンバ関数呼び出しを簡潔に記述するための記法であるため、
privateなメンバ関数はデフォルト引数を持つべきではない。


## RAII(scoped guard) <a id="SS_3_9"></a>
RAIIとは、「Resource Acquisition Is Initialization」の略語であり、
リソースの確保と解放をオブジェクトの初期化と破棄処理に結びつけるパターンもしくはイデオムである。
特にダイナミックにオブジェクトを生成する場合、
RAIIに従わないとメモリリークを防ぐことは困難である。

下記は、関数終了付近でdeleteする素朴なコードである。

```cpp
    // @@@ example/design_pattern/raii_ut.cpp 18

    // Aは外部の変数をリファレンスcounter_として保持し、
    //  * コンストラクタ呼び出し時に++counter_
    //  * デストラクタタ呼び出し時に--counter_
    // とするため、生成と解放が同じだけ行われれば外部の変数の値は0となる
    class A {
    public:
        A(uint32_t& couner) noexcept : counter_{++couner} {}
        ~A() { --counter_; }

    private:
        uint32_t& counter_;
    };

    char not_use_RAII_for_memory(size_t index, uint32_t& object_counter)
    {
        auto a = new A{object_counter};  // RAIIでない例
        auto s = std::string{"hehe"};

        auto ret = s.at(index);  // index >= 5でエクセプション発生

        // 何らかの処理

        delete a;         //  この行以前に関数を抜けるとaはメモリリーク

        return ret;
    }
```

このコードは下記の単体テストが示す通り、第1パラメータが5以上の場合、
エクセプションが発生しメモリリークしてしまう。

```cpp
    // @@@ example/design_pattern/raii_ut.cpp 71

    auto object_counter = 0U;

    // 第1引数が5なのでエクセプション発生
    ASSERT_THROW(not_use_RAII_for_memory(5, object_counter), std::exception);

    // 上記のnot_use_RAII_for_memoryではエクセプションが発生し、メモリリークする
    ASSERT_EQ(1, object_counter);
```

以下は、std::unique_ptrによってRAIIを導入し、この問題に対処した例である。

```cpp
    // @@@ example/design_pattern/raii_ut.cpp 83

    char use_RAII_for_memory(size_t index, uint32_t& object_counter)
    {
        auto a = std::make_unique<A>(object_counter);
        auto s = std::string{"hehe"};

        auto ret = s.at(index);  // index >= 5でエクセプション発生

        // 何らかの処理

        return ret;  // aは自動解放される
    }
```

下記単体テストで確認できるように、
エクセプション発生時にもstd::unique_ptrによる自動解放によりメモリリークは発生しない。

```cpp
    // @@@ example/design_pattern/raii_ut.cpp 100

    auto object_counter = 0U;

    // 第1引数が5なのでエクセプション発生
    ASSERT_THROW(use_RAII_for_memory(5, object_counter), std::exception);

    // 上記のuse_RAII_for_memoryではエクセプションが発生するがメモリリークはしない
    ASSERT_EQ(0, object_counter);
```

RAIIのテクニックはメモリ管理のみでなく、ファイルディスクリプタ(open-close、socket-close)
等のリソース管理においても有効であるという例を示す。

下記は、生成したソケットを関数終了付近でcloseする素朴なコードである。

```cpp
    // @@@ example/design_pattern/raii_ut.cpp 111

    // RAIIをしない例
    // 複数のclose()を書くような関数は、リソースリークを起こしやすい。
    void not_use_RAII_for_socket()
    {
        auto fd = socket(AF_INET, SOCK_STREAM, 0);

        try {
            // Do something
            ...
        }
        catch (std::exception const& e) {  // エクセプションはconstリファレンスで受ける。
            close(fd);                     // NG RAII未使用
            // Do something to recover
            ...

            return;
        }
        ...
        close(fd);  // NG RAII未使用
    }
```

エクセプションを扱うために関数の2か所でソケットをcloseしている。
この程度であれば大きな問題にはならないだろうが、実際には様々な条件が重なるため、
リソースの解放コードは醜悪にならざるを得ない。

このような場合には、下記するようなリソース解放用クラス

```cpp
    // @@@ h/scoped_guard.h 4

    /// @class ScopedGuard
    /// @brief RAIIのためのクラス。
    ///        コンストラクタ引数の関数オブジェクトをデストラクタから呼び出す。
    template <typename F>
    class ScopedGuard {
    public:
        explicit ScopedGuard(F&& f) noexcept : f_{f}
        {
            // f()がill-formedにならず、その戻りがvoidでなければならない
            static_assert(std::is_invocable_r_v<void, F>, "F must be callable and return void");
        }

        ~ScopedGuard() { f_(); }
        ScopedGuard(ScopedGuard const&)            = delete;  // copyは禁止
        ScopedGuard& operator=(ScopedGuard const&) = delete;  // copyは禁止

    private:
        F f_;
    };
```

を使用し、下記のようにすることで安全なコードをすっきりと書くことができる。

```cpp
    // @@@ example/design_pattern/raii_ut.cpp 138

    // RAIIをScopedGuardで行った例。
    // close()が自動実行されるためにリソース解放を忘れない。
    void use_RAII_for_socket()
    {
        auto fd    = socket(AF_INET, SOCK_STREAM, 0);
        auto guard = ScopedGuard{[fd] { close(fd); }};  // 関数終了時に自動実行

        try {
            // Do something
        }
        catch (...) {
            // Do something to recover

            return;
        }
        ...
    }
```

クリティカルセクションの保護をlock/unlockで行うstd::mutex等を使う場合にも、
std::lock_guard<>によってunlockを行うことで、同様の効果が得られる。


## Future <a id="SS_3_10"></a>
[Future](https://ja.wikipedia.org/wiki/Future_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)とは、
並行処理のためのデザインパターンであり、別スレッドに何らかの処理をさせる際、
その結果の取得を、必要になるまで後回しにする手法である。

C++11では、std::future, std::promise, std::asyncによって実現できる。

まずは、C++03以前のスタイルから示す。

```cpp
    // @@@ example/design_pattern/future_ut.cpp 11

    int do_something(std::string_view str0, std::string_view str1) noexcept
    {
        ...

        return ret0 + ret1;
    }

    TEST(Future, old_style)
    {
        auto str0 = std::string{};
        auto th0  = std::thread{[&str0]() noexcept { str0 = do_heavy_algorithm("thread 0"); }};

        auto str1 = std::string{};
        auto th1  = std::thread{[&str1]() noexcept { str1 = do_heavy_algorithm("thread 1"); }};

        //
        // このスレッドで行うべき何らかの処理
        //

        th0.join();
        th1.join();

        ASSERT_EQ("THREAD 0", str0);
        ASSERT_EQ("THREAD 1", str1);

        ASSERT_EQ(16, do_something(str0, str1));
    }
```

上記は、

1. 時間がかかる処理を並行して行うために、スレッドを二つ作る。
2. それぞれの完了をthread::join()で待ち合わせる。
3. その結果を参照キャプチャによって受け取る。
4. その2つの結果を別の関数に渡す。

という処理を行っている。

この程度の単純なコードでは特に問題にはならないが、目的外の処理が多いことがわかるだろう。

次にFutureパターンによって上記をリファクタリングした例を示す。

```cpp
    // @@@ example/design_pattern/future_ut.cpp 45

    TEST(Future, new_style)
    {
        std::future<std::string> result0
            = std::async(std::launch::async, []() noexcept { return do_heavy_algorithm("thread 0"); });

        std::future<std::string> result1
            = std::async(std::launch::async, []() noexcept { return do_heavy_algorithm("thread 1"); });

        // futre::get()は処理の待ち合わせと値の取り出しを行う。
        auto str0 = result0.get();
        auto str1 = result1.get();
        ASSERT_EQ(16, do_something(str0, str1));

        ASSERT_EQ("THREAD 0", str0);
        ASSERT_EQ("THREAD 1", str1);
    }
```

リファクタリングした例では、時間のかかる処理をstd::future型のオブジェクトにし、
その結果を必要とする関数に渡すことができるため、目的をよりダイレクトに表すことができる。

なお、

```cpp
    std::async(関数オブジェクト)
```

という形式を使った場合、関数オブジェクトは、

```cpp
    std::launch::async | std::launch::deferred
```

が指定されたとして実行される。この場合、

```cpp
    std::launch::deferred
```

の効果により、関数オブジェクトは、並行に実行されるとは限らない
(この仕様はランタイム系に依存しており、std::future::get()のコンテキストで実行されることもあり得る)。
従って、並行実行が必要な場合、上記例のように

```cpp
    std::launch::async
```

のみを明示的に指定するべきである。


## DI(dependency injection) <a id="SS_3_11"></a>
メンバ関数内でクラスDependedのオブジェクトを直接、生成する
(もしくは[Singleton](design_pattern.md#SS_3_12)オブジェクトや静的オブジェクト(std::coutやstd::cin等)に直接アクセスする)
クラスNotDIがあるとする。
この場合、クラスNotDIはクラスDependedのインスタンスに依存してしまう。
このような依存関係はクラスNotDIの可用性とテスト容易性を下げる。
これは、「仮にクラスDependedがデータベースをラップするクラスだった場合、
クラスNotDIの単体テストにデータベースが必要になる」ことからも容易に理解できる。

```cpp
    // @@@ example/design_pattern/di_ut.cpp 8

    /// @class Depended
    /// @brief NotDIや、DIから依存されるクラス
    class Depended {
        ...
    };

    /// @class NotDI
    /// @brief NotDIを使わない例。そのため、NotDIは、Dependedのインスタンスに依存している。
    class NotDI {
    public:
        NotDI() : not_di_depended_{std::make_unique<Depended>()} {}

        void DoSomething() { not_di_depended_->DoSomething(); }

    private:
        std::unique_ptr<Depended> not_di_depended_;
    };
```

下記は上記NotDIにDIパターンを適用した例である。
この場合、クラスDIは、クラスDependedの型にのみ依存する。

```cpp
    // @@@ example/design_pattern/di_ut.cpp 39

    /// @class DI
    /// @brief DIを使う例。そのため、DIは、Dependedの型に依存している。
    class DI {
    public:
        explicit DI(std::unique_ptr<Depended>&& di_depended) noexcept
            : di_depended_{std::move(di_depended)}
        {
        }

        void DoSomething() { di_depended_->DoSomething(); }

    private:
        std::unique_ptr<Depended> di_depended_;
    };
```

下記は、クラスNotDIとクラスDIがそれぞれのDoSomething()を呼び出すまでのシーケンス図である。

<!-- pu:plant_uml/di.pu--><p><img src="data:image/png;base64,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" /></p>

このパターンの効果により、
DIオブジェクトにはDependedかその派生クラスのオブジェクトを渡すことができるようになった。
これによりクラスDIは拡張性に対して柔軟になっただけでなく、テスト容易性も向上した。

次に示すのは、このパターンを使用して問題のある単体テストを修正した例である。

まずは、問題があるクラスとその単体テストを下記する。

```cpp
    // in device_io.h

    class DeviceIO {
    public:
        uint8_t read()
        {
            // ハードウェアに依存した何らかの処理
        }

        void write(uint8_t a)
        {
            // ハードウェアに依存した何らかの処理
        }

    private:
        // 何らかの宣言
    };

    #ifdef UNIT_TEST       // 単体テストビルドでは定義されるマクロ
    class DeviceIO_Mock {  // 単体テスト用のモック
    public:
        uint8_t read()
        {
            // ハードウェアに依存しない何らかの処理
        }

        void write(uint8_t a)
        {
            // ハードウェアに依存しない何らかの処理
        }

    private:
        // 何らかの宣言
    };
    #endif
```
```cpp
    // in widget.h
    
    #include "device_io.h"

    class Widget {
    public:
        void DoSomething()
        {
            // io_を使った何らかの処理
        }

        uint8_t GetResp()
        {
            // io_を使った何らかの処理
        }

    private:
    #ifdef UNIT_TEST
        DeviceIO_Mock io_;
    #else
        DeviceIO io_;
    #endif
    };
```
```cpp
    // in widget_ut.cpp

    // UNIT_TESTマクロが定義されたWidgetの単体テスト
    Widget w;

    w.DoSomething();
    ASSERT_EQ(0, w.GetResp());
```

当然であるが、この単体テストは、UNIT_TESTマクロを定義している場合のWidgetの評価であり、
UNIT_TESTを定義しない実際のコードの評価にはならない。

以下では、DIを用い、この問題を回避する。

```cpp
    // in device_io.h

    class DeviceIO {
    public:
        virtual uint8_t read()  // モックでオーバーライドするためvirtual
        {
            // ハードウェアに依存した何らかの処理
        }

        virtual void write(uint8_t a)  // モックでオーバーライドするためvirtual
        {
            // ハードウェアに依存した何らかの処理
        }
        virtual ~DeviceIO() = default;

    private:
        // 何らかの宣言
    };
```
```cpp
    // in widget.h

    class Widget {
    public:
        Widget(std::unique_ptr<DeviceIO> io = std::make_unique<DeviceIO>()) : io_{std::move(io)} {}

        void DoSomething()
        {
            // io_を使った何らかの処理
        }

        uint8_t GetResp()
        {
            // io_を使った何らかの処理
        }

    private:
        std::unique_ptr<DeviceIO> io_;
    };
```
```cpp
    // in widget_ut.cpp

    class DeviceIO_Mock : public DeviceIO {  // 単体テスト用のモック
    public:
        uint8_t read() override
        {
            // ハードウェアに依存しない何らかの処理
        }

        void write(uint8_t a) override
        {
            // ハードウェアに依存しない何らかの処理
        }

    private:
        // 何らかの宣言
    };
```
```cpp
    // 上記DeviceIO_Mockと同様に、in widget_ut.cpp

    Widget w{std::unique_ptr<DeviceIO>(new DeviceIO_Mock)};  // モックのインジェクション

    // Widgetの単体テスト
    w.DoSomething();
    ASSERT_EQ(1, w.GetResp());
```

この例では、単体テストのためだけに仮想関数を導入しているため、多少やりすぎの感がある。
そのような場合、下記のようにテンプレートを用いればよい。

```cpp
    // in device_io.h

    class DeviceIO {
    public:
        uint8_t read()  // Widgetがテンプレートであるため非virtualで良い
        {
            // ハードウェアに依存した何らかの処理
        }

        void write(uint8_t a)  // Widgetがテンプレートであるため非virtualで良い
        {
            // ハードウェアに依存した何らかの処理
        }
        virtual ~DeviceIO() = default;

    private:
        // 何らかの宣言
    };
```
```cpp
    // in widget.h

    template <class T = DeviceIO>
    class Widget {
    public:
        void DoSomething()
        {
            // io_を使った何らかの処理
        }

        uint8_t GetResp()
        {
            // io_を使った何らかの処理
        }

    private:
        T io_;
    };
```
```cpp
    // in widget_ut.cpp

    class DeviceIO_Mock {  // 単体テスト用のモック
    public:
        uint8_t read()  // Widgetがテンプレートであるため非virtualで良い
        {
            // ハードウェアに依存しない何らかの処理
        }

        void write(uint8_t a)  // Widgetがテンプレートであるため非virtualで良い
        {
            // ハードウェアに依存しない何らかの処理
        }

    private:
        // 何らかの宣言
    };
```
```cpp
    // 上記DeviceIO_Mockと同様に、in widget_ut.cpp

    Widget<DeviceIO_Mock> w;

    // Widget<>の単体テスト
    w.DoSomething();
    ASSERT_EQ(2, w.GetResp());
```

以上からわかるように、
ここで紹介したDIは単体テストを容易にするクラス設計のためにも非常に有用なパターンである。


## Singleton <a id="SS_3_12"></a>
このパターンにより、特定のクラスのインスタンスをシステム全体で唯一にすることができる。
これにより、グローバルオブジェクトを規律正しく使用しやすくなる。

以下は、Singletonの実装例である。

```cpp
    // @@@ example/design_pattern/singleton_ut.cpp 7

    class Singleton final {
    public:
        static Singleton&       Inst();
        static Singleton const& InstConst() noexcept  // constインスタンスを返す
        {
            return Inst();
        }
        ...

    private:
        Singleton() noexcept {}  // コンストラクタをprivateにすることで、
                                 // Inst()以外ではこのオブジェクトを生成できない。
        ...
    };

    Singleton& Singleton::Inst()
    {
        static Singleton inst;  //  instの初期化が同時に行われることはない。

        return inst;
    }

    TEST(Singleton, how_to_use)
    {
        auto&       inst       = Singleton::Inst();
        auto const& inst_const = Singleton::InstConst();

        ASSERT_EQ(0, inst.GetXxx());
        ASSERT_EQ(0, inst_const.GetXxx());
    #if 0
        inst_const.SetXxx(10);  // inst_constはconstオブジェクトなのでコンパイルエラー
    #else
        inst.SetXxx(10);
    #endif
        ASSERT_EQ(10, inst.GetXxx());
        ASSERT_EQ(10, inst_const.GetXxx());

        inst.SetXxx(0);
        ASSERT_EQ(0, inst.GetXxx());
        ASSERT_EQ(0, inst_const.GetXxx());
    }
    }  // namespace
```

このパターンを使用する場合、以下に注意する。  

* Singletonはデザインパターンの中でも、特にパターン猿病を発生しやすい。
  Singletonは「ほとんどグローバル変数である」ことを理解した上で、控えめに使用する。
* Singletonを定義する場合、以下の二つを定義する。
    * インスタンスを返すstaticメンバ関数Inst()
    * constインスタンスを返すstaticメンバ関数InstConst()
* InstConst()は、Inst()が返すオブジェクトと同じオブジェクトを返すようにする。
* Singletonには、可能な限りInstConst()経由でアクセスする。

Singletonオブジェクトの初期化(最初のコンストラクタ呼び出し)は、
C++03以前はスレッドセーフでなかったため、「 Double Checked Lockingを使って競合を避ける」か、
「他のスレッドを起動する前にメインスレッドから各SingletonのInstConst()を呼び出す」
ことが必要であった。
C++11から上記例のようなSingletonオブジェクトのコンストラクタ呼び出しはスレッドセーフとなったため、
このような黒魔術が不要になった。

なお、Inst()のような関数を複数定義する場合、そのパターンはNamed Constructor
(「[Named Constructor](design_pattern.md#SS_3_17)」参照)と呼ばれる。


## State <a id="SS_3_13"></a>
Stateは、オブジェクトの状態と、それに伴う振る舞いを分離して記述するためのパターンである。
これにより状態の追加、削減、変更に伴う修正範囲が限定される
(「[オープン・クローズドの原則(OCP)](solid.md#SS_2_2)」参照)。
またオブジェクトのインターフェース変更(パブリックメンバ関数の変更)に関しても、修正箇所が明確になる。

<!-- pu:plant_uml/state_machine.pu--><p><img src="data:image/png;base64,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" /></p>

上記ステートマシン図の「オールドスタイルによる実装」と、「stateパターンによる実装」、
それぞれを例示する。

まずは、下記にオールドスタイルな実装例を示す。
この実装では、状態を静的なenum変数thread_old_style_stateで管理するため、
ThreadOldStyleStateStr()、ThreadOldStyleRun()、ThreadOldStyleAbort()、ThreadOldStyleSuspend()
には、thread_old_style_stateに対する同型のswitch文が入ることになる(下記例では一部省略)。
これは醜悪で、バグを起こしやすい構造である。
ただし、要求される状態遷移がこの例程度であり、状態ごとに決められた振る舞いの数が少なければ、
この構造でも問題ないともいえる。

```cpp
    // @@@ example/design_pattern/state_machine_old.h 4

    extern std::string_view ThreadOldStyleStateStr() noexcept;
    extern void             ThreadOldStyleRun();
    extern void             ThreadOldStyleAbort();
    extern void             ThreadOldStyleSuspend();
```

```cpp
    // @@@ example/design_pattern/state_machine_old.cpp 6

    namespace {
    enum class ThreadOldStyleState {
        Idle,
        Running,
        Suspending,
    };

    ThreadOldStyleState thread_old_style_state;
    ...
    }  // namespace

    std::string_view ThreadOldStyleStateStr() noexcept
    {
        switch (thread_old_style_state) {  // このswitch文と同型switch文が何度も記述される
        case ThreadOldStyleState::Idle:
            return "Idle";
        case ThreadOldStyleState::Running:
            return "Running";
        case ThreadOldStyleState::Suspending:
            return "Suspending";
        default:
            assert(false);
            return "";
        }
    }

    void ThreadOldStyleRun()
    {
        switch (thread_old_style_state) {
        case ThreadOldStyleState::Idle:
        case ThreadOldStyleState::Running:
            thread_old_style_state = ThreadOldStyleState::Running;
            break;
        case ThreadOldStyleState::Suspending:
            --thread_old_style_suspend_count;
            if (thread_old_style_suspend_count == 0) {
                thread_old_style_state = ThreadOldStyleState::Running;
            }
            break;
        default:
            assert(false);
        }
    }

    void ThreadOldStyleAbort()
    {
        ...
    }

    void ThreadOldStyleSuspend()
    {
        ...
    }
```

```cpp
    // @@@ example/design_pattern/state_machine_ut.cpp 15

    // ステートのテスト。仕様書よりも単体テストでその仕様や使用法を記述したほうが正確に理解できる。
    TEST(StateMachine, old_style)
    {
        ASSERT_EQ("Idle", ThreadOldStyleStateStr());

        ThreadOldStyleAbort();
        ASSERT_EQ("Idle", ThreadOldStyleStateStr());

        ThreadOldStyleRun();
        ASSERT_EQ("Running", ThreadOldStyleStateStr());

        ThreadOldStyleRun();
        ASSERT_EQ("Running", ThreadOldStyleStateStr());

        ThreadOldStyleSuspend();
        ASSERT_EQ("Suspending", ThreadOldStyleStateStr());  // suspend_count_ == 1

        ThreadOldStyleSuspend();
        ASSERT_EQ("Suspending", ThreadOldStyleStateStr());  // suspend_count_ == 2

        ThreadOldStyleRun();
        ASSERT_EQ("Suspending", ThreadOldStyleStateStr());  // suspend_count_ == 1

        ...
    }
```

下記は、上記例へstateパターンを適用した例である。
まずは、stateパターンを形成するクラスの関係をクラス図で示す。

<!-- pu:plant_uml/state_machine_class.pu--><p><img src="data:image/png;base64,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" /></p>

次に上記クラス図の実装例を示す。

```cpp
    // @@@ example/design_pattern/state_machine_new.h 6

    /// @class ThreadNewStyleState
    /// @brief ThreadNewStyleのステートを表す基底クラス
    class ThreadNewStyleState {
    public:
        ThreadNewStyleState()          = default;
        virtual ~ThreadNewStyleState() = default;

        std::unique_ptr<ThreadNewStyleState> Abort()  // NVI
        {
            return abort_thread();
        }

        std::unique_ptr<ThreadNewStyleState> Run()  // NVI
        {
            return run_thread();
        }

        std::unique_ptr<ThreadNewStyleState> Suspend()  // NVI
        {
            return suspend_thread();
        }

        std::string_view GetStateStr() const noexcept { return get_state_str(); }

    private:
        virtual std::unique_ptr<ThreadNewStyleState> abort_thread()
        {
            return {};  // デフォルトでは何もしない。
        }

        virtual std::unique_ptr<ThreadNewStyleState> run_thread()
        {
            return {};  // デフォルトでは何もしない。
        }

        virtual std::unique_ptr<ThreadNewStyleState> suspend_thread()
        {
            return {};  // デフォルトでは何もしない。
        }

        virtual std::string_view get_state_str() const noexcept = 0;
    };
```

```cpp
    // @@@ example/design_pattern/state_machine_new.h 52

    class ThreadNewStyle final {
    public:
        ThreadNewStyle();

        void Abort() { change_state(state_->Abort()); }

        void Run() { change_state(state_->Run()); }

        void Suspend() { change_state(state_->Suspend()); }

        std::string_view GetStateStr() const noexcept { return state_->GetStateStr(); }

    private:
        std::unique_ptr<ThreadNewStyleState> state_;

        void change_state(std::unique_ptr<ThreadNewStyleState>&& new_state) noexcept
        {
            if (new_state) {
                state_ = std::move(new_state);
            }
        }
    };
```

```cpp
    // @@@ example/design_pattern/state_machine_new.cpp 10

    class ThreadNewStyleState_Idle final : public ThreadNewStyleState {
        ...
    };

    class ThreadNewStyleState_Running final : public ThreadNewStyleState {
        ...
    };

    class ThreadNewStyleState_Suspending final : public ThreadNewStyleState {
    public:
        ...
    private:
        virtual std::unique_ptr<ThreadNewStyleState> abort_thread() override
        {
            // do something to abort
            ...

            return std::make_unique<ThreadNewStyleState_Idle>();
        }

        virtual std::unique_ptr<ThreadNewStyleState> run_thread() override
        {
            --suspend_count_;

            if (suspend_count_ == 0) {
                // do something to resume
                ...
                return std::make_unique<ThreadNewStyleState_Running>();
            }
            else {
                return {};
            }
        }

        virtual std::unique_ptr<ThreadNewStyleState> suspend_thread() override
        {
            ++suspend_count_;

            return {};
        }
        ...
    };
```

```cpp
    // @@@ example/design_pattern/state_machine_ut.cpp 57

    TEST(StateMachine, new_style)
    {
        auto tns = ThreadNewStyle{};

        ASSERT_EQ("Idle", tns.GetStateStr());

        tns.Abort();
        ASSERT_EQ("Idle", tns.GetStateStr());

        tns.Run();
        ASSERT_EQ("Running", tns.GetStateStr());

        tns.Run();
        ASSERT_EQ("Running", tns.GetStateStr());

        tns.Suspend();
        ASSERT_EQ("Suspending", tns.GetStateStr());  // suspend_count_ == 1

        tns.Suspend();
        ASSERT_EQ("Suspending", tns.GetStateStr());  // suspend_count_ == 2

        tns.Run();
        ASSERT_EQ("Suspending", tns.GetStateStr());  // suspend_count_ == 1

        ...
    }
```

オールドスタイルな構造に比べると一見複雑に見えるが同型のswitch構造がないため、
状態の増減や振る舞いの変更等への対応が容易である。
一方で、前述したとおり、この例程度の要求であれば、
シンプルさという意味においてオールドスタイルのソースコードの方が優れているともいえる。
従って、オールドスタイルとstateパターンの選択は、
その要求の複雑さと安定度によって決定されるべきものである。

なお、C++でのstateパターンの実装には、下記に示すようなメンバ関数を使う方法もある。
多くのクラスを作る必要はないが、
各状態での状態管理変数を別の状態のものと分けて管理することができないため、
複雑な状態管理が必要な場合には使えないが、単純な状態管理で十分な場合には便利なパターンである。

```cpp
    // @@@ example/design_pattern/state_machine_new.h 77

    class ThreadNewStyle2 final {
    public:
        ThreadNewStyle2() noexcept {}

        void             Abort() { (this->*abort_)(); }
        void             Run() { (this->*run_)(); }
        void             Suspend() { (this->*suspend_)(); }
        std::string_view GetStateStr() const noexcept { return state_str_; }

    private:
        void (ThreadNewStyle2::*abort_)()   = &ThreadNewStyle2::abort_idle;
        void (ThreadNewStyle2::*run_)()     = &ThreadNewStyle2::run_idle;
        void (ThreadNewStyle2::*suspend_)() = &ThreadNewStyle2::suspend_idle;
        std::string_view state_str_{state_str_idle_};

        void                                 abort_idle() {}  // do nothing
        void                                 run_idle();
        void                                 suspend_idle() {}  // do nothing
        static inline std::string_view const state_str_idle_{"Idle"};

        void                                 abort_running();
        void                                 run_running() {}  // do nothing
        void                                 suspend_running();
        static inline std::string_view const state_str_running_{"Running"};

        void                                 abort_suspending();
        void                                 run_suspending();
        void                                 suspend_suspending() {}  // do nothing
        static inline std::string_view const state_str_suspending_{"Suspending"};
    };
```

```cpp
    // @@@ example/design_pattern/state_machine_new.cpp 106

    void ThreadNewStyle2::run_idle()
    {
        // スレッドの始動処理
        ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_running;
        suspend_   = &ThreadNewStyle2::suspend_running;
        state_str_ = state_str_running_;
    }

    void ThreadNewStyle2::abort_running()
    {
        // スレッドのアボート処理
        ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_idle;
        suspend_   = &ThreadNewStyle2::suspend_idle;
        state_str_ = state_str_idle_;
    }

    void ThreadNewStyle2::suspend_running()
    {
        // スレッドのサスペンド処理
        ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_suspending;
        suspend_   = &ThreadNewStyle2::suspend_suspending;
        state_str_ = state_str_suspending_;
    }

    void ThreadNewStyle2::run_suspending()
    {
        // スレッドのレジューム処理
        ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_running;
        suspend_   = &ThreadNewStyle2::suspend_running;
        state_str_ = state_str_running_;
    }
```

```cpp
    // @@@ example/design_pattern/state_machine_ut.cpp 95

    TEST(StateMachine, new_style2)
    {
        auto tns = ThreadNewStyle2{};

        ASSERT_EQ("Idle", tns.GetStateStr());

        tns.Run();
        ASSERT_EQ("Running", tns.GetStateStr());

        tns.Suspend();
        ASSERT_EQ("Suspending", tns.GetStateStr());

        tns.Suspend();
        ASSERT_EQ("Suspending", tns.GetStateStr());
    }
```


## Null Object <a id="SS_3_14"></a>
オブジェクトへのポインタを受け取った関数が
「そのポインタがnullptrでない場合、そのポインタが指すオブジェクトに何かをさせる」
というような典型的な条件文を削減するためのパターンである。

```cpp
    // @@@ example/design_pattern/null_object_ut.cpp 7

    class A {
    public:
        ...
        bool Action() noexcept
        {
            // do something
            ...
            return result;
        }
        ...
    };

    bool ActionOldStyle(A* a) noexcept
    {
        if (a != nullptr) {  // ←このif文を消すためのパターン。
            return a->Action();
        }
        else {
            return false;
        }
    }
```

上記例にNull Objectパターンを適用した例を下記する。

```cpp
    // @@@ example/design_pattern/null_object_ut.cpp 41

    class A {
    public:
        ...
        bool Action() noexcept { return action(); }

    private:
        virtual bool action() noexcept
        {
            // do something
            ...
            return result;
        }
        ...
    };

    class ANull final : public A {
        ...
    private:
        virtual bool action() noexcept override { return false; }
    };

    bool ActionNewStyle(A& a) noexcept
    {
        return a.Action();  // ←Null Objectによりif文が消えた。
    }
```

この単純な例では、逆にソースコードが複雑化したように見えるが、

```cpp
    if(a != nullptr)
```

を頻繁に使うような関数、
クラスではソースコードの単純化やnullptrチェック漏れの防止に非常に有効である。


## Templateメソッド <a id="SS_3_15"></a>
Templateメソッドは、雛形の形式(書式等)を定めるメンバ関数(templateメソッド)と、
それを埋めるための振る舞いやデータを定めるメンバ関数を分離するときに用いるパターンである。

以下に実装例を示す。

```cpp
    // @@@ example/design_pattern/template_method.h 6

    /// @class XxxData
    /// @brief 何かのデータを入れる箱
    struct XxxData {
        int a;
        int b;
        int c;
    };

    /// @class XxxDataFormatterIF
    /// @brief data_storer_if.cppに定義すべきだが、サンプルであるため便宜上同じファイルで定義する
    ///        データフォーマットを行うクラスのインターフェースクラス
    class XxxDataFormatterIF {
    public:
        explicit XxxDataFormatterIF(std::string_view formatter_name) noexcept
            : formatter_name_{formatter_name}
        {
        }
        virtual ~XxxDataFormatterIF() = default;

        std::string ToString(XxxData const& xxx_data) const
        {
            return header() + body(xxx_data) + footer();
        }

        std::string ToString(std::vector<XxxData> const& xxx_datas) const
        {
            std::string ret{header()};

            for (auto const& xxx_data : xxx_datas) {
                ret += body(xxx_data);
            }

            return ret + footer();
        }
        ...
    private:
        virtual std::string const& header() const                      = 0;
        virtual std::string const& footer() const                      = 0;
        virtual std::string        body(XxxData const& xxx_data) const = 0;

        ...
    };
```

上記XxxDataFormatterIFでは、以下のようなメンバ関数を宣言、定義している。

|メンバ関数  |                      | 振る舞い                                                 |
|:-----------|:---------------------|:---------------------------------------------------------|
| header()   | private pure-virtual | ヘッダをstd::stringオブジェクトとして生成                |
| footer()   | private pure-virtual | フッタをstd::stringオブジェクトとして生成                |
| body()     | private pure-virtual | XxxDataからボディをstd::stringオブジェクトとして生成     |
| ToString() | public  normal       | header(),body(),footer()の出力を組み合わせた全体像を生成 |

この構造により、XxxDataFormatterIFは、

* 全体の書式を定義している。
* 各行の生成をXxxDataFormatterIFから派生した具象クラスに委譲している。

下記XxxDataFormatterXml、XxxDataFormatterCsv、XxxDataFormatterTableでは、
header()、body()、footer()をオーバーライドすることで、それぞれの機能を実現している。

```cpp
    // @@@ example/design_pattern/template_method.cpp 8

    /// @class XxxDataFormatterXml
    /// @brief XxxDataをXmlに変換
    class XxxDataFormatterXml final : public XxxDataFormatterIF {
        ...
    private:
        virtual std::string const& header() const noexcept final { return header_; }
        virtual std::string const& footer() const noexcept final { return footer_; }
        virtual std::string        body(XxxData const& xxx_data) const override
        {
            auto content = std::string{"<Item>\n"};

            content += "    <XxxData a=\"" + std::to_string(xxx_data.a) + "\">\n";
            content += "    <XxxData b=\"" + std::to_string(xxx_data.b) + "\">\n";
            content += "    <XxxData c=\"" + std::to_string(xxx_data.c) + "\">\n";

            return content + "</Itemp>\n";
        }

        static inline std::string const header_{
            "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<XxxDataFormatterXml>\n"};
        static inline std::string const footer_{"</XxxDataFormatterXml>\n"};
    };

    /// @class XxxDataFormatterCsv
    /// @brief XxxDataをCsvに変換
    class XxxDataFormatterCsv final : public XxxDataFormatterIF {
        ...
    private:
        virtual std::string const& header() const noexcept final { return header_; }
        virtual std::string const& footer() const noexcept final { return footer_; }
        virtual std::string        body(XxxData const& xxx_data) const override
        {
            return std::string{std::to_string(xxx_data.a) + ", " + std::to_string(xxx_data.b) + ", "
                               + std::to_string(xxx_data.b) + "\n"};
        }

        static inline std::string const header_{"a, b, c\n"};
        static inline std::string const footer_{};
    };

    /// @class XxxDataFormatterTable
    /// @brief XxxDataをTableに変換
    class XxxDataFormatterTable final : public XxxDataFormatterIF {
        ...
    private:
        virtual std::string const& header() const noexcept final { return header_; }
        virtual std::string const& footer() const noexcept final { return footer_; }
        virtual std::string        body(XxxData const& xxx_data) const override
        {
            auto a = std::string{std::string{"| "} + std::to_string(xxx_data.a)};
            auto b = std::string{std::string{"| "} + std::to_string(xxx_data.b)};
            auto c = std::string{std::string{"| "} + std::to_string(xxx_data.c)};

            a += std::string(colomun_ - a.size() + 1, ' ');
            b += std::string(colomun_ - b.size() + 1, ' ');
            c += std::string(colomun_ - c.size() + 1, ' ');

            return a + b + c + "|\n" + border_;
        }
        ...
    };
```

以下の単体テストで、これらのクラスの振る舞いを示す。

```cpp
    // @@@ example/design_pattern/template_method_ut.cpp 6

    TEST(TemplateMethod, xml)
    {
        auto xml = XxxDataFormatterXml{};

        {
            auto const xd     = XxxData{1, 100, 10};
            auto const expect = std::string_view{
                "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
                "<XxxDataFormatterXml>\n"
                "<Item>\n"
                "    <XxxData a=\"1\">\n"
                "    <XxxData b=\"100\">\n"
                "    <XxxData c=\"10\">\n"
                "</Itemp>\n"
                "</XxxDataFormatterXml>\n"};
            auto const actual = xml.ToString(xd);

            ASSERT_EQ(expect, actual);
        }
        {
            auto const xds    = std::vector<XxxData>{{1, 100, 10}, {2, 200, 20}};
            auto const expect = std::string_view{
                "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
                "<XxxDataFormatterXml>\n"
                "<Item>\n"
                "    <XxxData a=\"1\">\n"
                "    <XxxData b=\"100\">\n"
                "    <XxxData c=\"10\">\n"
                "</Itemp>\n"
                "<Item>\n"
                "    <XxxData a=\"2\">\n"
                "    <XxxData b=\"200\">\n"
                "    <XxxData c=\"20\">\n"
                "</Itemp>\n"
                "</XxxDataFormatterXml>\n"};
            auto const actual = xml.ToString(xds);

            ASSERT_EQ(expect, actual);
        }
    }

    TEST(TemplateMethod, csv)
    {
        auto csv = XxxDataFormatterCsv{};

        {
            auto const xd     = XxxData{1, 100, 10};
            auto const expect = std::string_view{
                "a, b, c\n"
                "1, 100, 100\n"};
            auto const actual = csv.ToString(xd);

            ASSERT_EQ(expect, actual);
        }
        {
            auto const xds    = std::vector<XxxData>{{1, 100, 10}, {2, 200, 20}};
            auto const expect = std::string_view{
                "a, b, c\n"
                "1, 100, 100\n"
                "2, 200, 200\n"};
            auto const actual = csv.ToString(xds);

            ASSERT_EQ(expect, actual);
        }
    }

    TEST(TemplateMethod, table)
    {
        auto table = XxxDataFormatterTable{};

        ...
    }
```

上記で示した実装例は、public継承による動的ポリモーフィズムを使用したため、
XxxDataFormatterXml、XxxDataFormatterCsv、XxxDataFormatterTableのインスタンスやそのポインタは、
XxxDataFormatterIFのリファレンスやポインタとして表現できる。
この性質は、[Factory](design_pattern.md#SS_3_16)や[Named Constructor](design_pattern.md#SS_3_17)の実装には不可欠であるが、
逆にこのようなポリモーフィズムが不要な場合、このよう柔軟性も不要である。

そういった場合、private継承を用いるか、
テンプレートを用いた静的ポリモーフィズムを用いることでこの柔軟性を排除できる。

下記のコードはそのような実装例である。

```cpp
    // @@@ example/design_pattern/template_method_ut.cpp 111

    template <typename T>  // Tは下記のXxxDataFormatterXmlのようなクラス
    class XxxDataFormatter : private T {
    public:
        std::string ToString(XxxData const& xxx_data) const
        {
            return T::Header() + T::Body(xxx_data) + T::Footer();
        }

        std::string ToString(std::vector<XxxData> const& xxx_datas) const
        {
            auto ret = std::string{T::Header()};

            for (auto const& xxx_data : xxx_datas) {
                ret += T::Body(xxx_data);
            }

            return ret + T::Footer();
        }
    };

    class XxxDataFormatterXml_Impl {
    public:
        std::string const& Header() const noexcept { return header_; }
        std::string const& Footer() const noexcept { return footer_; }
        std::string        Body(XxxData const& xxx_data) const
        {
            auto content = std::string{"<Item>\n"};

            content += "    <XxxData a=\"" + std::to_string(xxx_data.a) + "\">\n";
            content += "    <XxxData b=\"" + std::to_string(xxx_data.b) + "\">\n";
            content += "    <XxxData c=\"" + std::to_string(xxx_data.c) + "\">\n";

            return content + "</Itemp>\n";
        }

    private:
        inline static std::string const header_{
            "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<XxxDataFormatterXml>\n"};
        inline static std::string const footer_{"</XxxDataFormatterXml>\n"};
    };

    using XxxDataFormatterXml = XxxDataFormatter<XxxDataFormatterXml_Impl>;
```

上記の単体テストは下記のようになる。

```cpp
    // @@@ example/design_pattern/template_method_ut.cpp 159

        auto xml = XxxDataFormatterXml{};

        {
            auto const xd     = XxxData{1, 100, 10};
            auto const expect = std::string{
                "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
                "<XxxDataFormatterXml>\n"
                "<Item>\n"
                "    <XxxData a=\"1\">\n"
                "    <XxxData b=\"100\">\n"
                "    <XxxData c=\"10\">\n"
                "</Itemp>\n"
                "</XxxDataFormatterXml>\n"};
            auto const actual = xml.ToString(xd);

            ASSERT_EQ(expect, actual);
        }
        {
            auto const xds    = std::vector<XxxData>{{1, 100, 10}, {2, 200, 20}};
            auto const expect = std::string{
                "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
                "<XxxDataFormatterXml>\n"
                "<Item>\n"
                "    <XxxData a=\"1\">\n"
                "    <XxxData b=\"100\">\n"
                "    <XxxData c=\"10\">\n"
                "</Itemp>\n"
                "<Item>\n"
                "    <XxxData a=\"2\">\n"
                "    <XxxData b=\"200\">\n"
                "    <XxxData c=\"20\">\n"
                "</Itemp>\n"
                "</XxxDataFormatterXml>\n"};
            auto const actual = xml.ToString(xds);

            ASSERT_EQ(expect, actual);
        }
```


## Factory <a id="SS_3_16"></a>
Factoryは、専用関数(Factory関数)にオブジェクト生成をさせるためのパターンである。
オブジェクトを生成するクラスや関数をそのオブジェクトの生成方法に依存させたくない場合や、
オブジェクトの生成に統一されたルールを適用したい場合等に用いられる。
DI(「[DI(dependency injection)](design_pattern.md#SS_3_11)」参照)と組み合わせて使われることが多い。

「[Templateメソッド](design_pattern.md#SS_3_15)」の例にFactoryを適用したソースコードを下記する。

下記のXxxDataFormatterFactory関数により、

* XxxDataFormatterIFオブジェクトはstd::unique_ptrで保持されることを強制できる
* XxxDataFormatterIFから派生したクラスはtemplate_method.cppの無名名前空間で宣言できるため、
  これらのクラスは他のクラスから直接依存されることがない

といった効果がある。

```cpp
    // @@@ example/design_pattern/template_method.h 73

    enum class XxxDataFormatterMethod {
        Xml,
        Csv,
        Table,
    };

    /// @fn XxxDataFormatterFactory
    /// @brief std::unique_ptrで保持されたXxxDataFormatterIFオブジェクトを生成するFactory関数
    /// @param method XxxDataFormatterMethodのいずれか
    /// @return std::unique_ptr<const XxxDataFormatterIF>
    ///         XxxDataFormatterIFはconstメンバ関数のみを持つため、戻り値もconstオブジェクト
    std::unique_ptr<XxxDataFormatterIF const> XxxDataFormatterFactory(XxxDataFormatterMethod method);
```

```cpp
    // @@@ example/design_pattern/template_method.cpp 109

    std::unique_ptr<XxxDataFormatterIF const> XxxDataFormatterFactory(XxxDataFormatterMethod method)
    {
        switch (method) {
        case XxxDataFormatterMethod::Xml:
            return std::unique_ptr<XxxDataFormatterIF const>{new XxxDataFormatterXml};  // C++11
        case XxxDataFormatterMethod::Csv:
            return std::make_unique<XxxDataFormatterCsv const>();  // C++14 make_uniqueもFactory
        case XxxDataFormatterMethod::Table:
            return std::make_unique<XxxDataFormatterTable const>();
        default:
            assert(false);
            return {};
        }
    }
```

以下に上記クラスの単体テストを示す。

```cpp
    // @@@ example/design_pattern/template_method_factory_ut.cpp 7

    TEST(Factory, xml)
    {
        auto xml = XxxDataFormatterFactory(XxxDataFormatterMethod::Xml);

        ...
    }

    TEST(Factory, csv)
    {
        auto csv = XxxDataFormatterFactory(XxxDataFormatterMethod::Csv);

        ...
    }

    TEST(Factory, table)
    {
        auto table = XxxDataFormatterFactory(XxxDataFormatterMethod::Table);

        {
            auto const xd     = XxxData{1, 100, 10};
            auto const expect = std::string_view{
                "+--------|--------|--------+\n"
                "| a      | b      | c      |\n"
                "+--------|--------|--------+\n"
                "| 1      | 100    | 10     |\n"
                "+--------|--------|--------+\n"};
            auto const actual = table->ToString(xd);

            ASSERT_EQ(expect, actual);
        }
        {
            auto const xds    = std::vector<XxxData>{{1, 100, 10}, {2, 200, 20}};
            auto const expect = std::string_view{
                "+--------|--------|--------+\n"
                "| a      | b      | c      |\n"
                "+--------|--------|--------+\n"
                "| 1      | 100    | 10     |\n"
                "+--------|--------|--------+\n"
                "| 2      | 200    | 20     |\n"
                "+--------|--------|--------+\n"};
            auto const actual = table->ToString(xds);

            ASSERT_EQ(expect, actual);
        }
    }
```

一般にFactory関数はヒープを使用してオブジェクトを生成する場合が多いため、
それを例示する目的でXxxDataFormatterFactoryもヒープを使用している。

この例ではその必要はないため、ヒープを使用しないFactory関数の例を下記する。

```cpp
    // @@@ example/design_pattern/template_method.cpp 126

    XxxDataFormatterIF const& XxxDataFormatterFactory2(XxxDataFormatterMethod method) noexcept
    {
        static auto xml   = XxxDataFormatterXml{};
        static auto csv   = XxxDataFormatterCsv{};
        static auto table = XxxDataFormatterTable{};

        switch (method) {
        case XxxDataFormatterMethod::Xml:
            return xml;
        case XxxDataFormatterMethod::Csv:
            return csv;
        case XxxDataFormatterMethod::Table:
            return table;
        default:
            assert(false);
            return xml;
        }
    }
```

次に示すのは、このパターンを使用して、プリプロセッサ命令を排除するリファクタリングの例である。

まずは、出荷仕分け向けのプリプロセッサ命令をロジックの内部に記述している問題のあるコードを示す。
このようなオールドスタイルなコードは様々な開発阻害要因になるため、避けるべきである。

```cpp
    // in shipping.h

    #define SHIP_TO_JAPAN 1
    #define SHIP_TO_US 2
    #define SHIP_TO_EU 3

    class ShippingOp {
    public:
        virtual int32_t DoSomething() = 0;
        virtual ~ShippingOp()         = default;
    };
```
```cpp
    // in shipping_japan.h

    class ShippingOp_Japan : public ShippingOp {
    public:
        ShippingOp_Japan();
        int32_t DoSomething() override;
        ~ShippingOp_Japan() override;

    private:
        // 何らかの宣言
    };
```
```cpp
    // in xxx.cpp 仕分けに依存した処理

    // SHIPPINGはmake等のビルドツールから渡される

    #if SHIPPING == SHIP_TO_JAPAN
        auto shipping = ShippingOp_Japan{};
    #elif SHIPPING == SHIP_TO_US
        auto shipping = ShippingOp_US{};
    #elif SHIPPING == SHIP_TO_EU
        auto shipping = ShippingOp_EU{};
    #else
    #error "SHIPPING must be defined"
    #endif

        shipping.DoSomething();
```

このコードは、
関数テンプレートの特殊化を利用したFactoryを以下のように定義することで改善することができる。

```cpp
    // in shipping.h

    // ShippingOpクラスは改善前のコードと同じ

    enum class ShippingRegion { Japan, US, EU };

    template <ShippingRegion>
    std::unique_ptr<ShippingOp> ShippingOpFactory();  // ShippingOpFactory特殊化のための宣言

    template <>
    std::unique_ptr<ShippingOp> ShippingOpFactory<ShippingRegion::Japan>();  // 特殊化関数の宣言

    template <>
    std::unique_ptr<ShippingOp> ShippingOpFactory<ShippingRegion::US>();  // 特殊化関数の宣言

    template <>
    std::unique_ptr<ShippingOp> ShippingOpFactory<ShippingRegion::EU>();  // 特殊化関数の宣言
```
```cpp
    // in shipping_japan.cpp
    // ファクトリーの効果で、ShippingOp_Japanは外部への公開が不要

    class ShippingOp_Japan : public ShippingOp {
    public:
        ShippingOp_Japan();
        int32_t DoSomething() override;
        ~ShippingOp_Japan() override;

    private:
        // 何らかの宣言
    };

    template <>
    std::unique_ptr<ShippingOp> ShippingOpFactory<ShippingRegion::Japan>()
    {
        return std::unique_ptr<ShippingOp>{new ShippingOp_Japan};
    }
```
```cpp
    // in xxx.cpp 仕分けに依存した処理

    // SHIPPINGはmake等のビルドツールからShippingRegionのいづれかとして渡される
    auto shipping = ShippingOpFactory<SHIPPING>();

    shipping->DoSomething();
```

もしくは、
関数オーバーロードを利用したFactoryを以下のように定義することで改善することもできる。

```cpp
    // in shipping.h

    // ShippingOpクラスは改善前のコードと同じ

    enum class ShippingRegion { Japan, US, EU };

    template <ShippingRegion R>
    class ShippingRegion2Type : std::integral_constant<ShippingRegion, R> {
    };

    using ShippingRegionType_Japan = ShippingRegion2Type<ShippingRegion::Japan>;
    using ShippingRegionType_US    = ShippingRegion2Type<ShippingRegion::US>;
    using ShippingRegionType_EU    = ShippingRegion2Type<ShippingRegion::EU>;

    std::unique_ptr<ShippingOp> ShippingOpFactory(ShippingRegionType_Japan);
    std::unique_ptr<ShippingOp> ShippingOpFactory(ShippingRegionType_US);
    std::unique_ptr<ShippingOp> ShippingOpFactory(ShippingRegionType_EU);
```
```cpp
    // in shipping_japan.cpp
    // ファクトリーの効果で、ShippingOp_Japanは外部への公開が不要

    class ShippingOp_Japan : public ShippingOp {
    public:
        ShippingOp_Japan();
        int32_t DoSomething() override;
        ~ShippingOp_Japan() override;

    private:
        // 何らかの宣言
    };

    std::unique_ptr<ShippingOp> ShippingOpFactory(ShippingRegionType_Japan)
    {
        return std::unique_ptr<ShippingOp>{new ShippingOp_Japan};
    }
```
```cpp
    // in xxx.cpp 仕分けに依存した処理

    // SHIPPINGはmake等のビルドツールからShippingRegionのいづれかとして渡される
    auto shipping = ShippingOpFactory(ShippingRegion2Type<SHIPPING>{});

    shipping->DoSomething();
```


## Named Constructor <a id="SS_3_17"></a>
Named Connstructorは、[Singleton](design_pattern.md#SS_3_12)のようなオブジェクトを複数、生成するためのパターンである。

```cpp
    // @@@ example/design_pattern/enum_operator.h 82

    class Mammals : public Animal {  // 哺乳類
    public:
        static Mammals& Human() noexcept
        {
            static auto inst = Mammals{PhisicalAbility::Run | PhisicalAbility::Swim};
            return inst;
        }

        static Mammals& Bat() noexcept
        {
            static auto inst = Mammals{PhisicalAbility::Run | PhisicalAbility::Fly};
            return inst;
        }

        static Mammals& Whale() noexcept
        {
            static auto inst = Mammals{PhisicalAbility::Swim};
            return inst;
        }

        bool Act();

    private:
        Mammals(PhisicalAbility pa) noexcept : Animal{pa} {}
    };
```

上記例のHuman()、Bat()、Whale()は、人、コウモリ、クジラに対応するクラスMammalsオブジェクトを返す。

次に示したのは「[Factory](design_pattern.md#SS_3_16)」の例にこのパターンを適応したコードである。

```cpp
    // @@@ example/design_pattern/template_method.h 16

    /// @class XxxDataFormatterIF
    /// @brief data_storer_if.cppに定義すべきだが、サンプルであるため便宜上同じファイルで定義する
    ///        データフォーマットを行うクラスのインターフェースクラス
    class XxxDataFormatterIF {
    public:
        explicit XxxDataFormatterIF(std::string_view formatter_name) noexcept
            : formatter_name_{formatter_name}
        {
        }
        virtual ~XxxDataFormatterIF() = default;

        static XxxDataFormatterIF const& Xml() noexcept;
        static XxxDataFormatterIF const& Csv() noexcept;
        static XxxDataFormatterIF const& Table() noexcept;

        ...
    };
```

```cpp
    // @@@ example/design_pattern/template_method.cpp 147

    XxxDataFormatterIF const& XxxDataFormatterIF::Xml() noexcept
    {
        static auto xml = XxxDataFormatterXml{};

        return xml;
    }

    XxxDataFormatterIF const& XxxDataFormatterIF::Csv() noexcept
    {
        static auto csv = XxxDataFormatterCsv{};

        return csv;
    }

    XxxDataFormatterIF const& XxxDataFormatterIF::Table() noexcept
    {
        static auto table = XxxDataFormatterTable{};

        return table;
    }
```

これまでにXxxDataFormatterIFオブジェクトを取得するパターンを以下のように3つ示した。

1. Factory関数によってstd::unique_ptr\<XxxDataFormatterIF>オブジェクトを返す。
2. Factory関数によってstaticなXxxDataFormatterIFオブジェクトを返す。
3. Named ConstructorによってstaticなXxxDataFormatterIFオブジェクトを返す。

最も汎用的な方法はパターン1であるが、
上記例のようにオブジェクトが状態を持たない場合、これは過剰な方法であり、
パターン3が最適であるように思える。このような考察からわかるように、
(単にnewする場合も含めて)オブジェクトの取得にどのような方法を用いるかは、
クラスの性質に依存する。


## Proxy <a id="SS_3_18"></a>
Proxyとは代理人という意味で、
本物のクラスに代わり代理クラス(Proxy)が処理を受け取る
(実際は、処理自体は本物クラスに委譲されることもある)パターンである。

以下の順番で例を示すことで、Proxyパターンの説明を行う。

1. 内部構造を外部公開しているサーバ クラス
2. そのサーバをラッピングして、使いやすくしたサーバ クラス(Facadeパターン)
3. サーバをラップしたクラスのProxyクラス

まずは、内部構造を外部公開しているの醜悪なサーバの実装例である。

```cpp
    // @@@ example/design_pattern/bare_server.h 5

    enum class Cmd {
        SayHello,
        SayGoodbye,
        Shutdown,
    };

    struct Packet {
        Cmd cmd;
    };

    class BareServer final {
    public:
        BareServer() noexcept;
        ~BareServer();
        int GetPipeW() const noexcept  // クライアントのwrite用
        {
            return to_server_[1];
        }

        int GetPipeR() const noexcept  // クライアントのread用
        {
            return to_client_[0];
        }

        void Start();
        void Wait() noexcept;

    private:
        int         to_server_[2];  // サーバへの通信用
        int         to_client_[2];  // クライアントへの通信用
        std::thread thread_;
    };
```

```cpp
    // @@@ example/design_pattern/bare_server.cpp 9

    namespace {
    bool cmd_dispatch(int wfd, Cmd cmd) noexcept
    {
        static char const hello[]   = "Hello";
        static char const goodbye[] = "Goodbye";

        switch (cmd) {
        case Cmd::SayHello:
            write(wfd, hello, sizeof(hello));
            break;
        case Cmd::SayGoodbye:
            write(wfd, goodbye, sizeof(goodbye));
            break;
        case Cmd::Shutdown:
        default:
            std::cout << "Shutdown" << std::endl;
            return false;
        }

        return true;
    }

    void thread_entry(int rfd, int wfd) noexcept
    {
        for (;;) {
            auto packet = Packet{};

            if (read(rfd, &packet, sizeof(packet)) < 0) {
                continue;
            }

            if (!cmd_dispatch(wfd, packet.cmd)) {
                break;
            }
        }
    }
    }  // namespace

    BareServer::BareServer() noexcept : to_server_{-1, -1}, to_client_{-1, -1}, thread_{}
    {
        auto ret = pipe(to_server_);
        assert(ret >= 0);

        ret = pipe(to_client_);
        assert(ret >= 0);
    }

    BareServer::~BareServer()
    {
        close(to_server_[0]);
        close(to_server_[1]);
        close(to_client_[0]);
        close(to_client_[1]);
    }

    void BareServer::Start()
    {
        thread_ = std::thread{thread_entry, to_server_[0], to_client_[1]};
        std::cout << "thread started !!!" << std::endl;
    }

    void BareServer::Wait() noexcept { thread_.join(); }
```

下記は、上記BareServerを使用するクライアントの実装例である。通信がpipe()によって行われ、
その中身がPacket{}であること等、不要な依存関係をbare_client()に強いていることがわかる。
このような構造は、機能追加、保守作業を非効率、困難にするアンチパターンである。

```cpp
    // @@@ example/design_pattern/proxy_ut.cpp 17

    /// @fn bare_client
    /// @brief 非同期サービスを隠蔽していないBareServerを使用したときのクライアントの例
    std::vector<std::string> bare_client(BareServer& bs)
    {
        auto const wfd = bs.GetPipeW();
        auto const rfd = bs.GetPipeR();
        auto       ret = std::vector<std::string>{};

        bs.Start();

        auto packet = Packet{};
        char buffer[30];

        packet.cmd = Cmd::SayHello;
        write(wfd, &packet, sizeof(packet));

        auto read_ret = read(rfd, buffer, sizeof(buffer));
        assert(read_ret > 0);

        ret.emplace_back(buffer);

        packet.cmd = Cmd::SayGoodbye;
        write(wfd, &packet, sizeof(packet));

        read_ret = read(rfd, buffer, sizeof(buffer));
        assert(read_ret > 0);

        ret.emplace_back(buffer);

        packet.cmd = Cmd::Shutdown;
        write(wfd, &packet, sizeof(packet));

        bs.Wait();

        return ret;
    }
```

次に、このむき出しの構造をラッピングする例を示す(このようなラッピングをFacadeパターンと呼ぶ)。

```cpp
    // @@@ example/design_pattern/bare_server_wrapper.h 6

    enum class Cmd;  // C++11からenumは前方宣言できる。
    class BareServer;

    class BareServerWrapper final {
    public:
        BareServerWrapper();

        void        Start();
        std::string SayHello();
        std::string SayGoodbye();
        void        Shutdown() noexcept;

    private:
        void                        send_message(enum Cmd cmd) noexcept;
        std::unique_ptr<BareServer> bare_server_;
    };
```

```cpp
    // @@@ example/design_pattern/bare_server_wrapper.cpp 8

    BareServerWrapper::BareServerWrapper() : bare_server_{std::make_unique<BareServer>()} {}

    void BareServerWrapper::Start() { bare_server_->Start(); }

    void BareServerWrapper::send_message(enum Cmd cmd) noexcept
    {
        auto packet = Packet{cmd};

        write(bare_server_->GetPipeW(), &packet, sizeof(packet));
    }

    std::string BareServerWrapper::SayHello()
    {
        char buffer[30];

        send_message(Cmd::SayHello);
        read(bare_server_->GetPipeR(), buffer, sizeof(buffer));

        return buffer;
    }

    std::string BareServerWrapper::SayGoodbye()
    {
        char buffer[30];

        send_message(Cmd::SayGoodbye);
        read(bare_server_->GetPipeR(), buffer, sizeof(buffer));

        return buffer;
    }

    void BareServerWrapper::Shutdown() noexcept
    {
        send_message(Cmd::Shutdown);

        bare_server_->Wait();
    }
```

下記は、上記BareServerWrapperのクライアントの実装例である。
BareServerWrapperがむき出しの通信をラップしたことで、bare_wrapper_client()は、
bare_client()に比べてシンプルになったことがわかる。

```cpp
    // @@@ example/design_pattern/proxy_ut.cpp 57

    /// @fn bare_wrapper_client
    /// @brief BareServerを使いやすくラップしたBareServerWrapperを使用したときのクライアントの例
    std::vector<std::string> bare_wrapper_client(BareServerWrapper& bsw)
    {
        auto ret = std::vector<std::string>{};

        bsw.Start();

        ret.emplace_back(bsw.SayHello());

        ret.emplace_back(bsw.SayGoodbye());

        bsw.Shutdown();

        return ret;
    }
```

次の例は、BareServerとBareServerWrapperを統合し、
さらに全体をシンプルにリファクタリングしたWrappedServerである。
Packet{}やpipe等の通信の詳細がwrapped_server.cppの無名名前空間に閉じ込められ、
クラスの隠蔽性が強化されたことで、より機能追加、保守が容易になった。

```cpp
    // @@@ example/design_pattern/wrapped_server.h 5

    class WrappedServer {
    public:
        WrappedServer() noexcept;
        virtual ~WrappedServer();

        void        Start();
        std::string SayHello() { return say_hello(); }
        std::string SayGoodbye() { return say_goodbye(); }
        void        Shutdown() noexcept;

    protected:
        virtual std::string say_hello();    // 後で拡張するためにvirtual
        virtual std::string say_goodbye();  // 同上

    private:
        int         to_server_[2];
        int         to_client_[2];
        std::thread thread_;
    };
```

```cpp
    // @@@ example/design_pattern/wrapped_server.cpp 8

    namespace {
    enum class Cmd {
        ...
    };

    struct Packet {
        Cmd cmd;
    };
    }  // namespace

    // 以下、bare_server_wrapper.cppのコードとほぼ同じであるため省略。

    ...
```

WrappedServerの使用例を下記する。当然ながらbare_wrapper_client()とほぼ同様になる。

```cpp
    // @@@ example/design_pattern/proxy_ut.cpp 77

    /// @fn wrapped_client
    /// @brief 非同期サービスを隠蔽しているWrappedServerを使用したときのクライアントの例
    std::vector<std::string> wrapped_client(WrappedServer& ws)
    {
        auto ret = std::vector<std::string>{};

        ws.Start();

        ret.emplace_back(ws.SayHello());

        ret.emplace_back(ws.SayGoodbye());

        ws.Shutdown();

        return ret;
    }
```

WrappedServerが提供する機能はスレッド間通信を含むため処理コストが高い。
その対策として、サーバから送られてきた文字列をキャッシュするクラス(Proxyパターン)の導入により、
そのコストを削減する例を下記する。

```cpp
    // @@@ example/design_pattern/wrapped_server_proxy.h 7

    class WrappedServerProxy final : public WrappedServer {
    public:
        WrappedServerProxy() = default;

    private:
        std::string         hello_cashe_{};
        virtual std::string say_hello() override;
        virtual std::string say_goodbye() override;
    };
```

```cpp
    // @@@ example/design_pattern/wrapped_server_proxy.cpp 7

    std::string WrappedServerProxy::say_hello()
    {
        if (hello_cashe_.size() == 0) {
            hello_cashe_ = WrappedServer::say_hello();  // キャッシュとし保存
        }

        return hello_cashe_;
    }

    std::string WrappedServerProxy::say_goodbye()
    {
        hello_cashe_ = std::string{};  // helloキャッシュをクリア

        return WrappedServer::say_goodbye();
    }
```

下記図のようにWrappedServerProxyはWrappedServerからのパブリック継承であるため、
WrappedServerのクライアントは、そのままWrappedServerProxyのクライアントとして利用できる。

<!-- pu:plant_uml/proxy.pu--><p><img src="data:image/png;base64,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" /></p>

なお、正確には下記のようなクラス構造をProxyパターンと呼ぶことが多いが、
ここでは単純さを優先した。

<!-- pu:plant_uml/proxy_general.pu--><p><img src="data:image/png;base64,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" /></p>


## Strategy <a id="SS_3_19"></a>
関数f(args)の振る舞いが、

* 全体の制御
* 部分的な振る舞い(何らかの条件を探す等)

に分けられるような場合、関数fを

* 「全体の制御」を行う関数g
* 「部分的な振る舞い」を規定するStrategyオブジェクト(関数へのポインタ、関数オブジェクト、ラムダ式)

に分割し、下記のように、Strategyオブジェクトをgの引数として外部から渡せるようにしたパターンである
(std::sort()のようなパターン)。

```cpp
    g(args, Strategyオブジェクト)
```

Strategyオブジェクトにいろいろなバリエーションがある場合、このパターンを使うと良い。
なお、このパターンの対象はクラスになる場合もある。

「ディレクトリをリカーシブに追跡し、引数で指定された属性にマッチしたファイルの一覧を返す関数」
を開発することを要求されたとする。

まずは、拡張性のない実装例を示す。

```cpp
    // @@@ example/design_pattern/find_files_old_style.h 4

    /// @enum FindCondition
    /// find_files_recursivelyの条件
    enum class FindCondition {
        File,              ///< pathがファイル
        Dir,               ///< pathがディレクトリ
        FileNameHeadIs_f,  ///< pathがファイル且つ、そのファイル名の先頭が"f"
    };
```

```cpp
    // @@@ example/design_pattern/find_files_old_style.cpp 9

    /// @fn std::vector<std::string> find_files_recursively(std::string const& path,
    ///                                                     FindCondition condition)
    /// @brief 条件にマッチしたファイルをリカーシブに探して返す
    /// @param path      リカーシブにディレクトリをたどるための起点となるパス
    /// @param condition どのようなファイルかを指定する
    /// @return 条件にマッチしたファイルをstd::vector<std::string>で返す
    std::vector<std::string> find_files_recursively(std::string const& path, FindCondition condition)
    {
        auto files = std::vector<fs::path>{};

        // recursive_directory_iteratorはファイルシステム依存するため、その依存を排除する他の処理
        std::copy(fs::recursive_directory_iterator{path}, fs::recursive_directory_iterator{},
                  std::back_inserter(files));

        std::sort(files.begin(), files.end());

        auto ret = std::vector<std::string>{};

        std::for_each(files.begin(), files.end(), [&](fs::path const& p) noexcept {
            auto is_match = false;

            switch (condition) {
            case FindCondition::File:
                if (fs::is_regular_file(p)) {
                    is_match = true;
                }
                break;
            case FindCondition::Dir:
                if (fs::is_directory(p)) {
                    is_match = true;
                }
                break;
                ...
            }

            if (is_match) {
                ret.emplace_back(p.generic_string());
            }
        });

        return ret;
    }
```

```cpp
    // @@@ example/design_pattern/find_files_ut.cpp 29

    TEST(Strategy, old_style)
    {
        assure_test_files_exist();  // test用のファイルがあることの確認

        auto const files_actual = find_files_recursively(test_dir, FindCondition::File);
        auto const files_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir0/gile3",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0",
            test_dir + "gile1"
        });
        ASSERT_EQ(files_expect, files_actual);

        auto const dirs_actual = find_files_recursively(test_dir, FindCondition::Dir);
        auto const dirs_expect = sort(std::vector{
            test_dir + "dir0",
            test_dir + "dir1",
            test_dir + "dir1/dir2"
        });
        ASSERT_EQ(dirs_expect, dirs_actual);

        auto const f_actual = find_files_recursively(test_dir, FindCondition::FileNameHeadIs_f);
        auto const f_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0"
        });
        ASSERT_EQ(f_expect, f_actual);
    }
```

この関数は、見つかったファイルが「引数で指定された属性」にマッチするかどうかを検査する。
検査は、「引数で指定された属性」に対するswitch文によって行われる。
これにより、この関数は「引数で指定された属性」の変更に強く影響を受ける。

下記は、この関数にStrategyパターンを適用したものである。

```cpp
    // @@@ example/design_pattern/find_files_strategy.h 7

    /// @typedef find_condition
    /// @brief find_files_recursively仮引数conditionの型(関数オブジェクトの型)
    using find_condition = std::function<bool(std::filesystem::path const&)>;

    // Strategyパターン
    /// @fn std::vector<std::string> find_files_recursively(std::string const& path,
    ///                                                     find_condition     condition);
    /// @brief 条件にマッチしたファイルをリカーシブに探索して返す
    /// @param path      リカーシブにディレクトリを辿るための起点となるパス
    /// @param condition 探索するファイルの条件
    /// @return 条件にマッチしたファイルをstd::vector<std::string>で返す
    extern std::vector<std::string> find_files_recursively(std::string const& path,
                                                           find_condition     condition);
```

```cpp
    // @@@ example/design_pattern/find_files_strategy.cpp 6

    std::vector<std::string> find_files_recursively(std::string const& path, find_condition condition)
    {
        namespace fs = std::filesystem;

        auto files = std::vector<fs::path>{};

        // recursive_directory_iteratorはファイルシステム依存するため、その依存を排除する他の処理
        std::copy(fs::recursive_directory_iterator{path}, fs::recursive_directory_iterator{},
                  std::back_inserter(files));

        std::sort(files.begin(), files.end());

        auto ret = std::vector<std::string>{};

        std::for_each(files.cbegin(), files.cend(), [&](fs::path const& p) {
            if (condition(p)) {
                ret.emplace_back(p.generic_string());
            }
        });

        return ret;
    }
```

```cpp
    // @@@ example/design_pattern/find_files_ut.cpp 69

    TEST(Strategy, strategy_lamda)
    {
        namespace fs = std::filesystem;

        assure_test_files_exist();  // test用のファイルがあることの確認

        // ラムダ式で実装
        auto const files_actual = find_files_recursively(
            test_dir, [](fs::path const& p) noexcept { return fs::is_regular_file(p); });

        auto const files_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir0/gile3",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0",
            test_dir + "gile1"
        });
        ASSERT_EQ(files_expect, files_actual);

        auto const dirs_actual = find_files_recursively(
            test_dir, [](fs::path const& p) noexcept { return fs::is_directory(p); });
        auto const dirs_expect = sort(std::vector{
            test_dir + "dir0",
            test_dir + "dir1",
            test_dir + "dir1/dir2"
        });
        ASSERT_EQ(dirs_expect, dirs_actual);

        auto const f_actual = find_files_recursively(test_dir, [](fs::path const& p) noexcept {
            return p.filename().generic_string()[0] == 'f';
        });

        auto const f_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0"
        });
        ASSERT_EQ(f_expect, f_actual);
    }

    /// @fn bool condition_func(std::filesystem::path const& path)
    /// @brief find_files_recursivelyの第2仮引数に渡すためのファイル属性を決める関数
    bool condition_func(std::filesystem::path const& path)
    {
        return path.filename().generic_string().at(0) == 'f';
    }

    TEST(Strategy, strategy_func_pointer)
    {
        assure_test_files_exist();  // test用のファイルがあることの確認

        // FindCondition::FileNameHeadIs_fで行ったことを関数ポインタで実装。
        auto const f_actual = find_files_recursively(test_dir, condition_func);
        auto const f_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0"
        });
        ASSERT_EQ(f_expect, f_actual);
    }

    /// @class ConditionFunctor
    /// @brief
    ///  find_files_recursivelyの第2仮引数に渡すためのファイル属性を決める関数オブジェクトクラス。
    ///  検索条件に状態が必要な場合、関数オブジェクトを使うとよい。
    class ConditionFunctor {
    public:
        ConditionFunctor()  = default;
        ~ConditionFunctor() = default;

        /// @fn bool operator()(std::filesystem::path const& path)
        /// @brief 先頭が'f'のファイルを最大2つまで探す
        bool operator()(std::filesystem::path const& path)
        {
            if (path.filename().generic_string().at(0) != 'f') {
                return false;
            }

            return ++count_ < 3;
        }

    private:
        int32_t count_{0};
    };

    TEST(Strategy, strategy_func_obj)
    {
        // 条件に状態が必要な場合(この例では最大2つまでを判断するのに状態が必要)、
        // 関数ポインタより、ファンクタの方が便利。
        auto const f_actual = find_files_recursively(test_dir, ConditionFunctor{});
        auto const f_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir1/dir2/file4",
        });
        ASSERT_EQ(f_expect, f_actual);
    }
```

捜査対象のファイル属性の指定をfind_files_recursively()の外に出しため、
その属性の追加に対して「[オープン・クローズドの原則(OCP)](solid.md#SS_2_2)」に対応した構造となった。

なお、上記find_files_recursivelyの第2パラメータをテンプレートパラメータとすることで、

```cpp
    // @@@ example/design_pattern/find_files_strategy.h 23

    template <typename F>  // Fはファンクタ
    auto find_files_recursively2(std::string const& path, F condition)
        -> std::enable_if_t<std::is_invocable_r_v<bool, F, std::filesystem::path const&>,
                            std::vector<std::string>>
    {
        namespace fs = std::filesystem;

        auto files = std::vector<fs::path>{};

        // recursive_directory_iteratorはファイルシステム依存するため、その依存を排除する他の処理
        std::copy(fs::recursive_directory_iterator{path}, fs::recursive_directory_iterator{},
                  std::back_inserter(files));

        std::sort(files.begin(), files.end());

        auto ret = std::vector<std::string>{};

        std::for_each(files.cbegin(), files.cend(), [&](fs::path const& p) {
            if (condition(p)) {
                ret.emplace_back(p.generic_string());
            }
        });

        return ret;
    }
```

のように書くこともできる。

次に示すのは、このパターンを使用して、プリプロセッサ命令を排除するリファクタリングの例である。

まずは、出荷仕分け向けのプリプロセッサ命令をロジックの内部に記述している問題のあるコードを示す。
このようなオールドスタイルなコードは様々な開発阻害要因になるため、避けるべきである。

```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 11

    class X {
    public:
        X() = default;

        int32_t DoSomething()
        {
            int32_t ret{0};

    #if SHIPPING == SHIP_TO_JAPAN
            // 日本向けの何らかの処理
    #elif SHIPPING == SHIP_TO_US
            // US向けの何らかの処理
    #elif SHIPPING == SHIP_TO_JAPAN
            // EU向けの何らかの処理
    #else
    #error "SHIPPING must be defined"
    #endif
            return ret;
        }

    private:
        // 何らかの宣言
    };
```
```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 43

    X x;

    x.DoSomething();
```

このコードは、Strategyを使用し以下のようにすることで、改善することができる。

```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 56

    class ShippingOp {
    public:
        virtual int32_t DoSomething() = 0;
        virtual ~ShippingOp()         = default;
    };

    class X {
    public:
        X() = default;

        int32_t DoSomething(ShippingOp& shipping)
        {
            int32_t ret = shipping.DoSomething();

            // 何らかの処理

            return ret;
        }

    private:
        // 何らかの宣言
    };
```
```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 81

    class ShippingOp_Japan : public ShippingOp {
    public:
        ShippingOp_Japan();
        int32_t DoSomething() override;
        ~ShippingOp_Japan() override;

    private:
        // 何らかの宣言
    };
```
```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 100

    X                x;
    ShippingOp_Japan sj;

    x.DoSomething(sj);
```

あるいは、[DI(dependency injection)](design_pattern.md#SS_3_11)と組み合わせて、下記のような改善も有用である。

```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 112

    class ShippingOp {
    public:
        virtual int32_t DoSomething() = 0;
        virtual ~ShippingOp()         = default;
    };

    class X {
    public:
        explicit X(std::unique_ptr<ShippingOp> shipping) : shipping_{std::move(shipping)} {}

        int32_t DoSomething()
        {
            int32_t ret = shipping_->DoSomething();

            // 何らかの処理

            return ret;
        }

    private:
        std::unique_ptr<ShippingOp> shipping_;
        // 何らかの宣言
    };
```
```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 138

    class ShippingOp_Japan : public ShippingOp {
    public:
        ShippingOp_Japan();
        int32_t DoSomething() override;
        ~ShippingOp_Japan() override;

    private:
        // 何らかの宣言
    };
```
```cpp
    // @@@ example/design_pattern/strategy_shipping_ut.cpp 157

    X x{std::unique_ptr<ShippingOp>(new ShippingOp_Japan)};

    x.DoSomething();
```


## Visitor <a id="SS_3_20"></a>
このパターンは、クラス構造とそれに関連するアルゴリズムを分離するためのものである。

最初に
「クラス構造とそれに関連するアルゴリズムは分離できているが、
それ以前にオブジェクト指向の原則に反している」
例を示す。

```cpp
    // @@@ example/design_pattern/visitor.cpp 42

    /// @class FileEntity
    /// @brief
    ///  ファイルシステムの構成物(ファイル、ディレクトリ等)を表すクラスの基底クラス
    class FileEntity {
    public:
        explicit FileEntity(std::string pathname) : pathname_{std::move(pathname)} {}
        virtual ~FileEntity() {}
        std::string const& Pathname() const { return pathname_; }

        ...

    private:
        std::string const pathname_;
    };

    class File final : public FileEntity {
        ...
    };

    class Dir final : public FileEntity {
        ...
    };

    class OtherEntity final : public FileEntity {
        ...
    };

    class Printer {
    public:
        static void PrintPathname1(FileEntity const& file_entity)
        {
            if (typeid(File) == typeid(file_entity)) {
                std::cout << file_entity.Pathname();
            }
            else if (typeid(Dir) == typeid(file_entity)) {
                std::cout << file_entity.Pathname() + "/";
            }
            else if (typeid(OtherEntity) == typeid(file_entity)) {
                std::cout << file_entity.Pathname() + "(o1)";
            }
            else {
                assert(false);
            }
        }

        static void PrintPathname2(FileEntity const& file_entity)
        {
            if (typeid(File) == typeid(file_entity)) {
                std::cout << file_entity.Pathname();
            }
            else if (typeid(Dir) == typeid(file_entity)) {
                std::cout << find_files(file_entity.Pathname());
            }
            else if (typeid(OtherEntity) == typeid(file_entity)) {
                std::cout << file_entity.Pathname() + "(o2)";
            }
            else {
                assert(false);
            }
        }
    };
```

下記クラス図からもわかる通り、ポリモーフィズムに反したこのような構造は複雑な依存関係を作り出す。
このアンチパターンにより同型の条件文が2度出てきてしまうため、
Printerのアルゴリズム関数が増えれば、この繰り返しはそれに比例して増える。
またFileEntityの派生が増えれば、それら条件文はすべて影響を受ける。
このようなソースコードは、このようにして等比級数的に複雑化する。

<!-- pu:plant_uml/visitor_ng1.pu--><p><img src="data:image/png;base64,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" /></p>

これをポリモーフィズムの導入で解決した例を示す。

```cpp
    // @@@ example/design_pattern/visitor.cpp 143

    class FileEntity {
    public:
        explicit FileEntity(std::string pathname) : pathname_{std::move(pathname)} {}
        ...
        virtual void PrintPathname1() const = 0;
        virtual void PrintPathname2() const = 0;

    private:
        std::string const pathname_;
    };

    class File final : public FileEntity {
    public:
        ...
        virtual void PrintPathname1() const override { std::cout << Pathname(); }
        virtual void PrintPathname2() const override { std::cout << Pathname(); }
    };

    class Dir final : public FileEntity {
    public:
        ...
        virtual void PrintPathname1() const override { std::cout << Pathname() + "/"; }
        virtual void PrintPathname2() const override { std::cout << find_files(Pathname()); }
    };

    class OtherEntity final : public FileEntity {
    public:
        ...
        virtual void PrintPathname1() const override { std::cout << Pathname() + "(o1)"; }
        virtual void PrintPathname2() const override { std::cout << Pathname() + "(o2)"; }
    };

    class Printer {
    public:
        static void PrintPathname1(FileEntity const& file_entity) { file_entity.PrintPathname1(); }
        static void PrintPathname2(FileEntity const& file_entity) { file_entity.PrintPathname2(); }
    };
```

上記例では、PrinterのアルゴリズムをFileEntityの各派生クラスのメンバ関数で実装することで、
Printerの各関数は単純化された。

<!-- pu:plant_uml/visitor_ng2.pu--><p><img src="data:image/png;base64,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" /></p>

これはポリモーフィズムによるリファクタリングの良い例と言えるが、
SRP(「[単一責任の原則(SRP)](solid.md#SS_2_1)」)に反するため、
Printerの関数が増えるたびにPrintPathname1、
PrintPathname2のようなFileEntityのインターフェースが増えてしまう。

このようなインターフェースの肥大化に対処するパターンがVisitorである。

上記例にVisitorを適用してリファクタリングした例を示す。

```cpp
    // @@@ example/design_pattern/visitor.h 9

    class FileEntityVisitor {
    public:
        virtual void Visit(File const&)        = 0;
        virtual void Visit(Dir const&)         = 0;
        virtual void Visit(OtherEntity const&) = 0;
        ...
    };

    class FileEntity {
    public:
        explicit FileEntity(std::string pathname) : pathname_{std::move(pathname)} {}
        ...
        std::string const& Pathname() const { return pathname_; }

        virtual void Accept(FileEntityVisitor&) const = 0;  // Acceptの仕様は安定しているので
                                                            // NVIは使わない。
    private:
        std::string const pathname_;
    };

    class File final : public FileEntity {
    public:
        using FileEntity::FileEntity;
        virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*this); }
    };

    class Dir final : public FileEntity {
    public:
        using FileEntity::FileEntity;
        virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*this); }
    };

    class OtherEntity final : public FileEntity {
    public:
        using FileEntity::FileEntity;
        virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*this); }
    };

    class PathnamePrinter1 final : public FileEntityVisitor {
    public:
        virtual void Visit(File const&) override;
        virtual void Visit(Dir const&) override;
        virtual void Visit(OtherEntity const&) override;
    };

    class PathnamePrinter2 final : public FileEntityVisitor {
    public:
        virtual void Visit(File const&) override;
        virtual void Visit(Dir const&) override;
        virtual void Visit(OtherEntity const&) override;
    };
```

```cpp
    // @@@ example/design_pattern/visitor.cpp 219

    void PathnamePrinter1::Visit(File const& file) { std::cout << file.Pathname(); }
    void PathnamePrinter1::Visit(Dir const& dir) { std::cout << dir.Pathname() + "/"; }
    void PathnamePrinter1::Visit(OtherEntity const& other) { std::cout << other.Pathname() + "(o1)"; }

    void PathnamePrinter2::Visit(File const& file) { std::cout << file.Pathname(); }
    void PathnamePrinter2::Visit(Dir const& dir) { std::cout << find_files(dir.Pathname()); }
    void PathnamePrinter2::Visit(OtherEntity const& other) { std::cout << other.Pathname() + "(o2)"; }

    class Printer {
    public:
        static void PrintPathname1(FileEntity const& file_entity)
        {
            auto visitor = PathnamePrinter1{};

            file_entity.Accept(visitor);
        }

        static void PrintPathname2(FileEntity const& file_entity)
        {
            auto visitor = PathnamePrinter2{};

            file_entity.Accept(visitor);
        }
    };
```

上記クラスの関係は下記のようになる。

<!-- pu:plant_uml/visitor_ok.pu--><p><img src="data:image/png;base64,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" /></p>

このリファクタリングには、

* FileEntityのインターフェースを小さくできる
* FileEntityVisitorから派生できるアルゴリズムについては、
  FileEntityのインターフェースに影響を与えずに追加できる
  (「[オープン・クローズドの原則(OCP)](solid.md#SS_2_2)」参照)

という利点がある。
一方で、この程度の複雑さの(単純な)例では、Visitorの適用によって以前よりも構造が複雑になり、
改悪してしまった可能性があるため、デザインパターンを使用する場合には注意が必要である。

なお、上記の抜粋である下記コード

```cpp
    // @@@ example/design_pattern/visitor.h 39

    virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*this); }
```

はコードクローンだが、thisの型が違うため、
各Acceptが呼び出すFileEntityVisitor::Visit()も異り、単純に統一することはできない。
これを改めるためには、「[CRTP(curiously recurring template pattern)](design_pattern.md#SS_3_21)」が必要になる。

次に示すソースコードはVisitorとは関係がないが、
FileEntityVisitorから派生するクラスを下記クラス図が示すように改善することで、
単体テストが容易になる例である(「[DI(dependency injection)](design_pattern.md#SS_3_11)」参照)。

<!-- pu:plant_uml/visitor_ut.pu--><p><img src="data:image/png;base64,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" /></p>

```cpp
    // @@@ example/design_pattern/visitor.h 72

    class TestablePrinter : public FileEntityVisitor {
    public:
        explicit TestablePrinter(std::ostream& os) : ostream_{os} {}

    protected:
        std::ostream& ostream_;
    };

    class TestablePathnamePrinter1 final : public TestablePrinter {
    public:
        explicit TestablePathnamePrinter1(std::ostream& os) : TestablePrinter{os} {}
        virtual void Visit(File const& file) override;
        virtual void Visit(Dir const& dir) override;
        virtual void Visit(OtherEntity const& other) override;
    };

    class TestablePathnamePrinter2 final : public TestablePrinter {
    public:
        explicit TestablePathnamePrinter2(std::ostream& os) : TestablePrinter{os} {}
        virtual void Visit(File const& file) override;
        virtual void Visit(Dir const& dir) override;
        virtual void Visit(OtherEntity const& other) override;
    };
```

```cpp
    // @@@ example/design_pattern/visitor.cpp 246

    void TestablePathnamePrinter1::Visit(File const& file) { ostream_ << file.Pathname(); }
    void TestablePathnamePrinter1::Visit(Dir const& dir) { ostream_ << dir.Pathname() + "/"; }
    void TestablePathnamePrinter1::Visit(OtherEntity const& other)
    {
        ostream_ << other.Pathname() + "(o1)";
    }

    void TestablePathnamePrinter2::Visit(File const& file) { ostream_ << file.Pathname(); }

    void TestablePathnamePrinter2::Visit(Dir const& dir) { ostream_ << find_files(dir.Pathname()); }

    void TestablePathnamePrinter2::Visit(OtherEntity const& other)
    {
        ostream_ << other.Pathname() + "(o2)";
    }
```

```cpp
    // @@@ example/design_pattern/visitor_ut.cpp 28

    TEST(Visitor, testable_visitor)
    {
        auto oss = std::ostringstream{};

        // 出力をキャプチャするため、std::coutに代えてossを使う
        auto visitor1 = TestablePathnamePrinter1{oss};
        auto visitor2 = TestablePathnamePrinter2{oss};

        auto file = File{"visitor.cpp"};
        {
            file.Accept(visitor1);
            ASSERT_EQ("visitor.cpp", oss.str());
            oss = {};
        }
        {
            file.Accept(visitor2);
            ASSERT_EQ("visitor.cpp", oss.str());
            oss = {};
        }

        auto dir = Dir{"find_files_ut_dir/dir0"};
        {
            dir.Accept(visitor1);
            ASSERT_EQ("find_files_ut_dir/dir0/", oss.str());
            oss = {};
        }
        {
            dir.Accept(visitor2);
            ASSERT_EQ("find_files_ut_dir/dir0/file2,find_files_ut_dir/dir0/gile3", oss.str());
            oss = {};
        }
    }
```


## CRTP(curiously recurring template pattern) <a id="SS_3_21"></a>
CRTPとは、

```cpp
    // @@@ example/design_pattern/crtp_ut.cpp 8

    template <typename T>
    class Base {
        ...
    };

    class Derived : public Base<Derived> {
        ...
    };
```

のようなテンプレートによる再帰構造を用いて、静的ポリモーフィズムを実現するためのパターンである。

このパターンを用いて、「[Visitor](design_pattern.md#SS_3_20)」のFileEntityの3つの派生クラスが持つコードクローン

```cpp
    // @@@ example/design_pattern/visitor.h 39

    virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*this); }
```

を解消した例を以下に示す。

```cpp
    // @@@ example/design_pattern/crtp.h 31

    class FileEntity {  // VisitorのFileEntityと同じ
    public:
        explicit FileEntity(std::string&& pathname) : pathname_{std::move(pathname)} {}
        virtual ~FileEntity() {}
        std::string const& Pathname() const { return pathname_; }

        virtual void Accept(FileEntityVisitor&) const = 0;  // Acceptの仕様は安定しているので
                                                            // NVIは使わない。
    private:
        std::string const pathname_;
    };

    template <typename T>
    class AcceptableFileEntity : public FileEntity {  // CRTP
    public:
        virtual void Accept(FileEntityVisitor& visitor) const override
        {
            visitor.Visit(*static_cast<T const*>(this));
        }

    private:
        // T : public AcceptableFileEntity<T> { ... };
        // 以外の使い方をコンパイルエラーにする
        AcceptableFileEntity(std::string&& pathname) : FileEntity{std::move(pathname)} {}
        friend T;
    };

    class File final : public AcceptableFileEntity<File> {  // CRTPでクローンを解消
    public:
        File(std::string pathname) : AcceptableFileEntity{std::move(pathname)} {}
    };

    class Dir final : public AcceptableFileEntity<Dir> {  // CRTPでクローンを解消
    public:
        Dir(std::string pathname) : AcceptableFileEntity{std::move(pathname)} {}
    };

    class OtherEntity final : public AcceptableFileEntity<OtherEntity> {  // CRTPでクローンを解消
    public:
        OtherEntity(std::string pathname) : AcceptableFileEntity{std::move(pathname)} {}
    };
```

## Observer <a id="SS_3_22"></a>
Observerは、クラスSubjectと複数のクラスObserverN(N = 0, 1, 2 ...)があり、
この関係が下記の条件を満たさなければならない場合に使用されるパターンである。

* ObserverNオブジェクトはSubjectオブジェクトが変更された際、その変更通知を受け取る。
* SubjectはObserverNへ依存してはならない。

GUIアプリケーションを[MVC](design_pattern.md#SS_3_23)で実装する場合のModelがSubjectであり、
ViewがObserverNである。

まずは、このパターンを使用しない実装例を示す。

```cpp
    // @@@ example/design_pattern/observer_ng.h 6

    /// @class ObserberNG_N
    /// @brief SubjectNGからの変更通知をUpdate()で受け取る。
    ///        Observerパターンを使用しない例。
    class ObserverNG_0 {
    public:
        ObserverNG_0() = default;

        virtual void Update(SubjectNG const& subject)  // テストのためにvirtual
        {
            // 何らかの処理
        }

        virtual ~ObserverNG_0() = default;
        // 何らかの定義、宣言
    };

    class ObserverNG_1 {
    public:
        ...
    };

    class ObserverNG_2 {
    public:
        ...
    };
```

```cpp
    // @@@ example/design_pattern/observer_ng.cpp 6

    void ObserverNG_1::Update(SubjectNG const& subject)
    {
        ...
    }

    void ObserverNG_2::Update(SubjectNG const& subject)
    {
        ...
    }
```

```cpp
    // @@@ example/design_pattern/subject_ng.h 9

    /// @class SubjectNG
    /// @brief 監視されるクラス。SetNumでの状態変更をObserverNG_Nに通知する。
    ///        Observerパターンを使用しない例。
    class SubjectNG final {
    public:
        explicit SubjectNG(ObserverNG_0& ng_0, ObserverNG_1& ng_1, ObserverNG_2& ng_2) noexcept
            : num_{0}, ng_0_{ng_0}, ng_1_{ng_1}, ng_2_{ng_2}
        {
        }

        void SetNum(uint32_t num);
        ...
    };
```

```cpp
    // @@@ example/design_pattern/subject_ng.cpp 4

    void SubjectNG::SetNum(uint32_t num)
    {
        if (num_ == num) {
            return;
        }

        num_ = num;

        notify();  // subjectが変更されたことをobserverへ通知
    }

    void SubjectNG::notify()
    {
        ng_0_.Update(*this);
        ng_1_.Update(*this);
        ng_2_.Update(*this);
    }
```

```cpp
    // @@@ example/design_pattern/observer_ut.cpp 15

    struct ObserverNG_0_Test : ObserverNG_0 {  // テスト用クラス
        virtual void Update(SubjectNG const& subject) final
        {
            ++call_count;
            num = subject.GetNum();
        }

        uint32_t                call_count{0};
        std::optional<uint32_t> num{};
    };

    auto ng0 = ObserverNG_0_Test{};
    auto ng1 = ObserverNG_1{};
    auto ng2 = ObserverNG_2{};

    auto subject = SubjectNG{ng0, ng1, ng2};

    ASSERT_EQ(0, ng0.call_count);  // まだ何もしていない
    ASSERT_FALSE(ng0.num);

    subject.SetNum(1);
    subject.SetNum(2);

    ASSERT_EQ(2, ng0.call_count);
    ASSERT_EQ(2, *ng0.num);

    subject.SetNum(2);  // 同じ値をセットしたため、Updateは呼ばれないはず
    ASSERT_EQ(2, ng0.call_count);
    ASSERT_EQ(2, *ng0.num);
```

上記実装例のクラス図を下記する。
これを見ればわかるように、クラスSubjectNGとクラスObserverNG_Nは相互依存しており、機能追加、
修正が難しいだけではなく、この図の通りにパッケージを分割した場合
(パッケージがライブラリとなると前提）、リンクすら難しくなる。

<!-- pu:plant_uml/observer_class_ng.pu--><p><img src="data:image/png;base64,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" /></p>

このようなクラス間の依存関係は下記のようにファイル間の依存関係に反映される。
このような相互依存は、差分ビルドの長時間化等の問題も引き起こす。

<!-- pu:plant_uml/observer_file_ng.pu--><p><img src="data:image/png;base64,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" /></p>

次に、上記にObserverパターンを適用した実装例
(Subjectを抽象クラスにすることもあるが、下記例ではSubjectを具象クラスにしている)を示す。

```cpp
    // @@@ example/design_pattern/observer_ok.h 3

    /// @class ObserverOK_0
    /// @brief SubjectOKからの変更通知をUpdate()で受け取る。
    ///        Observerパターンの使用例。
    class ObserverOK_0 : public Observer {
        ...
    private:
        virtual void update(SubjectOK const& subject) override;
    };

    class ObserverOK_1 : public Observer {
        ...
    private:
        virtual void update(SubjectOK const& subject) override;
    };

    class ObserverOK_2 : public Observer {
        ...
    private:
        virtual void update(SubjectOK const& subject) override;
    };
```

```cpp
    // @@@ example/design_pattern/observer_ok.cpp 5

    void ObserverOK_0::update(SubjectOK const& subject)
    {
        ...
    }

    void ObserverOK_1::update(SubjectOK const& subject)
    {
        ...
    }

    void ObserverOK_2::update(SubjectOK const& subject)
    {
        ...
    }
```

```cpp
    // @@@ example/design_pattern/subject_ok.h 8

    /// @class SubjectOK
    /// @brief 監視されるクラス。SetNumでの状態変更をObserverOK_Nに通知する。
    ///        Observerパターンの使用例。
    class SubjectOK final {
    public:
        SubjectOK() : observers_{}, num_{0} {}

        void SetNum(uint32_t num)
        {
            if (num_ == num) {
                return;
            }

            num_ = num;

            notify();  // subjectが変更されたことをobserverへ通知
        }

        void     Attach(Observer& observer);           // Observerの登録
        void     Detach(Observer& observer) noexcept;  // Observerの登録解除
        uint32_t GetNum() const noexcept { return num_; }

    private:
        void notify() const;

        std::list<Observer*> observers_;
        ...
    };

    /// @class Observer
    /// @brief SubjectOKを監視するクラスの基底クラス
    class Observer {
    public:
        Observer() = default;
        void Update(SubjectOK const& subject) { update(subject); }

        ...
    private:
        virtual void update(SubjectOK const& subject) = 0;
        ...
    };
```

```cpp
    // @@@ example/design_pattern/subject_ok.cpp 3

    void SubjectOK::Attach(Observer& observer_to_attach) { observers_.push_back(&observer_to_attach); }

    void SubjectOK::Detach(Observer& observer_to_detach) noexcept
    {
        observers_.remove_if(
            [&observer_to_detach](Observer* observer) { return &observer_to_detach == observer; });
    }

    void SubjectOK::notify() const
    {
        for (auto observer : observers_) {
            observer->Update(*this);
        }
    }
```

```cpp
    // @@@ example/design_pattern/observer_ut.cpp 51

    struct ObserverOK_Test : Observer {  // テスト用クラス
        virtual void update(SubjectOK const& subject) final
        {
            ++call_count;
            num = subject.GetNum();
        }

        uint32_t                call_count{0};
        std::optional<uint32_t> num{};
    };

    auto ok0 = ObserverOK_Test{};
    auto ok1 = ObserverOK_1{};
    auto ok2 = ObserverOK_2{};

    auto subject = SubjectOK{};

    subject.Attach(ok0);
    subject.Attach(ok1);
    subject.Attach(ok2);

    ASSERT_EQ(0, ok0.call_count);  // まだ何もしていない
    ASSERT_FALSE(ok0.num);

    subject.SetNum(1);
    subject.SetNum(2);

    ASSERT_EQ(2, ok0.call_count);
    ASSERT_EQ(2, *ok0.num);

    subject.SetNum(2);  // 同じ値をセットしたため、Updateは呼ばれないはず
    ASSERT_EQ(2, ok0.call_count);
    ASSERT_EQ(2, *ok0.num);
```

上記実装例のクラス図を下記する。
Observerパターンを使用しない例と比べると、
クラスSubjectOKとクラスObserverOK_Nとの相互依存が消えたことがわかる。

<!-- pu:plant_uml/observer_class_ok.pu--><p><img src="data:image/png;base64,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FsYrxtaIXbZcqRihUNGQVvjll1+69ej+VNMGczctxCRC/eMsdbr36E59twnF7UbmEA1Qq3P3zk82qX9dKj7drFHPXj2VihGIzCEafK/YrX7Tp65LxatesWcPpWIEQkVDmuDKlSvtO7TvNqTH+0fXB5qE84863QZ3b9++vX7LKNKQCUQDpGob37bzC11TSMXew/p06NBBqRhpyASiAVLFt4/vOrh7CqnYfUhPvKhSMdKgoiFNMG3atLZdnw+0hDD/2nZ7nqvchm4E27dvP3funFuquAVkAtEwecobLbu0DuRbmH+dena+FSpevnz5o48+0tfSqYtMIBqmTp3apmvbQL6F+fd89/hboSLYsmXLDz/84JYqbgEqGlIf33zzTZXoKkv3vRdoA2H+Ub9KdFWudZu7FrjjGjVqZMmShaeuVq3aunXrzKlSpUqtWbPGqhspwOxLlixJh3PmzNmsWTMmS8qJLsWLF9+3b598/OKLLypWrDh58mRzoYPhw4eXKFGCdnLlytWpU6dLly65NVIbGV00QKfKVSvfKBVX7E+Mjom+LhVnzJgB5WRamzZteuTIESn/8ssvKWRyr61++3Hx4sV+/frdd999dI+//fv3NxTCrB599FFTc9myZWXLlv34449NiYPZs2c3b968dOnSXbp0cc+lDTK6aLhpr1g1BV7x/fffj4mJYVpxjDVr1rQn7v7779+6datVNyLw+++/T5gwoVixYvT57rvvbt269ddffy2neFi84rFjx+Tj3r17YSZ8++/F14KmYDWNZMuWrVWrVpDcrZHaUNGQ+sC8+4zo57B/xeeJbfvGP1i8cJY7s9x9T66omlXz3ptv/IIEu07fEf251m3Owvr163PkyDFp0qSffvrp559/xmvz8b333pOzkSkaiPQPPPBAYmIiqefZs2c7d+5csGBBsRAegbnbsWMHx0gHyl955RX3eguDBg0ib7hy5QqGxMN2797drZHayOiiYdZfZnUb1vMmqDhk5LDwVGSmcMerVq3CZ+Hmunbtyix/9dVXXqSKBmhDOEFn79+/n4+fffYZYaZ27dq//fab50ede+65R2rOnTs3d+7clNiXOxg9enRCQkKLFi0aN27snksbZHTRQP97De9zE1Ts/9LA8FRE4eEGZ86ciT/BMU6cOBEViwqUs5EpGnr16lWkSJENGzZwfPLkSYI9AkJ+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" /></p>

最後に、上記のファイルの依存関係を示す。
ファイル(パッケージ)の依存関係においてもSubjectOKはObserverOKに依存していないことがわかる
(MVCに置き換えると、ModelはViewに依存していない状態であるといえる)。

<!-- pu:plant_uml/observer_file_ok.pu--><p><img src="data:image/png;base64,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" /></p>


## MVC <a id="SS_3_23"></a>

MVCはデザインパターンと言うよりもアーキテクチャパターンである。
一般にGUIアプリケーションのアーキテクチャに使用されるが、
外部からの非同期要求を処理するアプリケーションのアーキテクチャにも相性が良い。

MVCのそれぞれのアルファベットの意味は、下記テーブルの通りである。

|   | MVC            | 主な役割                        |
|:-:|:---------------|:--------------------------------|
| M | Model          | ビジネスロジックの処理          |
| V | View           | UIへの出力                      |
| C | Controller     | 入力をModelへ送信               |

下記はMVCの概念モデルである(矢印は制御の流れであって、依存関係ではない)。

<!-- pu:plant_uml/mvc.pu--><p><img src="data:image/png;base64,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" /></p>

制御の流れは、

1. ユーザの入力に応じてControllerのメソッドが呼び出される。
2. Controllerのメソッドは、ユーザの入力に応じた引数とともにModelのメソッドを呼び出す。
3. Modelは、それに対応するビジネスロジック等の処理を(通常、非同期に)行い、
自分自身の状態を変える(変わらないこともある)。
4. Modelの状態変化は、そのModelのオブザーバーとして登録されているViewに通知される。
5. Viewは関連するデータをModelから取得し、それを出力(UIに表示)する。

ViewはModelの[Observer](design_pattern.md#SS_3_22)であるため、ModelはViewへ依存しない。
多々あるMVC派生パターンすべてで、そのような依存関係は存在しない
(具体的なパターンの選択はプロジェクトで使用するGUIフレームワークに強く依存する)。

そのようにする理由は下記の通りで、極めて重要な規則である。

* GUIのテストは目で見る必要がある(ことが多い)ため、Viewに自動単体テストを実施することは困難である。
  一方、ViewがModelに依存しないのであれば、Modelは自動単体テストをすることが可能である。
* 通常、Viewの仕様は不安定で、Modelの仕様は安定しているため、Modelのソースコード変更は
  Viewのそれよりもかなり少ない。
  しかし、ModelがViewに依存してしまうと、Viewに影響されModelのソースコード変更も多くなる。


## Cでのクラス表現 <a id="SS_3_24"></a>
このドキュメントは、C++でのソフトウェア開発を前提としているため、
ここで示したコードもC++で書いているが、

* 何らかの事情でCを使わざるを得ないプログラマがデザインパターンを使用できるようにする
* クラスの理解が曖昧なC++プログラマの理解を助ける(「[クラスのレイアウト](term_explanation.md#SS_6_2_11)」参照)

ような目的のためにCでのクラスの実現方法を例示する。

下記のような基底クラスPointとその派生クラスPoint3Dがあった場合、

<!-- pu:plant_uml/class_c.pu--><p><img src="data:image/png;base64,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" /></p>

C++では、Pointのコードは下記のように表すことが一般的である。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 7

    class Point {
    public:
        explicit Point(int x, int y) noexcept : x_{x}, y_{y} {}
        virtual ~Point() = default;

        void SetXY(int x, int y) noexcept
        {
            x_ = x;
            y_ = y;
        }

        void GetXY(int& x, int& y) const noexcept
        {
            x = x_;
            y = y_;
        }

        virtual int Quantity() const noexcept { return x_ * y_; }

        virtual void Multipy(int m) noexcept
        {
            x_ *= m;
            y_ *= m;
        }

    private:
        int x_;
        int y_;
    };
```

この単体テストは、下記のようになる。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 42

    Point a{1, 2};

    int x;
    int y;
    a.GetXY(x, y);
    ASSERT_EQ(x, 1);
    ASSERT_EQ(y, 2);

    a.SetXY(3, 4);

    a.GetXY(x, y);
    ASSERT_EQ(x, 3);
    ASSERT_EQ(y, 4);

    ASSERT_EQ(a.Quantity(), 12);

    a.Multipy(2);
    ASSERT_EQ(a.Quantity(), 48);
```

これをCで表した場合、下記のようになる。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 124

    struct Point {
        int x;
        int y;

        int (*const Quantity)(Point const* self);
        void (*const Multipy)(Point* self, int m);
    };

    static int point_quantity(Point const* self) { return self->x * self->y; }

    static void point_multipy(Point* self, int m)
    {
        self->x *= m;
        self->y *= m;
    }

    Point Point_Construct(int x, int y)
    {
        Point ret = {x, y, point_quantity, point_multipy};  // C言語のつもり

        return ret;
    }

    void Point_SetXY(Point* self, int x, int y)
    {
        self->x = x;
        self->y = y;
    }

    void Point_GetXY(Point* self, int* x, int* y)
    {
        *x = self->x;
        *y = self->y;
    }
```

C++のメンバ関数はプログラマから見えない引数thisを持つ。
これを表したものが各関数の第1引数selfである。
また、ポリモーフィックな関数は関数ポインタで、
非ポリモーフィックな関数は通常の関数で表される。

この単体テストは、下記のようになる。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 164

    Point a = Point_Construct(1, 2);

    int x;
    int y;

    Point_GetXY(&a, &x, &y);
    ASSERT_EQ(x, 1);
    ASSERT_EQ(y, 2);

    Point_SetXY(&a, 3, 4);

    Point_GetXY(&a, &x, &y);
    ASSERT_EQ(x, 3);
    ASSERT_EQ(y, 4);

    ASSERT_EQ(a.Quantity(&a), 12);

    a.Multipy(&a, 2);
    ASSERT_EQ(a.Quantity(&a), 48);
```

Pointから派生したクラスPoint3DのC++での実装を以下に示す。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 65

    class Point3D : public Point {
    public:
        explicit Point3D(int x, int y, int z) noexcept : Point{x, y}, z_{z} {}

        void SetXYZ(int x, int y, int z) noexcept
        {
            SetXY(x, y);
            z_ = z;
        }

        void GetXYZ(int& x, int& y, int& z) const noexcept
        {
            GetXY(x, y);
            z = z_;
        }

        virtual int Quantity() const noexcept override { return Point::Quantity() * z_; }

        virtual void Multipy(int m) noexcept override
        {
            Point::Multipy(m);
            z_ *= m;
        }

    private:
        int z_;
    };
```

この単体テストは、下記のようになる。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 98

    auto  a = Point3D{1, 2, 3};
    auto& b = a;

    auto x = int{};
    auto y = int{};
    b.GetXY(x, y);
    ASSERT_EQ(x, 1);
    ASSERT_EQ(y, 2);

    b.SetXY(3, 4);

    b.GetXY(x, y);
    ASSERT_EQ(x, 3);
    ASSERT_EQ(y, 4);

    ASSERT_EQ(b.Quantity(), 36);

    b.Multipy(2);
    ASSERT_EQ(b.Quantity(), 288);
```

これをCで実装したものが下記である。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 188

    struct Point3D {
        Point point;
        int   z;
    };

    static int point3d_quantity(Point const* self)
    {
        Point3D const* self_derived = (Point3D const*)self;

        return point_quantity(self) * self_derived->z;
    }

    static void point3d_multipy(Point* self, int m)
    {
        point_multipy(self, m);

        Point3D* self_derived = (Point3D*)self;

        self_derived->z *= m;
    }

    Point3D Point3D_Construct(int x, int y, int z)
    {
        Point3D ret{{x, y, point3d_quantity, point3d_multipy}, z};

        return ret;
    }
```

この単体テストは、下記のようになる。

```cpp
    // @@@ example/design_pattern/class_ut.cpp 221

    Point3D a = Point3D_Construct(1, 2, 3);
    Point*  b = &a.point;

    int x;
    int y;

    Point_GetXY(b, &x, &y);
    ASSERT_EQ(x, 1);
    ASSERT_EQ(y, 2);

    Point_SetXY(b, 3, 4);

    Point_GetXY(b, &x, &y);
    ASSERT_EQ(x, 3);
    ASSERT_EQ(y, 4);

    ASSERT_EQ(b->Quantity(b), 36);

    b->Multipy(b, 2);
    ASSERT_EQ(b->Quantity(b), 288);
```

以上からわかる通り、Cでのクラス実装はC++のものに比べ、

* 記述が多い
* キャストを使わざるを得ない
* リファレンスが使えないため、NULLにならないハンドル変数をポインタにせざるを得ない

等といった問題があるため、「何らかの事情でC++が使えない」チームは、
なるべく早い時期にその障害を乗り越えることをお勧めする。

どうしてもその障害を超えられない場合は、
[モダンC言語プログラミング](https://www.amazon.co.jp/%E3%83%A2%E3%83%80%E3%83%B3C%E8%A8%80%E8%AA%9E%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E3%82%A2%E3%82%B9%E3%82%AD%E3%83%BC%E6%9B%B8%E7%B1%8D-%E8%8A%B1%E4%BA%95-%E5%BF%97%E7%94%9F-ebook/dp/B00HWLJEKW)
が役に立つだろう。


