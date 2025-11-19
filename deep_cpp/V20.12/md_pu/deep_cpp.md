<!-- ./md/deep_intro.md -->
# イントロダクション <a id="SS_1"></a>
このドキュメントは、C++の深い理解を促進するためのものである。
[SOLID](#SS_2)や[デザインパターン](#SS_3) を解説するドキュメントは珍しいものではないが、
一時、C++がその進化を止め、瀕死の状態に陥ったため、
両概念についてをC++で解説したドキュメントはきわめて珍しいと思われる。
また、C++の言語的な特徴であり、その優秀さを際立たせる
[テンプレートメタプログラミング](#SS_4)、[ダイナミックメモリアロケーション](#SS_5)について、
十分な知識を提供するドキュメントは上記と同様にきわめて珍しいと思われる。


## 改訂履歴 <a id="SS_1_1"></a>
* V20.12
    * CRTPの説明強化
    * 「標準ライブラリとプログラミングの概念」に「std::enable_shared_from_this」の説明追加
    * このドキュメントのSOLIDとデザインパターンの章をdeep_cppへ移動
    * C++慣用語句に「Modern CMake project layout」を追加

* V20.11
    * 用語説明の分割と再構成
        * C++コア言語仕様
        * 標準ライブラリとプログラミングの概念
        * C++慣用語句
    * 標準ライブラリとプログラミングの概念に「ロック所有ラッパー」、「並列処理」とstd::condition_variable追加
    * C++慣用語句に「関数設計のガイドライン」、「クラス設計のガイドライン」追加
    * essential_cppのSOLIDとデザインパターンの章をdeep_cppへ移動

* V20.10
    * moveセマンティクスの説明の改善
    * lvalueリファレンスの説明の改善
    * プログラミング概念と標準ライブラリの強化
        * 並行処理
        * ロック所有ラッパー

* V20.09
    * 「オブジェクトの循環所有」の説明強化
    * 「std::weak_ptr」の説明強化
    * 細かなバグやタイポの修正

* V20.08
    * 「rvalueリファレンス」の改定
    * 細かなバグやタイポの修正

* V20.07
    * プレースメントnewを使い、メモリアロケーションの数を少なくするPimpl(lightweight Pimpl)パターン追加
    * .clang-formatの修正し、一カラム120文字まで許容

* V20.06
    * expressionの説明の抜本的変更
    * lvalueリファレンス、rvalueリファレンス、forwardingリファレンスの説明の修正と追加

* V20.03
    * ダイヤモンド継承の図解と説明強化
    * 仮想継承の説明強化

* V20.02
    * std::weak_ptrの解説を追加
    * std::pmrの解説を追加
    * 用語説明追加
        * 畳み込み式
        * hidden-friend関数
        * プログラミング概念と標準ライブラリ
        * 指示付き初期化
        * コンテナ
        * スマートポインタ

* V20.01
    * pmrの解説を追加
    * templateメタプログラミング
        * 浮動小数点IsEqual
        * FixedPoint
        * std::enable_ifをコンセプトを使用しリファクタリング
    * 用語説明追加
        * モジュール
        * コルーチン
        * 畳み込み式
        * テンプレートのテクニックに畳み込み式の使用
        * explicit
        * コンセプト
        * <=>

* V18.07
    * 静的な文字列オブジェクトの強化

## インデックス <a id="SS_1_2"></a>
___

* [SOLID](#SS_2)
* [デザインパターン](#SS_3)
* [テンプレートメタプログラミング](#SS_4)
* [ダイナミックメモリアロケーション](#SS_5)
* [C++コア言語仕様](#SS_6)
* [標準ライブラリとプログラミングの概念](#SS_7)
* [C++慣用語句](#SS_8)
* [Sample Code](#SS_9)


<!-- ./md/solid.md -->
# SOLID <a id="SS_2"></a>
SOLIDとは、オブジェクト指向(OOD/OOP)プログラミングにおいて特に重要な下記の5つの原則である。

* [単一責任の原則(SRP)](#SS_2_1)
* [オープン・クローズドの原則(OCP)](#SS_2_2)
* [リスコフの置換原則(LSP)](#SS_2_3)
* [インターフェース分離の原則(ISP)](#SS_2_4)
* [依存関係逆転の原則(DIP)](#SS_2_5)

[インデックス](#SS_1_2)に戻る。  

___

## 単一責任の原則(SRP) <a id="SS_2_1"></a>
単一責任の原則(SRP, Single Responsibility Principle)とは、

* 一つのクラスは、ただ一つの責任(機能)を持つようにしなければならない
* 一つのクラスは、ただ一つの理由で変更されるように作られなければならない

というクラスデザイン上の制約である。

下記クラスSentenceHolderNotSRPは、一見問題ないように見えるが、std::stringの保持と、
その出力という二つの責務を持つため、SRP違反である。

```cpp
    //  example/solid/srp_ut.cpp 27

    class SentenceHolderNotSRP {
    public:
        SentenceHolderNotSRP()  = default;
        ~SentenceHolderNotSRP() = default;

        void Add(std::string const& sentence) { sentence_ += sentence; }

        std::string const& Get() const noexcept { return sentence_; }

        void Save(std::string const& file)
        {
            std::ofstream o{file};
            o << sentence_;
        }

        void Display() { std::cout << sentence_; }

    private:
        std::string sentence_{};
    };
```

実践的にはこの程度の単純なクラスでのSRP違反が問題になることは少ないが、
下記のコメントで示す通り、単体テストの実施が困難になる。

```cpp
    //  example/solid/srp_ut.cpp 53

    auto not_srp = SentenceHolderNotSRP{};

    not_srp.Add("haha\n");
    not_srp.Add("hihi\n");
    not_srp.Add("huhu\n");

    // SRPに従っていないため、テストが面倒
    not_srp.Save(not_srp_text_);  // not_srp_text_への書き込み

    auto ifs       = std::ifstream{not_srp_text_};
    auto ifs_begin = std::istreambuf_iterator<char>{ifs};
    auto ifs_end   = std::istreambuf_iterator<char>{};
    auto act       = std::string{ifs_begin, ifs_end};  // not_srp_text_ファイルの読み出し

    ASSERT_EQ("haha\nhihi\nhuhu\n", act);

    // SRPに従っていないため、テストできない
    not_srp.Display();
```

クラスSentenceHolderNotSRPの二つの責務をクラスSentenceHolderSRPと、
Output()に分離したコード実装例を下記する。

```cpp
    //  example/solid/srp_ut.cpp 75

    class SentenceHolderSRP {
    public:
        SentenceHolderSRP()  = default;
        ~SentenceHolderSRP() = default;

        void Add(std::string const& sentence) { sentence_ += sentence; }

        std::string const& Get() const noexcept { return sentence_; }

    private:
        std::string sentence_{};
    };

    // SRPに従うために、
    //    SentenceHolderNotSRP::Save(), SentenceHolderNotSRP::Display()
    // をクラスの外に出し、さらに仮引数に出力先(std::ostream&)を追加してこの2関数を統一。
    void Output(SentenceHolderSRP const& sentence_holder, std::ostream& o) { o << sentence_holder.Get(); }
```

下記のコードで示したように、この分離の効果で単体テストの実施が容易になった。

```cpp
    //  example/solid/srp_ut.cpp 98

    auto srp = SentenceHolderSRP{};

    srp.Add("haha\n");
    srp.Add("hihi\n");
    srp.Add("huhu\n");

    // SRPに従ったことで、ファイル操作やstd::coutへの操作が不要になり、単体テストの実施が容易
    auto act = std::ostringstream{};
    Output(srp, act);

    ASSERT_EQ("haha\nhihi\nhuhu\n", act.str());
```


## オープン・クローズドの原則(OCP) <a id="SS_2_2"></a>
オープン・クローズドの原則(OCP, Open-Closed Principle)とは、

* クラスは拡張に対して開いて (open) いなければならず、
* クラスは修正に対して閉じて (closed) いなければならない

というクラスデザイン上の制約である。

まずは、アンチパターンから示す。

```cpp
    //  example/solid/ocp_ut.cpp 14

    class TransactorGoogle {
    public:
        static bool Pay(Yen price) noexcept
        {
            // ...
        }

        static bool Charge(Yen price) noexcept
        {
            // ...
        }
    };

    class TransactorSuica {
        // ...
    };

    class TransactorEdy {
    public:
        // ...
    };

    class TransactorNotOCP {
    public:
        enum class TransactionMethod { Google, Suica, Edy };

        explicit TransactorNotOCP(TransactionMethod pay_method) noexcept : pay_method_{pay_method} {}

        // ...
        bool Charge(Yen price) noexcept
        {
            switch (pay_method_) {
            case TransactionMethod::Google:
                return TransactorGoogle::Charge(price);
            case TransactionMethod::Suica:
                return TransactorSuica::Charge(price);
                // ...
            }
        }

        bool Pay(Yen price) noexcept
        {
            switch (pay_method_) {
            case TransactionMethod::Google:
                return TransactorGoogle::Pay(price);
            case TransactionMethod::Suica:
                return TransactorSuica::Pay(price);
                // ...
            }
        }
        // ...
    };
```

Transaction Method(enum TransactionMethod)が増えた場合、
少なくとも3か所に手を入れなけばならなくなる(修正に対してclosedでない)。
従って、下記のTransactorNotOCP::Charge()や、TransactorNotOCP::Pay()は
Transaction Methodの追加、変更に対して、脆弱な構造だと言える。

次に上記ソースコードのクラス図を下記する。

クラス図が示す通り、
TransactorNotOCPは、TransactorGoogle, TransactorSuica, TransactorEdy
(Transaction Methodに対応した具体的なクラス)に強く依存する。
したがって、新たなTransactor Methodが追加されれば、
Transaction Methodを使用しているTransactorNotOCPのすべてのメンバ関数は影響を受ける。
この構造は、上位概念が下位概念に依存しているとも言えるため、
後述する「[依存関係逆転の原則(DIP)](#SS_2_5)」にも反している。

```plant_uml/ocp_ng.pu
@startuml

package Transactor {
    class TransactorNotOCP
}

package Transactor_Impl {
    class TransactorGoogle
    class TransactorSuica
    class TransactorEdy
}

TransactorNotOCP ---> TransactorGoogle
TransactorNotOCP ---> TransactorSuica
TransactorNotOCP ---> TransactorEdy

note as N
TransactorNotOCPは
    TransactorGoogle, 
    TransactorSuica, 
    TransactorEdy
すべてに強く依存する。
end note


@enduml
```

下記は、TransactorIFを導入することによって、上例をOCPに沿うように改善したクラス図と実装である。
TransactorOCPは、TransactorIFの効果によりTransaction Methodの追加に対して全く影響を受けなくなった
(実際には、TransactorIFから派生する具象クラスの生成用Factory関数(「[Factory](#SS_3_1_4)」参照)
が必要になるため全く影響がないわけではないが、
そのような箇所はソースコード全体でただ一つにすることができるため、
Transaction Methodの追加に対して強固な構造になったと言える)。

```plant_uml/ocp_ok.pu
@startuml

package Transactor {
    class TransactorOCP 
    class TransactorIF
}

package Transactor_Impl {
    class TransactorGoogle
    class TransactorSuica
    class TransactorEdy
}

TransactorIF <|-- TransactorGoogle
TransactorIF <|-- TransactorSuica
TransactorIF <|-- TransactorEdy

TransactorOCP --> TransactorIF

note as N
TransactorOCPはTransactorIF
にのみ依存するため、
Transaction Method
(TransactorIFの派生class)
に影響を受けない。
end note

@enduml


```

下記にこのクラス図に従ったコードを示す。

```cpp
    //  example/solid/ocp_ut.cpp 122

    class TransactorIF {
    public:
        // ...
        bool Charge(Yen price) noexcept { return charge(price); }
        bool Pay(Yen price) noexcept { return pay(price); }

    private:
        virtual bool charge(Yen price) = 0;
        virtual bool pay(Yen price)    = 0;
    };

    class TransactorGoogle : public TransactorIF {
        // ...
    };

    class TransactorSuica : public TransactorIF {
        // ...
    };

    class TransactorEdy : public TransactorIF {
        // ...
    };

    class TransactorOCP {
    public:
        explicit TransactorOCP(std::unique_ptr<TransactorIF>&& transactor) noexcept : transactor_{std::move(transactor)} {}

        bool Charge(Yen price) noexcept { return transactor_->Charge(price); }

        bool Pay(Yen price) noexcept { return transactor_->Pay(price); }

    private:
        std::unique_ptr<TransactorIF> transactor_;
    };
```

ここでは、この原則に沿う実装方法としてポリモーフィズムを使うパターンを紹介したが、
[Pimpl](#SS_8_2_1)のようにラッピングを使用するパターンも有用である。


## リスコフの置換原則(LSP) <a id="SS_2_3"></a>
リスコフの置換原則(LSP, Liskov Substitution Principle)とは、

* 基底クラスを使っているX(関数もしくはクラス)に、
  基底クラスの代わりにその派生クラスを渡した場合でも、
  Xはその実際の型を知ること無しに正常動作できなければならない

というクラスデザイン上の制約であり、
この制約を守るために下記のような契約プログラミングを行うことが求められる。

* 事前条件を派生クラスで強めることはできない。
  つまり、基底クラスよりも強い事前条件を持つ派生クラスを作ってはならない。
* 事後条件を派生クラスで弱めることはできない。
  つまり、基底クラスよりも弱い事後条件を持つ派生クラスを作ってはならない。

この原則に従わない実装例を示すために、以下のようなクラスRectangleとその派生クラスSquareを定義する。

```plant_uml/rectangle_square.pu
@startuml

class Rectangle {
    +SetX()
    +SetY()
    -set_x()
    -set_y()
}

class Square {
    -set_x()
    -set_y()
}

Rectangle <|-down- Square

@enduml
```

```cpp
    //  example/solid/lsp.h 5

    /// @brief (0, 0) からの矩形を表す
    class Rectangle {
    public:
        explicit Rectangle(int x, int y) noexcept : x_{x}, y_{y} {}
        // ...
        void SetX(int x) noexcept
        {
            auto temp = y_;
            set_x(x);
            assert(temp == y_);  // 「set_xはy_に影響を与えない」が事後条件
        }
        // ...

    protected:
        virtual void set_x(int x) noexcept { x_ = x; }

        // ...

    private:
        int x_;
        int y_;
    };

    /// @brief (0, 0) からの正方形を表す
    class Square : public Rectangle {
    public:
        explicit Square(int x) noexcept : Rectangle{x, x} {}
        // ...
    protected:
        virtual void set_x(int x) noexcept override
        {
            Rectangle::set_x(x);
            Rectangle::set_y(x);
        }

        virtual void set_y(int y) noexcept override { set_x(y); }
    };
```

Rectangleのリファレンスを受け取るSetX()とその単体テストを以下のようにすると、
Rectangleのテストでは問題は起こらないが、同じことをSquareに行うとアボートしてしまう
(下記例ではASSERT_DEATHを使用しアボートすることを確認している)。

```cpp
    //  example/solid/lsp_ut.cpp 13

    void SetX(Rectangle& rect, int x) noexcept { rect.SetX(x); }

    TEST(LSP_Opt, violation_abort)
    {
        // Rectangleのテスト
        auto rect = Rectangle{0, 0};
        SetX(rect, 3);
        ASSERT_EQ(3, rect.GetX());

        // Squareのテスト
        auto square = Square{0};
        ASSERT_DEATH(SetX(square, 3), "");  // ここでRectangle::SetX()の中のassert()がfailする。
    }
```

上記コードがアボート(assertion fail)してしまったのは  

* Rectangle::SetX()は、この実行によるy\_の値が不変であることを表明している
* この表明は、Rectangle::set_x()の事後条件となる
* Square::set_x()は、この事後条件を守らず、y\_の値を変えてしまった

が原因である。このデザイン上の問題には目をつぶり(Rectangle、Squareを修正せずに)、
しかもアボートしないSetX()の実装を考えてみよう。

SetX()は仮引数で渡されたオブジェクトの実際の型がわからなければアボートを避けることはできない。
従って、 新しいSetX()のコード実装例は以下のようになる。

```cpp
    //  example/solid/lsp_ut.cpp 32

    void SetX(Rectangle& rect, int x) noexcept
    {
        if (dynamic_cast<Square*>(&rect) != nullptr) {
            rect = Square(x);
        }
        else {
            // rectの型は、Rectangle
            rect.SetX(x);
        }
    }

    TEST(LSP, violation_not_abort)
    {
        // Rectangleのテスト
        auto rect = Rectangle{0, 0};
        SetX(rect, 3);
        ASSERT_EQ(3, rect.GetX());

        // Squareのテスト
        auto square = Square{0};
        SetX(square, 3);  // assert()はfailしない。
        ASSERT_EQ(3, square.GetX());
    }
```

上記の新たなSetX()は、アボートはしないがきわめて醜悪且つ、
Rectangleの全派生クラスに依存した、変更に弱い関数となる。  

なお、リスコフの置換原則とは関係しないが、上記のdynamic_castを含むSetX()は、
下記のように修正することができる。

```cpp
    //  example/solid/lsp_ut.cpp 61

    void SetX(Rectangle& rect, int x) noexcept
    {
        auto y = rect.GetY();
        rect   = Rectangle(x, y);
    }
```

このSetX()は、Rectangleからの派生クラスに依存していないため、良い解法に見える。
ところが実際にはオブジェクトの[スライシング](#SS_8_10_3)という別の問題を引き起こす。  

例示した問題は結局のところデザインの誤りが原因であり、それを修正しない限り、
問題の回避は容易ではない。

一般に、継承関係は、IS-Aの関係と呼ばれる。数学の世界では「正方形 is a 長方形」であるため、
この関係を継承で表したのだが、
「Rectangle::SetX()の性質より導き出されたRectangle::set_x()の事後条件」
により、「クラスSquare is **NOT** a クラスRectangle」となり、
SquareとRectangleは継承関係ではないため問題が発生した。

継承を用いなければこのような問題は発生しないため、public継承を使用する際には、
「本当にその関係は継承で表すべきか(それが最もシンプルな方法か)？」
について熟慮する必要がある。

なお、エクセプション記述子は、関数のエクセプション仕様を強制的にLSPに従わせる仕組みであるが、
C++11から非推奨になり、C++17では規格から削除された。
その理由は、
「[非推奨だった古い例外仕様を削除](https://cpprefjp.github.io/lang/cpp17/remove_deprecated_exception_specifications.html)」
の説明の通り、これを使用し場合、OCPに違反する可能性が高いからである。
従って、原則に従うのみでなく、その他の原則とのバランスも考慮する必要がある。


## インターフェース分離の原則(ISP) <a id="SS_2_4"></a>
インターフェース分離の原則 (ISP, Interface Segregation Principle)とは、

* クラスは、そのクライアントが使用しないメソッドへの依存を、そのクライアントに強制するべきではない。
    * クラスのインターフェースを巨大にしない。
    * 一つのヘッダファイルに互いが密接な関係を持たない複数のクラスを定義、宣言すべきでない。
    * 一つのヘッダファイルにそのファイルのコンパイルに不要なヘッダファイルをインクルードすべきでない。

というクラスデザイン上の制約である。

まずは、ISPに従っていない例を示す。
下記のStreamReadWriterは、ClientRからはStreamReadWriter::Read()のみが、
ClientWからはStreamReadWriter::Write()のみが使用されている。  

```plant_uml/isp_ng.pu
@startuml

rectangle stream_read_writer.h {
    class StreamReadWriter {
        Read(string&);
        Write(const string&);
    }
}

ClientR -up-> StreamReadWriter
ClientW -up-> StreamReadWriter

note as N
StreamReadWriterは、
ClientRからはRead、
ClientWからはWrite
のみを使用されている。
end note
@enduml
```

ほとんどのStreamReadWriter使用ファイルでこのような依存関係がある場合、
このクラスは下記のようにStreamReaderとStreamWriterに分割した方が良い(依存関係が小さくなる)。

```plant_uml/isp_ok.pu
@startuml

rectangle stream_reader.h {
    class StreamReader {
        Read(string&);
    }
}

rectangle stream_writer.h {
    class StreamWriter {
        Write(const string&);
    }
}

ClientR -up-> StreamReader
ClientW -up-> StreamWriter

note as N
StreamReaderはClientR
からのみ依存されている。
StreamWriterはClientW
からのみ依存されている。
end note

@enduml



```

クラスの設計時に統合か分割かで悩むことは多いが、一度統合してしまえば分割は困難であり、
逆に分割されたものを統合することは容易である。このことを考慮すれば、
このような逡巡に解を与えることは簡単である。言うまでもないが、「まずは分割」が原則である。


## 依存関係逆転の原則(DIP) <a id="SS_2_5"></a>
依存関係逆転の原則 (DIP, Dependency Inversion Principle)とは、

* 上位レベルのモジュールは下位レベルのモジュールに依存すべきではない。
* 抽象は具象に依存すべきではない。

というクラス デザイン上の制約である。

下記ServerNG::Serverは、ClientNG::Clientに非同期サービスを提供する
(従って、ServerNG::ServerはClientNG::Clientに対して上位概念である)。

```plant_uml/dip_ng_seq.pu
@startuml

hide footbox

participant "ClientNG::Client" as client
participant "ServerNG::Server" as server

[->  client           : GetString
     activate client
     client ->> server : RequireStringAsync
    
               server -> server : dispatch
               activate server
    
     client -> client : wait_done
     activate client
     client <- server : Done
                     deactivate server
     deactivate client
[<-- client : string
     deactivate client

@enduml
```

非同期サービスであるServerNG::Server::RequireStringAsync()の完了は
ServerNG::ServerがClientNG::Client::Done()を呼び出すことにより通知される。  
その実装、使用例を下記に示す。

```cpp
    //  example/solid/dip_server_ng.h 10

    namespace ServerNG {
    class Server {
    public:
        Server();
        void RequireStringAsync(ClientNG ::Client& client) noexcept;
        // ...
    };
    }  // namespace ServerNG
```

```cpp
    //  example/solid/dip_server_ng.cpp 6

    namespace ServerNG {
    namespace {
    void dispatch(ClientNG::Client& client)  // コマンドのディスパッチ
    {
        switch (client.GetNum()) {
        case 1:
            client.Done(new std::string{"hello"});
            break;
        case 2:
            client.Done(new std::string{"good bye"});
            break;
            // ...
        }
    }

    void thread_entry(Pipe& pipe)  // サーバーのスレッド関数
    {
        for (;;) {
            ClientNG::Client* client{nullptr};
            auto const        ret = pipe.Read(&client, sizeof(client));
            assert(ret == sizeof(client));

            if (client == nullptr) {  // nullptr受信でサーバー終了
                break;
            }

            dispatch(*client);
        }
    }
    }  // namespace
    // ...

    void Server::RequireStringAsync(ClientNG::Client& client) noexcept
    {
        void const* const buff{&client};

        auto ret = pipe_.Write(&buff, sizeof(buff));
        assert(ret == sizeof(&client));
    }
    // ...
    }  // namespace ServerNG
```

```cpp
    //  example/solid/dip_client_ng.h 10

    namespace ClientNG {
    class Client {
    public:
        explicit Client(ServerNG::Server& server) noexcept : server_{server}, pipe_{}, num_{0} {}

        std::string GetString(uint32_t num);

        void Done(std::string* str) noexcept  // サーバーからクライアントへのコマンド終了通知
        {
            auto const ret = pipe_.Write(&str, sizeof(str));
            assert(ret == sizeof(str));
        }

        // ...
    };
    }  // namespace ClientNG
```

```cpp
    //  example/solid/dip_client_ng.cpp 3

    namespace ClientNG {
    std::string Client::GetString(uint32_t num)
    {
        set_num(num);
        server_.RequireStringAsync(*this);

        return *wait_done();  // 非同期通知待ち
    }

    std::unique_ptr<std::string> Client::wait_done()
    {
        std::string* str{nullptr};
        auto const   ret = pipe_.Read(&str, sizeof(str));
        assert(ret == sizeof(str));

        return std::unique_ptr<std::string>{str};
    }
    }  // namespace ClientNG
```

```cpp
    //  example/solid/dip_ut.cpp 11

    TEST(DIP, ng_pattern)
    {
        auto server = ServerNG::Server{};
        auto client = ClientNG::Client{server};

        auto actual = client.GetString(1);
        ASSERT_EQ("hello", actual);

        actual = client.GetString(2);
        ASSERT_EQ("good bye", actual);

        actual = client.GetString(3);
        ASSERT_EQ("unknown", actual);
    }
```

上記ソースコードから明らかなようにServerNG::ServerとClientNG::Clientは相互に依存している。
このうちの一つはサーバがクライアントに依存(上位概念が下位概念に依存)する問題のある構造となっている。

```plant_uml/dip_ng.pu
@startuml

package ServerNG {
    class Server {
        RequireStringAsync()
    }
}

package ClientNG {
    class Client {
        Done()
    }
}

Server <--> Client

note as N
上位概念が下位概念に依存。
これは好ましい依存関係ではない。
end note

@enduml


```

このため、クライアントのバリエーションが増えた場合、容易にServerNG::Serverのコードは肥大化する。
また、ServerNG::Serverを介して各クライアント間にも(暗黙、明示両方の)依存関係が生まれやすいため、
ServerNG::Serverのコード修正は非常に困難になることが予想される。

次にDIPに従い上記コードを改善した例を示す。

```cpp
    //  example/solid/dip_server_ok.h 7

    namespace ServerOK {
    class ClientIF {
    public:
        ClientIF() noexcept : num_{0} {}
        void Done(std::string* str) { done(str); }  // サーバーからクライアントへのコマンド終了通知
        // ...
    private:
        virtual void done(std::string* str) = 0;
        // ...
    };

    class Server {
    public:
        Server();
        void RequireStringAsync(ClientIF& client) noexcept;
        // ...
    };
    }  // namespace ServerOK
```

```cpp
    //  example/solid/dip_server_ok.cpp 5

    namespace ServerOK {
    namespace {
    void dispatch(ClientIF& client)  // コマンドのディスパッチ
    {
        switch (client.GetNum()) {
        case 1:
            client.Done(new std::string{"hello"});
            break;
        case 2:
            client.Done(new std::string{"good bye"});
            break;
            // ...
        }
    }

    void thread_entry(Pipe& pipe)  // サーバーのスレッド関数
    {
        for (;;) {
            ClientIF*  client{nullptr};
            auto const ret = pipe.Read(&client, sizeof(client));
            assert(ret == sizeof(client));

            if (client == nullptr) {  // nullptr受信でサーバー終了
                break;
            }

            dispatch(*client);
        }
    }
    }  // namespace
    // ...

    void Server::RequireStringAsync(ClientIF& client) noexcept
    {
        void const* const buff{&client};

        auto ret = pipe_.Write(&buff, sizeof(buff));
        assert(ret == sizeof(&client));
    }
    // ...
    }  // namespace ServerOK
```

```cpp
    //  example/solid/dip_client_ok.h 10

    namespace ClientOK {
    class Client : public ServerOK::ClientIF {
    public:
        explicit Client(ServerOK::Server& server) noexcept : ClientIF{}, server_{server}, pipe_{} {}

        std::string GetString(uint32_t num);

        // ...
    };
    }  // namespace ClientOK
```

```cpp
    //  example/solid/dip_client_ok.cpp 3

    namespace ClientOK {
    std::string Client::GetString(uint32_t num)
    {
        SetNum(num);
        server_.RequireStringAsync(*this);

        return *wait_done();  // 非同期通知待ち
    }

    std::unique_ptr<std::string> Client::wait_done()
    {
        std::string* str{nullptr};
        auto const   ret = pipe_.Read(&str, sizeof(str));
        assert(ret == sizeof(str));

        return std::unique_ptr<std::string>{str};
    }
    }  // namespace ClientOK
```

```cpp
    //  example/solid/dip_ut.cpp 28

    // 使用方法は、ServerNG, ClientNGと同じ。
    TEST(DIP, ok_pattern)
    {
        auto server = ServerOK::Server{};
        auto client = ClientOK::Client{server};

        // 以下、ng_paternと同じ
        // ...
    }
```

修正後のコードは、

* ServerOK::ServerはServerOK::ClientIFに依存する。
* ClientOK::ClientはServerOK::ClientIFから派生する。

このクラス図を以下に示す。

```plant_uml/dip_ok.pu
@startuml

package ServerOK {
    class Server {
        RequireStringAsync()
    }
    class ClientIF {
        Done()
    }
}

package ClientOK{
    class Client {
        Done()
    }
}

Server -left-> ClientIF
ClientIF <|-- Client
Client --> Server

note as N
ServerOKは、ClientOKに依存していない。
end note

@enduml


```

ServerNGとClientNGの双方向依存関係は、ClientOKからServerOKへの単方向依存関係へと改善され、
サーバに影響を与えることなく、クライアントの機能変更やバリエーション追加を行うことが可能となった。


## まとめ <a id="SS_2_6"></a>
以上で述べたように、SOLIDはオブジェクト指向(OOD/OOP)プログラミングにおいて極めて重要な原則である。
この逸脱はソースコードを劣化させ、ソフトウェアの品質低下や開発費増大に直結するため、
厳守することが求められる。



<!-- ./md/design_pattern.md -->
# デザインパターン <a id="SS_3"></a>

ソースコードを劣化させるアンチパターンには、以下のようなものがある。

* 大きすぎる関数、クラス、ファイル等のソフトウェア構成物
* 複雑怪奇な依存関係
* コードクローン

こういった問題は、良質なコードを書くという意識を持ったプログラマの継続的な努力と、
ソフトウェア工学の知識によって回避可能である。
本章ではその知識の一翼を担うイディオム、デザインパターンを解説、例示する。

なお、ここに挙げるイディオム、デザインパターンは「適切な場所に適用される場合、
ソースコードをよりシンプルに記述できる」というメリットがある一方で、
「不適切な場所に適用される場合、ソースコードの複雑度を不要に上げてしまう」という負の一面を持つ。
また、この章で取り扱うパターンを覚えたてのプログラマは、自分のスキルが向上したという一種の高揚感や顕示欲から、
それらをむやみに多用してしまう状態に陥ることがある。

___

__この章の構成__

[イディオム](#SS_8_1)  

- [ガード節(Early Return)](#SS_8_1_1)
- [RAII(scoped guard)](#SS_8_1_2)
- [Copy-And-Swap](#SS_8_1_3)
- [CRTP(curiously recurring template pattern)](#SS_8_1_4)
- [Accessor](#SS_8_1_5)
- [Immutable](#SS_8_1_6)
- [NVI(non virtual interface)](#SS_8_1_7)

[実装パターン](#SS_8_2)

- [Pimpl](#SS_8_2_1)
- [lightweight Pimpl](#SS_8_2_2)
- [BitmaskType](#SS_8_2_3)
- [Future](#SS_8_2_4)
- [Null Object](#SS_8_2_5)
- [Cでのクラス表現](#SS_8_2_6)

[オブジェクト生成系デザインパターン](#SS_3_1)

- [Singleton](#SS_3_1_1)
- [Named Constructor](#SS_3_1_2)
- [Clone(仮想コンストラクタ)](#SS_3_1_3)
- [Factory](#SS_3_1_4)

[オブジェクトの動作/協調に関するデザインパターン](#SS_3_2)

- [Templateメソッド](#SS_3_2_1)
- [Strategy](#SS_3_2_2)
- [State](#SS_3_2_3)
- [Observer](#SS_3_2_4)
- [Visitor](#SS_3_2_5)

[アーキテクチャパターン(システムレベルの構造)](#SS_3_3)

- [DI(dependency injection)](#SS_3_3_1)
- [MVC](#SS_3_3_2)


[インデックス](#SS_1_2)に戻る。  

___

## オブジェクト生成系デザインパターン <a id="SS_3_1"></a>
### Singleton <a id="SS_3_1_1"></a>
このパターンにより、特定のクラスのインスタンスをシステム全体で唯一にすることができる。
これにより、グローバルオブジェクトを規律正しく使用しやすくなる。

以下は、Singletonの実装例である。

```cpp
    //  example/design_pattern/singleton_ut.cpp 7

    class Singleton final {
    public:
        static Singleton&       Inst();
        static Singleton const& InstConst() noexcept  // constインスタンスを返す
        {
            return Inst();
        }
        // ...

    private:
        Singleton() noexcept {}  // コンストラクタをprivateにすることで、
                                 // Inst()以外ではこのオブジェクトを生成できない。
        // ...
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
(「[Named Constructor](#SS_3_1_2)」参照)と呼ばれる。


### Named Constructor <a id="SS_3_1_2"></a>
Named Connstructorは、[Singleton](#SS_3_1_1)のようなオブジェクトを複数、生成するためのパターンである。

```cpp
    //  example/design_pattern/enum_operator.h 76

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

次に示したのは「[Factory](#SS_3_1_4)」の例にこのパターンを適応したコードである。

```cpp
    //  example/design_pattern/template_method.h 15

    /// @brief data_storer_if.cppに定義すべきだが、サンプルであるため便宜上同じファイルで定義する
    ///        データフォーマットを行うクラスのインターフェースクラス
    class XxxDataFormatterIF {
    public:
        explicit XxxDataFormatterIF(std::string_view formatter_name) noexcept : formatter_name_{formatter_name} {}
        virtual ~XxxDataFormatterIF() = default;

        static XxxDataFormatterIF const& Xml() noexcept;
        static XxxDataFormatterIF const& Csv() noexcept;
        static XxxDataFormatterIF const& Table() noexcept;

        // ...
    };
```

```cpp
    //  example/design_pattern/template_method.cpp 146

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


### Clone(仮想コンストラクタ) <a id="SS_3_1_3"></a>
オブジェクトコピーによる[スライシング](#SS_8_10_3)を回避するためのイデオムである。

下記は、オブジェクトコピーによるスライシングを起こしてしまう例である。

```cpp
    //  example/design_pattern/clone_ut.cpp 8

    class BaseSlicing {
    public:
        // ...
        virtual char const* Name() const noexcept { return "BaseSlicing"; }
    };

    class DerivedSlicing final : public BaseSlicing {
    public:
        // ...
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
    //  example/design_pattern/clone_ut.cpp 50

    // スライシングを起こさないようにコピー演算子の代わりにClone()を実装。
    class BaseNoSlicing {
    public:
        // ...
        virtual char const* Name() const noexcept { return "BaseNoSlicing"; }

        virtual std::unique_ptr<BaseNoSlicing> Clone() { return std::make_unique<BaseNoSlicing>(); }

        BaseNoSlicing(BaseNoSlicing const&)            = delete;  // copy生成の禁止
        BaseNoSlicing& operator=(BaseNoSlicing const&) = delete;  // copy代入の禁止
    };

    class DerivedNoSlicing final : public BaseNoSlicing {
    public:
        // ...
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
        auto b_uptr = b_ptr_d->Clone();              // コピー演算子の代わりにClone()を使う。
    #endif

        ASSERT_STREQ("DerivedNoSlicing", b_uptr->Name());  // 意図通り"DerivedNoSlicing"が返る。
    }
```

B1::Clone()やそのオーバーライドであるD1::Clone()を使うことで、
スライシングを起こすことなくオブジェクトのコピーを行うことができるようになった。


### Factory <a id="SS_3_1_4"></a>
Factoryは、専用関数(Factory関数)にオブジェクト生成をさせるためのパターンである。
オブジェクトを生成するクラスや関数をそのオブジェクトの生成方法に依存させたくない場合や、
オブジェクトの生成に統一されたルールを適用したい場合等に用いられる。
DI(「[DI(dependency injection)](#SS_3_3_1)」参照)と組み合わせて使われることが多い。

「[Templateメソッド](#SS_3_2_1)」の例にFactoryを適用したソースコードを下記する。

下記のXxxDataFormatterFactory関数により、

* XxxDataFormatterIFオブジェクトはstd::unique_ptrで保持されることを強制できる
* XxxDataFormatterIFから派生したクラスはtemplate_method.cppの無名名前空間で宣言できるため、
  これらのクラスは他のクラスから直接依存されることがない

といった効果がある。

```cpp
    //  example/design_pattern/template_method.h 65

    enum class XxxDataFormatterMethod {
        Xml,
        Csv,
        Table,
    };

    /// @brief std::unique_ptrで保持されたXxxDataFormatterIFオブジェクトを生成するFactory関数
    /// @param method XxxDataFormatterMethodのいずれか
    /// @return std::unique_ptr<const XxxDataFormatterIF>
    ///         XxxDataFormatterIFはconstメンバ関数のみを持つため、戻り値もconstオブジェクト
    std::unique_ptr<XxxDataFormatterIF const> XxxDataFormatterFactory(XxxDataFormatterMethod method);
```

```cpp
    //  example/design_pattern/template_method.cpp 108

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
    //  example/design_pattern/template_method_factory_ut.cpp 7

    TEST(Factory, xml)
    {
        auto xml = XxxDataFormatterFactory(XxxDataFormatterMethod::Xml);

        // ...
    }

    TEST(Factory, csv)
    {
        auto csv = XxxDataFormatterFactory(XxxDataFormatterMethod::Csv);

        // ...
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
    //  example/design_pattern/template_method.cpp 125

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


## オブジェクトの動作/協調に関するデザインパターン <a id="SS_3_2"></a>

### Templateメソッド <a id="SS_3_2_1"></a>
Templateメソッドは、雛形の形式(書式等)を定めるメンバ関数(templateメソッド)と、
それを埋めるための振る舞いやデータを定めるメンバ関数を分離するときに用いるパターンである。

以下に実装例を示す。

```cpp
    //  example/design_pattern/template_method.h 6

    /// @brief 何かのデータを入れる箱
    struct XxxData {
        int a;
        int b;
        int c;
    };

    /// @brief data_storer_if.cppに定義すべきだが、サンプルであるため便宜上同じファイルで定義する
    ///        データフォーマットを行うクラスのインターフェースクラス
    class XxxDataFormatterIF {
    public:
        explicit XxxDataFormatterIF(std::string_view formatter_name) noexcept : formatter_name_{formatter_name} {}
        virtual ~XxxDataFormatterIF() = default;

        std::string ToString(XxxData const& xxx_data) const { return header() + body(xxx_data) + footer(); }

        std::string ToString(std::vector<XxxData> const& xxx_datas) const
        {
            std::string ret{header()};

            for (auto const& xxx_data : xxx_datas) {
                ret += body(xxx_data);
            }

            return ret + footer();
        }
        // ...
    private:
        virtual std::string const& header() const                      = 0;
        virtual std::string const& footer() const                      = 0;
        virtual std::string        body(XxxData const& xxx_data) const = 0;

        // ...
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
    //  example/design_pattern/template_method.cpp 8

    /// @class XxxDataFormatterXml
    /// @brief XxxDataをXmlに変換
    class XxxDataFormatterXml final : public XxxDataFormatterIF {
        // ...
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

        static inline std::string const header_{"<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<XxxDataFormatterXml>\n"};
        static inline std::string const footer_{"</XxxDataFormatterXml>\n"};
    };

    /// @class XxxDataFormatterCsv
    /// @brief XxxDataをCsvに変換
    class XxxDataFormatterCsv final : public XxxDataFormatterIF {
        // ...
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
        // ...
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
        // ...
    };
```

以下の単体テストで、これらのクラスの振る舞いを示す。

```cpp
    //  example/design_pattern/template_method_ut.cpp 6

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

        // ...
    }
```

上記で示した実装例は、public継承による動的ポリモーフィズムを使用したため、
XxxDataFormatterXml、XxxDataFormatterCsv、XxxDataFormatterTableのインスタンスやそのポインタは、
XxxDataFormatterIFのリファレンスやポインタとして表現できる。
この性質は、[Factory](#SS_3_1_4)や[Named Constructor](#SS_3_1_2)の実装には不可欠であるが、
逆にこのようなポリモーフィズムが不要な場合、このよう柔軟性も不要である。

そういった場合、private継承を用いるか、
テンプレートを用いた静的ポリモーフィズムを用いることでこの柔軟性を排除できる。

下記のコードはそのような実装例である。

```cpp
    //  example/design_pattern/template_method_ut.cpp 112

    #if __cplusplus >= 202002L // c++20
    template <typename T>
    concept DataFormattable = requires(T t, const XxxData& xxx_data) {
        { t.Header() } -> std::convertible_to<std::string>;
        { t.Body(xxx_data) } -> std::convertible_to<std::string>;
        { t.Footer() } -> std::convertible_to<std::string>;
    };
    template <DataFormattable T>  // TはDataFormattableに制約される

    #else // c++17
    template <typename T>  // Tは下記のXxxDataFormatterXmlのようなクラス
    #endif
    class XxxDataFormatter : private T {
    public:
        std::string ToString(XxxData const& xxx_data) const { return T::Header() + T::Body(xxx_data) + T::Footer(); }

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
        inline static std::string const header_{"<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<XxxDataFormatterXml>\n"};
        inline static std::string const footer_{"</XxxDataFormatterXml>\n"};
    };

    using XxxDataFormatterXml = XxxDataFormatter<XxxDataFormatterXml_Impl>;
```

上記の単体テストは下記のようになる。

```cpp
    //  example/design_pattern/template_method_ut.cpp 168

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


### Strategy <a id="SS_3_2_2"></a>
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
    //  example/design_pattern/find_files_old_style.h 4

    /// @enum FindCondition
    /// find_files_recursivelyの条件
    enum class FindCondition {
        File,              ///< pathがファイル
        Dir,               ///< pathがディレクトリ
        FileNameHeadIs_f,  ///< pathがファイル且つ、そのファイル名の先頭が"f"
    };
```

```cpp
    //  example/design_pattern/find_files_old_style.cpp 9

    /// @brief 条件にマッチしたファイルをリカーシブに探して返す
    /// @param path      リカーシブにディレクトリをたどるための起点となるパス
    /// @param condition どのようなファイルかを指定する
    /// @return 条件にマッチしたファイルをstd::vector<std::string>で返す
    std::vector<std::string> find_files_recursively(std::string const& path, FindCondition condition)
    {
        auto files = std::vector<fs::path>{};

        // recursive_directory_iteratorはファイルシステム依存するため、その依存を排除する他の処理
        std::copy(fs::recursive_directory_iterator{path}, fs::recursive_directory_iterator{}, std::back_inserter(files));

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
                // ...
            }

            if (is_match) {
                ret.emplace_back(p.generic_string());
            }
        });

        return ret;
    }
```

```cpp
    //  example/design_pattern/find_files_ut.cpp 29

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
    //  example/design_pattern/find_files_strategy.h 7

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
    extern std::vector<std::string> find_files_recursively(std::string const& path, find_condition condition);
```

```cpp
    //  example/design_pattern/find_files_strategy.cpp 6

    std::vector<std::string> find_files_recursively(std::string const& path, find_condition condition)
    {
        namespace fs = std::filesystem;

        auto files = std::vector<fs::path>{};

        // recursive_directory_iteratorはファイルシステム依存するため、その依存を排除する他の処理
        std::copy(fs::recursive_directory_iterator{path}, fs::recursive_directory_iterator{}, std::back_inserter(files));

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
    //  example/design_pattern/find_files_ut.cpp 69

    TEST(Strategy, strategy_lamda)
    {
        namespace fs = std::filesystem;

        assure_test_files_exist();  // test用のファイルがあることの確認

        // ラムダ式で実装
        auto const files_actual
            = find_files_recursively(test_dir, [](fs::path const& p) noexcept { return fs::is_regular_file(p); });

        auto const files_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir0/gile3",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0",
            test_dir + "gile1"
        });
        ASSERT_EQ(files_expect, files_actual);

        auto const dirs_actual
            = find_files_recursively(test_dir, [](fs::path const& p) noexcept { return fs::is_directory(p); });
        auto const dirs_expect = sort(std::vector{
            test_dir + "dir0",
            test_dir + "dir1",
            test_dir + "dir1/dir2"
        });
        ASSERT_EQ(dirs_expect, dirs_actual);

        auto const f_actual = find_files_recursively(
            test_dir, [](fs::path const& p) noexcept { return p.filename().generic_string()[0] == 'f'; });

        auto const f_expect = sort(std::vector{
            test_dir + "dir0/file2",
            test_dir + "dir1/dir2/file4",
            test_dir + "file0"
        });
        ASSERT_EQ(f_expect, f_actual);
    }

    /// @brief find_files_recursivelyの第2仮引数に渡すためのファイル属性を決める関数
    bool condition_func(std::filesystem::path const& path) { return path.filename().generic_string().at(0) == 'f'; }

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

    /// @brief
    ///  find_files_recursivelyの第2仮引数に渡すためのファイル属性を決める関数オブジェクトクラス。
    ///  検索条件に状態が必要な場合、関数オブジェクトを使うとよい。
    class ConditionFunctor {
    public:
        ConditionFunctor()  = default;
        ~ConditionFunctor() = default;

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
その属性の追加に対して「[オープン・クローズドの原則(OCP)](#SS_2_2)」に対応した構造となった。

なお、上記find_files_recursivelyの第2パラメータをテンプレートパラメータとすることで、

```cpp
    //  example/design_pattern/find_files_strategy.h 22

    #if __cplusplus >= 202002L  // c++20
    // ファンクタがboolを返し、std::filesystem::path const&を引数に取るかを確認するコンセプト
    namespace Inner_ {
    template <typename F>
    concept find_condition = requires(F f, std::filesystem::path const& p)
    {
        { f(p) } -> std::same_as<bool>;
    };
    }  // namespace Inner_

    template <Inner_::find_condition F>
    auto find_files_recursively2(std::string const& path, F condition)
        -> std::enable_if_t<std::is_invocable_r_v<bool, F, std::filesystem::path const&>, std::vector<std::string>>

    #else  // c++17
    template <typename F>  // Fはファンクタ
    auto find_files_recursively2(std::string const& path, F&& condition) -> std::vector<std::string>
    #endif
    {
        namespace fs = std::filesystem;

        auto files = std::vector<fs::path>{};

        // recursive_directory_iteratorでディレクトリ内のファイルを再帰的に取得
        std::copy(fs::recursive_directory_iterator{path}, fs::recursive_directory_iterator{}, std::back_inserter(files));

        std::sort(files.begin(), files.end());  // ファイルリストをソート

        auto ret = std::vector<std::string>{};

        std::for_each(files.cbegin(), files.cend(), [&](fs::path const& p) {
            if (condition(p)) {  // 条件を満たすファイルをretに追加
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
    //  example/design_pattern/strategy_shipping_ut.cpp 11

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
    //  example/design_pattern/strategy_shipping_ut.cpp 43

    X x;

    x.DoSomething();
```

このコードは、Strategyを使用し以下のようにすることで、改善することができる。

```cpp
    //  example/design_pattern/strategy_shipping_ut.cpp 56

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
    //  example/design_pattern/strategy_shipping_ut.cpp 81

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
    //  example/design_pattern/strategy_shipping_ut.cpp 100

    X                x;
    ShippingOp_Japan sj;

    x.DoSomething(sj);
```

あるいは、[DI(dependency injection)](#SS_3_3_1)と組み合わせて、下記のような改善も有用である。

```cpp
    //  example/design_pattern/strategy_shipping_ut.cpp 112

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
    //  example/design_pattern/strategy_shipping_ut.cpp 138

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
    //  example/design_pattern/strategy_shipping_ut.cpp 157

    X x{std::unique_ptr<ShippingOp>(new ShippingOp_Japan)};

    x.DoSomething();
```


### State <a id="SS_3_2_3"></a>
Stateは、オブジェクトの状態と、それに伴う振る舞いを分離して記述するためのパターンである。
これにより状態の追加、削減、変更に伴う修正範囲が限定される
(「[オープン・クローズドの原則(OCP)](#SS_2_2)」参照)。
またオブジェクトのインターフェース変更(パブリックメンバ関数の変更)に関しても、修正箇所が明確になる。

```plant_uml/state_machine.pu
@startuml

[*] --> idle
idle    --> running : run
idle    --> idle : abort
idle    --> idle : suspend

running --> running : run
running --> idle : abort
running --> suspending : suspend/suspend_count = 1

suspending  --> running: run [suspend_count == 0]/\n--suspend_count 
suspending  --> idle : abort / suspend_count = 0
suspending  --> suspending : suspend/++suspend_count 

note top of idle
    threadの状態を単純に表した
    ステートマシン図
end note

@enduml
```

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
    //  example/design_pattern/state_machine_old.h 4

    extern std::string_view ThreadOldStyleStateStr() noexcept;
    extern void             ThreadOldStyleRun();
    extern void             ThreadOldStyleAbort();
    extern void             ThreadOldStyleSuspend();
```

```cpp
    //  example/design_pattern/state_machine_old.cpp 6

    namespace {
    enum class ThreadOldStyleState {
        Idle,
        Running,
        Suspending,
    };

    ThreadOldStyleState thread_old_style_state;
    // ...
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
        // ...
    }

    void ThreadOldStyleSuspend()
    {
        // ...
    }
```

```cpp
    //  example/design_pattern/state_machine_ut.cpp 15

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

        // ...
    }
```

下記は、上記例へstateパターンを適用した例である。
まずは、stateパターンを形成するクラスの関係をクラス図で示す。

```plant_uml/state_machine_class.pu
@startuml

class ThreadNewStyle {
    Abort()
    Run()
    Suspend()
}

class ThreadNewStyleState {
    Abort()
    Run()
    Suspend()
}

ThreadNewStyleState <-up- ThreadNewStyle

ThreadNewStyleState_Idle       -up-|> ThreadNewStyleState
ThreadNewStyleState_Running    -up-|> ThreadNewStyleState
ThreadNewStyleState_Suspending -left-|> ThreadNewStyleState

note as N
ThreadNewStyleは、ほとんどの動作を
ThreadNewStyleStateに委譲する。
end note

@enduml

```

次に上記クラス図の実装例を示す。

```cpp
    //  example/design_pattern/state_machine_new.h 6

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
    //  example/design_pattern/state_machine_new.h 51

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
    //  example/design_pattern/state_machine_new.cpp 10

    class ThreadNewStyleState_Idle final : public ThreadNewStyleState {
        // ...
    };

    class ThreadNewStyleState_Running final : public ThreadNewStyleState {
        // ...
    };

    class ThreadNewStyleState_Suspending final : public ThreadNewStyleState {
    public:
        // ...
    private:
        virtual std::unique_ptr<ThreadNewStyleState> abort_thread() override
        {
            // do something to abort
            // ...

            return std::make_unique<ThreadNewStyleState_Idle>();
        }

        virtual std::unique_ptr<ThreadNewStyleState> run_thread() override
        {
            --suspend_count_;

            if (suspend_count_ == 0) {
                // do something to resume
                // ...
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
        // ...
    };
```

```cpp
    //  example/design_pattern/state_machine_ut.cpp 57

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

        // ...
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
    //  example/design_pattern/state_machine_new.h 76

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
    //  example/design_pattern/state_machine_new.cpp 106

    void ThreadNewStyle2::run_idle()
    {
        // スレッドの始動処理
        // ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_running;
        suspend_   = &ThreadNewStyle2::suspend_running;
        state_str_ = state_str_running_;
    }

    void ThreadNewStyle2::abort_running()
    {
        // スレッドのアボート処理
        // ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_idle;
        suspend_   = &ThreadNewStyle2::suspend_idle;
        state_str_ = state_str_idle_;
    }

    void ThreadNewStyle2::suspend_running()
    {
        // スレッドのサスペンド処理
        // ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_suspending;
        suspend_   = &ThreadNewStyle2::suspend_suspending;
        state_str_ = state_str_suspending_;
    }

    void ThreadNewStyle2::run_suspending()
    {
        // スレッドのレジューム処理
        // ...

        // ステートの切り替え
        run_       = &ThreadNewStyle2::run_running;
        suspend_   = &ThreadNewStyle2::suspend_running;
        state_str_ = state_str_running_;
    }
```

```cpp
    //  example/design_pattern/state_machine_ut.cpp 95

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


### Observer <a id="SS_3_2_4"></a>
Observerは、クラスSubjectと複数のクラスObserverN(N = 0, 1, 2 ...)があり、
この関係が下記の条件を満たさなければならない場合に使用されるパターンである。

* ObserverNオブジェクトはSubjectオブジェクトが変更された際、その変更通知を受け取る。
* SubjectはObserverNへ依存してはならない。

GUIアプリケーションを[MVC](#SS_3_3_2)で実装する場合のModelがSubjectであり、
ViewがObserverNである。

まずは、このパターンを使用しない実装例を示す。

```cpp
    //  example/design_pattern/observer_ng.h 6

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
        // ...
    };

    class ObserverNG_2 {
    public:
        // ...
    };
```

```cpp
    //  example/design_pattern/observer_ng.cpp 6

    void ObserverNG_1::Update(SubjectNG const& subject)
    {
        // ...
    }

    void ObserverNG_2::Update(SubjectNG const& subject)
    {
        // ...
    }
```

```cpp
    //  example/design_pattern/subject_ng.h 9

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
        // ...
    };
```

```cpp
    //  example/design_pattern/subject_ng.cpp 4

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
    //  example/design_pattern/observer_ut.cpp 15

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

```plant_uml/observer_class_ng.pu
@startuml
scale max 700 width

package "SubjectNG" as SubjectNG_Pkg {
    class SubjectNG {
        -notify()
    }
}

package ObserverNG {
    class ObserverNG_2 {
        Update(const SubjectNG&)
    }

    class ObserverNG_1 {
        Update(const SubjectNG&)
    }

    class ObserverNG_0 {
        Update(const SubjectNG&)
    }
}

SubjectNG o-down->   ObserverNG_0
SubjectNG o-down->   ObserverNG_1
SubjectNG o-down->   ObserverNG_2

ObserverNG_0 -up-->   SubjectNG
ObserverNG_1 -up-->   SubjectNG
ObserverNG_2 -up-->   SubjectNG

note as N
SubjectNGとPackageObserverNG
が相互依存になる。
end note

@enduml



```

このようなクラス間の依存関係は下記のようにファイル間の依存関係に反映される。
このような相互依存は、差分ビルドの長時間化等の問題も引き起こす。

```plant_uml/observer_file_ng.pu
@startuml

package  ObserverNG {
    agent "observer_ng.h" as observer_ng_h
    agent "observer_ng.cpp" as observer_ng_cpp
}

package  SubjectNG {
    agent "subject_ng.h" as   subject_ng_h
    agent "subject_ng.cpp" as subject_ng_cpp
}

observer_ng_h   <-right->  subject_ng_h
observer_ng_cpp -up->      observer_ng_h
subject_ng_cpp  -up->      subject_ng_h

note as N
SubjectNGとObserverNG
が相互依存になる。
end note

@enduml
```

次に、上記にObserverパターンを適用した実装例
(Subjectを抽象クラスにすることもあるが、下記例ではSubjectを具象クラスにしている)を示す。

```cpp
    //  example/design_pattern/observer_ok.h 3

    /// @brief SubjectOKからの変更通知をUpdate()で受け取る。
    ///        Observerパターンの使用例。
    class ObserverOK_0 : public Observer {
        // ...
    private:
        virtual void update(SubjectOK const& subject) override;
    };

    class ObserverOK_1 : public Observer {
        // ...
    private:
        virtual void update(SubjectOK const& subject) override;
    };

    class ObserverOK_2 : public Observer {
        // ...
    private:
        virtual void update(SubjectOK const& subject) override;
    };
```

```cpp
    //  example/design_pattern/observer_ok.cpp 5

    void ObserverOK_0::update(SubjectOK const& subject)
    {
        // ...
    }

    void ObserverOK_1::update(SubjectOK const& subject)
    {
        // ...
    }

    void ObserverOK_2::update(SubjectOK const& subject)
    {
        // ...
    }
```

```cpp
    //  example/design_pattern/subject_ok.h 8

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
        // ...
    };

    /// @brief SubjectOKを監視するクラスの基底クラス
    class Observer {
    public:
        Observer() = default;
        void Update(SubjectOK const& subject) { update(subject); }

        // ...
    private:
        virtual void update(SubjectOK const& subject) = 0;
        // ...
    };
```

```cpp
    //  example/design_pattern/subject_ok.cpp 3

    void SubjectOK::Attach(Observer& observer_to_attach) { observers_.push_back(&observer_to_attach); }

    void SubjectOK::Detach(Observer& observer_to_detach) noexcept
    {
        observers_.remove_if([&observer_to_detach](Observer* observer) { return &observer_to_detach == observer; });
    }

    void SubjectOK::notify() const
    {
        for (auto observer : observers_) {
            observer->Update(*this);
        }
    }
```

```cpp
    //  example/design_pattern/observer_ut.cpp 51

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

```plant_uml/observer_class_ok.pu
@startuml
scale max 700 width

package "SubjectOK" as SubjectOK_Pkg {
    class SubjectOK {
        Attach()
        Notify()
    }

    class Observer {
        Update(const SubjectOK&)
    }
}

package ObserverOK {
    class ObserverOK_0 {
        Update(const SubjectOK&)
    }
    class ObserverOK_1 {
        Update(const SubjectOK&)
    }
    class ObserverOK_2 {
        Update(const SubjectOK&)
    }
}

Observer -up->      SubjectOK  
SubjectOK    o-down->   Observer
ObserverOK_0 -up-|>     Observer
ObserverOK_1 -up-|>     Observer
ObserverOK_2 -up-|>     Observer

note as N
SubjectOKはObserverOKに依存しない。
end note

@enduml

```

最後に、上記のファイルの依存関係を示す。
ファイル(パッケージ)の依存関係においてもSubjectOKはObserverOKに依存していないことがわかる
(MVCに置き換えると、ModelはViewに依存していない状態であるといえる)。

```plant_uml/observer_file_ok.pu
@startuml

package ObserverOK {
    agent "observer_ok.h" as   observer_ok_h
    agent "observer_ok.cpp" as observer_ok_cpp
}

package SubjectOK {
    agent "subject_ok.h" as   subject_ok_h
    agent "subject_ok.cpp" as subject_ok_cpp
}

observer_ok_h   -right->  subject_ok_h
observer_ok_cpp -up->     observer_ok_h
subject_ok_cpp  -up->     subject_ok_h


note as N
SubjectOKはObserverOK
に依存しない。
end note

@enduml
```


### Visitor <a id="SS_3_2_5"></a>
このパターンは、クラス構造とそれに関連するアルゴリズムを分離するためのものである。

最初に
「クラス構造とそれに関連するアルゴリズムは分離できているが、
それ以前にオブジェクト指向の原則に反している」
例を示す。

```cpp
    //  example/design_pattern/visitor.cpp 42

    /// @brief
    ///  ファイルシステムの構成物(ファイル、ディレクトリ等)を表すクラスの基底クラス
    class FileEntity {
    public:
        explicit FileEntity(std::string pathname) : pathname_{std::move(pathname)} {}
        virtual ~FileEntity() {}
        std::string const& Pathname() const { return pathname_; }

        // ...

    private:
        std::string const pathname_;
    };

    class File final : public FileEntity {
        // ...
    };

    class Dir final : public FileEntity {
        // ...
    };

    class OtherEntity final : public FileEntity {
        // ...
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

```plant_uml/visitor_ng1.pu
@startuml

class FileEntity
class File
class Dir
class OtherEntity

File  -up-|> FileEntity
Dir   -up-|> FileEntity
OtherEntity -up-|> FileEntity

Printer -> FileEntity
Printer -> File
Printer -> Dir
Printer -> OtherEntity

@enduml

```

これをポリモーフィズムの導入で解決した例を示す。

```cpp
    //  example/design_pattern/visitor.cpp 142

    class FileEntity {
    public:
        explicit FileEntity(std::string pathname) : pathname_{std::move(pathname)} {}
        // ...
        virtual void PrintPathname1() const = 0;
        virtual void PrintPathname2() const = 0;

    private:
        std::string const pathname_;
    };

    class File final : public FileEntity {
    public:
        // ...
        virtual void PrintPathname1() const override { std::cout << Pathname(); }
        virtual void PrintPathname2() const override { std::cout << Pathname(); }
    };

    class Dir final : public FileEntity {
    public:
        // ...
        virtual void PrintPathname1() const override { std::cout << Pathname() + "/"; }
        virtual void PrintPathname2() const override { std::cout << find_files(Pathname()); }
    };

    class OtherEntity final : public FileEntity {
    public:
        // ...
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

```plant_uml/visitor_ng2.pu
@startuml

class FileEntity {
    PrintPathname1()
    PrintPathname2()
}

class File {
    PrintPathname1()
    PrintPathname2()
}

class Dir {
    PrintPathname1()
    PrintPathname2()
}

class OtherEntity {
    PrintPathname1()
    PrintPathname2()
}

class Printer {
    PrintPathname1()
    PrintPathname2()
}

File  -up-|> FileEntity
Dir   -up-|> FileEntity
OtherEntity -up-|> FileEntity

Printer -> FileEntity

@enduml

```

これはポリモーフィズムによるリファクタリングの良い例と言えるが、
SRP(「[単一責任の原則(SRP)](#SS_2_1)」)に反するため、
Printerの関数が増えるたびにPrintPathname1、
PrintPathname2のようなFileEntityのインターフェースが増えてしまう。

このようなインターフェースの肥大化に対処するパターンがVisitorである。

上記例にVisitorを適用してリファクタリングした例を示す。

```cpp
    //  example/design_pattern/visitor.h 9

    class FileEntityVisitor {
    public:
        virtual void Visit(File const&)        = 0;
        virtual void Visit(Dir const&)         = 0;
        virtual void Visit(OtherEntity const&) = 0;
        // ...
    };

    class FileEntity {
    public:
        explicit FileEntity(std::string pathname) : pathname_{std::move(pathname)} {}
        // ...
        std::string const& Pathname() const { return pathname_; }

        virtual void Accept(FileEntityVisitor&) const = 0;  // Acceptの仕様は安定しているのでNVIは使わない。
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
    //  example/design_pattern/visitor.cpp 218

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

```plant_uml/visitor_ok.pu
@startuml
scale max 700 width

class FileEntityVisitor {
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

class PathnamePrinter1 {
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

class PathnamePrinter2 {
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

PathnamePrinter1 -up-|> FileEntityVisitor
PathnamePrinter2 -up-|> FileEntityVisitor

class FileEntity {
    Accept(FileEntityVisitor&)
}

class File {
    Accept(FileEntityVisitor&)
}

class Dir {
    Accept(FileEntityVisitor&)
}

class OtherEntity {
    Accept(FileEntityVisitor&)
}

FileEntityVisitor -up-> File
FileEntityVisitor -up-> Dir
FileEntityVisitor -up-> OtherEntity

File  -up-|> FileEntity
Dir   -up-|> FileEntity
OtherEntity -up-|> FileEntity

FileEntity -down-> FileEntityVisitor

Printer -right->FileEntityVisitor
Printer -right->FileEntity

@enduml
```

このリファクタリングには、

* FileEntityのインターフェースを小さくできる
* FileEntityVisitorから派生できるアルゴリズムについては、
  FileEntityのインターフェースに影響を与えずに追加できる
  (「[オープン・クローズドの原則(OCP)](#SS_2_2)」参照)

という利点がある。
一方で、この程度の複雑さの(単純な)例では、Visitorの適用によって以前よりも構造が複雑になり、
改悪してしまった可能性があるため、デザインパターンを使用する場合には注意が必要である。

なお、上記の抜粋である下記コード

```cpp
    //  example/design_pattern/visitor.h 38

    virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*this); }
```

はコードクローンだが、thisの型が違うため、
各Acceptが呼び出すFileEntityVisitor::Visit()も異り、単純に統一することはできない。
これを改めるためには、「[CRTP(curiously recurring template pattern)](#SS_8_1_4)」が必要になる。

このパターンを用いて、前記したFileEntityの3つの派生クラスが持つコードクローンを解消した例を以下に示す。

```cpp
    //  example/design_pattern/visitor_crtp.h 31

    class FileEntity {  // VisitorのFileEntityと同じ
    public:
        explicit FileEntity(std::string&& pathname) : pathname_{std::move(pathname)} {}
        virtual ~FileEntity() {}
        std::string const& Pathname() const { return pathname_; }

        virtual void Accept(FileEntityVisitor&) const = 0;  // Acceptの仕様は安定しているのでNVIは使わない。
    private:
        std::string const pathname_;
    };

    template <typename T>
    class AcceptableFileEntity : public FileEntity {  // CRTP
    public:
        virtual void Accept(FileEntityVisitor& visitor) const override { visitor.Visit(*static_cast<T const*>(this)); }

    private:
        // T : public AcceptableFileEntity<T> { ... };
        // 以外の使い方をコンパイルエラーにする
        AcceptableFileEntity(std::string&& pathname) : FileEntity{std::move(pathname)} {}
        friend T;
    };

    class File final : public AcceptableFileEntity<File> {  // CRTPでクローンを解消
    public:
        explicit File(std::string pathname) : AcceptableFileEntity{std::move(pathname)} {}
    };

    class Dir final : public AcceptableFileEntity<Dir> {  // CRTPでクローンを解消
    public:
        explicit Dir(std::string pathname) : AcceptableFileEntity{std::move(pathname)} {}
    };

    class OtherEntity final : public AcceptableFileEntity<OtherEntity> {  // CRTPでクローンを解消
    public:
        explicit OtherEntity(std::string pathname) : AcceptableFileEntity{std::move(pathname)} {}
    };
```

---

次に示すソースコードはVisitorとは関係がないが、
FileEntityVisitorから派生するクラスを下記クラス図が示すように改善することで、
単体テストが容易になる例である(「[DI(dependency injection)](#SS_3_3_1)」参照)。

```plant_uml/visitor_ut.pu
@startuml

class FileEntityVisitor {
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

class TestablePrinter {
    TestablePrinter(ostream&)
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

class PathnamePrinter1 {
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

class PathnamePrinter2 {
    Visit(File&)
    Visit(Dir&)
    Visit(OtherEntity&)
}

TestablePrinter -up-|> FileEntityVisitor
PathnamePrinter1 -up-|> TestablePrinter
PathnamePrinter2 -up-|> TestablePrinter

@enduml
```

```cpp
    //  example/design_pattern/visitor.h 71

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
    //  example/design_pattern/visitor.cpp 245

    void TestablePathnamePrinter1::Visit(File const& file) { ostream_ << file.Pathname(); }
    void TestablePathnamePrinter1::Visit(Dir const& dir) { ostream_ << dir.Pathname() + "/"; }
    void TestablePathnamePrinter1::Visit(OtherEntity const& other) { ostream_ << other.Pathname() + "(o1)"; }

    void TestablePathnamePrinter2::Visit(File const& file) { ostream_ << file.Pathname(); }

    void TestablePathnamePrinter2::Visit(Dir const& dir) { ostream_ << find_files(dir.Pathname()); }

    void TestablePathnamePrinter2::Visit(OtherEntity const& other) { ostream_ << other.Pathname() + "(o2)"; }
```

```cpp
    //  example/design_pattern/visitor_ut.cpp 28

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


### Proxy <a id="SS_3_2_6"></a>
Proxyとは代理人という意味で、
本物のクラスに代わり代理クラス(Proxy)が処理を受け取る
(実際は、処理自体は本物クラスに委譲されることもある)パターンである。

以下の順番で例を示すことで、Proxyパターンの説明を行う。

1. 内部構造を外部公開しているサーバ クラス
2. そのサーバをラッピングして、使いやすくしたサーバ クラス(Facadeパターン)
3. サーバをラップしたクラスのProxyクラス

まずは、内部構造を外部公開しているの醜悪なサーバの実装例である。

```cpp
    //  example/design_pattern/bare_server.h 5

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
    //  example/design_pattern/bare_server.cpp 9

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
    //  example/design_pattern/proxy_ut.cpp 17

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
    //  example/design_pattern/bare_server_wrapper.h 6

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
    //  example/design_pattern/bare_server_wrapper.cpp 8

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
    //  example/design_pattern/proxy_ut.cpp 56

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
    //  example/design_pattern/wrapped_server.h 5

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
    //  example/design_pattern/wrapped_server.cpp 8

    namespace {
    enum class Cmd {
        // ...
    };

    struct Packet {
        Cmd cmd;
    };
    }  // namespace

    // 以下、bare_server_wrapper.cppのコードとほぼ同じであるため省略。

    // ...
```

WrappedServerの使用例を下記する。当然ながらbare_wrapper_client()とほぼ同様になる。

```cpp
    //  example/design_pattern/proxy_ut.cpp 75

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
    //  example/design_pattern/wrapped_server_proxy.h 7

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
    //  example/design_pattern/wrapped_server_proxy.cpp 7

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

```plant_uml/proxy.pu
@startuml
class WrappedServer {
    Start()
    SayHello()
    SayGoodbye()
    Shutdown()
}

Client -right-> WrappedServer

WrappedServerProxy -up-|> WrappedServer

WrappedServerProxy --> WrappedServer
@enduml
```

なお、正確には下記のようなクラス構造をProxyパターンと呼ぶことが多いが、
ここでは単純さを優先した。

```plant_uml/proxy_general.pu
@startuml

class Subject {
    DoSomething()
}

class RealSubject {
    DoSomething()
}

class Proxy {
    DoSomething()
}

Proxy -up-|> Subject
RealSubject -up-|> Subject

Client -right-> Subject

Proxy -right-> RealSubject

@enduml

```



## アーキテクチャパターン(システムレベルの構造) <a id="SS_3_3"></a>

### DI(dependency injection) <a id="SS_3_3_1"></a>
メンバ関数内でクラスDependedのオブジェクトを直接、生成する
(もしくは[Singleton](#SS_3_1_1)オブジェクトや静的オブジェクト(std::coutやstd::cin等)に直接アクセスする)
クラスNotDIがあるとする。
この場合、クラスNotDIはクラスDependedのインスタンスに依存してしまう。
このような依存関係はクラスNotDIの可用性とテスト容易性を下げる。
これは、「仮にクラスDependedがデータベースをラップするクラスだった場合、
クラスNotDIの単体テストにデータベースが必要になる」ことからも容易に理解できる。

```cpp
    //  example/design_pattern/di_ut.cpp 8

    /// @brief NotDIや、DIから依存されるクラス
    class Depended {
        // ...
    };

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
    //  example/design_pattern/di_ut.cpp 37

    /// @brief DIを使う例。そのため、DIは、Dependedの型に依存している。
    class DI {
    public:
        explicit DI(std::unique_ptr<Depended>&& di_depended) noexcept : di_depended_{std::move(di_depended)} {}

        void DoSomething() { di_depended_->DoSomething(); }

    private:
        std::unique_ptr<Depended> di_depended_;
    };
```

下記は、クラスNotDIとクラスDIがそれぞれのDoSomething()を呼び出すまでのシーケンス図である。

```plant_uml/di.pu
@startuml

hide footbox

participant XXX
participant NotDI
participant DI

alt not use DI

    create NotDI
    XXX -> NotDI : new

    note left: DIを使わないパターン

    create Depended
    NotDI -> Depended : new

    XXX -> NotDI : DoSomething
    activate NotDI

        NotDI -> Depended : DoSomething
        activate Depended
        deactivate Depended

    deactivate NotDI

else use DI

    create Depended
    XXX -> Depended : depended = make_unique<Depended>()

    create DI
    XXX -> DI : new DI(depended)

    note left: DIを使うパターン

    XXX -> DI : DoSomething
    activate DI

        DI -> Depended : DoSomething
        activate Depended
        deactivate Depended

    deactivate DI
end

@enduml
```

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



### MVC <a id="SS_3_3_2"></a>

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

```plant_uml/mvc.pu
@startditaa

                    /------------\ 
        manipulate  |            |    use
       +------------+ Controller |<------------+
       |            |            |             |
       |            \------------/             |
       v                                      /-\   
   /-------\                                  \+/   
   |       |                                ---+--- 
   | Model |                                   | User
   |       |                                 +-+-+ 
   \---+---/                                 |   | 
       |               /------\                ^
       |               |      |                |
       +-------------->| View +----------------+
            update     |      |       see
                       \------/

@endditaa
```

制御の流れは、

1. ユーザの入力に応じてControllerのメソッドが呼び出される。
2. Controllerのメソッドは、ユーザの入力に応じた引数とともにModelのメソッドを呼び出す。
3. Modelは、それに対応するビジネスロジック等の処理を(通常、非同期に)行い、
自分自身の状態を変える(変わらないこともある)。
4. Modelの状態変化は、そのModelのオブザーバーとして登録されているViewに通知される。
5. Viewは関連するデータをModelから取得し、それを出力(UIに表示)する。

ViewはModelの[Observer](#SS_3_2_4)であるため、ModelはViewへ依存しない。
多々あるMVC派生パターンすべてで、そのような依存関係は存在しない
(具体的なパターンの選択はプロジェクトで使用するGUIフレームワークに強く依存する)。

そのようにする理由は下記の通りで、極めて重要な規則である。

* GUIのテストは目で見る必要がある(ことが多い)ため、Viewに自動単体テストを実施することは困難である。
  一方、ViewがModelに依存しないのであれば、Modelは自動単体テストをすることが可能である。
* 通常、Viewの仕様は不安定で、Modelの仕様は安定しているため、Modelのソースコード変更は
  Viewのそれよりもかなり少ない。
  しかし、ModelがViewに依存してしまうと、Viewに影響されModelのソースコード変更も多くなる。





<!-- ./md/template_meta_programming.md -->
# テンプレートメタプログラミング <a id="SS_4"></a>

本章でのテンプレートメタプログラミングとは、下記の2つを指す。

* ジェネリックプログラミング
* メタプログラミング

C++においては、この2つはテンプレートを用いたプログラミングとなる。

ジェネリックプログラミングとは、具体的なデータ型に依存しない抽象的プログラミングであり、
その代表的な成果物はSTLのコンテナやそれらを扱うアルゴリズム関数テンプレートである。

この利点は、

* i種の型
* j種のコンテナ
* k種のアルゴリズム

の開発を行うことを考えれば明らかである。

ジェネリックプログラミングが無ければ、コンテナの種類はi x j個必要になり、
それらに適用するアルゴリズム関数は、i x j x k個必要になる。
また、サポートする型の増加に伴いコンテナやアルゴリズム関数は指数関数的に増えて行く。
C言語のqsort()のように強引なキャストを使い、この増加をある程度食い止めることはできるが、
それによりコンパイラによる型チェックは無効化され、
静的な型付け言語を使うメリットの多くを失うことになる。

メタプログラミングとは、

* ジェネリックのサポート
* 実行時コードの最適化
* 関数やクラスを生成するコードのプログラミング

のような目的で行われるテンプレートプログラミングの総称である。

ジェネリックプログラミングとメタプログラミングに明確な境界はない、
また明確にしたところで大きなメリットはと思われるため、
本章では、これらをまとめた概念であるテンプレートメタプログラミングとして扱い、
ログ取得ライブラリやSTLを応用したNstdライブラリの実装を通して、
これらのテクニックや、使用上の注意点について解説する。

c++20から導入された[コンセプト](#SS_6_11_3)によりジェネリックプログラミングは、
開発容易性、可読性、保守性が大きく向上しため、この章のコード例には、
[コンセプト](#SS_6_11_3)(`concept`, `requires`)を多用した。

が、この副作用として、
c++17までしか使えない読者の参考にならないコードが増えてしまうことを避けるため、
以下のような`#ifdef`を使うことによりc++17でも使えるコード例となるようにした
(本来、`#ifdef`は使うべきではないが、`#ifdef`の数少ない使いどころだと判断した)。

```cpp
    //  example/template/cplusplus.cpp 4

    #if __cplusplus >= 202002L  // c++20
    // c++20以上の機能を使い、c++17以下の機能ではill-formedとなるコード
    template <typename T, typename U>
    concept same_as = requires(T const* t, U const* u)
    {
        {t = u, u = t};
    };

    #else  // c++17以下の機能を使い上記のコードと同じ機能を持つ実装
    template <typename T, typename U>
    inline constexpr bool same_as = std::is_same_t<T, U>;
    #endif
```
___

__この章の構成__

&emsp;&emsp; [ログ取得ライブラリの開発](#SS_4_1)  
&emsp;&emsp;&emsp; [要件](#SS_4_1_1)  
&emsp;&emsp;&emsp; [ログ取得ライブラリのインターフェース](#SS_4_1_2)  
&emsp;&emsp;&emsp; [パラメータパックを使用したテクニック](#SS_4_1_3)  
&emsp;&emsp;&emsp; [Loggerの実装](#SS_4_1_4)  
&emsp;&emsp;&emsp; [ユーザ定義型とそのoperator\<\<のname lookup](#SS_4_1_5)  
&emsp;&emsp;&emsp; [Ints_tのログ登録](#SS_4_1_6)  

&emsp;&emsp; [Nstdライブラリの開発](#SS_4_2)  
&emsp;&emsp;&emsp; [Nstdライブラリを使用したリファクタリング](#SS_4_2_1)  
&emsp;&emsp;&emsp; [安全なvector](#SS_4_2_2)  
&emsp;&emsp;&emsp; [安全な配列型コンテナ](#SS_4_2_3)  
&emsp;&emsp;&emsp; [初期化子リストの副作用](#SS_4_2_4)  

&emsp;&emsp; [メタ関数のテクニック](#SS_4_3)  
&emsp;&emsp;&emsp; [is_void_xxxの実装](#SS_4_3_1)  
&emsp;&emsp;&emsp; [is_same_xxxの実装](#SS_4_3_2)  
&emsp;&emsp;&emsp; [AreConvertibleXxxの実装](#SS_4_3_3)  
&emsp;&emsp;&emsp; [関数の存在の診断](#SS_4_3_4)  

&emsp;&emsp; [Nstdライブラリの開発2](#SS_4_4)  
&emsp;&emsp;&emsp; [SafeArray2の開発](#SS_4_4_1)  
&emsp;&emsp;&emsp; [Nstd::SafeIndexの開発](#SS_4_4_2)  
&emsp;&emsp;&emsp; [Nstd::SafeIndexのoperator\<\<の開発](#SS_4_4_3)  
&emsp;&emsp;&emsp; [コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)  

&emsp;&emsp; [Nstdライブラリの開発3(浮動小数点関連)](#SS_4_5)  
&emsp;&emsp;&emsp; [浮動小数点の比較](#SS_4_5_1)  
&emsp;&emsp;&emsp; [固定小数点クラス](#SS_4_5_2)  
&emsp;&emsp;&emsp; [固定小数点リテラル](#SS_4_5_3)  
&emsp;&emsp;&emsp; [有理数クラス](#SS_4_5_4)  
&emsp;&emsp;&emsp; [有理数リテラル](#SS_4_5_5)  

&emsp;&emsp; [ログ取得ライブラリの開発2](#SS_4_6)  
&emsp;&emsp; [その他のテンプレートテクニック](#SS_4_7)  
&emsp;&emsp;&emsp; [forwardingリファレンスとstd::forward](#SS_4_7_1)  
&emsp;&emsp;&emsp; [ジェネリックラムダによる関数内での関数テンプレートの定義](#SS_4_7_2)  
&emsp;&emsp;&emsp; [クラステンプレートと継承の再帰構造](#SS_4_7_3)  
&emsp;&emsp;&emsp; [意図しないname lookupの防止](#SS_4_7_4)  
&emsp;&emsp;&emsp; [Nstd::Type2Strの開発](#SS_4_7_5)  
&emsp;&emsp;&emsp; [静的な文字列オブジェクト](#SS_4_7_6)  
&emsp;&emsp;&emsp; [関数型をテンプレートパラメータで使う](#SS_4_7_7)  

&emsp;&emsp; [注意点まとめ](#SS_4_8)  
  
  

[インデックス](#SS_1_2)に戻る。  
___

## ログ取得ライブラリの開発 <a id="SS_4_1"></a>
ここではログ取得ライブラリの開発を行う。

### 要件 <a id="SS_4_1_1"></a>

ログ取得ライブラリの要件は、

* ソースコードの場所とそこで指示されたオブジェクトの値を文字列で保持する
* 後からそれらを取り出せる

ことのみとする。下記はその文字列を取り出した例である。

```
    app/src/main.cpp: 96:Options
                         cmd       : GenPkg
                         in        : 
                         out       : 
                         recursive : true
                         src_as_pkg: false
        ...

    app/src/main.cpp: 51:start GenPkg

    file_utils/ut/path_utils.cpp: 38:1
    file_utils/ut/path_utils.cpp: 48:ut_data/app1
                         ut_data/app1/mod1
                         ut_data/app1/mod2

        ...

    app/src/main.cpp:100:Exit:0
```

単純化のためログの番号やタイムスタンプのサポートはしない。
また、実行速度や仕様メモリ量の制限等も本章の趣旨とは離れるため考慮しない。

### ログ取得ライブラリのインターフェース <a id="SS_4_1_2"></a>

ログ取得コードにより、コードクローンが増えたり、主なロジックの可読性が下がったのでは、
本末転倒であるため、下記のようにワンライナーで記述できるべきだろう。

```cpp
    LOGGER("start GenPkg", objA, objB, objC);
```

また、要件で述べた通り、ソースコード位置を特定できなければならないため、
上記LOGGERは下記のような関数型マクロにならざるを得ない。

```cpp
    #define LOGGER(...) CppLoggerFunc(__FILE__, __LINE__, __VA_ARGS__)
```

CppLoggerFuncをクラス外の関数として実装した場合、ログ保持のための静的なオブジェクトが必要になる。
これは避けるべきなので、「[Singleton](#SS_3_1_1)」で述べた構造を導入すると、

```cpp
    #define LOGGER(...) Logger::Inst().Set(__FILE__, __LINE__, __VA_ARGS__)
```

のような関数型マクロとなる。これがログ取得ライブラリの主なインターフェースとなる。

C言語プログラミングばかりをやりすぎて、
視神経と手の運動神経が直結してしまった大脳レス・プログラマーは、

```cpp
    __VA_ARGS__
```

を見るとprintf(...)のような可変長引数を取る関数を思い浮かべる。
「人は一昨日も行ったことを昨日も行ったという理由で、今日もそれを行う」
という諺を思い出すと気持ちは分からなくもないが、 
C++ではprintf(...)のような危険な可変長引数を取る関数を作ってはならない。
[パラメータパック](#SS_6_11_4)を使って実装するべきである。

### パラメータパックを使用したテクニック <a id="SS_4_1_3"></a>
[パラメータパック](#SS_6_11_4)を使用するには独特なテクニックが必要となるため、まずは単純な例から説明する。

次のような単体テストをパスする関数テンプレートsumをパラメータパックで実装することを考える。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 26

    ASSERT_EQ(1, sum(1));
    ASSERT_EQ(3, sum(1, 2));
    ASSERT_EQ(6, sum(1, 2, 3));
    ASSERT_FLOAT_EQ(6.0, sum(1, 2.0, 3.0));
    ASSERT_EQ(10, sum(1, 2, 3, 4));

    // ...

    ASSERT_EQ(55, sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

    // ...
```

sumの要件は、

* 可変長引数を持つ
* [算術型](#SS_6_1_3)の引数と戻り値を持つ
* すべての引数の和を返す

のようなものになるため、関数テンプレートsumは下記のように書ける。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 9

    template <typename HEAD>
    int sum(HEAD head)
    {
        return head;
    }

    template <typename HEAD, typename... TAIL>
    int sum(HEAD head, TAIL... tails)
    {
        return head + sum(tails...);
    }
```

1つ目の関数テンプレートsumは引数が一つの場合に対応する。
2つ目の関数テンプレートsumは引数が2つ以上の場合に対応する。

2つ目の関数テンプレートsumのテンプレートパラメータ

```cpp
    typename... TAIL
```

がパラメータパックであり、0個以上の型が指定されることを意味する。
これを関数の引数として表すシンタックスが

```cpp
    TAIL... tails
```

であり、同様に0個以上のインスタンスが指定されることを表している。

HEADとTAILより、2つ目のsumは1個以上の引数を取れることになるため、
引数が1つの場合、どちらのsumを呼び出すかが曖昧になるように思えるが、
ベストマッチの観点から1つ目のsumが呼び出される。

sum(1, 2, 3)の呼び出し時のsumの展開を見てみることでパラメータパックの振る舞いを解説する。

この呼び出しは、2つ目のsumにマッチする。従って下記のように展開される。

```cpp
    return 1 + sum(2, 3);
```

sum(2, 3)も同様に展開されるため、上記コードは下記のようになる。

```cpp
    return 1 + 2 + sum(3);
```

sum(3)は1つ目のsumにマッチするため、最終的には下記のように展開される。

```cpp
    return 1 + 2 + 3;
```

これで基本的な要件は満たしたが、このsumでは下記のようなコードもコンパイルできてしまう。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 43

    ASSERT_EQ(2, sum(1, true, false));
```

これを認めるかどうかはsumの仕様次第だが、ここではこれらを認めないようにしたい。
また、引数に浮動小数が与えられた場合でも、sumの戻り値の型がintなる仕様には問題がある。
合わせてそれも修正する。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 53

    template <typename HEAD>
    auto sum(HEAD head)
    {
        // std::is_sameの2パラメータが同一であれば、std::is_same<>::value == true
        static_assert(!std::is_same<HEAD, bool>::value, "arguemnt type must not be bool.");

        return head;
    }

    template <typename HEAD, typename... TAIL>
    auto sum(HEAD head, TAIL... tails)
    {
        // std::is_sameの2パラメータが同一であれば、std::is_same<>::value == true
        static_assert(!std::is_same<HEAD, bool>::value, "arguemnt type must not be bool.");

        return head + sum(tails...);
    }
```
```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 83

    // boolを除く算術型のみ認めるため、下記はコンパイルできない。
    // ASSERT_EQ(2, sum(1, true, false));

    auto i1 = sum(1);
    auto i2 = sum(1, 2);

    static_assert(std::is_same<int, decltype(i1)>::value);  // 1の型はint
    static_assert(std::is_same<int, decltype(i2)>::value);  // 1 + 2の型はint

    auto u1 = sum(1U);
    auto u2 = sum(1U, 2);

    static_assert(std::is_same<unsigned int, decltype(u1)>::value);  // 1Uの型はunsigned int
    static_assert(std::is_same<unsigned int, decltype(u2)>::value);  // 1U + 2の型はunsigned int

    auto f0 = sum(1.0, 1.2);
    static_assert(std::is_same<double, decltype(f0)>::value);

    // ただし、戻り型をautoにしたため、下記も認められるようになった。
    // これに対しての対処は別の関数で行う。
    auto str = sum(std::string{"1"}, std::string{"2"});

    ASSERT_EQ(str, "12");
    static_assert(std::is_same<std::string, decltype(str)>::value);
```

以上で示したようにパラメータパックにより、
C言語での可変長引数関数では不可能だった引数の型チェックができるようになったため、
C言語でのランタイムエラーがコンパイルエラーにできるようになった。

なお、上記コードで使用した[std::is_same](#SS_7_2_4)は、
与えられた2つのテンプレートパラメータが同じ型であった場合、
valueをtrueで初期化するクラステンプレートであり、 type_traitsで定義されている
(後ほど使用するstd::is_same_vはstd::is_same<>::valueと等価な定数テンプレート)。
この実装については、後ほど説明する。


#### パラメータパックの畳みこみ式 <a id="SS_4_1_3_1"></a>
上記したsumは、パラメータパックの展開に汎用的な再帰構造を用いたが、
C++17で導入された畳みこみ式を用い、以下の様に簡潔に記述することもできる。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 123

    template <typename... ARGS>
    auto sum(ARGS... args)
    {
        return (args + ...);  // 畳みこみ式は()で囲まなければならない。
    }
```
```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 134

    ASSERT_EQ(1, sum(1));
    ASSERT_EQ(3, sum(1, 2));
    ASSERT_EQ(6, sum(1, 2, 3));
    ASSERT_EQ(6.0, sum(1, 2.0, 3.0));
    ASSERT_EQ(10, sum(1, 2, 3, 4));
    ASSERT_EQ(55, sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
```

畳みこみ式で使用できる演算子を以下に示す。

```
    + - * / % ^ & | = < > << >> += -= *= /= %= ^= &= |= <<= >>= == != <= >= && || , .* ->*
```

これらの演算子がオーバーロードである場合でも、畳みこみ式は利用できる。


#### 前から演算するパラメータパック <a id="SS_4_1_3_2"></a>
パラメータパックを使うプログラミングでは、
上記したHEADとTAILによるリカーシブコールがよく使われるパターンであるが、
これには後ろから処理されるという、微妙な問題点がある。

これまでのsumに代えて下記のようなproduct(掛け算)を考える。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 149

    template <typename HEAD>
    auto product(HEAD head)
    {
        static_assert(!std::is_same_v<HEAD, bool>, "arguemnt type must not be bool.");
        static_assert(std::is_arithmetic_v<HEAD>, "arguemnt type must be arithmetic.");

        return head;
    }

    template <typename HEAD, typename... TAIL>
    auto product(HEAD head, TAIL... tails)
    {
        static_assert(!std::is_same_v<HEAD, bool>, "arguemnt type must not be bool.");
        static_assert(std::is_arithmetic_v<HEAD>, "arguemnt type must be arithmetic.");

        return head * product(tails...);
    }
```

このコードの単体テストは、

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 173

    ASSERT_EQ(1, product(100, 0.1, 0.1));
```

のようになるだろうが、
std::numeric_limits<>::epsilonを使用していないため
(「[浮動小数点型](#SS_6_1_12)」参照)
、このテストはパスしない。一方で、以下のテストはパスする。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 178

    ASSERT_EQ(1, product(0.1, 0.1, 100));

```

一般に0.01の2進数表現は無限小数になるため、これを含む演算にはepsilon以下の演算誤差が発生する。
前者単体テストでは、後ろから演算されるために処理の途中に0.01が現れるが、
後者では現れないため、この誤差の有無が結果の差になる。

このような演算順序による微妙な誤差が問題になるような関数を開発する場合、
演算は見た目の順序通りに行われた方が良いだろう。
ということで、productを前から演算するように修正する。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 196

    template <typename HEAD>
    auto product(HEAD head)
    {
        static_assert(!std::is_same_v<HEAD, bool>, "arguemnt type must not be bool.");
        static_assert(std::is_arithmetic_v<HEAD>, "arguemnt type must be arithmetic.");

        return head;
    }

    template <typename HEAD, typename HEAD2, typename... TAIL>
    auto product(HEAD head, HEAD2 head2, TAIL... tails)
    {
        static_assert(!std::is_same_v<HEAD, bool>, "arguemnt type must not be bool.");
        static_assert(std::is_arithmetic_v<HEAD>, "arguemnt type must be arithmetic.");

        return product(head * head2, tails...);
    }
```

HEAD、TAILに加えHEAD2を導入することで、前からの演算を実装できる
(引数が一つのproductに変更はない)。当然ながら、これにより、

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 220

    ASSERT_EQ(1, product(100, 0.1, 0.1));
```

はパスし、下記はパスしなくなる。

```cpp
    //  example/template_cpp17/parameter_pack_ut.cpp 225

    ASSERT_EQ(1, product(0.1, 0.1, 100));

```


### Loggerの実装 <a id="SS_4_1_4"></a>

パラメータパックを使用したログ取得コードは以下のようになる。

```cpp
    //  example/template/logger_0.h 48

    #define LOGGER_P(...) Logging::Logger::Inst().Set(__FILE__, __LINE__)
    #define LOGGER(...) Logging::Logger::Inst().Set(__FILE__, __LINE__, __VA_ARGS__)
```

予定していたものと若干違う理由は、\_\_VA\_ARGS\_\_が1個以上の識別子を表しているからである。
従って、通過ポイントのみをロギングしたい場合、LOGGER_P()を使うことになる。
gcc拡張を使えば、LOGGER_PとLOGGERを統一できるが、そのようなことをすると別のコンパイラや、
静的解析ツールが使用できなくなることがあるため、残念だが上記のように実装するべきである。

Loggerクラスの実装は、下記のようになる。

```cpp
    //  example/template/logger_0.h 6

    namespace Logging {
    class Logger {
    public:
        static Logger&       Inst();
        static Logger const& InstConst() { return Inst(); }

        std::string Get() const;  // ログデータの取得
        void        Clear();      // ログデータの消去

        template <typename... ARGS>  // ログの登録
        void Set(char const* filename, uint32_t line_no, ARGS const&... args)
        {
            oss_.width(32);
            oss_ << filename << ":";

            oss_.width(3);
            oss_ << line_no;

            set_inner(args...);
        }

        Logger(Logger const&)            = delete;
        Logger& operator=(Logger const&) = delete;

    private:
        void set_inner() { oss_ << std::endl; }

        template <Nstd::Printable HEAD, Nstd::Printable... TAIL>
        void set_inner(HEAD const& head, TAIL const&... tails)
        {
            oss_ << ":" << head;
            set_inner(tails...);
        }

        Logger() {}
        std::ostringstream oss_{};
    };
    }  // namespace Logging
```

すでに述べた通り、

* クラスはシングルトンにする
* パラメータパックにより可変長引数を実現する

ようにした。
また、識別子の衝突を避けるために、名前空間Loggingを導入し、Loggerはその中で宣言した。

次に、どのように動作するのかを単体テストで示す。

```cpp
    //  example/template/logger_0_ut.cpp 16

    auto a = 1;
    auto b = std::string{"b"};

    LOGGER_P();               // (1)
    LOGGER(5, "hehe", a, b);  // (2)
    auto line_num = __LINE__;

    auto s = Logging::Logger::InstConst().Get();

    auto exp = std::string{log_str_exp(__FILE__, line_num - 2, "\n")};  // (1)のログ
    exp += log_str_exp(__FILE__, line_num - 1, ":5:hehe:1:b\n");        // (2)のログ
    ASSERT_EQ(exp, s);

    Logging::Logger::Inst().Clear();  // クリアの確認
    ASSERT_EQ("", Logging::Logger::InstConst().Get());
```

行を含む出力の期待値をソースコードに直接書くと行増減のたびにそれらを修正する必要ある。
期待値の一部を自動計算する下記コード(上記コードで使用)を単体テストに導入することで、
そういった修正を避けている。

```cpp
    //  example/template/logger_ut.h 4

    inline std::string line_to_str(uint32_t line)
    {
        if (line < 10) {
            return ":  ";
        }
        else if (line < 100) {
            return ": ";
        }
        else if (line < 1000) {
            return ":";
        }
        else {
            assert(false);  // 1000行を超える単体テストファイルを認めない
            return "";
        }
    }

    inline std::string log_str_exp(char const* filename_cstr, uint32_t line, char const* str)
    {
        auto const filename = std::string{filename_cstr};
        auto const len      = 32 > filename.size() ? 32 - filename.size() : 0;
        auto       ret      = std::string(len, ' ');

        ret += filename;
        ret += line_to_str(line);
        ret += std::to_string(line);
        ret += str;

        return ret;
    }
```

アプリケーションの開発では、
下記のようなユーザが定義した名前空間とクラスを用いることがほとんどである。

```cpp
    //  example/template/app_ints.h 12

    namespace App {

    class X {
    public:
        X(std::string str, int num) : str_{std::move(str)}, num_{num} {}
        std::string ToString() const { return str_ + "/" + std::to_string(num_); }
        // ...
    };
    }  // namespace App
```

このApp::Xのインスタンスのログを取得できることも、当然Logging::Loggerの要件となる。
従って、下記の単体テストはコンパイルでき、且つパスすることが必要になる。


```cpp
    //  example/template/logger_0_ut.cpp 42

    auto x = App::X{"name", 3};

    LOGGER(1, x);
    auto line_num = __LINE__;

    auto s = Logging::Logger::InstConst().Get();

    auto exp = std::string{log_str_exp(__FILE__, line_num - 1, ":1:name/3\n")};
    ASSERT_EQ(exp, s);
```

Logging::Loggerのコードからオブジェクトのログを登録するためには、
Logging::Logger::set_innerがコンパイルできなければならない。
つまり、

```cpp
    std::ostream& operator<<(std::ostream&, ログ登録オブジェクトの型)
```

の実装が必要条件となる。App::Xでは下記のようなコードになる。

```cpp
    //  example/template/app_ints.h 28

    namespace App {

    inline std::ostream& operator<<(std::ostream& os, X const& x) { return os << x.ToString(); }
    }  // namespace App
```

他の任意のユーザ定義型に対しても、このようにすることでログ登録が可能になる。

なお、ヒューマンリーダブルな文字列でその状態を表示できる関数をユーザ定義型に与えることは、
デバッガを使用したデバッグ時にも有用である。

### ユーザ定義型とそのoperator\<\<のname lookup <a id="SS_4_1_5"></a>

ここで、一旦Logging::Loggerの開発を止め、
Logging::Logger::set_innerでのApp::operator<<の[name lookup](#SS_6_12_2)について考えてみることにする。

ここまでで紹介したログ取得ライブラリやそれを使うユーザ定義型等の定義、宣言の順番は、

1. Logging::Logger
2. App::X
3. App::operator<<
4. 単体テスト(Logger::set_innerのインスタンス化される場所)

となっている。
name lookupの原則に従い、App::Xの宣言は、App::operator<<より前に行われている。
これを逆にするとコンパイルできない。
しかし、Logging::Loggerは、後から宣言されたApp::operator<<を使うことができる。
多くのプログラマは、これについて気づいていないか、その理由を間違っての認識している。

その認識とは、「テンプレート内の識別子の[name lookup](#SS_6_12_2)は、
それがインスタンス化される時に行われる」というものであり、これにより
「 Logging::Loggerのname lookupは単体テスト内で行われる。
それはApp::operator<<宣言後であるためコンパイルできる」と考えることができるが、
[two phase name lookup](#SS_6_12_3)で行われるプロセスと反するため誤りである。

まずは、この認識の誤りを下記のコードで説明する。

```cpp
    //  example/template/logger_0_ut.cpp 68

    namespace App2 {
    class X {
    public:
        explicit X(std::string str, int num) : str_{std::move(str)}, num_{num} {}
        std::string ToString() const { return str_ + "/" + std::to_string(num_); }
        // ...
    };
    }  // namespace App2

    namespace App3 {  // App3をApp2にすればコンパイルできる
    std::ostream& operator<<(std::ostream& os, App2::X const& x) { return os << x.ToString(); }
    }  // namespace App3

    namespace {

    TEST(Template, logger_0_X_in_AppX)
    {
        Logging::Logger::Inst().Clear();

        auto x = App2::X{"name", 3};

        using namespace App3;  // この記述は下記のエラーに効果がない

        LOGGER(1, x);  // ここがコンパイルエラーとなる
        auto line_num = __LINE__;

        auto s = Logging::Logger::InstConst().Get();

        auto exp = std::string{log_str_exp(__FILE__, line_num - 1, ":1:name/3\n")};
        ASSERT_EQ(exp, s);
    }
    }  // namespace
```

このコードは、もともとのコードの名前空間名をApp2とApp3にしただけのものである。
もし、前記した「認識」の内容が正しいのであれば、このコードもコンパイルできるはずであるが
(実際にApp3と書いた部分をApp2に書き換えればコンパイルできる)、
実際には下記のようなエラーが発生する。


```
    logger_0.h:37:21: error: no match for ‘operator<<’ 
    (operand types are ‘std::basic_ostream<char>’ and ‘const App2::X’)
       37 |         oss_ << ":" << head;
          |         ~~~~~~~~~~~~^~~~~~~

```

エラー内容からoperator<<が発見できないことは明らかである。
単体テスト内でのusing namespace App3はLogging::Logger::set_innerの宣言より後に書かれているため、
このエラーを防ぐ効果はない。

Logging::Logger::set_innerの中でusing namespace App3とした上で、
two phase name lookupの原則に従い、
App2::XとApp3::operator<<をLogging::Loggerの宣言より前に宣言することで、
ようやくコンパイルすることができる。

名前空間Appの例と名前空間App2、App3の例での本質的な違いは、
「型Xとそのoperator<<が同じ名前空間で宣言されているかどうか」である。

名前空間Appの例の場合、型Xとそのoperator<<が同じ名前空間で宣言されているため、
[ADL](#SS_6_12_5)(実引数依存探索)が働く。
また、Logging::Logger::set_inner(x)はテンプレートであるため、[two phase name lookup](#SS_6_12_3)
が使用される。
その結果、Logging::Logger::set_inner(x)でのname lookupの対象には、
「Logging::Logger::set_inner(x)がインスタンス化される場所
(単体テスト内でのLOGGER_PやLOGGERが使われている場所)より前方で宣言された名前空間App」も含まれる。
こういったメカニズムにより、
Logging::Logger::set_inner定義位置の後方で宣言されたApp::operator<<も発見できることになる。

一方で、名前空間App2、App3の例では、型XがApp2で宣言されているため、
Logging::Logger::set_inner(x)でのname lookupの対象にApp3は含ず、
App3::operator<<は発見されない(繰り返すが、インスタン化の場所直前でのusing nameには効果がない)。

型Xとそのoperator<<を同じ名前空間で宣言することは本質的に重要なことであるが、
名前空間を使用する場合、自然にそのような構造になるため、
その重要性の理由を知る必要はないように思われる。
しかし、次の例で示すようにこのメカニズムを知らずに解決することができないケースが存在する。

### Ints_tのログ登録 <a id="SS_4_1_6"></a>
話題はログ取得ライブラリの開発に戻る。
アプリケーションの開発では、下記のように宣言された型エイリアスを使うことは珍しくない。

```cpp
    //  example/template/app_ints.h 6

    namespace App {
    using Ints_t = std::vector<int>;
    }
```

そのoperator<<を下記のように定義したとする。

```cpp
    //  example/template/logger_0_ut.cpp 109

    namespace App {
    std::ostream& operator<<(std::ostream& os, Ints_t const& ints)
    {
        auto sep = "";

        for (auto const i : ints) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
    }  // namespace App
```

単体テストは下記のように書けるが、残念ながらコンパイルエラーになり、

```cpp
    //  example/template/logger_0_ut.cpp 131

    auto ints = App::Ints_t{1, 2, 3};

    auto oss = std::ostringstream{};

    oss << ints;
    ASSERT_EQ("1, 2, 3", oss.str());
```

下記のようなエラーメッセージが表示される。

```
    logger_0_ut.cpp:140:9: error: no match for ‘operator<<’
        (operand types are ‘std::ostringstream’ {aka ‘std::basic_ostringstream<char>’}
         and ‘App::Ints_t’ {aka ‘std::vector<int>’})
      140 |     oss << ints;
          |     ~~~ ^~ ~~~~
          |     |      |
          |     |      App::Ints_t {aka std::vector<int>}
          |     std::ostringstream {aka std::basic_ostringstream<char>}
```

Ints_tはAppで定義されているが、実際の型はstdで定義されているため、
instsの[関連名前空間](#SS_6_12_6)もstdであり、Appではない。
その結果App::operator<<は発見できず、このようなエラーになった。

LOGGERからApp::operator<<を使う場合の単体テストは下記のようになるが、
[ADL](#SS_6_12_5)によってLogging::Logger::set_inner(ints)内に導入される名前空間はstdのみであり、
前記単体テスト同様にコンパイルできない。

```cpp
    //  example/template/logger_0_ints_ut.h 8

    auto ints = App::Ints_t{1, 2, 3};

    LOGGER("Ints", ints);
    auto line_num = __LINE__;

    auto s = Logging::Logger::InstConst().Get();

    auto exp = std::string{log_str_exp(__FILE__, line_num - 1, ":Ints:1, 2, 3\n")};
    ASSERT_EQ(exp, s);
```

この解決方法は、

* [operator\<\<をstd内で宣言する](#SS_4_1_6_1)
* [operator\<\<をグローバル名前空間内で宣言する](#SS_4_1_6_2)
* [operator\<\<をLogging内で宣言する](#SS_4_1_6_3)
* [Logging::Logger::set_inner(ints)内でusing namespace Appを行う](#SS_4_1_6_4)
* [Ints_tを構造体としてApp内に宣言する](#SS_4_1_6_5)
* [operator\<\<を使わない](#SS_4_1_6_6)

のようにいくつか考えられる。以下では、順を追ってこれらの問題点について解説を行う。


#### operator\<\<をstd内で宣言する <a id="SS_4_1_6_1"></a>
ここで解決したい問題は、すでに示した通り、
「[ADL](#SS_6_12_5)によってLogging::Logger::set_inner(ints)内に導入される名前空間はstdである」
ことにって発生する。であれば、App内でのoperator<<の宣言をstdで行えばコンパイルできるはずである。
下記はその変更を行ったコードである。

```cpp
    //  example/template/app_ints.h 6

    namespace App {
    using Ints_t = std::vector<int>;
    }
```
```cpp
    //  example/template/logger_0_std_ut.cpp 11

    namespace std {  // operator<<の定義をstdで行う
    ostream& operator<<(std::ostream& os, App::Ints_t const& ints)
    {
        auto sep = "";

        for (auto const& i : ints) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
    }  // namespace std
```

上記コードは[two phase name lookup](#SS_6_12_3)等の効果により、想定通りコンパイルできるが、
stdをユーザが拡張することは一部の例外を除き未定義動作を引き起こす可能性があり、
たとえこのコードがうまく動作したとしても
(実際、このコードはこのドキュメント作成時には正常動作している)、
未来においてその保証はなく、このようなプログラミングは厳に避けるべきである。


#### operator\<\<をグローバル名前空間内で宣言する <a id="SS_4_1_6_2"></a>
すでに述べた通り、
「ADLによってLogging::Logger::set_inner(ints)内に導入される名前空間はstdのみである」ため、
この関数の中でのname lookupに使用される名前空間は、std、グローバル名前空間、
Loggerを宣言しているLoggingの3つである。

ここでは、下記のコードのようにグローバル名前空間内でのoperator<<の宣言を試す。

```cpp
    //  example/template/app_ints.h 6

    namespace App {
    using Ints_t = std::vector<int>;
    }
```
```cpp
    //  example/template/logger_0_global_ut.cpp 10

    // グローバル名前空間
    std::ostream& operator<<(std::ostream& os, App::Ints_t const& ints)
    {
        auto sep = "";

        for (auto const& i : ints) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
```

このドキュメントで使用している[g++](#SS_8_13_1)ではこのコードはコンパイルでき、
動作も問題ないように思われるが、[clang++](#SS_8_13_2)では以下のようなエラーが発生し、コンパイルできない。

```
    ./logger_0.h:37:21: error: call to function 'operator<<' that is neither 
    visible in the tem plate definition nor found by argument-dependent lookup
            oss_ << ":" << head;
```

この理由は「[two phase name lookup](#SS_6_12_3)」の後半で詳しく解説したので、ここでは繰り返さないが、
このようなコードを使うと、コード解析ツール等が使用できなくなることがあるため、
避けるべきである
。

多くのプログラマは、コードに問題があるとしても、
それが意図通りに動くように見えるのであればその問題を無視する。
今回のような難題に対しては、なおさらそのような邪悪な欲求に負けやすい。
そのような観点でclang++が吐き出したエラーメッセージを眺めると、上記したメッセージの後に、
下記のような出力を見つけるかもしれない。

```
    logger_0_global_ut.cpp:13:15: note: 'operator<<' should be declared prior to the call site
    std::ostream& operator<<(std::ostream& os, App::Ints_t const& ints)
```

clang++は「LOGGERの前にoperator<<を宣言せよ」と言っている。
実際そうすれば、clang++でのコンパイルも通り、単体テストもパスする。
しかし、それには下記のような問題がある。

* operator<<(std::ostream& os, App::Ints_t const& ints)
  という名前空間Appローカルな宣言をグローバル名前空間で行うことによって、
  グローバル名前空間を汚染してしまう
  (このコードは名前空間を正しく使うことに対しての割れ窓
  (「[割れ窓理論](#SS_8_14_2)」参照)になってしまうかもしれない)。
* 例示したコードでのoperator<<(std::ostream& os, App::Ints_t const& ints)の定義は、
  単体テストファイル内にあったが、実際には何らかのヘッダファイル内で定義されることになる。
  その場合、ロガーのヘッダファイルよりも、
  そのヘッダファイルを先にインクルードしなければならなくなる。
  これは大した問題ではないように見えるが、
  ヘッダファイル間の暗黙の依存関係を生み出し将来の保守作業を難しくさせる。


以上述べた理由からこのアイデアを選択するべきではない。


#### operator\<\<をLogging内で宣言する <a id="SS_4_1_6_3"></a>
前節でのグローバル名前空間内でのoperator<<の宣言はうまく行かなかったので、
同様のことをLoggingで試す。

```cpp
    //  example/template/app_ints.h 6

    namespace App {
    using Ints_t = std::vector<int>;
    }
```
```cpp
    //  example/template/logger_0_logging_ut.cpp 10

    namespace Logging {  // operator<<の定義をLoggingで行う
    std::ostream& operator<<(std::ostream& os, App::Ints_t const& ints)
    {
        auto sep = "";

        for (auto const& i : ints) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
    }  // namespace Logging
```

動作はするものの、当然ながら結果は「[operator\<\<をグローバル名前空間内で宣言する](#SS_4_1_6_2)」
で述べた状況とほぼ同様であるため、このアイデアを採用することはできない。

#### Logging::Logger::set_inner(ints)内でusing namespace Appを行う <a id="SS_4_1_6_4"></a>
Logging::Logger::set_inner(ints)内でusing namespace Appを行えば、
意図通りに動作させることができるが、App内のロギングは名前空間Loggingに依存するため、
AppとLoggingが循環した依存関係を持ってしまう。
また、LoggingはAppに対して上位概念であるため、[依存関係逆転の原則(DIP)](#SS_2_5)にも反する。
よって、このアイデアを採用することはできない。

#### Ints_tを構造体としてApp内に宣言する <a id="SS_4_1_6_5"></a>

App::Ints_t用のoperator<<がLogging::Logger::set_inner内でname lookup出来ない理由は、
これまで述べてきたようにApp::Inst_tの[関連名前空間](#SS_6_12_6)がAppではなく、stdになってしまうからである。

これを回避するためにはその原因を取り払えばよく、
つまり、App::Inst_tの[関連名前空間](#SS_6_12_6)がAppになるようにすればよい。
これを実現するために、次のコードを試してみる。

```cpp
    //  example/template/logger_0_struct_ut.cpp 10

    namespace App {                     // Ints_tの宣言はApp
    struct Ints_t : std::vector<int> {  // エイリアスではなく、継承を使う
        using vector::vector;           // 継承コンストラクタ
    };

    // App内
    std::ostream& operator<<(std::ostream& os, Ints_t const& ints)
    {
        auto sep = "";

        for (auto const& i : ints) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
    }  // namespace App
```

上記のコードでは、

* App::Ints_tをstd::vectorからpublic継承
* using宣言によりstd::vectorのすべてのコンストラクタをApp::Ints_tに導入
  (「[継承コンストラクタ](#SS_6_6_1_2)」参照)

としているため、エイリアスで宣言されたInts_tと等価である。
C++03では、[継承コンストラクタ](#SS_6_6_1_2)が使えなかったため、
上記のような構造体を定義するためには、
std::vectorのすべてのコンストラクタと等価なコンストラクタをApp::Ints_t内に定義することが必要で、
実践的にはこのようなアイデアは使い物にならなかったが、
C++11での改善により、実践的なアイデアとして使用できるようになった。

実際、名前空間の問題もなく、すでに示した単体テストもパスするので有力な候補となるが、
若干の「やりすぎ感」は否めない。


#### operator\<\<を使わない <a id="SS_4_1_6_6"></a>
色々なアイデアを試してみたが、これまでの議論ではこれといった解決方法を発見できなかった。
「[バーニーの祈り](https://ja.wikipedia.org/wiki/%E3%83%8B%E3%83%BC%E3%83%90%E3%83%BC%E3%81%AE%E7%A5%88%E3%82%8A)」
が言っている通り、時にはどうにもならないことを受け入れることも重要である。
LOGGERの中でname lookupできる、エイリアスApp::Ints_tのoperator<<の開発をあきらめ、
ここでは一旦、下記のような受け入れがたいコードを受け入れることにする。


```cpp
    //  example/template/app_ints.h 6

    namespace App {
    using Ints_t = std::vector<int>;
    }
```
```cpp
    //  example/template/logger_0_no_put_to_ut.cpp 10

    namespace App {  // App::Ints_tのoperator<<とToStringをApp内で定義
    namespace {      // operator<<は外部から使わない
    std::ostream& operator<<(std::ostream& os, Ints_t const& ints)
    {
        auto sep = "";

        for (auto const& i : ints) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
    }  // namespace

    // Ints_tオブジェクトをstd::stringに変換する
    // この変換によりロガーに渡すことができる
    std::string ToString(Ints_t const& inst)
    {
        auto oss = std::ostringstream{};

        oss << inst;

        return oss.str();
    }
    }  // namespace App
```

当然だが、恥を忍んで受け入れたコードにも単体テストは必要である。

```cpp
    //  example/template/logger_0_no_put_to_ut.cpp 44

    auto ints = App::Ints_t{1, 2, 3};

    // ToStringのテスト
    ASSERT_EQ("1, 2, 3", App::ToString(ints));

    // LOGGERのテスト
    LOGGER("Ints", App::ToString(ints));
    auto line_num = __LINE__;

    auto s = Logging::Logger::InstConst().Get();

    auto exp = std::string{log_str_exp(__FILE__, line_num - 1, ":Ints:1, 2, 3\n")};
    ASSERT_EQ(exp, s);
```

上記コードから明らかな通り、App::Ints_tのインスタンスをログ登録する場合、
App::ToString()によりstd::stringへ変換する必要があり、残念なインターフェースとなっている。


#### Ints_tのログ登録のまとめ <a id="SS_4_1_6_7"></a>
製品開発では、満足できる仕様の関数やクラスが作れず、妥協せざるを得ないことはよくあることである。
このような場合、将来、良いアイデアが見つかった時に備えて、
妥協コードを簡単に修正できるようなレベルにした後、捲土重来を期してさっさと退却するのがベストである。
ただし、漫然と過ごしても良いアイデアは浮かばない。
時間を作り、関連書籍やウェブドキュメント等を読み、学習を継続する必要があることは言うまでもない。


## Nstdライブラリの開発 <a id="SS_4_2"></a>

「[operator\<\<を使わない](#SS_4_1_6_6)」で導入したコードは、短いながらも汎用性が高い。
このようなコードをローカルなファイルに閉じ込めてしまうと、
コードクローンや、[車輪の再発明](#SS_8_14_3)による開発効率の低下につながることがある。

通常、プロジェクトの全ファイルから参照可能で且つ、
プロジェクトの他のパッケージに非依存なパッケージを用意することで、このような問題を回避できる。

ここでは、そのようなパッケージをNstd(not standard library)とし、名前空間も同様に宣言する。
そうした場合、この章の例題で使用している名前空間の依存関係は下記のようになる。

```plant_uml/template_dependency.pu
@startuml

rectangle std #lightyellow
rectangle Nstd #lightblue
rectangle Logging #lightgreen
rectangle App #pink
rectangle Global #white

std <-right- Nstd #blue
std <-right- Logging #yellowgreen
std <-right- App #pink
std <-right- Global #black

Nstd <-right- Logging #yellowgreen
Nstd <-right- App #pink
Nstd <-right- Global #black

Logging <-right- App #pink
Logging <-right- Global #black

App <-right- Global #black

@enduml

```

このように整理された依存関係は、
大規模ソフトウェア開発においては特に重要であり、決して循環しないように維持しなければならない。


### Nstdライブラリを使用したリファクタリング <a id="SS_4_2_1"></a>
すでに述べた通り、「[operator\<\<を使わない](#SS_4_1_6_6)」で導入したコードは、Nstdで定義するべきである。
その場合、下記のようにさらに一般化するのが良いだろう。

```cpp
    //  example/template/nstd_0.h 4

    namespace Nstd {

    template <typename T>
    std::ostream& operator<<(std::ostream& os, std::vector<T> const& vec)
    {
        auto sep = "";

        for (auto const& i : vec) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }

    template <typename T>
    std::string ToString(std::vector<T> const& vec)
    {
        auto oss = std::ostringstream{};

        oss << vec;

        return oss.str();
    }
    }  // namespace Nstd
```

その単体テストは下記のようになる。

```cpp
    //  example/template/nstd_0_ut.cpp 13

    auto const ints = App::Ints_t{1, 2, 3};

    {
        auto oss = std::ostringstream{};

        using namespace Nstd;
        oss << ints << 4;
        ASSERT_EQ("1, 2, 34", oss.str());
    }
    {
        auto oss = std::ostringstream{};

        Nstd::operator<<(oss, ints) << 4;  // 念のためこの形式でもテスト
        ASSERT_EQ("1, 2, 34", oss.str());
    }

    ASSERT_EQ("1, 2, 3", Nstd::ToString(ints));
```

勘のいい読者なら、このコードをLOGGERから利用することで、
App:Ints_tのログ登録問題を解消できると思うかもしれない。
実際その通りなのであるが、そうした場合、
std::list等の他のコンテナや配列には対応できないという問題が残るため、
以降もしばらくNstdの開発を続ける。


### 安全なvector <a id="SS_4_2_2"></a>
std::vector、std::basic_string、std::array等の配列型コンテナは、

* operator[]経由でのメンバアクセスについて範囲の妥当性をチェックしない
* 範囲のチェックが必要ならばat()を使用する

という仕様になっているが、
ここではoperator[]にも範囲のチェックを行う配列型コンテナが必要になった場合について考える。

手始めにoperator[]にも範囲のチェックを行うstd::vector相当のコンテナSafeVectorを作ると、
下記のコードのようになる。

```cpp
    //  example/template/safe_vector_ut.cpp 10

namespace Nstd {

template <typename T>
struct SafeVector : std::vector<T> {
    using std::vector<T>::vector;  // 継承コンストラクタ

    using base_type = std::vector<T>;
    using size_type = typename base_type::size_type;

    typename base_type::reference       operator[](size_type i) { return this->at(i); }
    typename base_type::const_reference operator[](size_type i) const { return this->at(i); }
};
}  // namespace Nstd
```

このコードで行ったことは、

* std::vectorからSafeVectorをpublic継承する
* 継承コンストラクタの機能を使い、std::vectorのコンストラクタをSafeVectorで宣言する
* std::vector::atを使い、SafeVector::operator[]を定義する

である。単体テストは下記のようになる。

```cpp
    //  example/template/safe_vector_ut.cpp 30

    {
        auto v = Nstd::SafeVector<int>(10);  // ()での初期化

        ASSERT_EQ(10, v.size());
    }
    {
        auto const v = Nstd::SafeVector<int>{10};

        ASSERT_EQ(1, v.size());
        ASSERT_EQ(10, v[0]);
        ASSERT_THROW(v[1], std::out_of_range);  // エクセプションの発生
    }
    {
        auto v = Nstd::SafeVector<std::string>{"1", "2", "3"};

        ASSERT_EQ(3, v.size());
        ASSERT_EQ((std::vector<std::string>{"1", "2", "3"}), v);
        ASSERT_THROW(v[3], std::out_of_range);  // エクセプションの発生
    }
    {
        auto const v = Nstd::SafeVector<std::string>{"1", "2", "3"};

        ASSERT_EQ(3, v.size());
        ASSERT_EQ((std::vector<std::string>{"1", "2", "3"}), v);
        ASSERT_THROW(v[3], std::out_of_range);  // エクセプションの発生
    }
```


### 安全な配列型コンテナ <a id="SS_4_2_3"></a>
配列型コンテナはすでに述べたようにstd::vectorの他にすくなともstd::basic_string、
std::arrayがあるため、それらにも範囲チェックを導入する。

std::basic_stringはstd::vectorとほぼ同様に下記のようになる。

```cpp
    //  example/template/safe_vector_ut.cpp 62
    namespace Nstd {

    struct SafeString : std::string {
        using std::string::string;  // 継承コンストラクタ

        using base_type = std::string;
        using size_type = typename base_type::size_type;

        typename base_type::reference       operator[](size_type i) { return this->at(i); }
        typename base_type::const_reference operator[](size_type i) const { return this->at(i); }
    };
    }  // namespace Nstd
```

std::stringはstd::basic_string\<char>のエイリアスであるため、
上記では、通常使われる形式であるstd::stringを継承したSafeStringを定義した。

この単体テストはSafeVectorの場合と同様に下記のようになる。

```cpp
    //  example/template/safe_vector_ut.cpp 80

    {
        auto s = Nstd::SafeString{"0123456789"};

        ASSERT_EQ(10, s.size());
        ASSERT_EQ("0123456789", s);
        ASSERT_THROW(s[10], std::out_of_range);
    }
    {
        auto const s = Nstd::SafeString(3, 'c');  // ()での初期化が必要

        ASSERT_EQ(3, s.size());
        ASSERT_EQ("ccc", s);
    }
```

std::arrayでは少々事情が異なるが、
std::vectorのコードパターンをそのまま適用すると下記のようになる。

```cpp
    //  example/template/safe_vector_ut.cpp 101

    namespace Nstd {

    template <typename T, size_t N>
    struct SafeArray : std::array<T, N> {
        using std::array<T, N>::array;  // 継承コンストラクタ

        using base_type = std::array<T, N>;
        using size_type = typename base_type::size_type;

        typename base_type::reference       operator[](size_type i) { return this->at(i); }
        typename base_type::const_reference operator[](size_type i) const { return this->at(i); }
    };
    }  // namespace Nstd
```

ただし、この実装には問題がある。

```cpp
    //  example/template/safe_vector_ut.cpp 122

    auto sa_not_init = Nstd::SafeArray<int, 3>{};

    ASSERT_EQ(3, sa_not_init.size());
    ASSERT_THROW(sa_not_init[3], std::out_of_range);
```

上記コードでは、その問題が露見することはないが、以下のコードはコンパイルできない。

```cpp
    //  example/template/safe_vector_ut.cpp 132

    // std::initializer_listを引数とするコンストラクタが未定義
    auto sa_init = Nstd::SafeArray<int, 3>{1, 2, 3};

    // デフォルトコンストラクタがないため、未初期化
    Nstd::SafeArray<int, 3> const sa_const;
```

std::arrayにはコンストラクタが明示的に定義されていないため、
std::arrayにはデフォルトで自動生成される

* デフォルトコンストラクタ
* copyコンストラクタ
* moveコンストラクタ

以外のコンストラクタがないことが原因である。
従って、SafeArray(std::initializer_list)が定義されず前述したようにコンパイルエラーとなる。

この問題に対処したのが以下のコードである。

```cpp
    //  example/template/safe_vector_ut.cpp 146

    namespace Nstd {

    template <typename T, size_t N>
    struct SafeArray : std::array<T, N> {
        using std::array<T, N>::array;  // 継承コンストラクタ
        using base_type = std::array<T, N>;

        template <typename... ARGS>  // コンストラクタを定義
        SafeArray(ARGS... args) : base_type{args...}
        {
        }

        using size_type = typename base_type::size_type;

        typename base_type::reference       operator[](size_type i) { return this->at(i); }
        typename base_type::const_reference operator[](size_type i) const { return this->at(i); }
    };
    }  // namespace Nstd
```

上記コードで注目すべきは、パラメータパックをテンプレートパラメータとしたコンストラクタである。
これにより、前例ではコンパイルすらできなかった下記のような初期化子リストを用いた単体テストが、
このコンストラクタによりパスするようになった。

```cpp
    //  example/template/safe_vector_ut.cpp 181
    {
        auto sa_init = Nstd::SafeArray<int, 3>{1, 2, 3};

        ASSERT_EQ(3, sa_init.size());
        ASSERT_EQ(1, sa_init[0]);
        ASSERT_EQ(2, sa_init[1]);
        ASSERT_EQ(3, sa_init[2]);
        ASSERT_THROW(sa_init[3], std::out_of_range);
    }
    {
        auto const sa_string_const = Nstd::SafeArray<std::string, 5>{"1", "2", "3"};

        ASSERT_EQ(5, sa_string_const.size());
        ASSERT_EQ("1", sa_string_const[0]);
        ASSERT_EQ("2", sa_string_const[1]);
        ASSERT_EQ("3", sa_string_const[2]);
        ASSERT_EQ("", sa_string_const[3]);
        ASSERT_EQ("", sa_string_const[4]);
        ASSERT_THROW(sa_string_const[5], std::out_of_range);
    }
```

この効果を生み出した上記を抜粋した下記のコードには解説が必要だろう。

```cpp
    //  example/template/safe_vector_ut.cpp 155

    template <typename... ARGS>  // コンストラクタを定義
    SafeArray(ARGS... args) : base_type{args...}
    {
    }
```

一般にコンストラクタには「メンバ変数の初期化」と「基底クラスの初期化」が求められるが、
SafeArrayにはメンバ変数が存在しないため、
このコンストラクタの役割は「基底クラスの初期化」のみとなる。
基底クラスstd::array(上記例ではbase_typeにエイリアスしている)
には名前が非規定の配列メンバのみを持つため、
これを初期化するためには初期化子リスト
(「[初期化子リストコンストラクタ](#SS_6_6_1_1)」、
「[一様初期化](#SS_6_6_6)」参照)を用いるのが良い。

ということは、SafeArrayの初期化子リストコンストラクタには、
「基底クラスstd::arrayに初期子リストを与えて初期化する」形式が必要になる。
値を持つパラメータパックは初期化子リストに展開できるため、
ここで必要な形式はパラメータパックとなる。
これを実現したのが上記に抜粋したわずか数行のコードである。


### 初期化子リストの副作用 <a id="SS_4_2_4"></a>
上記SafeArrayの初期化子リストコンストラクタは以下のようなコードを許可しない。

```cpp
    //  example/template/safe_vector_ut.cpp 213
    {
        auto sa_init = Nstd::SafeArray<int, 3>{1.0, 2, 3};

        ASSERT_EQ(3, sa_init.size());
        ASSERT_EQ(1, sa_init[0]);
        ASSERT_EQ(2, sa_init[1]);
        ASSERT_EQ(3, sa_init[2]);
        ASSERT_THROW(sa_init[3], std::out_of_range);
    }
```

このコードをコンパイルすると、

```
    safe_vector_ut.cpp:147:41: error: narrowing conversion of ‘
                                        args#0’ from ‘double’ to ‘int’ -Werror=narrowing]
      147 |     SafeArray(ARGS... args) : base_type{args...}
          |                                         ^~~~
```

のようなエラーが出力されるが、

* double(上記例では1.0)をintに変換する際に縮小変換(narrowing conversio)nが起こる
* 初期化子リストでの縮小変換は許可されない

が原因である。これは意図しない縮小変換によるバグを防ぐ良い機能だと思うが、
ここではテンプレートメタプログラミングのテクニックを解説するため、
あえてこのコンパイルエラーを起こさないSafeArray2を開発する
(言うまでもないが、通常のソフトウェア開発では、
縮小変換によるコンパイルエラーを回避するようなコードを書いてはならない)。

SafeArray2のコードは、

* STLのtype_traitsの使用
* テンプレートの特殊化
* メンバ関数テンプレートとオーバーロードによる静的ディスパッチ(コンパイル時ディスパッチ)
* [SFINAE](#SS_6_11_1)

等のメタ関数系のテクニックが必要になるため、
まずはこれらを含めたテンプレートのテクニックについて解説し、
その後SafeArray2を見ていくことにする。

## メタ関数のテクニック <a id="SS_4_3"></a>
本節では、[type_traits](#SS_7_2)の[メタ関数](#SS_6_11_2)の実装等で広く使われいる下記のようなテクニックを

- [std::is_void](#SS_7_2_7)と同等のメタ関数を[is_void_xxxの実装](#SS_4_3_1)
- [std::is_same](#SS_7_2_4)と同等のメタ関数を[is_same_xxxの実装](#SS_4_3_2)
- std::is_convertibleと同等のメタ関数を[AreConvertibleXxxの実装](#SS_4_3_3)

で紹介する。




### is_void_xxxの実装 <a id="SS_4_3_1"></a>
ここではstd::is_voidに似た以下のような仕様を持ついくつかのテンプレートis_void_xxxの実装を考える。

|テンプレートパラメータ|戻り値            |
|----------------------|------------------|
|void                  |true              |
|非void                |false             |

それぞれのis_void_xxxは下記テーブルで示した言語機能を使用して実装する。

|is_void_xxx                  |実装方法                                               |
|-----------------------------|-------------------------------------------------------|
|[is_void_f](#SS_4_3_1_1)             |関数テンプレートの特殊化                               |
|[is_void_s](#SS_4_3_1_2)             |クラステンプレートの特殊化                             |
|[is_void_sfinae_f](#SS_4_3_1_3)      |FINAEと関数テンプレートのオーバーロード                |
|[is_void_sfinae_s](#SS_4_3_1_4)      |FINAEとクラステンプレートの特殊化                      |
|[is_void_concept_s](#SS_4_3_1_5)     |コンセプトとクラステンプレートの特殊化                 |
|[is_void_ena_s](#SS_4_3_1_6)         |std::enable_ifによるSFINAEとクラステンプレートの特殊化 |
|[is_void_cond_s](#SS_4_3_1_7)        |std::conditionalと関数テンプレートの特殊化             |

なお、実装例をシンプルに保つため、
理解の妨げとなり得る下記のような正確性(例外条件の対応)等のためのコードを最低限に留めた。

* テンプレートパラメータの型のチェック
* テンプレートパラメータの型からのポインタ/リファレンス/const/volatileの削除
* 戻り型からのconst/volatileの削除

これは、「テンプレートプログラミングでの有用なテクニックの解説」
というここでの目的を見失わないための措置である。


#### is_void_f <a id="SS_4_3_1_1"></a>
関数テンプレートの特殊化を使用したis_void_fの実装は以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 8

    template <typename T>
    constexpr bool is_void_f() noexcept
    {
        return false;
    }

    template <>
    constexpr bool is_void_f<void>() noexcept
    {
        return true;
    }

    template <typename T>
    constexpr bool is_void_f_v{is_void_f<T>()};
```

単純なので解説は不要だろう。これらの単体テストは下記のようになる。

```cpp
    //  example/template/is_void_ut.cpp 28

    static_assert(!is_void_f_v<int>);
    static_assert(!is_void_f_v<std::string>);
    static_assert(is_void_f_v<void>);
```

関数テンプレートの特殊化には、

* 特殊化された関数テンプレートとそのプライマリテンプレートのシグネチャ、
  戻り値は一致しなければならない
* クラステンプレートのような部分特殊化は許可されない

のような制限があるため用途は限られるが、関数テンプレートはオーバーロードすることが可能である。


#### is_void_s <a id="SS_4_3_1_2"></a>
クラステンプレートの特殊化を使用したis_void_sの実装は以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 36

    template <typename T>
    struct is_void_s {
        static constexpr bool value{false};
    };

    template <>
    struct is_void_s<void> {
        static constexpr bool value{true};
    };

    template <typename T>
    constexpr bool is_void_s_v{is_void_s<T>::value};
```

is_void_fと同様に単純なので解説は不要だろう。これらの単体テストは下記のようになる。

```cpp
    //  example/template/is_void_ut.cpp 54

    static_assert(!is_void_s_v<int>);
    static_assert(!is_void_s_v<std::string>);
    static_assert(is_void_s_v<void>);
```


#### is_void_sfinae_f <a id="SS_4_3_1_3"></a>
[SFINAE](#SS_6_11_1)を使用した関数テンプレートis_void_sfinae_fの実装は以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 62

    namespace Inner_ {

    // T == void
    template <typename T>
    constexpr auto is_void_sfinae_f_detector(void const* v, T const* t) noexcept
        -> decltype(t = v, bool{})  // T != voidの場合、t = vはill-formed
                                    // T == voidの場合、well-formedでbool型生成
    {
        return true;
    }

    // T != void
    template <typename T>
    constexpr auto is_void_sfinae_f_detector(void const*, T const*) noexcept
        -> decltype(sizeof(T), bool{})  // T != voidの場合、well-formedでbool型生成
                                        // T == voidの場合、sizeof(T)はill-formed
    {
        return false;
    }
    }  // namespace Inner_

    template <typename T>
    constexpr bool is_void_sfinae_f() noexcept
    {
        return Inner_::is_void_sfinae_f_detector(nullptr, static_cast<T*>(nullptr));
    }

    template <typename T>
    constexpr bool is_void_sfinae_f_v{is_void_sfinae_f<T>()};
```

関数テンプレートである2つのis_void_sfinae_f_detectorのオーバーロードにSFINAEを使用している。

1つ目のis_void_sfinae_f_detectorでは、

| T       | t = v の診断(コンパイル) |
|---------|--------------------------|
| == void | well-formed              |
| != void | ill-formed               |

であるため、Tがvoidの時のみ[name lookup](#SS_6_12_2)の対象になる。

2つ目のis_void_sfinae_f_detectorでは、

| T       | sizeof(T)の診断(コンパイル) |
|---------|-----------------------------|
| == void | ill-formed                  |
| != void | well-formed                 |

であるため、Tが非voidの時のみ[name lookup](#SS_6_12_2)の対象になる。

is_void_sfinae_fはこの性質を利用し、

* T == voidの場合、1つ目のis_void_sfinae_f_detectorが選択され、戻り値はtrue
* T != voidの場合、2つ目のis_void_sfinae_f_detectorが選択され、戻り値はfalse

となる。念のため単体テストを示すと下記のようになる。

```cpp
    //  example/template/is_void_ut.cpp 97

    static_assert(!is_void_sfinae_f_v<int>);
    static_assert(!is_void_sfinae_f_v<std::string>);
    static_assert(is_void_sfinae_f_v<void>);
```

一般にファイル外部に公開するテンプレートは、
コンパイルの都合上ヘッダファイルにその全実装を記述することになる。
これは、本来外部公開すべきでない実装の詳細である
is_void_sfinae_f_detectorのようなテンプレートに関しては大変都合が悪い。
というのは、外部から使用されたくない実装の詳細が使われてしまうことがあり得るからである。
上記の例では、こういうことに備え
「これは外部非公開である」ということを示す名前空間Inner\_
を導入した。

関数テンプレートはクラステンプレート内にも定義することができるため、
is_void_sfinae_fは下記のように実装することも可能である。この場合、名前空間Inner\_は不要になる。

```cpp
    //  example/template/is_void_ut.cpp 106

    template <typename T>
    class is_void_sfinae_f {
        // U == void
        template <typename U>
        static constexpr auto detector(void const* v, U const* u) noexcept
            -> decltype(u = v, bool{})  // U != voidの場合、t = vはill-formed
                                        // U == voidの場合、well-formedでbool型生成
        {
            return true;
        }

        // U != void
        template <typename U>
        static constexpr auto detector(void const*, U const*) noexcept
            -> decltype(sizeof(U), bool{})  // U != voidの場合、well-formedでbool型生成
                                            // U == voidの場合、ill-formed
        {
            return false;
        }

    public:
        static constexpr bool value{is_void_sfinae_f::detector(nullptr, static_cast<T*>(nullptr))};
    };

    template <typename T>
    constexpr bool is_void_sfinae_f_v{is_void_sfinae_f<T>::value};
```

```cpp
    //  example/template/is_void_ut.cpp 138

    static_assert(!is_void_sfinae_f_v<int>);
    static_assert(!is_void_sfinae_f_v<std::string>);
    static_assert(is_void_sfinae_f_v<void>);
```


#### is_void_sfinae_s <a id="SS_4_3_1_4"></a>
[SFINAE](#SS_6_11_1)を使用したクラステンプレートis_void_sfinae_sの実装は以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 147

    namespace Inner_ {
    template <typename T>
    T*& t2ptr();  // 定義は不要
    }  // namespace Inner_

    template <typename T, typename = void*&>
    struct is_void_sfinae_s : std::false_type {
    };

    template <typename T>
    struct is_void_sfinae_s<
        T,
        // T != voidの場合、ill-formed
        // T == voidの場合、well-formedでvoid*&生成
        decltype(Inner_::t2ptr<T>() = Inner_::t2ptr<void>())

        > : std::true_type {
    };

    template <typename T>
    constexpr bool is_void_sfinae_s_v{is_void_sfinae_s<T>::value};
```

1つ目のis_void_sfinae_sはプライマリテンプレートである。
is_void_sfinae_sの特殊化が[name lookup](#SS_6_12_2)の対象の中に見つからなかった場合、
これが使われる。

2つ目のis_void_sfinae_sは、上記を抜粋した下記のコード

```cpp
    //  example/template/is_void_ut.cpp 163

    // T != voidの場合、ill-formed
    // T == voidの場合、well-formedでvoid*&生成
    decltype(Inner_::t2ptr<T>() = Inner_::t2ptr<void>())
```

がT == voidの時のみ、well-formedになり、このテンプレートは下記のようにインスタンス化される。

```cpp
    struct is_void_sfinae_s<void, void*&>
```

この形状はプライマリテンプレートの

* 第1パラメータにvoidを与える
* 第2パラメータには何も与えない(デフォルトのまま)

とした場合の、つまりプライマリテンプレートを

```cpp
    struct is_void_sfinae_s<void>   // プライマリテンプレート
```

としてインスタンス化した場合と一致する。
プライマリと特殊化が一致した場合、特殊化されたものがname lookupで選択される。

T != voidの場合、 2つ目のis_void_sfinae_sはill-formedになり、name lookupの対象から外れるため、
プライマリが選択される。

以上をまとめると、

| T       | is_void_sfinae_sの基底クラス |
|---------|------------------------------|
| == void | std::true_type               |
| != void | std::false_type              |

となる。以下の単体テストによって、このことを確かめることができる。

```cpp
    //  example/template/is_void_ut.cpp 180

    static_assert(!is_void_sfinae_s_v<int>);
    static_assert(std::is_base_of_v<std::false_type, is_void_sfinae_s<int>>);

    static_assert(!is_void_sfinae_s_v<std::string>);
    static_assert(std::is_base_of_v<std::false_type, is_void_sfinae_s<std::string>>);

    static_assert(is_void_sfinae_s_v<void>);
    static_assert(std::is_base_of_v<std::true_type, is_void_sfinae_s<void>>);
```

上記コードのように「プライマリテンプレートのデフォルトパラメータ」と、

```cpp
    //  example/template/is_void_ut.cpp 163

    // T != voidの場合、ill-formed
    // T == voidの場合、well-formedでvoid*&生成
    decltype(Inner_::t2ptr<T>() = Inner_::t2ptr<void>())
```

が「well-formedであった場合に生成される型」が一致することを利用した静的ディスパッチは、
SFINAEとクラステンプレートの特殊化を組み合わせたメタ関数の典型的な実装パターンである。
ただし、一般にはill-formedを起こすためにst::enable_ifを使うことが多いため、
「[is_void_ena_s](#SS_4_3_1_6)の実装」でその例を示す。


#### is_void_concept_s <a id="SS_4_3_1_5"></a>
[is_void_sfinae_s](#SS_4_3_1_4)の実装で使用したSFINAEを回避し、
コンセプトを使用することで可読性の向上が見込める。
以下の実装で使用した[same_as](#SS_4_3_2_6)は\<concepts>で定義されているコンセプトと同様のものである。

```cpp
    //  example/template/is_void_ut.cpp 193

    template <typename T>
    struct is_void_concept_s : std::false_type {
    };

    template <typename T>
    requires std::same_as<T, void>  // コンセプトによるTの制約
    struct is_void_concept_s<T> : std::true_type {
    };
```
```cpp
    //  example/template/is_void_ut.cpp 207

    static_assert(!is_void_concept_s<int>::value);
    static_assert(std::is_base_of_v<std::false_type, is_void_concept_s<int>>);

    static_assert(!is_void_concept_s<std::string>::value);
    static_assert(std::is_base_of_v<std::false_type, is_void_concept_s<std::string>>);

    static_assert(is_void_concept_s<void>::value);
    static_assert(std::is_base_of_v<std::true_type, is_void_concept_s<void>>);
```

下記に示した通り、テンプレート特殊化はクラスのみなく定数に対しても使用することができる。

```cpp
    //  example/template/is_void_ut.cpp 220

    template <typename T>
    constexpr bool is_void_concept_s_v = false;

    template <typename T>
    requires std::same_as<T, void>
    constexpr bool is_void_concept_s_v<T> = true;
```

以下に示した通り、[is_void_sfinae_s](#SS_4_3_1_4)の実装で示した定数テンプレートのテストと同様になっている。

```cpp
    //  example/template/is_void_ut.cpp 232

    static_assert(!is_void_concept_s_v<int>);
    static_assert(!is_void_concept_s_v<std::string>);
    static_assert(is_void_concept_s_v<void>);
```

#### is_void_ena_s <a id="SS_4_3_1_6"></a>
[std::enable_if](#SS_7_2_5)による[SFINAE](#SS_6_11_1)とクラステンプレートの特殊化を使用した
is_void_ena_sの実装は以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 240
    template <typename T, typename = void>
    struct is_void_ena_s : std::false_type {
    };

    template <typename T>
    struct is_void_ena_s<
        T,
        typename std::enable_if_t<is_void_f<T>()>
        > : std::true_type {
    };

    template <typename T>
    constexpr bool is_void_ena_s_v{is_void_ena_s<T>::value};
```

この例では、「[is_void_sfinae_s](#SS_4_3_1_4)の実装」の

```cpp
    //  example/template/is_void_ut.cpp 163

    // T != voidの場合、ill-formed
    // T == voidの場合、well-formedでvoid*&生成
    decltype(Inner_::t2ptr<T>() = Inner_::t2ptr<void>())
```

で示したSFINAEの処理を上記を抜粋した下記のコード

```cpp
    //  example/template/is_void_ut.cpp 250

    typename std::enable_if_t<is_void_f<T>()>
```

で行っている。
std::enable_ifの値パラメータis_void_f\<T>()は、「[is_void_f](#SS_4_3_1_1)の実装」で示したものである。

単体テストは、「[is_void_sfinae_s](#SS_4_3_1_4)の実装」で示したものとほぼ同様で、以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 264

    static_assert(!is_void_ena_s_v<int>);
    static_assert(std::is_base_of_v<std::false_type, is_void_ena_s<int>>);

    static_assert(!is_void_ena_s_v<std::string>);
    static_assert(std::is_base_of_v<std::false_type, is_void_ena_s<std::string>>);

    static_assert(is_void_ena_s_v<void>);
    static_assert(std::is_base_of_v<std::true_type, is_void_ena_s<void>>);
```


#### is_void_cond_s <a id="SS_4_3_1_7"></a>
[std::conditional](#SS_7_2_6)と関数テンプレートの特殊化を使用したis_void_cond_sの実装は以下のようになる。

```cpp
    //  example/template/is_void_ut.cpp 277
    template <typename T>
    struct is_void_cond_s : std::conditional_t<is_void_f<T>(), std::true_type, std::false_type> {
    };

    template <typename T>
    constexpr bool is_void_cond_s_v{is_void_cond_s<T>::value};
```

std::conditionalの値パラメータis_void_f\<T>()は、「[is_void_f](#SS_4_3_1_1)の実装」で示したものである。
この例では、[SFINAE](#SS_6_11_1)もクラステンプレートの特殊化も使用していないが、
下記単体テストからわかる通り、「[is_void_sfinae_s](#SS_4_3_1_4)の実装」と同じ機能を備えている。

```cpp
    //  example/template/is_void_ut.cpp 288

    static_assert(!is_void_cond_s_v<int>);
    static_assert(std::is_base_of_v<std::false_type, is_void_cond_s<int>>);

    static_assert(!is_void_cond_s_v<std::string>);
    static_assert(std::is_base_of_v<std::false_type, is_void_cond_s<std::string>>);

    static_assert(is_void_cond_s_v<void>);
    static_assert(std::is_base_of_v<std::true_type, is_void_cond_s<void>>);
```


### is_same_xxxの実装 <a id="SS_4_3_2"></a>
ここではstd::is_same\<T, U>に似た、
以下のような仕様を持ついくつかのテンプレートis_same_xxxの実装を考える。

|テンプレートパラメータ|戻り値            |
|----------------------|------------------|
|T == U                |true              |
|T != U                |false             |

それぞれのis_same_xxxは下記テーブルで示された言語機能を使用して実装する。

|is_same_xxx                   |実装方法                                               |
|------------------------------|-------------------------------------------------------|
|[is_same_f](#SS_4_3_2_1)              |関数テンプレートのオーバーロード                       |
|[is_same_v](#SS_4_3_2_2)              |定数テンプレートの特殊化                               |
|[is_same_s](#SS_4_3_2_3)              |クラステンプレートの特殊化                             |
|[is_same_sfinae_f](#SS_4_3_2_4)       |SFINAEと関数テンプレート/関数のオーバーロード          |
|[is_same_sfinae_s](#SS_4_3_2_5)       |SFINAEとクラステンプレートの特殊化                     |
|[same_as](#SS_4_3_2_6)                |[コンセプト](#SS_6_11_3)よるis_same_sfinae_sと同一の機能      |
|[is_same_templ](#SS_4_3_2_7)          |テンプレートテンプレートパラメータ                     |
|[IsSameSomeOf](#SS_4_3_2_8)           |パラメータパックと再帰                                 |
|[OneOf](#SS_4_3_2_9)                  |IsSameSomeOfをコンセプトに                             |

#### is_same_f <a id="SS_4_3_2_1"></a>
関数テンプレートのオーバーロードを用いたis_same_fの実装は以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 9

    template <typename T, typename U>
    constexpr bool is_same_f_helper(T const*, U const*) noexcept
    {
        return false;
    }

    template <typename T>
    constexpr bool is_same_f_helper(T const*, T const*) noexcept
    {
        return true;
    }

    template <typename T, typename U>
    constexpr bool is_same_f() noexcept
    {
        return is_same_f_helper(static_cast<T*>(nullptr), static_cast<U*>(nullptr));
    }

    template <typename T, typename U>
    constexpr bool is_same_f_v{is_same_f<T, U>()};
```

すでに述べたように関数テンプレートの部分特殊化は言語仕様として認められておらず、

```cpp
    //  example/template_cpp17/is_same_ut.cpp 34

    template <typename T, typename U>
    constexpr bool is_same_f()
    {
        return true;
    }

    template <typename T>
    constexpr bool is_same_f<T, T>()
    {
        return true;
    }
```

上記のようなのようなコードは、以下のようなコンパイルエラーになる
(g++/clang++のような優れたコンパイラを使えば、
以下のメッセージのように簡単に問題点が理解できることもある)。

```
    is_same_ut.cpp:35:32: error: non-class, non-variable partial specialization ‘
                                          is_same_f<T, T>’ is not allowed
        35 | constexpr bool is_same_f<T, T>()
```

関数テンプレートは部分特殊化が出来ない代わりに、
同じ識別子を持つ関数や関数テンプレートとのオーバーロードができる。関数とのオーバーロードの場合、
is_same_f_helper\<T>()のようなテンプレートパラメータを直接使用した静的ディスパッチが出来ないため、
常に型推測によるディスパッチが必要になる。

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 52

    static_assert(!is_same_f_v<int, void>);
    static_assert(is_same_f_v<int, int>);
    static_assert(!is_same_f_v<int, uint32_t>);
    static_assert(is_same_f_v<std::string, std::basic_string<char>>);
```

#### is_same_v <a id="SS_4_3_2_2"></a>
定数テンプレートの特殊化を用いたis_same_vの実装は以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 61

    template <typename T, typename U>
    constexpr bool is_same_v{false};

    template <typename T>
    constexpr bool is_same_v<T, T>{true};
```

単純であるため、解説は不要だろう。 単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 72

    static_assert(!is_same_v<int, void>);
    static_assert(is_same_v<int, int>);
    static_assert(!is_same_v<int, uint32_t>);
    static_assert(is_same_v<std::string, std::basic_string<char>>);
```


#### is_same_s <a id="SS_4_3_2_3"></a>
クラステンプレートの特殊化を用いたis_same_sの実装は以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 81

    template <class T, class U>
    struct is_same_s : std::false_type {
    };

    template <class T>
    struct is_same_s<T, T> : std::true_type {
    };

    template <typename T, typename U>
    constexpr bool is_same_s_v{is_same_s<T, U>::value};
```

「[is_same_v](#SS_4_3_2_2)の実装」と同様に単純であるため、解説は不要だろう。 単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 97

    static_assert(!is_same_s_v<int, void>);
    static_assert(is_same_s_v<int, int>);
    static_assert(!is_same_s_v<int, uint32_t>);
    static_assert(is_same_s_v<std::string, std::basic_string<char>>);
```


#### is_same_sfinae_f <a id="SS_4_3_2_4"></a>
SFINAEと関数テンプレート/関数のオーバーロードを用いたis_same_sfinae_f実装は以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 106

    namespace Inner_ {
    template <typename T, typename U>
    constexpr auto is_same_sfinae_f_detector(T const* t, U const* u) noexcept
        -> decltype(t = u, u = t, bool{})  // T != Uの場合、t = u, u = tはill-formed
                                           // T == Uの場合、well-formedでbool型生成
    {
        return true;
    }

    constexpr bool is_same_sfinae_f_detector(...) noexcept { return false; }
    }  // namespace Inner_

    template <typename T, typename U>
    constexpr bool is_same_sfinae_f() noexcept
    {
        return Inner_::is_same_sfinae_f_detector(static_cast<T*>(nullptr), static_cast<U*>(nullptr));
    }

    template <typename T, typename U>
    constexpr bool is_same_sfinae_f_v{is_same_sfinae_f<T, U>()};
```

上記の抜粋である下記コードのコメントで示したように、

```cpp
    //  example/template_cpp17/is_same_ut.cpp 112

    -> decltype(t = u, u = t, bool{})  // T != Uの場合、t = u, u = tはill-formed
                                       // T == Uの場合、well-formedでbool型生成
```

T != Uの場合、この関数テンプレートはill-formedとなりname lookupの対象ではなくなる。
その結果、関数is_same_sfinae_f_detectorが選択される。
省略記号"..."(ellipsis)を引数とする関数は、そのオーバーロード群の中での最後の選択となるため、
T == Uの場合は、関数テンプレートis_same_sfinae_f_detectorが選択される。

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 136

    static_assert(!is_same_sfinae_f_v<int, void>);
    static_assert(is_same_sfinae_f_v<int, int>);
    static_assert(!is_same_sfinae_f_v<int, uint32_t>);
    static_assert(is_same_sfinae_f_v<std::string, std::basic_string<char>>);
```

#### is_same_sfinae_s <a id="SS_4_3_2_5"></a>
SFINAEとクラステンプレートの特殊化を用いたis_same_sfinae_sの実装は以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 144

    namespace Inner_ {
    template <typename T>
    T*& t2ptr();
    }

    template <typename T, typename U, typename = T*&>
    struct is_same_sfinae_s : std::false_type {
    };

    template <typename T, typename U>
    struct is_same_sfinae_s<
        T, U,

        // T != Uの場合、ill-formed
        // T == Uの場合、well-formedでT*&生成
        decltype(Inner_::t2ptr<T>() = Inner_::t2ptr<U>(), Inner_::t2ptr<U>() = Inner_::t2ptr<T>())
        > : std::true_type {
    };

    template <typename T, typename U>
    constexpr bool is_same_sfinae_s_v{is_same_sfinae_s<T, U>::value};
```

「[is_void_sfinae_s](#SS_4_3_1_4)の実装」とほぼ同様であるため、解説は不要だろう。 
単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 172

    static_assert(!is_same_sfinae_s_v<int, void>);
    static_assert(is_same_sfinae_s_v<int, int>);
    static_assert(!is_same_sfinae_s_v<int, uint32_t>);
    static_assert(is_same_sfinae_s_v<std::string, std::basic_string<char>>);
```

#### same_as <a id="SS_4_3_2_6"></a>
[SFINAE](#SS_6_11_1)による[is_same_sfinae_s](#SS_4_3_2_5)の難解なコードを[コンセプト](#SS_6_11_3)
よりリファクタリングしたコードを以下に示す。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 181

    #if __cplusplus >= 202002L  // c++20
    template <typename T, typename U>
    concept same_as = requires(T const* t, U const* u)
    {
        {t = u, u = t};
    };

    #else  // c++17
    template <typename T, typename U>
    inline constexpr bool same_as = is_same_sfinae_s_v<T, U>;

    #endif
```
is_same_sfinae_sは定数テンプレートであり、same_asはコンセプトであるが、
下記のテストから明らかな通り、ほぼ同様に同様に使用することができる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 196

    static_assert(!same_as<int, void>);
    static_assert(same_as<int, int>);
    static_assert(!same_as<int, uint32_t>);
    static_assert(same_as<std::string, std::basic_string<char>>);
```

「[is_same_s](#SS_4_3_2_3)」で紹介した特殊化のテクニックを下記のように使用することができる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 203

    #if __cplusplus >= 202002L  // c++20
    template <typename T, typename U>
    struct is_same_concept_s : std::false_type {
    };

    template <typename T, typename U>
    requires same_as<T, U>
    struct is_same_concept_s<T, U> : std::true_type {
    };

    #else  // c++17
    template <typename T, typename U, typename = void>
    struct is_same_concept_s : std::false_type {
    };

    template <typename T, typename U>
    struct is_same_concept_s<T, U, std::enable_if_t<same_as<T, U>, void>> : std::true_type {
    };

    #endif

    static_assert(!is_same_concept_s<int, void>::value);
    static_assert(is_same_concept_s<int, int>::value);
    static_assert(!is_same_concept_s<int, uint32_t>::value);
    static_assert(is_same_concept_s<std::string, std::basic_string<char>>::value);
```

#### is_same_templ <a id="SS_4_3_2_7"></a>
例えば、std::stringとstd::basic_string\<T>が同じもしくは違う型であることを確認するためには、
すでに示したis_same_sを使用し、

```cpp
    //  example/template_cpp17/is_same_ut.cpp 246

    static_assert(is_same_s_v<std::string, std::basic_string<char>>);
    static_assert(!is_same_s_v<std::string, std::basic_string<signed char>>);
```

のようにすればよいが、
以下に示したコードのようにテンプレートテンプレートパラメータを使うことでも実装できる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 234

    template <typename T, template <class...> class TEMPL, typename... ARGS>
    struct is_same_templ : is_same_sfinae_s<T, TEMPL<ARGS...>> {
    };

    template <typename T, template <class...> class TEMPL, typename... ARGS>
    constexpr bool is_same_templ_v{is_same_templ<T, TEMPL, ARGS...>::value};
```

上記のis_same_templは、第2引数にクラステンプレート、
第3引数以降にそのクラステンプレートの1個以上の引数を取ることができる。
使用例を兼ねた単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 251

    static_assert(is_same_templ_v<std::string, std::basic_string, char>);
    static_assert(!is_same_templ_v<std::string, std::basic_string, signed char>);
```

これを応用したエイリアステンプレート

```cpp
    //  example/template_cpp17/is_same_ut.cpp 258

    template <typename T>
    using gen_std_string = is_same_templ<std::string, std::basic_string, T>;

    template <typename T>
    constexpr bool gen_std_string_v{gen_std_string<T>::value};
```

は与えられたテンプレートパラメータがstd::stringを生成するかどうかを判定することができる。

```cpp
    //  example/template_cpp17/is_same_ut.cpp 269

    static_assert(gen_std_string_v<char>);
    static_assert(!gen_std_string_v<signed char>);
```


#### IsSameSomeOf <a id="SS_4_3_2_8"></a>
IsSameSomeOfはこれまでの例とは少々異なり、

* 第1パラメータが第2パラメータ以降で指定された型のどれかと一致する
  SameAsSomeOfという名前の[コンセプト](#SS_6_11_3)を[畳み込み式](#SS_6_11_5)を使用し定義する
* SameAsSomeOfで制約したテンプレートパラメータをstd::bool_constantからIsSameSomeOfを派生させる

のような特徴のを持つ。
このようなIsSameSomeOfの実装はは以下のようになる。

```cpp
    //  example/h/nstd_type_traits.h 13

    namespace Nstd {
    namespace Inner_ {
    template <typename T, typename U, typename... Us>
    struct is_same_as_some_of_impl {  // 型特性の補助クラス: 複数の型と比較する再帰的な実装
        static constexpr bool value = std::is_same<T, U>::value || is_same_as_some_of_impl<T, Us...>::value;
    };

    // 再帰の終端条件: 比較する型が1つの場合
    template <typename T, typename U>
    struct is_same_as_some_of_impl<T, U> {
        static constexpr bool value = std::is_same<T, U>::value;
    };
    }  // namespace Inner_

    #if __cplusplus >= 202002L  // c++20
    // コンセプト: 複数の型のいずれかがTと同じかどうかをチェック
    template <typename T, typename U, typename... Us>
    concept SameAsSomeOf = (std::same_as<T, U> || (std::same_as<T, Us> || ...));

    #else  // c++17
    // コンセプトが使えない場合、上と同じ機能を持つ変数テンプレート
    template <typename T, typename U, typename... Us>
    constexpr bool SameAsSomeOf = Inner_::is_same_as_some_of_impl<T, U, Us...>::value;
    #endif

    // 型特性: TがUsのいずれかと同じ場合true_type、そうでない場合false_typeを継承
    template <typename T, typename U, typename... Us>
    struct IsSameSomeOf : std::bool_constant<SameAsSomeOf<T, U, Us...>> {
    };

    // 便利な定数テンプレート
    template <typename T, typename U, typename... Us>
    constexpr bool IsSameSomeOfV = IsSameSomeOf<T, U, Us...>::value;
    }  // namespace Nstd
```

IsSameSomeOfは、TがUsのいずれかと一致するかどうかのほとんどの処理をSameAsSomeOfに移譲する。

Usが1つだった場合、SameAsSomeOfは処理をstd::same_as(「[same_as](#SS_4_3_2_6)」参照)に委譲する。
Usが複数だった場合、[畳み込み式](--)を使用し上記の処理をその数分、繰り返す。

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 14

    static_assert(!Nstd::IsSameSomeOfV<int, int8_t, int16_t, uint16_t>);
    static_assert(Nstd::IsSameSomeOfV<int, int8_t, int16_t, uint16_t, int32_t>);
    static_assert(Nstd::IsSameSomeOfV<int&, int8_t, int16_t, int32_t&, int32_t>);
    static_assert(!Nstd::IsSameSomeOfV<int&, int8_t, int16_t, uint32_t&, int32_t>);
    static_assert(Nstd::IsSameSomeOfV<std::string, int, char*, std::string>);
    static_assert(!Nstd::IsSameSomeOfV<std::string, int, char*>);
```


#### OneOf <a id="SS_4_3_2_9"></a>
OneOfは、[IsSameSomeOf](#SS_4_3_2_8)同様の機能を持つコンセプトである。
OneOfの実装にはシンプルに記述するための[畳み込み式](#SS_6_11_5)を使用した。

```cpp
    //  essential/h/nstd_concepts.h 52

    template <typename T, typename... Us>
    concept OneOf = (std::same_as<T, Us> || ...);
```
単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 29

    static_assert(!Nstd::OneOf<int, int8_t, int16_t, uint16_t>);
    static_assert(Nstd::OneOf<int, int8_t, int16_t, uint16_t, int32_t>);
    static_assert(Nstd::OneOf<int&, int8_t, int16_t, int32_t&, int32_t>);
    static_assert(!Nstd::OneOf<int&, int8_t, int16_t, uint32_t&, int32_t>);
    static_assert(Nstd::OneOf<std::string, int, char*, std::string>);
    static_assert(!Nstd::OneOf<std::string, int, char*>);
```

### AreConvertibleXxxの実装 <a id="SS_4_3_3"></a>
std::is_convertible\<FROM, TO>は、

* 型FROMが型TOに変換できる場合、std::true_typeから派生する
* 型FROMが型TOに変換できない場合、std::false_typeから派生する

のような仕様を持つテンプレートである。

ここでは、

* std::is_convertibleを複数のFROMが指定できるように拡張したNstd::AreConvertible
* 縮小無しでの型変換ができるかどうかを判定するAreConvertibleWithoutNarrowConv

の実装を考える。

|AreConvertibleXxx                     |実装方法                                     |
|--------------------------------------|---------------------------------------------|
|[AreConvertible](#SS_4_3_3_1)                 |クラステンプレートの特殊化                   |
|[ConvertibleToAll](#SS_4_3_3_3)               |AreConvertibleをコンセプトへ                 |
|[AreConvertibleWithoutNarrowConv](#SS_4_3_3_2)|SFINAEとクラステンプレートの特殊化           |
|[ConvertibleWithoutNarrowing](#SS_4_3_3_4)    |AreConvertibleWithoutNarrowConvをコンセプトへ|


#### AreConvertible <a id="SS_4_3_3_1"></a>
AreConvertibleの実装は以下のようになる。

```cpp
    //  example/h/nstd_type_traits.h 53

    namespace Nstd {
    namespace Inner_ {

    template <typename TO, typename FROM, typename... FROMs>
    struct are_convertible {
        static constexpr bool value{std::is_convertible_v<FROM, TO> && are_convertible<TO, FROMs...>::value};
    };

    template <typename TO, typename FROM>
    struct are_convertible<TO, FROM> {
        static constexpr bool value{std::is_convertible_v<FROM, TO>};
    };

    template <typename TO, typename... FROMs>
    constexpr bool are_convertible_v{are_convertible<TO, FROMs...>::value};
    }  // namespace Inner_

    template <typename TO, typename... FROMs>
    struct AreConvertible : std::conditional_t<Inner_::are_convertible_v<TO, FROMs...>, std::true_type, std::false_type> {
    };

    template <typename TO, typename... FROMs>
    constexpr bool AreConvertibleV{AreConvertible<TO, FROMs...>::value};
    }  // namespace Nstd
```


「[IsSameSomeOf](#SS_4_3_2_8)の実装」のコードパターンとほぼ同様であるため、解説は不要だろうが、

* パラメータパックの都合上、TOとFROMのパラメータの位置がstd::is_convertibleとは逆になる
* IsSameSomeOfでは条件の一つがtrueであればIsSameSomeOf::valueがtrueとなるが、
  AreConvertibleでは全条件がtrueとならない限り、AreConvertible::valueがtrueとならない

ので注意が必要である。

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 43

    static_assert(Nstd::AreConvertibleV<int, int8_t, int16_t, int>);
    static_assert(Nstd::AreConvertibleV<int, char, int, int>);
    static_assert(!Nstd::AreConvertibleV<int, char*, int, int>);
    static_assert(Nstd::AreConvertibleV<std::string, std::string, char*, char[3]>);
    static_assert(!Nstd::AreConvertibleV<std::string, std::string, char*, int>);
```


#### AreConvertibleWithoutNarrowConv <a id="SS_4_3_3_2"></a>
縮小無しの型変換ができるかどうかを判定するAreConvertibleWithoutNarrowConvは、
AreConvertibleと同じように実装できるが、
その場合、AreConvertibleに対してstd::is_convertibleが必要になったように、
AreConvertibleWithoutNarrowConvに対しis_convertible_without_narrow_convが必要になる。

縮小無しでFROMからTOへの型変換ができるかどうかを判定するis_convertible_without_narrow_convは、
SFINAEと関数テンプレート/関数のオーバーライドを使用し以下のように実装できる。

```cpp
    //  example/h/nstd_type_traits.h 85

    namespace Nstd {
    namespace Inner_ {

    template <typename TO, typename FROM>
    class is_convertible_without_narrow_conv {
        template <typename T = TO, typename U = FROM>
        static constexpr auto detector(T* t, U* u) noexcept
            // 縮小無しでFROMからTOへ変換可能な場合、*t = T{*u}はwell-formed
            // 上記ではない場合、*t = T{*u}はill-formed
            -> decltype(*t = T{*u}, bool{})
        {
            return true;
        }

        static constexpr bool detector(...) noexcept { return false; }

    public:
        static constexpr bool value{
            is_convertible_without_narrow_conv::detector(static_cast<TO*>(nullptr), static_cast<FROM*>(nullptr))};
    };

    template <typename TO, typename FROM>
    constexpr bool is_convertible_without_narrow_conv_v{is_convertible_without_narrow_conv<TO, FROM>::value};
    }  // namespace Inner_
    }  // namespace Nstd
```

AreConvertibleWithoutNarrowConvはNstdで定義するため、その内部のみで用いる
is_convertible_without_narrow_convはNstd::Inner\_で定義している。

上記を抜粋した下記のコードは「縮小型変換を発生さる{}による初期化は[ill-formed](#SS_6_14_1)になる」
ことをSFINAEに利用している。

```cpp
    //  example/h/nstd_type_traits.h 95

    // 縮小無しでFROMからTOへ変換可能な場合、*t = T{*u}はwell-formed
    // 上記ではない場合、*t = T{*u}はill-formed
    -> decltype(*t = T{*u}, bool{})
```

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 55

    static_assert(Nstd::Inner_::is_convertible_without_narrow_conv_v<int, int>);
    static_assert(Nstd::Inner_::is_convertible_without_narrow_conv_v<int, int16_t>);
    static_assert(!Nstd::Inner_::is_convertible_without_narrow_conv_v<int16_t, int>);
    static_assert(Nstd::Inner_::is_convertible_without_narrow_conv_v<std::string, char*>);
    static_assert(!Nstd::Inner_::is_convertible_without_narrow_conv_v<char*, std::string>);
```

is_convertible_without_narrow_convを利用したAreConvertibleWithoutNarrowConv
の実装は以下のようになる。

```cpp
    //  example/h/nstd_type_traits.h 117

    namespace Nstd {
    namespace Inner_ {

    template <typename TO, typename FROM, typename... FROMs>
    struct are_convertible_without_narrow_conv {
        static constexpr bool value{
            is_convertible_without_narrow_conv_v<TO, FROM> 
                  && are_convertible_without_narrow_conv<TO, FROMs...>::value};
    };

    template <typename TO, typename FROM>
    struct are_convertible_without_narrow_conv<TO, FROM> {
        static constexpr bool value{is_convertible_without_narrow_conv_v<TO, FROM>};
    };

    template <typename TO, typename FROM, typename... FROMs>
    constexpr bool are_convertible_without_narrow_conv_v{are_convertible_without_narrow_conv<TO, FROM, FROMs...>::value};
    }  // namespace Inner_

    template <typename TO, typename FROM, typename... FROMs>
    struct AreConvertibleWithoutNarrowConv
        : std::conditional_t<Inner_::are_convertible_without_narrow_conv_v<TO, FROM, FROMs...>, std::true_type,
                             std::false_type> {
    };

    template <typename TO, typename FROM, typename... FROMs>
    constexpr bool AreConvertibleWithoutNarrowConvV{AreConvertibleWithoutNarrowConv<TO, FROM, FROMs...>::value};
    }  // namespace Nstd
```

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 63

    static_assert(Nstd::AreConvertibleWithoutNarrowConvV<int, char, int16_t, uint16_t>);
    static_assert(!Nstd::AreConvertibleWithoutNarrowConvV<int, char, int16_t, uint32_t>);
    static_assert(Nstd::AreConvertibleWithoutNarrowConvV<std::string, char[5], char*>);
    static_assert(Nstd::AreConvertibleWithoutNarrowConvV<double, float>);

    // int8_t -> doubleは縮小型変換
    static_assert(!Nstd::AreConvertibleWithoutNarrowConvV<double, float, int8_t>);
```

#### ConvertibleToAll <a id="SS_4_3_3_3"></a>
ConvertibleToAllの実装は下記のようになる。

```cpp
    //  essential/h/nstd_concepts.h 57

// 複数の型 FROMs がすべて TO に変換可能かどうかを制約するコンセプト
template <typename TO, typename... FROMs>
concept ConvertibleToAll = (std::convertible_to<FROMs, TO> && ...);
```

使用方法を含めて、単体テストは以下のようになる。

```cpp
    //  example/template/nstd_concepts_ut.cpp 137

    // ConvertibleToAll_Test テンプレートの定義
    template <typename TO, typename... FROMs>
    struct ConvertibleToAll_Test : std::false_type {
    };

    // すべての FROMs が TO に変換可能な場合の部分特殊化
    template <typename TO, typename... Us>
    requires ConvertibleToAll<TO, Us...>
    struct ConvertibleToAll_Test<TO, Us...> : std::true_type {
    };

    struct convert_bool {
        operator bool() const { return false; }
    };

    static_assert(!ConvertibleToAll_Test<bool, int, std::string>::value);
    static_assert(ConvertibleToAll_Test<bool, int, convert_bool>::value);
```

#### ConvertibleWithoutNarrowing <a id="SS_4_3_3_4"></a>
ConvertibleWithoutNarrowingは以下のようなコンセプトである。

* [AreConvertibleWithoutNarrowConv](#SS_4_3_3_2)と同様の機能を持つ
* [ConvertibleToAll](#SS_4_3_3_3)と同様構造を持つ

実装は以下のようになる。

```cpp
    //  essential/h/nstd_concepts.h 63

namespace Inner_ {

template <typename TO, typename FROM>
concept convertible_without_narrowing = requires(FROM from)
{
    { TO {from} } -> std::same_as<TO>;
};

// 複数の型が変換可能かどうかを確認するバージョン
template <typename TO, typename... FROMs>
concept all_convertible_without_narrowing = (convertible_without_narrowing<TO, FROMs> && ...);

}  // namespace Inner_

// コンセプトを使用
template <typename TO, typename... FROMs>
concept ConvertibleWithoutNarrowing = Inner_::all_convertible_without_narrowing<TO, FROMs...>;
```

単体テストは他の似たコンセプトとほぼ同様になるため省略する。


### 関数の存在の診断 <a id="SS_4_3_4"></a>
Nstdライブラリの開発には関数の存在の診断が欠かせない。
例えば、

* テンプレートパラメータに特定のメンバ関数がある場合、特殊化を作る
* テンプレートパラメータに範囲for文が適用できる場合にのみoperator<<を適用する
* テンプレートパラメータに適用できるoperator<<がすでにあった場合、
  自作operator<<を不活性化する

等、応用範囲は多岐にわたる。
ここでは、上記の場合分けを可能とするようなメタ関数に必要なテクニックや、
それらを使用したNstdのメタ関数の実装を下記のように示す。

* テンプレートパラメータである型が、メンバ関数void func()を持つかどうかの診断について、
  次の表のように実装を示す。

|メタ関数名                              |メタ関数の目的                                    |
|----------------------------------------|--------------------------------------------------|
|[exists_void_func_sfinae_f](#SS_4_3_4_1)        |メンバ関数void func()を持つかどうかの判断         |
|[exists_void_func_sfinae_s](#SS_4_3_4_2)        |同上                                              |
|[exists_void_func_sfinae_s2](#SS_4_3_4_3)       |同上                                              |
|[exists_void_func_concept](#SS_4_3_4_4)         |同上。コンセプトによるSFINAEの回避                |

* テンプレートパラメータに範囲for文ができるかどうかの診断について、
  次の表のように実装を示す。

|メタ関数名                            |メタ関数の目的                                                     |
|--------------------------------------|-------------------------------------------------------------------|
|[exists_begin/exsits_end](#SS_4_3_4_5)        |SFINAEを使用したstd::begin(T)/std::end(T)が存在するか否かの診断    |
|[Array](#SS_4_3_4_7)                          |型が配列である制約を行うためのコンセプト                           |
|[Beginable/Endable](#SS_4_3_4_8)              |[コンセプト](#SS_6_11_3)を使用したexists_begin/exsits_endを単純化した例   |
|[IsRange](#SS_4_3_4_6)                        |exists_begin/exsits_endを使し、範囲forのオペランドになれるか?の判断|
|[Ranged](#SS_4_3_4_9)                         |機能はIsRangeと同一だが、[コンセプト](#SS_6_11_3)を使用しSFINAEの回避     |
|[Container](#SS_4_3_4_10)                      |Ranged且つ!Arrayをコンテナと便宜的に決めつける                     |

* テンプレートパラメータにoperator<<(put toと発音する)ができるかどうかの診断について、
  次の表のように実装を示す。

|メタ関数名                            |メタ関数の目的                                         |
|--------------------------------------|-------------------------------------------------------|
|[exists_put_to_as_member](#SS_4_3_4_11)        |std::ostream::operator<<(T)が存在するか否かの診断      |
|[exists_put_to_as_non_member](#SS_4_3_4_12)    |operator<<(std::ostream&, T)が存在するか否かの診断     |
|[ExistsPutTo](#SS_4_3_4_13)                    |std::ostream& << Tができるかどうかの診断               |
|[Printable](#SS_4_3_4_14)                      |std::ostream& << Tができるかどうか制約コンセプト       |

* テンプレートパラメータがT[N]やC\<T>の形式である時のTに、
  operator<<が適用できるかの診断については、Tの型を取り出す必要がある。
  そのようなメタ関数ValueTypeの実装を示す。


#### exists_void_func_sfinae_f <a id="SS_4_3_4_1"></a>
「テンプレートパラメータである型が、メンバ関数void func()を持つかどうかを診断する」
exists_void_func_sfinae_f
のSFINAEと関数テンプレート/関数のオーバーロードを用いた実装は以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 13

    namespace Inner_ {

    template <typename T>
    using exists_void_func_void =
        // メンバvoid func(void)があれば、voidを生成
        // メンバvoid func(void)がなければ、ill-formed
        typename std::enable_if_t<std::is_same_v<decltype(std::declval<T>().func()), void>>;
    }  // namespace Inner_

    template <typename T, typename = Inner_::exists_void_func_void<T>>
    constexpr bool exists_void_func_sfinae_f(T) noexcept
    {
        return true;
    }

    constexpr bool exists_void_func_sfinae_f(...) noexcept { return false; }
```

decltypeの中での関数呼び出しは、実際には呼び出されず関数の戻り値の型になる。
上記の抜粋である下記のコードはこの性質を利用してSFINAEによる静的ディスパッチを行っている。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 20

    // メンバvoid func(void)があれば、voidを生成
    // メンバvoid func(void)がなければ、ill-formed
    typename std::enable_if_t<std::is_same_v<decltype(std::declval<T>().func()), void>>;
```

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 40

    // テスト用クラス
    struct X {
        void func();
    };

    struct Y {
        int func();
    };

    struct Z {
    private:
        void func();  // privateなvoid func()は外部からは呼び出せない
    };
```

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 60

    static_assert(!exists_void_func_sfinae_f(int{}));
    static_assert(exists_void_func_sfinae_f(X{}));
    static_assert(!exists_void_func_sfinae_f(Y{}));
    static_assert(!exists_void_func_sfinae_f(Z{}));
```


#### exists_void_func_sfinae_s <a id="SS_4_3_4_2"></a>
「テンプレートパラメータである型が、メンバ関数void func()を持つかどうかを診断」する
exists_void_func_sfinae_s
のSFINAEとクラステンプレートの特殊化を用いた実装は以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 69

    template <typename T, typename U = void>
    struct exists_void_func_sfinae_s : std::false_type {
    };

    template <typename T>
    struct exists_void_func_sfinae_s<T,
        // メンバvoid func()が呼び出せれば、voidを生成
        // メンバvoid func()が呼び出せなければ、ill-formed
        decltype(std::declval<T>().func())
        > : std::true_type {
    };

    template <typename T>
    constexpr bool exists_void_func_sfinae_s_v{exists_void_func_sfinae_s<T>::value};
```

exists_void_func_sfinae_fとほぼ等しいSFINAEを利用したクラステンプレートの特殊化により、
静的ディスパッチを行っている。

単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 91

    static_assert(!exists_void_func_sfinae_s_v<int>);
    static_assert(exists_void_func_sfinae_s_v<X>);
    static_assert(!exists_void_func_sfinae_s_v<Y>);
    static_assert(!exists_void_func_sfinae_s_v<Z>);
```


#### exists_void_func_sfinae_s2 <a id="SS_4_3_4_3"></a>
exists_void_func_sfinae_sとほぼ同様の仕様を持つexists_void_func_sfinae_s2の

* SFINAE
* メンバ関数テンプレート/メンバ関数のオーバーロード
* メンバ関数へのポインタ

を用いた実装は以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 100

    template <typename T>
    class exists_void_func_sfinae_s2 {

        // メンバvoid func()が呼び出せれば、メンバ関数テンプレートはtrueを返す
        // メンバvoid func()が呼び出せなければ、ill-formed
        template <typename U, void (U::*)() = &U::func>
        static constexpr bool detector(U*) noexcept
        {
            return true;
        }

        static constexpr bool detector(...) noexcept { return false; }

    public:
        static constexpr bool value{exists_void_func_sfinae_s2::detector(static_cast<T*>(nullptr))};
    };

    template <typename T>
    constexpr bool exists_void_func_sfinae_s2_v{exists_void_func_sfinae_s2<T>::value};
```

前2例とは異なり、上記の抜粋である下記コードのように、
メンバ関数へのポインタを使用しSFINAEを実装している。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 105

    // メンバvoid func()が呼び出せれば、メンバ関数テンプレートはtrueを返す
    // メンバvoid func()が呼び出せなければ、ill-formed
    template <typename U, void (U::*)() = &U::func>
    static constexpr bool detector(U*) noexcept
    {
        return true;
    }
```

あまり応用範囲が広くない方法ではあるが、
decltypeを使っていないのでC++03コンパイラにも受け入れられるメリットがある。

exists_void_func_sfinae_fと同じテスト用クラスを用いた単体テストは以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 129

    static_assert(!exists_void_func_sfinae_s2_v<int>);
    static_assert(exists_void_func_sfinae_s2_v<X>);
    static_assert(!exists_void_func_sfinae_s2_v<Y>);
    static_assert(!exists_void_func_sfinae_s2_v<Z>);
```


#### exists_void_func_concept <a id="SS_4_3_4_4"></a>
[exists_void_func_sfinae_s](#SS_4_3_4_2)や[exists_void_func_sfinae_s2](#SS_4_3_4_3)
の実装で見たようなSFINAEによるテンプレートの特殊化は難解なコードを生み出す。
また、シンタックスエラー時、ほぼ理解できない大量のコンパイラのメッセージを生成する。
このため、このようなテクニックはきわめて有用である一方で、開発に多くの時間を消費する、
保守員を選んでしまう、といった問題があった。
以下に示すように、C++20から導入された[コンセプト](#SS_6_11_3)はこのような問題の軽減につながる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 138

    #if __cplusplus >= 202002L  // c++20
    template <typename T>  // C++20スタイル。concept/requiresによるSFINAEの回避
    concept exists_void_func_concept = requires(T& t)
    {
        { t.func() } -> std::same_as<void>;
    };

    #else  // c++17
    namespace Inner_ {
    template <typename T, typename = void>
    struct exists_void_func_impl : std::false_type {
    };

    template <typename T>  // C++17スタイル。SFINAEでの実装
    struct exists_void_func_impl<T,
                                 std::void_t<decltype(std::declval<T&>().func())>>  // func()が呼び出し可能か確認
        : std::is_same<void, decltype(std::declval<T&>().func())>                   // 戻り値がvoidか確認
    {
    };
    }  // namespace Inner_

    template <typename T>
    inline constexpr bool exists_void_func_concept = Inner_::exists_void_func_impl<T>::value;
    #endif
```
```cpp
    //  example/template_cpp17/exists_func_ut.cpp 170
    static_assert(!exists_void_func_concept<decltype(int{})>);
    static_assert(exists_void_func_concept<decltype(X{})>);
    static_assert(!exists_void_func_concept<decltype(Y{})>);  // Y::funcの戻りはint
    static_assert(!exists_void_func_concept<decltype(Z{})>);  // Z::funcは呼び出せない
```

#### exists_begin/exsits_end <a id="SS_4_3_4_5"></a>
「テンプレートパラメータTに対して、
std::begin(T)が存在するか否かの診断」をするexists_beginの実装は、
「[exists_void_func_sfinae_s](#SS_4_3_4_2)」
で用いたパターンのメンバ関数を非メンバ関数に置き換えて使えば以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 180

    template <typename, typename = void>
    struct exists_begin : std::false_type {
    };

    template <typename T>
    struct exists_begin<T, std::void_t<decltype(std::begin(std::declval<T>()))>> : std::true_type {
    };

    template <typename T>
    constexpr bool exists_begin_v{exists_begin<T>::value};
```

上記で使用したstd::void_tは、テンプレートパラメータが

* [ill-formed](#SS_6_14_1)ならばill-formedになる
* [well-formed](#SS_6_14_2)ならvoidを生成する

テンプレートである。

下記単体テストでは問題ないように見えるが、

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 196

    static_assert(exists_begin_v<std::string>);
    static_assert(!exists_begin_v<int>);
    static_assert(exists_begin_v<int const[3]>);
```

下記の単体テストはstatic_assertがフェールするためコンパイルできない。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 206

    // 以下が問題
    static_assert(exists_begin_v<int[3]>);
```

理由は、

```cpp
    std::declval<int[3]>())
```

の戻り型が配列型の[rvalue](#SS_6_7_1_2)である"int (&&) [3]"となり、
これに対応するstd::beginが定義されていないためである。

これに対処する方法方はいくつかあるが、
すべての配列は常にstd::beginの引数になれることに気づけば、
テンプレートパラメータが配列か否かで場合分けしたクラステンプレートの特殊化を使い、
下記のように実装できることにも気付けるだろう。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 223

    template <typename, typename = void>
    struct exists_begin : std::false_type {
    };

    // Tが非配列の場合の特殊化
    template <typename T>
    struct exists_begin<
        T, typename std::enable_if_t<!std::is_array_v<T>, std::void_t<decltype(std::begin(std::declval<T>()))>>>
        : std::true_type {
    };

    // Tが配列の場合の特殊化
    template <typename T>
    struct exists_begin<T, typename std::enable_if_t<std::is_array_v<T>>> : std::true_type {
    };

    template <typename T>
    constexpr bool exists_begin_v{exists_begin<T>::value};
```

2個目のexists_beginはTが配列でない場合、
3個目のexists_beginはTが配列ある場合にそれぞれが対応しているが、複雑すぎて何とも醜い。
ということで、このコードは却下して、別のアイデアを試そう。

テンプレートパラメータが配列である場合でも、
そのオブジェクトが[lvalue](#SS_6_7_1_1)(この例ではint (&)[3])であれば、
std::beginはそのオブジェクトを使用できるので、
decltype内で使用できるlvalueのT型オブジェクトを生成できれば、
と考えれば下記のような実装を思いつくだろう。

```cpp
    //  example/h/nstd_type_traits.h 158

    template <typename, typename = void>
    struct exists_begin : std::false_type {
    };

    template <typename T>
    struct exists_begin<T, std::void_t<decltype(std::begin(std::declval<T&>()))>> : std::true_type {
    };

    template <typename T>
    constexpr bool exists_begin_v{exists_begin<T>::value};
```

十分にシンプルなのでこれを採用し、exists_endも同様に実装する。

```cpp
    //  example/h/nstd_type_traits.h 171

    template <typename, typename = void>
    struct exists_end : std::false_type {
    };

    template <typename T>
    struct exists_end<T, std::void_t<decltype(std::end(std::declval<T&>()))>> : std::true_type {
    };
    template <typename T>
    constexpr bool exists_end_v{exists_end<T>::value};
```

単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 97

    static_assert(exists_begin_v<std::string>);
    static_assert(!exists_begin_v<int>);
    static_assert(exists_begin_v<int const[3]>);
    static_assert(exists_begin_v<int[3]>);  // 問題が解決

    static_assert(exists_end_v<std::string>);
    static_assert(!exists_end_v<int>);
    static_assert(exists_end_v<int const[3]>);
    static_assert(exists_end_v<int[3]>);
```

#### IsRange <a id="SS_4_3_4_6"></a>
[範囲for文](https://cpprefjp.github.io/lang/cpp11/range_based_for.html)
文の":"の後ろにT型オブジェクトが指定できる要件は、

* std::begin(T)、std::end(T)がTのイテレータであるITOR型のオブジェクトを返す
* std::begin(T)が返すITORオブジェクトはTが保持する先頭の要素を指す
* std::end(T)が返すITORオブジェクトはTが保持する最後の要素の次を指す
* ++ITORによりTが保持する全要素にアクセスできる

ようなことである。多くの要件はセマンティクス的なものであり、
メタ関数で診断できることは前項で見たようなstd::begin(T)、std::end(T)の可否のみであると考えれば、
IsRangeの実装は以下のようになる。

```cpp
    //  example/h/nstd_type_traits.h 185

    template <typename T>
    struct IsRange
        : std::conditional_t<Inner_::exists_begin_v<T> && Inner_::exists_end_v<T>, std::true_type, std::false_type> {
    };

    template <typename T>
    constexpr bool IsRangeV{IsRange<T>::value};
```

なお、上記のコードでは、exists_begin/exsits_endは、IsRangeの実装の詳細であるため、
名前空間Inner\_で宣言している。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 116

    static_assert(IsRangeV<std::string>);
    static_assert(!IsRangeV<int>);
    static_assert(IsRangeV<int const[3]>);
    static_assert(IsRangeV<int[3]>);
```


#### Array <a id="SS_4_3_4_7"></a>

以降の節で使用するため、テンプレートパラメータが配列である制約を下記のように宣言する。

```cpp
    //  essential/h/nstd_concepts.h 9

    template <typename T>
    concept Array = std::is_array_v<T>;
```
```cpp
    //  example/template/nstd_concepts_ut.cpp 18

    int  a[3];
    int* ptr = a;
    auto v   = std::vector{1, 2, 3};

    static_assert(Array<decltype(a)>);

    static_assert(Array<decltype(a)>);
    static_assert(!Array<decltype(ptr)>);
```

#### Beginable/Endable <a id="SS_4_3_4_8"></a>
コンセプトを使用し、[exists_begin/exsits_end](#SS_4_3_4_5)をリファクタリングした例を以下に示す。

```cpp
    //  essential/h/nstd_concepts.h 15

    template <typename T>
    concept Beginable = Array<T> || requires(T& t)
    {
        { std::begin(t) } -> std::same_as<typename T::iterator>;
    };

    template <typename T>
    concept Endable = Array<T> || requires(T& t)
    {
        { std::end(t) } -> std::same_as<typename T::iterator>;
    };
```
```cpp
    //  example/template/nstd_concepts_ut.cpp 34

    int  a[3];
    int* ptr = a;
    auto v   = std::vector{1, 2, 3};

    static_assert(Array<decltype(a)>);

    static_assert(Beginable<decltype(a)>);
    static_assert(!Beginable<decltype(ptr)>);
    static_assert(Beginable<decltype(v)>);
```


#### Ranged <a id="SS_4_3_4_9"></a>
IsRangeと同一の機能を持つコンセプトRangedを以下のように定義する。

```cpp
    //  essential/h/nstd_concepts.h 33

    template <typename T>
    concept Ranged = Beginable<T> && Endable<T>;
```

単体テストは以下のようになる。

```cpp
    //  example/template/nstd_concepts_ut.cpp 53

    static_assert(Ranged<std::string>);
    static_assert(!Ranged<int>);
    static_assert(Ranged<int const[3]>);
    static_assert(Ranged<int[3]>);
```

すでにみたようにRangedは[exists_begin/exsits_end](#SS_4_3_4_5)の醜いコードを使用しないことで、
Rangedの可読性はIsRangedに比べ格段に改善している。

#### Container <a id="SS_4_3_4_10"></a>
与えられた型をコンテナに制約するためのコンセプトを下記のように便宜的に宣言する。

```cpp
    //  essential/h/nstd_concepts.h 33

    template <typename T>
    concept Ranged = Beginable<T> && Endable<T>;
```

単体テストには少々の工夫が必要になる。

```cpp
    //  example/template/nstd_concepts_ut.cpp 62

    struct X {
        std::vector<int> data{1, 2, 3, 4, 5};

        auto begin() { return data.begin(); }  // std::begin
        auto end() { return data.end(); }      // std::end
    };

    //  example/template/nstd_concepts_ut.cpp 74

    static_assert(Container<std::string>);
    static_assert(!Container<int>);
    static_assert(!Container<int const[3]>);

    static_assert(!Ranged<X>);  // begin/endがあるが、value_typeをもっていない

```

#### exists_put_to_as_member <a id="SS_4_3_4_11"></a>
std::ostreamのメンバ関数operator<<の戻り型はstd::ostream&であるため、
exists_put_to_as_memberの実装は以下のようになる("<<"は英語で"put to"と発音する)。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 258

    template <typename, typename = std::ostream&>
    struct exists_put_to_as_member : std::false_type {
    };

    template <typename T>
    struct exists_put_to_as_member<T, decltype(std::declval<std::ostream&>().operator<<(std::declval<T>()))>
        : std::true_type {
    };

    template <typename T>
    constexpr bool exists_put_to_as_member_v{exists_put_to_as_member<T>::value};
```

「[exists_void_func_sfinae_f](#SS_4_3_4_1)の実装」と同様のパターンを使用したので解説は不要だろう。

単体テストは以下のようになる。

```cpp
    //  example/template/test_class.h 3

    class test_class_exits_put_to {
    public:
        test_class_exits_put_to(int i = 0) noexcept : i_{i} {}
        int get() const noexcept { return i_; }

    private:
        int i_;
    };

    inline std::ostream& operator<<(std::ostream& os, test_class_exits_put_to const& p) { return os << p.get(); }

    class test_class_not_exits_put_to {};
```

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 275

    static_assert(exists_put_to_as_member_v<bool>);
    static_assert(!exists_put_to_as_member_v<std::string>);
    static_assert(!exists_put_to_as_member_v<std::vector<int>>);
    static_assert(exists_put_to_as_member_v<std::vector<int>*>);
    static_assert(!exists_put_to_as_member_v<test_class_exits_put_to>);
    static_assert(!exists_put_to_as_member_v<test_class_not_exits_put_to>);
    static_assert(exists_put_to_as_member_v<test_class_not_exits_put_to[3]>);  // 驚き!
```

やや驚きなのは、上記の抜粋である下記コードがコンパイルできることである。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 284

    static_assert(exists_put_to_as_member_v<test_class_not_exits_put_to[3]>);  // 驚き!
```

これは、

```cpp
    std::ostream& std::ostream::operator<<(void const*)
```

が定義されているため、配列がポインタに変換されてこのメンバ関数にバインドした結果である。


#### exists_put_to_as_non_member <a id="SS_4_3_4_12"></a>
exists_put_to_as_non_memberの実装は以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 293

    template <typename, typename = std::ostream&>
    struct exists_put_to_as_non_member : std::false_type {
    };

    template <typename T>
    struct exists_put_to_as_non_member<T, decltype(operator<<(std::declval<std::ostream&>(), std::declval<T>()))>
        : std::true_type {
    };

    template <typename T>
    constexpr bool exists_put_to_as_non_member_v{exists_put_to_as_non_member<T>::value};
```

「[exists_begin/exsits_end](#SS_4_3_4_5)や[exists_put_to_as_member](#SS_4_3_4_11)の実装」
で使用したパターンを混合しただけなので解説や単体テストは省略する。


#### ExistsPutTo <a id="SS_4_3_4_13"></a>
テンプレートパラメータT、T型オブジェクトtに対して、
std::ostream << tができるかどうかを判断するExistsPutToの実装は以下のようになる。

```cpp
    //  example/template_cpp17/exists_func_ut.cpp 322

    template <typename T>
    struct ExistsPutTo
        : std::conditional_t<Inner_::exists_put_to_as_member_v<T> || Inner_::exists_put_to_as_non_member_v<T>,
                             std::true_type, std::false_type> {
    };

    template <typename T>
    constexpr bool ExistsPutToV{ExistsPutTo<T>::value};
```

「[IsRange](#SS_4_3_4_6)の実装」に影響されて、一旦このように実装したが、先に書いた通り、
そもそものExistsPutToの役割はstd::ostream << tができるかどうかの診断であることを思い出せば、
下記のように、もっとシンプルに実装できることに気づくだろう。

```cpp
    //  example/h/nstd_type_traits.h 200

    namespace Nstd {

    template <typename, typename = std::ostream&>
    struct ExistsPutTo : std::false_type {
    };

    template <typename T>
    struct ExistsPutTo<T, decltype(std::declval<std::ostream&>() << std::declval<T>())> : std::true_type {
    };

    template <typename T>
    constexpr bool ExistsPutToV{ExistsPutTo<T>::value};
    }  // namespace Nstd
```

単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 127

    static_assert(Nstd::ExistsPutToV<bool>);
    static_assert(Nstd::ExistsPutToV<std::string>);
    static_assert(!Nstd::ExistsPutToV<std::vector<int>>);
    static_assert(Nstd::ExistsPutToV<std::vector<int>*>);
    static_assert(Nstd::ExistsPutToV<test_class_exits_put_to>);
    static_assert(!Nstd::ExistsPutToV<test_class_not_exits_put_to>);
    static_assert(Nstd::ExistsPutToV<test_class_not_exits_put_to[3]>);
```

#### Printable <a id="SS_4_3_4_14"></a>
これまでのパターンに従ってPrintableを以下のように作る。

* [SFINAE](#SS_6_11_1)を利用した[ExistsPutTo](#SS_4_3_4_13)は複雑で醜いため、リファクタリングする。
* リファクタリングに合わせてコンセプト化し、それらしい名称にする。

```cpp
    //  essential/h/nstd_concepts.h 42

    template <typename T>
    concept Printable = requires(T t, std::ostream& os)
    {
        { os << t } -> std::same_as<std::ostream&>;
    };
```
```cpp
    //  example/template/nstd_concepts_ut.cpp 86

    struct X {};  // Non-pritable
    struct Y {};  // Printable

    std::ostream& operator<<(std::ostream& os, Y)
    {
        return os;  // 何もしない
    }

    //  example/template/nstd_concepts_ut.cpp 99

    static_assert(Printable<bool>);
    static_assert(Printable<std::string>);
    static_assert(!Printable<std::vector<int>>);
    static_assert(Printable<std::vector<int>*>);
    static_assert(!Printable<X>);
    static_assert(Printable<Y>);
```

これ以降は、[ExistsPutTo](#SS_4_3_4_13)ではなくPrintableを使用する。

#### ValueTypeの実装 <a id="SS_4_3_4_15"></a>
下記で示す通り、

```cpp
    //  example/template_cpp17/nstd_type_traits_ut.cpp 145

    struct T {};

    std::ostream& operator<<(std::ostream& os, std::vector<T> const& x) { return os << "T:" << x.size(); }

    std::ostream& operator<<(std::ostream&, T const&) = delete;

    static_assert(!Nstd::ExistsPutToV<T>);              // std::cout << T{} はできない
    static_assert(Nstd::ExistsPutToV<std::vector<T>>);  // std::cout << std::vector<T>{} はできる
    static_assert(Nstd::ExistsPutToV<T[3]>);            // std::cout << T[3]{} はできる
```

型Xが与えれ、その形式が、

* クラステンプレートCとその型パラメータTにより、C\<T>
* 型Tと定数整数Nにより、T[N]

のような場合、Printable\<X>がtrueであっても、Printable\<T>の真偽はわからない。
従って上記のようなTに対して、Printable\<T>がtrueかどうかを診断するためには、
XからTを導出することが必要になる。ここでは、そのようなメタ関数ValueTypeの実装を考える。
このValueTypeは上記のX、Tに対して、

```cpp
    static_assert(std::is_same<ValueType<X>::type, T>);
    // もしくは、
    static_assert(std::is_same<ValueType<X, T>);
```

となるような機能を持たなければならないことは明らかだろう。
その他の機能については実装しながら決定していく。

一見、難しそうなテンプレートを作るコツは、条件を絞って少しずつ作っていくことである。
いきなり大量のテンプレートを書いてしまうと、
その何十倍ものコンパイルエラーに打ちのめされること必至である。

ということで、まずは、1次元の配列に対してのみ動作するValueTypeの実装を示す
(下記で使用するstd::remove_extent_t\<T>は、テンプレートパラメータが配列だった場合に、
その次元を一つだけ除去するメタ関数である)。

```cpp
    //  example/template/value_type_ut.cpp 18

    template <typename T, typename = void>
    struct ValueType {
        using type = void;
    };

    template <typename T, size_t N>
    struct ValueType<T[N]> {  // 配列型の特殊化
        using type = T;
    };

    template <typename T>
    using ValueTypeT = typename ValueType<T>::type;
```

このコードは問題なく動作するが、下記の通り、2次元配列に対するValueType::typeは1次元配列となる。

```cpp
    //  example/template/value_type_ut.cpp 36

    static_assert(std::is_same_v<int, ValueTypeT<int[1]>>);
    static_assert(std::is_same_v<void, ValueTypeT<int>>);
    static_assert(std::is_same_v<int[2], ValueTypeT<int[1][2]>>);
```

これを多次元配列に拡張する前に、配列の次元をで返すValueType::Nestや、extent、type_directを追加することにすると、
コードは下記のようになるだろう。

```cpp
    //  example/template/value_type_ut.cpp 49

    template <typename T, typename = void>
    struct ValueType {
        using type        = void;
        using type_direct = T;
        static constexpr size_t Nest{0};
    };

    template <typename T, size_t N>
    struct ValueType<T[N]> {  // 配列型の特殊化
        using type                     = T;
        using type_direct              = T;  // T = S[N]の場合、Tを保存
        static constexpr size_t extent = N;  // T = S[N]の場合、Nを保存
        static constexpr size_t Nest{ValueType<type>::Nest + 1};
    };

    template <typename T>
    using ValueTypeT = typename ValueType<T>::type;
```

動作は下記のようになる。

```cpp
    //  example/template/value_type_ut.cpp 76

    static_assert(0 == ValueType<int>::Nest);
    static_assert(1 == ValueType<int[1]>::Nest);
    static_assert(2 == ValueType<int[1][2]>::Nest);
    static_assert(1 == ValueType<int[1]>::extent);
    static_assert(1 == ValueType<int[1][2]>::extent);  // int[1][2] == (int[1])[2]
```

ここで、下記のような仕様をもつValueType::type_n\<N>を考える。

```
    ValueType<int[1][2][3]>::type_n<0>が表す型は、int[1][2][3]
    ValueType<int[1][2][3]>::type_n<1>が表す型は、int[2][3]
    ValueType<int[1][2][3]>::type_n<2>が表す型は、int[3]
    ValueType<int[1][2][3]>::type_n<3>が表す型は、int
```

ValueType::type_n\<N>は玉ねぎの皮を一枚ずつむくようなメンバテンプレートになる。
プライマリの実装は以下のようになる。

```cpp
    //  example/template/value_type_ut.cpp 91

    template <typename T>
    struct ValueType {
        using type                     = T;
        using type_direct              = T;
        static constexpr size_t extent = 0;
        static constexpr size_t Nest   = 0;

        template <size_t N>
        using type_n = std::conditional_t<N == 0, T, void>;  // Nが0のときはT、それ以外はvoidを返す
    };
```

Nが非0の場合、Value::type_n\<N>はvoidになる仕様にした。

配列に対する特殊化は以下のようになる。

```cpp
    //  example/template/value_type_ut.cpp 104

    template <typename T, size_t N>  // Array Tを使わずに配列の一般的な表現を使用してNを取り出す
    struct ValueType<T[N]> {         // 配列型の特殊化
        using type                     = typename ValueType<T>::type;
        using type_direct              = T;
        static constexpr size_t extent = N;
        static constexpr size_t Nest   = ValueType<T>::Nest + 1;

        template <size_t M>
        using type_n = std::conditional_t<M == 0, T[N], typename ValueType<T>::template type_n<M - 1>>;
    };
```

Value::type_n\<>のリカーシブ展開を頭の中で行うことは難しいので、
読者の理解を確かめるため、以下のように順を追って一枚づつ配列の階層を剝ぎ取る様子を見ていく。

```cpp
    //  example/template/value_type_ut.cpp 126

    // ValueType<int[1][2][3]>の展開について、考えよう。

    // int[1][2][3]は == (int[2][3])[1]であるため、下記の式が成立する
    static_assert(std::is_same_v<ValueType<int[1][2][3]>::type_direct, int[2][3]>);
    static_assert(ValueType<int[1][2][3]>::extent == 1);

    // type_n<M>の仕様は、Mが1の時、配列から1階層を1枚剥ぎ取ることである
    using T1 = ValueType<int[1][2][3]>::type_n<1>;  // 長い式は可読性が劣化するからT1を宣言

    // int[2][3] == (int[3])[2]であるため、下記の式が成立する
    static_assert(std::is_same_v<T1, int[2][3]>);
    static_assert(ValueType<T1>::extent == 2);

    // 上記T1と同様にT2を宣言する
    using T2 = ValueType<T1>::type_n<1>;

    // int[2][3] == (int[3])[2]であるため、下記の式が成立する
    static_assert(std::is_same_v<T2, int[3]>);
    static_assert(ValueType<T2>::extent == 3);

    // 上記T1、T2と同様にT3を宣言する
    using T3 = ValueType<T2>::type_n<1>;

    static_assert(std::is_same_v<T3, int>);
    static_assert(ValueType<T3>::extent == 0);
```

単体テストは下記のようになる。

```cpp
    //  example/template/value_type_ut.cpp 155

    using T = int[1][2][3];

    static_assert(std::is_same_v<int[1][2][3], ValueType<T>::type_n<0>>);  // 0枚剝く
    static_assert(std::is_same_v<int[2][3], ValueType<T>::type_n<1>>);     // 1枚剝く
    static_assert(std::is_same_v<int[3], ValueType<T>::type_n<2>>);        // 2枚剝く
    static_assert(std::is_same_v<int, ValueType<T>::type_n<3>>);           // 3枚剝く
    static_assert(std::is_same_v<void, ValueType<T>::type_n<4>>);          // 全部剝く
```

また、ValueType::NestとValueType::type_n<>の関係に注目すれば、
上記エイリアスTに対して下記が成立する。

```cpp
    //  example/template/value_type_ut.cpp 178

    using T = ValueTypeT_n<int[1][2][3], 3>;

    static_assert(std::is_same_v<int, T>);
    static_assert(std::is_same_v<int, ValueTypeT_n<T, ValueType<T>::Nest>>);
```


このテンプレートにコンテナが渡された時の特殊化を与えることができればValueTypeは完成するが、
こういったタイミングで、リファクタリングを行い名前の整理や不要になったコードを削除することは良い習慣である。

これによりValueTypeは下記のようになる。

```cpp
    //  example/template/value_type_ut.cpp 240

    template <typename T>
    struct ValueType {  // プライマリ
        using type                   = T;
        static constexpr size_t Nest = 0;

        template <size_t N>
        using type_n = std::conditional_t<N == 0, T, void>;
    };

    template <typename T, size_t N>
    struct ValueType<T[N]> {  // 配列型の特殊化
        using type                   = typename ValueType<T>::type;
        static constexpr size_t Nest = ValueType<T>::Nest + 1;

        template <size_t M>
        using type_n = std::conditional_t<M == 0, T[N], typename ValueType<T>::template type_n<M - 1>>;
    };
```

準備は整ったので上記のValueTypeに下記のようなコンテナ用特殊化を追加する。
この特殊化のテンプレートパラメータの制約にはすでに開発したコンセプト[Container](#SS_4_3_4_10)を使用する。

```cpp
    //  example/template/value_type_ut.cpp 261

    template <Container T>
    struct ValueType<T> {  // コンテナ型の特殊化
        using type                   = typename ValueType<typename T::value_type>::type;
        static constexpr size_t Nest = ValueType<typename T::value_type>::Nest + 1;

        template <size_t N>
        using type_n = std::conditional_t<N == 0, T, typename ValueType<typename T::value_type>::template type_n<N - 1>>;
    };
```

まずは、追加した特殊化の機能を下記のように単体テストを行う。

```cpp
    //  example/template/value_type_ut.cpp 278

    using T = int[1][2][3];

    // コンテナ特殊化以外の機能チェック
    static_assert(std::is_same_v<T, ValueType<T>::type_n<0>>);
    static_assert(std::is_same_v<int[2][3], ValueType<T>::type_n<1>>);
    static_assert(std::is_same_v<int[3], ValueType<T>::type_n<2>>);
    static_assert(std::is_same_v<int, ValueType<T>::type_n<3>>);
    static_assert(std::is_same_v<int, ValueType<T>::type>);
```

次に特殊化がデグレードを起こしていないことを下記のように証明する。

```cpp
    //  example/template/value_type_ut.cpp 291

    // コンテナ特殊化の機能の機能チェック
    using T = std::vector<std::vector<std::vector<int>>>;

    static_assert(std::is_same_v<T, ValueType<T>::type_n<0>>);
    static_assert(std::is_same_v<int, ValueType<T>::type_n<3>>);
    static_assert(ValueType<T>::Nest == 3);
    static_assert(std::is_same_v<int, ValueType<T>::type>);
```

ValueTypeの最終的な単体テストのために上記を統合したテストを行う。

```cpp
    //  example/template/value_type_ut.cpp 303

    // 統合した機能チェック
    using T = std::vector<int[1][2][3]>;

    static_assert(std::is_same_v<T, ValueType<T>::type_n<0>>);
    static_assert(std::is_same_v<int[1][2][3], ValueType<T>::type_n<1>>);
    static_assert(std::is_same_v<int[2][3], ValueType<T>::type_n<2>>);
    static_assert(std::is_same_v<int[3], ValueType<T>::type_n<3>>);
    static_assert(std::is_same_v<int, ValueType<T>::type_n<4>>);
    static_assert(std::is_same_v<int, ValueType<T>::type>);
    static_assert(ValueType<T>::Nest == 4);

    using L = std::list<T>;

    static_assert(std::is_same_v<T, ValueType<L>::type_n<1>>);
    static_assert(std::is_same_v<int[1][2][3], ValueType<L>::type_n<2>>);
    static_assert(std::is_same_v<int, ValueType<T>::type>);
    static_assert(ValueType<L>::Nest == 5);
```

以上でValueTypeは完成したが、これ以降のこのドキュメントの前準備として、
多少のメンバの追加や調整をした最終のコードを以下に示す。

```cpp
    //  example/h/nstd_type_traits.h 220

    namespace Nstd {
    template <typename T, typename = void>  // ValueTypeのプライマリ
    struct ValueType {
        using type_direct = void;

        static constexpr bool   IsBuiltinArray{false};
        static constexpr size_t Nest{0};

        template <size_t N>
        using type_n = typename std::conditional_t<N == 0, T, void>;

        using type = type_n<Nest>;
    };

    #if __cplusplus <= 201703L  // c++17
    namespace Inner_ {

    template <typename T, size_t N>
    struct conditional_value_type_n {
        using type =
            typename std::conditional_t<ValueType<T>::Nest != 0,
                                        typename ValueType<typename ValueType<T>::type_direct>::template type_n<N - 1>, T>;
    };

    template <typename T>
    struct conditional_value_type_n<T, 0> {
        using type = T;
    };

    template <typename T, typename = void>
    struct array_or_container : std::false_type {
    };

    template <typename T>
    struct array_or_container<T, typename std::enable_if_t<std::is_array_v<T>>> : std::true_type {
        using type = typename std::remove_extent_t<T>;
    };

    // Tが配列でなく、且つT型インスタンスに範囲for文が適用できるならばstdコンテナと診断する
    template <typename T>
    constexpr bool is_container_v{Nstd::IsRange<T>::value && !std::is_array_v<T>};

    template <typename T>
    struct array_or_container<T, typename std::enable_if_t<is_container_v<T>>> : std::true_type {
        using type = typename T::value_type;
    };

    template <typename T>
    constexpr bool array_or_container_v{array_or_container<T>::value};
    }  // namespace Inner_

    template <typename T>  // ValueTypeの特殊化
    struct ValueType<T, typename std::enable_if_t<Inner_::array_or_container_v<T>>> {
        using type_direct = typename Inner_::array_or_container<T>::type;

        static constexpr bool   IsBuiltinArray{std::is_array_v<T>};
        static constexpr size_t Nest{ValueType<type_direct>::Nest + 1};

        template <size_t N>
        using type_n = typename Inner_::conditional_value_type_n<T, N>::type;

        using type = type_n<Nest>;
    };
    #else  // c++17

    template <typename T, size_t N>
    struct ValueType<T[N]> {  // 配列型の特殊化
        using type_direct = T;

        static constexpr bool   IsBuiltinArray{true};
        static constexpr size_t Nest{ValueType<type_direct>::Nest + 1};

        template <size_t M>
        using type_n = std::conditional_t<M == 0, T[N], typename ValueType<T>::template type_n<M - 1>>;

        using type = type_n<Nest>;
    };

    template <Container T>  // ValueTypeの特殊化
    struct ValueType<T> {   // コンセプトによるSFINAEの回避
        using type_direct = typename T::value_type;

        static constexpr bool   IsBuiltinArray{false};
        static constexpr size_t Nest{ValueType<type_direct>::Nest + 1};

        template <size_t N>
        using type_n = std::conditional_t<N == 0, T, typename ValueType<typename T::value_type>::template type_n<N - 1>>;

        using type = type_n<Nest>;
    };
    #endif

    template <typename T>
    using ValueTypeT = typename ValueType<T>::type;

    template <typename T, size_t N>
    using ValueTypeT_n = typename ValueType<T>::template type_n<N>;
    }  // namespace Nstd
```


## Nstdライブラリの開発2 <a id="SS_4_4"></a>
ここでは予定していた通りSafeArray2を開発し、その後Nstdに必要なライブラリの開発を続ける。


### SafeArray2の開発 <a id="SS_4_4_1"></a>
「[安全な配列型コンテナ](#SS_4_2_3)」で断念したSafeArray2の開発を再開する前に、
SafeArray2の要件をまとめると、

* std::arrayを基底クラスとする
* operator[]に範囲チェックを行う
* SafeArrayでのパラメータパックによる初期化機能はそのまま残す
* SafeArrayではできなかった縮小型変換が起こる初期化にも対応する
* 新規要件として、
  縮小型変換により初期化されたかどうかを示すメンバ関数InitWithNarrowing()を持つ。

となる。この要件を満たすためには、SafeArrayが

```cpp
    //  example/template/safe_vector_ut.cpp 155

    template <typename... ARGS>  // コンストラクタを定義
    SafeArray(ARGS... args) : base_type{args...}
    {
    }
```

で行っていた初期化を、SafeArray2では、
「縮小型変換が起こるか否かによる場合分けを行い、
それぞれの場合に対応するコンストラクタテンプレートによって初期化」
するようにすれば良いことがわかる。

パラメータパックによるコンストラクタのシグネチャは上記した一種類しかないため、
関数のシグネチャの差異よるオーバーロードは使えない。
とすれば、テンプレートパラメータの型の差異によるオーバーロードを使うしか方法がない。
縮小型変換が起こるか否かの場合分けは、
コンセプト[ConvertibleWithoutNarrowing](#SS_4_3_3_4)を使用したSFINAEで実現させることができる。
という風な思考の変遷により以下のコードにたどり着く。


```cpp
    //  example/template/safe_vector_ut.cpp 228
namespace Nstd {

template <typename T, size_t N>
struct SafeArray2 : std::array<T, N> {
    using std::array<T, N>::array;  // 継承コンストラクタ
    using base_type = std::array<T, N>;

    // 縮小型変換した場合には、ill-formedになるコンストラクタ
    /* c++17スタイルのSFINAE
    template <typename... ARGS,
              typename = 
                  typename std::enable_if_t<
                       AreConvertibleWithoutNarrowConvV<T, ARGS...>>>
    */ 
    template <typename... ARGS> // C++20のコンセプトを使用したSFINAE
    requires ConvertibleWithoutNarrowing<T, ARGS...>
    SafeArray2(ARGS... args) : base_type{args...} // 初期化子リストによるarrayの初期化
    {
    }

    // 縮小型変換しない場合には、ill-formedになるコンストラクタ
    /* C++17までのSFINAE
    template <typename... ARGS, 
              typename std::enable_if_t<
                  !AreConvertibleWithoutNarrowConvV<T, ARGS...>>* = nullptr>
    */
    template <typename... ARGS> // C++20のコンセプトを使用したSFINAE
    requires (!ConvertibleWithoutNarrowing<T, ARGS...>)  // この行には()が必要
    SafeArray2(ARGS... args) :
        base_type{T(args)...},  // 縮小型変換を抑止するため、T(args)が必要
        is_with_narrow_conv_{true}
    {
    }

    using size_type = typename base_type::size_type;

    typename base_type::reference       operator[](size_type i) { return this->at(i); }
    typename base_type::const_reference operator[](size_type i) const { return this->at(i); }

    bool InitWithNarrowing() const noexcept { return is_with_narrow_conv_; }

private:
    bool const is_with_narrow_conv_{false};
};
}  // namespace Nstd
```

下記のようなコードでのコンストラクタ呼び出しには、

```cpp
    //  example/template/safe_vector_ut.cpp 299

    auto sa_init = Nstd::SafeArray2<int, 3>{1, 2, 3};
```

上記の抜粋である下記のコンストラクタが置換失敗により排除される(SFINAE)。

```cpp
    //  example/template/safe_vector_ut.cpp 252

    // 縮小型変換しない場合には、ill-formedになるコンストラクタ
    /* C++17までのSFINAE
    template <typename... ARGS, 
              typename std::enable_if_t<
                  !AreConvertibleWithoutNarrowConvV<T, ARGS...>>* = nullptr>
    */
    template <typename... ARGS> // C++20のコンセプトを使用したSFINAE
    requires (!ConvertibleWithoutNarrowing<T, ARGS...>)  // この行には()が必要
    SafeArray2(ARGS... args) :
        base_type{T(args)...},  // 縮小型変換を抑止するため、T(args)が必要
        is_with_narrow_conv_{true}
    {
    }
```

従って、マッチするコンストラクタは

```cpp
    //  example/template/safe_vector_ut.cpp 237

    // 縮小型変換した場合には、ill-formedになるコンストラクタ
    /* c++17スタイルのSFINAE
    template <typename... ARGS,
              typename = 
                  typename std::enable_if_t<
                       AreConvertibleWithoutNarrowConvV<T, ARGS...>>>
    */ 
    template <typename... ARGS> // C++20のコンセプトを使用したSFINAE
    requires ConvertibleWithoutNarrowing<T, ARGS...>
    SafeArray2(ARGS... args) : base_type{args...} // 初期化子リストによるarrayの初期化
    {
    }
```

のみとなり、無事にコンパイルが成功し、下記の単体テストもパスする。

```cpp
    //  example/template/safe_vector_ut.cpp 299

    auto sa_init = Nstd::SafeArray2<int, 3>{1, 2, 3};

    ASSERT_FALSE(sa_init.InitWithNarrowing());  // 縮小型変換なし
    ASSERT_EQ(3, sa_init.size());
    ASSERT_EQ(1, sa_init[0]);
    ASSERT_EQ(2, sa_init[1]);
    ASSERT_EQ(3, sa_init[2]);
    ASSERT_THROW(sa_init[3], std::out_of_range);
```

下記の単体テストの場合、SFINAEにより、先述の例とは逆のコンストラクタが選択され、
コンパイルも単体テストもパスする。

```cpp
    //  example/template/safe_vector_ut.cpp 314
    auto const sa_init = Nstd::SafeArray2<int, 3>{10, 20, 30.0};  // 30.0はintに縮小型変換される

    ASSERT_TRUE(sa_init.InitWithNarrowing());  // 縮小型変換あり
    ASSERT_EQ(3, sa_init.size());
    ASSERT_EQ(10, sa_init[0]);
    ASSERT_EQ(20, sa_init[1]);
    ASSERT_EQ(30, sa_init[2]);
    ASSERT_THROW(sa_init[3], std::out_of_range);
```

ここで紹介したC++17スタイルの2つのコンストラクタテンプレートの最後のパラメータには、
かなりの違和感があるだろうが、
引数や戻り値に制限の多いコンストラクタテンプレートでSFINAEを起こすためには、
このような記述が必要になる。
一方で[コンセプト](#SS_6_11_3)を使用したC++20スタイルのSFINAEの可読性の高さを実感できただろう。

なお、2つ目のコンストラクタテンプレートの中で使用した下記のコードは、
パラメータパックで与えられた全引数をそれぞれにT型オブジェクトに変換するための記法である。

```cpp
    //  example/template/safe_vector_ut.cpp 264

    base_type{T(args)...},  // 縮小型変換を抑止するため、T(args)が必要
```

これにより、std::array\<T, N>のstd::initializer_listによる初期化が縮小変換を検出しなくなる。


### Nstd::SafeIndexの開発 <a id="SS_4_4_2"></a>
「[安全なvector](#SS_4_2_2)」、「[安全な配列型コンテナ](#SS_4_2_3)」等の中で、

* Nstd::SafeVector
* Nstd::SafeString
* Nstd::SafeArray

を定義した。これらは少しだけランタイム速度を犠牲にすることで、
安全な(未定義動作を起こさない)インデックスアクセスを保障するため、
一般のソフトウェア開発にも有用であると思われるが、コードクローンして作ったため、
リファクタリングを行う必要がある。

まずは、Nstd::SafeVectorとNstd::SafeStringの統一を考える。

std::stringは、実際にはstd::basic_string\<char>のエイリアスであることに注目すれば、
Nstd::SafeStringの基底クラスはstd::basic_string\<char>であることがわかる。
この形式は、std::vector\<T>と同形であるため、
Nstd::SafeVectorとNstd::SafeStringの共通コードはテンプレートテンプレートパラメータ
(「[is_same_templ](#SS_4_3_2_7)」参照)を使用し下記のように書ける。


```cpp
    //  example/template/nstd_safe_index.h 8

    namespace Nstd {

    template <template <class...> class C, typename... Ts>
    struct SafeIndex : C<Ts...> {
        using C<Ts...>::C;

        using base_type = C<Ts...>;
        using size_type = typename base_type::size_type;

        typename base_type::reference       operator[](size_type i) { return this->at(i); }
        typename base_type::const_reference operator[](size_type i) const { return this->at(i); }
    };
    }  // namespace Nstd
```

このコードの使用例を兼ねた単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 8

    auto v_i = Nstd::SafeIndex<std::vector, int>{1, 2};

    static_assert(std::is_same_v<int&, decltype(v_i[0])>);
    static_assert(std::is_base_of_v<std::vector<int>, decltype(v_i)>);
    ASSERT_EQ(1, v_i[0]);
    ASSERT_EQ(2, v_i[1]);
    ASSERT_THROW(v_i[2], std::out_of_range);

    auto str = Nstd::SafeIndex<std::basic_string, char>{"123"};

    static_assert(std::is_same_v<char&, decltype(str[0])>);
    static_assert(std::is_base_of_v<std::string, decltype(str)>);
    ASSERT_EQ(3, str.size());
    ASSERT_EQ("123", str);
    ASSERT_THROW(str[3], std::out_of_range);
```

このままでは使いづらいので下記のようにエイリアスを使い、元のテンプレートと同じ名前を与える。

```cpp
    //  example/template/nstd_safe_index.h 24

    namespace Nstd {

    template <typename T>
    using SafeVector = Nstd::SafeIndex<std::vector, T>;

    using SafeString = Nstd::SafeIndex<std::basic_string, char>;
    }  // namespace Nstd
```

このコードの単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 54

    auto v_i = Nstd::SafeVector<int>{1, 2};

    static_assert(std::is_same_v<int&, decltype(v_i[0])>);
    static_assert(std::is_base_of_v<std::vector<int>, decltype(v_i)>);
    ASSERT_EQ(1, v_i[0]);
    ASSERT_EQ(2, v_i[1]);
    ASSERT_THROW(v_i[2], std::out_of_range);

    auto str = Nstd::SafeString{"123"};

    static_assert(std::is_same_v<char&, decltype(str[0])>);
    static_assert(std::is_base_of_v<std::string, decltype(str)>);
    ASSERT_EQ(3, str.size());
    ASSERT_EQ("123", str);
    ASSERT_THROW(str[3], std::out_of_range);
```

これで、Nstd::SafeVectorとNstd::SafeStringは統一できたので、
Nstd::SafeIndexにNstd::SafeArrayの実装が取り込めれば、リファクタリングは終了となるが、
残念ながら、下記のコードはコンパイルできない。

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 44

    // 下記のように書きたいが、パラメータパックは型と値を混在できないのでコンパイルエラー
    auto a_i = Nstd::SafeIndex<std::array, int, 5>{};
```

理由は、パラメータパックにはそのすべてに型を指定するか、そのすべてに値を指定しなければならず、
上記のコードのような型と値の混在が許されていないからである。

値を型に変換する[std::integral_constant](#SS_7_2_1)を使用し、この問題を解決できる。
std::arrayから派生した下記のStdArrayLikeは、std::integral_constant::valueから値を取り出し、
基底クラスstd::arrayの第2テンプレートパラメータとする。
この仕組みにより、StdArrayLikeは、
Nstd::SafeIndexのテンプレートテンプレートパラメータとして使用できるようになる。

```cpp
    //  example/template/nstd_safe_index.h 34

    namespace Nstd {
    namespace Inner_ {

    template <typename T, typename U>
    struct std_array_like : std::array<T, U::value> {
        using std::array<T, U::value>::array;

        template <typename... ARGS>
        std_array_like(ARGS... args) noexcept(std::is_nothrow_constructible_v<T, ARGS...>)
            : std::array<T, U::value>{args...}
        {
            static_assert(ConvertibleToAll<T, ARGS...>, "arguemnt error");
        }
    };
    }  // namespace Inner_
    }  // namespace Nstd
```

まずは、このコードの使用例を兼ねた単体テストを下記に示す。

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 134

    auto sal = Nstd::Inner_::std_array_like<int, std::integral_constant<size_t, 3>>{1, 2, 3};

    static_assert(std::is_nothrow_constructible_v<decltype(sal), int>);  // エクセプション無し生成
    static_assert(std::is_same_v<int&, decltype(sal[0])>);
    static_assert(std::is_base_of_v<std::array<int, 3>, decltype(sal)>);
    ASSERT_EQ(1, sal[0]);
    ASSERT_EQ(2, sal[1]);
    ASSERT_EQ(3, sal[2]);

    using T   = Nstd::Inner_::std_array_like<std::string, std::integral_constant<size_t, 3>>;
    auto sal2 = T{"1", "2", "3"};

    static_assert(!std::is_nothrow_constructible_v<std::string, char const*>);
    static_assert(!std::is_nothrow_constructible_v<T, char const*>);  // エクセプション有り生成
    static_assert(std::is_same_v<std::string&, decltype(sal2[0])>);
    static_assert(std::is_base_of_v<std::array<std::string, 3>, decltype(sal2)>);
    ASSERT_EQ("1", sal2[0]);
    ASSERT_EQ("2", sal2[1]);
    ASSERT_EQ("3", sal2[2]);
```

これを使えば、下記のような記述が可能となる。

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 157

    using T2   = Nstd::SafeIndex<Nstd::Inner_::std_array_like, std::string, std::integral_constant<size_t, 4>>;
    auto sal_s = T2{"1", "2", "3"};

    static_assert(!std::is_nothrow_constructible_v<T2, char const*>);  // エクセプション有り生成
    static_assert(std::is_same_v<std::string&, decltype(sal_s[0])>);
    static_assert(std::is_base_of_v<std::array<std::string, 4>, decltype(sal_s)>);
    ASSERT_EQ("1", sal_s[0]);
    ASSERT_EQ("2", sal_s[1]);
    ASSERT_EQ("3", sal_s[2]);
    ASSERT_EQ("", sal_s[3]);
    ASSERT_THROW(sal_s[4], std::out_of_range);
```

このままでは使いづらいのでNstd::SafeVector、Nstd::Stringと同様にエイリアスを使えば、
下記のようになる。

```cpp
    //  example/template/nstd_safe_index.h 53

    namespace Nstd {

    template <typename T, size_t N>
    using SafeArray = Nstd::SafeIndex<Nstd::Inner_::std_array_like, T, std::integral_constant<size_t, N>>;
    }  // namespace Nstd
```

このコードの単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 89

    auto sal_s = Nstd::SafeArray<std::string, 4>{"1", "2", "3"};

    static_assert(std::is_same_v<std::string&, decltype(sal_s[0])>);
    static_assert(std::is_base_of_v<std::array<std::string, 4>, decltype(sal_s)>);
    ASSERT_EQ("1", sal_s[0]);
    ASSERT_EQ("2", sal_s[1]);
    ASSERT_EQ("3", sal_s[2]);
    ASSERT_EQ("", sal_s[3]);
    ASSERT_THROW(sal_s[4], std::out_of_range);
```

これにより、当初の目的であったコードクローンの除去が完了した。
この効果により、下記に示したような拡張もコードクローンせずに簡単に行えるようになった。

```cpp
    //  example/template/nstd_safe_index.h 61

    namespace Nstd {

    using SafeStringU16 = Nstd::SafeIndex<std::basic_string, char16_t>;
    using SafeStringU32 = Nstd::SafeIndex<std::basic_string, char32_t>;
    }  // namespace Nstd
```

```cpp
    //  example/template_cpp17/nstd_safe_index_ut.cpp 112

    auto u16str = Nstd::SafeStringU16{u"あいうえお"};

    static_assert(std::is_same_v<char16_t&, decltype(u16str[0])>);
    static_assert(std::is_base_of_v<std::u16string, decltype(u16str)>);
    ASSERT_EQ(5, u16str.size());
    ASSERT_EQ(u"あいうえお", u16str);
    ASSERT_THROW(u16str[5], std::out_of_range);

    auto u32str = Nstd::SafeStringU32{U"かきくけこ"};

    static_assert(std::is_same_v<char32_t&, decltype(u32str[0])>);
    static_assert(std::is_base_of_v<std::u32string, decltype(u32str)>);
    ASSERT_EQ(5, u32str.size());
    ASSERT_EQ(U"かきくけこ", u32str);
    ASSERT_THROW(u32str[5], std::out_of_range);
```

### Nstd::SafeIndexのoperator\<\<の開発 <a id="SS_4_4_3"></a>
ここでは、Nstd::SafeIndexのoperator\<\<の開発を行う。

他のoperator\<\<との間で定義が曖昧にならないようにするためには、
テンプレートテンプレートパラメータを使って以下のようにすることが考えられる。

```cpp
    //  example/template_cpp17/safe_index_put_to_ut.cpp 8

    template <template <class...> class C, typename... Ts>
    std::ostream& operator<<(std::ostream& os, Nstd::SafeIndex<C, Ts...> const& safe_index)
    {
        auto sep = "";

        for (auto const& i : safe_index) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
```

以下の単体テストで動作確認する。

```cpp
    //  example/template_cpp17/safe_index_put_to_ut.cpp 25
    {
        auto v_i = Nstd::SafeVector<int>{1, 2};

        auto oss = std::ostringstream{};
        oss << v_i;
        ASSERT_EQ("1, 2", oss.str());
    }
    {
        auto sal_s = Nstd::SafeArray<std::string, 4>{"1", "2", "3"};
        auto oss   = std::ostringstream{};
        oss << sal_s;
        ASSERT_EQ("1, 2, 3, ", oss.str());  // 4番目には何も入っていない
    }
```

ここまではうまく行っているが、以下の単体テストによりバグが発覚する。

```cpp
    //  example/template_cpp17/safe_index_put_to_ut.cpp 40

    {
        auto s_str = Nstd::SafeString{"hello"};
        auto oss   = std::ostringstream{};
        oss << s_str;

        // ASSERT_EQ("hello", oss.s_str());     // これがパス出来たらよいが、
        ASSERT_EQ("h, e, l, l, o", oss.str());  // 実際にはこのようになる。
    }
    {
        auto str = std::string{"hello"};  // 上記と比較のためのstd::stringでのoperator<<

        auto oss = std::ostringstream{};
        oss << str;
        ASSERT_EQ("hello", oss.str());
    }
```

この原因は、Nstd::SafeStringオブジェクトに対して、std::operator<<が使用されなかったからである。

「[メタ関数のテクニック](#SS_4_3)」で紹介したSFINAEによりこの問題を回避できるが、
ここでも、すでにみてきた[コンセプト](#SS_6_11_3)による制約によりこの問題に対処する。

```cpp
    //  example/template_cpp17/safe_index_put_to_ut.cpp 98


    #if __cplusplus >= 202002L  // c++20
    namespace Inner_ {
    template <typename T>
    concept not_safe_string = !std::is_same_v<T, Nstd::SafeString>;
    }
    #endif

    template <template <class...> class C, typename... Ts>
    #if __cplusplus >= 202002L  // c++20
    auto operator<<(std::ostream& os, Nstd::SafeIndex<C, Ts...> const& safe_index) -> std::ostream& 
        requires Inner_::not_safe_string<Nstd::SafeIndex<C, Ts...>> // enable_ifによるSFINAEを避け、

    #else  // c++17
    auto operator<<(std::ostream& os, Nstd::SafeIndex<C, Ts...> const& safe_index) ->
        typename std::enable_if_t<    // safe_indexがSafeString型ならば、SFINAEにより非活性化
            !std::is_same_v<Nstd::SafeIndex<C, Ts...>, Nstd::SafeString>, std::ostream&>
    #endif
    {  // コンセプトによる制約
        auto sep = "";

        for (auto const& i : safe_index) {
            os << std::exchange(sep, ", ") << i;
        }

        return os;
    }
```

これにより先ほど問題が発生した単体テストも下記のようにパスする。

```cpp
    //  example/template_cpp17/safe_index_put_to_ut.cpp 145

    auto str = Nstd::SafeString{"hello"};
    auto oss = std::ostringstream{};
    oss << str;
    ASSERT_EQ("hello", oss.str());  // std::operator<<が使われる
    // ASSERT_EQ("h, e, l, l, o", oss.str());
```


### コンテナ用Nstd::operator\<\<の開発 <a id="SS_4_4_4"></a>
「[Nstd::SafeIndexのoperator\<\<の開発](#SS_4_4_3)」で定義したNstd::operator\<\<の構造は、
範囲for文に適用できる配列やstdコンテナにも使えるため、ここではその拡張を考える。

すでに述べたように注意すべきは、

* 使い勝手の良いstd::operator\<\<(例えばchar[N]やstd::stringのoperator\<\<)はそのまま使う
* ほとんど使い物にならないstd::operator\<\<(例えば、int[N]のような配列に対するoperator\<\<(void\*))
  の代わりに、ここで拡張するNstd::operator\<\<を使う

であるため、型Tが新しいNstd::operator\<\<を使用できる条件は、

* Tの型が、以下の条件を満たす
    * T == U[N]であった場合、Uはcharではない
    * std::stringおよびその派生型ではない
* Nstd::ValueType\<T>::typeがoperator\<\<を持つ

となるだろう。この条件を診断するためのメタ関数は以下のようになる。

```cpp
    //  example/template/nstd_put_to.h 17

    namespace Nstd {
    namespace Inner_ {

    template <typename T>  // Nstd::Printableを使用するとg++のバグで、問題が発生するため、
                           // バグ回避のため敢えてここでNstd::Inner_::Printableを宣言する
    concept Printable = requires(T t, std::ostream& os)
    {
        { os << t } -> std::same_as<std::ostream&>;
    };

    template <typename T>
    constexpr bool enable_range_put_to() noexcept
    {
        if constexpr (Nstd::ValueType<T>::IsBuiltinArray) {  // Tは配列
            if constexpr (std::is_same_v<char,
                                         typename Nstd::ValueType<T>::type_direct>) {  // Tはchar配列
                return false;
            }
            else {
                return Nstd::Printable<typename Nstd::ValueTypeT<T>>;
            }
        }
        else {  // Tは配列ではない
            if constexpr (Printable<T>) {
                return false;
            }
            else {
                if constexpr (Nstd::IsRangeV<T>) {  // 範囲for文に適用できる
                    return Nstd::Printable<typename Nstd::ValueTypeT<T>>;
                }
                else {
                    return false;
                }
            }
        }
    }

    template <typename T>
    constexpr bool enable_range_put_to_v{enable_range_put_to<T>()};
    }  // namespace Inner_
    }  // namespace Nstd
```

ただし、このようなコードはコンパイラのバグによりコンパイルできないことがある。
実際、現在使用中の[g++](#SS_8_13_1)ではこのコードはコンパイルできず、
上記コードでコメントにも書いた通り、Inner_の中でPrintableを再定義することで、
そのワークアラウンドを行っている。

このような場合、条件分岐に三項演算子や中間式にconstexprを使うことで回避できることが多い。
このような複雑なメタ関数には単体テストは必須である。

```cpp
    //  example/template/test_class.h 3

    class test_class_exits_put_to {
    public:
        test_class_exits_put_to(int i = 0) noexcept : i_{i} {}
        int get() const noexcept { return i_; }

    private:
        int i_;
    };

    inline std::ostream& operator<<(std::ostream& os, test_class_exits_put_to const& p) { return os << p.get(); }

    class test_class_not_exits_put_to {};
```

```cpp
    //  example/template/nstd_put_to_ut.cpp 31

    static_assert(enable_range_put_to_v<int[3]>);                         // Nstd::operator<<
    static_assert(!enable_range_put_to_v<char[3]>);                       // std::operator<<
    static_assert(!enable_range_put_to_v<int>);                           // std::operator<<
    static_assert(enable_range_put_to_v<std::vector<int>>);               // Nstd::operator<<
    static_assert(enable_range_put_to_v<std::vector<std::vector<int>>>);  // Nstd::operator<<
    static_assert(!enable_range_put_to_v<std::string>);                   // std::operator<<
    static_assert(enable_range_put_to_v<std::vector<std::string>>);       // Nstd::operator<<

    static_assert(!enable_range_put_to_v<test_class_not_exits_put_to>);               // operator<<無し
    static_assert(!enable_range_put_to_v<test_class_exits_put_to>);                   // ユーザ定義operator<<
    static_assert(!enable_range_put_to_v<std::vector<test_class_not_exits_put_to>>);  // operator<<無し
    static_assert(enable_range_put_to_v<std::vector<test_class_exits_put_to>>);       // Nstd::operator<<
    static_assert(!enable_range_put_to_v<std::list<test_class_not_exits_put_to>>);    // operator<<無し
    static_assert(enable_range_put_to_v<std::list<test_class_exits_put_to>>);         // Nstd::operator<<
```

以上によりstd::enable_ifの第1引数に渡す値(enable_range_put_to_vはconstexpr)が用意できたので、
Nstd::operator\<\<は下記のように定義できる。

```cpp
    //  example/template/nstd_put_to.h 64

    namespace Nstd {
    namespace Inner_ {

    template <size_t N>
    constexpr std::string_view range_put_to_sep() noexcept
    {
        static_assert(N != 0);
        switch (N) {
        case 1:
            return ", ";
        case 2:
            return " | ";
        case 3:
        default:
            return " # ";
        }
    };

    template <typename T>
    concept range_put_to = Inner_::enable_range_put_to_v<T>;
    }  // namespace Inner_

    template <typename T>
    auto operator<<(std::ostream& os, T const& t) ->
        typename std::enable_if_t<Inner_::enable_range_put_to_v<T>, std::ostream&>
    // std::enable_if_t<Inner_::enable_range_put_to_v<T>を使わずに上のrange_put_toを使いたいが、
    // コンパイラのバグによりコンパイルできない
    {
        auto sep = std::string_view("");
        auto s   = Inner_::range_put_to_sep<ValueType<T>::Nest>();

        for (auto const& i : t) {
            os << std::exchange(sep, s) << i;
        }

        return os;
    }
    }  // namespace Nstd
```

値表示用のセパレータに","のみを用いるとコンテナや配列が多次元(ValueType::Nest > 2)の場合、
各次元でのデータの判別が難しくなるため、ValueType::Nestの値によってセパレータの種類を変える
range_put_to_sep<>()を用意した。
下記単体テストでわかる通り、この効果により値の構造が見やすくなっている。

まずは、配列の単体テストを示す。

```cpp
    //  example/template/nstd_put_to_ut.cpp 111

    using namespace Nstd;
    {
        char str[] = "abcdef";
        auto oss   = std::ostringstream{};

        oss << str;  // std::operator<<
        ASSERT_EQ(str, oss.str());
    }
    {
        char str[2][4] = {"abc", "def"};
        auto oss       = std::ostringstream{};

        oss << str;  // Nstd::operator<<
        ASSERT_EQ("abc | def", oss.str());
    }
    {
        test_class_exits_put_to p1[3]{1, 2, 3};
        auto                    oss = std::ostringstream{};

        oss << p1;  // Nstd::operator<<
        ASSERT_EQ("1, 2, 3", oss.str());
    }
    {
        char const* str[] = {"abc", "def", "ghi"};
        auto        oss   = std::ostringstream{};

        oss << str;  // Nstd::operator<<
        ASSERT_EQ("abc, def, ghi", oss.str());
    }
    {
        int  v[2][3][2]{{{0, 1}, {2, 3}, {4, 5}}, {{6, 7}, {8, 9}, {10, 11}}};
        auto oss = std::ostringstream{};

        oss << v;
        ASSERT_EQ("0, 1 | 2, 3 | 4, 5 # 6, 7 | 8, 9 | 10, 11", oss.str());
    }
```

次に、コンテナの単体テストを示す。

```cpp
    //  example/template/nstd_put_to_ut.cpp 168

    using namespace Nstd;
    {
        auto v   = std::vector<int>{1, 2, 3};
        auto oss = std::ostringstream{};

        oss << v;
        ASSERT_EQ("1, 2, 3", oss.str());
    }
    {
        auto p1  = std::list<test_class_exits_put_to>{1, 2, 3, 4};
        auto oss = std::ostringstream{};

        oss << p1;
        ASSERT_EQ("1, 2, 3, 4", oss.str());
    }
    {
        std::vector<int> v[2]{{1, 2}, {3, 4, 5}};  // std::vectorの配列
        auto             oss = std::ostringstream{};

        oss << v;
        ASSERT_EQ("1, 2 | 3, 4, 5", oss.str());
    }
```

最後に、Nstd::SafeIndexの単体テストを示す。

```cpp
    //  example/template/nstd_put_to_ut.cpp 218

    {
        auto sal_s = Nstd::SafeArray<std::string, 4>{"1", "2", "3"};
        auto oss   = std::ostringstream{};

        oss << sal_s;
        ASSERT_EQ("1 | 2 | 3 | ", oss.str());
    }
    {
        auto sv  = Nstd::SafeVector<Nstd::SafeArray<Nstd::SafeString, 2>>{{"ab", "cd"}, {"ef", "gh"}};
        auto oss = std::ostringstream{};

        oss << sv;
        ASSERT_EQ("ab | cd # ef | gh", oss.str());
    }
```

## Nstdライブラリの開発3(浮動小数点関連) <a id="SS_4_5"></a>
[浮動小数点型](#SS_6_1_12)を頻繁に使用するソフトウェアの開発を行うに場合、
ソースコードの中で、場当たり的に浮動小数点型を使用すると、
[浮動小数点の誤差](#SS_6_1_12_2)や[浮動小数点の演算エラー](#SS_6_1_12_4)
にまつわるバグの修正に多くの工数をロスしてしまうことになる。

これらの課題に対処するため、この節は浮動小数点演算によるバグを未然に防ぎ、
精度を確保するための機能を提供することを目的としている。
[浮動小数点の比較](#SS_4_5_1)方法や、
浮動小数点を避けて高精度な演算を実現する[固定小数点クラス](#SS_4_5_2)および[有理数クラス](#SS_4_5_4)を導入し、
さらにそれらを簡単に使用できるリテラル表記もサポートしている。

### 浮動小数点の比較 <a id="SS_4_5_1"></a>
浮動小数点の演算には下記に示したような問題が起こり得るため、単純な==の比較はできない。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 9

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    ASSERT_FALSE(0.05F == a + b);  // a + b == 0.05Fは一般には成立しない。
```

この問題に対処するのが以下のコードである。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 17

    float epsilon  = std::abs(0.05F - (a + b));
    bool  is_equal = epsilon <= std::numeric_limits<float>::epsilon();
    ASSERT_TRUE(is_equal);
```

単なる浮動小数変数の比較にこのようなコードを書くのは間違えやすいし、非効率であるため、
下記のような関数(float用とdouble用)で対処することが一般的である。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 25

    namespace Nstd {

    /// @brief float比較用関数
    bool is_equal_f(float lhs, float rhs) noexcept { return std::abs(lhs - rhs) <= std::numeric_limits<float>::epsilon(); }

    /// @brief double比較用関数
    bool is_equal_d(double lhs, double rhs) noexcept
    {
        return std::abs(lhs - rhs) <= std::numeric_limits<double>::epsilon();
    }
```
実際に使う場面を以下に示す。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 41

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    // floatの比較はis_equal_fのような関数を使う。
    bool is_equal = Nstd::is_equal_f(0.05F, a + b);
    ASSERT_TRUE(is_equal);
```

一見これで万事うまくいくように見えるが、そうは行かないことを以下の例で示す。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 56

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    // a + bはfloatの精度のまま、is_equal_dの引数の型であるdoubleに昇格される。
    // 一方、0.05はdoubleであるため(循環小数をdoubleの精度で切り捨てた値であるため)、
    // a + b(floatの精度の値)と0.05の差はdoubleのepsilonを超える。
    //  ASSERT_TRUE(is_equal_d(0.05, a + b));  // NG
    ASSERT_FALSE(Nstd::is_equal_d(0.05, a + b));
```

dobuleとfloatを1つの式に混載するとfloatがdoubleに昇格されるため、このような問題が起こり得る。
これに対処する方法を以下に示す。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 71

    namespace Nstd {
    // is_equal_dを改良して、引数の型が統一されていない呼び出しをコンパイルエラーにできるようにした。
    /// @brief 浮動小数点比較用関数
    template <typename FLOAT_0, typename FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        static_assert(std::is_floating_point_v<FLOAT_0>);
        static_assert(std::is_same_v<FLOAT_0, FLOAT_1>);

        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }
    }  // namespace Nstd
```

この関数のテストは以下の通りである。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 88

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    // a + bはfloatであり、0.05はdoubleであるため、下記コードはコンパイルできない。
    // ASSERT_TRUE(Nstd::is_equal(0.05, a + b));
    ASSERT_TRUE(Nstd::is_equal(0.05F, a + b));  // OK リテラルに型を指定して、引数の型を統一
```

通常の浮動小数の比較は相対誤差を指定できる必要性がある場合が多いため、
さらに下記のように拡張変更した。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 103

    /// @brief 浮動小数点比較用関数
    /// 相対誤差を考慮して、lhs と rhs の絶対値に基づくトレランスの範囲内での比較を行う。
    /// これにより、数値の大小に関わらず、適切な誤差で比較できる。
    template <typename FLOAT_0, typename FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs, FLOAT_0 tolerance = std::numeric_limits<FLOAT_0>::epsilon()) noexcept
    {
        static_assert(std::is_floating_point_v<FLOAT_0>);
        static_assert(std::is_same_v<FLOAT_0, FLOAT_1>);

        return std::abs(lhs - rhs) <= tolerance * std::max(std::abs(lhs), std::abs(rhs));
    }
```

この関数のテストは以下の通りである。

```cpp
    //  example/template_cpp17/nstd_float_ut.cpp 121

    float a = 1000000.0F;
    float b = 1000000.1F;

    ASSERT_FALSE(Nstd::is_equal(a, b));       // a, bはほぼ同じだが。
    ASSERT_TRUE(Nstd::is_equal(a, b, 0.1F));  // 相対誤差を指定できる。
```

### 固定小数点クラス <a id="SS_4_5_2"></a>
以上で見てきたように浮動小数点の扱いはやや面倒であるため、
浮動小数点のダイナミックレンジが必要な場合以外では安易に浮動小数点を使うべきでない。

従って、intやlong等のダイナミックレンジで表現できる1未満の値が必要な場合、
intやlongの値を100倍などのスケーリングして使うのが、浮動小数点の微妙な問題を避ける手段となる。
スケーリングとは、
整数型変数変数のスケーリングとは、intやlongの値を、
特定の倍率で拡大することで小数点以下の値を扱う方法を指す。
例えば、100倍にスケーリングして「1.23」を「123」として整数で表現するようする。
この方法は浮動小数点の代わりに使えるが、
スケーリング値を常に意識する必要があり、コードの可読性や保守性に影響を与える問題がある。

以下に示す固定小数点クラス(FixedPoint)はこれらの問題を解決できる。

```cpp
    //  example/template_cpp17/fixed_point.h 7

    namespace Nstd {
    /// @brief BASIC_TYPEで指定する基本型のビット長を持つ固定小数点を扱うためのクラス
    /// @tparam BASIC_TYPE       全体のビット長や、符号を指定するための整数型
    /// @tparam FRACTION_BIT_NUM 小数点保持のためのビット長
    template <typename BASIC_TYPE, uint32_t FRACTION_BIT_NUM>
    class FixedPoint {
    public:
        constexpr FixedPoint(BASIC_TYPE integer = 0, typename std::make_unsigned_t<BASIC_TYPE> fraction = 0) noexcept
            : value_{get_init_value(integer, fraction)}
        {
            // signedに対する右ビットシフトの仕様が、算術右ビットシフトでないと
            // このクラスは成立しない。下記のstatic_assertはその確認。
            static_assert(IsSigned() ? (-1 >> 1 == -1) : true, "need logical right bit sift");

            // BASIC_TYPEをcharにすることは認めない。
            static_assert(!std::is_same_v<BASIC_TYPE, char>, "BASIC_TYPE should not be char");
        }

        // 以下、特殊メンバ定義
        ~FixedPoint()                                = default;
        FixedPoint(FixedPoint const&)                = default;
        FixedPoint& operator=(FixedPoint const&)     = default;
        FixedPoint(FixedPoint&&) noexcept            = default;
        FixedPoint& operator=(FixedPoint&&) noexcept = default;

        // 以下、インターフェース定義
        constexpr BASIC_TYPE GetValue() const noexcept { return value_; }
        constexpr BASIC_TYPE GetInteger() const noexcept { return value_ >> fraction_bit_num_; }
        constexpr BASIC_TYPE GetFraction() const noexcept { return value_ & fraction_bit_mask_; }

        /// @brief doubleに変換する
        constexpr double ToFloatPoint() const noexcept
        {
            return GetInteger() + (static_cast<double>(GetFraction()) / (fraction_bit_mask_ + 1));
        }

        /// @brief 小数部のビット長を返す
        constexpr typename std::make_unsigned_t<BASIC_TYPE> GetFractionMask() const noexcept { return fraction_bit_mask_; }

        /// @brief 整数部のビット長を返す
        constexpr typename std::make_unsigned_t<BASIC_TYPE> GetIntegerMask() const noexcept { return integer_bit_mask_; }

        static constexpr bool IsSigned() noexcept { return std::is_signed_v<BASIC_TYPE>; }

        static constexpr bool IsUnsigned() noexcept { return std::is_unsigned_v<BASIC_TYPE>; }

        /// @brief    以下operator @=の定義
        FixedPoint& operator+=(FixedPoint rhs) noexcept
        {
            value_ += rhs.value_;
            return *this;
        }

        FixedPoint& operator-=(FixedPoint rhs) noexcept
        {
            value_ -= rhs.value_;
            return *this;
        }

        FixedPoint& operator*=(FixedPoint rhs) noexcept
        {
            value_ *= rhs.value_ >> fraction_bit_num_;
            return *this;
        }

        FixedPoint& operator/=(FixedPoint rhs) noexcept
        {
            using T = std::conditional_t<IsSigned(), int64_t, uint64_t>;

            value_ = (static_cast<T>(value_) << fraction_bit_num_) / rhs.value_;

            return *this;
        }

    private:
        BASIC_TYPE value_;  // FixedPointの実際の値

        static constexpr uint32_t bit_mask(uint32_t bit_len) noexcept
        {
            if (bit_len == 0) {
                return 0x0;
            }

            return bit_mask(bit_len - 1) | (0x01 << (bit_len - 1));
        }

        static constexpr uint32_t fraction_bit_num_{FRACTION_BIT_NUM};
        static constexpr uint32_t fraction_bit_mask_{bit_mask(fraction_bit_num_)};
        static constexpr uint32_t integer_bit_num_{sizeof(BASIC_TYPE) * 8 - FRACTION_BIT_NUM};
        static constexpr uint32_t integer_bit_mask_{bit_mask(integer_bit_num_) << fraction_bit_num_};

        static constexpr BASIC_TYPE get_init_value(BASIC_TYPE integer, BASIC_TYPE fraction) noexcept
        {
            // 本来は左シフト<<を使いたいが、signedに対しての<<ランタイム実装依存であるので、
            // return (integer << fraction_bit_num_) | fraction;

            return (integer * (fraction_bit_mask_ + 1)) | fraction;
        }

        /// 以下比較演算子の定義

    #if __cplusplus >= 202002L  // c++20
        friend auto operator<=>(FixedPoint lhs, FixedPoint rhs) noexcept = default;

    #else  // c++17
        friend bool operator==(FixedPoint lhs, FixedPoint rhs) noexcept { return lhs.value_ == rhs.value_; }

        friend bool operator!=(FixedPoint lhs, FixedPoint rhs) noexcept { return !(lhs == rhs); }

        friend bool operator>(FixedPoint lhs, FixedPoint rhs) noexcept { return lhs.value_ > rhs.value_; }

        friend bool operator>=(FixedPoint lhs, FixedPoint rhs) noexcept { return (lhs > rhs) || (lhs == rhs); }

        friend bool operator<(FixedPoint lhs, FixedPoint rhs) noexcept { return (rhs > lhs); }

        friend bool operator<=(FixedPoint lhs, FixedPoint rhs) noexcept { return (lhs < rhs) || (lhs == rhs); }
    #endif

        /// @brief FixedPoint() + intのようなオーバーロードを作るためにあえてfriend
        friend FixedPoint operator+(FixedPoint lhs, FixedPoint rhs) noexcept
        {
            lhs += rhs;
            return lhs;
        }

        friend FixedPoint operator-(FixedPoint lhs, FixedPoint rhs) noexcept
        {
            lhs -= rhs;
            return lhs;
        }

        friend FixedPoint operator*(FixedPoint lhs, FixedPoint rhs) noexcept
        {
            lhs *= rhs;
            return lhs;
        }

        friend FixedPoint operator/(FixedPoint lhs, FixedPoint rhs) noexcept
        {
            lhs /= rhs;
            return lhs;
        }
    };
```

FixedPointの単体テストコードを以下に示す。

```cpp
    //  example/template_cpp17/fixed_point_ut.cpp 21

    // 以下は、FixedPoint<>の使用例である。
    using FP4 = Nstd::FixedPoint<uint8_t, 4>;  // 基本型uint8_t、小数点4ビット
    auto fp0  = FP4{};

    ASSERT_FALSE(fp0.IsSigned());
    ASSERT_TRUE(fp0.IsUnsigned());

    fp0 = 7;    ASSERT_EQ(7, fp0);
    fp0 = 7;    ASSERT_NE(6, fp0);
    fp0 += 2;   ASSERT_EQ(FP4{9}, fp0);         
                ASSERT_DOUBLE_EQ(9.0, fp0.ToFloatPoint());
    fp0 /= 2;   ASSERT_EQ((FP4{4, 8}), fp0);    
                ASSERT_DOUBLE_EQ(4.5, fp0.ToFloatPoint());
    fp0 /= 2;   ASSERT_EQ((FP4{2, 4}), fp0);    
                ASSERT_DOUBLE_EQ(2.25, fp0.ToFloatPoint());
    fp0 *= 4;   ASSERT_EQ(FP4{9}, fp0);
    fp0 += 7;   ASSERT_EQ(FP4{0}, fp0);
```

### 固定小数点リテラル <a id="SS_4_5_3"></a>
[固定小数点クラス](#SS_4_5_2)のようなクラス定義には、以下に示すようにユーザ定義リテラルを定義し、
使い勝手のよい環境をユーザに提供するべきである。

```cpp
    //  example/template_cpp17/fixed_point.h 156

    namespace Nstd {
    namespace fixed_point_literals {
    // FixedPoint<int32_t, 8> 用のユーザ定義リテラル
    FixedPoint<int32_t, 8> operator"" _fxp(unsigned long long int val)
    {
        // 整数部分を取り、FixedPoint<int32_t, 8>のインスタンスを作成
        return FixedPoint<int32_t, 8>(static_cast<int32_t>(val));
    }

    FixedPoint<int32_t, 8> operator"" _fxp(long double val)
    {
        // 浮動小数点数からFixedPoint<int32_t, 8>のインスタンスを作成
        int32_t integer_part  = static_cast<int32_t>(val);
        int32_t fraction_part = static_cast<int32_t>((val - integer_part) * 256);  // 2^8 = 256
        return FixedPoint<int32_t, 8>(integer_part, fraction_part);
    }
    }  // namespace fixed_point_literals
    }  // namespace Nstd
```

以上のコードの単体テストを以下に示す。これにより使用方も明らかになるだろう。

```cpp
    //  example/template_cpp17/fixed_point_ut.cpp 171

    using namespace Nstd::fixed_point_literals;

    auto a = 123_fxp;  // 整数リテラル

    EXPECT_EQ(a.GetInteger(), 123);
    EXPECT_EQ(a.GetFraction(), 0);  // 小数部は0のはず

    auto b      = 50.25_fxp;
    auto result = a + b;

    EXPECT_NEAR(result.ToFloatPoint(), 173.25, 0.01);
```

### 有理数クラス <a id="SS_4_5_4"></a>
[固定小数点クラス](#SS_4_5_2)では精度が足りず、浮動小数点を使用したくない場合、
以下のコードで示す有理数クラスがちょうどよい選択となることがある。

```cpp
    //  example/template_cpp17/rational.h 10

    namespace Nstd {
    /// @brief ユーザー指定の型で分数を扱うためのクラス
    /// @tparam T 基本の整数型（デフォルトはint32_t）
    #if __cplusplus >= 202002L  // c++20
    template <std::signed_integral T = int32_t>
    #else  // c++17
    template <typename T = int32_t>
    #endif
    class Rational {
    public:
        using underlying_type_t = T;
        /// @brief コンストラクタ
        /// @param num 分子
        /// @param deno 分母
        constexpr Rational(T num, T deno = 1) : value_{reduce(num, deno)} {}
        T getNumerator() const noexcept { return value_.num; }
        T getDenominator() const noexcept { return value_.deno; }
        /// @brief 2項演算子(四則演算)の定義
        Rational operator+(const Rational& rhs) const noexcept
        {
            T num  = value_.num * rhs.value_.deno + rhs.value_.num * value_.deno;
            T deno = value_.deno * rhs.value_.deno;
            return Rational{num, deno};
        }
        Rational operator-(const Rational& rhs) const noexcept
        {
            T num  = value_.num * rhs.value_.deno - rhs.value_.num * value_.deno;
            T deno = value_.deno * rhs.value_.deno;
            return Rational{num, deno};
        }
        Rational operator*(const Rational& rhs) const noexcept
        {
            return Rational{value_.num * rhs.value_.num, value_.deno * rhs.value_.deno};
        }
        Rational operator/(const Rational& rhs) const noexcept
        {
            return Rational(value_.num * rhs.value_.deno, value_.deno * rhs.value_.num);
        }
        /// @brief 複合代入演算子(四則演算)の定義
        Rational& operator+=(Rational const& rhs)
        {
            *this = *this + rhs;
            return *this;
        }
        Rational& operator-=(Rational const& rhs)
        {
            *this = *this - rhs;
            return *this;
        }
        Rational& operator*=(Rational const& rhs)
        {
            *this = *this * rhs;
            return *this;
        }
        Rational& operator/=(Rational const& rhs)
        {
            *this = *this / rhs;
            return *this;
        }
        /// @brief 単項演算子の定義
        constexpr Rational operator+() const noexcept { return *this; }
        constexpr Rational operator-() const noexcept { return Rational{-value_.num, value_.deno}; }
        /// @brief 比較演算子の定義
    #if __cplusplus >= 202002L  // c++20
        friend bool operator==(Rational const& lhs, Rational const& rhs) noexcept = default;
        friend auto operator<=>(Rational const& lhs, Rational const& rhs) noexcept
        {
            return (lhs.value_.num * rhs.value_.deno) <=> (rhs.value_.num * lhs.value_.deno);
        }

    #else  // c++17
        friend bool operator==(Rational const& lhs, Rational const& rhs) noexcept
        {
            return (lhs.value_.num * rhs.value_.deno) == (rhs.value_.num * lhs.value_.deno);
        }
        friend bool operator!=(Rational const& lhs, Rational const& rhs) noexcept { return !(lhs == rhs); }
        friend bool operator<(Rational const& lhs, Rational const& rhs) noexcept
        {
            return (lhs.value_.num * rhs.value_.deno) < (rhs.value_.num * lhs.value_.deno);
        }
        friend bool operator<=(Rational const& lhs, Rational const& rhs) noexcept { return !(rhs < lhs); }
        friend bool operator>(Rational const& lhs, Rational const& rhs) noexcept { return rhs < lhs; }
        friend bool operator>=(Rational const& lhs, Rational const& rhs) noexcept { return !(lhs < rhs); }
    #endif
        /// @brief put-to演算子の定義
        friend std::ostream& operator<<(std::ostream& os, const Rational& rhs)
        {
            return (rhs.value_.deno == 1) ? os << rhs.value_.num : os << rhs.value_.num << "/" << rhs.value_.deno;
        }

        /// @brief doubleへの変換演算子
        /// @brief doubleで表現可能な場合のみ利用可能
        template <typename U = T>
        explicit operator double() const noexcept
    #if __cplusplus >= 202002L  // c++20
            requires std::is_convertible_v<U, double>
    #endif
        {
            return static_cast<double>(value_.num) / static_cast<double>(value_.deno);
        }

    private:
        struct rational_t {
            T num;
            T deno;

    #if __cplusplus >= 202002  // c++20
            friend bool operator==(rational_t const& lhs, rational_t const& rhs) noexcept = default;

    #else  // c++17
            friend bool operator==(rational_t const& lhs, rational_t const& rhs) noexcept
            {
                return lhs.num == rhs.num && lhs.deno == rhs.deno;
            }
    #endif
        };
        /// @brief num/denoを約分して、rational_tで返す
        static rational_t reduce(T num, T deno) noexcept
        {
            T const gcd = std::gcd(num, deno);
            num /= gcd;
            deno /= gcd;
            if (deno < 0) {  // 分母を正に保つ
                return {-num, -deno};
            }
            else {
                return {num, deno};
            }
        }

    private:
        rational_t value_;
    };
    }  // namespace Nstd
```
```cpp
    //  example/template_cpp17/rational_ut.cpp 12

    auto       r1    = Rational{1, 2};
    const auto r1_sv = r1;
    auto       r2    = Rational{1, 3};

    ASSERT_GE(r1, r2);

    r1 += r2;  // operator+
    ASSERT_EQ((Rational{5, 6}), r1);
    r1 = r1_sv;

    r1 -= r2;
    ASSERT_EQ((Rational{1, 6}), r1);
    r1 = r1_sv;

    auto oss = std::ostringstream{};
    oss << r1;
    ASSERT_EQ("1/2", oss.str());  // operator<<
```

### 有理数リテラル <a id="SS_4_5_5"></a>
[固定小数点クラス](#SS_4_5_2)に対して、[固定小数点リテラル](#SS_4_5_3)を定義したように、
使い勝手のよい環境をユーザに提供するために、
[有理数クラス](#SS_4_5_4)に対して、有理数リテラルを定義するべきである。

```cpp
    //  example/template_cpp17/rational.h 147

    namespace Nstd {
    /// @brief Rational<int32_t>をユーザ定義リテラルとして扱うためのオペレータ
    ///        _rn: rational number
    ///  @param N/Mの形式の文字列リテラル
    Rational<int32_t> operator"" _rn(char const* str, size_t)
    {
        std::string_view input{str};
        size_t           sep = input.find('/');

        if (sep == std::string::npos) {
            throw std::invalid_argument("invalid formt for user-defined rational number");
        }

        int32_t num  = std::stoi(str);
        int32_t deno = std::stoi(input.substr(sep + 1).data());

        return {num, deno};
    }
    }  // namespace Nstd
```
```cpp
    //  example/template_cpp17/rational_ut.cpp 55

    auto r1 = "1/2"_rn;
    auto r2 = "1/3"_rn;

    ASSERT_GE(r1, r2);
    ASSERT_DOUBLE_EQ(static_cast<double>(r1), 0.5);
```

## ログ取得ライブラリの開発2 <a id="SS_4_6"></a>
ログ取得ライブラリでの問題は「Logging名前空間が依存してよい名前空間」に

```cpp
    //  example/template/app_ints.h 6

    namespace App {
    using Ints_t = std::vector<int>;
    }
```

のようなコンテナに共通したoperator<<を定義することで解決する。
それは 「[コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)」で示したコードそのものであるため、
これを使い、問題を解決したログ取得ライブラリを以下に示す。

```cpp
    //  example/template/logger.h 7

    namespace Logging {
    class Logger {
    public:
        static Logger&       Inst();
        static Logger const& InstConst() { return Inst(); }

        std::string Get() const;  // ログデータの取得
        void        Clear();      // ログデータの消去

        template <typename... ARGS>  // ログの登録
        void Set(char const* filename, uint32_t line_no, ARGS const&... args)
        {
            oss_.width(32);
            oss_ << filename << ":";

            oss_.width(3);
            oss_ << line_no;

            set_inner(args...);
        }

        Logger(Logger const&)            = delete;
        Logger& operator=(Logger const&) = delete;

    private:
        void set_inner() { oss_ << std::endl; }

        template <typename HEAD, typename... TAIL>
        void set_inner(HEAD const& head, TAIL const&... tails)
        {
            using Nstd::operator<<;  // Nstd::operator<<もname lookupの対象にする

            oss_ << ":" << head;
            set_inner(tails...);
        }

        Logger() {}
        std::ostringstream oss_{};
    };
    }  // namespace Logging

    #define LOGGER_P(...) Logging::Logger::Inst().Set(__FILE__, __LINE__)
    #define LOGGER(...) Logging::Logger::Inst().Set(__FILE__, __LINE__, __VA_ARGS__)
```

問題のあったコードとの差分は、メンバ関数テンプレートset_innerの

```cpp
    //  example/template/logger.h 40

    using Nstd::operator<<;  // Nstd::operator<<もname lookupの対象にする
```

のみである。実際に解決できたことを以下の単体テストで示す。

```cpp
    //  example/template/logger_0_ints_ut.h 8

    auto ints = App::Ints_t{1, 2, 3};

    LOGGER("Ints", ints);
    auto line_num = __LINE__;

    auto s = Logging::Logger::InstConst().Get();

    auto exp = std::string{log_str_exp(__FILE__, line_num - 1, ":Ints:1, 2, 3\n")};
    ASSERT_EQ(exp, s);
```

また、

```cpp
    //  example/template/app_ints.h 12

    namespace App {

    class X {
    public:
        X(std::string str, int num) : str_{std::move(str)}, num_{num} {}
        std::string ToString() const { return str_ + "/" + std::to_string(num_); }
        // ...
    };
    }  // namespace App
```

のように定義されたクラスも、

```cpp
    //  example/template/app_ints.h 28

    namespace App {

    inline std::ostream& operator<<(std::ostream& os, X const& x) { return os << x.ToString(); }
    }  // namespace App
```

のような型専用のoperator<<があれば、そのオブジェクトのみではなく、
コンテナや配列に対しても下記のようにログ取得が可能となる。

```cpp
    //  example/template/logger_ut.cpp 37

    using namespace Nstd;

    auto         x  = App::X{"name", 3};
    auto         lx = std::list<App::X>{{"lx3", 3}, {"lx4", 1}};
    App::X const x3[3]{{"x0", 0}, {"x1", 1}, {"x2", 2}};

    LOGGER(1, x, x3, lx);
    auto line_num = __LINE__;

    auto s = Logging::Logger::InstConst().Get();

    auto const exp = log_str_exp(__FILE__, line_num - 1, ":1:name/3:x0/0, x1/1, x2/2:lx3/3, lx4/1\n");
    ASSERT_EQ(exp, s);
```

「[Nstdライブラリの開発](#SS_4_2)」で示した依存関係も維持されており、
これでログ取得ライブラリは完成したと言って良いだろう。


## その他のテンプレートテクニック <a id="SS_4_7"></a>
ここでは、これまでの議論の対象にならなかったテンプレートのテクニックや注意点について記述する。

### forwardingリファレンスとstd::forward <a id="SS_4_7_1"></a>
2個の文字列からstd::vector\<std::string>を生成する下記のような関数について考える。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 9

    std::vector<std::string> gen_vector(std::string const& s0, std::string const& s1)
    {
        auto ret = std::vector<std::string>{};

        ret.push_back(s0);
        ret.push_back(s1);

        return ret;
    }
```

これは下記のように動作する。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 25

    auto a = std::string{"a"};
    auto b = std::string{"b"};

    auto v = gen_vector(a, std::move(b));

    ASSERT_EQ((std::vector<std::string>{"a", "b"}), v);
    ASSERT_EQ("a", a);
    ASSERT_EQ("b", b);  // bはmoveされない
```

このコードは正しく動作するものの、move代入できず、パフォーマンス問題を引き起こす可能性があるため、
[forwardingリファレンス](#SS_6_8_3)を使って下記のように書き直した。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 41

    template <typename STR0, typename STR1>
    std::vector<std::string> gen_vector(STR0&& s0, STR1&& s1)
    {
        auto ret = std::vector<std::string>{};

        ret.push_back(s0);
        ret.push_back(s1);

        return ret;
    }
```

残念ながら、このコードは意図したようには動作せず、下記に示した通り相変わらずmove代入ができない。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 58

    auto a = std::string{"a"};
    auto b = std::string{"b"};

    auto v = gen_vector(a, std::move(b));

    ASSERT_EQ((std::vector<std::string>{"a", "b"}), v);
    ASSERT_EQ("a", a);
    ASSERT_EQ("b", b);  // bはmoveされない
```

この原因は、
「関数が受け取った[rvalue](#SS_6_7_1_2)リファレンスは、
その関数から別の関数に受け渡される時に[lvalue](#SS_6_7_1_1)リファレンスとして扱われる」からである。

この現象について下記の関数テンプレートを用いて解説を行う。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 71

    enum class ExpressionType { Lvalue, Rvalue };

    template <typename T>
    constexpr ExpressionType forwarding_ref2(T&& t)
    {
        return std::is_lvalue_reference_v<decltype(t)> ? ExpressionType::Lvalue : ExpressionType::Rvalue;
    }

    // std::pair<>::first  : forwarding_refの中のtのExpressionType
    // std::pair<>::second : forwarding_ref2の中でtのExpressionType
    template <typename T>
    constexpr std::pair<ExpressionType, ExpressionType> forwarding_ref(T&& t)
    {
        return std::make_pair(std::is_lvalue_reference_v<decltype(t)> ? ExpressionType::Lvalue : ExpressionType::Rvalue,
                              forwarding_ref2(t));
    }
```

下記に示した通り、forwarding_refとforwarding_ref2のパラメータが同じ型であるとは限らない。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 94

    auto i = 0;

    constexpr auto p = forwarding_ref(i);
    static_assert(forwarding_ref2(i) == ExpressionType::Lvalue);  // iはlvalue
    static_assert(p.first == ExpressionType::Lvalue);             // forwarding_refの引数はlvalue
    static_assert(p.second == ExpressionType::Lvalue);            // forwarding_ref中のforwarding_ref2の引数はlvalue

    constexpr auto pm = forwarding_ref(std::move(i));                        // forwarding_refの引数はrvalue
    static_assert(forwarding_ref2(std::move(i)) == ExpressionType::Rvalue);  // forwarding_ref2の引数はrvalue
    static_assert(pm.first == ExpressionType::Rvalue);                       // forwarding_refの引数はrvalue
    static_assert(pm.second == ExpressionType::Lvalue);                      // forwarding_ref中のforwarding_ref2の引数はrvalue

    constexpr auto pm2 = forwarding_ref(int{});
    static_assert(forwarding_ref2(int{}) == ExpressionType::Rvalue);  // forwarding_ref2の引数はrvalue
    static_assert(pm2.first == ExpressionType::Rvalue);               // forwarding_refの引数はrvalue
    static_assert(pm2.second == ExpressionType::Lvalue);              // forwarding_ref中のforwarding_ref2の引数はrvalue
```

この問題はstd::forwardにより対処できる。これによって改良されたコードを下記に示す。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 122

    template <typename STR0, typename STR1>
    std::vector<std::string> gen_vector(STR0&& s0, STR1&& s1)
    {
        auto ret = std::vector<std::string>{};

        ret.push_back(std::forward<STR0>(s0));
        ret.push_back(std::forward<STR1>(s1));

        return ret;
    }
```

下記単体テストが示す通り、rvalueリファレンスはmove代入され、lvalueリファレンスはcopy代入されている。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 140

    auto a = std::string{"a"};
    auto b = std::string{"b"};

    auto v = gen_vector(a, std::move(b));

    ASSERT_EQ((std::vector<std::string>{"a", "b"}), v);
    ASSERT_EQ("a", a);
    ASSERT_EQ("", b);  // bはmoveされた
```

しかし残念ながら、このコードにも改良すべき点がある。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 153

    auto a = std::string{"a"};

    auto v = gen_vector(a, "b");

    ASSERT_EQ((std::vector<std::string>{"a", "b"}), v);
    ASSERT_EQ("a", a);
```

上記の"b"のような文字列リテラルを引数にした場合、
それをstd::vector\<std::string>::push_backに渡した時に、
"b"はテンポラリオブジェクトstd::string("b")のに変換されてしまう。
std::vector\<std::string>へのオブジェクトの挿入は、文字列リテラルから行うことが出来るため、
このテンポラリオブジェクトの生成は明らかに不要な処理である。

下記は、この対策を施すとともに任意の数の引数を受け取れるように改良したコードである。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 169

    void emplace_back(std::vector<std::string>&) {}

    template <typename HEAD, typename... TAIL>
    void emplace_back(std::vector<std::string>& strs, HEAD&& head, TAIL&&... tails)
    {
        strs.emplace_back(std::forward<HEAD>(head));

        if constexpr (sizeof...(tails) != 0) {
            emplace_back(strs, std::forward<TAIL>(tails)...);
        }
    }

    template <typename... STR>
    std::vector<std::string> gen_vector(STR&&... ss)
    {
        auto ret = std::vector<std::string>{};

        emplace_back(ret, std::forward<STR>(ss)...);

        return ret;
    }
```

上記の

```cpp
    sizeof...(tails)
```

はパラメータパックの個数を受け取るための記法である。
従ってこのコードではすべてのパラメータパック変数を消費するまでリカーシブコールを続けることになる
(が、このリカーシブコールはコンパイル時に行われるため、実行時の速度低下は起こさない)。

上記の

```cpp
    std::forward<TAIL>(tails)...
```

は、それぞれのパラメータパック変数をstd::forwardに渡した戻り値を、
再びパラメータパックにするための記法である。

このコードは下記の単体テストが示すように正しく動作する
(が、残念ならがテンポラリオブジェクトが生成されていないことを単体テストで証明することはできない)。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 195

    auto a = std::string{"a"};
    auto b = std::string{"b"};

    auto v = gen_vector(a, std::move(b), "c");

    ASSERT_EQ((std::vector<std::string>{"a", "b", "c"}), v);
    ASSERT_EQ("a", a);
    ASSERT_EQ("", b);  // bはmoveされた
```

上記のgen_vectorはリカーシブコールを使って実装したが、
[畳み込み式](#SS_6_11_5)を使用した下記の実装の方がより明確である。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 209

    template <typename... STR>
    std::vector<std::string> gen_vector(STR&&... ss)
    {
        auto ret = std::vector<std::string>{};

        (ret.emplace_back(std::forward<STR>(ss)), ...);

        return ret;
    }
```

forwardingリファレンスはconstにすることができないが
(T const&&はconstな[rvalue](#SS_6_7_1_2)リファレンスである)、
forwardingリファレンスが[lvalue](#SS_6_7_1_1)リファレンスであった場合は、
constなlvalueリファレンスとして扱うべきである。

従って、下記のようなコードは書くべきではない。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 238

    template <typename STR0, typename STR1>
    std::vector<std::string> gen_vector(STR0&& s0, STR1&& s1)
    {
        auto ret = std::vector<std::string>{};

        ret.push_back(std::move(s0));
        ret.push_back(std::move(s1));

        return ret;
    }
```

もしそのようにしてしまえば、
下記単体テストが示すように非constな実引数はmoveされてしまうことになる。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 255

    auto       a = std::string{"a"};
    auto const b = std::string{"b"};

    auto v = gen_vector(a, std::move(b));

    ASSERT_EQ((std::vector<std::string>{"a", "b"}), v);
    ASSERT_EQ("", a);   // aはmoveされてしまう
    ASSERT_EQ("b", b);  // bはconstなのでmoveされない
```

任意の型Tのrvalueのみを引数に取る関数テンプレートを下記のように記述した場合、
すでに述べたように引数はforwardingリファレンスとなってしまうため、lvalueにもバインドしてしまう。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 271

    template <typename T>
    void f(T&& t) noexcept
    {
        // ...
    }
```

このような場合、下記の記述が必要になる。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 290

    template <typename T>
    void f(T&) = delete;
```

この効果により、下記に示した通りlvalueにはバインドできなくなり、
当初の目的通り、rvalueのみを引数に取る関数テンプレートが定義できたことになる。

```cpp
    //  example/template_cpp17/universal_ref_ut.cpp 298

    auto s = std::string{};

    // f(s);           // f(std::string&)はdeleteされたため、コンパイルエラー
    f(std::string{});  // f(std::string&&)にはバインドできる
```

なお、forwardingリファレンスは、[リファレンスcollapsing](#SS_6_8_6)の一機能としても理解できる。

### ジェネリックラムダによる関数内での関数テンプレートの定義 <a id="SS_4_7_2"></a>
下記のようなクラスとoperator<<があった場合を考える。

```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 13

    struct XYZ {
        XYZ(int ax, int ay, int az) noexcept : x{ax}, y{ay}, z{az} {}
        int x;
        int y;
        int z;
    };

    std::ostream& operator<<(std::ostream& os, XYZ const& xyz)
    {
        return os << std::to_string(xyz.x) + "/" + std::to_string(xyz.y) + "/" + std::to_string(xyz.z);
    }
```

「[Nstd::SafeIndexの開発](#SS_4_4_2)」や「[コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)」
の成果物との組み合わせの単体テストは下記のように書けるだろう。

```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 31

    auto v   = Nstd::SafeVector<XYZ>{{9, 8, 7}, {6, 5, 4}, {3, 2, 1}, {0, 1, 2}};
    auto oss = std::ostringstream{};

    oss << v;
    ASSERT_EQ("9/8/7, 6/5/4, 3/2/1, 0/1/2", oss.str());
```

std::sortによるソートができるかどうかのテストは、C++11までは、

```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 41

    auto v = Nstd::SafeVector<XYZ>{{9, 8, 7}, {6, 5, 4}, {3, 2, 1}, {0, 1, 2}};

    // C++11 lambda                  型の明示が必要
    //                               ↓               ↓
    std::sort(v.begin(), v.end(), [](XYZ const& lhs, XYZ const& rhs) noexcept {
        return std::tie(lhs.x, lhs.y, lhs.z) < std::tie(rhs.x, rhs.y, rhs.z);
    });
    auto oss = std::ostringstream{};

    oss << v;
    ASSERT_EQ("0/1/2, 3/2/1, 6/5/4, 9/8/7", oss.str());
```

のように書くのが一般的だろう。ラムダ式の引数の型を指定しなければならないのは、
範囲for文でautoが使用出来ること等と比べると見劣りがするが、
C++14からは下記のコードで示した通り引数にautoが使えるようになった。

```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 57

    auto v = Nstd::SafeVector<XYZ>{{9, 8, 7}, {6, 5, 4}, {3, 2, 1}, {0, 1, 2}};

    // C++14 generic lambda          型の明示が不要
    //                               ↓                ↓
    std::sort(v.begin(), v.end(), [](auto const& lhs, auto const& rhs) noexcept {
        return std::tie(lhs.x, lhs.y, lhs.z) < std::tie(rhs.x, rhs.y, rhs.z);
    });
    auto oss = std::ostringstream{};

    oss << v;
    ASSERT_EQ("0/1/2, 3/2/1, 6/5/4, 9/8/7", oss.str());
```

この記法は[ジェネリックラムダ](#SS_6_11_6)と呼ばれる。
この機能により関数の中で関数テンプレートと同等のものが定義できるようになった。

#### ジェネリックラムダの内部構造 <a id="SS_4_7_2_1"></a>
ジェネリックラムダは下記のように使用することができる。

```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 73

    template <typename PUTTO>
    void f(PUTTO&& p)
    {
        p(1);       // ラムダの引数elemの型はint
        p(2.71);    // ラムダの引数elemは型はdouble
        p("hehe");  // ラムダの引数elemは型はchar [5]
    }

    TEST(Template, generic_lambda)
    {
        auto oss = std::ostringstream{};

        f([&oss](auto const& elem) { oss << elem << std::endl; });

        ASSERT_EQ("1\n2.71\nhehe\n", oss.str());
    }
```

この例で使用しているクロージャは一見、型をダイナミックに扱っているように見えるが、
下記のような「テンプレートoperator()を持つ関数型」オブジェクトとして展開されていると考えれば、
理解できる。

```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 92

    class Closure {
    public:
        Closure(std::ostream& os) : os_{os} {}

        template <typename T>
        void operator()(T&& t)
        {
            os_ << t << std::endl;
        }

    private:
        std::ostream& os_;
    };
```
```cpp
    //  example/template_cpp17/generic_lambda_ut.cpp 111

    auto oss = std::ostringstream{};

    auto closure = Closure{oss};
    f(closure);

    ASSERT_EQ("1\n2.71\nhehe\n", oss.str());
```

#### std::variantとジェネリックラムダ <a id="SS_4_7_2_2"></a>
unionは、オブジェクトを全く無関係な複数の型に切り替えることができるため、
これが必要な場面では有用な機能であるが、未定義動作を誘発してしまう問題がある。
この対策としてC++17で導入されたものが、std::variantである。

まずは、std::variantの使用例を下記する。

```cpp
    //  example/template_cpp17/variant_ut.cpp 13

    auto v = std::variant<int, std::string, double>{};  // 3つの型を切り替える

    // std::get<N>()の戻り値型は、下記の通りで、
    // N == 0, 1, 2 は、それぞれint, std::string, doubleに対応
    static_assert(std::is_same_v<decltype(std::get<0>(v)), int&>);
    static_assert(std::is_same_v<decltype(std::get<1>(v)), std::string&>);
    static_assert(std::is_same_v<decltype(std::get<2>(v)), double&>);

    v = int{3};  // int型の3を代入

    ASSERT_EQ(v.index(), 0);                                // intを保持
    ASSERT_EQ(std::get<0>(v), 3);                           // intなので問題なくアクセス
    ASSERT_THROW(std::get<1>(v), std::bad_variant_access);  // std::stringではないのでエクセプション
    ASSERT_THROW(std::get<2>(v), std::bad_variant_access);  // doubleではないのでエクセプション

    v = std::string{"str"};  // std::stringオブジェクトを代入

    ASSERT_EQ(v.index(), 1);                                // std::stringを保持
    ASSERT_THROW(std::get<0>(v), std::bad_variant_access);  // intではないのでエクセプション
    ASSERT_EQ(std::get<1>(v), std::string{"str"});          // std::stringなので問題なくアクセス
    ASSERT_THROW(std::get<2>(v), std::bad_variant_access);  // doubleではないのでエクセプション
```

上記からわかる通り、std::variantオブジェクトは、直前に代入されたオブジェクトの型以外で、
値を読み出した場合、問題なく読み出せるが、それ以外ではエクセプションを発生させる。

このstd::variantオブジェクトの保持する型とその値を文字列として取り出すラムダ式は、
下記のように書ける。

```cpp
    //  example/template_cpp17/variant_ut.cpp 37

    auto oss = std::ostringstream{};

    // type_valueはvが保持する型をその値を文字列で返す
    auto type_value = [&oss](auto const& v) {  // ジェネリックラムダでなくても実装可能
        if (v.index() == 0) {
            auto a  = std::get<0>(v);
            using T = std::remove_const_t<std::remove_reference_t<decltype(a)>>;
            oss << Nstd::Type2Str<T>() << " : " << a;  // Nstd::Type2Str<T>はTの型を文字列にする
        }
        else if (v.index() == 1) {
            auto a  = std::get<1>(v);
            using T = std::remove_const_t<std::remove_reference_t<decltype(a)>>;
            oss << Nstd::Type2Str<T>() << " : " << a;  // Nstd::Type2Str<T>はTの型を文字列にする
        }
        else if (v.index() == 2) {
            auto a  = std::get<2>(v);
            using T = std::remove_const_t<std::remove_reference_t<decltype(a)>>;
            oss << Nstd::Type2Str<T>() << " : " << a;  // Nstd::Type2Str<T>はTの型を文字列にする
        }
        else {
            assert(false);  // ここには来ないはず
        }
    };

    v = 3;  // int型の3を代入
    type_value(v);
    ASSERT_EQ("int : 3", oss.str());
    oss = std::ostringstream{};  // ossのリセット

    v = std::string{"str"};  // std::stringオブジェクトを代入
    type_value(v);
    ASSERT_EQ("std::string : str", oss.str());
    oss = std::ostringstream{};  // ossのリセット

    v = 1.1;  // double型の1.1を代入
    type_value(v);
    ASSERT_EQ("double : 1.1", oss.str());
```

このラムダは、
3つの型をテンプレートパラメータとするstd::variantオブジェクト以外には適用できないため、
型の個数に制限のない方法を考える。

この実装は、

* 保持する型が何番目かを見つけるための関数テンプレート
* 関数テンプレートの引数となるジェネリックラムダ

の2つによって下記のように行うことができる。

```cpp
    //  example/template_cpp17/variant_ut.cpp 79

    template <typename VARIANT, typename F, size_t INDEX = 0>
    void org_visit(const F& f, const VARIANT& v)
    {
        constexpr auto n = std::variant_size_v<VARIANT>;

        if constexpr (INDEX < n) {
            if (v.index() == INDEX) {  // 保持する型が見つかった
                f(std::get<INDEX>(v));
                return;
            }
            else {  // 保持する型が見つかるまでリカーシブ
                org_visit<VARIANT, F, INDEX + 1>(f, v);
            }
        }
        else {
            assert(false);  // ここには来ないはず
        }
    }
```
```cpp
    //  example/template_cpp17/variant_ut.cpp 103

    auto oss = std::ostringstream{};

    // 文字列を返すためのジェネリックラムダ
    auto type_value = [&oss](auto const& a) {
        using T = std::remove_const_t<std::remove_reference_t<decltype(a)>>;
        oss << Nstd::Type2Str<T>() << " : " << a;
    };
```

単体テストは、以下のようになる。

```cpp
    //  example/template_cpp17/variant_ut.cpp 113
    {
        auto v = std::variant<int, std::string, double>{};  // 3つの型を切り替える

        v = 3;
        org_visit(type_value, v);
        ASSERT_EQ("int : 3", oss.str());
        oss = std::ostringstream{};  // ossのリセット

        // ...
    }
    {
        auto v = std::variant<char, int, std::string, double>{};  // 4つの型を切り替える

        v = 3;
        org_visit(type_value, v);
        ASSERT_EQ("int : 3", oss.str());
        oss = std::ostringstream{};  // ossのリセット

        v = 'c';
        org_visit(type_value, v);
        ASSERT_EQ("char : c", oss.str());
        oss = std::ostringstream{};  // ossのリセット

        // ...
    }
```

下記のように継承関係のない複数のクラスが同じシグネチャのメンバ関数を持つ場合、

```cpp
    //  example/template_cpp17/variant_ut.cpp 177

    class A {
    public:
        char f() const noexcept { return 'A'; }
    };

    class B {
    public:
        char f() const noexcept { return 'B'; }
    };

    class C {
    public:
        char f() const noexcept { return 'C'; }
    };
```

std::variant、上に示した関数テンプレート、ジェネリックラムダを使い、
下記に示したような疑似的なポリモーフィズムを実現できる。

```cpp
    //  example/template_cpp17/variant_ut.cpp 197

    char ret{};
    auto call_f = [&ret](auto const& a) { ret = a.f(); };

    auto v = std::variant<A, B, C>{};

    org_visit(call_f, v);  // 疑似的なポリモーフィズム
    ASSERT_EQ('A', ret);

    v = B{};
    org_visit(call_f, v);  // 疑似的なポリモーフィズム
    ASSERT_EQ('B', ret);

    v = C{};
    org_visit(call_f, v);  // 疑似的なポリモーフィズム
    ASSERT_EQ('C', ret);
```

ここで示した関数テンプレートは、デザインパターン[Visitor](#SS_3_2_5)の例であり、
ほぼこれと同様のものがstd::visitとして定義されている。

```cpp
    //  example/template_cpp17/variant_ut.cpp 215

    v = A{};
    std::visit(call_f, v);  // 疑似的なポリモーフィズム
    ASSERT_EQ('A', ret);

    v = B{};
    std::visit(call_f, v);  // 疑似的なポリモーフィズム
    ASSERT_EQ('B', ret);

    v = C{};
    std::visit(call_f, v);  // 疑似的なポリモーフィズム
    ASSERT_EQ('C', ret);
```

### クラステンプレートと継承の再帰構造 <a id="SS_4_7_3"></a>
クラステンプレートと継承の再帰構造はCRTPと呼ばれる。
このコードパターンについては、
「[CRTP(curiously recurring template pattern)](#SS_8_1_4)」で説明している。


### 意図しないname lookupの防止 <a id="SS_4_7_4"></a>
下記のようにクラスや関数テンプレートが定義されている場合を考える。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 11

    namespace App {

    struct XY {
        int x;
        int y;
    };

    // このような関数テンプレートは適用範囲が広すぎるので定義すべきではないが、
    // 危険な例を示すためあえて定義している
    template <typename T, typename U>
    inline auto is_equal(T const& lhs, U const& rhs) noexcept -> decltype(lhs.x == rhs.x, lhs.y == rhs.y)
    {
        return lhs.x == rhs.x && lhs.y == rhs.y;
    }
    }  // namespace App
```

これに対しての単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 36

    auto xy0 = App::XY{0, 1};
    auto xy1 = App::XY{0, 2};
    auto xy2 = App::XY{0, 1};

    ASSERT_FALSE(is_equal(xy0, xy1));
    ASSERT_TRUE(is_equal(xy0, xy2));

    struct point {
        int x;
        int y;
    };
    auto p0 = point{0, 1};

    // 下記のような比較ができるようにするためis_equalはテンプレートで実装している
    ASSERT_TRUE(is_equal(p0, xy0));
    ASSERT_FALSE(is_equal(p0, xy1));
```

上記の抜粋である

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 42

    ASSERT_FALSE(is_equal(xy0, xy1));
    ASSERT_TRUE(is_equal(xy0, xy2));
```

が名前空間Appの指定なしでコンパイルできる理由は、
[ADL](#SS_6_12_5)(実引数依存探索)により、Appもis_equalの[name lookup](#SS_6_12_2)の対象になるからである。
これは便利な機能であるが、その副作用として意図しないname
lookupによるバグの混入を起こしてしまうことがある。

上記の名前空間での定義が可視である状態で、下記のようなコードを書いた場合を考える。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 62

    namespace App2 {
    struct XYZ {
        int x;
        int y;
        int z;
    };

    inline bool is_equal(XYZ const& lhs, XYZ const& rhs) noexcept
    {
        return lhs.x == rhs.x && lhs.y == rhs.y && lhs.z == rhs.z;
    }
    }  // namespace App2
```

この単体テストは、やはりADLを使い下記のように書ける。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 83
    auto xyz0 = App2::XYZ{0, 2, 2};
    auto xyz1 = App2::XYZ{0, 1, 2};

    ASSERT_TRUE(is_equal(xyz0, xyz0));
    ASSERT_FALSE(is_equal(xyz0, xyz1));
```

これに問題はないが、下記のテストもコンパイルでき、且つテストもパスしてしまうことには問題がある。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 92

    auto xyz0 = App2::XYZ{0, 2, 2};
    auto xyz1 = App2::XYZ{0, 1, 2};
    auto xy0  = App::XY{0, 1};

    ASSERT_FALSE(is_equal(xy0, xyz0));  // これがコンパイルできてしまう
    ASSERT_TRUE(is_equal(xy0, xyz1));   // このis_equalはAppで定義されたもの
```

このセマンティクス的に無意味な(もしくは混乱を引き起こしてしまうであろう)コードは、

* is_equalの引数の型XY、XYZはそれぞれ名前空間App、App2で定義されている
* 従って、ADLによりis_equalのname lookupには名前空間App、App2も使われる
* 引数の型XY、XYZを取り得るis_equalはAppで定義されたもののみである

というメカニズムによりコンパイルできてしまう。

こういったname lookup、特にADLの問題に対処する方法は、

* [ジェネリックすぎるテンプレートを書かない](#SS_4_7_4_1)
* [ADLが本当に必要でない限り名前を修飾する](#SS_4_7_4_2)
* [ADL Firewallを使う](#SS_4_7_4_3)

のようにいくつか考えられる。これらについて以下で説明を行う。

#### ジェネリックすぎるテンプレートを書かない <a id="SS_4_7_4_1"></a>
ここでの「ジェネリックすぎるテンプレート」とは、
シンタックス的には適用範囲が広いにもかかわらず、セマンティクス的な適用範囲は限られているものを指す。
従って下記のような関数テンプレートを指す概念ではない。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 107

    template <typename T, size_t N>
    constexpr auto array_length(T const (&)[N]) noexcept
    {
        return N;
    }
```

前記で問題を起こした関数テンプレート

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 20

    // このような関数テンプレートは適用範囲が広すぎるので定義すべきではないが、
    // 危険な例を示すためあえて定義している
    template <typename T, typename U>
    inline auto is_equal(T const& lhs, U const& rhs) noexcept -> decltype(lhs.x == rhs.x, lhs.y == rhs.y)
    {
        return lhs.x == rhs.x && lhs.y == rhs.y;
    }
    }  // namespace App
```

が典型的な「ジェネリックすぎるテンプレート」である。
これに対する最も安全な対処は下記コードで示す通りテンプレートを使わないことである。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 125

    namespace App {

    struct XY {
        int x;
        int y;
    };

    inline bool is_equal(XY const& lhs, XY const& rhs) noexcept { return lhs.x == rhs.x && lhs.y == rhs.y; }
    }  // namespace App
```

ジェネリックなis_equalが必要であれば下記単体テストのように
[ジェネリックラムダによる関数内での関数テンプレートの定義](#SS_4_7_2)を行えばよい。
こうすることでその適用範囲はそれを定義した関数内に留まる。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 149

    // 下記のpointのようなクラスが他にもいくつかあった場合、
    // このジェネリックラムダでコードの被りは回避できる
    auto is_equal = [](auto const& lhs, auto const& rhs) noexcept { return lhs.x == rhs.x && lhs.y == rhs.y; };

    struct point {
        int x;
        int y;
    };
    auto p0 = point{0, 1};

    ASSERT_TRUE(is_equal(p0, xy0));
    ASSERT_FALSE(is_equal(p0, xy1));
```

上記で示した

* テンプレートを使わない
* 適用範囲の広いテンプレート(ジェネリック)に対してはアクセスできる箇所を局所化する

といった方法の他にも、「[コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)」で示した

* [std::enable_if](#SS_7_2_5)や[コンセプト](#SS_6_11_3)等を使用してテンプレートに適用できる型を制約する

ことも考えられる。
ベストな方法は状況に大きく依存するため一概には決められない。
その状況でのもっとも単純は方法を選ぶべきだろう(が、何が単純かも一概に決めることは難しい)。


#### ADLが本当に必要でない限り名前を修飾する <a id="SS_4_7_4_2"></a>
下記のコードについて考える。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 170

    struct A {
        int f(int i) noexcept { return i * 3; }
    };

    int f(int i) noexcept { return i * 2; }

    namespace App {

    template <typename T>
    class ExecF : public T {
    public:
        int operator()(int i) noexcept
        {
            return f(i);  // T::fの呼び出しにも見えるが、::fの呼び出し
        }

        // Tを使ったコード
        // ...
    };
    }  // namespace App
```

基底クラスのメンバ関数を呼び出す場合は、T::f()、もしくは、this->f()と書く必要があるため、
下記コードで呼び出した関数fは外部関数fの呼び出しになる
([two phase name lookup](#SS_6_12_3)の一回目のname lookupでfがバインドされるため)。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 197

    auto ef = App::ExecF<A>{};

    ASSERT_EQ(4, ef(2));  // ::fの呼び出しなので、2 * 2 == 4となる
```

これだけでも十分わかりづらいが、
ExecFのテンプレートパラメータにはクラスAしか使われないことがわかったので、
下記のようにリファクタリングしたとしよう。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 207

    struct A {
        int f(int i) noexcept { return i * 3; }
    };

    int f(int i) noexcept { return i * 2; }

    namespace App {

    class ExecF : public A {
    public:
        int operator()(int i) noexcept { return f(i); }

        // Tを使ったコード
        // ...
    };
    }  // namespace App
```

すると、fのname lookupの対象が変わってしまい、元の単体テストはパスしなくなる。

```cpp
    //  example/template_cpp17/suppress_adl_ut.cpp 230

    auto ef = App::ExecF{};

    // ASSERT_EQ(4, ef(2));
    ASSERT_EQ(6, ef(2));  // リファクタリングでname lookupの対象が変わり、A::fが呼ばれる
```

こういった場合に備え単体テストを実行すべきなのだが、この程度の問題はコンパイルで検出したい。
[ADL](#SS_6_12_5)や[two phase name lookup](#SS_6_12_3)が絡む場合ならなおさらである。

こういう意図しない[name lookup](#SS_6_12_2)に備えるためには、
修飾されていない識別子を使わないこと、つまり、
識別子には、名前空間、クラス名、this->等による修飾を施すことが重要である。

ただし、「[コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)」で示したコード等にはADLが欠かせないため、
修飾することをルール化することはできない。場合に合わせた運用が唯一の解となる。


#### ADL Firewallを使う <a id="SS_4_7_4_3"></a>
下記のコードについて考える。

```cpp
    //  example/template_cpp17/adl_firewall_0_ut.cpp 10

    namespace App {

    template <typename T>
    std::string ToString(std::vector<T> const& t)
    {
        auto oss = std::ostringstream{};

        using Nstd::operator<<;
        oss << t;  // Nstd::operator<<もname lookupの対象に含める

        return oss.str();
    }
    }  // namespace App

    // ...

    namespace App {
    struct XY {
        XY(int ax, int ay) noexcept : x{ax}, y{ay} {}
        int x;
        int y;
    };

    std::ostream& operator<<(std::ostream& os, XY const& xyz)
    {
        return os << std::to_string(xyz.x) + "/" + std::to_string(xyz.y);
    }
    }  // namespace App
```

上記のApp::ToStringは「[コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)」のコードを使用し、
std::vectorオブジェクトをstd::stringに変換する。

これに対しての単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/adl_firewall_0_ut.cpp 47

    auto xys = std::vector<App::XY>{{9, 8}, {7, 6}};

    ASSERT_EQ("9/8, 7/6", App::ToString(xys));
```

これは想定通りの動作だが、上記のAppの後に下記のコードを追加するとApp::ToStringは影響を受ける。

```cpp
    //  example/template_cpp17/adl_firewall_1_ut.cpp 40

    // Appに下記を追加
    namespace App {
    template <typename T>
    std::ostream& operator<<(std::ostream& os, std::vector<T> const& t)
    {
        return os << "size:" << t.size();
    }
    }  // namespace App
```

これにより元の単体テストはエラーとなり、新しい単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/adl_firewall_1_ut.cpp 56

    auto xys = std::vector<App::XY>{{9, 8}, {7, 6}};

    // App::operator<<の追加で、App::ToStringの出力が影響を受ける
    // ASSERT_EQ("9/8, 7/6", App::ToString(xys));
    ASSERT_EQ("size:2", App::ToString(xys));
```

これが意図通りなら問題ないが、
ここでは「新たに追加した関数テンプレートApp::operator<<はstd::vector\<App::XY>用ではなかった」
としよう。その場合、これは意図しないADLによるバグの混入となる。
「[ジェネリックすぎるテンプレートを書かない](#SS_4_7_4_1)」
で述べたように追加した関数テンプレートの適用範囲が広すぎることが原因であるが、
XY型から生成されたオブジェクト(std::vector\<App::XY>も含む)によるADLのため、
Appの宣言がname lookupの対象になったことにも原因がある。

下記のコードは後者の原因を解消する。

```cpp
    //  example/template_cpp17/adl_firewall_2_ut.cpp 23

    // Appの中の新たな名前空間XY_Firewall_でstruct XYとoperator<<を宣言
    namespace App {
    namespace XY_Firewall_ {

    struct XY {
        XY(int ax, int ay) noexcept : x{ax}, y{ay} {}
        int x;
        int y;
    };

    std::ostream& operator<<(std::ostream& os, XY const& xyz)
    {
        return os << std::to_string(xyz.x) + "/" + std::to_string(xyz.y);
    }
    }  // namespace XY_Firewall_

    using XY = XY_Firewall_::XY;

    }  // namespace App
```

XY型オブジェクトを引数にした関数呼び出しによる[関連名前空間](#SS_6_12_6)は、
極小なApp::XY_Firewall\_であるため、意図しないADLは起こりづらく、起こっても発見しやすい。
また、XY型用operator<<もApp::XY_Firewall\_で定義し、
App内でusing XYを宣言したことで、これまで通りApp::XYが使える。

このようなテクニックをADL firewallと呼ぶ。


### Nstd::Type2Strの開発 <a id="SS_4_7_5"></a>
「[Nstdライブラリの開発](#SS_4_2)」等で行ったメタ関数の実装は、

* 入り組んだ<>や()の対応漏れ
* &や&&のつけ忘れ
* typenameやtemplateキーワードの漏れ
* メタ関数メンバー::valueや::typeの漏れ

等によるコンパイルエラーとの戦いである。
また、これをクリアしても[two phase name lookup](#SS_6_12_3)や[ADL](#SS_6_12_5)が次の関門になる。
これには、デバッガのステップ実行が強力な武器となるが、
型を文字列に変換する関数があればこれもまた強力な武器となる。

以下に示すNstd::Type2Strは、「[Nstdライブラリの開発](#SS_4_2)」等で実際に使用したそのような関数である。

```cpp
    //  essential/h/nstd_type2str.h 9

    namespace Nstd {
    namespace Inner_ {

    inline std::string demangle(char const* to_demagle)
    {
        int status;

        auto demangled
            = std::unique_ptr<char, decltype(&std::free)>{abi::__cxa_demangle(to_demagle, 0, 0, &status), &std::free};

        return demangled.get();
    }

    template <typename>  // typenameを取り出すためだけのクラステンプレート
    struct type_capture {
    };
    }  // namespace Inner_

    template <typename T>
    std::string Type2Str()
    {
        // typeid(T)とした場合、const/volatile/&の情報が捨てられるため、
        // typeid(type_capture<T>)とし、それを防ぐ。
        auto str = std::string{Inner_::demangle(typeid(Inner_::type_capture<T>).name())};

        // T   == const int ならば、
        // str == Nstd::Inner_::type_capture<int const>
        //        <----------- 27 ----------><-- x --> 下記ではxを切り出す
        constexpr auto beg  = 27U;                                    // 先頭の不要な文字列数
        auto           name = str.substr(beg, str.size() - beg - 1);  // 最後の文字は>なので不要

        while (name.back() == ' ') {  // 無駄なスペースを消す
            auto last = --name.end();
            name.erase(last);
        }

        return name;
    }
    }  // namespace Nstd
```

typeid::name()が返す文字列リテラルは引数の型の文字列表現を持つが、
マングリングされているためヒューマンリーダブルではない。
それをデマングルするのがabi::\_\_cxa\_demangleであるが、
残念なことにこの関数は非標準であるため、
それを使っているNstd::Inner\_::demangleは[g++](#SS_8_13_1)/[clang++](#SS_8_13_2)
でなければコンパイルできないだろう。

それを除けば、
複雑なシンタックスを持つ型を文字列で表現できるNstd::Type2Strは、
テンプレートプログラミングおける有効なデバッグツールであると言える。

下記単体テストは、そのことを示している。

```cpp
    //  example/template/nstd_type2str_ut.cpp 11

    ASSERT_EQ("int const", Nstd::Type2Str<int const>());
    ASSERT_EQ("std::string", Nstd::Type2Str<std::string>());
    ASSERT_EQ("std::vector<int, std::allocator<int> >", Nstd::Type2Str<std::vector<int>>());

    extern void f(int);
    ASSERT_EQ("void (int)", Nstd::Type2Str<decltype(f)>());  // 関数の型

    auto lamda = []() noexcept {};
    ASSERT_NE("", Nstd::Type2Str<decltype(lamda)>());  // XXX::{lambda()#1}な感じになる

    ASSERT_EQ("std::ostream& (std::ostream&, int const (&) [3])",
              Nstd::Type2Str<decltype(Nstd::operator<< <int[3]>)>());

    // std::declvalはrvalueリファレンスを返す
    ASSERT_EQ("int (&&) [3]", Nstd::Type2Str<decltype(std::declval<int[3]>())>());

    int i3[3];
    ASSERT_EQ("int [3]", Nstd::Type2Str<decltype(i3)>());
    ASSERT_EQ("int (&) [3]", Nstd::Type2Str<decltype((i3))>());  // (i3)はlvalueリファレンス

    auto& r = i3;
    ASSERT_EQ("int (&) [3]", Nstd::Type2Str<decltype(r)>());
```

### 静的な文字列オブジェクト <a id="SS_4_7_6"></a>
std::stringは文字列を扱うことにおいて、非常に有益なクラスではあるが、
コンパイル時に文字列が決定できる場合でも、動的にメモリを確保する。

この振る舞いは、

* ランタイム時にnew/deleteを行うため、処理の遅さにつながる。
* 下記のようにエクセプションオブジェクトにファイル位置を埋め込むことは、
  デバッグに便利であるが、メモリ確保失敗を通知するような場面ではこの方法は使えない。

```cpp
    //  example/template_cpp17/nstd_exception_ut.cpp 6

    class Exception : std::exception {
    public:
        Exception(char const* filename, uint32_t line_num, char const* msg)
            : what_str_{std::string{filename} + ":" + std::to_string(line_num) + ":" + msg}
        {
        }

        char const* what() const noexcept override { return what_str_.c_str(); }

    private:
        std::string what_str_;
    };

    int32_t div(int32_t a, int32_t b)
    {
        if (b == 0) {
            throw Exception{__FILE__, __LINE__, "divided by 0"};  // 24行目
        }

        return a / b;
    }
```
```cpp
    //  example/template_cpp17/nstd_exception_ut.cpp 34

    auto caught = false;
    try {
        div(1, 0);
    }
    catch (Exception const& e) {
        ASSERT_STREQ("nstd_exception_ut.cpp:24:divided by 0", e.what());
        caught = true;
    }
    ASSERT_TRUE(caught);
```

このような問題を回避するために、ここでは静的に文字列を扱うためのクラスStaticStringを開発する。

#### StaticStringのヘルパークラスの開発 <a id="SS_4_7_6_1"></a>
StaticStringオブジェクトは、char配列をメンバとして持つが、
コンパイル時に解決できる配列の初期化にはパラメータパックが利用できる。
そのパラメータパック生成クラスを下記のように定義する。

```cpp
    //  example/template_cpp17/nstd_seq.h 4

    // パラメータパック展開ヘルパクラス
    template <size_t... Ns>
    struct index_sequence {
    };

    // index_sequence<0, 1, 2, ...>を作るためのクラステンプレート
    // make_index_sequence<3>
    // -> make_index_sequence<2, 2>
    // -> make_index_sequence<1, 1, 2>
    // -> make_index_sequence<0, 0, 1, 2>
    // -> index_sequence<0, 1, 2>
    template <size_t N, size_t... Ns>
    struct make_index_sequence : make_index_sequence<N - 1, N - 1, Ns...> {
    };

    template <size_t... Ns>
    struct make_index_sequence<0, Ns...> : index_sequence<Ns...> {
    };

```

このクラスにより、下記のような配列メンバの初期ができるようになる。

```cpp
    //  example/template_cpp17/nstd_seq_ut.cpp 7

    template <size_t N>
    struct seq_test {
        template <size_t... S>
        constexpr seq_test(index_sequence<S...>) noexcept : data{S...}
        {
        }
        int const data[N];
    };
```
```cpp
    //  example/template_cpp17/nstd_seq_ut.cpp 24

    constexpr auto st = seq_test<3>{index_sequence<1, 2, 3>()};
    ASSERT_EQ(1, st.data[0]);
    ASSERT_EQ(2, st.data[1]);
    ASSERT_EQ(3, st.data[2]);
```

これを下記のように使うことで、メンバである文字列配列のコンパイル時初期化ができるようになる。

```cpp
    //  example/template_cpp17/nstd_seq_ut.cpp 33

    template <size_t N>
    class seq_test2 {
    public:
        template <size_t... S>
        constexpr seq_test2(char const (&str)[N], index_sequence<S...>) noexcept : string_{str[S]...}
        {
        }

        constexpr char const (&String() const noexcept)[N] { return string_; }

    private:
        char const string_[N];
    };
```
```cpp
    //  example/template_cpp17/nstd_seq_ut.cpp 52

    constexpr char const str[]{"123"};

    constexpr auto st = seq_test2<4>{str, index_sequence<0, 1, 2>()};
    ASSERT_STREQ("123", st.String());

    constexpr auto st2 = seq_test2<4>{str, make_index_sequence<sizeof(str) - 1>()};
    ASSERT_STREQ("123", st2.String());
```

上記とほぼ同様のクラステンプレートstd::index_sequence、std::make_index_sequenceが、
utilityで定義されているため、以下ではこれらを使用する。

#### StaticStringの開発 <a id="SS_4_7_6_2"></a>
StaticStringはすでに示したテクニックを使い、下記のように定義できる。

```cpp
    //  example/h/nstd_static_string.h 10

    template <size_t N>
    class StaticString {
    public:
        constexpr StaticString(char const (&str)[N]) noexcept : StaticString{0, str, std::make_index_sequence<N - 1>{}} {}

        template <size_t M>
        constexpr StaticString(size_t offset, StaticString<M> ss) noexcept
            : StaticString{offset, ss.string_, std::make_index_sequence<N - 1>{}}
        {
        }

        constexpr StaticString(std::initializer_list<char> args) noexcept
            : StaticString{0, args, std::make_index_sequence<N - 1>{}}
        {
        }

        constexpr char const (&String() const noexcept)[N] { return string_; }
        constexpr size_t Size() const noexcept { return N; }

    private:
        char const string_[N];

    #if __cplusplus >= 202002L  // c++20
        template <Beginable T, size_t... I>
    #else  // c++17
        template <typename T, size_t... I>
    #endif
        // offsetは部分StaticString切り出しのため(TopStr, BottomStr)
        constexpr StaticString(size_t offset, T& t, std::index_sequence<I...>) noexcept
            : string_{std::begin(t)[I + offset]...}
        {
        }

        template <size_t M>
        friend class StaticString;
    };
```

文字列リテラルからStaticStringを生成する単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_static_string_ut.cpp 12

    const auto fs = StaticString{"abc"};  // C++17からのNの指定は不要

    static_assert(sizeof(4) == fs.Size());
    ASSERT_STREQ("abc", fs.String());

    // 文字列不足であるため、下記はコンパイルさせない
    // constexpr StaticString<4> fs2{"ab"};
```

また、std::initializer_list\<char>による初期化の単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_static_string_ut.cpp 24

    const auto fs = StaticString<4>{'a', 'b', 'c'};  // C++17でもNの指定は必要

    static_assert(sizeof(4) == fs.Size());
    ASSERT_STREQ("abc", fs.String());

    // 文字列不足であるため、下記はコンパイルさせない
    // constexpr StaticString<4> fs2{'a', 'b'};
```

次にこのクラスにc++17用に`operator==`とc++20用に`operator<=>`を追加する。

```cpp
    //  example/h/nstd_static_string.h 49

    namespace Inner_ {
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

    #if __cplusplus <= 201703L  // c++17
    template <size_t N1, size_t N2>
    constexpr bool operator==(StaticString<N1> const&, StaticString<N2> const&) noexcept
    {
        return false;
    }

    template <size_t N1, size_t N2>
    constexpr bool operator!=(StaticString<N1> const& lhs, StaticString<N2> const& rhs) noexcept
    {
        return !(lhs == rhs);
    }

    template <size_t N>
    constexpr bool operator==(StaticString<N> const& lhs, StaticString<N> const& rhs) noexcept
    {
        return Inner_::equal_n(0, lhs, rhs);
    }

    template <size_t N>
    constexpr bool operator!=(StaticString<N> const& lhs, StaticString<N> const& rhs) noexcept
    {
        return !(lhs == rhs);
    }

    template <size_t N1, size_t N2>
    constexpr bool operator==(StaticString<N1> const& lhs, char const (&rhs)[N2]) noexcept
    {
        return lhs == StaticString{rhs};
    }

    template <size_t N1, size_t N2>
    constexpr bool operator!=(StaticString<N1> const& lhs, char const (&rhs)[N2]) noexcept
    {
        return !(lhs == rhs);
    }

    template <size_t N1, size_t N2>
    constexpr bool operator==(char const (&lhs)[N1], StaticString<N2> const& rhs) noexcept
    {
        return StaticString{lhs} == rhs;
    }

    template <size_t N1, size_t N2>
    constexpr bool operator!=(char const (&lhs)[N1], StaticString<N2> const& rhs) noexcept
    {
        return !(lhs == rhs);
    }
    #elif __cplusplus >= 202002L  // c++20
    // 以下、operator==とoperator!=を<=>に置き換え
    template <size_t N1, size_t N2>
    constexpr auto operator<=>(StaticString<N1> const& lhs, StaticString<N2> const& rhs) noexcept
    {
        if constexpr (N1 != N2) {
            return N1 <=> N2;  // サイズが異なる場合は直接サイズを比較
        }
        else {
            return std::lexicographical_compare_three_way(lhs.String(), lhs.String() + N1 - 1, rhs.String(),
                                                          rhs.String() + N2 - 1);
        }
    }

    template <size_t N1, size_t N2>
    constexpr auto operator<=>(StaticString<N1> const& lhs, char const (&rhs)[N2]) noexcept
    {
        return lhs <=> StaticString{rhs};
    }

    template <size_t N1, size_t N2>
    constexpr auto operator<=>(char const (&lhs)[N1], StaticString<N2> const& rhs) noexcept
    {
        return StaticString{lhs} <=> rhs;
    }

    // operator==は明示的に定義する必要がある（<=>からは自動生成されない）
    template <size_t N1, size_t N2>
    constexpr bool operator==(StaticString<N1> const& lhs, StaticString<N2> const& rhs) noexcept
    {
        return (lhs <=> rhs) == 0;
    }

    template <size_t N1, size_t N2>
    constexpr bool operator==(StaticString<N1> const& lhs, char const (&rhs)[N2]) noexcept
    {
        return lhs == StaticString{rhs};
    }

    template <size_t N1, size_t N2>
    constexpr bool operator==(char const (&lhs)[N1], StaticString<N2> const& rhs) noexcept
    {
        return StaticString{lhs} == rhs;
    }
    #endif
```

単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_static_string_ut.cpp 70

    static_assert(StaticString{"123"} == StaticString{"123"});
    static_assert(StaticString{"123"} != StaticString{"1234"});
    static_assert(StaticString{"123"} == "123");
    static_assert("123" == StaticString{"123"});
    static_assert(StaticString{"123"} != "1234");
    static_assert("1234" != StaticString{"123"});
```

[暗黙の型変換](#SS_6_6_2_2)を利用した文字列リテラルからStaticStringオブジェクトへの変換は、
StaticStringがテンプレートであるため機能せず、上記のように書く必要がある。

同様にoperator + を追加する。

```cpp
    //  example/h/nstd_static_string.h 158

    namespace Inner_ {
    template <size_t N1, size_t... I1, size_t N2, size_t... I2>
    constexpr StaticString<N1 + N2 - 1> concat(char const (&str1)[N1], std::index_sequence<I1...>, char const (&str2)[N2],
                                               std::index_sequence<I2...>) noexcept
    {
        return {str1[I1]..., str2[I2]...};
    }
    }  // namespace Inner_

    template <size_t N1, size_t N2>
    constexpr auto operator+(StaticString<N1> const& lhs, StaticString<N2> const& rhs) noexcept
    {
        return Inner_::concat(lhs.String(), std::make_index_sequence<N1 - 1>{}, rhs.String(),
                              std::make_index_sequence<N2>{});
    }

    template <size_t N1, size_t N2>
    constexpr auto operator+(StaticString<N1> const& lhs, char const (&rhs)[N2]) noexcept
    {
        return lhs + StaticString{rhs};
    }

    template <size_t N1, size_t N2>
    constexpr auto operator+(char const (&lhs)[N1], StaticString<N2> const& rhs) noexcept
    {
        return StaticString{lhs} + rhs;
    }
```

```cpp
    //  example/template_cpp17/nstd_static_string_ut.cpp 83

    constexpr auto fs0 = StaticString{"1234"} + StaticString{"567"};
    static_assert(std::is_same_v<StaticString<fs0.Size()> const, decltype(fs0)>);
    static_assert("1234567" == fs0);

    constexpr auto fs1 = StaticString{"1234"} + ":";
    static_assert(std::is_same_v<StaticString<fs1.Size()> const, decltype(fs1)>);
    static_assert("1234:" == fs1);

    constexpr auto fs2 = ":" + StaticString{"567"};
    static_assert(std::is_same_v<StaticString<fs2.Size()> const, decltype(fs2)>);
    static_assert(":567" == fs2);

    constexpr auto fs3 = StaticString{"1234"} + ":" + StaticString{"567"};
    static_assert(std::is_same_v<StaticString<fs3.Size()> const, decltype(fs3)>);
    static_assert("1234:567" == fs3);
```

以上でstd::stringのように=、==、+などの演算が可能となった。
さらに下記の関数を追加することで、任意の位置、
任意のサイズの文字列を切り出せるようにすることでStaticStringはより便利に使用できるようになる。

```cpp
    //  example/h/nstd_static_string.h 188

    template <size_t SIZE, size_t N>  // StaticString<SiZE>の部分文字列生成
    constexpr auto TopStr(StaticString<N> ss) noexcept
    {
        return StaticString<SIZE + 1>{0, ss};  // SIZE文字 + 終端文字
    }

    template <size_t OFFSET, size_t N>  // 先頭からオフセット2文字～終端文字まで
    constexpr auto BottomStr(StaticString<N> ss) noexcept
    {
        return StaticString<N - OFFSET>{OFFSET, ss};
    }
```

```cpp
    //  example/template_cpp17/nstd_static_string_ut.cpp 53

    constexpr auto ss  = StaticString{"0123456789"};
    auto           ss2 = TopStr<2>(ss);  // 先頭2文字
    static_assert(3 == ss2.Size());      // 先頭2文字 + 終端文字
    ASSERT_STREQ("01", ss2.String());

    auto ss8 = BottomStr<2>(ss);     // 先頭からオフセット2文字～終端文字まで
    static_assert(9 == ss8.Size());  // 先頭からオフセット2文字～終端文字までは結果的に9文字
    ASSERT_STREQ("23456789", ss8.String());

    ASSERT_EQ(ss2 + ss8, ss);  // 元に戻す。+、= が使用される。
```

#### 整数をStaticStringに変換する関数の開発 <a id="SS_4_7_6_3"></a>
コンパイル時に__LINE__をStaticStringに変換できれば、
ファイル位置をStaticStringで表現できるため、
ここではその変換関数Int2StaticString\<>()の実装を行う。

行番号を10進数での文字列で表現するため、いくつかのヘルパ関数を下記のように定義する。

```cpp
    //  example/h/nstd_static_string_num.h 8

    namespace Inner_ {

    // 10進数桁数を返す
    constexpr size_t num_of_digits(size_t n) noexcept { return n > 0 ? 1 + num_of_digits(n / 10) : 0; }

    // 10のn乗を返す
    constexpr uint32_t ten_to_nth_power(uint32_t n) noexcept { return n == 0 ? 1 : 10 * ten_to_nth_power(n - 1); }

    // 10進数の桁の若い順番に左から並べなおす(12345 -> 54321)
    constexpr uint32_t reverse_num(uint32_t num) noexcept
    {
        return num != 0 ? (num % 10) * ten_to_nth_power(num_of_digits(num) - 1) + reverse_num(num / 10) : 0;
    }

    // 10進数一桁をacsii文字に変換
    constexpr char digit_to_char(uint32_t num, uint32_t n_th) noexcept
    {
        return '0' + (num % (ten_to_nth_power(n_th + 1))) / ten_to_nth_power(n_th);
    }

    // Int2StaticStringのヘルパ関数
    template <size_t N, size_t... Cs>
    constexpr StaticString<num_of_digits(N) + 1> make_static_string(std::index_sequence<Cs...>) noexcept
    {
        return {digit_to_char(reverse_num(N), Cs)...};
    }
    }  // namespace Inner_
```

単体テストは下記のようになる。

```cpp
    //  example/template/nstd_static_string_num_ut.cpp 47

    constexpr auto ns       = make_static_string<__LINE__>(std::make_index_sequence<Inner_::num_of_digits(__LINE__)>());
    auto           line_num = __LINE__ - 1;

    ASSERT_EQ(std::to_string(line_num), ns.String());
```

このままでは使いづらいため、これをラッピングした関数を下記のように定義することで、
Int2StaticString\<>()が得られる。

```cpp
    //  example/h/nstd_static_string_num.h 38

    template <size_t N>
    constexpr StaticString<Inner_::num_of_digits(N) + 1> Int2StaticString() noexcept
    {
        return Inner_::make_static_string<N>(std::make_index_sequence<Inner_::num_of_digits(N)>());
    }
```

単体テストは下記のようになる。

```cpp
    //  example/template/nstd_static_string_num_ut.cpp 65

    constexpr auto ns       = Int2StaticString<__LINE__>();
    auto           line_num = __LINE__ - 1;

    ASSERT_EQ(std::to_string(line_num), ns.String());
```

#### ファイル位置を静的に保持したエクセプションクラスの開発 <a id="SS_4_7_6_4"></a>
「[静的な文字列オブジェクト](#SS_4_7_6)」で見たように、
ファイル位置を動的に保持するエクセプションクラスは使い勝手が悪い。
ここでは、その問題を解決するためのExceptionクラスの実装を示す。

```cpp
    //  example/h/nstd_exception.h 11

    /// @class Exception
    /// @brief StaticString<>を使ったエクセプションクラス
    ///        下記のMAKE_EXCEPTIONを使い生成
    /// @tparam E   std::exceptionから派生したエクセプションクラス
    /// @tparam N   StaticString<N>
    template <typename E, size_t N>
    #if __cplusplus >= 202002L  // c++20
    requires std::derived_from<E, std::exception>
    #endif
    class Exception : public E {
    public:
        static_assert(std::is_base_of_v<std::exception, E>);

        Exception(StaticString<N> const& what_str) noexcept : what_str_{what_str} {}
        char const* what() const noexcept override { return what_str_.String(); }

    private:
        StaticString<N> const what_str_;
    };
```

StaticStringと同様に、このままでは不便であるため、下記の関数を定義する。

```cpp
    //  example/h/nstd_exception.h 33

    namespace Inner_ {
    template <typename E, template <size_t> class STATIC_STR, size_t N>
    #if __cplusplus >= 202002L  // c++20
    requires std::derived_from<E, std::exception>
    #endif
    auto make_exception(STATIC_STR<N> exception_str) noexcept { return Exception<E, N>{exception_str}; }
    }  // namespace Inner_

    template <typename E, size_t LINE_NUM, size_t F_N, size_t M_N>
    #if __cplusplus >= 202002L  // c++20
    requires std::derived_from<E, std::exception>
    #endif
    auto MakeException(char const (&filename)[F_N], char const (&msg)[M_N]) noexcept
    {
        return Inner_::make_exception<E>(StaticString{filename} + ":" + Int2StaticString<LINE_NUM>() + ":" + msg);
    }
```

単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_exception_ut.cpp 89

    auto caught   = false;
    auto line_num = __LINE__ + 2;  // 2行下の行番号
    try {
        throw MakeException<std::exception, __LINE__>(__FILE__, "some error message");
    }
    catch (std::exception const& e) {
        auto oss = std::ostringstream{};
        oss << __FILE__ << ":" << line_num << ":some error message";

        ASSERT_EQ(oss.str(), e.what());
        caught = true;
    }

    ASSERT_TRUE(caught);
```

Exceptionクラスの利便性をさらに高めるため、下記の定義を行う。

```cpp
    //  example/h/nstd_exception.h 54

    #define MAKE_EXCEPTION(E__, msg__) Nstd::MakeException<E__, __LINE__>(__FILE__, msg__)
```

上記は、関数型マクロの数少ない使いどころである。

単体テストは下記のようになる。

```cpp
    //  example/template_cpp17/nstd_exception_ut.cpp 109

    uint32_t line_num_div;  // エクセプション行を指定

    int32_t div(int32_t a, int32_t b)
    {
        if (b == 0) {
            line_num_div = __LINE__ + 1;  // 次の行番号
            throw MAKE_EXCEPTION(std::exception, "divided by 0");
        }

        return a / b;
    }
```
```cpp
    //  example/template_cpp17/nstd_exception_ut.cpp 126

    auto caught = false;

    try {
        div(1, 0);
    }
    catch (std::exception const& e) {  // リファレンスでcatchしなければならない
        auto oss = std::ostringstream{};
        oss << __FILE__ << ":" << line_num_div << ":divided by 0";
        ASSERT_EQ(oss.str(), e.what());
        caught = true;
    }

    ASSERT_TRUE(caught);
```

### 関数型をテンプレートパラメータで使う <a id="SS_4_7_7"></a>
ここで使う「関数型」とは、

* 関数へのポインタの型
* クロージャの型、もしくはラムダ式の型
* 関数オブジェクトの型

の総称を指す。

std::unique_ptrは、

* 第1パラメータにポインタの型
* 第2パラメータにそのポインタの解放用の関数ポインタの型

を取ることができるが、通常は第2パラメータは省略される。
省略時にはstd::default_deleteが割り当てられ、そのオブジェクトによって、
第1パラメータに対応するポインタがdeleteされる。

下記コードではこの第2パラメータにstd::freeのポインタの型を与え、
それから生成されるstd::unique_ptrオブジェクトを、

* abi::\__cxa_demangleがstd::mallocで取得したchar型ポインタ
* std::freeのポインタ

で初期化することでメモリの解放を行っている。

```cpp
    //  essential/h/nstd_type2str.h 18

    auto demangled
        = std::unique_ptr<char, decltype(&std::free)>{abi::__cxa_demangle(to_demagle, 0, 0, &status), &std::free};
```

std::unique_ptrの第2パラメータには、上記のような関数へのポインタのみではなく、
関数型を取ることができる。

そのことを順を追って示す。
まずは、std::unique_ptrの動作を確かめるためのクラスを下記のように定義する。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 8

    // デストラクタが呼び出された時に、外部から渡されたフラグをtrueにする
    struct A {
        explicit A(bool& destructor_called) noexcept : destructor_called{destructor_called} {}
        ~A() { destructor_called = true; };

        bool& destructor_called;
    };
```

次に示すのは、第2パラメータに何も指定しないパターンである。
テスト用クラスAの動作確認ができるはずである。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 25

    {  // 第2パラメータに何も指定しない
        auto is_called = false;
        {
            auto ua = std::unique_ptr<A>{new A{is_called}};
            ASSERT_FALSE(is_called);  // uaのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // uaのデストラクタは呼ばれた
    }
```

次に示すのは、

```cpp
    //  example/template_cpp17/func_type_ut.cpp 18

    void delete_func(A* a) noexcept { delete a; }
```

のポインタをstd::unique_ptrの第2パラメータに与えた例である。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 36

    {  // 第2パラメータに関数ポインタを与える
        auto is_called = false;
        {
            auto ua = std::unique_ptr<A, void (*)(A*)>{new A{is_called}, &delete_func};
            ASSERT_FALSE(is_called);  // uaのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // uaのデストラクタは呼ばれた
    }
```

次に示すのは、std::unique_ptrの第2パラメータにラムダを与えた例である。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 47

    {  // 第2パラメータにラムダを与える
        auto is_called = false;
        {
            auto delete_lambda = [](A* a) noexcept { delete a; };

            // ラムダ式の型はインスタンス毎に異なるため、
            // ラムダ式の型を取得するためには下記のようにdecltypeを使う必要がある
            auto ua = std::unique_ptr<A, decltype(delete_lambda)>{new A{is_called}, delete_lambda};
            ASSERT_FALSE(is_called);  // uaのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // uaのデストラクタは呼ばれた
    }
```

次に示すのは、
std::unique_ptrの第2パラメータに関数型オブジェクトの型(std::function)を与えた例である。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 62

    {  // 第2パラメータにstd::function型オブジェクトを与える
        auto is_called = false;
        {
            auto delete_obj = std::function<void(A*)>{[](A* a) noexcept { delete a; }};
            auto ua         = std::unique_ptr<A, std::function<void(A*)>&>{new A{is_called}, delete_obj};
            ASSERT_FALSE(is_called);  // uaのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // uaのデストラクタは呼ばれた
    }
```

以上で見てきたようにstd::unique_ptrの第2パラメータには、
第1パラメータのポインタを引数に取る関数型であれば指定できる。

このようなテンプレートパラメータを持つクラステンプレートの実装例を示すため、
「[RAII(scoped guard)](#SS_8_1_2)でも示したScopedGuardの実装を下記する。

やや意外だが、このようなテンプレートパラメータに特別な記法はなく、以下のようにすれば良い。

```cpp
    //  essential/h/scoped_guard.h 7

    /// @brief RAIIのためのクラス。コンストラクタ引数の関数オブジェクトをデストラクタから呼び出す
    ///
    #if __cplusplus >= 202002L   // c++20

    template <std::invocable F>  // Fが呼び出し可能であることを制約
    #else  // c++17

    template <typename F>
    #endif
    class ScopedGuard {
    public:
        explicit ScopedGuard(F&& f) noexcept : f_{f}
        {
        }

        ~ScopedGuard() { f_(); }
        ScopedGuard(ScopedGuard const&)            = delete;  // copyは禁止
        ScopedGuard& operator=(ScopedGuard const&) = delete;  // copyは禁止

    private:
        F f_;
    };
```

上記コードの抜粋である下記は、テンプレートパラメータを関数型に制約するためのものである。

```cpp
    //  essential/h/scoped_guard.h 7

    /// @brief RAIIのためのクラス。コンストラクタ引数の関数オブジェクトをデストラクタから呼び出す
    ///
    #if __cplusplus >= 202002L   // c++20

    template <std::invocable F>  // Fが呼び出し可能であることを制約
    #else  // c++17

    template <typename F>
    #endif
```

これがなければ、誤った型の関数型をテンプレートパラメータに指定できてしまう。

以下にこのクラステンプレートの単体テストを示す。

まずは、以下の関数と静的変数の組み合わせ

```cpp
    //  example/template_cpp17/func_type_ut.cpp 78

    bool is_caleded_in_static{false};
    void caleded_by_destructor() noexcept { is_caleded_in_static = true; }
```

を使った例である。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 86

    {  // Fに関数ポインタを与える
        is_caleded_in_static = false;
        {
            auto sg = ScopedGuard{&caleded_by_destructor};
            ASSERT_FALSE(is_caleded_in_static);  // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_caleded_in_static);  // sgのデストラクタは呼ばれた
    }
```

次に示すのは、それぞれにラムダ式とstd::functionを使った2例である。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 101

    {  // Fにラムダ式を与える
        auto is_called = false;
        {
            auto gs = ScopedGuard{[&is_called]() noexcept { is_called = true; }};
            ASSERT_FALSE(is_called);  // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // sgのデストラクタは呼ばれた
    }
    {  // Fにstd::function型オブジェクトを与える
        auto is_called = false;
        {
            auto f  = std::function<void(void)>{[&is_called]() noexcept { is_called = true; }};
            auto gs = ScopedGuard{std::move(f)};  // sgのデストラクタは呼ばれていない
            ASSERT_FALSE(is_called);              // sgのデストラクタは呼ばれた
        }
        ASSERT_TRUE(is_called);
    }
```

次に示すのは関数型オブジェクト

```cpp
    //  example/template_cpp17/func_type_ut.cpp 123

    struct TestFunctor {
        explicit TestFunctor(bool& is_called) : is_called_{is_called} {}
        void  operator()() noexcept { is_called_ = true; }
        bool& is_called_;
    };
```

を使った例である。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 134

    {  // Fに関数型オブジェクトを与える
        auto is_called = false;
        auto tf        = TestFunctor{is_called};
        {
            auto sg = ScopedGuard{std::move(tf)};  // C++17以降の記法
            ASSERT_FALSE(is_called);               // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // sgのデストラクタは呼ばれた
    }
```

C++17からサポートされた「クラステンプレートのテンプレートパラメータ推論」が使えないC++14以前では、
下記に示すようにScopedGuardのテンプレートラメータ型を指定しなければならない煩雑さがある。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 146
    {  // Fに関数型オブジェクトを与える
        auto is_called = false;
        auto tf        = TestFunctor{is_called};
        {
            auto sg = ScopedGuard<TestFunctor>{std::move(tf)};  // C++14以前の記法
            ASSERT_FALSE(is_called);                            // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // sgのデストラクタは呼ばれた
    }
```

これを回避するためには下記のような関数テンプレートを用意すればよい。

```cpp
    //  essential/h/scoped_guard.h 38

    template <typename F>
    ScopedGuard<F> MakeScopedGuard(F&& f) noexcept
    {
        return ScopedGuard<F>(std::move(f));
    }
```

下記に示した単体テストから明らかな通り、関数テンプレートの型推測の機能により、
テンプレートパラメータを指定する必要がなくなる。

```cpp
    //  example/template_cpp17/func_type_ut.cpp 161

    {  // Fに関数ポインタを与える
        is_caleded_in_static = false;
        {
            auto sg = MakeScopedGuard(&caleded_by_destructor);
            ASSERT_FALSE(is_caleded_in_static);  // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_caleded_in_static);  // sgのデストラクタは呼ばれた
    }
    {  // Fにラムダ式を与える
        auto is_called = false;
        {
            auto sg = MakeScopedGuard([&is_called]() noexcept { is_called = true; });
            ASSERT_FALSE(is_called);  // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // sgのデストラクタは呼ばれた
    }
    {  // Fにstd::function型オブジェクトを与える
        auto is_called = false;
        {
            auto f  = std::function<void(void)>{[&is_called]() noexcept { is_called = true; }};
            auto sg = MakeScopedGuard(std::move(f));
            ASSERT_FALSE(is_called);  // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // sgのデストラクタは呼ばれた
    }
    {  // Fに関数型オブジェクトを与える
        auto is_called = false;
        auto tf        = TestFunctor{is_called};
        {
            auto sg = MakeScopedGuard(std::ref(tf));  // std::refが必要
            ASSERT_FALSE(is_called);                  // sgのデストラクタは呼ばれていない
        }
        ASSERT_TRUE(is_called);  // sgのデストラクタは呼ばれた
    }
```

このような便利なテンプレートは、Nstdのようなライブラリで定義、宣言し、
ソースコード全域からアクセスできるようにするとプロジェクトの開発効率が少しだけ高まる。


## 注意点まとめ <a id="SS_4_8"></a>
本章では、テンプレートメタプログラミングのテクニックや注意点について解説したが、
本章の情報量は多く、また他の章で行ったものもあるため以下にそれらをまとめる。

* [name lookup](#SS_6_12_2)には複雑なルールが適用されるため、非直感的なバインドが行われる場合がある。
  従って、テンプレートライブラリの開発には単体テストは必須である。

* 使用しているコンパイラが[two phase name lookup](#SS_6_12_3)をサポートしているか否かに気を付ける。
  それがオプションである場合は、two phase name lookupを活性化させる。

* 関数型マクロはそれ以外に実装方法がない時のみに使用する
  。

* 可変長引数を持つ関数の実装には[パラメータパック](#SS_6_11_4)を使う。

* 処理速度や関数のリターンの型に影響する場合があるため、
  パラメータパックの処理の順番に気を付ける(「[前から演算するパラメータパック](#SS_4_1_3_2)」参照)。

* [ADL](#SS_6_12_5)を利用しない場合、テンプレートで使う識別子は名前空間名やthis->等で修飾する
  (「[意図しないname lookupの防止](#SS_4_7_4)」参照)。

* テンプレートのインターフェースではないが、実装の都合上ヘッダファイルに記述する定義は、
  "namespace Inner\_"を使用し、非公開であることを明示する。
  また、"namespace Inner\_"で宣言、定義されている宣言、定義は単体テストを除き、
  外部から参照しない(「[is_void_sfinae_f](#SS_4_3_1_3)の実装」参照)。

* [forwardingリファレンス](#SS_6_8_3)の実際の型がlvalueリファレンスであるならば、
  constなlvalueリファレンスとして扱う
  。

* ユニバーサルリファレンス引数を他の関数に渡すのであれば、std::forwardを使う
  (「[forwardingリファレンス](#SS_6_8_3)」、「[forwardingリファレンスとstd::forward](#SS_4_7_1)」参照)。

* 関数テンプレートとその特殊化はソースコード上なるべく近い位置で定義する
  (「[two phase name lookup](#SS_6_12_3)」参照)。

* [two phase name lookup](#SS_6_12_3)により意図しない副作用が発生する可能性があるため、
  STLが特殊化を想定しているstd::hash等を除き、STLの拡張は行わない。

* ユーザが定義するテンプレートは適切に定義された名前空間内で定義する
  。

* 型とその2項演算子オーバーロードは同じ名前空間で定義する
  (「[two phase name lookup](#SS_6_12_3)」参照)。

* 関数テンプレートのオーバーロードと特殊化の[name lookup](#SS_6_12_2)の優先度に気を付ける。
  オーバーロードのベストマッチ選択後に特殊化された関数テンプレートがname lookupの対象になるため、
  下記コードが示すように直感に反する関数が選択される場合がある。

```cpp
    //  example/template_cpp17/etc_ut.cpp 7

    template <typename T> constexpr int32_t f(T) noexcept { return 0; }                   // f-0
    template <typename T> constexpr int32_t f(T*) noexcept { return 1; }                  // f-1
    template <>           constexpr int32_t f<int32_t*>(int32_t*) noexcept { return 2; }  // f-2
    // f-2はf-1の特殊化のように見えるが、T == int32_t*の場合のf-0の特殊化である。
```
```cpp
    //  example/template_cpp17/etc_ut.cpp 18

    // 以下、f-0/f-1/f-2のテスト
    auto c   = char{0};
    auto i32 = 0;

    // 以下はおそらく直感通り
    static_assert(f(0) == 0);               // f-0が呼ばれる
    static_assert(f(&c) == 1);              // f-1が呼ばれる
    static_assert(f<int32_t*>(&i32) == 2);  // f-2が呼ばれる

    // 以下はおそらく直感に反する
    static_assert(f(nullptr) == 0);  // f-1ではなく、f-0が呼ばれる
    static_assert(f(&i32) == 1);     // f-2ではなく、f-1が呼ばれる
```

* forwardingリファレンスを持つ関数テンプレートをオーバーロードしない。
  「[forwardingリファレンスとstd::forward](#SS_4_7_1)」で述べたように、
  forwardingリファレンスはオーバーロードするためのものではなく、
  lvalue、rvalue両方を受け取ることができる関数テンプレートを、
  オーバーロードを使わずに実現するための記法である。

* テンプレートに関数型オブジェクトを渡す場合、リファレンスの付け忘れに気を付ける
  (「[関数型をテンプレートパラメータで使う](#SS_4_7_7)」
  参照)。

* 意図しないテンプレートパラメータによるインスタンス化の防止や、
  コンパイルエラーを解読しやすくするために、適切にstatic_assert使うことは重要であるが、
  static_assertによるテンプレートパラメータの制約よりも、[コンセプト](#SS_6_11_3)による制約を優先する。

* ランタイム時の処理を削減する、static_assertを適切に用いる等の目的のために、
  関数テンプレートには適切にconstexprを付けて宣言する
  (「[コンテナ用Nstd::operator\<\<の開発](#SS_4_4_4)」
  、「[constexpr関数](#SS_6_5_3)」
  参照)。


<!-- ./md/dynamic_memory_allocation.md -->
# ダイナミックメモリアロケーション <a id="SS_5"></a>
本章で扱うダイナミックメモリアロケーション([ヒープ](#SS_8_12_1)の使用)とは、new/delete、malloc/free
によるメモリ確保/解放のことである。

malloc/freeは、

* 最長処理時間を規定できない(リアルタイム性の欠如)
* メモリのフラグメントを起こす

等の問題(「[malloc/freeの問題点](#SS_5_1)」参照)を持っている。
new/deleteは通常malloc/freeを使って実装されているため同じ問題を持っているが、
これらが汎用OS上でのアプリケーションで実際の不具合につながることはほとんどない。一方で、 

* リアルタイムな応答が要求される(MISRA/AUTOSAR C++等のガイドラインの遵守が求められる)
* メモリの使用制限が厳しい(ページングと2次記憶がない)

ようなソフトウェアでは、malloc/freeの問題は致命的な不具合につながる。

このような場合、以下のようなテクニックが有効となる。

* 「[グローバルnew/deleteのオーバーロード](#SS_5_4_1)」で述べたようなnewを実装する。
* グローバルnewを使用せず、 「[クラスnew/deleteのオーバーロード](#SS_5_4_3)」で述べたようなクラス毎のnewを実装する。
* malloc/newを用いてエクセプション送出を行っているツールチェーンを使用している場合、
 「[エクセプション処理機構の変更](#SS_5_3_2)」で述べたような方法でリアルタイム制を確保するか、
  エクセプションを使用しない。

本章では、このようなテクニックの実装を詳しく説明する。

__この章の構成__

&emsp;&emsp; [malloc/freeの問題点](#SS_5_1)  
&emsp;&emsp; [メモリプール](#SS_5_2)  
&emsp;&emsp;&emsp; [固定長メモリプール](#SS_5_2_1)  
&emsp;&emsp;&emsp; [可変長メモリプール](#SS_5_2_2)  

&emsp;&emsp; [メモリプールのエクセプション](#SS_5_3)  
&emsp;&emsp;&emsp; [MPoolBadAlloc](#SS_5_3_1)  
&emsp;&emsp;&emsp; [エクセプション処理機構の変更](#SS_5_3_2)  

&emsp;&emsp; [new/deleteのオーバーロード](#SS_5_4)  
&emsp;&emsp;&emsp; [グローバルnew/deleteのオーバーロード](#SS_5_4_1)  
&emsp;&emsp;&emsp; [デバッグ用イテレータ](#SS_5_4_2)  
&emsp;&emsp;&emsp; [クラスnew/deleteのオーバーロード](#SS_5_4_3)  
&emsp;&emsp;&emsp; [new/deleteのオーバーロードのまとめ](#SS_5_4_4)  

&emsp;&emsp; [標準ライブラリのコンテナ用アロケータ](#SS_5_5)  
&emsp;&emsp;&emsp; [デバッグ用イテレータ](#SS_5_5_1)  
  
  

[インデックス](#SS_1_2)に戻る。  

___

## malloc/freeの問題点 <a id="SS_5_1"></a>
UNIX系のOSでの典型的なmalloc/freeの実装例の一部を以下に示す
(この実装は長いため、
全体は巻末の「[example/dynamic_memory_allocation/malloc_ut.cpp](#SS_9_1_1)」に掲載する)。

```cpp
    //  example/dynamic_memory_allocation/malloc_ut.cpp 19

    namespace {

    struct header_t {
        header_t* next;
        size_t    n_units;  // header_tが何個あるか
    };

    header_t*        header{nullptr};
    SpinLock         spin_lock{};
    constexpr size_t unit_size{sizeof(header_t)};

    inline bool sprit(header_t* header, size_t n_units, header_t*& next) noexcept
    {
        // ...
    }

    inline void concat(header_t* front, header_t* rear) noexcept
    {
        // ...
    }

    header_t* set_back(void* mem) noexcept { return static_cast<header_t*>(mem) - 1; }

    static_assert(sizeof(header_t) == alignof(std::max_align_t));

    void* malloc_inner(size_t size) noexcept
    {
        // ...
    }
    }  // namespace
```
```cpp
    //  example/dynamic_memory_allocation/malloc_ut.cpp 105

    void free(void* mem) noexcept
    {
        header_t* mem_to_free = set_back(mem);

        mem_to_free->next = nullptr;

        auto lock = std::lock_guard{spin_lock};

        if (header == nullptr) {
            header = mem_to_free;
            return;
        }

        if (mem_to_free < header) {
            concat(mem_to_free, header);
            header = mem_to_free;
            return;
        }

        auto curr = header;
        for (; curr->next != nullptr; curr = curr->next) {
            if (mem_to_free < curr->next) {  // 常に curr < mem_to_free
                concat(mem_to_free, curr->next);
                concat(curr, mem_to_free);
                return;
            }
        }

        concat(curr, mem_to_free);
    }

    void* malloc(size_t size) noexcept
    {
        void* mem = malloc_inner(size);

        if (mem == nullptr) {
            auto const add_size = Roundup(unit_size, 1024 * 1024 + size);  // 1MB追加

            header_t* add = static_cast<header_t*>(sbrk(add_size));
            add->n_units  = add_size / unit_size;
            free(++add);
            mem = malloc_inner(size);
        }

        return mem;
    }
```

上記で示したようにmalloc/freeで使用されるメモリはHeader_t型のheaderで管理され、
このアクセスの競合は[スピンロック](#SS_8_12_5)(SpinLock)によって回避される。
headerが管理するメモリ用域からのメモリの切り出しはmalloc_innerによって行われるが、
下のフラグメントの説明でも示す通り、
headerで管理されたメモリは長さの上限が単純には決まらないリスト構造になるため、
このリストをなぞるmalloc/freeにリアルタイム性の保証をすることは困難である。

アプリケーションが実行する最初のmallocから呼び出されるmalloc_innerは、
headerがnullptrであるため必ずnullptrを返すことになる。

上記の抜粋である下記のコードによりmalloc_innerの戻りがnullptrであった場合、sbrkが呼び出される。

```cpp
    //  example/dynamic_memory_allocation/malloc_ut.cpp 148

    if (mem == nullptr) {
        auto const add_size = Roundup(unit_size, 1024 * 1024 + size);  // 1MB追加

        header_t* add = static_cast<header_t*>(sbrk(add_size));
        add->n_units  = add_size / unit_size;
        free(++add);
        mem = malloc_inner(size);
    }
```

sbrkとはOSからメモリを新たに取得するための下記のようなシステムコールである。

```cpp
    //  example/dynamic_memory_allocation/malloc_ut.cpp 13

    extern "C" void* sbrk(ptrdiff_t __incr);
```

OSがアプリケーションに割り当てるための十分なメモリを持っていない場合、
sbrkは
[ページング](https://ja.wikipedia.org/wiki/%E3%83%9A%E3%83%BC%E3%82%B8%E3%83%B3%E3%82%B0%E6%96%B9%E5%BC%8F)
によるメモリ確保のトリガーとなる。
これはOSのファイルシステムの動作を含む処理であるため、やはりリアルタイム性の保証は困難である。

[フリースタンディング環境](#SS_8_12_8)では、sbrkのようなシステムコールは存在しないため、
アプリケーションの未使用領域や静的に確保した領域を上記コードで示したようなリスト構造で管理し、
mallocで使用することになる。
このような環境では、sbrkによるリアルタイム性の阻害は発生しないものの、
メモリ管理ためのリスト構造があるため、やはりリアルタイム性の保証は難しい。

次にもう一つの問題である「メモリのフラグメントを起こす」ことについて見て行く。

```cpp
    //  example/dynamic_memory_allocation/malloc_ut.cpp 190

    void* mem[1024];

    for (auto& m : mem) {  // 32バイト x 1024個のメモリ確保
        m = malloc(32);
    }

    // memを使用した何らかの処理
    // ...

    for (auto i = 0U; i < ArrayLength(mem); i += 2) {  // 512個のメモリを解放
        free(mem[i]);
    }
```

上記のような処理の後、解放されたメモリは、32バイト
(メモリヘッダがあるため、実際はもう少し大きい)の断片が512個ある状態になるため、
このサイズを超える新たなmallocの呼び出しには使えない。
このため、ページングが行えないようなOS上のアプリケーションでは、
メモリは十分にあるにもかかわらずmallocが失敗してしまうことが起こり得る。

また、上記freeの実装例の抜粋である下記のコードからわかるように、
このように断片化されたメモリは、そのアドレス順にソートされた単方向リストによって管理される。

```cpp
    //  example/dynamic_memory_allocation/malloc_ut.cpp 120

    if (mem_to_free < header) {
        concat(mem_to_free, header);
        header = mem_to_free;
        return;
    }

    auto curr = header;
    for (; curr->next != nullptr; curr = curr->next) {
        if (mem_to_free < curr->next) {  // 常に curr < mem_to_free
            concat(mem_to_free, curr->next);
            concat(curr, mem_to_free);
            return;
        }
    }

    concat(curr, mem_to_free);
```

この状態でさらにメモリ解放が行われた場合、
freeはこのリストを辿りメモリを最適な場所に戻す必要がある。
戻したメモリがリスト前後のメモリと隣接していれば、それらは結合される。
この処理は断片化への対策であるが、
ページングの無いOS上のアプリケーションにとっては不十分であるばかりでなく、

* freeの排他ロックする期間が長い
* freeの処理が遅い

といったリアルタイム処理を阻害する別の問題も発生させる
(繰り返しになるが、windows/linuxのような通常のOS上のアプリケーションでは、
このような仕様が問題になることはほとんどない)。

## メモリプール <a id="SS_5_2"></a>
このドキュメントでは、メモリの確保/解放をサポートするサブシステムをメモリプールと呼ぶ。

[malloc/freeの問題点](#SS_5_1)の問題を回避するすために２種類のメモリプールの実装を示す。

* リアルタイム性が保証されれた[固定長メモリプール](#SS_5_2_1)
* フラグメントの状態を確認することができる[可変長メモリプール](#SS_5_2_2)


### 固定長メモリプール <a id="SS_5_2_1"></a>
malloc/freeにリアルタイム性がない原因は、

* リアルタイム性がないOSのシステムコールを使用している
* メモリを可変長で管理しているため処理が重いにもかかわらず、この処理中にグローバルロックを行う

ためである。従って、この問題に対処するためのメモリ管理システムは、

* 初期に静的なメモリを確保
* メモリを固定長で管理(リスト構造でメモリ管理できないため)

する必要がある。

このメモリプールは管理する固定長のメモリブロックのサイズごとに複数必要になる一方で、
これらを統合的に扱う必要も出てくる。

そのため、固定長のメモリプールは、

* 複数個のメモリプールを統合的に扱う[インターフェースクラス](#SS_6_4_11)MPool
* MPoolを基底クラスとし、固定長メモリブロックを管理するクラステンプレートMPoolFixed

によって実装することにする。

まずは、MPoolを下記に示す。なお、throwするオブジェクトの型は[MPoolBadAlloc](#SS_5_3_1)を使用している。

```cpp
    //  example/dynamic_memory_allocation/mpool.h 12

    class MPool {
    public:
        explicit MPool(size_t max_size) : max_size_{max_size} {}

        void* Alloc(size_t size)
        {
            if (size > max_size_) {
                throw MAKE_EXCEPTION(MPoolBadAlloc, "MPF : memory size too big");
            }

            void* mem = alloc(size);

            if (mem == nullptr) {
                throw MAKE_EXCEPTION(MPoolBadAlloc, "MPF : out of memory");
            }

            return mem;
        }

        void* AllocNoExcept(size_t size) noexcept { return alloc(size); }

        void   Free(void* area) noexcept { free(area); }
        size_t GetSize() const noexcept { return get_size(); }           // メモリ最小単位
        size_t GetCount() const noexcept { return get_count(); }         // メモリ最小単位が何個取れるか
        size_t GetCountMin() const noexcept { return get_count_min(); }  // GetCount()の最小値
        bool   IsValid(void const* area) const noexcept { return is_valid(area); }

    protected:
        ~MPool() = default;

    private:
        size_t const max_size_;

        virtual void*  alloc(size_t size) noexcept               = 0;
        virtual void   free(void* area) noexcept                 = 0;
        virtual size_t get_size() const noexcept                 = 0;
        virtual size_t get_count() const noexcept                = 0;
        virtual size_t get_count_min() const noexcept            = 0;
        virtual bool   is_valid(void const* area) const noexcept = 0;
    };
```

次に、MPoolFixedを下記に示す。

```cpp
    //  example/dynamic_memory_allocation/mpool_fixed.h 25

    template <uint32_t MEM_SIZE, uint32_t MEM_COUNT>
    class MPoolFixed final : public MPool {
    public:
        MPoolFixed() noexcept : MPool{mem_chunk_size_} {}

    private:
        using chunk_t = Inner_::mem_chunk<MEM_SIZE>;
        static constexpr size_t mem_chunk_size_{sizeof(chunk_t)};

        size_t           mem_count_{MEM_COUNT};
        size_t           mem_count_min_{MEM_COUNT};
        chunk_t          mem_chunk_[MEM_COUNT]{};
        chunk_t*         mem_head_{setup_mem()};
        mutable SpinLock spin_lock_{};

        chunk_t* setup_mem() noexcept
        {
            for (auto i = 0U; i < MEM_COUNT - 1; ++i) {
                mem_chunk_[i].next = &mem_chunk_[i + 1];
            }

            mem_chunk_[MEM_COUNT - 1].next = nullptr;

            return mem_chunk_;
        }

        virtual void* alloc(size_t size) noexcept override
        {
            assert(size <= mem_chunk_size_);

            auto lock = std::lock_guard{spin_lock_};

            auto mem = mem_head_;

            if (mem != nullptr) {
                mem_head_ = mem_head_->next;
                --mem_count_;
                mem_count_min_ = std::min(mem_count_, mem_count_min_);
            }

            return mem;
        }

        virtual void free(void* mem) noexcept override
        {
            assert(is_valid(mem));

            auto lock = std::lock_guard{spin_lock_};

            chunk_t* curr_head = static_cast<chunk_t*>(mem);
            curr_head->next    = mem_head_;
            mem_head_          = curr_head;

            mem_count_min_ = std::min(++mem_count_, mem_count_min_);
        }

        virtual size_t get_size() const noexcept override { return mem_chunk_size_; }
        virtual size_t get_count() const noexcept override { return mem_count_; }
        virtual size_t get_count_min() const noexcept override { return mem_count_min_; }

        virtual bool is_valid(void const* mem) const noexcept override
        {
            return (&mem_chunk_[0] <= mem) && (mem <= &mem_chunk_[MEM_COUNT - 1]);
        }
    };
```

上記コードからわかる通り、MPoolFixedは初期化直後、
サイズMEM_SIZのメモリブロックをMEM_COUNT個、保持する。
個々のメモリブロックは、下記のコードのalignasでアライメントされた領域となる。

```cpp
    //  example/dynamic_memory_allocation/mpool_fixed.h 11

    constexpr size_t MPoolFixed_MinSize{32};

    namespace Inner_ {
    template <uint32_t MEM_SIZE>
    union mem_chunk {
        mem_chunk* next;

        // MPoolFixed_MinSizeの整数倍のエリアを、最大アラインメントが必要な基本型にアライン
        alignas(std::max_align_t) uint8_t mem[Roundup(MPoolFixed_MinSize, MEM_SIZE)];
    };
    }  // namespace Inner_
```

MPoolFixedに限らずメモリアロケータが返すメモリは、
どのようなアライメントにも対応できなければならないため、このようにする必要がある。

MPoolFixed::alloc/MPoolFixed::freeを見ればわかる通り、malloc/freeの実装に比べ格段にシンプルであり、
これによりリアルタイム性の保障は容易である。

なお、この実装ではmalloc/freeと同様に使用制限の少ない[スピンロック](#SS_8_12_5)(SpinLock)を使用したが、
このロックは、ラウンドロビンでスケジューリングされるスレッドの競合を防ぐためのものであり、
固定プライオリティでのスケジューリングが前提となるような組み込みソフトで使用した場合、
デッドロックを引き起こす可能性がある。
組み込みソフトでは、割り込みディセーブル/イネーブルを使ってロックすることを推奨する。

MPoolFixedの単体テストは、下記のようになる。

```cpp
    //  example/dynamic_memory_allocation/mpool_fixed_ut.cpp 10

    Inner_::mem_chunk<5> mc5[3];
    static_assert(32 == sizeof(mc5[0]));
    static_assert(96 == sizeof(mc5));

    auto mc33 = Inner_::mem_chunk<33>{};
    static_assert(64 == sizeof(mc33));
```
```cpp
    //  example/dynamic_memory_allocation/mpool_fixed_ut.cpp 106

    auto mpf = MPoolFixed<33, 2>{};

    ASSERT_EQ(64, mpf.GetSize());
    ASSERT_EQ(2, mpf.GetCount());
    ASSERT_EQ(2, mpf.GetCountMin());
    ASSERT_FALSE(mpf.IsValid(&mpf));  // mpfの管理外のアドレス

    auto m0 = mpf.Alloc(1);
    ASSERT_TRUE(mpf.IsValid(m0));  // mpfの管理のアドレス
    ASSERT_NE(nullptr, m0);
    ASSERT_EQ(1, mpf.GetCount());
    ASSERT_EQ(1, mpf.GetCountMin());

    auto m1 = mpf.Alloc(1);
    ASSERT_TRUE(mpf.IsValid(m1));  // mpfの管理のアドレス
    ASSERT_NE(nullptr, m1);
    ASSERT_EQ(0, mpf.GetCount());
    ASSERT_EQ(0, mpf.GetCountMin());

    // mpfが空の場合のテスト
    ASSERT_THROW(mpf.Alloc(1), MPoolBadAlloc);  // MPoolBadAlloc例外が発生するはず
    auto m2 = mpf.AllocNoExcept(1);
    ASSERT_EQ(nullptr, m2);
    ASSERT_EQ(0, mpf.GetCount());

    mpf.Free(m0);
    ASSERT_EQ(1, mpf.GetCount());
    ASSERT_EQ(0, mpf.GetCountMin());

    mpf.Free(m1);
    ASSERT_EQ(2, mpf.GetCount());
    ASSERT_EQ(0, mpf.GetCountMin());

    ASSERT_THROW(mpf.Alloc(65), MPoolBadAlloc);  // MPoolBadAlloc例外が発生するはず
```

### 可変長メモリプール <a id="SS_5_2_2"></a>
可変長メモリプールを生成するMPoolVariableの実装は下記のようになる
(全体は巻末の「[example/dynamic_memory_allocation/mpool_variable.h](#SS_9_1_2)」に掲載する)。

```cpp
    //  example/dynamic_memory_allocation/mpool_variable.h 59

    template <uint32_t MEM_SIZE>
    class MPoolVariable final : public MPool {
    public:
        MPoolVariable() noexcept : MPool{MEM_SIZE}
        {
            header_->next    = nullptr;
            header_->n_units = sizeof(buff_) / Inner_::unit_size;
        }

        class const_iterator {
        public:
            explicit const_iterator(Inner_::header_t const* header) noexcept : header_{header} {}
            const_iterator(const_iterator const&) = default;
            const_iterator(const_iterator&&)      = default;

            const_iterator& operator++() noexcept  // 前置++のみ実装
            {
                assert(header_ != nullptr);
                header_ = header_->next;

                return *this;
            }

            Inner_::header_t const* operator*() noexcept { return header_; }


        #if __cplusplus <= 201703L  // c++17
            bool operator==(const_iterator const& rhs) noexcept { return header_ == rhs.header_; }
            bool operator!=(const_iterator const& rhs) noexcept { return !(*this == rhs); }
        #else  // c++20

            auto operator<=>(const const_iterator&) const = default;
        #endif

        private:
            Inner_::header_t const* header_;
        };

        const_iterator begin() const noexcept { return const_iterator{header_}; }
        const_iterator end() const noexcept { return const_iterator{nullptr}; }
        const_iterator cbegin() const noexcept { return const_iterator{header_}; }
        const_iterator cend() const noexcept { return const_iterator{nullptr}; }

    private:
        using header_t = Inner_::header_t;

        Inner_::buffer_t<MEM_SIZE> buff_{};
        header_t*                  header_{reinterpret_cast<header_t*>(buff_.buffer)};
        mutable SpinLock           spin_lock_{};
        size_t                     unit_count_{sizeof(buff_) / Inner_::unit_size};
        size_t                     unit_count_min_{sizeof(buff_) / Inner_::unit_size};

        virtual void* alloc(size_t size) noexcept override
        {
            // ...
        }

        virtual void free(void* mem) noexcept override
        {
            // ...
        }

        virtual size_t get_size() const noexcept override { return 1; }
        virtual size_t get_count() const noexcept override { return unit_count_ * Inner_::unit_size; }
        virtual size_t get_count_min() const noexcept override { return unit_count_min_ * Inner_::unit_size; }

        virtual bool is_valid(void const* mem) const noexcept override
        {
            return (&buff_ < mem) && (mem < &buff_.buffer[ArrayLength(buff_.buffer)]);
        }
    };
```

上記の抜粋である下記のイテレータにより、このメモリプールの状態を見ることができる。

```cpp
    //  example/dynamic_memory_allocation/mpool_variable.h 72

    class const_iterator {
    public:
        explicit const_iterator(Inner_::header_t const* header) noexcept : header_{header} {}
        const_iterator(const_iterator const&) = default;
        const_iterator(const_iterator&&)      = default;

        const_iterator& operator++() noexcept  // 前置++のみ実装
        {
            assert(header_ != nullptr);
            header_ = header_->next;

            return *this;
        }

        Inner_::header_t const* operator*() noexcept { return header_; }


    #if __cplusplus <= 201703L  // c++17
        bool operator==(const_iterator const& rhs) noexcept { return header_ == rhs.header_; }
        bool operator!=(const_iterator const& rhs) noexcept { return !(*this == rhs); }
    #else  // c++20

        auto operator<=>(const const_iterator&) const = default;
    #endif

    private:
        Inner_::header_t const* header_;
    };

    const_iterator begin() const noexcept { return const_iterator{header_}; }
    const_iterator end() const noexcept { return const_iterator{nullptr}; }
    const_iterator cbegin() const noexcept { return const_iterator{header_}; }
    const_iterator cend() const noexcept { return const_iterator{nullptr}; }
```

可変長メモリプールとイテレータの使用例を下記に示す。

```cpp
    //  example/dynamic_memory_allocation/mpool_variable_ut.cpp 322

    MPoolVariable<1024 * 64> mpv;  // 可変長メモリプール

    constexpr size_t alloc_cout = 100U;
    void*            mem[alloc_cout]{};

    for (size_t i = 0; i < alloc_cout; ++i) {
        mem[i] = mpv.Alloc(i + 100);
    }
```
上記のような使用ではフラグメントは発生しないが、下記によりそのことを見てみよう。

```cpp
    //  example/dynamic_memory_allocation/mpool_variable_ut.cpp 333

    std::cout << "mpv:" << __LINE__ << std::endl;
    for (auto itor = mpv.cbegin(); itor != mpv.cend(); ++itor) {
        std::cout << std::setw(16) << (*itor)->next << ":" << (*itor)->n_units << std::endl;
    }
```

この結果は、下記のように出力される(後に示すが、mpvが保持しているメモリが１つの塊のままであり、
フラグメントを起こしていないことを示している)。

```
mpv:238
               0:3014
```

敢えてフラグメントを起こすために、以下のようなコードを実行する。

```cpp
    //  example/dynamic_memory_allocation/mpool_variable_ut.cpp 340

    for (size_t i = 0; i < alloc_cout; ++i) {
        if (i % 2 == 0) {  // 偶数だけ解放
            mpv.Free(mem[i]);
        }
    }

    std::cout << "mpv:" << __LINE__ << std::endl;
    for (auto itor = mpv.cbegin(); itor != mpv.cend(); ++itor) {
        std::cout << std::setw(16) << (*itor)->next << ":" << (*itor)->n_units << std::endl;
    }
```

この結果、以下のような出力が得られる。これはmpvにはまだメモリが残されているものの、
mpvが保持しているメモリの先頭付近がフラグメントを起こしていることを示している。

```
mpv:249
  0x7ffdeca0b4a0:8            
  0x7ffdeca0b5a0:8
  0x7ffdeca0b6a0:8
  0x7ffdeca0b7a0:8
  0x7ffdeca0b8a0:8
  ... 省略
               0:3014     <- アロケーションされていないメモリの塊
```

## メモリプールのエクセプション <a id="SS_5_3"></a>
メモリプール内で回復不可能なエラーが発生した場合、
エクセプションの送出によりそのことを使用側にそれを伝えなければならない。

多くのコンパイラのエクセプション処理機構にはmalloc/freeが使われているため、
メモリプールの実装に通常の例外を使用した場合、メモリプールの開発趣旨に反する。


ここでは、

- エクセプション用の型[MPoolBadAlloc](#SS_5_3_1)の開発
- [エクセプション処理機構の変更](#SS_5_3_2)

を通じて、メモリプールのエクセプション機構を紹介する。

### MPoolBadAlloc <a id="SS_5_3_1"></a>
MPoolBadAllocは下記のように定義されたクラスであり、
「[ファイル位置を静的に保持したエクセプションクラスの開発](#SS_4_7_6_4)」
で示したのクラスライブラリ基づいたメモリプール専用のエクセプション型である。

```cpp
    //  example/h/nstd_exception.h 11

    /// @class Exception
    /// @brief StaticString<>を使ったエクセプションクラス
    ///        下記のMAKE_EXCEPTIONを使い生成
    /// @tparam E   std::exceptionから派生したエクセプションクラス
    /// @tparam N   StaticString<N>
    template <typename E, size_t N>
    #if __cplusplus >= 202002L  // c++20
    requires std::derived_from<E, std::exception>
    #endif
    class Exception : public E {
    public:
        static_assert(std::is_base_of_v<std::exception, E>);

        Exception(StaticString<N> const& what_str) noexcept : what_str_{what_str} {}
        char const* what() const noexcept override { return what_str_.String(); }

    private:
        StaticString<N> const what_str_;
    };

    #define MAKE_EXCEPTION(E__, msg__) Nstd::MakeException<E__, __LINE__>(__FILE__, msg__)
```
```cpp
    //  example/dynamic_memory_allocation/mpool.h 7

    class MPoolBadAlloc : public std::bad_alloc {  // Nstd::Exceptionの基底クラス
    };
```

MPoolから派生したクラスが、

* メモリブロックを保持していない状態でのMPool::alloc(size, true)の呼び出し
* MEM_SIZEを超えたsizeでのMPool::alloc(size, true)の呼び出し

のような処理の継続ができない場合に用いるエクセプション専用クラスである。


### エクセプション処理機構の変更 <a id="SS_5_3_2"></a>
多くのコンパイラのエクセプション処理機構にはnew/deleteやmalloc/freeが使われているため、
リアルタイム性が必要な個所でエクセプション処理を行ってはならない。
そういった規制でプログラミングを行っていると、
リアルタイム性が不要な処理であるため使用しているstdコンテナにすら、
既存のエクセプション処理機構を使わせたく無くなるものである。

コンパイラに[g++](#SS_8_13_1)や[clang++](#SS_8_13_2)を使っている場合、
下記関数を置き換えることでそういった要望を叶えることができる。

|関数                                           |機能                            |
|-----------------------------------------------|--------------------------------|
|`__cxa_allocate_exception(size_t thrown_size)` |エクセプション処理用のメモリ確保|
|`__cxa_free_exception(void\* thrown_exception)`|上記で確保したメモリの解放      |

オープンソースである[static exception](https://github.com/ApexAI/static_exception)を使うことで、
上記2関数を置き換えることもできるが、この実装が複雑すぎると思うのであれば、
下記に示すような、これまで使用したMPoolFixedによる単純な実装を使うこともできる。

```cpp
    //  example/dynamic_memory_allocation/exception_allocator_ut.cpp 15

    // https://github.com/hjl-tools/gcc/blob/master/libstdc%2B%2B-v3/libsupc%2B%2B/unwind-cxx.h
    // の抜粋
    namespace __cxxabiv1 {
    struct __cxa_exception {
        // ...
    };
    SUPPRESS_WARN_END;
    }  // namespace __cxxabiv1

    namespace {

    constexpr size_t             offset{sizeof(__cxxabiv1::__cxa_exception)};
    MPoolFixed<offset + 128, 50> mpf_exception;
    }  // namespace

    extern "C" {

    void* __cxa_allocate_exception(size_t thrown_size)
    {
        auto alloc_size = thrown_size + offset;  // メモリの実際の必要量はthrown_size+offset
        auto mem        = mpf_exception.AllocNoExcept(alloc_size);

        assert(mem != nullptr);

        memset(mem, 0, alloc_size);
        auto* ret = static_cast<uint8_t*>(mem);

        ret += offset;

        return ret;
    }

    void __cxa_free_exception(void* thrown_exception)
    {
        auto* ret = static_cast<uint8_t*>(thrown_exception);

        ret -= offset;
        mpf_exception.Free(ret);
    }
```

以下に単体テストを示す。

```cpp
    //  example/dynamic_memory_allocation/exception_allocator_ut.cpp 104

    auto count             = mpf_exception.GetCount();
    auto exception_occured = false;

    try {
        throw std::exception{};
    }
    catch (std::exception const& e) {
        ASSERT_EQ(count - 1, mpf_exception.GetCount());  // 1個消費
        exception_occured = true;
    }

    ASSERT_TRUE(exception_occured);
    ASSERT_EQ(count, mpf_exception.GetCount());  // 1個解放
```

すでに述べたが、残念なことに、この方法はC++の標準外であるため、
これを適用できるコンパイラは限られている。
しかし、多くのコンパイラはこれと同様の拡張方法を備えているため、
安易にエクセプションや標準ライブラリのコンテナを使用禁止することなく、安全に使用する方法を探るべきだろう。


## new/deleteのオーバーロード <a id="SS_5_4"></a>
前述したように、組み込みソフトにはmalloc/freeを使用したnew/deleteではシステムの制限を満たせないことが多い。
C++11では、以下のような方法により、このような問題を回避することができる。

* [グローバルnew/deleteのオーバーロード](#SS_5_4_1)
* [クラスnew/deleteのオーバーロード](#SS_5_4_3)



### グローバルnew/deleteのオーバーロード <a id="SS_5_4_1"></a>
[固定長メモリプール](#SS_5_2_1)を使用した`operator new`のオーバーロードの実装例を以下に示す。

```cpp
    //  example/dynamic_memory_allocation/global_new_delete.cpp 31

    namespace {

    MPool* mpool_table[32];

    // mainの前に呼ばれるため、mpool_tableを初期化するには下記のような方法が必要
    bool is_setup{false};

    void setup() noexcept
    {
        is_setup = true;

        mpool_table[0] = gen_mpool<1, 128>();  //   32
        mpool_table[1] = gen_mpool<2, 128>();  //   64
        mpool_table[2] = gen_mpool<3, 128>();  //   96

        // ...

        mpool_table[29] = gen_mpool<30, 128>();  //  960
        mpool_table[30] = gen_mpool<31, 128>();  //  992
        mpool_table[31] = gen_mpool<32, 128>();  // 1024
    }

    size_t size2index(size_t v) noexcept { return (((v + (min_unit - 1)) & ~(min_unit - 1)) / min_unit) - 1; }
    }  // namespace

    [[nodiscard]] void* operator new(std::size_t size)
    {
        if (!is_setup) {
            setup();
        }

        for (auto i = size2index(size); i < ArrayLength(mpool_table); ++i) {
            void* mem = mpool_table[i]->AllocNoExcept(size);
            if (mem != nullptr) {
                return mem;
            }
        }

        throw std::bad_alloc{};

        static char fake;

        return &fake;
    }
```

上記で定義された`operator new`は、

* 32の整数倍のサイズを持つ32個のメモリプールを持つ
* 各メモリープールは128個のメモリブロックを持つ
* メモリブロックの最大長は1024バイト

のような仕様を持つため、実際に使う場合は、メモリのサイズや個数の調整が必要だろうが、
後で詳しく見るようにリアルタイム性の阻害となるようなコードはないため、
リアルタイム性が必要なソフトウェアでも使用可能である。

静的オブジェクトを含まないアプリケーションでは、
上記のコードのsetupで行っているmpool_tableの初期化は
[一様初期化](#SS_6_6_6)で行った方が良いが、
例で用いたアプリケーションにはnewを行う静的オブジェクトが存在するため
(google testは静的オブジェクトを利用する)、
setupで行っているような方法以外では、
最初の`operator new`の呼び出しより前にmpool_tableの初期化をすることはできない。

mpool_tableはMPoolポインタを保持するが、そのポインタが指すオブジェクトの実態は、
gen_mpool<>が生成したMPoolFixed<>オブジェクトである。
gen_mpool<>については、その内部に静的に確保したメモリを使用して、
[プレースメントnew](#SS_6_6_9)によりMPoolオブジェクトを生成する下記の関数テンプレートである。

```cpp
    //  example/dynamic_memory_allocation/global_new_delete.cpp 8

    namespace {

    constexpr size_t min_unit{MPoolFixed_MinSize};

    template <uint32_t N_UNITS, uint32_t MEM_COUNT>
    [[nodiscard]] MPool* gen_mpool() noexcept
    {
        using mp_t = MPoolFixed<min_unit * N_UNITS, MEM_COUNT>;

        static union {
            std::max_align_t max_align;
            uint8_t          mem[sizeof(mp_t)];
        } mem;

        static_assert(static_cast<void*>(&mem.max_align) == static_cast<void*>(mem.mem));
        static_assert(sizeof(mem) >= sizeof(mp_t));

        return new (mem.mem) mp_t;  // プレースメントnew
    }
    }  // namespace
```


この実装では対応するMPoolが空であった場合、
それよりも大きいメモリブロックを持つMPoolからメモリを返す仕様としたが、
その時点でアサーションフェールさせ
(つまり、対応するMPoolが空である状態でのAllocの呼び出しをバグとして扱う)、
MEM_COUNTの値を見直した方が、
より少ないメモリで動作する組み込みソフトを作りやすいだろう。

`operator delete`については、下記の2種類が必要となる。

size2indexは要求されたサイズから、
それに対応するMPoolポインタを保持するmpool_tableのインデックスを導出する関数である。

```cpp
    //  example/dynamic_memory_allocation/global_new_delete.cpp 111

    void operator delete(void* mem) noexcept
    {
        for (MPool* mp : mpool_table) {
            if (mp->IsValid(mem)) {
                mp->Free(mem);
                return;
            }
        }
        assert(false);
    }

    void operator delete(void* mem, std::size_t size) noexcept
    {
        for (auto i = size2index(size); i < ArrayLength(mpool_table); ++i) {
            if (mpool_table[i]->IsValid(mem)) {
                mpool_table[i]->Free(mem);
                return;
            }
        }
        assert(false);
    }
```

`operator delete(void* mem, std::size_t size)`は、完全型のオブジェクトのメモリ解放に使用され、
`operator delete(void* mem)`は、それ以外のメモリ解放に使用される。

コードから明らかな通り、size付きの`operator delete`の方がループの回転数が少なくなるため、
高速に動作するが、malloc/freeの実装(「[malloc/freeの問題点](#SS_5_1)」参照)で使用したHeader_t
を導入することでこの実行コストはほとんど排除できる。
そのトレードオフとしてメモリコストが増えるため、ここでは例示した仕様にした。

### デバッグ用イテレータ <a id="SS_5_4_2"></a>
[グローバルnew/deleteのオーバーロード](#SS_5_4_1)で示したグローバルnew/deleteの実装は、適切なメモリの量を調整する必要がある。
そのためには、これを使用するアプリケーションをある程度動作させた後、
グローバルnew/deleteのメモリの消費量を計測しなければならない。

下記のコードは、そのためのインターフェースを提供する。

```cpp
    //  example/dynamic_memory_allocation/global_new_delete.h 4

    class GlobalNewDeleteMonitor {
    public:
        MPool const* const* cbegin() const noexcept;
        MPool const* const* cend() const noexcept;
        MPool const* const* begin() const noexcept;
        MPool const* const* end() const noexcept;
    };
```
```cpp
    //  example/dynamic_memory_allocation/global_new_delete.cpp 35

    MPool* mpool_table[32];
```
```cpp
    //  example/dynamic_memory_allocation/global_new_delete.cpp 137

    MPool const* const* GlobalNewDeleteMonitor::begin() const noexcept { return &mpool_table[0]; }
    MPool const* const* GlobalNewDeleteMonitor::end() const noexcept { return &mpool_table[ArrayLength(mpool_table)]; }

    MPool const* const* GlobalNewDeleteMonitor::cbegin() const noexcept { return begin(); }
    MPool const* const* GlobalNewDeleteMonitor::cend() const noexcept { return end(); }
```

このインターフェースを下記のように使用することで、

```cpp
    //  example/dynamic_memory_allocation/global_new_delete_ut.cpp 119

    auto gm = GlobalNewDeleteMonitor{};

    std::cout << "  size current   min" << std::endl;
    std::cout << "  ------------------" << std::endl;

    for (MPool const* mp : gm) {
        std::cout << std::setw(6) << mp->GetSize() << std::setw(8) << mp->GetCount() << std::setw(6)
                  << mp->GetCountMin() << std::endl;
    }
```

下記のようにメモリの現在の状態や使用履歴を見ることができる。

```
          size current   min
          ------------------
            32      90     0
            64      78    74
            96     127   125

           ...

           992     128   128
          1024     128     0
```

実際の組み込みソフトの開発では、
デバッグ用入出力機能からこのようなコードを実行できるようにすることで、
グローバルnew/deleteが使用するそれぞれのMPoolFixedインスタンスのメモリの調整ができるだろう。



### クラスnew/deleteのオーバーロード <a id="SS_5_4_3"></a>
「[グローバルnew/deleteのオーバーロード](#SS_5_4_1)」で示したコードのロックを、
「割り込みディセーブル/イネーブル」に置き換えることで、リアルタイム性を保障することができるが、
この機構はある程度多くのメモリを必要とするため、
極めてメモリ制限の厳しいシステムでは使用が困難である場合もあるだろう。

そのような場合、非スタック上でのオブジェクト生成には、

* 限定的なクラスのみ、newによる動的な方法を用いる
* その他のクラスに対しては、[Singleton](#SS_3_1_1)や[Named Constructor](#SS_3_1_2)と同様な静的な方法を用いる

とし、グローバルnewを使用しないことが、より良いメモリ使用方法となり得る。

グローバルnewを使わずに動的にオブジェクトを生成するためには、

* [プレースメントnew](#SS_6_6_9)を使う
* クラス毎にnew/deleteをオーバーロードする

という2つの選択肢が考えられるが、プレースメントnewは見慣れないシンタックスを用いるため、これの使用は避けるべきである。
従って、その方法はクラス毎のnew/deleteのオーバーロードになる。

メモリ管理に「[固定長メモリプール](#SS_5_2_1)」で示したMPoolFixedを利用した実装例を以下に示す。

```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 14

    struct A {
        A() noexcept : name0{"A"} {}
        char const* name0;

        [[nodiscard]] static void* operator new(size_t size);
        static void                operator delete(void* mem) noexcept;
        static void                operator delete(void* mem, std::size_t size) noexcept;

        [[nodiscard]] static void* operator new[](size_t size)                             = delete;
        static void                operator delete[](void* mem) noexcept                   = delete;
        static void                operator delete[](void* mem, std::size_t size) noexcept = delete;
    };

    MPoolFixed<sizeof(A), 3> mpf_A;

    void* A::operator new(size_t size) { return mpf_A.Alloc(size); }
    void A::operator delete(void* mem) noexcept { mpf_A.Free(mem); }
    void A::operator delete(void* mem, std::size_t) noexcept { mpf_A.Free(mem); }
```

以下の単体テストが示す通り、
静的に定義したMPoolFixedインスタンスがオーバーロードしたnew/deleteから使われていることがわかる
(従ってグローバルnew/deleteは使われていないこともわかる)。

```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 43

    ASSERT_EQ(3, mpf_A.GetCount());

    {
        auto a = std::make_unique<A>();
        ASSERT_STREQ("A", a->name0);
        ASSERT_EQ(2, mpf_A.GetCount());
    }
    ASSERT_EQ(3, mpf_A.GetCount());

    {
        auto a = std::make_unique<A>();
        ASSERT_STREQ("A", a->name0);
        ASSERT_EQ(2, mpf_A.GetCount());

        auto b = std::make_unique<A>();
        ASSERT_STREQ("A", b->name0);
        ASSERT_EQ(1, mpf_A.GetCount());

        auto c = std::make_unique<A>();
        ASSERT_STREQ("A", c->name0);
        ASSERT_EQ(0, mpf_A.GetCount());

        ASSERT_THROW(std::make_unique<A>(), MPoolBadAlloc);
    }
    ASSERT_EQ(3, mpf_A.GetCount());
```

しかし、この方法ではnewのオーバーロードを行うクラス毎に、

```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 20

    [[nodiscard]] static void* operator new(size_t size);
    static void                operator delete(void* mem) noexcept;
    static void                operator delete(void* mem, std::size_t size) noexcept;

    [[nodiscard]] static void* operator new[](size_t size)                             = delete;
    static void                operator delete[](void* mem) noexcept                   = delete;
    static void                operator delete[](void* mem, std::size_t size) noexcept = delete;
```

を記述しなければならず、コードクローンの温床となってしまう。
これを避けるためには、
[CRTP(curiously recurring template pattern)](#SS_8_1_4)
を利用した下記のようなクラステンプレートを導入すれば良い。

```cpp
    //  example/dynamic_memory_allocation/op_new.h 5

    template <typename T>
    class OpNew {
    public:
        [[nodiscard]] static void* operator new(size_t size) { return mpool_.Alloc(size); }
        static void                operator delete(void* mem) noexcept { mpool_.Free(mem); }
        static void                operator delete(void* mem, std::size_t) noexcept { mpool_.Free(mem); }

        [[nodiscard]] static void* operator new[](size_t size)                             = delete;
        static void                operator delete[](void* mem) noexcept                   = delete;
        static void                operator delete[](void* mem, std::size_t size) noexcept = delete;

    private:
        static MPool& mpool_;
    };
```

このOpeNewを使用した「new/deleteのオーバーロードを持つ基底クラスとその一連の派生クラス」
の実装例を以下に示す。

```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 77

    struct A : public OpNew<A> {
        A() noexcept : name0{"A"} {}
        char const* name0;
    };

    struct B : A {
        B() noexcept : name1{"B"} {}
        char const* name1;
    };

    struct C : A {
        C() noexcept : name1{"C"} {}
        char const* name1;
    };

    struct D : C {
        D() noexcept : name2{"D"} {}
        char const* name2;
    };

    MPoolFixed<MaxSizeof<A, B, C, D>(), 10> mpf_ABCD;

    template <>
    MPool& OpNew<A>::mpool_ = mpf_ABCD;
```

OpNewをクラステンプレートとし、内部で利用しないテンプレートパラメータを宣言した理由は、
別のクラスからはOpNewの別インスタンスを使用できるようにするためである。

この方法は、コードが若干複雑にることを除けば、
「[グローバルnew/deleteのオーバーロード](#SS_5_4_1)」に比べ、優れているように見えてしまうかもしれないが、
下記のように、さらに派生クラスを定義してしまうとnewが失敗してしまうことがあるので注意が必要である。

```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 135

    struct Large : A {
        uint8_t buff[1024];  // mpf_ABCDのメモリブロックのサイズを超える
    };
```
```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 144

    ASSERT_EQ(10, mpf_ABCD.GetCount());
    ASSERT_THROW(auto large = std::make_unique<Large>(), MPoolBadAlloc);  // サイズが大きすぎる
```

なお、 下記のようなクラスをnew/deleteをオーバーロードしないすべのクラスの基底クラスとすることで、
偶発的にグローバルnewを使ってしまわないようにすることもできる。

```cpp
    //  example/dynamic_memory_allocation/op_new_deleted.h 3

    class OpNewDeleted {
        static void* operator new(size_t size)                             = delete;
        static void  operator delete(void* mem) noexcept                   = delete;
        static void  operator delete(void* mem, std::size_t size) noexcept = delete;
    };
```
```cpp
    //  example/dynamic_memory_allocation/class_new_delete_ut.cpp 153

    class DeletedNew : OpNewDeleted {  // プライベート継承
    };

    class DelivedDeletedNew : DeletedNew {  // プライベート継承
    };

    // DeletedNew* ptr0 { new DeletedNew };                // OpNewDeletedの効果でコンパイルエラー
    // DelivedDeletedNew* ptr1 { new DelivedDeletedNew };  // 同上
```

この記述方法は、コードインスペクションの省力化にも繋がるため、
OpNewを使うプロジェクトには導入するべきだろう。


### new/deleteのオーバーロードのまとめ <a id="SS_5_4_4"></a>
ここまで、malloc/freeの問題の様々な回避方法を示したのでその組み合わせをまとめる。

1. リアルタイムパスでのオブジェクトの生成/解放を行う必要があるクラスのnew/deleteのオーバーロードを
  [固定長メモリプール](#SS_5_2_1)により実装する。
2. グローバルnew/deleteのオーバーロードを[可変長メモリプール](#SS_5_2_2)により実装する。

上記1によりリアルタイム性の問題は発生しない。
2により、フラグメントの状態を調査できるようになる。
ここではデバッグイテレータの実装を行っていないが、
[デバッグ用イテレータ](#SS_5_5_1)の実装例が参考になるだろう。


## 標準ライブラリのコンテナ用アロケータ <a id="SS_5_5"></a>
アロケータの定義例を以下に示す。

```cpp
    //  example/dynamic_memory_allocation/mpool_allocator.h 7

    template <typename T>
    class MPoolBasedAllocator {
    public:
        using pointer                                = T*;
        using const_pointer                          = T const*;
        using value_type                             = T;
        using propagate_on_container_move_assignment = std::true_type;
        using is_always_equal                        = std::true_type;
        using size_type                              = size_t;
        using difference_type                        = size_t;

        template <class U>
        struct rebind {
            using other = MPoolBasedAllocator<U>;
        };

        T*   allocate(size_type count) { return static_cast<pointer>(mpool_.Alloc(count * sizeof(T))); }
        void deallocate(T* mem, size_type) noexcept { mpool_.Free(mem); }

    private:
        static MPool& mpool_;
    };

    template <class T>  // T型のMPoolBasedAllocatorはシステムに唯一
    bool operator==(MPoolBasedAllocator<T> const&, MPoolBasedAllocator<T> const&) noexcept
    {
        return true;
    }

    template <class T, class U>
    bool operator==(MPoolBasedAllocator<T> const&, MPoolBasedAllocator<U> const&) noexcept
    {
        return false;
    }

    template <class T, class U>
    bool operator!=(MPoolBasedAllocator<T> const& lhs, MPoolBasedAllocator<U> const& rhs) noexcept
    {
        return !(lhs == rhs);
    }
```

アロケータのパブリックなメンバやoperator ==、operator !=は、標準ライブラリに従い定義している
([標準ライブラリのallocator](https://cpprefjp.github.io/reference/memory/allocator.html)参照)。

上記コードからわかるようにメモリの実際のアロケーションには、
これまでと同様にMPoolから派生したクラスを使用するが、
リアルタイム性は不要であるためメモリ効率が悪いMPoolFixedは使わない。
代わりに、可変長メモリを扱うためメモリ効率がよいMPoolVariabl
(「[可変長メモリプール](#SS_5_2_2)」参照)を使う。

C++14の環境で標準ライブラリのアロケータを置き換える場合は、上記のような方法で実現できるが、
C++17以降では、[std::pmr::polymorphic_allocator](#SS_7_6_2)を使用するべきである。

### デバッグ用イテレータ <a id="SS_5_5_1"></a>
[可変長メモリプール](#SS_5_2_2)を使用すると、
メモリのフラグメントによりアロケーションが失敗することがあり得る。
このような事態が発生している可能性がある場合、
アロケータが保持しているメモリの状態を表示させることがデバッグの第一歩となる。

下記のコードは、そのためのインターフェースを提供する。


```cpp
    //  example/dynamic_memory_allocation/mpool_variable.h 59

    template <uint32_t MEM_SIZE>
    class MPoolVariable final : public MPool {
    public:

        // 中略
        ...

        class const_iterator {
        public:
            explicit const_iterator(Inner_::header_t const* header) noexcept : header_{header} {}
            const_iterator(const_iterator const&) = default;
            const_iterator(const_iterator&&)      = default;

            const_iterator& operator++() noexcept  // 前置++のみ実装
            {
                assert(header_ != nullptr);
                header_ = header_->next;

                return *this;
            }

            Inner_::header_t const* operator*() noexcept { return header_; }


        #if __cplusplus <= 201703L  // c++17
            bool operator==(const_iterator const& rhs) noexcept { return header_ == rhs.header_; }
            bool operator!=(const_iterator const& rhs) noexcept { return !(*this == rhs); }
        #else  // c++20

            auto operator<=>(const const_iterator&) const = default;
        #endif

        private:
            Inner_::header_t const* header_;
        };

        const_iterator begin() const noexcept { return const_iterator{header_}; }
        const_iterator end() const noexcept { return const_iterator{nullptr}; }
        const_iterator cbegin() const noexcept { return const_iterator{header_}; }
        const_iterator cend() const noexcept { return const_iterator{nullptr}; }

        // 中略
        ...
    };
```

このインターフェースを下記のように使用することで、

```cpp
    //  example/dynamic_memory_allocation/mpool_variable_ut.cpp 322

    MPoolVariable<1024 * 64> mpv;  // 可変長メモリプール

    constexpr size_t alloc_cout = 100U;
    void*            mem[alloc_cout]{};

    for (size_t i = 0; i < alloc_cout; ++i) {
        mem[i] = mpv.Alloc(i + 100);
    }
```

下記のようにmpv_allocator.header\_が保持するメモリの現在の状態を見ることができる
(これによるとmpv_allocatorが保持するメモリの先頭付近では多少フラグメントを起こしているが、
最後に大きなメモリブロックがあるため、全体としては問題ないレベルである)。

```
        0x7f073afe59d0:3
        0x7f073afe5a60:3
        0x7f073afe5ac0:3
        0x7f073afe5b70:3
        0x7f073afe5c50:11
        0x7f073afe5cb0:3
        0x7f073afe5e50:13
                     0:4018
```

「[グローバルnew/deleteのオーバーロード](#SS_5_4_1)」でも述べたように、
デバッグ用入出力機能からこのような出力を得られるようにしておくべきである。




<!-- essential/md/core_lang_spec.md -->
# C++コア言語仕様 <a id="SS_6"></a>
この章では、C++コア言語仕様について説明する。

___

__この章の構成__

&emsp;&emsp; [型システムと算術の基礎](#SS_6_1)  
&emsp;&emsp;&emsp; [基本型](#SS_6_1_1)  
&emsp;&emsp;&emsp; [組み込み型](#SS_6_1_2)  
&emsp;&emsp;&emsp; [算術型](#SS_6_1_3)  
&emsp;&emsp;&emsp; [汎整数型](#SS_6_1_4)  
&emsp;&emsp;&emsp; [整数型](#SS_6_1_5)  
&emsp;&emsp;&emsp;&emsp; [ビットシフトにおける未定義動作](#SS_6_1_5_1)  

&emsp;&emsp;&emsp; [算術変換](#SS_6_1_6)  
&emsp;&emsp;&emsp; [汎整数型昇格](#SS_6_1_7)  
&emsp;&emsp;&emsp; [汎整数型拡張](#SS_6_1_8)  
&emsp;&emsp;&emsp; [浮動小数点型昇格](#SS_6_1_9)  
&emsp;&emsp;&emsp; [デフォルト引数昇格](#SS_6_1_10)  
&emsp;&emsp;&emsp; [縮小型変換](#SS_6_1_11)  
&emsp;&emsp;&emsp; [浮動小数点型](#SS_6_1_12)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点型のダイナミックレンジ](#SS_6_1_12_1)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点の誤差](#SS_6_1_12_2)  
&emsp;&emsp;&emsp;&emsp; [イプシロン](#SS_6_1_12_3)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点の演算エラー](#SS_6_1_12_4)  

&emsp;&emsp; [リテラル](#SS_6_2)  
&emsp;&emsp;&emsp; [生文字列リテラル](#SS_6_2_1)  
&emsp;&emsp;&emsp; [2進数リテラル](#SS_6_2_2)  
&emsp;&emsp;&emsp; [数値リテラル](#SS_6_2_3)  
&emsp;&emsp;&emsp; [ワイド文字列](#SS_6_2_4)  
&emsp;&emsp;&emsp; [16進浮動小数点数リテラル](#SS_6_2_5)  
&emsp;&emsp;&emsp; [ユーザー定義リテラル](#SS_6_2_6)  
&emsp;&emsp;&emsp;&emsp; [ユーザ定義リテラル演算子](#SS_6_2_6_1)  
&emsp;&emsp;&emsp;&emsp; [std::string型リテラル](#SS_6_2_6_2)  
&emsp;&emsp;&emsp;&emsp; [std::chronoのリテラル](#SS_6_2_6_3)  
&emsp;&emsp;&emsp;&emsp; [std::complexリテラル](#SS_6_2_6_4)  

&emsp;&emsp; [列挙型とバイト表現](#SS_6_3)  
&emsp;&emsp;&emsp; [enum](#SS_6_3_1)  
&emsp;&emsp;&emsp; [enum class](#SS_6_3_2)  
&emsp;&emsp;&emsp; [スコープドenum](#SS_6_3_3)  
&emsp;&emsp;&emsp; [underlying type](#SS_6_3_4)  
&emsp;&emsp;&emsp; [std::byte](#SS_6_3_5)  
&emsp;&emsp;&emsp; [using enum](#SS_6_3_6)  

&emsp;&emsp; [型とインスタンス](#SS_6_4)  
&emsp;&emsp;&emsp; [トリビアル型](#SS_6_4_1)  
&emsp;&emsp;&emsp; [トリビアルに破壊可能な型](#SS_6_4_2)  
&emsp;&emsp;&emsp; [標準レイアウト型](#SS_6_4_3)  
&emsp;&emsp;&emsp; [集成体](#SS_6_4_4)  
&emsp;&emsp;&emsp; [POD](#SS_6_4_5)  
&emsp;&emsp;&emsp; [不完全型](#SS_6_4_6)  
&emsp;&emsp;&emsp; [完全型](#SS_6_4_7)  
&emsp;&emsp;&emsp; [ポリモーフィックなクラス](#SS_6_4_8)  
&emsp;&emsp;&emsp; [RTTI](#SS_6_4_9)  
&emsp;&emsp;&emsp;&emsp; [dynamic_cast](#SS_6_4_9_1)  
&emsp;&emsp;&emsp;&emsp; [typeid](#SS_6_4_9_2)  
&emsp;&emsp;&emsp;&emsp; [std::type_info](#SS_6_4_9_3)  

&emsp;&emsp;&emsp; [Run-time Type Information](#SS_6_4_10)  
&emsp;&emsp;&emsp; [インターフェースクラス](#SS_6_4_11)  
&emsp;&emsp;&emsp; [constインスタンス](#SS_6_4_12)  

&emsp;&emsp; [定数式とコンパイル時評価](#SS_6_5)  
&emsp;&emsp;&emsp; [constexpr](#SS_6_5_1)  
&emsp;&emsp;&emsp; [constexpr定数](#SS_6_5_2)  
&emsp;&emsp;&emsp; [constexpr関数](#SS_6_5_3)  
&emsp;&emsp;&emsp; [コア定数式](#SS_6_5_4)  
&emsp;&emsp;&emsp; [リテラル型](#SS_6_5_5)  
&emsp;&emsp;&emsp; [constexprインスタンス](#SS_6_5_6)  
&emsp;&emsp;&emsp; [consteval](#SS_6_5_7)  
&emsp;&emsp;&emsp; [constinit](#SS_6_5_8)  
&emsp;&emsp;&emsp; [constexprラムダ](#SS_6_5_9)  

&emsp;&emsp; [オブジェクト生成と初期化](#SS_6_6)  
&emsp;&emsp;&emsp; [特殊メンバ関数](#SS_6_6_1)  
&emsp;&emsp;&emsp;&emsp; [初期化子リストコンストラクタ](#SS_6_6_1_1)  
&emsp;&emsp;&emsp;&emsp; [継承コンストラクタ](#SS_6_6_1_2)  
&emsp;&emsp;&emsp;&emsp; [委譲コンストラクタ](#SS_6_6_1_3)  

&emsp;&emsp;&emsp; [explicit コンストラクタと型変換制御](#SS_6_6_2)  
&emsp;&emsp;&emsp;&emsp; [explicit](#SS_6_6_2_1)  
&emsp;&emsp;&emsp;&emsp; [暗黙の型変換](#SS_6_6_2_2)  
&emsp;&emsp;&emsp;&emsp; [暗黙の型変換抑止](#SS_6_6_2_3)  
&emsp;&emsp;&emsp;&emsp; [explicit(COND)](#SS_6_6_2_4)  
&emsp;&emsp;&emsp;&emsp; [explicit type operator()](#SS_6_6_2_5)  

&emsp;&emsp;&emsp; [==演算子](#SS_6_6_3)  
&emsp;&emsp;&emsp;&emsp; [メンバ==演算子](#SS_6_6_3_1)  
&emsp;&emsp;&emsp;&emsp; [非メンバ==演算子](#SS_6_6_3_2)  

&emsp;&emsp;&emsp; [比較演算子](#SS_6_6_4)  
&emsp;&emsp;&emsp;&emsp; [<=>演算子](#SS_6_6_4_1)  
&emsp;&emsp;&emsp;&emsp; [三方比較演算子](#SS_6_6_4_2)  
&emsp;&emsp;&emsp;&emsp; [spaceship operator](#SS_6_6_4_3)  

&emsp;&emsp;&emsp; [リスト初期化](#SS_6_6_5)  
&emsp;&emsp;&emsp; [一様初期化](#SS_6_6_6)  
&emsp;&emsp;&emsp; [非静的なメンバ変数の初期化](#SS_6_6_7)  
&emsp;&emsp;&emsp;&emsp; [NSDMI](#SS_6_6_7_1)  
&emsp;&emsp;&emsp;&emsp; [初期化子リストでの初期化](#SS_6_6_7_2)  
&emsp;&emsp;&emsp;&emsp; [コンストラクタ内での非静的なメンバ変数の初期値の代入](#SS_6_6_7_3)  

&emsp;&emsp;&emsp; [オブジェクトのライフタイム](#SS_6_6_8)  
&emsp;&emsp;&emsp; [プレースメントnew](#SS_6_6_9)  
&emsp;&emsp;&emsp; [new (std::nothrow)](#SS_6_6_10)  

&emsp;&emsp; [値カテゴリとリファレンス](#SS_6_7)  
&emsp;&emsp;&emsp; [expression](#SS_6_7_1)  
&emsp;&emsp;&emsp;&emsp; [lvalue](#SS_6_7_1_1)  
&emsp;&emsp;&emsp;&emsp; [rvalue](#SS_6_7_1_2)  
&emsp;&emsp;&emsp;&emsp; [xvalue](#SS_6_7_1_3)  
&emsp;&emsp;&emsp;&emsp; [prvalue](#SS_6_7_1_4)  
&emsp;&emsp;&emsp;&emsp; [glvalue](#SS_6_7_1_5)  

&emsp;&emsp;&emsp; [decltypeとexpression](#SS_6_7_2)  

&emsp;&emsp; [リファレンス](#SS_6_8)  
&emsp;&emsp;&emsp; [lvalueリファレンス](#SS_6_8_1)  
&emsp;&emsp;&emsp; [rvalueリファレンス](#SS_6_8_2)  
&emsp;&emsp;&emsp;&emsp; [lvalueからの代入](#SS_6_8_2_1)  
&emsp;&emsp;&emsp;&emsp; [rvalueからの代入](#SS_6_8_2_2)  
&emsp;&emsp;&emsp;&emsp; [std::move(lvalue)からの代入](#SS_6_8_2_3)  

&emsp;&emsp;&emsp; [forwardingリファレンス](#SS_6_8_3)  
&emsp;&emsp;&emsp; [ユニバーサルリファレンス](#SS_6_8_4)  
&emsp;&emsp;&emsp; [perfect forwarding](#SS_6_8_5)  
&emsp;&emsp;&emsp; [リファレンスcollapsing](#SS_6_8_6)  
&emsp;&emsp;&emsp; [リファレンス修飾](#SS_6_8_7)  
&emsp;&emsp;&emsp;&emsp; [rvalue修飾](#SS_6_8_7_1)  
&emsp;&emsp;&emsp;&emsp; [lvalue修飾](#SS_6_8_7_2)  

&emsp;&emsp; [構文と制御構造](#SS_6_9)  
&emsp;&emsp;&emsp; [属性構文](#SS_6_9_1)  
&emsp;&emsp;&emsp; [関数tryブロック](#SS_6_9_2)  
&emsp;&emsp;&emsp; [範囲for文](#SS_6_9_3)  
&emsp;&emsp;&emsp; [構造化束縛](#SS_6_9_4)  
&emsp;&emsp;&emsp; [初期化付きif/switch文](#SS_6_9_5)  
&emsp;&emsp;&emsp;&emsp; [初期化付きfor文(従来のfor文)](#SS_6_9_5_1)  
&emsp;&emsp;&emsp;&emsp; [初期化付きwhile文(従来のwhile文)](#SS_6_9_5_2)  
&emsp;&emsp;&emsp;&emsp; [初期化付きif文](#SS_6_9_5_3)  
&emsp;&emsp;&emsp;&emsp; [初期化付きswitch文](#SS_6_9_5_4)  

&emsp;&emsp; [言語拡張機能](#SS_6_10)  
&emsp;&emsp;&emsp; [コルーチン](#SS_6_10_1)  
&emsp;&emsp;&emsp;&emsp; [co_await](#SS_6_10_1_1)  
&emsp;&emsp;&emsp;&emsp; [co_return](#SS_6_10_1_2)  
&emsp;&emsp;&emsp;&emsp; [co_yield](#SS_6_10_1_3)  

&emsp;&emsp;&emsp; [モジュール](#SS_6_10_2)  
&emsp;&emsp;&emsp; [ラムダ式](#SS_6_10_3)  
&emsp;&emsp;&emsp;&emsp; [クロージャ](#SS_6_10_3_1)  
&emsp;&emsp;&emsp;&emsp; [クロージャ型](#SS_6_10_3_2)  
&emsp;&emsp;&emsp;&emsp; [一時的ラムダ](#SS_6_10_3_3)  
&emsp;&emsp;&emsp;&emsp; [transient lambda](#SS_6_10_3_4)  

&emsp;&emsp;&emsp; [指示付き初期化](#SS_6_10_4)  

&emsp;&emsp; [テンプレートと型推論](#SS_6_11)  
&emsp;&emsp;&emsp; [SFINAE](#SS_6_11_1)  
&emsp;&emsp;&emsp; [メタ関数](#SS_6_11_2)  
&emsp;&emsp;&emsp; [コンセプト](#SS_6_11_3)  
&emsp;&emsp;&emsp; [パラメータパック](#SS_6_11_4)  
&emsp;&emsp;&emsp; [畳み込み式](#SS_6_11_5)  
&emsp;&emsp;&emsp; [ジェネリックラムダ](#SS_6_11_6)  
&emsp;&emsp;&emsp; [クラステンプレートのテンプレート引数の型推論](#SS_6_11_7)  
&emsp;&emsp;&emsp; [CTAD(Class Template Argument Deduction)](#SS_6_11_8)  
&emsp;&emsp;&emsp; [テンプレートの型推論ガイド](#SS_6_11_9)  
&emsp;&emsp;&emsp; [変数テンプレート](#SS_6_11_10)  
&emsp;&emsp;&emsp; [エイリアステンプレート](#SS_6_11_11)  
&emsp;&emsp;&emsp; [constexpr if文](#SS_6_11_12)  
&emsp;&emsp;&emsp; [autoパラメータによる関数テンプレートの簡易定義](#SS_6_11_13)  
&emsp;&emsp;&emsp; [auto](#SS_6_11_14)  
&emsp;&emsp;&emsp; [decltype](#SS_6_11_15)  
&emsp;&emsp;&emsp; [decltype(auto)](#SS_6_11_16)  
&emsp;&emsp;&emsp; [戻り値型を後置する関数宣言](#SS_6_11_17)  
&emsp;&emsp;&emsp; [関数の戻り値型auto](#SS_6_11_18)  
&emsp;&emsp;&emsp; [後置戻り値型auto](#SS_6_11_19)  

&emsp;&emsp; [name lookupと継承構造](#SS_6_12)  
&emsp;&emsp;&emsp; [ルックアップ](#SS_6_12_1)  
&emsp;&emsp;&emsp; [name lookup](#SS_6_12_2)  
&emsp;&emsp;&emsp; [two phase name lookup](#SS_6_12_3)  
&emsp;&emsp;&emsp; [実引数依存探索](#SS_6_12_4)  
&emsp;&emsp;&emsp; [ADL](#SS_6_12_5)  
&emsp;&emsp;&emsp; [関連名前空間](#SS_6_12_6)  
&emsp;&emsp;&emsp; [修飾付き関数呼び出し](#SS_6_12_7)  
&emsp;&emsp;&emsp; [hidden-friend関数](#SS_6_12_8)  
&emsp;&emsp;&emsp; [name-hiding](#SS_6_12_9)  
&emsp;&emsp;&emsp; [ダイヤモンド継承](#SS_6_12_10)  
&emsp;&emsp;&emsp; [仮想継承](#SS_6_12_11)  
&emsp;&emsp;&emsp; [仮想基底](#SS_6_12_12)  
&emsp;&emsp;&emsp; [ドミナンス](#SS_6_12_13)  
&emsp;&emsp;&emsp;&emsp; [ダイヤモンド継承を含まない場合](#SS_6_12_13_1)  
&emsp;&emsp;&emsp;&emsp; [ダイヤモンド継承かつそれが仮想継承でない場合](#SS_6_12_13_2)  
&emsp;&emsp;&emsp;&emsp; [ダイヤモンド継承かつそれが仮想継承である場合](#SS_6_12_13_3)  

&emsp;&emsp;&emsp; [using宣言](#SS_6_12_14)  
&emsp;&emsp;&emsp; [usingディレクティブ](#SS_6_12_15)  

&emsp;&emsp; [エクセプション安全性の保証](#SS_6_13)  
&emsp;&emsp;&emsp; [no-fail保証](#SS_6_13_1)  
&emsp;&emsp;&emsp; [強い安全性の保証](#SS_6_13_2)  
&emsp;&emsp;&emsp; [基本的な安全性の保証](#SS_6_13_3)  
&emsp;&emsp;&emsp; [noexcept](#SS_6_13_4)  
&emsp;&emsp;&emsp; [exception-unfriendly](#SS_6_13_5)  

&emsp;&emsp; [言語仕様の定義要素](#SS_6_14)  
&emsp;&emsp;&emsp; [ill-formed](#SS_6_14_1)  
&emsp;&emsp;&emsp; [well-formed](#SS_6_14_2)  
&emsp;&emsp;&emsp; [未定義動作](#SS_6_14_3)  
&emsp;&emsp;&emsp; [未規定動作](#SS_6_14_4)  
&emsp;&emsp;&emsp; [未定義動作と未規定動作](#SS_6_14_5)  
&emsp;&emsp;&emsp; [被修飾型](#SS_6_14_6)  
&emsp;&emsp;&emsp; [実引数/仮引数](#SS_6_14_7)  
&emsp;&emsp;&emsp; [単純代入](#SS_6_14_8)  
&emsp;&emsp;&emsp; [one-definition rule](#SS_6_14_9)  
&emsp;&emsp;&emsp; [ODR](#SS_6_14_10)  
&emsp;&emsp;&emsp; [型特性キーワード](#SS_6_14_11)  
&emsp;&emsp;&emsp;&emsp; [alignof](#SS_6_14_11_1)  
&emsp;&emsp;&emsp;&emsp; [alignas](#SS_6_14_11_2)  
&emsp;&emsp;&emsp;&emsp; [addressof](#SS_6_14_11_3)  

&emsp;&emsp;&emsp; [演算子のオペランドの評価順位](#SS_6_14_12)  

&emsp;&emsp; [その他](#SS_6_15)  
&emsp;&emsp;&emsp; [RVO(Return Value Optimization)](#SS_6_15_1)  
&emsp;&emsp;&emsp; [トライグラフ](#SS_6_15_2)  
  
  

[インデックス](#SS_1_2)に戻る。  

___

## 型システムと算術の基礎 <a id="SS_6_1"></a>

### 基本型 <a id="SS_6_1_1"></a>
基本型(fundamental types)は、C++の標準で定義されている型で、
特別なキーワードを使用して直接宣言できる型の総称である。
[組み込み型](#SS_6_1_2)とも呼ばれることもある。

基本型は以下のに示した型によって構成される。

* [算術型](#SS_6_1_3)
* [汎整数型](#SS_6_1_4)
* [浮動小数点型](#SS_6_1_12)
* void
* 上記した型のポインタ型

注:  
リファレンスは基本型に含まれない。

### 組み込み型 <a id="SS_6_1_2"></a>
組み込み型(built-in types)は[基本型](#SS_6_1_1)(fundamental types)の別称。

### 算術型 <a id="SS_6_1_3"></a>
算術型とは下記の型の総称である。

* [汎整数型](#SS_6_1_4)(bool, char, int, unsigned int, long long等)
* [浮動小数点型](#SS_6_1_12)(float、double、long double)

算術型のサイズは下記のように規定されている。

* 1 == sizeof(bool) == sizeof(char)
* sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)
* 4 <= sizeof(long)
* 8 <= sizeof(long long)
* 4 == sizeof(float)
* 8 == sizeof(double) <= sizeof(long double)

### 汎整数型 <a id="SS_6_1_4"></a>
汎整数型とは下記の型の総称である。

* 論理型(bool)
* 文字型(char、wchar_t等)
* [整数型](#SS_6_1_5)(int、unsigned int、long等)

### 整数型 <a id="SS_6_1_5"></a>
整数型とは下記の型の総称である。

* signed char
* unsigned char
* short
* unsigned short
* int
* unsigned int
* long
* unsigned long
* long long
* unsigned long long

#### ビットシフトにおける未定義動作 <a id="SS_6_1_5_1"></a>

__[動作の分類]__

| 条件                     | unsigned                   | signed (C++17以前) | signed (C++20以降)   |
|--------------------------|:---------------------------|--------------------|----------------------|
| シフト量が負             | 未定義動作                 | 未定義動作         | 未定義動作           |
| シフト量 ≥ ビット数      | 未定義動作                 | 未定義動作         | 未定義動作           |
| 負の値の左シフト         | N/A                        | 未定義動作         | 未定義動作           |
| 左シフトでオーバーフロー | 定義済み(ラップアラウンド) | 未定義動作         | 未定義動作           |
| 負の値の右シフト         | N/A                        | 実装定義           | 定義済み(算術シフト) |
| 正の値の右シフト         | 定義済み（論理シフト）     | 定義済み           | 定義済み             |

__[具体例]__

| コード例                        | 動作                       | 説明                                                 |
|---------------------------------|----------------------------|------------------------------------------------------|
| `x << -1`                       | 未定義動作                 | 負のシフト量(型に関わらず)                           |
| `x << 32`                       | 未定義動作                 | シフト量がビット数以上(intが32ビットの場合)          |
| `int x = -1; x << 1`            | 未定義動作                 | 負の値の左シフト                                     |
| `int x = INT_MAX; x << 1`       | 未定義動作                 | オーバーフロー                                       |
| `unsigned x = UINT_MAX; x << 1` | 定義済み                   | ラップアラウンド(結果は最大値の2倍を2^nで割った余り) |
| `int x = -8; x >> 1`            | 実装定義(上記テーブル参照) | 負の値の右シフト                                     |
| `unsigned x = 8; x >> 1`        | 定義済み                   | 論理シフト                                           |

__[安全なビットシフトのガイドライン]__

| 推奨事項                      | 理由                          |
|-------------------------------|-------------------------------|
| 符号なし整数型を使用(注)      | 未定義動作を回避しやすい      |
| シフト量の範囲チェック        | 0 ≤ シフト量 < ビット数を保証 |
| 負の値をシフトしない          | 未定義動作の原因              |
| オーバーフローの可能性を考慮  | 特にsigned型での左シフト      |
| 静的解析ツールを活用          | コンパイル時に検出可能        |
(注) 符号なし[整数型](#SS_6_1_5)変数(us)をオペランドにした左ビットシフトがオーバーフローした場合、
     usが整数昇格によりintに変換されるため、未定義動作になる可能性がある。

### 算術変換 <a id="SS_6_1_6"></a>
C++における算術変換とは、算術演算の1つのオペランドが他のオペランドと同じ型でない場合、
1つのオペランドを他のオペランドと同じ型に変換するプロセスのことを指す。

算術変換は、[汎整数型昇格](#SS_6_1_7)と通常算術変換に分けられる。

```cpp
    //  example/core_lang_spec/integral_promotion_ut.cpp 11

    bool           bval{};
    char           cval{};
    short          sval{};
    unsigned short usval{};
    int            ival{};
    unsigned int   uival{};
    long           lval{};
    unsigned long  ulval{};
    float          fval{};
    double         dval{};

    auto ret_0 = 3.14159 + 'a';  // 'a'は汎整数拡張でintになった後、さらに通常算術変換でdoubleに
    static_assert(std::is_same<decltype(ret_0), double>::value, "");

    auto ret_1 = dval + ival;  // ivalは通常算術変換でdoubleに
    static_assert(std::is_same<decltype(ret_1), double>::value, "");

    auto ret_2 = dval + fval;  // fvalは通常算術変換でdoubleに
    static_assert(std::is_same<decltype(ret_2), double>::value, "");

    auto ret_3 = ival = dval;  // dvalは通常算術変換でintに
    static_assert(std::is_same<decltype(ret_3), int>::value, "");

    bval = dval;  // dvalは通常算術変換でboolに
    ASSERT_FALSE(bval);

    auto ret_4 = cval + fval;  // cvalは汎整数拡張でintになった後、さらに通常算術変換でfloatに
    static_assert(std::is_same<decltype(ret_4), float>::value, "");

    auto ret_5 = sval + cval;  // svalとcvalは汎整数拡張でintに
    static_assert(std::is_same<decltype(ret_5), int>::value, "");

    auto ret_6 = cval + lval;  // cvalはは汎整数拡張でintになった後、通常算術変換でlongに
    static_assert(std::is_same<decltype(ret_6), long>::value, "");

    auto ret_7 = ival + ulval;  // ivalは通常算術変換でunsigned longに
    static_assert(std::is_same<decltype(ret_7), unsigned long>::value, "");

    auto ret_8 = usval + ival;  // usvalは汎整数拡張でintに
                                // ただし、この変換はunsigned shortとintのサイズに依存する
    static_assert(std::is_same<decltype(ret_8), int>::value, "");

    auto ret_9 = uival + lval;  // uivalは通常算術変換でlongに
                                // ただし、この変換はunsigned intとlongのサイズに依存する
    static_assert(std::is_same<decltype(ret_9), long>::value, "");
```

[一様初期化](#SS_6_6_6)を使用することで、
変数定義時の算術変換による意図しない値の変換([縮小型変換](#SS_6_1_11))を防ぐことができる。

```cpp
    //  example/core_lang_spec/integral_promotion_ut.cpp 62

    int i{-1};
    // int8_t i8 {i};  縮小型変換によりコンパイル不可
    int8_t i8 = i;  // intからint8_tへの型変換
    // これには問題ないが

    ASSERT_EQ(-1, i8);

    // uint8_t ui8 {i};  縮小型変換によりコンパイル不可
    uint8_t ui8 = i;  // intからuint8_tへの型変換
    // おそらく意図通りではない

    ASSERT_EQ(255, ui8);
```

以下に示すように、算術変換の結果は直感に反することがあるため、注意が必要である。

```cpp
    //  example/core_lang_spec/integral_promotion_ut.cpp 81

    int          i{-1};
    unsigned int ui{1};

    // ASSERT_TRUE(i < ui);
    ASSERT_TRUE(i > ui);  // 算術変換の影響で、-1 < 1が成立しない

    signed short   s{-1};
    unsigned short us{1};

    ASSERT_TRUE(s < us);  // 汎整数拡張により、-1 < 1が成立
```

### 汎整数型昇格 <a id="SS_6_1_7"></a>
bool、char、signed char、unsigned char、short、unsigned short型の変数が、
算術のオペランドとして使用される場合、

* その変数の型の取り得る値全てがintで表現できるのならば、int型に変換される。
* そうでなければ、その変数はunsigned int型に変換される。

この変換を汎整数型昇格(integral promotion)と呼ぶ。

従って、sizof(short) < sizeof(int)である処理系では、
bool、char、signed char、unsigned char、short、unsigned short型の変数は、
下記のようにintに変換される。

```cpp
    //  example/core_lang_spec/integral_promotion_ut.cpp 100

    bool bval;
    static_assert(std::is_same<int, decltype(bval + bval)>::value, "");

    char cval;
    static_assert(std::is_same<int, decltype(cval + cval)>::value, "");

    unsigned char ucval = 128;
    static_assert(std::is_same<int, decltype(ucval + ucval)>::value, "");
    ASSERT_EQ(256, ucval + ucval);  // 汎整数拡張により256になる

    static_assert(std::is_same<int, decltype(cval + ucval)>::value, "");

    short sval;
    static_assert(std::is_same<int, decltype(sval + sval)>::value, "");

    unsigned short usval;
    static_assert(std::is_same<int, decltype(usval + usval)>::value, "");

    static_assert(std::is_same<int, decltype(sval + usval)>::value, "");
```

### 汎整数型拡張 <a id="SS_6_1_8"></a>
汎整数型拡張とは[汎整数型昇格](#SS_6_1_7)と同じ概念を指す。

### 浮動小数点型昇格 <a id="SS_6_1_9"></a>
浮動小数点型昇格とは、float型とdouble型の演算で、
float型オブジェクトがdoulbe型に変換されることを指す。

```cpp
    //  example/core_lang_spec/integral_promotion_ut.cpp 126

    double d = 0.05;  // 0.05は循環少数
    float  f = 0.05f;

    bool b1 = d == f;  // fはdoubleに昇格
    ASSERT_FALSE(b1);  // 0.05は循環少数であるため、0.5と0.5fは異なる。

    bool b2 = std::abs(d - f) <= std::numeric_limits<decltype(d - f)>::epsilon();
    ASSERT_FALSE(b2);  // dとfの差はdoubleのイプシロンには収まらない。
```

### デフォルト引数昇格 <a id="SS_6_1_10"></a>
デフォルト引数昇格(Default Argument Promotions)とは、可変長引数`(...)`や、
プロトタイプを持たない関数に[算術型](#SS_6_1_3)引数を渡す際に適用される昇格ルールの総称である。

デフォルト引数昇格には以下が含まれる。

- [汎整数型昇格](#SS_6_1_7)
- [浮動小数点型昇格](#SS_6_1_9)

### 縮小型変換 <a id="SS_6_1_11"></a>
縮小型変換(Narrowing Conversion) とは、あるデータ型から別のデータ型に変換する際に、
変換先の型が元の型の表現範囲を完全にカバーしていない場合に発生する変換を指す。
主に[整数型](#SS_6_1_5)や[浮動小数点型](#SS_6_1_12)などの値を小さな範囲の型に変換する際に起こる。

```cpp
    //  example/core_lang_spec/etc_ut.cpp 19

    int32_t large  = 300;
    int8_t  small  = large;  // 縮小型変換
    bool    b      = large;
    double  d      = large;  // 単単なる型変換(縮小ではない)
    int32_t large2 = d;      // 縮小型変換

    // large = int32_t{d};   縮小型変換回避のためリスト初期化の使用。コンパイルエラー
```

[リスト初期化](#SS_6_6_5)を使うことで、このような変換によるバグの発生を防ぐことができる。


### 浮動小数点型 <a id="SS_6_1_12"></a>
浮動小数点型は以下の型の総称である。

* `float`
* `double`
* `long double`

浮動小数点の仕様は、IEEE 754標準に準拠している。
この標準は、浮動小数点演算の表現方法、精度、丸め方法、および例外処理を規定しており、
広く使用されている。

#### 浮動小数点型のダイナミックレンジ <a id="SS_6_1_12_1"></a>

| 型                          | 正の最小値                    | 正の最大値                    |
|:----------------------------|:------------------------------|:------------------------------|
| `float`                     | 1.175494351 e-38              | 3.402823466 e+38              |
| `double`                    | 2.2250738585072014 e-308      | 1.7976931348623158 e+308      |
| `long double`               | 3.36210314311209350626 e-4932 | 1.18973149535723176502 e+4932 |
| `int32_t`                   | -2,147,483,648                | 2,147,483,647                 |
| `int64_t`                   | -9,223,372,036,854,775,808    | 9,223,372,036,854,775,807     |

ここで`long double`の最小値と最大値は、システムやコンパイラに依存して異なる場合がある点に留意する。

#### 浮動小数点の誤差 <a id="SS_6_1_12_2"></a>
浮動小数点変数の10進数の表現が2進数では循環小数となる場合があり、
正確に表現できないことがある。これにより、計算結果がわずかに異なる値を返す場合がある。
浮動小数点誤差は、特に計算の繰り返しや桁数の多い計算で顕著になる。

以下のコードにより誤差が容易に発生することを示す。

```cpp
    //  example/core_lang_spec/float_ut.cpp 12

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    //  ASSERT_EQ(0.05F, a + b);  // NG  a + b == 0.05Fは一般には成立しない。
    ASSERT_NE(0.05F, a + b);
```

#### イプシロン <a id="SS_6_1_12_3"></a>
イプシロン(epsilon)とは、ある浮動小数点数に対して「1」を加えた時に、
異なる値として識別できる最小の差分を指す。
つまり、イプシロンは浮動小数点数の精度を示す尺度である。

任意の浮動小数点変数a, bがあり、`|a - b| <= epsilon`であった場合、
浮動小数点の仕組みではa、bの差が無いものと考えて、aとbが同値であると考えることが一般的である。

イプシロンを使用した浮動小数点変数の同値判定のコード例を以下に示す。

```cpp
    //  example/core_lang_spec/float_ut.cpp 24

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    bool is_equal = 0.05F == (a + b);
    ASSERT_FALSE(is_equal);  // is_equalはtrueにはならない

    bool is_nearly_equal = std::abs(0.05F - (a + b)) <= std::numeric_limits<float>::epsilon();
    ASSERT_TRUE(is_nearly_equal);  // 浮動小数点の同値はこのように判定する
```

#### 浮動小数点の演算エラー <a id="SS_6_1_12_4"></a>
浮動小数点の演算は以下のようなエラーを生じることがある。

| エラーの種類   | 説明                                                                           | 例                           |
|:---------------|:-------------------------------------------------------------------------------|:-----------------------------|
| 丸め誤差       | 有限桁数による四捨五入の誤差が発生し、正確な値とわずかに異なる場合がある。     | `0.1 + 0.2 != 0.3`           |
| 桁落ち         | 非常に小さい数と大きい数の加算時に、小さい数が無視され、精度が低下する。       | `1e20 + 1 - 1e20 == 0`       |
| 累積誤差       | 繰り返し演算で小さな誤差が積み重なり、最終的に大きなズレが生じることがある。   | ループ内での浮動小数点の加算 |
| ゼロ除算       | 0での除算により計算が定義されず、例外が発生または±無限大が返される。           | `1.0 / 0.0`                  |
| オーバーフロー | 型が表現可能な最大値を超えると無限大（`inf`）として扱われる。                  | `std::pow(10.0, 308)`        |
| アンダーフロー | 型の最小値より小さい数値は0または非常に小さな値として表現され、精度が失われる。| `std::pow(10.0, -308)`       |
| NaN            | 実数では表現できない。                                                         | `std::sqrt(-1)`              |

浮動小数点の演算エラーの検出コード例を以下に示す。

```cpp
    //  example/core_lang_spec/float_ut.cpp 43

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

なお、上記のコードで使用した`std::fetestexcept`は一般にスレッドセーフである。
`std::fetestexcept`がスレッドセーフでない処理系では、浮動小数演算エラーの検出は、
実質的には不可能になってしまうため、
浮動小数演算を複数コンテキストで行うソフトウェアの開発する場合、
処理系の選択に注意が必要である。

## リテラル <a id="SS_6_2"></a>
プログラムに具体的な値を与えるための基本的な即値を指す。
例えば、1, 2, 1.0, true/false, nullptr, "literal string"など。

### 生文字列リテラル <a id="SS_6_2_1"></a>
下記の例にあるように正規表現をそのまま文字列リテラルとして表現するために、
C++11から導入された導入されたリテラル。

```cpp
    //  example/core_lang_spec/literal_ut.cpp 15

        std::regex raw_re{R"(\d+)"};     // 生文字リテラルで正規表現パターン。\のエスケープが不要
        std::regex normal_re{"(\\d+)"};  // 生文字リテラルで正規表現パターン。\のエスケープが必要

        std::string test_str = "The year is 2024";  // テスト対象の文字列

        {
            std::smatch match;
            ASSERT_TRUE(std::regex_search(test_str, match, raw_re));  // 正規表現で数字部分を検索
            ASSERT_EQ(match.str(), "2024");  // マッチした部分が "2024" であることをチェック
        }
        {
            std::smatch match;
            ASSERT_TRUE(std::regex_search(test_str, match, normal_re));  // 正規表現で数字部分を検索
            ASSERT_EQ(match.str(), "2024");  // マッチした部分が "2024" であることをチェック
        }
```

### 2進数リテラル <a id="SS_6_2_2"></a>
C++14以降では、0bまたは 0B をプレフィックスとして使うことで、2進数リテラルを表現できる。

```cpp
    //  example/core_lang_spec/literal_ut.cpp 36

    int bin_value = 0b1101;  // 2進数リテラル  2進数1101 は10進数で 13
    ASSERT_EQ(bin_value, 13);
```

### 数値リテラル <a id="SS_6_2_3"></a>
C++14では区切り文字'を使用し、数値リテラルを記述できるようになった。

```cpp
    //  example/core_lang_spec/literal_ut.cpp 42

    // 区切り文字を使った数値リテラル
    int large_number = 1'000'000;  // 10進数は3桁で区切るとわかりやすい
    ASSERT_EQ(large_number, 1000000);

    int bin_with_separator = 0b1011'0010;  // 10進数は4桁で区切るとわかりやすい
    ASSERT_EQ(bin_with_separator, 178);    // 2進数 1011 0010 は 10進数で 178

    int hex_with_separator = 0x00'00'ff'ff;  // 16進数は2桁で区切るとわかりやすい
    ASSERT_EQ(hex_with_separator, 65535);    // 16進数 0x00010011 == 65535
```

### ワイド文字列 <a id="SS_6_2_4"></a>
ワイド文字列リテラルを保持する型は下記のように定義された。

* char16_t: UTF-16エンコーディングのコード単位を扱う型。 u"..." というリテラルでUTF-16文字列を表す。
* char32_t: UTF-32エンコーディングのコード単位を扱う型。 U"..." というリテラルでUTF-32文字列を表す。
* char8_t: UTF-8エンコーディングのコード単位を扱う型。 u8"..." というリテラルでUTF-8文字列を表す。

```cpp
    //  example/core_lang_spec/literal_ut.cpp 59

        // UTF-16 文字列リテラル（uプレフィックスを使用）
        char16_t       utf16_str[]  = u"こんにちは";
        std::u16string utf16_string = u"こんにちは";  // UTF-16 std::u16string 型

        // UTF-32 文字列リテラル（Uプレフィックスを使用）
        char32_t       utf32_str[]  = U"こんにちは";
        std::u32string utf32_string = U"こんにちは";  // UTF-32 std::u32string 型

    #if __cplusplus >= 202002L  // c++20
        // UTF-8 文字列リテラル（u8プレフィックスを使用）
        const char8_t* utf8_str    = u8"こんにちは";
        std::u8string  utf8_string = u8"こんにちは";  // UTF-8 std::string 型

    #else // c++17
        // UTF-8 文字列リテラル（u8プレフィックスを使用）
        const char* utf8_str    = "こんにちは";
        std::string utf8_string = "こんにちは";  // UTF-8 std::string 型
    #endif
```

### 16進浮動小数点数リテラル <a id="SS_6_2_5"></a>
16進浮動小数点数リテラルは、
C++17から導入された浮動小数点数を16進数で表現する方法である。
特に、ハードウェアや低レベルのプログラミングで、
浮動小数点数の内部表現を直接扱う際に便利である

```
    一般的な形式:
        0x[数字].[数字]p[指数]
        0x: 16進数を表すプレフィックス
        [数字]: 16進数の数字 (0-9, a-f, A-F)
        .: 小数点
        p: 指数部を表す
        [指数]: 10進数の指数

    例:
        0x1.2p3は下記に解説する

    リテラルの構成:
        0x: 16進数の開始を示す。
        1.2: 仮数部を表す。この部分は16進数。
        p3: 指数部を表す。この場合、2の3乗を意味すため、つまり8。

        1.2(16進数) =  1 + 2 / 16 = 1.125(10進数)
        1.125 * 8 = 9.0
```

```cpp
    //  example/core_lang_spec/literal_ut.cpp 87

    // float型
    float hex_float = 0x1.2p3;
    EXPECT_FLOAT_EQ(hex_float, 9.0f);  // 正しい期待値は9.0f

    // double型
    double hex_double = 0x1.2p3;
    EXPECT_DOUBLE_EQ(hex_double, 9.0);  // 正しい期待値は9.0

    // 指数部が負の場合 (double型)
    double negative_exp = 0x1.2p-2;
    EXPECT_DOUBLE_EQ(negative_exp, 0.28125);  // 期待値は正しい

    // 小数点以下の部分がない場合 (double型)
    double integer_part = 0x1p3;
    EXPECT_DOUBLE_EQ(integer_part, 8.0);  // 期待値は正しい

    EXPECT_FLOAT_EQ(static_cast<float>(hex_double), hex_float);  // double型をfloatにキャスト
```

### ユーザー定義リテラル <a id="SS_6_2_6"></a>
[ユーザ定義リテラル演算子](#SS_6_2_6_1)により定義されたリテラルを指す。

#### ユーザ定義リテラル演算子 <a id="SS_6_2_6_1"></a>
ユーザ定義リテラル演算子とは以下のようなものである。

```cpp
    //  example/core_lang_spec/user_defined_literal_ut.cpp 4

    constexpr int32_t one_km = 1000;

    // ユーザ定義リテラル演算子の定義
    constexpr int32_t operator""_kilo_meter(unsigned long long num_by_mk) { return num_by_mk * one_km; }
    constexpr int32_t operator""_meter(unsigned long long num_by_m) { return num_by_m; }
```
```cpp
    //  example/core_lang_spec/user_defined_literal_ut.cpp 15

    int32_t km = 3_kilo_meter;  // ユーザ定義リテラル演算子の利用
    int32_t m  = 3000_meter;    // ユーザ定義リテラル演算子の利用

    ASSERT_EQ(m, km);
```

#### std::string型リテラル <a id="SS_6_2_6_2"></a>
"xxx"sとすることで、std::string型のリテラルを作ることができる。

```cpp
    //  example/core_lang_spec/user_defined_literal_ut.cpp 26

    using namespace std::literals::string_literals;

    auto a = "str"s;  // aはstd::string
    auto b = "str";   // bはconst char*

    static_assert(std::is_same_v<decltype(a), std::string>);
    ASSERT_EQ(std::string{"str"}, a);

    static_assert(std::is_same_v<decltype(b), char const*>);
    ASSERT_STREQ("str", b);
```

#### std::chronoのリテラル <a id="SS_6_2_6_3"></a>
std::chronoのリテラルは以下のコードのように使用できる。

```cpp
    //  example/core_lang_spec/literal_ut.cpp 109

    using namespace std::chrono_literals;

    static_assert(1s == 1000ms);  // 1秒 (1s) は 1000 ミリ秒 (1000ms) と等しい

    static_assert(1min == 60s);  // 1分 (1min) は 60秒 (60s) と等しい

    static_assert(1h == 3600s);  // 1時間 (1h) は 3600秒 (3600s) と等しい

    static_assert(1.5s == 1500ms);  // 小数点を使った時間リテラル
```

#### std::complexリテラル <a id="SS_6_2_6_4"></a>
std::complexリテラル以下のコードのように使用できる。

```cpp
    //  example/core_lang_spec/literal_ut.cpp 124

    using namespace std::complex_literals;  // 複素数リテラルを使うための名前空間

    auto a = 1.0 + 2.0i;  // std::complex<double>
    auto b = 3.0 + 4.0i;  // std::complex<double>

    auto result = a + b;
    EXPECT_EQ(result.real(), 4.0);
    EXPECT_EQ(result.imag(), 6.0);
    EXPECT_EQ(result, 4.0 + 6.0i);
```

## 列挙型とバイト表現 <a id="SS_6_3"></a>
### enum <a id="SS_6_3_1"></a>
C++03までのenumは定数を分かりやすい名前で定義するための記法である。
このドキュメントでは、[スコープドenum](#SS_6_3_3)に対して、C++03までのenumを非スコープドenum、
通常のenum、あるいは単にenumと呼ぶことがある。
C++03までのenumには、以下のような問題があった。

* スコープの制限: 名前付きスコープ内に定義するためには、クラスのメンバとして定義しなければならない。
* 型安全性: enumの値は整数型と暗黙の変換が行われてしまう。
* 名前空間の汚染: グローバルスコープに定義されたenumは、名前空間を汚染する。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 14

    enum DayOfWeek { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

    ASSERT_TRUE(1 == Monday);  // intへの暗黙の変換

    enum Color { Red, Green, Blue };

    ASSERT_TRUE(Green == Monday);  // 別のenumが比較できてしまう
```

### enum class <a id="SS_6_3_2"></a>
enum classは通常の[enum](#SS_6_3_1)の問題を解決するためにC++11から導入された。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 29

    enum class DayOfWeek { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

    // ASSERT_TRUE(1 == Monday);  // intへの暗黙の変換できないため、コンパイルエラー
    ASSERT_TRUE(1 == static_cast<int>(DayOfWeek::Monday));

    enum class Color { Red, Green, Blue };

    // ASSERT_TRUE(Green == Monday);  // 別のenumが比較できないため、コンパイルエラー
    ASSERT_TRUE(static_cast<DayOfWeek>(Color::Green) == DayOfWeek::Monday);
```

```cpp
    //  example/core_lang_spec/enum_ut.cpp 41

    // DayOfWeek d0 {0}; intからの暗黙の型変換は許可されないため、コンパイルエラー
    DayOfWeek d0{static_cast<DayOfWeek>(0)};
    DayOfWeek d1{};  // デフォルト初期化
    ASSERT_EQ(d1, DayOfWeek::Sunday);

    DayOfWeek d2{DayOfWeek::Tuesday};  // 値あり初期化
```

### スコープドenum <a id="SS_6_3_3"></a>
[enum class](#SS_6_3_2)はスコープドenum(scoped enum)と呼ばれることがある。


### underlying type <a id="SS_6_3_4"></a>
underlying typeとは、enumやenum classの[汎整数型](#SS_6_1_4)を指定できるようにするために、
C++11で導入されたシンタックスである。enumのサイズをユーザが定義できるため、
特定のバイナリプロトコルとの互換性が必要な場合や、特定のハードウェアと連携する際に特に有効である。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 54

    enum NormalEnum {  // underlying typeの指定しない従来のenum
    };

    enum NormalEnumUnderlyingType : int8_t {  // enum underlying typeがint8_tに指定された従来のenum
    };

    // enum class
    enum class EnumClass {  // underlying typeの指定しないenum class
    };

    enum class EnumClassUnderlyingType : int64_t {  // enum underlying typeがint64_tに指定されたenum
                                                    // class
    };

    static_assert(4 ==  sizeof(NormalEnum));  // 列挙子の値を表現するのに十分なサイズの整数型で処理系依存
    static_assert(4 ==  sizeof(EnumClass));   // 列挙子の値を表現するのに十分なサイズの整数型で処理系依存
    static_assert(sizeof(int8_t) == sizeof(NormalEnumUnderlyingType));
    static_assert(sizeof(int64_t) == sizeof(EnumClassUnderlyingType));
```

C++17までは、型安全の観点から、初期化においては、以下のコードコメントのような仕様であったが、
C++17から導入された[std::byte](#SS_6_3_5)の利便性のため、
underlying typeを指定したenumやenum class変数のunderlying typeインスタンスによる初期化が認められるようになった。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 80

    enum class Color : int { Red, Green, Blue };

    // Color red{0}; C++14まではコンパイルエラー

    Color red{0};  // underlying typeの効果でC++17からコンパイルできる。

    long a{1};
    // Color green{a};  // 縮小型変換が発生するため、コンパイルエラー

```

上記コードにもあるが、underlying typeインスタンスによる初期化を行う場合は、
意図しない縮小型変換によるバグの発生を防ぐためにも、
[一様初期化](#SS_6_6_6)を使用するべきだろう。

一部の例外を除くとunderlying typeを指定しないenumやenum classはコンパイル時にサイズが確定できないため、
前方宣言できないが、underlying typeを指定したenum、enum classは前方宣言することができる。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 97

    // in calender.h
    enum class DayOfWeek : int8_t;  // DayOfWeekの前方宣言

    bool calender(DayOfWeek);  // 前方宣言の効果でこのヘッダでの#include "day_of_week.h"が不要

    // in day_of_week.h
    enum class DayOfWeek : int8_t { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
```

### std::byte <a id="SS_6_3_5"></a>
C++17で導入されたstd::byte型は、バイト単位のデータ操作に使用され、
[整数型](#SS_6_1_5)としての意味を持たないため、型安全性を確保する。
uint8_t型と似ているが、uint8_t型の演算による[汎整数型昇格](#SS_6_1_7)を発生させないため、
可読性、保守性の向上が見込める。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 113

    uint8_t u8_0     = 0x80;
    auto    result_0 = u8_0 << 1;  // 汎整数拡張のためresult_0の型はintになる

    static_assert(std::is_same_v<decltype(result_0), int>);
    ASSERT_EQ(0x100, result_0);  // これがわかりずらいバグにつながることがある

    auto u8_1     = std::byte{0x80};
    auto result_1 = u8_1 << 1;  // 汎整数拡張は発生せず、result_1の型はstd::byteになる

    static_assert(std::is_same_v<decltype(result_1), std::byte>);

    // 整数型を取り出すためには、暗黙の型変換ではなく、
    // 明示的なto_integerの呼び出しが必要になることもコードの安全性につながる
    ASSERT_EQ(0x00, std::to_integer<int>(result_1));  // 0x100はstd::byteでは0
```

### using enum <a id="SS_6_3_6"></a>
名前空間のように、

```cpp
    using enum EnumType;
```

もしくは

```cpp
    using EnumType::enumerator
```

とすることで、スコープによる修飾を省略するための記法である。

```cpp
    //  example/core_lang_spec/enum_ut.cpp 158

    enum class Color { Red, Green, Yellow };

    constexpr std::string_view to_str(Color color)
    {
    #if __cplusplus >= 202002L  // c++20
        using enum Color;       // 名前修飾の省略可能にする

        switch (color) {
        case Red:
            return "Red";
        case Green:
            return "Green";
        case Yellow:
            return "Yellow";
        }

    #else  // c++17
        switch (color) {
        case Color::Red:
            return "Red";
        case Color::Green:
            return "Green";
        case Color::Yellow:
            return "Yellow";
        }
    #endif
        assert(false);
        return "";
    }
```
```cpp
    //  example/core_lang_spec/enum_ut.cpp 194

    #if __cplusplus >= 202002L  // c++20
        using Color::Red;  // Redに関しては名前修飾なしで使用する

        ASSERT_EQ("Red", to_str(Red));
        ASSERT_EQ("Yellow", to_str(Color::Yellow));

    #else  // c++17
        ASSERT_EQ("Red", to_str(Color::Red));
        ASSERT_EQ("Yellow", to_str(Color::Yellow));
    #endif
```

```cpp
    //  example/core_lang_spec/enum_ut.cpp 213

    class Signal {
    public:
        enum class Color { Red, Green, Yellow };
        using enum Color;

        void Set(Color);

    private:
        // ...
    };
```
```cpp
    //  example/core_lang_spec/enum_ut.cpp 229

    Signal s{};

    s.Set(Signal::Color::Red);  // 名前修飾が長すぎる感じがする
    s.Set(Signal::Red);         // using enum colorがあるために、簡潔に書ける

    using Signal::Red;  // Redに関しては名前修飾なしで使用する
                        // この記述によりこの名前空間でのRed識別子が使えなくなる
    s.Set(Red);
```

この記法は、簡潔に記述できるものの、一方では過度な使用は、
C++03までのenumが持っていた問題を再発生させてしまうため、
ブロックスコープ以外での使用に関しては控え目に使用するべきだろう。

## 型とインスタンス <a id="SS_6_4"></a>
### トリビアル型 <a id="SS_6_4_1"></a>
トリビアル型とは、

* 全ての[特殊メンバ関数](#SS_6_6_1)がデフォルトである。
* バーチャル関数や仮想継承を持たない。
* 基底クラスがある場合、基底クラスもトリビアルである。

である。その結果、トリビアル型とは、[トリビアルに破壊可能な型](#SS_6_4_2)となる。

「型Tがトリビアルであること」と「以下の行がコンパイルできること」は等価である。

```cpp
    static_assert(std::is_trivial_v<T>);
```

下記のコードはその使用例である。

```cpp
    //  example/core_lang_spec/trivial_ut.cpp 63

    static_assert(std::is_trivial_v<int>);
    static_assert(std::is_trivial_v<int*>);
    static_assert(std::is_trivial_v<int[1]>);
    static_assert(!std::is_trivial_v<int&>);

    enum class SizeUndefined { su_0, su_1 };

    struct Trivial {      // トリビアルだが標準レイアウトではない
        int&          a;  // リファレンスは標準レイアウトではない
        SizeUndefined b;
    };

    static_assert(!std::is_standard_layout_v<Trivial>);
    static_assert(std::is_trivial_v<Trivial>);
    static_assert(!is_pod_v<Trivial>);
```

### トリビアルに破壊可能な型 <a id="SS_6_4_2"></a>
「トリビアルに破壊可能な型(Trivially Destructible)」とは、以下の条件を満たす型を指す。

* デストラクタがユーザー定義されていない
  (つまりコンパイラが生成したデフォルトのデストラクタを使用している)。
* 型に含まれるすべてのメンバ変数や基底クラスも「トリビアルに破壊可能」である。

```cpp
    //  example/core_lang_spec/trivial_ut.cpp 84

    static_assert(std::is_trivially_destructible_v<int>);
    static_assert(std::is_trivially_destructible_v<int*>);
    static_assert(std::is_trivially_destructible_v<int[1]>);
    static_assert(std::is_trivially_destructible_v<int&>);

    enum class SizeUndefined { su_0, su_1 };

    struct Trivial {  // トリビアルに破壊可能でないため、トリビアル型ではない
        int           a;
        SizeUndefined b;
        ~Trivial() {}
    };

    static_assert(std::is_standard_layout_v<Trivial>);
    static_assert(!std::is_trivial_v<Trivial>);
    static_assert(!std::is_trivially_destructible_v<Trivial>);
```

### 標準レイアウト型 <a id="SS_6_4_3"></a>
「型Tが標準レイアウトであること」と「以下の行がコンパイルできること」は等価である。

```cpp
    static_assert(std::is_standard_layout_v<T>);
```

下記のコードはその使用例である。

```cpp
    //  example/core_lang_spec/trivial_ut.cpp 42

    static_assert(std::is_standard_layout_v<int>);
    static_assert(std::is_standard_layout_v<int*>);
    static_assert(std::is_standard_layout_v<int[1]>);
    static_assert(!std::is_standard_layout_v<int&>);

    enum class SizeUndefined { su_0, su_1 };

    struct StanderdLayout {  // 標準レイアウトだがトリビアルではない
        StanderdLayout() : a{0}, b{SizeUndefined::su_0} {}
        int           a;
        SizeUndefined b;
    };

    static_assert(std::is_standard_layout_v<StanderdLayout>);
    static_assert(!std::is_trivial_v<StanderdLayout>);
    static_assert(!is_pod_v<StanderdLayout>);
```

### 集成体 <a id="SS_6_4_4"></a>
型Tが集成体であるための条件を以下に示す。

* 型Tが`class`、`struct`、`union`であった場合、以下の条件を満たせばTは集成体である。
    * 以下に示したユーザ定義による特殊関数が存在しない。
        * ユーザー定義のコンストラクタ(デフォルトコンストラクタ、コピーコンストラクタ、ムーブコンストラクタ)
        * デストラクタ
        * コピー代入演算子
        * ムーブ代入演算子

    * すべての非静的メンバがpublicであるか、それらに外部からアクセスできる。
    * 仮想関数や仮想基底クラスを持たないこと
    * 仮想関数が定義されておらず、仮想基底クラス（仮想継承）を使用していない。
    * 基底クラスを持たない。

* 集成体の配列や、組み込み型の配列は集成体である。

### POD <a id="SS_6_4_5"></a>
PODとは、 Plain Old Dataの略語であり、
「型TがPODであること」と「以下の行がコンパイルできること」は等価である。

```cpp
    static_assert(std::is_pod_v<T>);  // is_podはC++20から非推奨
```

「型が[トリビアル型](#SS_6_4_1)且つ[標準レイアウト型](#SS_6_4_3)であること」と
「型が[POD](#SS_6_4_5)であること」は等価であるため、C++20では、
[PODという用語は非推奨](https://cpprefjp.github.io/lang/cpp20/deprecate_pod.html)となった。
従って、std::is_pod_vは以下のように置き換えられるべきである。

```cpp
    //  example/core_lang_spec/trivial_ut.cpp 9

    template <typename T>  // std::is_povはC++20から非推奨
    constexpr bool is_pod_v = std::is_trivial_v<T>&& std::is_standard_layout_v<T>;
```

下記のコードは置き換えられたstd::is_pod_vの使用例である。

```cpp
    //  example/core_lang_spec/trivial_ut.cpp 18

    static_assert(is_pod_v<int>);
    static_assert(is_pod_v<int const>);
    static_assert(is_pod_v<int*>);
    static_assert(is_pod_v<int[3]>);
    static_assert(!is_pod_v<int&>);  // リファレンスはPODではない

    struct Pod {};

    static_assert(is_pod_v<Pod>);
    static_assert(is_pod_v<Pod const>);
    static_assert(is_pod_v<Pod*>);
    static_assert(is_pod_v<Pod[3]>);
    static_assert(!is_pod_v<Pod&>);

    struct NonPod {  // コンストラクタがあるためPODではない
        NonPod();
    };

    static_assert(!is_pod_v<NonPod>);
```

上記からわかる通り、POD型とは概ね、C言語と互換性のある型を指すと思って良い。


### 不完全型 <a id="SS_6_4_6"></a>
不完全型とは、型のサイズや構造が不明な型を指す。
以下のis_completeで示したテンプレート定数で、不完全型か否かを判定できる。

```cpp
    //  example/core_lang_spec/incomplete_type_ut.cpp 4

    template <typename T, typename = void>
    struct is_complete : std::false_type {
    };

    template <typename T>  // sizeof(T) が有効であれば、Tは完全型であると判定
    struct is_complete<T, std::void_t<decltype(sizeof(T))>> : std::true_type {
    };

    template <typename T>
    constexpr bool is_complete_v = is_complete<T>::value;
```
```cpp
    //  example/core_lang_spec/incomplete_type_ut.cpp 21

    class A;  // Aの前方宣言
              // これ以降、Aは不完全型となる

    // auto a = sizeof(A);  Aが不完全型であるため、コンパイルエラー
    static_assert(!is_complete_v<A>);
```
```cpp
    //  example/core_lang_spec/incomplete_type_ut.cpp 31

    class A {  // この宣言により、この行以降はAは完全型になる
    public:
        // 何らかの宣言
    };

    auto a = sizeof(A);  // Aが完全型であるため、コンパイル可能
    static_assert(is_complete_v<A>);
```

### 完全型 <a id="SS_6_4_7"></a>
[不完全型](#SS_6_4_6)ではない型を指す。

### ポリモーフィックなクラス <a id="SS_6_4_8"></a>
ポリモーフィックなクラスとは仮想関数を持つクラスや、
ポリモーフィックなクラスから派生したクラスを指す。
なお、純粋仮想関数を持つクラスは、
仮想クラスと呼ばれれる(「[インターフェースクラス](#SS_6_4_11)」参照)。
ポリモーフィックなクラスと、
非ポリモーフィックなクラスは[RTTI](#SS_6_4_9)との組み合わせで動作の違いが顕著となる。

非ポリモーフィックなクラスは非静的なメンバ変数が定義された順にメモリ上に配置されたレイアウトを持つ
(CPUアーキテクチャに依存したパディング領域が変数間に挿入されることもある)。
このようなクラスは[POD](#SS_6_4_5)
(C++20では、[PODという用語は非推奨](https://cpprefjp.github.io/lang/cpp20/deprecate_pod.html)
となり、[トリビアル型](#SS_6_4_1)と[標準レイアウト型](#SS_6_4_3)に用語が分割された)とも呼ばれ、
C言語の構造体のレイアウトと互換性を持つことが一般的である。

ポリモーフィックなクラスは、
仮想関数呼び出しを行う(「[オーバーライドとオーバーロードの違い](#SS_8_11_1)」参照)
ためのメモリレイアウトが必要になる。
それを示すために、まずは下記のようにクラスX、Y、Zを定義する。

```cpp
    //  example/core_lang_spec/class_layout_ut.cpp 4

    class X {
    public:
        virtual int64_t GetX() { return x_; }
        virtual ~X() {}

    private:
        int64_t x_{1};
    };

    class Y : public X {
    public:
        virtual int64_t GetX() override { return X::GetX() + y_; }
        virtual int64_t GetY() { return y_; }
        virtual ~Y() override {}

    private:
        int64_t y_{2};
    };

    class Z : public Y {
    public:
        virtual int64_t GetX() override { return Y::GetX() + z_; }
        virtual int64_t GetY() override { return Y::GetY() + z_; }
        virtual int64_t GetZ() { return z_; }
        virtual ~Z() override {}

    private:
        int64_t z_{3};
    };
```

通常のC++コンパイラが作り出すX、Y、Zの概念的なメモリレイアウトは下記のようになる。

下図中のvtbl(virtual table または virtual function table)とは、
仮想関数ポインタを保持するための構造体であり、仮想関数呼び出しを解決するための仕組みである。

```essential/plant_uml/class_layout.pu
@startditaa

+---------------------+
|class X              |
+---------------------+
|cGRE pointer to vtbl +--> +--------------+
+---------------------+    |vtbl for X    |
|cBLU  x_             |    +--------------+
+---------------------+    |cPNK &X꞉꞉GetX | 
                           +--------------+
                           |cPNK &X꞉꞉~X   | 
                           +--------------+

+---------------------+
|class Y              |
+---------------------+
|cGRE pointer to vtbl +--> +--------------+
+---------------------+    |vtbl for Y    |
|cBLU  x_             |    +--------------+
+---------------------+    |cPNK &Y꞉꞉GetX | 
|cBLU  y_             |    +--------------+
+---------------------+    |cPNK &Y꞉꞉~Y   | 
                           +--------------+
                           |cPNK &Y꞉꞉GetY | 
                           +--------------+

+---------------------+
|class Z              |
+---------------------+
|cGRE pointer to vtbl +--> +--------------+
+---------------------+    |vtbl for Z    |
|cBLU  x_             |    +--------------+
+---------------------+    |cPNK &Z꞉꞉GetX | 
|cBLU  y_             |    +--------------+
+---------------------+    |cPNK &Z꞉꞉~Z   | 
|cBLU  z_             |    +--------------+
+---------------------+    |cPNK &Z꞉꞉GetY | 
                           +--------------+
                           |cPNK &Z꞉꞉GetZ | 
                           +--------------+

@endditaa
# ファイルエンコーディング utf-8
```

各クラスがvtblへのポインタを保持するため、このドキュメントで使用している[g++](#SS_8_13_1)では、
sizeof(X)は8ではなく16、sizeof(Y)は16ではなく24、sizeof(Z)は24ではなく32となる。

g++の場合、以下のオプションを使用し、クラスのメモリレイアウトをファイルに出力することができる。

```cpp
    //  example/core_lang_spec/Makefile 23

    CCFLAGS_ADD:=-fdump-lang-class
```

X、Y、Zのメモリレイアウトは以下の様に出力される。

```
    Vtable for X
    X::_ZTV1X: 5 entries
    0     (int (*)(...))0
    8     (int (*)(...))(& _ZTI1X)
    16    (int (*)(...))X::GetX
    24    (int (*)(...))X::~X
    32    (int (*)(...))X::~X

    Class X
       size=16 align=8
       base size=16 base align=8
    X (0x0x7f54bbc23a80) 0
        vptr=((& X::_ZTV1X) + 16)

    Vtable for Y
    Y::_ZTV1Y: 6 entries
    0     (int (*)(...))0
    8     (int (*)(...))(& _ZTI1Y)
    16    (int (*)(...))Y::GetX
    24    (int (*)(...))Y::~Y
    32    (int (*)(...))Y::~Y
    40    (int (*)(...))Y::GetY

    Class Y
       size=24 align=8
       base size=24 base align=8
    Y (0x0x7f54bbc3f000) 0
        vptr=((& Y::_ZTV1Y) + 16)
      X (0x0x7f54bbc23d20) 0
          primary-for Y (0x0x7f54bbc3f000)

    Vtable for Z
    Z::_ZTV1Z: 7 entries
    0     (int (*)(...))0
    8     (int (*)(...))(& _ZTI1Z)
    16    (int (*)(...))Z::GetX
    24    (int (*)(...))Z::~Z
    32    (int (*)(...))Z::~Z
    40    (int (*)(...))Z::GetY
    48    (int (*)(...))Z::GetZ

    Class Z
       size=32 align=8
       base size=32 base align=8
    Z (0x0x7f54bbc3f068) 0
        vptr=((& Z::_ZTV1Z) + 16)
      Y (0x0x7f54bbc3f0d0) 0
          primary-for Z (0x0x7f54bbc3f068)
        X (0x0x7f54bbc43060) 0
            primary-for Y (0x0x7f54bbc3f0d0)
```

このようなメモリレイアウトは、

```cpp
    //  example/core_lang_spec/class_layout_ut.cpp 40

    auto z_ptr = new Z;
```

のようなオブジェクト生成に密接に関係する。その手順を下記の疑似コードにより示す。

```cpp
    // ステップ1  メモリアロケーション
    void* ptr = malloc(sizeof(Z));

    // ステップ2  ZオブジェクトのX部分の初期化
    X* x_ptr = (X*)ptr;
    x_ptr->vtbl = &vtbl_for_X       // Xのコンストラクタ呼び出し処理
    x_ptr->x_ = 1;                  // Xのコンストラクタ呼び出し処理

    // ステップ3  ZオブジェクトのY部分の初期化
    Y* y_ptr = (Y*)ptr;
    y_ptr->vtbl = &vtbl_for_Y       // Yのコンストラクタ呼び出し処理
    y_ptr->y_ = 2;                  // Yのコンストラクタ呼び出し処理

    // ステップ4  ZオブジェクトのZ部分の初期化
    Z* z_ptr = (Z*)ptr;
    z_ptr->vtbl = &vtbl_for_Z       // Zのコンストラクタ呼び出し処理
    z_ptr->z_ = 3;                  // Zのコンストラクタ呼び出し処理
```

オブジェクトの生成がこのように行われるため、Xのコンストラクタ内で仮想関数GetX()を呼び出した場合、
その時のvtblへのポインタはXのvtblを指しており(上記ステップ2)、X::GetX()の呼び出しとなる
(Z::GetX()の呼び出しとはならない)。

なお、オブジェクトの解放は生成とは逆の順番で行われる。

### RTTI <a id="SS_6_4_9"></a>
RTTI(Run-time Type Information)とは、プログラム実行中のオブジェクトの型を導出するための機能であり、
具体的には下記の3つの要素を指す。

* [dynamic_cast](#SS_6_4_9_1)
* [typeid](#SS_6_4_9_2)
* [std::type_info](#SS_6_4_9_3)


#### dynamic_cast <a id="SS_6_4_9_1"></a>
dynamic_castは、実行時の型チェックと安全なダウンキャストを行うためのキャスト演算子であるため、
[ポリモーフィックなクラス](#SS_6_4_8)とは密接な関係を持つ。


下記のような[ポリモーフィックなクラス](#SS_6_4_8)に対しては、

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 8

    class Polymorphic_Base {  // ポリモーフィックな基底クラス
    public:
        virtual ~Polymorphic_Base() = default;
    };

    class Polymorphic_Derived : public Polymorphic_Base {  // ポリモーフィックな派生クラス
    };
```

dynamic_castは下記のように振舞う。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 25

    auto b = Polymorphic_Base{};
    auto d = Polymorphic_Derived{};

    Polymorphic_Base& b_ref_d = d;
    Polymorphic_Base& b_ref_b = b;

    // ポインタへのdynamic_cast
    auto* d_ptr = dynamic_cast<Polymorphic_Derived*>(&b_ref_d);
    ASSERT_EQ(d_ptr, &d);

    auto* d_ptr2 = dynamic_cast<Polymorphic_Derived*>(&b_ref_b);
    ASSERT_EQ(d_ptr2, nullptr);  // キャストできない場合、nullptrが返る

    // リファレンスへのdynamic_cast
    auto& d_ref = dynamic_cast<Polymorphic_Derived&>(b_ref_d);
    ASSERT_EQ(&d_ref, &d);

    // キャストできない場合、エクセプションのが発生する
    ASSERT_THROW(dynamic_cast<Polymorphic_Derived&>(b_ref_b), std::bad_cast);
```


一方で、下記のような非[ポリモーフィックなクラス](#SS_6_4_8)に対しては、

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 102

    class NonPolymorphic_Base {  // 非ポリモーフィックな基底クラス
    };

    class NonPolymorphic_Derived : public NonPolymorphic_Base {  // 非ポリモーフィックな派生クラス
    };
```

dynamic_castは下記のように振舞う。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 115

    auto b = NonPolymorphic_Base{};
    auto d = NonPolymorphic_Derived{};

    NonPolymorphic_Base& b_ref_d = d;
    NonPolymorphic_Base& b_ref_b = b;

    #if 0  // 非ポリモーフィックなクラスへのdynamic_castはill-formedになる
    auto* d_ptr = dynamic_cast<NonPolymorphic_Derived*>(&b_ref_d);
    auto* d_ptr2 = dynamic_cast<NonPolymorphic_Derived*>(&b_ref_b);
    
    //virtual関数を持たないため、リファレンスへのdynamic_castはコンパイルできない
    auto& d_ref = dynamic_cast<NonPolymorphic_Derived&>(b_ref_d);
    ASSERT_THROW(dynamic_cast<NonPolymorphic_Derived&>(b_ref_b), std::bad_cast);
    #endif
```

#### typeid <a id="SS_6_4_9_2"></a>
typeidは[RTTI](#SS_6_4_9)オブジェクトの型情報
([std::type_info](#SS_6_4_9_3))を実行時に取得するための演算子である。
dynamic_castとは違い、
typeidのオペランドは[ポリモーフィックなクラス](#SS_6_4_8)のインスタンスでなくても良い。
以下の例では[基本型](#SS_6_1_1)に対するtypeidが返す[std::type_info](#SS_6_4_9_3)の振る舞いを表す。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 52

    int   i{};
    long  j{};
    auto& i_ref = i;

    auto const& type_info_i     = typeid(i);
    auto const& type_info_i_ref = typeid(i_ref);

    ASSERT_NE(typeid(i), typeid(j));
    ASSERT_EQ(type_info_i, type_info_i_ref);
    ASSERT_STREQ(type_info_i.name(), "i");  // 実装定義の型名(clang++/g++ではintはi)
```

下記のような[ポリモーフィックなクラス](#SS_6_4_8)のインスタンスに関して、

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 8

class Polymorphic_Base {  // ポリモーフィックな基底クラス
public:
    virtual ~Polymorphic_Base() = default;
};

class Polymorphic_Derived : public Polymorphic_Base {  // ポリモーフィックな派生クラス
};
```

typeidが返す[std::type_info](#SS_6_4_9_3)オブジェクトは下記のように振舞う。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 65

    auto b = Polymorphic_Base{};
    auto d = Polymorphic_Derived{};

    Polymorphic_Base& b_ref_d = d;
    Polymorphic_Base& b_ref_b = b;

    // ポリモーフィックなクラスインスタンスに対するtypeidが返す
    // std::type_infoオブジェクトが示す型は、オペランドの実際の型である。
    // * b_ref_dの表層の型:Polymorphic_Base
    // * b_ref_dの実際の型:Polymorphic_Derived
    // 下記のアサーションはこのことを表す。
    ASSERT_EQ(typeid(b_ref_d), typeid(d));  // b_ref_dとdの実際の型が同じであることを示す
    ASSERT_EQ(typeid(b_ref_b), typeid(b));  // b_ref_bとbの表層の型が同じであることを示す
```

一方で、下記のような非[ポリモーフィックなクラス](#SS_6_4_8)に対しては、

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 102

    class NonPolymorphic_Base {  // 非ポリモーフィックな基底クラス
    };

    class NonPolymorphic_Derived : public NonPolymorphic_Base {  // 非ポリモーフィックな派生クラス
    };
```

typeidが返す[std::type_info](#SS_6_4_9_3)オブジェクトは下記のように振舞う。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 139

    auto b = NonPolymorphic_Base{};
    auto d = NonPolymorphic_Derived{};

    NonPolymorphic_Base& b_ref_d = d;
    NonPolymorphic_Base& b_ref_b = b;

    // 非ポリモーフィックなクラスインスタンスに対するtypeidが返す
    // std::type_infoオブジェクトが示す型は、オペランドの表層の型である。
    // * b_ref_dの表層の型:Polymorphic_Base
    // * b_ref_dの実際の型:Polymorphic_Derived
    // 下記のアサーションはこのことを表す。
    ASSERT_EQ(typeid(b_ref_d), typeid(b));  // b_ref_dとdの表層の型が同じであることを示す
    ASSERT_EQ(typeid(b_ref_b), typeid(b));  // b_ref_bとbの表層の型が同じであることを示す
```

従って、このような場合のtypeidは静的な型(表層の型)に対しての情報を返すため、
コンパイル時にのみ評価され、ランタイム時に評価されない。

[ポリモーフィックなクラス](#SS_6_4_8)のオブジェクトをオペランドとするtypeidの実行は、
そのオペランドの実際のオブジェクトの型を取得することはすでに示した。
このような場合、オペランド式は実行時に評価される。以下のコードはそのことを表している。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 87

    Polymorphic_Base    base;
    Polymorphic_Derived derived;
    Polymorphic_Base*   base_ptr = &derived;

    ASSERT_EQ(typeid(Polymorphic_Derived), typeid(*base_ptr));
    ASSERT_EQ(typeid(Polymorphic_Base), typeid(*(base_ptr = &base)));  // 注意

    // ポリモーフィックなクラスは対しては、typeid内の式が実行される
    ASSERT_EQ(base_ptr, &base);  // base_ptr = &baseが実行される
```


一方、非[ポリモーフィックなクラス](#SS_6_4_8)のオブジェクトをオペランドとするtypeidのオペランド式は、
コンパイル時に処理されるため、その式は実行されない。以下のコードはそのことを表している。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 161

    NonPolymorphic_Base    base;
    NonPolymorphic_Derived derived;
    NonPolymorphic_Base*   base_ptr = &derived;

    ASSERT_NE(typeid(NonPolymorphic_Derived), typeid(*base_ptr));
    ASSERT_EQ(typeid(NonPolymorphic_Base), typeid(*(base_ptr = &base)));  // 注意

    // 非ポリモーフィックなクラスに対しては、typeid内の式は実行されない
    ASSERT_EQ(base_ptr, &derived);  // base_ptr = &baseは実行されない
```

#### std::type_info <a id="SS_6_4_9_3"></a>
type_infoクラスは、[typeid](----)演算子によって返される、型の情報が格納された型である。

std::type_infoはコンパイラの実装で定義された型名を含んでいる。
以下のコードで示したように`std::type_info::name()`によりその型名を取り出すことができる。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 179

    auto s = std::string{"str"};
    auto v = std::string_view{"str"};
    auto b = std::byte{0b1001};

    ASSERT_STREQ(typeid(s).name(), "Ss");       // 実装定義の型名
    ASSERT_STREQ(typeid(b).name(), "St4byte");  // 実装定義の型名
    ASSERT_STREQ(typeid(v).name(), "St17basic_string_viewIcSt11char_traitsIcEE");
```

`std::type_info::name()`が返すCスタイルの文字列リテラルを、
「人間が認知できる元の型名に戻す関数」を通常のコンパイラは独自に提供する。
このドキュメントのコードのコンパイルに使用している[g++](#SS_8_13_1)/[clang++](#SS_8_13_2)では、
そのような関数は、`abi::__cxa_demangle`である。

`std::type_info::name()`と`abi::__cxa_demangle`を利用して、
オブジェクトの[被修飾型](#SS_6_14_6)名をstd::stringオブジェクトとして取り出す関数とその使用例を以下に示す。

```cpp
    //  example/core_lang_spec/rtti_ut.cpp 191

    #include <cxxabi.h>  // g++/clang++実装依存ヘッダ abi::__cxa_demangleの宣言

    #include <memory>
    #include <string>

    template <typename T>
    std::string type2str(T&& obj)
    {
        int status;

        // objに基づく型情報を取得
        auto demangled = std::unique_ptr<char, decltype(&std::free)>{abi::__cxa_demangle(typeid(obj).name(), 0, 0, &status),
                                                                     &std::free};

        return demangled ? demangled.get() : "unknown";
    }
```
```cpp
    //  example/core_lang_spec/rtti_ut.cpp 213

    int   i{};
    auto  s     = std::string{"str"};
    auto& s_ref = s;
    auto  v     = std::string_view{"str"};

    ASSERT_EQ(type2str(i), "int");
    ASSERT_EQ(type2str(s), "std::string");
    ASSERT_EQ(type2str(s_ref), "std::string");
    ASSERT_EQ(type2str(v), "std::basic_string_view<char, std::char_traits<char> >");

    auto b = Polymorphic_Base{};
    auto d = Polymorphic_Derived{};

    Polymorphic_Base& b_ref_d = d;
    Polymorphic_Base& b_ref_b = b;

    ASSERT_EQ(type2str(b_ref_d), "Polymorphic_Derived");  // b_ref_dの実際の型はPolymorphic_Derived
    ASSERT_EQ(type2str(b_ref_b), "Polymorphic_Base");     // b_ref_bの実際の型はPolymorphic_Base
```

### Run-time Type Information <a id="SS_6_4_10"></a>
「[RTTI](#SS_6_4_9)」を参照せよ。


### インターフェースクラス <a id="SS_6_4_11"></a>
インターフェースクラスとは、純粋仮想関数のみを持つ抽象クラスのことを指す。
インターフェースクラスは、クラスの実装を提供することなく、
クラスのインターフェースを定義するために使用される。
インターフェースクラスは、クラスの仕様を定義するために使用されるため、
多くの場合、抽象基底クラスとして使用される。

```cpp
    //  example/core_lang_spec/interface_class.cpp 8

    class InterfaceClass {  // インターフェースクラス
    public:
        virtual void DoSomething(int32_t) = 0;
        virtual bool IsXxx() const        = 0;
        virtual ~InterfaceClass()         = 0;
    };

    class NotInterfaceClass {  // メンバ変数があるためインターフェースクラスではない
    public:
        NotInterfaceClass();
        virtual void DoSomething(int32_t) = 0;
        virtual bool IsXxx() const        = 0;
        virtual ~NotInterfaceClass()      = 0;

    private:
        int32_t num_;
    };
```

### constインスタンス <a id="SS_6_4_12"></a>
constインスタンスは、ランタイムまたはコンパイル時に初期化され、
その後、状態が不変であるインスタンスである。
必ずしも以下に示すようにconstインスタンスがコンパイル時に値が定まっているわけではない。
[constexprインスタンス](#SS_6_5_6)はconstインスタンスである。
C++03までのコンパイラに、
最適化の一環で`static const`インスタンスを[constexprインスタンス](#SS_6_5_6)と扱うものもあった。


```cpp
    //  example/core_lang_spec/const_ut.cpp 12

    using namespace std;
    auto const str = string{"str"};  // strはプログラムがこの行を通過するときに初期化

    char const* c_str = str.c_str();

    static_assert(!is_const_v<decltype(c_str)>);
    c_str = nullptr;                                                  // c_strは変数としてconstではない
    static_assert(is_const_v<remove_reference_t<decltype(*c_str)>>);  // *cは_strはconst
    static_assert(is_same_v<char const&, decltype(*c_str)>);          // *c_strはconstリファレンス

    char const* const cc_str = c_str;

    static_assert(is_const_v<decltype(cc_str)>);
    // cc_str = nullptr;  // cc_strは変数としてconstであるためコンパイルエラー
    static_assert(is_const_v<remove_reference_t<decltype(*cc_str)>>);  // *cc_strはconst
    static_assert(is_same_v<char const&, decltype(*cc_str)>);          // *cc_strはconstリファレンス

    constexpr int c_int = 1;
    static_assert(is_const_v<decltype(c_int)>);  // c_intはcons
```

## 定数式とコンパイル時評価 <a id="SS_6_5"></a>

### constexpr <a id="SS_6_5_1"></a>
constexprはC++11で導入されたキーワードで、
関数や変数をコンパイル時に評価可能にする。
これにより、定数計算がコンパイル時に行われ、
実行時のパフォーマンスが向上し、コンパイル時にエラーを検出できることがある。

### constexpr定数 <a id="SS_6_5_2"></a>
C++11以前で定数を定義する方法は、

* マクロ定数
* [enum](#SS_6_3_1)
* static const(定数となるか否かは、コンパイラの実装依存に依存する)

の方法があったが、それぞれの方法には下記のような問題がある。

* マクロにはスコープが無く、`#undef`できてしまう。
* enumには整数の定義に限られる。
* static constに関しては、コンパイラの実装依存に依存する。

こういった問題を解決できるのがconstexpr定数である。constexpr定数とは下記のような定数を指す。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 11

    template <int N>
    struct Templ {
        static constexpr auto value = N;  // valueは定数
    };
```
```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 20

    constexpr int a = 5;  // aは定数であるためかきのような使い方ができる
    static_assert(a == 5);

    constexpr int b = 5;  // bは定数でないため、下記のような使い方ができない
    // static_assert(b == 5);  // コンパイルエラー

    constexpr double PI{3.14159265358979323846};  // PIはconstexpr

    auto templ = Templ<a>{};  // aはconstexprなのでaの初期化が可能

    static_assert(templ.value == 5);
```

constexpr定数がif文のオカレンスになる場合、[constexpr if文](#SS_6_11_12)することで、
[ill-formed](#SS_6_14_1)を使用した場合分けが可能になる。


### constexpr関数 <a id="SS_6_5_3"></a>
関数に`constexpr`をつけて宣言することで定数を定義することができる。
constexpr関数の呼び出し式の値がコンパイル時に確定する場合、
その値はconstexpr定数となるため、関数呼び出しが発生しないため、実行効率が向上する。
一方で、constexpr関数の呼び出し式の値が、コンパイル時に確定しない場合、
通常の関数呼び出しと同じになる。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 39

    constexpr int f(int a) noexcept { return a * 3; }  // aがconstexprならばf(a)もconstexpr
    int g(int a) noexcept { return a * 3; }            // aがconstexprであってもg(a)は非constexpr
```
```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 49

    auto x = int{0};

    constexpr auto a = f(3);     // f(3)はconstexprなのでaの初期化が可能
    // constexpr auto b = f(x);  // xは非constexprなのでbの初期化はコンパイルエラー
    auto const c = f(3);         // cはconstexpr定数と定義とすべき
    // constexpr auto d = g(3);  // g(3)は非constexprなのでdの初期化はコンパイルエラー
    auto const e = g(x);         // eはここで初期化して、この後不変
```

C++11の規約では、constexpr関数の制約は厳しく、
for/if文や条件分岐のような処理を含むことができなかったため、
下記のコード例で示した通り、条件演算子とリカーシブコールをうことが多かった。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 64

    constexpr uint64_t bit_mask(uint32_t max) { return max == 0 ? 0 : (1ULL << (max - 1)) | bit_mask(max - 1); }
    constexpr uint64_t bit_mask_0 = bit_mask(4);  // C++11ではコンパイルエラー
    static_assert(0b1111 == bit_mask_0);
```
このため、可読性、保守性があったため、C++14で制約が緩和され、
さらにC++17では for/if文などの一般的な制御構文も使えるようになった。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 70

    constexpr uint64_t bit_mask_for(uint32_t max)
    {
        uint64_t ret = 0;

        for (auto i = 0u; i < max; ++i) {
            ret |= 1ULL << i;
        }

        return ret;
    }
    constexpr uint64_t bit_mask_1 = bit_mask_for(4);  // C++17からサポート
    static_assert(0b1111 == bit_mask_1);
```

### コア定数式 <a id="SS_6_5_4"></a>
コア定数式(core constant expression)とは以下の条件を満たす式である。

1. 以下のいずれかに該当する式であること  
   - リテラル
   - constexpr変数への参照
   - 定数式で初期化された参照
   - constexprサブオブジェクトへの参照
   - constexpr関数呼び出し
   - sizeof演算子の適用結果
   - typeid演算子の適用結果(式の値が[ポリモーフィックなクラス](#SS_6_4_8)である場合を除く)

2. 以下のすべてを満たすこと:  
   - 浮動小数点の比較演算を含まない
   - インクリメント/デクリメント演算を含まない
   - 代入演算を含まない
   - 動的メモリ割り当てを含まない
   - 仮想関数の呼び出しを含まない
   - 未定義動作を引き起こさない
   - エクセプションを投げない
   - アドレス取得演算子の使用が定数式の評価に限定される

3. その式の評価において:  
   - すべてのサブ式も定数式である
   - 使用されるすべての変数は定数式で初期化されている
   - 呼び出されるすべての関数はconstexpr関数である

このドキュメントでは慣用的に[constexpr定数](#SS_6_5_2)と呼んでいる概念が、コア定数式である。

### リテラル型 <a id="SS_6_5_5"></a>
constexpr導入後のC++11の標準では、下記の条件を満たすクラスは、

* constexprコンストラクタを持つ
* すべてのメンバ変数がリテラル型である
* 仮想関数や仮想基底クラスを持たない

constexpr定数もしくはconstexprインスタンスをコンストラクタに渡すことにより、
[constexprインスタンス](#SS_6_5_6)を生成できる。

このようなクラスは慣習的にリテラル型(literal type)と呼ばれる。

以下にリテラル型を例示する。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 87

    class Integer {
    public:
        constexpr Integer(int32_t integer) noexcept : integer_{integer} {}
        constexpr operator int() const noexcept { return integer_; }  // constexprメンバ関数はconst
        constexpr int32_t Allways2() const noexcept { return 2; }     // constexprメンバ関数はconst
        static constexpr int32_t Allways3() noexcept { return 3; }    // static関数のconstexpr化

    private:
        int32_t integer_;
    };
```
```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 105

    constexpr auto i5 = 5;                // i5はconstexprインスタンス
    constexpr auto int_5 = Integer{i5};   // int_5はconstexprインスタンス
    static_assert(int_5 == 5);            // intへの暗黙の型変換

    auto i3  = 3;                         // i3はconstexpr定数ではない
    auto int_3 = Integer{i3};             // int_3はconstexprインスタンスではない
    // static_assert(int_3 == 5);         // int_3がconstexprではないため、コンパイルエラー
    static_assert(int_3.Allways2() == 2); // int_3はconstexprインスタンスではないが、
                                          // int_3.Allways2()はconstexprt定数
    static_assert(int_3.Allways3() == 3); // int_3はconstexprインスタンスではないが、
                                          // int_3.Allways3()はconstexprt定数
```

### constexprインスタンス <a id="SS_6_5_6"></a>
[constexpr定数](#SS_6_5_2)を引数にして、[リテラル型](#SS_6_5_5)のconstexprコンストラクタを呼び出せば、
constexprインスタンスを生成できる。このリテラル型を使用して下記のように[ユーザー定義リテラル](#SS_6_2_6)
を定義することで、constexprインスタンスをより簡易に使用することができるようになる。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 122

    constexpr Integer operator"" _i(unsigned long long int value)  // ユーザ定義リテラルの定義
    {
        return Integer(static_cast<int32_t>(value));
    }
```
```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 132

    constexpr auto i = 123_i;
    static_assert(i == 123);
    static_assert(std::is_same_v<decltype(i), Integer const>);
```

### consteval <a id="SS_6_5_7"></a>
constevalはC++20から導入されたキーワードであり、
呼び出しが必ずコンパイル時に評価されなければならない関数を定義するために使用される。
この関数は、コンパイル時に評価できない引数や式が与えられるとコンパイルエラーとなる。
constexpr関数が「コンパイル時に評価されることもできる」のに対し、
consteval関数は「必ずコンパイル時に評価されなければならない」という点で異なる。

この特性により、ランタイム評価を完全に排除した定数生成専用関数を記述でき、
パフォーマンスの最適化や定数検証（static_assertなど）に利用できる。
consteval関数の呼び出しは、その結果が定数式でなければコンパイルエラーとなる。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 154

    #if __cplusplus >= 202002L  // c++20
    consteval uint64_t bit_mask(uint32_t max)  // コンパイル時、評価ができなければエラー

    #else // C++17
    constexpr uint64_t bit_mask(uint32_t max)  // コンパイル時、評価されるとは限らない
    #endif
    {
        if (max == 0) {
            return 0;
        }
        else {
            return (1ULL << (max - 1)) | bit_mask(max - 1);
        }
    }
```
```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 176

    static_assert(0b1111'1111 == bit_mask(8));

    // auto i = 8UL;         // bit_maskがconstevalであるため、コンパイルエラー
    constexpr auto i = 8UL;  // iがconstexprであるためbit_maskがコンパイル時評価されるため、
    auto bm = bit_mask(i);   // bit_mask(i)の呼び出しは効率的になる
                             // bmをconsexprにするとさらに効率的になる

    ASSERT_EQ(0b1111'1111, bm);
```

### constinit <a id="SS_6_5_8"></a>
constinitはC++20から導入されたキーワードであり、
静的記憶域期間（static、namespaceスコープ）またはthread_local変数が、
コンパイル時に初期化されることを保証するために使用される。
これにより、[Static Initialization Order Fiasco(静的初期化順序問題)](#SS_8_12_12)を回避できる。

このキーワードを付与すると、初期化が動的である場合にはコンパイルエラーとなる。
ただし、constexprと異なり、変数自体がconstになるわけではないため、再代入は可能である。
また、constinitはローカル(自動変数)には意味を持たない。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 192

    #if __cplusplus >= 202002L  // c++20

    // constinit は静的・スレッドローカル変数の初期化が動的でないことを保証する。
    // この変数は const にはならず、後から変更可能である。
    constinit float pi = 3.14f;

    // C++17以前ではconstinitが存在しないため、constexprを使用する。
    // ただしconstexprでは変数がconstになり、再代入はできない点が異なる。
    constinit uint32_t mask = bit_mask(16);

    #else  // C++17

    // C++17ではconstinitが存在しないため、constexprを代用する。
    // ただしconstexprでは変数がconstとなり、再代入はできない。
    constexpr float    pi   = 3.14f;
    constexpr uint32_t mask = bit_mask(16);
    #endif
```

### constexprラムダ <a id="SS_6_5_9"></a>
constexprラムダはC++17から導入された機能であり、以下の条件を満たした[ラムダ式](#SS_6_10_3)である。

* 引数やラムダ式内の処理がコンパイル時に評価可能である必要がある。
  すべての処理はconstexpr関数のようにコンパイル時に確定する必要があり、
  動的な処理やランタイムでしか決定できないものは含めることができない。

* ラムダ内で使用される関数や式もconstexprでなければならない。
  たとえば、関数の呼び出しや算術演算は、コンパイル時に評価可能なものであることが求められる。

* ラムダキャプチャはconstexprに適合している必要がある。
  キャプチャする変数もコンパイル時に確定できるものに限られる。
  動的な変数をキャプチャすると、コンパイルエラーとなる。

* エクセプション処理 (try/catch/throw) が禁止されている。
  constexprラムダでは、エクセプション処理を含むことはできない。

* 動的メモリの割り当て(new/delete) が禁止されている。
  これらの操作はコンパイル時には行えないため、constexprラムダでは使用できない。

```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 217

    constexpr auto factorial = [](int n) {  // constexpr ラムダの定義
        int result = 1;
        for (int i = 2; i <= n; ++i) {
            result *= i;
        }
        return result;
    };

    constexpr int fact_5 = factorial(5);  // コンパイル時に計算される
    static_assert(fact_5 == 120);
```
```cpp
    //  example/core_lang_spec/constexpr_ut.cpp 234

    constexpr auto factorial = [](auto self, int n) -> int {  // リカーシブconstexprラムダ
        return (n <= 1) ? 1 : n * self(self, n - 1);
    };

    constexpr int fact_5 = factorial(factorial, 5);  // コンパイル時の評価
    static_assert(fact_5 == 120);
```

## オブジェクト生成と初期化 <a id="SS_6_6"></a>
### 特殊メンバ関数 <a id="SS_6_6_1"></a>
特殊メンバ関数とは下記の関数を指す。

* デフォルトコンストラクタ
* copyコンストラクタ
* copy代入演算子
* moveコンストラクタ
* move代入演算子
* デストラクタ

以下のメンバ関数は特殊関数ではないが、C++20から特殊関数と同様に`=default`とすることで自動生成される。

* [==演算子](#SS_6_6_3)  
  クラス内のすべてのメンバが==をサポートしている場合、`= default`とすることで自動生成される。
* [<=>演算子](#SS_6_6_4_1)  
  すべてのメンバが[<=>演算子](#SS_6_6_4_1)での比較可能である場合、`= default`とすることで自動生成される。 

ユーザがこれらを一切定義しない場合、または一部のみを定義する場合、
コンパイラは、下記のテーブル等で示すルールに従い、特殊関数メンバの宣言、定義の状態を定める。

左1列目がユーザによる各関数の宣言を表し、2列目以降はユーザ宣言の影響による各関数の宣言の状態を表す。  
下記表において、

* 「`= default`」とは、「コンパイラによってその関数が`= default`と宣言された」状態であることを表す。
* 「~~= default~~」とは、`= default`と同じであるが、バグが発生しやすいので推奨されない。
* 「宣言無し」とは、「コンパイラによってその関数が`= default`と宣言された状態ではない」ことを表す。
    * 「moveコンストラクタが`= default`と宣言された状態ではない」且つ
      「copyコンストラクタが宣言されている」場合、
      rvalueを使用したオブジェクトの初期化には、
      moveコンストラクタの代わりにcopyコンストラクタが使われる。
    * 「move代入演算子が`= default`と宣言された状態ではない」且つ
      「copy代入演算子が宣言されている」場合、
      rvalueを使用したオブジェクトの代入には、
      move代入演算子の代わりにcopy代入演算子が使われる。
* 「= delete」とは「コンパイラによってその関数が= deleteと宣言された」状態であることを表す。

|  user-defined  |default ctor|   dtor  |  copy ctor  | copy assign |move ctor|move assign|   `==`   |   `<=>`  |
|:--------------:|:----------:|:-------:|:-----------:|:-----------:|:-------:|:---------:|:--------:|:--------:|
|   undeclared   |  = default |= default|  = default  |  = default  |= default| = default |undeclared|undeclared|
|non-default ctor| undeclared |= default|  = default  |  = default  |= default| = default |undeclared|undeclared|
|  default ctor  |      -     |= default|  = default  |  = default  |= default| = default |undeclared|undeclared|
|      dtor      |  = default |    -    |~~= default~~|~~= default~~|= default| = default |undeclared|undeclared|
|    copy ctor   |  = default |= default|      -      |~~= default~~|= default| = default |undeclared|undeclared|
|   copy assign  |  = default |= default|~~= default~~|      -      |= default| = default |undeclared|undeclared|
|    move ctor   |  = default |= default|   = delete  |   = delete  |    -    | = default |undeclared|undeclared|
|   move assign  |  = default |= default|   = delete  |   = delete  |= default|     -     |undeclared|undeclared|
|      `==`      |      -     |    -    |      -      |      -      |    -    |     -     |     -    |undeclared|
|      `<=>`     |      -     |    -    |      -      |      -      |    -    |     -     |undeclared|     -    |


**テーブル注**  

* C++14以前と、C++17以降での仕様の差は以下のようになる。
    * C++14以前では、コピーコンストラクタやコピー代入演算子をユーザ定義すると、
      ムーブコンストラクタ／ムーブ代入演算子は自動生成されず` = delete`となる。
    * C++17以降では、コピー系をユーザ定義していても、ムーブ系は自動生成される(` = default`と同等になる)ことがある。
      コンパイラは「コピー系の存在」だけではムーブ系を削除しない。
      ただし、ムーブ不可能なメンバや基底がある場合は、結果的に` = delete`になる。
    * C++17以降では、` = default`された特殊メンバ関数は明示的に`noexcept`推定され、ムーブセマンティクスの活用がしやすくなる。
    * C++20以降では、比較演算子(`==, <=>`)も`= default`によって自動生成可能だが、特殊メンバ関数とは分類が異なるが、
      上記テーブルでは同じように扱う。
* ctor: コンストラクタを指す。
* dtor: デストラクタを指す。
* assign: 代入演算子（assignment）を指す。
* user-defined: この列の関数がユーザによって定義されていることを指す。
  従って、non-default ctorは、デフォルトコンストラクタでないコンストラクタが定義されている行を指す。
* undeclared: 特定の特殊メンバ関数がユーザによって宣言されていないことを指し、
  コンパイラによる自動生成もされていないことを指す。
* 「~~= default~~」とは、`= default`と同様に自動生成されるが、
  場合によっては不適切な挙動を引き起こす可能性があるため、推奨されない。


上記表より、下記のようなことがわかる。

* ユーザが上記6メンバ関数を一切宣言しない場合、それらはコンパイラにより暗黙に宣言、定義される。
* ユーザがcopyコンストラクタを宣言した場合、デフォルトコンストラクタは暗黙に宣言、定義されない。
* moveコンストラクタ、move代入演算子は、
  以下のいずれもが明示的に宣言されていない場合にのみ暗黙に宣言、定義される。
    * copyコンストラクタ
    * copy代入演算子(operator =)
    * moveコンストラクタ
    * move代入演算子
    * デストラクタ

* ユーザがmoveコンストラクタまたはmove代入演算子を宣言した場合、
  copyコンストラクタ、copy代入演算子は`= delete`される。


これらの特殊メンバ関数に対しての設計のガイドラインには、以下のようなものがある。

* [ゼロの原則(Rule of Zero)](#SS_8_7_1)
* [五の原則(Rule of Five)](#SS_8_7_2)

この2つの原則(ガイドライン)の使い分けに関しては、

* リソース管理を外部([RAII(scoped guard)](#SS_8_1_2)クラス)に任せられる場合: ゼロの法則を採用し、特殊メンバ関数を明示的に定義しない。
* リソースをクラス内で直接管理する場合: 五の法則を採用し、すべての特殊メンバ関数を適切に定義する。

とすることで安全で保守性性の高いコードを設計できる。

#### 初期化子リストコンストラクタ <a id="SS_6_6_1_1"></a>
初期化子リストコンストラクタ([リスト初期化](#SS_6_6_5)用のコンストラクタ)とは、
{}による[リスト初期化](#SS_6_6_5)をサポートするためのコンストラクタである。
下記コードでは、 E::E(std::initializer_list\<uint32_t>)が初期化子リストコンストラクタである。

```cpp
    //  example/core_lang_spec/constructor_ut.cpp 6

    class E {
    public:
        E() : str_{"default constructor"} {}

        // 初期化子リストコンストラクタ
        explicit E(std::initializer_list<uint32_t>) : str_{"initializer list constructor"} {}

        explicit E(uint32_t, uint32_t) : str_{"uint32_t uint32_t constructor"} {}

        std::string const& GetString() const { return str_; }

    private:
        std::string const str_;
    };

    TEST(Constructor, initializer_list_constructor)
    {
        E const e0;
        ASSERT_EQ("default constructor", e0.GetString());

        E const e1{};
        ASSERT_EQ("default constructor", e1.GetString());

        E const e2{3, 4};  // E::E(uint32_t, uint32_t)の呼び出しと区別が困難
        ASSERT_EQ("initializer list constructor", e2.GetString());

        E const e3(3, 4);  // E::E(std::initializer_list<uint32_t>)の呼び出しと区別が困難
        ASSERT_EQ("uint32_t uint32_t constructor", e3.GetString());
    }
```

デフォルトコンストラクタと初期化子リストコンストラクタが、
それぞれに定義されているクラスの初期化時に空の初期化子リストが渡された場合、
デフォルトコンストラクタが呼び出される。

初期化子リストコンストラクタと、
「その初期化子リストの要素型と同じ型の仮引数のみを受け取るコンストラクタ
(上記コードのE::E(uint32_t, uint32_t))」
の両方を持つクラスの初期化時にどちらでも呼び出せる初期化子リストが渡された場合({}を使った呼び出し)、
初期化子コンストラクタが呼び出される。

#### 継承コンストラクタ <a id="SS_6_6_1_2"></a>
継承コンストラクタとは、基底クラスで定義したコンストラクタ群を、
派生クラスのインターフェースとしても使用できるようにするための機能である。
下記コードのように、継承コンストラクタは派生クラス内でusingを用いて宣言される。

```cpp
    //  example/core_lang_spec/constructor_ut.cpp 40

    class Base {
    public:
        explicit Base(int32_t b) noexcept : b_{b} {}
        virtual ~Base() = default;
        // ...
    };

    class Derived : public Base {
    public:
        using Base::Base;  // 継承コンストラクタ
    #if 0
        Derived(int32_t b) : Base{b} {}  // オールドスタイル
    #endif
    };

    void f() noexcept
    {
        Derived d{1};  // Derived::Derived(int32_t)が使える
        // ...
    }
```

#### 委譲コンストラクタ <a id="SS_6_6_1_3"></a>
委譲コンストラクタとは、コンストラクタから同じクラスの他のコンストラクタに処理を委譲する機能である。
以下のコード中では、委譲コンストラクタを使い、
A::A(uint32_t)の処理をA::A(std::string const&)へ委譲している。

```cpp
    //  example/core_lang_spec/constructor_ut.cpp 72

    class A {
    public:
        explicit A(std::string str) : str_{std::move(str)}
        {
            // ...
        }

        explicit A(uint32_t num) : A{std::to_string(num)}  // 委譲コンストラクタ
        {
        }

    private:
        std::string str_;
    };
```

### explicit コンストラクタと型変換制御 <a id="SS_6_6_2"></a>

#### explicit <a id="SS_6_6_2_1"></a>
explicitは、コンストラクタに対して付与することで、
コンストラクタによる暗黙の型変換を禁止するためのキーワードである。
暗黙の型変換とは、ある型の値を別の型の値に自動的に変換する言語機能を指す。
explicitキーワードを付けることで、意図しない型変換を防ぎ、コードの堅牢性を高めることがでできる。

この節で説明するexplicitの機能は下記のような項目に渡って説明を行う。

- [暗黙の型変換](#SS_6_6_2_2)
- [暗黙の型変換抑止](#SS_6_6_2_3)
- [explicit(COND)](#SS_6_6_2_4)
- [explicit type operator()](#SS_6_6_2_5)

#### 暗黙の型変換 <a id="SS_6_6_2_2"></a>
この節で扱う暗黙の型変換とは、
以下に示したような「非explicitなコンストラクタを持つクラス」による暗黙の型変換を指し、
[汎整数型昇格](#SS_6_1_7)や[算術変換](#SS_6_1_6)等を指さない。

```cpp
    //  example/core_lang_spec/implicit_conversion_ut.cpp 8

    class Person {
    public:
        Person(char const* name, uint32_t age = 0) : name_{name}, age_{age} {}
        Person(Person const&)            = default;
        Person& operator=(Person const&) = default;

        std::string const& GetName() const noexcept { return name_; }
        uint32_t           GetAge() const noexcept { return age_; }

    private:
        std::string name_;  // コピーをするため非const
        uint32_t    age_;
    };

    #if __cplusplus <= 201703L  // c++17
    bool operator==(Person const& lhs, Person const& rhs) noexcept
    {
        return std::tuple(lhs.GetName(), lhs.GetAge()) == std::tuple(rhs.GetName(), rhs.GetAge());
    }

    #else  // c++20
    auto operator<=>(Person const& lhs, Person const& rhs) noexcept
    {
        return std::tuple(lhs.GetName(), lhs.GetAge()) <=> std::tuple(rhs.GetName(), rhs.GetAge());
    }

    // <=>から自動的に==が生成されないため、明示的に定義する必要がある
    bool operator==(Person const& lhs, Person const& rhs) noexcept { return (lhs <=> rhs) == 0; }
    #endif
```

上記のクラスPersonを使用して、下記のようなコードをコンパイルできるようにする機能である。

```cpp
    //  example/core_lang_spec/implicit_conversion_ut.cpp 40

    void f(Person const& person) noexcept
    {
        // ...
    }

    void using_implicit_coversion()
    {
        f("Ohtani");  // "Ohtani"はPerson型ではないが、コンパイル可能
    }
```

この記法は下記コードの短縮形であり、コードの見た目をシンプルに保つ効果がある。

```cpp
    //  example/core_lang_spec/implicit_conversion_ut.cpp 54

    void not_using_implicit_coversion()
    {
        f(Person{"Ohtani"});  // 本来は、fの引数はPerson型
    }
```

この記法は下記のようにstd::string等のSTLでも多用され、その効果は十分に発揮されているものの、

```cpp
    //  example/core_lang_spec/implicit_conversion_ut.cpp 66

    auto otani = std::string{"Ohtani"};

    // ...

    if (otani == "Ohtani") {  // 暗黙の型変換によりコンパイルできる
        // ...
    }
```

以下のようなコードがコンパイルできてしまうため、わかりづらいバグの元にもなる。

```cpp
    //  example/core_lang_spec/implicit_conversion_ut.cpp 80

    auto otani = Person{"Ohtani", 26};

    // ...

    if (otani == "Otani") {  // このコードがコンパイルされる。
        // ...
    }

    if (otani == Person{"Otani"}) {  // 暗黙の型変換を使わない記法
        // ...
    }
```

下記のようにコンストラクタにexplicitを付けて宣言することにより、この問題を防ぐことができる。

```cpp
    //  example/core_lang_spec/implicit_conversion_ut.cpp 112

    class Person {
    public:
        explicit Person(char const* name, uint32_t age = 0) : name_{name}, age_{age} {}
        Person(Person const&)            = default;
        Person& operator=(Person const&) = default;

        // ...
    };

    void prohibit_implicit_coversion()
    {
    #if 0  // explicit付きのコンストラクタを持つPersonと違い、コンパイルできない。
        f("Ohtani");
    #else
        f(Person{"Ohtani"});
    #endif

        auto otani = Person{"Ohtani", 26};

        // ...

    #if 0
        if (otani == "Otani") {  // このコードもコンパイルできない。
            // ...
        }
    #else
        if (otani == Person{"Otani", 26}) {  // この記述を強制できる。
            // ...
        }
    #endif
    }
```

std::stringは暗黙の型変換を許して良く、(多くの場合)Personには暗黙の型変換をしない方が良い理由は、

* std::stringの役割は文字列の管理と演算のみであるため、
  std::stringを文字列リテラルと等価なもののように扱っても違和感がない
* Personは、明らかに文字列リテラルと等価なものではない

といった[セマンティクス](#SS_8_14_1)的観点によるものである。

クラスPersonと同様に、
ほとんどのユーザ定義クラスには非explicitなコンストラクタによる暗黙の型変換は必要ない。

#### 暗黙の型変換抑止 <a id="SS_6_6_2_3"></a>
explicit宣言されていないコンストラクタを持つクラスは、
下記のコードのように[暗黙の型変換](#SS_6_6_2_2)が起こる。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 10

    struct A {
        A(int a) : x{a} {}
        int x;
    };

    A f(A a) { return a; };
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 21

    A a = 1;  // A::Aがexplicitでないため、iはA{1}に変換される
    ASSERT_EQ(a.x, 1);

    auto b = f(2);  // A::Aがexplicitでないため、2はA{2}に変換される
    ASSERT_EQ(b.x, 2);
```

暗黙の型変換はわかりづらいバグを生み出してしまうことがあるため、
下記のように適切にexplicitを使うことで、このような変換を抑止することができる。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 34

    struct A {
        explicit A(int a) : x{a} {}  // 暗黙の型変換の抑止
        int x;
    };

    A f(A a) { return a; };
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 45

    // A a = 1;    // A::Aがexplicitであるため、コンパイルエラー
    // auto b = f(2);  // A::Aがexplicitであるため、コンパイルエラー
```

C++03までは、[一様初期化](#SS_6_6_6)がサポートされていなかったため、
explicitは単一引数のコンストラクタに使用されることが一般的であった。

C++11からサポートされた[一様初期化](#SS_6_6_6)を下記のように使用することで、
暗黙の型変換を使用できる。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 56

    struct A {
        A(int a, int b) : x{a}, y{b} {}
        int x;
        int y;
    };

    A    f(A a) { return a; };
    bool operator==(A lhs, A rhs) { return std::tuple(lhs.x, lhs.x) == std::tuple(rhs.x, rhs.x); }
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 70

    A a = {1, 2};  // A::Aがexplicitでないため、iはA{1, 2}に変換される
    ASSERT_EQ(a, (A{1, 2}));

    auto b = f({2, 1});  // A::Aがexplicitでないため、2はA{2,1}に変換される
    ASSERT_EQ(b, (A{2, 1}));
```

以下に示す通り、コンストラクタの引数の数によらず、
C++11からは暗黙の型変換を抑止したい型のコンストラクタにはexplicit宣言することが一般的となっている。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 82

    struct A {
        explicit A(int a, int b) : x{a}, y{b} {}
        int x;
        int y;
    };

    A    f(A a) { return a; };
    bool operator==(A lhs, A rhs) { return std::tuple(lhs.x, lhs.x) == std::tuple(rhs.x, rhs.x); }
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 96

    // A a = {1, 2};  // A::Aがexplicitであるため、コンパイルエラー
    // auto b = f({2, 1});  // A::Aがexplicitであるため、コンパイルエラー
```

#### explicit(COND) <a id="SS_6_6_2_4"></a>
C++20から導入されたexplicit(COND)は、
コンストラクタや変換演算子に対して、
特定の条件下で暗黙の型変換を許可または禁止する機能である。
CONDには、型特性や定数式などの任意のconstexprな条件式を指定できる。
以下にこのシンタックスの単純な使用例を示す。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 162

    template <typename T>  // Tが整数型の場合、暗黙の型変換を許可
    struct S {
    #if __cplusplus >= 202002L  // c++20
        explicit(!std::is_integral_v<T>) S(T x) : value{x} {}

    #else  // c++17
        // T が整数型でない場合に有効なコンストラクタ
        template <typename U = T, std::enable_if_t<!std::is_integral_v<U>>* = nullptr>
        explicit S(U x) : value{x} { }

        // T が整数型の場合に有効な非explicitコンストラクタ
        // T が整数型の場合に有効な非explicitコンストラクタ
        template <typename U = T, std::enable_if_t<std::is_integral_v<U>>* = nullptr>
        S(U x) : value{x} { }
    #endif

        T value;
    };

    template <typename T>  // 推論ガイド
    S(T)->S<T>;
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 190

    S s = 1;      // Tがintであるため、explicit宣言されていないため、暗黙の型変換は許可
    // S t = 1.0; // Tが整数型でないため暗黙の型変換は禁止であるため、コンパイルエラー
    S t{1.0};     // Tが整数型でないが、明示的な初期化は問題ない

    ASSERT_EQ(s.value, 1);
```

テンプレートのパラメータの型による暗黙の型変換の可否をコントロールする例を以下に示す。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 203

    template <typename T>
    struct Optional {
    #if __cplusplus >= 202002L  // c++20
        explicit(std::is_same_v<T, std::nullptr_t>) Optional(const T& value)
            : has_value_(!std::is_same_v<T, std::nullptr_t>), value_(value) { }

    #else  // c++17
        // Tがnullptr_tではない場合に有効なコンストラクタ
        template <typename U = T, std::enable_if_t<!std::is_same_v<U, std::nullptr_t>>* = nullptr>
        Optional(const U& value) : has_value_(true), value_(value) { }

        // Tがnullptr_tの場合に有効なexplicitコンストラクタ
        template <typename U = T, std::enable_if_t<std::is_same_v<U, std::nullptr_t>>* = nullptr>
        explicit Optional(const U& value) : has_value_(false), value_(value) { }
    #endif

        explicit operator bool() const noexcept { return has_value_; }  // bool型への変換
                 operator T() const noexcept { return value_; }         // T型への変換

    private:
        bool has_value_;
        T    value_;
    };
    template <typename T>  // 推論ガイド
    Optional(T)->Optional<T>;
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 235

    Optional a = 2;   // T == intであるため、暗黙の型変換を許可
    ASSERT_TRUE(a);   // has_value_がtrueであるため
    ASSERT_EQ(a, 2);  // T型への暗黙的変換をチェック

    // Optional n = nullptr; // T == std::nullptr_tのため暗黙の型変換抑止により、コンパイルエラー
    Optional n{nullptr};  // 通常の初期化
    ASSERT_FALSE(n);
```

こういった工夫により、コードの過度な柔軟性を適度に保つことができ、
可読性の向上につながる。

#### explicit type operator() <a id="SS_6_6_2_5"></a>
型変換演算子のオーバーロードの戻り値をさらに別の型に変換すると、
きわめてわかりづらいバグを生み出してしまうことがあるため、
この機能を使用すると型変換演算子のオーバーロードの型変換の抑止することができる。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 110

    struct A {
        explicit A(int a) : x{a} {}  // 暗黙の型変換の抑止
        operator bool() const noexcept { return x; }
        int x;
    };
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 123

    auto a = A{2};

    ASSERT_TRUE(a);
    ASSERT_EQ(1, a);  // aをboolに変換するとtrue、trueをintに変換すると1

    int b = a + 1;  // aをboolに変換するとtrue、trueをintに変換すると1であるため、bは2
    ASSERT_EQ(b, 2);

```

以下に示すようにexplicitを使うことで、このような暗黙の型変換を抑止できる。

```cpp
    //  example/core_lang_spec/explicit_ut.cpp 137

    struct A {
        explicit A(int a) : x{a} {}  // 暗黙の型変換の抑止
        explicit operator bool() const noexcept { return x; }// 暗黙の型変換の抑止
        int x;
    };
```
```cpp
    //  example/core_lang_spec/explicit_ut.cpp 150

    auto a = A{2};

    // ASSERT_EQ(1, a);  // operator boolがexplicitであるため、コンパイルエラー
    // int b = a + 1;  // operator boolがexplicitであるため、コンパイルエラー
```

### ==演算子 <a id="SS_6_6_3"></a>
クラスの==演算子の実装方法には、
[メンバ==演算子](#SS_6_6_3_1)、[非メンバ==演算子](#SS_6_6_3_2)の2つの方法がある。

#### メンバ==演算子 <a id="SS_6_6_3_1"></a>
メンバ==演算子には、[非メンバ==演算子](#SS_6_6_3_2)に比べ、下記のようなメリットがある。

* メンバ変数へのアクセスが容易であるため、より実装が単純になりやすい。
* メンバ変数へのアクセスが容易であるため、パフォーマンスが向上する。
* インライン化し易い。

```cpp
    //  example/core_lang_spec/comparison_operator_old_ut.cpp 12

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

すべてのメンバ変数に==演算子が定義されている場合、
C++20以降より、`=default`により==演算子を自動生成させることができるようになった。

```cpp
    //  example/core_lang_spec20/comparison_operator_ut.cpp 11

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        bool operator==(const Integer& other) const noexcept = default;  // 自動生成

    private:
        int x_;
    };
```

#### 非メンバ==演算子 <a id="SS_6_6_3_2"></a>
非メンバ==演算子には、[メンバ==演算子](#SS_6_6_3_1)に比べ、下記のようなメリットがある。

* クラスをよりコンパクトに記述できるが、その副作用として、
  アクセッサやfriend宣言が必要になることがある。

```cpp
    //  example/core_lang_spec/comparison_operator_old_ut.cpp 53

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        // operator==とoperator<だけを定義
        int get() const noexcept { return x_; }

        // メンバ関数の比較演算子に見えるが、非メンバ関数
        friend bool operator==(const Integer& lhs, const Integer& rhs) noexcept { return lhs.x_ == rhs.x_; }

        friend bool operator<(const Integer& lhs, const Integer& rhs) noexcept { return lhs.x_ < rhs.x_; }

    private:
        int x_;
    };
```

* [暗黙の型変換](#SS_6_6_2_2)を利用した以下に示すようなシンプルな記述ができる場合がある。

```cpp
    //  example/core_lang_spec/comparison_operator_old_ut.cpp 75

    auto a = Integer{5};

    ASSERT_TRUE(5 == a);  // 5がInteger{5}に型型変換される
```

すべてのメンバ変数に==演算子が定義されている場合、
C++20以降より、`=default`により==演算子を自動生成させることができるようになった。

```cpp
    //  example/core_lang_spec20/comparison_operator_ut.cpp 35

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        friend bool operator==(Integer const& lhs, Integer const& rhs) noexcept;

    private:
        int x_;
    };

    bool operator==(Integer const& lhs, Integer const& rhs) noexcept = default;  // 自動生成
```

### 比較演算子 <a id="SS_6_6_4"></a>
比較演算子とは、[==演算子](--)の他に、!=、 <=、>、>= <、>を指す。
C++20から導入された[<=>演算子](#SS_6_6_4_1)の定義により、すべてが定義される。

#### <=>演算子 <a id="SS_6_6_4_1"></a>
「[std::tuppleを使用した比較演算子の実装方法](#SS_7_10_2)」
で示した定型のコードはコンパイラが自動生成するのがC++規格のセオリーである。
このためC++20から導入されたのが<=>演算子`<=>`である。

```cpp
    //  example/core_lang_spec20/comparison_operator_ut.cpp 61

    struct Point {
        int x;
        int y;

        auto operator<=>(const Point& other) const noexcept = default;  // 三方比較演算子 (C++20)
        // 通常autoとするが、実際の戻り型はstd::strong_ordering
    };
```
```cpp
    //  example/core_lang_spec20/comparison_operator_ut.cpp 74

    auto p1 = Point{1, 2};
    auto p2 = Point{1, 2};
    auto p3 = Point{2, 3};

    ASSERT_EQ(p1, p2);  // p1 == p2
    ASSERT_NE(p1, p3);  // p1 != p3
    ASSERT_TRUE(p1 < p3);
    ASSERT_FALSE(p1 > p3);

    auto cmp_1_2 = p1 <=> p2;
    auto cmp_1_3 = p1 <=> p3;
    auto cmp_3_1 = p3 <=> p1;
    static_assert(std::is_same_v<std::strong_ordering, decltype(cmp_1_2)>);

    ASSERT_EQ(std::strong_ordering::equal, cmp_1_2);    // 等しい
    ASSERT_EQ(std::strong_ordering::less, cmp_1_3);     // <=>の左オペランドが小さい
    ASSERT_EQ(std::strong_ordering::greater, cmp_3_1);  // <=>の左オペランドが大きい

    // std::strong_orderingの値
    // ASSERT_EQ(static_cast<int32_t>(cmp_1_2), 0); キャストできないのでコンパイルエラー
    ASSERT_TRUE(cmp_1_2 == 0);
    ASSERT_TRUE(cmp_1_3 < 0);  // cmp_1_3は実質的には-1
    ASSERT_TRUE(cmp_3_1 > 0);  // cmp_3_1は実質的には1

```

定型の比較演算子では不十分である場合、<=>演算子を実装する必要が出てくる。
そのような場合に備えて、上記の自動生成コードの内容を敢えて実装して、以下に示す。

```cpp
    //  example/core_lang_spec20/comparison_operator_ut.cpp 105

    struct Point {
        int x;
        int y;

        std::strong_ordering operator<=>(const Point& other) const noexcept
        {
            return std::tie(x, y) <=> std::tie(other.x, other.y);
        }

        bool operator==(const Point& other) const noexcept { return std::tie(x, y) == std::tie(other.x, other.y); }
    };
```

#### 三方比較演算子 <a id="SS_6_6_4_2"></a>
三方比較演算子とは[<=>演算子](#SS_6_6_4_1)を指す。

#### spaceship operator <a id="SS_6_6_4_3"></a>
spaceship operatorとは[<=>演算子](#SS_6_6_4_1)を指す。
この名前は`<=>`が宇宙船に見えることに由来としている。


### リスト初期化 <a id="SS_6_6_5"></a>
リスト初期化とは、C++11で導入された`{}`を使ったオブジェクトの初期化構文を指す。
以下にコード例を示す。

```cpp
    //  example/core_lang_spec/uniform_initialization_ut.cpp 12

    struct X {
        X(int) {}
    };

    X x0(0);   // 通常従来のコンストラクタ呼び出し
    X x1 = 0;  // 暗黙の型変換を使用した従来のコンストラクタ呼び出し

    X x2{0};     // リスト初期化
    X x3 = {0};  // 暗黙の型変換を使用したリスト初期化

    struct Y {
        Y(int, double, std::string) {}
    };

    auto lamda = [](int, double, std::string) -> Y {
        return {1, 3.14, "hello"};  // 暗黙の型変換を使用したリスト初期化でのYの生成
    };
```

変数による一様初期化が縮小型変換を起こす場合や、
リテラルによる一様初期化がその値を変更する場合、コンパイルエラーとなるため、
この機能を積極的に使用することで、縮小型変換による初期化のバグを未然に防ぐことができる。

```cpp
    //  example/core_lang_spec/uniform_initialization_ut.cpp 34

    int i{0};  // リスト初期化

    bool b0 = 7;  // 縮小型変換のため、b0の値はtrue(通常は1)となる
    ASSERT_EQ(b0, 1);

    // bool b1{7};  // 縮小型変換のため、コンパイルエラー
    // bool b2{i};  // 縮小型変換のため、コンパイルエラー

    uint8_t u8_0 = 256;  // 縮小型変換のためu8_0は0となる
    ASSERT_EQ(u8_0, 0);

    // uint8_t u8_1{256};  // 縮小型変換のため、コンパイルエラー
    // uint8_t u8_2{i};    // 縮小型変換のため、コンパイルエラー

    uint8_t array0[3]{1, 2, 255};  // リスト初期化
    // uint8_t array1[3] = {1, 2, 256};  // 縮小型変換のため、コンパイルエラー
    // uint8_t array2[3]{1, 2, 256};     // 縮小型変換のため、コンパイルエラー
    // uint8_t array2[3]{1, 2, i};       // 縮小型変換のため、コンパイルエラー

    int i0 = 1.0;  // 縮小型変換のため、i0の値は1
    ASSERT_EQ(i0, 1);

    // int i1{1.0};  // 縮小型変換のため、コンパイルエラー

    double d{1};  // 縮小型変換は起こらないのでコンパイル可能
    // int i2{d};  // 縮小型変換のため、コンパイルエラー
```

### 一様初期化 <a id="SS_6_6_6"></a>
一様初期化(Uniform Initialization)は 、
[リスト初期化](#SS_6_6_5)による初期化方法がC++における初期化を統一的に扱えるように設計された概念を指さす。

### 非静的なメンバ変数の初期化 <a id="SS_6_6_7"></a>
非静的なメンバ変数の初期化には下記の3つの方法がある。

* [NSDMI](#SS_6_6_7_1)
* [初期化子リストでの初期化](#SS_6_6_7_2)
* [コンストラクタ内での非静的なメンバ変数の初期値の代入](#SS_6_6_7_3)

同一変数に対して、
「[NSDMI](#SS_6_6_7_1)」と「[初期化子リストでの初期化](#SS_6_6_7_2)」
が行われた場合、その変数に対するNSDMIは行われない。


#### NSDMI <a id="SS_6_6_7_1"></a>
NSDMIとは、non-static data member initializerの略語であり、
下記のような非静的なメンバ変数の初期化子を指す。

```cpp
    //  example/core_lang_spec/nsdmi.cpp 11

    class A {
    public:
        A() : a_{1}  // NSDMIではなく、非静的なメンバ初期化子による初期化
        {
        }

    private:
        int32_t     a_;
        int32_t     b_ = 0;        // NSDMI
        std::string str_{"init"};  // NSDMI
    };
```

#### 初期化子リストでの初期化 <a id="SS_6_6_7_2"></a>
「非静的メンバ変数をコンストラクタの本体よりも前に初期化する」言語機能である。
メンバ変数は宣言された順序で初期化されるため、
初期化子リストでの順序は、実際の初期化の順序とは関係がない。

この機能を使うことで、メンバ変数の初期化処理が簡素に記述できる。
constメンバ変数は、初期化子リストでの初期化か[NSDMI](#SS_6_6_7_1)でしか初期化できない。

```cpp
    //  example/core_lang_spec/nsdmi.cpp 27

    class A {
    public:
        A(int a, int b) : v_{a, b, 3}, a_{a}  // 非静的なメンバ初期化子による初期化
        //                 ^^^^^^^^^^^^^ メンバ変数の初期化は
        //                                  - 宣言順に行われる。
        //                                  - 初期化リストの順番と、初期化の順番には関係がない。
        {
        }

    private:
        int              a_;
        std::vector<int> v_;
    };
```

#### コンストラクタ内での非静的なメンバ変数の初期値の代入 <a id="SS_6_6_7_3"></a>
この方法は単なる代入でありメンバ変数の初期化ではない。

[NSDMI](#SS_6_6_7_1)、
[初期化子リストでの初期化](#SS_6_6_7_2)で初期化できない変数を未初期化でない状態にするための唯一の方法である。

```cpp
    //  example/core_lang_spec/nsdmi.cpp 45

    class A {
    public:
        A(int a, int b)
        {
            a_ = b;                     // 非静的なメンバのコンストラクタでの代入
            v_ = std::vector{a, b, 3};  // 非静的なメンバのコンストラクタでの代入
        }

    private:
        int              a_;
        std::vector<int> v_;
    };
```

### オブジェクトのライフタイム <a id="SS_6_6_8"></a>
オブジェクトは、以下のような種類のライフタイムを持つ。

* 静的に生成されたオブジェクトのライフタイム
* thread_localに生成されたオブジェクトのライフタイム
* newで生成されたオブジェクトのライフタイム
* スタック上に生成されたオブジェクトのライフタイム
* prvalue(「[rvalue](#SS_6_7_1_2)」参照)のライフタイム

なお、リファレンスの初期化をrvalueで行った場合、
そのrvalueはリファレンスがスコープを抜けるまで存続し続ける。

rvalueをバインドするリファレンスが存在しない状態で、
そのrvalueがメンバ変数へのリファレンスを返す関数を呼び出し、
そのリファレンスをバインドするリファレンス変数を初期化した場合、
リファレンスが指すオブジェクトはすでにライフタイムを終了している。
このような状態のリファレンスを[danglingリファレンス](#SS_8_11_2)と呼ぶ。
同様に、このような状態のポインタを[danglingポインタ](#SS_8_11_3)と呼ぶ。

### プレースメントnew <a id="SS_6_6_9"></a>
プレースメントnewは、既に確保済みの生ストレージ上で、
オブジェクトを生成するための `new(raw_storage) T(args...)`のような構文である。
通常のnew演算子が「メモリ確保＋初期化」を同時に行うのに対し、プレースメントnewは「初期化のみ」を担当する。
これにより、メモリ確保の責務を呼び出し側に委ねることができ、
アロケーションコストの削減やメモリプールとの統合が可能となる。
また、リアルタイム処理や組込みソフトウェアなど、ヒープからの動的割り当てを避けたい場面でも有用である。

```cpp
    //  example/core_lang_spec/placement_new_ut.cpp 10

    class X {
    public:
        explicit X(int v) : str_{std::to_string(v)} {}
        std::string const& get_str() const noexcept { return str_; }

        ~X() {}

    private:
        std::string str_;
    };
```

上記クラスをプレースメントnewを使用して生成するコード例を以下に示す。

```cpp
    //  example/core_lang_spec/placement_new_ut.cpp 26

    alignas(X) uint8_t memory_[sizeof(X)];
    // alignas(X)はXのアライメント要件(通常4や8バイト境界)に合わせる
    // これがないと、memory_が不適切な境界(例:奇数アドレス)に配置され、
    // 一部のCPUアーキテクチャでクラッシュやパフォーマンス低下を引き起こす

    X* x = new (memory_) X{42};  // X型オブジェクトをmemory_上に生成

    ASSERT_EQ("42", x->get_str());  // 正しく生成されたかどうかの確認

    // ...
    // ... ここでエクセプションが発生して、
    // ... 以下のコードが実行できないとデストラクタが呼ばれないためメモリリークする可能性がある

    x->~X();  // プレースメントしたオブジェクトの解放にはdeleteを使ってはならないため、
              // このように直接デストラクタを呼び出す必要がある
```

このコードからわかる通り、プレースメントnewで生成したオブジェクトは手動でデストラクタを呼び出す必要があるため、
例外が発生した場合にリソースリークのリスクがある。
下記のようにstd::unique_ptrにカスタムデリータを指定することで、この問題を解決できる。

```cpp
    //  example/core_lang_spec/placement_new_ut.cpp 48

    alignas(X) uint8_t memory_[sizeof(X)];

    auto deleter = [](X* p) {  // カスタムデリータの定義
        if (p) {
            p->~X();  // デストラクタのみ呼び出し
        }
    };

    std::unique_ptr<X, decltype(deleter)> x{new (memory_) X{42}, deleter};

    ASSERT_EQ("42", x->get_str());
    // xがスコープアウトするタイミングでカスタムデリータdeleterが呼ばれるため、~X()の呼び出し漏れが回避できる
```

### new (std::nothrow) <a id="SS_6_6_10"></a>
`new (std::nothrow)`は、メモリ確保失敗時に例外を投げずnullptrを返すnewの形式である。
通常のnewはメモリ確保に失敗するとstd::bad_alloc例外を投げるが、
`new (std::nothrow)`はstd::nothrow_t型の引数を取ることで、失敗時にnullptrを返す動作に変更される。
この形式は例外を使わない環境(組み込みシステムなど)や、明示的なnullチェックによるエラー処理が望ましい場合に使用される。
解放方法は通常のnewと同じで、単一オブジェクトの場合はdelete、配列の場合はdelete[]を使用する。

## 値カテゴリとリファレンス <a id="SS_6_7"></a>
ここでは、expression(式)の値カテゴリや、それに付随した機能についての解説を行う。

### expression <a id="SS_6_7_1"></a>

[expression](https://ja.cppreference.com/w/cpp/language/expressions)(式)とは、
「演算子とそのオペランドの並び」である(オペランドのみの記述も式である)。
演算子とは以下のようなものである。

* 四則演算、代入(a = b、a += b ...)、インクリメント、比較、論理式
* 明示的キャストや型変換
* メンバアクセス(a.b、a->b、a[x]、 \*a、&a ...)
* 関数呼び出し演算子(f(...))、sizeof、decltype等


expressionは、

* [lvalue](#SS_6_7_1_1)
* [rvalue](#SS_6_7_1_2)
* [xvalue](#SS_6_7_1_3)
* [glvalue](#SS_6_7_1_5)
* [prvalue](#SS_6_7_1_4)

に分類される。
```essential/plant_uml/rvalue.pu
@startditaa

         expression
+---------------------------+
|                           |
v                           v

      glvalue
+-----------------+
|                 |
V                 v

+--------+--------+---------+
|        |        |         |
| lvalue | xvalue | prvalue |
| cBLU   | cYEL   | cGRE    |
+--------+--------+---------+

         ^                  ^
         |                  |
         +------------------+
                rvalue
@endditaa

```


expressionは、[lvalue](#SS_6_7_1_1)か[rvalue](#SS_6_7_1_2)である。


#### lvalue <a id="SS_6_7_1_1"></a>
lvalueとは、

* 名前を持つオブジェクト(識別子で参照可能)や関数を指す式
* 代入式の左辺になり得る式であるため、左辺値と呼ばれることがある。
* constなlvalueは代入式の左辺にはなり得ないが、lvalueである。
* [rvalue](#SS_6_7_1_2)でない[expression](#SS_6_7_1)がlvalueである。

`T const&`は代入式の左辺になりは得ないがlvalueである。[rvalueリファレンス](#SS_6_8_2)もlvalueである。

#### rvalue <a id="SS_6_7_1_2"></a>
rvalueとは、

* テンポラリな値を表す式(代入式の右辺値として使われることが多い)
* [xvalue](#SS_6_7_1_3)か[prvalue](#SS_6_7_1_4)である。
* [lvalue](#SS_6_7_1_1)でない[expression](#SS_6_7_1)がrvalueである。

[rvalueリファレンス](#SS_6_8_2)(`T&&`型の変数)はlvalueである。
一方、その初期化に使われる式(例えばstd::move(x))は[xvalue](#SS_6_7_1_3)である。


#### xvalue <a id="SS_6_7_1_3"></a>
xvalueとは以下のようなものである。

* 戻り値の型がT&&(Tは任意の型)である関数の呼び出し式(std::move(x))
* オブジェクトへのT&&へのキャスト式(static_cast<char&&>(x))
* aを配列のxvalueとした場合のa[N]や、cをクラス型のrvalueとした場合のc.m(mはaの非staticメンバ)等

#### prvalue <a id="SS_6_7_1_4"></a>
prvalueとは、オブジェクトやビットフィールドを初期化する、
もしくはオペランドの値を計算する式であり、以下のようなものである。

* 文字列リテラルを除くリテラル
* 戻り値の型が非リファレンスである関数呼び出し式、
  または前置++と前置--を除くオーバーロードされた演算子式(`path.string()`、`str1 + str2`、`it++` ...)
* 組み込み型インスタンスaの`a++`、`a--`(`++a`や`--a`はlvalue)
* 組み込み型インスタンスa、bに対する
  `a + b`、 `a % b`、 `a & b`、 `a && b`、 `a || b`、 `!a`、 `a < b`、 `a == b`等
* prvalue(もしくはrvalue)は、
    * アドレス演算子(&)のオペランドになれない。
    * 非constな[lvalueリファレンス](#SS_6_8_1)ではバインドできないが、
      constな[lvalueリファレンス](#SS_6_8_1)や[rvalueリファレンス](#SS_6_8_2)でバインドできる。
  

つまり、prvalueとはいわゆるテンポラリオブジェクトのことである(下記の`std::string{}`で作られるようなオブジェクト)。
多くの場合、prvalueはテンポラリオブジェクトを生成するが、
C++17以降は[RVO(Return Value Optimization)](#SS_6_15_1)により、
テンポラリオブジェクトを生成せず、直接、初期化に使われる場合もある。  
また、正確にはprvalueと呼ぶべき場面でも単にrvalueと呼ばれることがある。
このドキュメントでも、そうなっていることもある。

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 10
    // str0を初期化するためにstd::string{}により生成されるオブジェクトはprvalue、 str0はlvalue
    //   ↓lvalue
    auto str0 = std::string{};  // この式の左辺はテンポラリオブジェクト(つまりprvalue)

    /*
    auto* str0_ptr = &std::string{};  // prvalueのアドレスの取得はできない
    ↑は、メッセージは error: taking address of rvalue でコンパイルエラー */

    /*
    std::string& str1_ref = std::string{};  // prvalueを非constなlvalueリファレンスではバインドできない
    ↑は、コンパイルエラーで、エラーメッセージは error: taking address of rvalue */

    std::string const& str2_ref = std::string{};  // prvalueはconstなlvalueリファレンスでバインドできる
    // ↓のようにすればアドレスを取得できるが、このようなことはすべきではない。
    std::string const* str2_ptr = &str2_ref;  // str_ptrはprvalueのアドレスを指しているが、、、

    auto&& str3_ref = std::string{};  // prvalueはprvalueリファレンスでバインドできる
    // ↓のようにすればアドレスを取得できるが、このようなことはすべきではない。
    std::string* str3_ptr = &str3_ref;  // str_ptrはprvalueのアドレスを指しているが、、、
```

#### glvalue <a id="SS_6_7_1_5"></a>
glvalueは、

* [lvalue](#SS_6_7_1_1)か[xvalue](#SS_6_7_1_3)である。
* "generalized lvalue"の略称

オブジェクトや関数を参照する式を総称してglvalueと呼ぶ。
これにより、式が「場所を指す」か「一時的な値を表す」かを大きく分類できる。


### decltypeとexpression <a id="SS_6_7_2"></a>
エッセンシャルタイプがTであるlvalue、xvalue、prvalueに対して
(例えば、std::string const&のエッセンシャルタイプはstd::stringである)、
decltypeの算出結果は下表のようになる。

|decltype           |算出された型|
|:------------------|:-----------|
|decltype(lvalue)   |T           |
|decltype((lvalue)) |T&          |
|decltype(xvalue)   |T&&         |
|decltype((xvalue)) |T&&         |
|decltype(prvalue)  |T           |
|decltype((prvalue))|T           |

この表の結果を使用した下記の関数型マクロ群により式を分類できる。
定義から明らかな通り、これらは
[テンプレートメタプログラミング](https://ja.wikipedia.org/wiki/%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%A1%E3%82%BF%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0)
に有効に活用できる。

```cpp
    //  example/core_lang_spec/decltype_expression_ut.cpp 7

    #define IS_LVALUE(EXPR_) std::is_lvalue_reference_v<decltype((EXPR_))>
    #define IS_XVALUE(EXPR_) std::is_rvalue_reference_v<decltype((EXPR_))>
    #define IS_PRVALUE(EXPR_) !std::is_reference_v<decltype((EXPR_))>
    #define IS_RVALUE(EXPR_) (IS_PRVALUE(EXPR_) || IS_XVALUE(EXPR_))

    auto str = std::string{};

    static_assert(IS_LVALUE(str), "EXPR_ must be lvalue");
    static_assert(!IS_RVALUE(str), "EXPR_ must NOT be rvalue");

    static_assert(IS_XVALUE(std::move(str)), "EXPR_ must be xvalue");
    static_assert(!IS_PRVALUE(std::move(str)), "EXPR_ must NOT be prvalue");

    static_assert(IS_PRVALUE(std::string{}), "EXPR_ must be prvalue");
    static_assert(IS_RVALUE(std::string{}), "EXPR_ must be rvalue");
    static_assert(!IS_LVALUE(std::string{}), "EXPR_ must NOT be lvalue");
```

## リファレンス <a id="SS_6_8"></a>

リファレンス(参照)とは、以下のいずれか、もしくはすべてを指すが、
単にリファレンスと呼ぶ場合、lvalueリファレンスを指すことが多い。

* [lvalueリファレンス](#SS_6_8_1)
* [rvalueリファレンス](#SS_6_8_2)
* [forwardingリファレンス](#SS_6_8_3)


これらの概念と関わり強い、[リファレンスcollapsing](#SS_6_8_6)についても併せて解説を行う。

### lvalueリファレンス <a id="SS_6_8_1"></a>
lvalueリファレンスとは、

* C++98(もしくは03)から導入されたシンタックスであり、任意の型Tに対して`T&`という形式で宣言される。
* 既存のオブジェクトに対する別名(エイリアス)であり、宣言時に必ず初期化が必要で、
  一度初期化後は別のオブジェクトを参照することはできない。
* [rvalueリファレンス](#SS_6_8_2)導入前のC++では、すべてのリファレンスはlvalueリファレンスであったため、
  lvalueリファレンスを単にリファレンスと呼んでいた。
* オブジェクトaのエイリアスとして、
   リファレンスa_refが宣言されることを「a_refはaをバインドする」という。
* 以下のコード例で示すように、
    * 非const lvalueリファレンスは[rvalue](#SS_6_7_1_2)をバインドできないが、
    * const lvalueリファレンスは[rvalue](#SS_6_7_1_2)をバインドできる。

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 40

    int  a     = 0;
    int& a_ref = a;  // a_refはaのリファレンス
                     // a_refはaをバインドする

    ASSERT_EQ(&a, &a_ref);  // リファレンスは別名に過ぎないため、このテストが成立

    int b = 1;
    a_ref = b;  // 一見、a_refの再初期化に見えるが、実際は値の代入になるため、以下のテストが成立
    ASSERT_EQ(a, b);  // リファレンスは別名に過ぎないため、このテストが成立

    /*
    int& t_ref = int{99};  非const lvalueリファレンスはrvalueをバインドできない */
    int const& t_ref = int{99};  // 上記とは異なり、const lvalueリファレンスはrvalueをバインドできる
    ASSERT_EQ(t_ref, 99);
```

このようなリファレンスのバインドの可否はオーバーロードにも影響を与える。


```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 60

    int f(int& )        { return 1; }   // f-1
    int f(int const & ) { return 2; }   // f-2
```

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 69

    int       a = 0;
    int const b = 0;

    ASSERT_EQ(1, f(a));  // f(a)は、f-2も呼び出せるが、デフォルトでは、f-1が呼ばれる
    ASSERT_EQ(2, f(static_cast<int const&>(a)));  // aをconstにキャストして、強制的にf-2の呼び出し
    ASSERT_EQ(2, f(b));                           // constオブジェクトのバインド
    ASSERT_EQ(2, f(int{}));                       // rvalueのバインド
```

### rvalueリファレンス <a id="SS_6_8_2"></a>
rvalueリファレンスは、

* C++11で導入されたシンタックスであり、任意の型Tに対して、`T&&`で宣言される。
* 「テンポラリオブジェクト([rvalue](#SS_6_7_1_2))」をバインドできるリファレンス。
* C++11の[moveセマンティクス](#SS_8_5_3)と[perfect forwarding](#SS_6_8_5)を実現するために導入された。
* **注意1** 型が`T&&`である変数の値カテゴリは[lvalue](#SS_6_7_1_1)である。
* **注意2** 型が`T&&`である変数は、`T&`でバインドできる。

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 87

    int        a      = 0;
    int const& a_ref0 = a;        // const lvalueリファレンスはlvalueをバインドできる
    int const& a_ref1 = int{99};  // const lvalueリファレンスはrvalueもバインドできる
    int&& a_ref2 = int{99};       // rvalueリファレンスはテンポラリオブジェクトをバインドできる
    int& a_ref3 = a_ref2;         // rvalueリファレンス型の変数は、lvalueリファレンスでバインドできる
    /*
    int&& a_ref4 = a_ref2;       以下のメッセージでコンパイルエラー
                                 cannot bind rvalue reference of type ‘int&&’ to lvalue of type ‘int’ 
                                 rvalueリファレンス型の変数(lvalue)は、rvalueリファレンスでバインドできない */
```

このようなリファレンスのバインドの可否はオーバーロードにも影響を与える。


```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 118

    int f(int&)       { return 1; } // f-1
    int f(int const&) { return 2; } // f-2
    int f(int&&)      { return 3; } // f-3
```

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 129

    int       a = 0;
    int const b = 0;

    ASSERT_EQ(1, f(a));                           // f-1の呼び出し
    ASSERT_EQ(2, f(b));                           // f-2の呼び出し、constなlvalueリファレンスのバインド
    ASSERT_EQ(3, f(int{}));                       // f-3の呼び出し(f-3が無ければ、f-2を呼ばれる)
    ASSERT_EQ(2, f(static_cast<int const&>(a)));  // aをconstリファレンスにキャストして、強制的にf-2の呼び出し
    ASSERT_EQ(3, f(static_cast<int&&>(a)));       // aをrvalueリファレンスにキャストして、強制的にf-3の呼び出し
    ASSERT_EQ(3, f(std::move(a)));                // f-3の呼び出し

    int&& ref_ref = int{};

    ASSERT_EQ(1, f(ref_ref));                     // f-3ではなくf-1を呼び出す。従って間違いなくこのテストはパスする
```

上記コードの最後の部分の抜粋である以下のコードについては、少々解説が必要だろう。

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 141

    int&& ref_ref = int{};

    ASSERT_EQ(1, f(ref_ref));                     // f-3ではなくf-1を呼び出す。従って間違いなくこのテストはパスする
```

ref_refの型は`int &&`であるが、ref_refの値カテゴリは[rvalue](#SS_6_7_1_2)ではなく、[lvalue](#SS_6_7_1_1)である。
そのため、`f(ref_ref)`はlvalueリファレンスを引数とするf-1が選択される。

rvalueリファレンス型の仮引数（`T&&`）を持つ関数は、ムーブコンストラクタやムーブ代入演算子など頻繁に使用される。
しかし、関数内では仮引数は名前を持つため、常にlvalueとして扱われる。
この動作を理解することは、
[moveセマンティクス](#SS_8_5_3)や[perfect forwarding](#SS_6_8_5)を正しく実装/使用するために極めて重要である。

```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 150

    int g(int&& a) { return f(a); }            // g-1    仮引数aはlvalue -> f-1が呼ばれる
    int g(int& a) { return f(std::move(a)); }  // g-2    std::moveでrvalueに変換 -> f-3が呼ばれる
```
```cpp
    //  example/core_lang_spec/rvalue_lvalue_ut.cpp 158

    ASSERT_EQ(1, g(int{}));  // int{}はrvalue -> g-1が呼ばれ、内部でf-1が呼ばれる

    int a{};
    ASSERT_EQ(3, g(a));  // aはlvalue -> g-2が呼ばれ、内部でf-3が呼ばれる
```
---

C++11でrvalueの概念の整理やrvalueリファレンス、
std::move()の導入が行われた目的はプログラム実行速度の向上である。
以下のパターンの代入式の処理がどのように違うのかを見ることでrvalueやstd::moveの効果について説明する。

* [lvalueからの代入](#SS_6_8_2_1)
* [rvalueからの代入](#SS_6_8_2_2)
* [std::move(lvalue)からの代入](#SS_6_8_2_3)



#### lvalueからの代入 <a id="SS_6_8_2_1"></a>
下記コードにより「[lvalue](#SS_6_7_1_1)からの代入」を説明する。

```.cpp
    //  example/core_lang_spec/rvalue_move_ut.cpp 10

    auto str0 = std::string{};        // 行１   str0はlvalue
    auto str1 = std::string{"hehe"};  // 行２   str1もlvalue
    str0      = str1;                 // 行３   lvalueからの代入
```

* 行１、２  
  str0、str1がそれぞれ初期化される
  ("hehe"を保持するバッファが生成され、それをstr1オブジェクトが所有する)。

* 行３  
  str1が所有している文字列バッファと同じ内容を持つ新しいバッファが確保され、
  その内容がコピーされstr0がそれを所有する。従って、"hehe"を保持するバッファが2つできる。この代入をcopy代入と呼ぶ。

```essential/plant_uml/rvalue_from_lvalue.pu
@startditaa
行１、行２
    +---------------+       +---------------+ 
    |               |       |               | 
    |      str0     |       |      str1     | 
    |               |       |               | 
    +-------+-------+       +-------+-------+    
            |                       |
            V                       V
            nullptr                +------+        
                       copy        |"hehe"|
                        +--------- | cGRE |
                        |          +------+
-=--------------------- | -=---------------------
行３                      |
    +---------------+   |   +---------------+ 
    |               |   |   |               | 
    |      str0     |   |   |      str1     | 
    |               |   |   |               | 
    +-------+-------+   |   +-------+-------+    
            |           |           |
            V           |           V
           +------+     |           +------+
           |"hehe"|<----+           |"hehe"|
           | cBLU |                 | cGRE |
           +------+                 +------+
@endditaa
```


#### rvalueからの代入 <a id="SS_6_8_2_2"></a>
下記コードにより「[rvalue](#SS_6_7_1_2)からの代入」を説明する。

```.cpp
    //  example/core_lang_spec/rvalue_move_ut.cpp 23

    auto str0 = std::string{};        // 行１   str0はlvalue
    str0      = std::string{"hehe"};  // 行２   rvalueからの代入
                                      // 行３   行２で生成されたテンポラリオブジェクト(rvalue)は解放
```

* 行１  
  str0が「std::string()により作られたテンポラリオブジェクト」により初期化される。

* 行２の右辺  
 「"hehe"を保持するをstd::stringテンポラリオブジェクトが生成される。

* 行２の左辺  
  この例の場合、std::stringがmoveコンストラクタ／move代入演算子を提供しているため、
  下記図のようなバッファの所有が移し替えられるだけである(この代入をmove代入と呼ぶ)。

* 行３  
  テンポラリオブジェクトが解体されるが、heheバッファはstr0の所有になったためdeleteする必要がなく、
  実際には何もしない。move代入によって、文字列バッファの生成と破棄の回数がそれぞれ1回少なくなったため、
  実行速度は向上する(通常、new/deleteの処理コストは高い)。

```essential/plant_uml/rvalue_from_rvalue.pu
@startditaa
行１
    +---------------+
    |               |
    |      str0     |
    |               |
    +-------+-------+
            |
            V
            nullptr
-=-----------------------------------------------
行２の右辺
                            +---------------+ 
                            |               | 
                            | std꞉꞉string() | 
                            |               | 
                            +-------+-------+    
                                    |
                                    V
                                   +------+        
                                   |"hehe"|
                        +--------- | cGRE |
                        |          +------+
-=--------------------- | -=---------------------
行２の左辺                   |
    +---------------+   |   +---------------+ 
    |               |   |   |               | 
    |      str0     |   |   | std꞉꞉string() | 
    |               |   |   |           cRED| 
    +-------+-------+   |   +-------+-------+    
            |           |           |
            V           |           V
           +------+     |           nullptr
           |"hehe"|<----+
           | cGRE |    move
           +------+
-=-----------------------------------------------
行３
    +---------------+       +-=-------------+ 
    |               |       |               | destructing
    |      str0     |       | std꞉꞉string() | 
    |               |       |           cRED| 
    +-------+-------+       +-------+-------+    
            |                       |
            V                       V
           +------+                 nullptr
           |"hehe"|      
           | cGRE |
           +------+
@endditaa
```

#### std::move(lvalue)からの代入 <a id="SS_6_8_2_3"></a>
下記コードにより「std::move(lvalue)からの代入」を説明する。

```.cpp
    //  example/core_lang_spec/rvalue_move_ut.cpp 36

    auto str0 = std::string{};        // 行１   str0はlvalue
    auto str1 = std::string{"hehe"};  // 行２   str1もlvalue
    str0      = std::move(str1);      // 行３   str1への代入以外のアクセスは未規定である。
```

* 行１  
  「[lvalueからの代入](#SS_6_8_2_1)」の行１と同じである。

* 行２  
  「[lvalueからの代入](#SS_6_8_2_1)」の行２と同じである。

* 行３  
  std::moveは単にrvalueリファレンスへのキャストを行うだけであり、ランタイム時の処理コストは発生しない。
  この例の場合、std::stringがmoveコンストラクタ／move代入演算子を提供しているため、
  下記図のようなバッファの所有が移し替えられるだけである(この代入もmove代入と呼ぶ)。
  この動作は「[rvalueからの代入](#SS_6_8_2_2)の行２の左辺」と同じであり、同様に速度が向上するが、その副作用として、
  str1への代入以外のアクセスは[未規定動作](#SS_6_14_4)であるため、避けるべきである
  (多くの実装では、str1.size() == 0となることが多いがこの動作は約束されない)。

```essential/plant_uml/rvalue_from_move.pu
@startditaa
行１、行２
    +---------------+       +---------------+ 
    |               |       |               | 
    |      str0     |       |      str1     | 
    |               |       |               | 
    +-------+-------+       +-------+-------+    
            |                       |
            V                       V
            nullptr                +------+        
                                   |"hehe"|
                        +--------- | cGRE |
                        |          +------+
-=--------------------- | -=---------------------
行３                      |
    +---------------+   |   +---------------+ 
    |               |   |   |               | 
    |      str0     |   |   |      str1     | 
    |               |   |   |           cRED| 
    +-------+-------+   |   +-------+-------+    
            |           |           |
            V           |           V
           +------+     |           nullptr
           |"hehe"|<----+
           | cGRE |    move
           +------+
@endditaa
```


### forwardingリファレンス <a id="SS_6_8_3"></a>
関数テンプレートの型パラメータTに対して`T&&`として宣言された仮引数、
または型推論を伴うauto&&として宣言された変数を、forwardingリファレンスと呼ぶ
(この概念はC++14から存在し、慣用的にユニバーサルリファレンスと呼ばれていたが、
C++17から正式にforwardingリファレンスと命名された)。
forwardingリファレンスは一見rvalueリファレンスのように見えるが、
下記に示す通り、lvalueにもrvalueにもバインドできる
([リファレンスcollapsing](#SS_6_8_6)により、このようなバインドが可能になる)。

```cpp
    //  example/core_lang_spec/universal_ref_ut.cpp 8

    template <typename T>
    void f(T&& t) noexcept  // tはforwardingリファレンス
    {
        // ...
    }

    template <typename T>
    void g(std::vector<T>&& t) noexcept  // tはrvalueリファレンス
    {
        // ...
    }
```
```cpp
    //  example/core_lang_spec/universal_ref_ut.cpp 29

    auto       vec  = std::vector<std::string>{"lvalue"};   // vecはlvalue
    auto const cvec = std::vector<std::string>{"clvalue"};  // cvecはconstなlvalue

    f(vec);                                 // 引数はlvalue
    f(cvec);                                // 引数はconstなlvalue
    f(std::vector<std::string>{"rvalue"});  // 引数はrvalue

    // g(vec);  // 引数がlvalueなのでコンパイルエラー
    // g(cvec); // 引数がconst lvalueなのでコンパイルエラー
    g(std::vector<std::string>{"rvalue"});  // 引数はrvalue
```

下記のコードは[ジェネリックラムダ](#SS_6_11_6)の引数をforwardingリファレンスにした例である。

```cpp
    //  example/core_lang_spec/universal_ref_ut.cpp 47

    // sはforwardingリファレンス
    auto value_type = [](auto&& s) noexcept {
        if (std::is_same_v<std::string&, decltype(s)>) {
            return 0;
        }
        if (std::is_same_v<std::string const&, decltype(s)>) {
            return 1;
        }
        if (std::is_same_v<std::string&&, decltype(s)>) {
            return 2;
        }
        return 3;
    };

    auto       str  = std::string{"lvalue"};
    auto const cstr = std::string{"const lvalue"};

    ASSERT_EQ(0, value_type(str));
    ASSERT_EQ(1, value_type(cstr));
    ASSERT_EQ(2, value_type(std::string{"rvalue"}));
```

通常、forwardingリファレンスはstd::forwardと組み合わせて使用される。


### ユニバーサルリファレンス <a id="SS_6_8_4"></a>
ユニバーサルリファレンスとは、「[forwardingリファレンス](#SS_6_8_3)」の通称、もしくは旧称である。

### perfect forwarding <a id="SS_6_8_5"></a>
perfect forwarding(完全転送)とは、引数の[rvalue](#SS_6_7_1_2)性や
[lvalue](#SS_6_7_1_1)性を損失することなく、
その引数を別の関数に転送する技術のことを指す。
通常は、[forwardingリファレンス](#SS_6_8_3)である関数の仮引数をstd::forwardを用いて、
他の関数に渡すことで実現される。

perfect forwardingの使用例を以下に示す。

```cpp
    //  example/core_lang_spec/perfect_forwarding_ut.cpp 7

    class Widget {
    public:
        explicit Widget(std::string const& name) : name_{name} {}        // lvalueによるコンストラクタ
        explicit Widget(std::string&& name) : name_{std::move(name)} {}  // rvalueによるコンストラクタ
        std::string const& GetName() const { return name_; }

    private:
        std::string name_;  // コンストラクタの引数をcopy/move構築
    };

    template <typename T>
    Widget make_Widget(T&& str)
    {                                         // strはforwardingリファレンス
        return Widget(std::forward<T>(str));  // perfect forwarding
    }
```
```cpp
    //  example/core_lang_spec/perfect_forwarding_ut.cpp 28

    std::string       str{"lvalue ref"};
    std::string const cstr{"lvalue const ref"};

    Widget w0 = make_Widget(str);  // make_Widget -> Widget(std::string const&)
    ASSERT_EQ(w0.GetName(), str);

    Widget w1 = make_Widget(cstr);  // make_Widget -> Widget(std::string const&)
    ASSERT_EQ(w1.GetName(), cstr);

    Widget w2 = make_Widget(std::string{"rvalue ref"});  // make_Widget -> Widget(std::string &&)
    ASSERT_EQ(w2.GetName(), "rvalue ref");

    Widget w3 = make_Widget(std::move(str));  // make_Widget -> Widget(std::string &&)
    ASSERT_EQ(w3.GetName(), "lvalue ref");    // strはムーブされたのでアクセス不可
```

### リファレンスcollapsing <a id="SS_6_8_6"></a>
Tを任意の型とし、TRを下記のように宣言した場合、

```cpp
    using TR = T&;
```

下記のようなコードは、C++03ではコンパイルエラーとなったが、
C++11からはエラーとならず、TRRはT&となる。

```cpp
    using TRR = TR&;
```

2つの&を1つに折り畳む、このような機能をリファレンスcollapsingと呼ぶ。

下記はTをintとした場合のリファレンスcollapsingの動きを示している。

```cpp
    //  example/core_lang_spec/ref_collapsing_ut.cpp 7

    int i;

    using IR  = int&;
    using IRR = IR&;  // IRRはint& &となり、int&に変換される

    IR  ir  = i;
    IRR irr = ir;

    static_assert(std::is_same_v<int&, decltype(ir)>);   // lvalueリファレンス
    static_assert(std::is_same_v<int&, decltype(irr)>);  // lvalueリファレンス
```

リファレンスcollapsingは、型エイリアス、型であるテンプレートパラメータ、decltypeに対して行われる。
詳細な変換則は、下記のようになる。

```
    T& &   -> T&
    T& &&  -> T&
    T&& &  -> T&
    T&& && -> T&&
```

下記のようなクラステンプレートを定義した場合、

```cpp
    //  example/core_lang_spec/ref_collapsing_ut.cpp 26

    template <typename T>
    struct Ref {
        T&  t;
        T&& u;
    };
```

下記のコードにより、テンプレートパラメータに対するこの変換則を確かめることができる。

```cpp
    //  example/core_lang_spec/ref_collapsing_ut.cpp 38

    static_assert(std::is_same_v<int&, decltype(Ref<int>::t)>);    // lvalueリファレンス
    static_assert(std::is_same_v<int&&, decltype(Ref<int>::u)>);   // rvalueリファレンス

    static_assert(std::is_same_v<int&, decltype(Ref<int&>::t)>);   // lvalueリファレンス
    static_assert(std::is_same_v<int&, decltype(Ref<int&>::u)>);   // lvalueリファレンス

    static_assert(std::is_same_v<int&, decltype(Ref<int&&>::t)>);  // lvalueリファレンス
    static_assert(std::is_same_v<int&&, decltype(Ref<int&&>::u)>); // rvalueリファレンス
```

この機能がないC++03では、

```cpp
    //  example/core_lang_spec/ref_collapsing_ut.cpp 52

    template <typename T>
    struct AddRef {
        using type = T&;
    };
```

ようなクラステンプレートに下記コードのようにリファレンス型を渡すとコンパイルエラーとなる。

```cpp
    //  example/core_lang_spec/ref_collapsing_ut.cpp 69

    static_assert(std::is_same_v<int&, AddRef<int&>::type>);
```

この問題を回避するためには下記のようなテンプレートの特殊化が必要になる。

```cpp
    //  example/core_lang_spec/ref_collapsing_ut.cpp 59

    template <typename T>
    struct AddRef<T&> {
        using type = T&;
    };
```

上記したようなクラステンプレートでのメンバエイリアスの宣言は、
[テンプレートメタプログラミング](https://ja.wikipedia.org/wiki/%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%A1%E3%82%BF%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0)
で頻繁に使用されるため、
このようなテンプレートの特殊化を不要にするリファレンスcollapsingは、
有用な機能拡張であると言える。

### リファレンス修飾 <a id="SS_6_8_7"></a>
[rvalue修飾](#SS_6_8_7_1)と[lvalue修飾](#SS_6_8_7_2)とを併せて、リファレンス修飾と呼ぶ。

#### rvalue修飾 <a id="SS_6_8_7_1"></a>
下記GetString0()のような関数が返すオブジェクトの内部メンバに対する[ハンドル](#SS_8_12_7)は、
オブジェクトのライフタイム終了後にもアクセスすることができるため、
そのハンドルを通じて、
ライフタイム終了後のオブジェクトのメンバオブジェクトにもアクセスできてしまう。

ライフタイム終了後のオブジェクトにアクセスすることは未定義動作であり、
特にそのオブジェクトがrvalueであった場合、さらにその危険性は高まる。

こういったコードに対処するためのシンタックスが、lvalue修飾、rvalue修飾である。

下記GetString1()、GetString3()、GetString4()のようにメンバ関数をlvalue修飾やrvalue修飾することで、
rvalueの内部ハンドルを返さないようにすることが可能となり、上記の危険性を緩和することができる。

```cpp
    //  example/core_lang_spec/ref_qualifiers_ut.cpp 8

    class C {
    public:
        explicit C(char const* str) : str_{str} {}

        // lvalue修飾なし、rvalue修飾なし
        std::string& GetString0() noexcept { return str_; }

        // lvalue修飾
        std::string const& GetString1() const& noexcept { return str_; }

        // rvalue修飾
        // *thisがrvalueの場合でのGetString1()の呼び出しは、この関数を呼び出すため、
        // class内部のハンドルを返してはならない。
        // また、それによりstd::stringを生成するため、noexcept指定してはならない。
        std::string GetString1() const&& { return str_; }

        // lvalue修飾だが、const関数はrvalueからでも呼び出せる。
        // rvalueに対しての呼び出しを禁止したい場合には、GetString4のようにする。
        std::string const& GetString2() const& noexcept { return str_; }

        // lvalue修飾
        // 非constなのでrvalueからは呼び出せない。
        std::string const& GetString3() & noexcept { return str_; }

        // lvalue修飾
        std::string const& GetString4() const& noexcept { return str_; }

        // rvalue修飾
        // rvalueからこの関数を呼び出されるとrvalueオブジェクトの内部ハンドルを返してしまい、
        // 危険なので=deleteすべき。
        std::string const& GetString4() const&& = delete;

    private:
        std::string str_;
    };
```
```cpp
    //  example/core_lang_spec/ref_qualifiers_ut.cpp 49

    auto        c    = C{"c0"};
    auto const& s0_0 = c.GetString0();        // OK cが解放されるまでs0_0は有効
    auto        s0_1 = C{"c1"}.GetString0();  // NG 危険なコード
    // s0_1が指すオブジェクトは、次の行で無効になる

    auto const& s1_0 = c.GetString1();        // OK GetString1()&が呼び出される
    auto const& s1_1 = C{"c1"}.GetString1();  // OK GetString1()&&が呼び出される
    // s1_0が指すrvalueはs1_0がスコープアウトするまで有効

    auto const& s2_0 = c.GetString2();        // OK GetString2()&が呼び出される
    auto const& s2_1 = C{"c1"}.GetString2();  // NG const関数はlvalue修飾しても呼び出し可能
    // s2_1が指すオブジェクトは、次の行で無効になる

    auto const& s3_0 = c.GetString3();  // OK GetString3()&が呼び出される
    // auto const& s3_1 = C{"c1"}.GetString3();  // 危険なのでコンパイルさせない

    auto const& s4_0 = c.GetString4();  // OK GetString4()&が呼び出される
    // auto const& s4_1 = C{"c1"}.GetString4();  // 危険なのでコンパイルさせない
```

#### lvalue修飾 <a id="SS_6_8_7_2"></a>
[rvalue修飾](#SS_6_8_7_1)を参照せよ。


## 構文と制御構造 <a id="SS_6_9"></a>

### 属性構文 <a id="SS_6_9_1"></a>
C++14から導入されたの属性構文は、[[属性名]]の形式で記述され、
特定のコード要素に対する追加情報やコンパイラへの指示を与えるためのものである。

|属性                 |C++Ver|効果                                               |
|---------------------|------|---------------------------------------------------|
|[[noreturn]]         |C++11 |関数が決して返らないことを示す                     |
|[[deprecated]]       |C++14 |関数や変数が非推奨であることを示しめす             |
|[[maybe_unused]]     |C++17 |変数や関数が未使用である警告の抑止                 |
|[[nodiscard]]        |C++17 |戻り値が無視されると警告                           |
|[[fallthrough]]      |C++14 |switch文のfallthroughの警告抑止                    |
|[[no_unique_address]]|C++20 |クラスや構造体のメンバに対して、メモリの最適化促進 |

```cpp
    //  example/core_lang_spec/attr_ut.cpp 10

    // 非推奨の関数
    [[deprecated("この関数は非推奨です。代わりに newFunction を使用してください。")]]  // 
    void oldFunction();  // この関数を呼び出すと警告される
    void newFunction();
```
```cpp
    //  example/core_lang_spec/attr_ut.cpp 20
    void processValues()
    {
        [[maybe_unused]] int unusedValue = 42;  // 使用しない変数でも警告が出ない

        // do something
    }
```
```cpp
    //  example/core_lang_spec/attr_ut.cpp 28

    [[nodiscard]] int computeResult() { return 42; }

    //  example/core_lang_spec/attr_ut.cpp 38

    computeResult();               // 警告が出る：戻り値が無視されている
    int result = computeResult();  // これはOK
```
```cpp
    //  example/core_lang_spec/attr_ut.cpp 54

    switch (value) {
    case 1:
        // do something
        [[fallthrough]];  // 明示的に fallthrough を宣言することができる
    case 2:
        // do something
        break;
    default:
        break;
    }
```

### 関数tryブロック <a id="SS_6_9_2"></a>
関数tryブロックとはtry-catchを本体とした下記のような関数のブロックを指す。

```cpp
    //  example/core_lang_spec/func_try_block.cpp 8

    void function_try_block()
    try {  // 関数tryブロック
        // 何らかの処理
        // ...
    }
    catch (std::length_error const& e) {  // 関数tryブロックのエクセプションハンドラ
        // ...
    }
    catch (std::logic_error const& e) {  // 関数tryブロックのエクセプションハンドラ
        // ...
    }
```

### 範囲for文 <a id="SS_6_9_3"></a>
範囲for文は、

```cpp
    for ( for-range-declaration : for-range-initializer ) statement
```

このような形式で表され、C++17までは下記のような疑似コードに展開される。

```cpp
    {
        auto && __range = for-range-initializer;
        for ( auto __begin = begin-expr, __end = end-expr; __begin != __end; ++__begin ) {
        for-range-declaration = *__begin;
        statement
      }
    }
```

単純な範囲for文の使用例は下記の通りである。

```cpp
    //  example/core_lang_spec/range_for_ut.cpp 14

    auto list = std::list{1, 2, 3};
    auto oss  = std::stringstream{};

    for (auto a : list) {  // 範囲for文
        oss << a;
    }
    ASSERT_EQ(oss.str(), "123");
```

上記のコードは下記のように展開される。

```cpp
    //  example/core_lang_spec/range_for_ut.cpp 26

    auto list = std::list{1, 2, 3};
    auto oss  = std::stringstream{};

    // std::begin(list)、std::end(list)の戻り型が同一
    static_assert(std::is_same_v<decltype(std::begin(list)), decltype(std::end(list))>);

    // 上記の範囲for文は下記のように展開される
    for (auto it = std::begin(list); it != std::end(list); ++it) {
        oss << *it;
    }

    ASSERT_EQ(oss.str(), "123");
```


C++17以前は、上記のコードのコメントにある通り、`__begin`と`__end`が同一の型である前提であった。
C++17以降は、この規制が緩和されたため、以下のように展開されることになった。

```cpp
    {
        auto && __range = for-range-initializer;
        auto __begin = begin-expr;
        auto __end = end-expr;     // C++17までは、__begin と __endは同一である前提
        for ( ; __begin != __end; ++__begin ) {
            for-range-declaration = *__begin;
            statement
        }
    }
```

この規制緩和により、以下のようなコードが範囲for文で記述できるようになった。
下記のコードはこの緩和ルールの応用例である。

```cpp
    //  example/core_lang_spec/range_for_ut.cpp 73

    delimited_string<','> delimited_str{"Hello,World"};
    std::ostringstream    oss;

    // ',' を終了文字として "Hello" だけをループして出力
    for (auto c : delimited_str) {
        oss << c;
    }

    ASSERT_EQ("Hello", oss.str());  // 結果は "Hello" になるはず
```
上記のコードは下記のように展開される。

```cpp
    //  example/core_lang_spec/range_for_ut.cpp 87

    delimited_string<','> delimited_str{"Hello,World"};
    std::ostringstream    oss;

    // ',' を終了文字として"Hello" だけをループして出力
    for (auto it = delimited_str.begin(); it != delimited_str.end(); ++it) {
        oss << *it;
    }

    ASSERT_EQ("Hello", oss.str());  // 結果は "Hello" になるはず
```

### 構造化束縛 <a id="SS_6_9_4"></a>
構造化束縛はC++17 から導入されたもので、std::tuppleやstd::pair、std::arrayなど、
構造体のメンバーを個別の変数に分解して簡潔に扱うことをできるようにするための機能である。

```cpp
    //  example/core_lang_spec/structured_binding_ut.cpp 13

    // tupleでの構造化束縛の例
    std::tuple<int, double, std::string> tobj(1, 2.5, "Hello");

    auto [i, d, s] = tobj;  // 構造化束縛を使用してタプルを分解

    ASSERT_EQ(i, 1);
    ASSERT_DOUBLE_EQ(d, 2.5);
    ASSERT_EQ("Hello", s);
```
```cpp
    //  example/core_lang_spec/structured_binding_ut.cpp 28

    // pairでの構造化束縛の例
    std::pair<int, std::string> pobj(42, "example");

    auto [i, s] = pobj;  // 構造化束縛を使用してペアを分解

    ASSERT_EQ(i, 42);
    ASSERT_EQ("example", s);
```
```cpp
    //  example/core_lang_spec/structured_binding_ut.cpp 42

    struct Person {
        std::string name;
        int         age;
    };

    Person person{"Ichiro", 30};  // 構造体のインスタンス

    auto& [name, age] = person;  // 構造化束縛を使用して構造体のメンバーを分解

    static_assert(std::is_same_v<decltype(name), std::string>);  // これは正しい
    // static_assert(std::is_same_v<decltype(name), std::string&>); これはコンパイルエラー
    // 上記がコンパイルエラーになる理由は以下の通り。
    //
    // 変数宣言は、 autoを記述したあとに角カッコ内に変数名を列挙する。
    // それぞれの変数に対する型や修飾子の指定はできない。
    // autoの部分を const auto&のように、全体に対してCV修飾や参照を付加することはできる。
    // それぞれの変数の型は、各要素をdecltypeしたものとなる。
    //                        ^^^^^^^^^^^^^^ nameの型がstd::stringと評価された理由

    name = "Taro";  // nameはリファレンス
    age  = 56;      // ageはリファレンス
    ASSERT_EQ(person.name, "Taro");
    ASSERT_EQ(person.age, 56);
```
```cpp
    //  example/core_lang_spec/structured_binding_ut.cpp 72

    auto array = std::array<int, 3>{1, 2, 3};

    auto [x, y, z] = array;  // 構造化束縛を使って std::array の要素を分解

    ASSERT_EQ(x, 1);
    ASSERT_EQ(y, 2);
    ASSERT_EQ(z, 3);
```

### 初期化付きif/switch文 <a id="SS_6_9_5"></a>
C++17で、if文とswitc文に初期化を行う構文が導入された。
これにより、変数をそのスコープ内で初期化し、その変数を条件式の評価に使用できる。
初期化された変数は、if文やswitch文のスコープ内でのみ有効であり、他のスコープには影響を与えない。

この構文は、従来のfor文で使用されていた初期化ステートメントを、if/switch文に拡張したものである。
この類似性が理解しやすいように、本節では、 敢えて以下のコード例で同じ関数、同じクラスを使用し、
対比できるようにした。

- [初期化付きfor文(従来のfor文)](#SS_6_9_5_1)
- [初期化付きwhile文(従来のwhile文)](#SS_6_9_5_2)
- [初期化付きif文](#SS_6_9_5_3)
- [初期化付きswitch文](#SS_6_9_5_4)


#### 初期化付きfor文(従来のfor文) <a id="SS_6_9_5_1"></a>
下記の疑似コードは従来のfor文の構造を表す。

```cpp
    for (init-statement; condition; post-statement) {
        // ループ処理
    }
```
上記のと同様の実際のfor文のコードを以下に示す。

```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 8

    class OperationResult {
    public:
        enum class ErrorCode { NoError, ErrorPattern1, ErrorPattern2, ErrorPattern3 };
        bool      IsError() const noexcept;
        ErrorCode Get() const noexcept;
                  operator bool() const noexcept { return IsError(); }

    private:
        // 何らかの定義
    };

    OperationResult DoOperation();                                 // 何らかの処理
    void            RecoverOperation(OperationResult::ErrorCode);  // リカバリ処理
```
```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 33

    for (auto result = DoOperation(); result.IsError(); result = DoOperation()) {
        RecoverOperation(result.Get());  // エラー処理
    }

    // 以下、成功時の処理
    // ...
```

#### 初期化付きwhile文(従来のwhile文) <a id="SS_6_9_5_2"></a>
下記の疑似コードこの節で説明しようとしているwhile文の構造を表す(従来からのwhile文)。

```cpp
    while (type-specifier-seq declarator) {
        // 条件がtrueの場合の処理
    }
```

[初期化付きif文](#SS_6_9_5_3)/[初期化付きswitch文](#SS_6_9_5_4)はC++17から導入されたシンタックスであるが、
それと同様のシンタックスはwhileには存在しないが、
以下のコード例のように従来の記法は広く知られているため、念とため紹介する。

```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 46

    while (auto result = DoOperation()) {  // resultはboolへの暗黙の型変換が行われる
        // エラー処理
    }
    // resultはスコープアウトする
```

#### 初期化付きif文 <a id="SS_6_9_5_3"></a>
下記の疑似コードこの節で説明しようとしているif文の構造を表す。

```cpp
    if (init-statement; condition) {
        // 条件がtrueの場合の処理
    }
```

上記と同様の構造を持つ実際のif文のコードを以下に示す。

```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 8

    class OperationResult {
    public:
        enum class ErrorCode { NoError, ErrorPattern1, ErrorPattern2, ErrorPattern3 };
        bool      IsError() const noexcept;
        ErrorCode Get() const noexcept;
                  operator bool() const noexcept { return IsError(); }

    private:
        // 何らかの定義
    };

    OperationResult DoOperation();                                 // 何らかの処理
    void            RecoverOperation(OperationResult::ErrorCode);  // リカバリ処理
```
```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 57

    if (auto result = DoOperation(); !result.IsError()) {
        // 成功処理
    }
    else {
        RecoverOperation(result.Get());  // エラー処理
    }
    // resultはスコープアウトする
```

クラスの独自の[<=>演算子](#SS_6_6_4_1)を定義する場合、下記のように使用することができる。

```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 70

    struct DoubleName {
        std::string name0;
        std::string name1;
        friend bool operator==(DoubleName const& lhs, DoubleName const& rhs) noexcept = default;
    };

    inline auto operator<=>(DoubleName const& lhs, DoubleName const& rhs) noexcept
    {
        // name0 を比較し、等しくなければその比較結果を返す
        if (auto cmp = lhs.name0 <=> rhs.name0; cmp != 0) {
            return cmp;
        }

        return lhs.name1 <=> rhs.name1;  // name0が等しければ name1を比較
    }
```

#### 初期化付きswitch文 <a id="SS_6_9_5_4"></a>
下記の疑似コードはこの節で説明しようとしているswitch文の構造を表す。

```cpp
    switch (init-statement; condition) {
        case value1:
            // 条件が value1 の場合の処理
            break;
        case value2:
            // 条件が value2 の場合の処理
            break;
        // その他のケース
    }

```
上記と同様の構造を持つ実際のswitch文のコードを以下に示す。

```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 8

    class OperationResult {
    public:
        enum class ErrorCode { NoError, ErrorPattern1, ErrorPattern2, ErrorPattern3 };
        bool      IsError() const noexcept;
        ErrorCode Get() const noexcept;
                  operator bool() const noexcept { return IsError(); }

    private:
        // 何らかの定義
    };

    OperationResult DoOperation();                                 // 何らかの処理
    void            RecoverOperation(OperationResult::ErrorCode);  // リカバリ処理
```
```cpp
    //  example/core_lang_spec/if_switch_init_ut.cpp 101

    switch (auto result = DoOperation(); result.Get()) {
    case OperationResult::ErrorCode::ErrorPattern1:
        RecoverOperation(result.Get());  // エラー処理
        break;
        // エラー処理のいくつかのパターン
    case OperationResult::ErrorCode::NoError:
        // 成功処理
    default:
        assert(false);  // ここには来ないはず
    }
    // resultはスコープアウトする
```

## 言語拡張機能 <a id="SS_6_10"></a>
### コルーチン <a id="SS_6_10_1"></a>
コルーチンはC++20から導入された機能であり、以下の新しいキーワードによりサポートされる。

* [co_await](#SS_6_10_1_1)
* [co_return](#SS_6_10_1_2)
* [co_yield](#SS_6_10_1_3)

#### co_await <a id="SS_6_10_1_1"></a>
co_awaitはコルーチンの非同期操作の一時停止と再開に使用される。
co_waitとco_returnを使用したコードを以下に示す。

```cpp
    //  example/core_lang_spec20/co_await_ut.cpp 12

    class Task {  // コルーチンが返す型
    public:
        /// @struct promise_type
        /// @brief コルーチンのライフサイクルを管理する構造体
        struct promise_type {
            /// @brief コルーチンから Task 型のオブジェクトを返す関数
            /// @return Taskオブジェクト
            Task get_return_object() { return Task{std::coroutine_handle<promise_type>::from_promise(*this)}; }

            /// @brief コルーチンの最初のサスペンドポイント
            /// @return 常にサスペンドするオブジェクトを返す
            std::suspend_always initial_suspend() { return {}; }

            /// @brief コルーチンの最後のサスペンドポイント
            /// @return 常にサスペンドするオブジェクトを返す
            std::suspend_always final_suspend() noexcept { return {}; }

            /// @brief コルーチン内で例外が発生した場合に呼び出される
            /// @details コルーチン内で未処理の例外が発生した場合に、プロセスを終了する
            void unhandled_exception() { std::exit(1); }

            /// @brief コルーチンが終了した際に呼び出される
            /// @details co_return で値が返されない場合に呼び出されるが、何も行わない
            void return_void() {}
        };

        /// @brief Task のコンストラクタ
        /// @param h コルーチンハンドル
        Task(std::coroutine_handle<promise_type> h) : coro{h} {}

        /// @brief コルーチンの呼び出し回数に基づいた文字列を返す
        /// @return 呼び出し回数に応じた "call X" という文字列
        std::string get_value() { return "call " + std::to_string(called); }

        /// @brief コルーチンを再開する
        /// @details コルーチンが終了していなければ再開し、呼び出し回数をカウントする
        /// @return コルーチンが完了していなければ true、完了していれば false
        bool resume()
        {
            ++called;                 // コルーチンを呼び出した回数をカウント
            if (!coro.done()) {       // コルーチンが完了していなければ
                coro.resume();        // 再開
                return !coro.done();  // 再開後も完了していなければ true を返す
            }
            return false;  // すでに完了している場合は false を返す
        }

        /// @brief Task のデストラクタ
        /// @details コルーチンハンドルが有効であれば破棄する
        ~Task()
        {
            if (coro) coro.destroy();
        }

    private:
        std::coroutine_handle<promise_type> coro;        ///< コルーチンハンドル
        uint32_t                            called = 0;  ///< コルーチンが再開された回数
    };

    /// @brief コルーチンを生成する関数
    /// @return Taskオブジェクト
    Task gen_coroutine()
    {
        co_await std::suspend_always{};  // 最初のサスペンドポイント
        co_await std::suspend_always{};  // 2回目のサスペンドポイント
        co_return;                       // コルーチン終了
    }
```
以下単体テストコードによりに上記コルーチンの動作を示す。

```cpp
    //  example/core_lang_spec20/co_await_ut.cpp 85

    Task    task  = gen_coroutine();  // gen_coroutine から Task オブジェクトを生成
    int32_t calls = 0;

    /// @test コルーチンを resume() で再開し、完了するまでループする
    while (task.resume()) {  // コルーチンが完了していない間、再開
        switch (calls) {
        case 0:
            /// @test コルーチンが1回目の再開後、"call 1" が返されることを確認
            ASSERT_EQ("call 1", task.get_value());
            break;
        case 1:
            /// @test コルーチンが2回目の再開後、"call 2" が返されることを確認
            ASSERT_EQ("call 2", task.get_value());
            break;
        case 2:
            /// @test コルーチンが3回目の再開後、"call 3" が返されることを確認
            ASSERT_EQ("call 3", task.get_value());
            break;
        }
        ++calls;
    }

    /// @test コルーチンが 2 回 resume された後に終了していることを確認
    ASSERT_EQ(2, calls);
```

上記のコルーチンと同じ機能を持つクラスのco_await/co_returnを使わない実装を以下に示す。

```cpp
    //  example/core_lang_spec20/co_await_ut.cpp 115

    /// @enum CoroutineState
    /// @brief ManualCoroutine の状態を表す enum 型
    enum class CoroutineState {
        Start,             ///< コルーチンが開始された状態
        FirstSuspension,   ///< コルーチンが最初にサスペンドされた状態
        SecondSuspension,  ///< コルーチンが2回目にサスペンドされた状態
        Finished           ///< コルーチンが完了した状態
    };

    /// @brief コルーチンの状態を保持し、進行を管理するためのクラス
    class ManualCoroutine {
    public:
        /// @brief コルーチンの代わりに状態を進行させる関数
        /// @details コルーチンの状態に基づいて進行し、コルーチンのように振る舞う
        /// @return コルーチンが継続可能なら true、終了していれば false を返す
        bool resume()
        {
            ++called;  // コルーチンの再開回数をカウント
            switch (state) {
            case CoroutineState::Start:
                state = CoroutineState::FirstSuspension;
                return true;  // 継続可能

            case CoroutineState::FirstSuspension:
                state = CoroutineState::SecondSuspension;
                return true;  // 継続可能

            case CoroutineState::SecondSuspension:
                state = CoroutineState::Finished;
                return false;  // 終了

            case CoroutineState::Finished:
                return false;  // 既に終了している
            }
            assert(false);  // 不正な状態（理論的には到達しないはず）
            return false;
        }

        /// @brief 呼び出し回数に基づいた文字列を返す
        /// @return "call X" という形式の文字列（X は呼び出し回数）
        std::string get_value() { return "call " + std::to_string(called); }

    private:
        uint32_t       called = 0;                      ///< コルーチンが再開された回数
        CoroutineState state  = CoroutineState::Start;  ///< 現在のコルーチンの状態
    };
```

このクラスは当然ながら、前記のコルーチンの単体テストコードとほぼ同じになる。

```cpp
    //  example/core_lang_spec20/co_await_ut.cpp 167

    auto    manual_coroutine = ManualCoroutine{};
    int32_t calls            = 0;

    while (manual_coroutine.resume()) {  // コルーチンを再開する
        switch (calls) {
        case 0:
            /// @test 1回目の再開後に "call 1" が返されることを確認
            ASSERT_EQ("call 1", manual_coroutine.get_value());
            break;
        case 1:
            /// @test 2回目の再開後に "call 2" が返されることを確認
            ASSERT_EQ("call 2", manual_coroutine.get_value());
            break;
        case 2:
            /// @test 3回目の再開後に "call 3" が返されることを確認
            ASSERT_EQ("call 3", manual_coroutine.get_value());
            break;
        }
        ++calls;  ///< コルーチンの再開回数をインクリメント
    }

    /// @test コルーチンが2回 resume された後に終了していることを確認
    ASSERT_EQ(2, calls);
```

C++20から導入されたco_await、co_return、TaskとC++17以前の機能のみを使用したコードの対比によって、
コルーチンのサポート機能により実装が容易になることが理解できるだろう。

#### co_return <a id="SS_6_10_1_2"></a>
co_returnはコルーチンの終了時に値を返すために使用される。
co_returnは通常[co_await](#SS_6_10_1_1)と同時に使われることが多い。

#### co_yield <a id="SS_6_10_1_3"></a>
co_yieldはコルーチンから値を返しつつ、
次の再開ポイントまで処理を中断する。これはジェネレーターの実装に便利である。

```cpp
    //  example/core_lang_spec20/co_yield_ut.cpp 12

    template <typename T>
    class Generator {
    public:
        Generator(Generator&& other) noexcept : coro{std::move(other.coro)} { other.coro = nullptr; }

        Generator& operator=(Generator&& other) noexcept
        {
            if (this != &other) {
                coro       = other.coro;
                other.coro = nullptr;
            }
            return *this;
        }

        /// @struct promise_type
        /// @brief コルーチンのライフサイクルを管理する構造体
        struct promise_type {
            T current_value;

            /// @brief コルーチンから Generator 型のオブジェクトを返す関数
            /// @return Generatorオブジェクト
            Generator get_return_object() { return Generator{std::coroutine_handle<promise_type>::from_promise(*this)}; }

            /// @brief コルーチンの最初のサスペンドポイント
            /// @return 常にサスペンドするオブジェクトを返す
            std::suspend_always initial_suspend() { return {}; }

            /// @brief コルーチンの最後のサスペンドポイント
            /// @return 常にサスペンドするオブジェクトを返す
            std::suspend_always final_suspend() noexcept { return {}; }

            /// @brief コルーチンで値を生成するためのサスペンドポイント
            /// @param value 生成された値
            /// @return 常にサスペンドするオブジェクトを返す
            std::suspend_always yield_value(T value)
            {
                current_value = value;
                return {};
            }

            /// @brief コルーチン内で例外が発生した場合に呼び出される
            void unhandled_exception() { std::exit(1); }

            /// @brief コルーチンの終了時に呼び出される
            void return_void() {}
        };

        /// @brief コルーチンを再開し、次の値を生成する
        /// @return 次の値が生成された場合は true、終了した場合は false
        bool move_next()
        {
            if (coro && !coro.done()) {
                coro.resume();
                return !coro.done();
            }
            return false;
        }

        /// @brief 現在の値を取得する
        /// @return 現在の値
        T current_value() const { return coro.promise().current_value; }

        /// @brief Generator のコンストラクタ
        /// @param h コルーチンハンドル
        Generator(std::coroutine_handle<promise_type> h) : coro(h) {}

        /// @brief Generator のデストラクタ
        /// @details コルーチンハンドルが有効であれば破棄する
        ~Generator()
        {
            if (coro) coro.destroy();
        }

    private:
        std::coroutine_handle<promise_type> coro;
    };

    /// @brief 偶数のみをフィルタリングする
    /// @param input フィルタ対象の Generator
    /// @return フィルタ後の Generator
    Generator<int> filter_even(Generator<int> input)
    {
        while (input.move_next()) {
            if (input.current_value() % 2 == 0) {
                co_yield input.current_value();
            }
        }
    }

    /// @brief 値を2倍に変換する
    /// @param input 変換対象の Generator
    /// @return 変換後の Generator
    Generator<int> double_values(Generator<int> input)
    {
        while (input.move_next()) {
            co_yield input.current_value() * 2;
        }
    }

    /// @brief 数値の範囲を生成する
    /// @param start 開始値
    /// @param end 終了値
    /// @return 範囲内の数値を生成する Generator
    Generator<int> generate_numbers(int start, int end)
    {
        for (int i = start; i <= end; ++i) {
            co_yield i;
        }
    }
```
このテストを以下に示す。

```cpp
    //  example/core_lang_spec20/co_yield_ut.cpp 127

    // 数値を生成し、それをパイプライン処理に通す
    auto numbers         = generate_numbers(1, 10);
    auto even_numbers    = filter_even(std::move(numbers));
    auto doubled_numbers = double_values(std::move(even_numbers));

    // 結果を検証するために期待される値の配列を準備
    std::vector<int> expected_values = {4, 8, 12, 16, 20};

    // 生成された値を順に取得し、期待される値と比較
    size_t index = 0;
    while (doubled_numbers.move_next()) {
        ASSERT_LT(index, expected_values.size());  // インデックスが範囲内か確認
        EXPECT_EQ(doubled_numbers.current_value(), expected_values[index]);
        ++index;
    }

    // 最終的にすべての期待される値が生成されたことを確認
    EXPECT_EQ(index, expected_values.size());
```

[co_await](#SS_6_10_1_1)、co_returnの例でみたように、
co_yieldを使用したコルーチンと同じ機能を持つクラスのco_yieldを使わない実装を以下に示す。

```cpp
    //  example/core_lang_spec20/co_yield_ut.cpp 152

    /// @brief コルーチンを使わずにデータを逐次的に提供するジェネレータークラス
    template <typename T>
    class Generator {
    public:
        /// @brief コンストラクタ
        /// @param data 生成対象のデータ
        Generator(std::vector<T>&& data) : data_(std::move(data)), current_index_(0) {}

        /// @brief 次の値があるかを確認し、次の値に進む
        /// @return 次の値が存在する場合は true、存在しない場合は false
        bool move_next()
        {
            if (current_index_ < data_.size()) {
                ++current_index_;
                return true;
            }
            return false;
        }

        /// @brief 現在の値を取得する
        /// @return 現在の値
        T current_value() const
        {
            if (current_index_ > 0 && current_index_ <= data_.size()) {
                return data_[current_index_ - 1];
            }
            throw std::out_of_range("Invalid current value access");
        }

    private:
        std::vector<T> data_;           ///< データを保持
        size_t         current_index_;  ///< 現在のインデックス
    };

    /// @brief 偶数のみをフィルタリングする
    /// @param input フィルタ対象の Generator
    /// @return フィルタ後の Generator
    Generator<int> filter_even(const Generator<int>& input)
    {
        std::vector<int> filtered;
        auto             gen = input;

        while (gen.move_next()) {
            if (gen.current_value() % 2 == 0) {
                filtered.push_back(gen.current_value());
            }
        }
        return Generator<int>(std::move(filtered));
    }

    /// @brief 値を2倍に変換する
    /// @param input 変換対象の Generator
    /// @return 変換後の Generator
    Generator<int> double_values(const Generator<int>& input)
    {
        std::vector<int> doubled;
        auto             gen = input;

        while (gen.move_next()) {
            doubled.push_back(gen.current_value() * 2);
        }
        return Generator<int>(std::move(doubled));
    }

    /// @brief 数値の範囲を生成する
    /// @param start 開始値
    /// @param end 終了値
    /// @return 範囲内の数値を生成する Generator
    Generator<int> generate_numbers(int start, int end)
    {
        std::vector<int> numbers;
        for (int i = start; i <= end; ++i) {
            numbers.push_back(i);
        }
        return Generator<int>(std::move(numbers));
    }
```

このクラスは当然ながら、前記のコルーチンの単体テストコードとほぼ同じになる。

```cpp
    //  example/core_lang_spec20/co_yield_ut.cpp 234

    // 数値を生成し、それをパイプライン処理に通す
    auto numbers         = generate_numbers(1, 10);
    auto even_numbers    = filter_even(std::move(numbers));
    auto doubled_numbers = double_values(std::move(even_numbers));

    // 結果を検証するために期待される値の配列を準備
    std::vector<int> expected_values = {4, 8, 12, 16, 20};

    // 生成された値を順に取得し、期待される値と比較
    size_t index = 0;
    while (doubled_numbers.move_next()) {
        ASSERT_LT(index, expected_values.size());  // インデックスが範囲内か確認
        EXPECT_EQ(doubled_numbers.current_value(), expected_values[index]);
        ++index;
    }

    // 最終的にすべての期待される値が生成されたことを確認
    EXPECT_EQ(index, expected_values.size());
```

C++20から導入されたco_await、co_return、TaskとC++17以前の機能のみを使用したコードの対比によって、
コルーチンのサポート機能により実装が容易になることが理解できるだろう。

### モジュール <a id="SS_6_10_2"></a>
モジュールはC++20から導入された機能であり、以下の新しいキーワードによりサポートされる。

* module: モジュールを宣言する。独立した構造を持ち、名前の衝突を防ぐ。
* export: モジュール外部に公開する関数やクラスを指定する。公開しない要素はモジュール内に限定される。
* import: 他のモジュールをインポートして利用できる。従来の#includeと異なり、依存関係を最適化し、ビルド時間を短縮する。

以下にこれらのキーワードのコード例を示す。

まずは、同時に使われることが多い`module`と`export`の使用例を示す。

```cpp
    //  example/module_cmake/type_traits.cppm 1

    export module type_traits;  // モジュール宣言

    namespace type_traits {  // 通常の名前空間。モジュール名と同じにして良い
    namespace Inner_ {       // 内部実装であるためexportしない

    // T == void
    template <typename T>
    constexpr auto is_void_sfinae_f_detector(void const* v, T const* t) noexcept
        -> decltype(t = v, bool{})  // T != voidの場合、t = vはill-formed
                                    // T == voidの場合、well-formedでbool型生成
    {
        return true;
    }

    // T != void
    template <typename T>
    constexpr auto is_void_sfinae_f_detector(void const*, T const*) noexcept
        -> decltype(sizeof(T), bool{})  // T != voidの場合、well-formedでbool型生成
                                        // T == voidの場合、sizeof(T)はill-formed
    {
        return false;
    }
    }  // namespace Inner_

    export
    {  // 纏めてexport
        template <typename T>
        constexpr bool is_void() noexcept
        {
            return Inner_::is_void_sfinae_f_detector(nullptr, static_cast<T*>(nullptr));
        }
        template <typename T>
        bool is_void_v = is_void<T>();
    }
    }  // namespace type_traits
```

最後に`import`の使用例を示す。

```cpp
    //  example/module_cmake/main.cpp 1

    import math;        // モジュールのインポート
    import type_traits; // モジュールのインポート

    #include <iostream>  // これまで同様のインクルード。stdのモジュール化はC++23から

    void f(int a, int b)
    {
        std::cout << "Add: " << math::add(a, b) << std::endl;
        std::cout << "Multiply: " << math::multiply(a, b) << std::endl;

        std::cout << std::boolalpha << type_traits::is_void<void>() << std::endl;
        std::cout << std::boolalpha << type_traits::is_void_v<decltype(a)> << std::endl;
    }
```

これらにより、モジュールは依存関係の管理、名前空間の分離、ビルド時間の短縮を実現し、
大規模プロジェクトでの保守性向上に貢献する。
が、一方ではC++のモジュールに対応してるビルドツールを使用することが望ましい。

### ラムダ式 <a id="SS_6_10_3"></a>
ラムダ式に関する言葉の定義と例を示す。

* ラムダ式とは、その場で関数オブジェクトを定義する式。
* クロージャ(オブジェクト)とは、ラムダ式から生成された関数オブジェクト。
* クロージャ型とは、クロージャオブジェクトの型。
* キャプチャとは、ラムダ式外部の変数をラムダ式内にコピーかリファレンスとして定義する機能。
* ラムダ式からキャプチャできるのは、ラムダ式から可視である自動変数と仮引数(thisを含む)。
* [constexprラムダ](#SS_6_5_9)とはクロージャ型の[constexprインスタンス](#SS_6_5_6)。
* [ジェネリックラムダ](#SS_6_11_6)とは、C++11のラムダ式を拡張して、
  パラメータにautoを使用(型推測)できるようにした機能。

```cpp
    //  example/core_lang_spec/lambda.cpp 10

    auto a = 0;

    // closureがクロージャ。それを初期化する式がラムダ式
    // [a = a]がキャプチャ
    // [a = a]内の右辺aは上記で定義されたa
    // [a = a]内の左辺aは右辺aで初期化された変数。ラムダ式内で使用されるaは左辺a。
    auto closure = [a = a](int32_t b) noexcept { return a + b; };

    auto ret = closure(3);  // クロージャの実行

    // g_closureはジェネリックラムダ
    auto g_closure = [](auto t0, auto t1) { return t0 + t1; };

    auto i = g_closure(1, 2);                                // t0、t1はint
    auto s = g_closure(std::string{"1"}, std::string{"2"});  // t0、t1はstd::string
```

#### クロージャ <a id="SS_6_10_3_1"></a>
「[ラムダ式](#SS_6_10_3)」を参照せよ。

#### クロージャ型 <a id="SS_6_10_3_2"></a>
「[ラムダ式](#SS_6_10_3)」を参照せよ。

#### 一時的ラムダ <a id="SS_6_10_3_3"></a>
一時的ラムダ(transient lambda)とは下記のような使い方をするラムダ式指す慣用用語である。

複雑な初期化を必要とするconstオブジェクトの生成をするような場合に有用なテクニックである。

```cpp
    //  example/core_lang_spec/transient_lambda_ut.cpp 9

    std::vector<int> vec{1, 2, 3};

    // ラムダ式を即時実行するために () を追加
    auto const vec_act = [&vec = vec]() {
        using arg_type = std::remove_reference_t<decltype(vec)>;
        arg_type temp;
        for (auto val : vec) {
            temp.push_back(val * 2);
        }
        return temp;  // 変更後のベクターを返す
    }();

    std::vector<int> const vec_exp{2, 4, 6};

    ASSERT_EQ(vec_act, vec_exp);
```

#### transient lambda <a id="SS_6_10_3_4"></a>
「[一時的ラムダ](#SS_6_10_3_3)」を参照せよ。


### 指示付き初期化 <a id="SS_6_10_4"></a>
指示付き初期化(designated initialization)とは、C++20から導入されたシンタックスであり、
構造体やクラスのメンバを明示的に指定して初期化できるようにする機能である。
この構文により、コードの可読性と安全性が向上し、初期化漏れや順序の誤りを防ぐことができる。

まずは、この機能を有効に使えるクラス例を以下に示す。

```cpp
    //  example/core_lang_spec20/designated_init_ut.cpp 11

    struct Point {
        int  x;
        int  y;
        bool operator==(Point const& rhs) const noexcept = default;
    };

    class Circl {
    public:
        Circl(Point center, uint32_t radius) : center_{center}, radius_{radius} {}

        std::string to_string()
        {
            std::ostringstream oss;

            oss << "center x:" << center_.x << " y:" << center_.y << " radius:" << radius_;
            return oss.str();
        }

        bool operator==(Circl const& rhs) const noexcept = default;

    private:
        Point const center_;
        uint32_t    radius_;
    };
```
```cpp
    //  example/core_lang_spec20/designated_init_ut.cpp 41

    struct Point p0 {
        10, 20
    };
    struct Point p1 {
        .x = 10, .y = 20
    };  // x、yを明示できるため、可読性向上が見込める

    ASSERT_EQ(p0, p1);

    Circl circl_0{p1, 2U};
    ASSERT_EQ("center x:10 y:20 radius:2", circl_0.to_string());

    Circl circl_1{{10, 20}, 2U};  // circl_2に比べると可読性に劣る
    ASSERT_EQ("center x:10 y:20 radius:2", circl_1.to_string());

    Circl circl_2{{.x = 10, .y = 20}, 2U};  // x、yを明示できるため、可読性向上が見込める
    ASSERT_EQ("center x:10 y:20 radius:2", circl_2.to_string());

    ASSERT_EQ(circl_1, circl_2);
```

下記に示すように、[Polymorphic Memory Resource(pmr)](#SS_7_6)のpool_resourceの初期化には、
この機能を使うと可読性の改善が期待できる。

```cpp
    //  example/core_lang_spec20/designated_init_ut.cpp 68

    std::pmr::unsynchronized_pool_resource pool_resource(
        std::pmr::pool_options{
            .max_blocks_per_chunk        = 10,   // チャンクあたりの最大ブロック数
            .largest_required_pool_block = 1024  // 最大ブロックサイズ
        },
        std::pmr::new_delete_resource()  // フォールバックリソース
    );

    std::pmr::vector<int> vec{&pool_resource};  // pmrを使用するベクタの定義
```

指示付き初期化を使わない以下のコード例と上記を比べれば可読性の改善に議論の余地はないだろう。

```cpp
    //  example/core_lang_spec20/designated_init_ut.cpp 83

    // 指示付き初期化を使わずにstd::pmr::unsynchronized_pool_resourceの初期化
    std::pmr::unsynchronized_pool_resource pool_resource(
        std::pmr::pool_options{
            10,   // チャンクあたりの最大ブロック数
            1024  // 最大ブロックサイズ
        },
        std::pmr::new_delete_resource()  // フォールバックリソース
    );

    std::pmr::vector<int> vec{&pool_resource};  // pmrを使用するベクタの定義
```

## テンプレートと型推論 <a id="SS_6_11"></a>
### SFINAE <a id="SS_6_11_1"></a>
[SFINAE](https://cpprefjp.github.io/lang/cpp11/sfinae_expressions.html)
(Substitution Failure Is Not An Errorの略称、スフィネェと読む)とは、
「テンプレートのパラメータ置き換えに失敗した([ill-formed](#SS_6_14_1)になった)際に、
即時にコンパイルエラーとはせず、置き換えに失敗したテンプレートを
[name lookup](#SS_6_12_2)の候補から除外する」
という言語機能である。

### メタ関数 <a id="SS_6_11_2"></a>
メタ関数とは、型を引数として型または値を返すテンプレートのことを指す。
通常の関数が実行時に値を返すのに対し、メタ関数はコンパイル時に型情報を生成または変換する。
主要なメタ関数は標準ライブラリの[type_traits](#SS_7_2)で定義されている。

### コンセプト <a id="SS_6_11_3"></a>
C++17までのテンプレートには以下のような問題があった。

* [SFINAE](#SS_6_11_1)による制約が複雑  
  テンプレートの制約を行うために、
  std::enable_ifやの仕組みを使う必要があり、コードが非常に複雑で難読になりがちだった。
* エラーメッセージが不明瞭  
  テンプレートのパラメータが不適切な型だった場合に、
  コンパイルエラーのメッセージが非常にわかりにくく、問題の原因を特定するのが困難だった。
* テンプレートの適用範囲が不明確  
  テンプレートの使用可能な型の範囲がドキュメントやコメントでしか表現されず、
  明確な制約がコードに反映されていなかったため、コードの意図が伝わりづらい。
* 部分特殊化やオーバーロードによる冗長性  
  特定の型に対するテンプレートの処理を制限するために、
  部分特殊化やテンプレートオーバーロードを行うことが多く、コードが冗長になりがちだった。

C++20から導入された「コンセプト(concepts)」は、
テンプレートパラメータを制約する機能である。
この機能を使用することで、以下のようなプログラミングでのメリットが得られる。

* テンプレートの制約を明確に定義できる  
  コンセプトを使うことで、テンプレートパラメータが満たすべき条件を宣言的に記述できるため、
  コードの意図が明確にできる。
* コンパイルエラーがわかりやすくなる  
  コンセプトを使用すると、テンプレートの適用範囲外の型に対して、
  より具体的でわかりやすいエラーメッセージが表示される。
* コードの可読性が向上する  
  コンセプトを利用することで、
  テンプレート関数やクラスのインターフェースが明確になり、可読性が向上する。

```cpp
    //  example/core_lang_spec/concept_ut.cpp 12

    // SFINAEを使用したc++17スタイル
    template <typename T, typename = typename std::enable_if<std::is_arithmetic<T>::value>::type>
    T add(T a, T b)
    {
        return a + b;
    }

    //  example/core_lang_spec/concept_ut.cpp 24

    ASSERT_EQ(add(10, 20), 30);     // int型
    ASSERT_EQ(add(1.5, 2.5), 4.0);  // double型

    auto str1 = std::string{"Hello, "};
    auto str2 = std::string{"World!"};
    // add(str1, str2);  // これを試すとコンパイルエラー
    // concept_ut.cpp:10:3: note: candidate: ‘template<class T, class> T
    // {anonymous}::old_style::add(T, T)’
    //    10 | T add(T a, T b) {
    //       |   ^~~
    // concept_ut.cpp:10:3: note:   template argument deduction/substitution failed:
    // concept_ut.cpp:9:22: error: no type named ‘type’ in ‘struct std::enable_if<false, void>’
    //     9 | template<typename T, typename = typename
    //     std::enable_if<std::is_arithmetic<T>::value>::type>
    //       |                      ^~~~~~~~
    // エラーメッセージがわかりずらい
```

```cpp
    //  example/core_lang_spec/concept_ut.cpp 49

    // コンセプトを使用したC++20スタイル
    template <typename T>
    concept Arithmetic = std::is_arithmetic_v<T>;

    template <Arithmetic T>
    T add(T a, T b)
    {
        return a + b;
    }

    //  example/core_lang_spec/concept_ut.cpp 64

    ASSERT_EQ(add(10, 20), 30);     // int型
    ASSERT_EQ(add(1.5, 2.5), 4.0);  // double型

    auto str1 = std::string{"Hello, "};
    auto str2 = std::string{"World!"};
    // add(str1, str2);  // これを試すとコンパイルエラー
    // concept_ut.cpp:36:27: note: the expression ‘is_arithmetic_v<T> [with T =
    // std::basic_string<char, std
    // ::char_traits<char>, std::allocator<char> >]’ evaluated to ‘false’
    //    36 | concept Arithmetic = std::is_arithmetic_v<T>;
    //       |                      ~~~~~^~~~~~~~~~~~~~~~~~
    // ↑  エラーメッセージがわかりよい。テンプレートTがコンセプトfalseとなる
```

以下はテンプレートパラメータの制約にstatic_assertを使用した例である。

```cpp
    //  example/core_lang_spec/concept_ut.cpp 85

    // 制約のためにstatic_assertを使用したC++17スタイル
    template <typename FLOAT_0, typename FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        static_assert(std::is_floating_point_v<FLOAT_0>, "FLOAT_0 shoud be float or double.");
        static_assert(std::is_same_v<FLOAT_0, FLOAT_1>, "FLOAT_0 and FLOAT_1 shoud be a same type.");

        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }
```

以上の関数テンプレートをコンセプトを使用して改善した例である。

```cpp
    //  example/core_lang_spec/concept_ut.cpp 113

    // 標準コンセプト std::floating_point と std::same_as を使用
    template <std::floating_point FLOAT_0, std::same_as<FLOAT_0> FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }
```

フレキシブルに制約を記述するためにrequiresを使用したコード例を下記する。

```cpp
    //  example/core_lang_spec/concept_ut.cpp 138

    #if __cplusplus >= 202002L  // c++20

    // requiresを使った関数テンプレートの制約
    template <typename FLOAT_0, typename FLOAT_1>
    requires std::floating_point<FLOAT_0> && std::same_as<FLOAT_0, FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }

    #else  // c++17
    template <typename FLOAT_0, typename FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        static_assert(std::is_same_v<FLOAT_0, FLOAT_1>);
        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }
    #endif

```

### パラメータパック <a id="SS_6_11_4"></a>
パラメータパック(parameter pack)は、可変長テンプレート引数を表現するためにC++11で導入されたシンタックスである。
テンプレートの定義時に、任意個数のテンプレート引数または関数引数をまとめて受け取ることができる。

パラメータパックのシンタックスは以下のようなものである。

* `typename... Args` - テンプレートパラメータパック
* `Args... args` - 関数パラメータパック
* `args...` - パック展開（pack expansion）
* `sizeof...(args)` - パック内の要素数を取得

パラメータパックを使用した関数テンプレートは以下のように定義する。

```cpp
    //  example/core_lang_spec/template_ut.cpp 70

    void print(std::ostream& os) { os << std::endl; }

    template <typename HEAD, typename... TAIL>
    int print(std::ostream& os, HEAD head, TAIL... tail)
    {
        os << head;
        print(os, tail...);  // 残りの引数を再帰的に処理

        return 1 + sizeof...(tail);  // headの1個 + tailの個数 = 全パラメータ数
                                     // sizeof...(tail)はパック内の要素数
    }
```

以下の単体テストは上記の関数の使い方を示している。

```cpp
    //  example/core_lang_spec/template_ut.cpp 87

    std::stringstream os;

    auto parameter_pack_count = print(os, 1, "-", "c_str-", std::string{"std::string"});

    ASSERT_EQ("1-c_str-std::string\n", os.str());
    ASSERT_EQ(4, parameter_pack_count);
```

### 畳み込み式 <a id="SS_6_11_5"></a>
畳み式(fold expression)とは、C++17から導入された新機能であり、
可変引数テンプレートのパラメータパックに対して二項演算を累積的に行うためのものである。

畳み込み式のシンタックスの使用は下記のようなものである。
```
( pack op ... )          // (1) 単項右畳み込み
( ... op pack )          // (2) 単項左畳み込み
( pack op ... op init )  // (3) 二項右畳み込み
( init op ... op pack )  // (4) 二項左畳み込み
```

1. 単項右畳み込み
```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 9

    namespace cpp14_style {  // c++14までのスタイル
    template <typename T>
    constexpr bool all_true(T arg)
    {
        return arg;
    }
    template <typename T, typename... Args>
    constexpr bool all_true(T arg, Args... args)
    {
        return arg && all_true(args...);
    }
    }  // namespace cpp14_style

    namespace cpp17_style {  // 畳み込み式を使用したスタイル
    template <typename... Ts>
    constexpr bool all_true(Ts... args)
    {
        return (args && ...);  // 単項右畳み込み
    }
    }  // namespace cpp17_style

    static_assert(cpp14_style::all_true(true, true, true));
    static_assert(cpp17_style::all_true(true, true, true));
```
2. 単項左畳み込み
```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 36
    namespace cpp14_style {  // c++14までのスタイル
    template <typename T>
    constexpr bool any_true(T arg)
    {
        return arg;
    }
    template <typename T, typename... Args>
    constexpr bool any_true(T arg, Args... args)
    {
        return arg || any_true(args...);
    }
    }  // namespace cpp14_style

    namespace cpp17_style {  // 畳み込み式を使用したスタイル
    template <typename... Ts>
    constexpr bool any_true(Ts... args)
    {
        return (... || args);  // 単項左畳み込み
    }
    }  // namespace cpp17_style
    static_assert(cpp14_style::any_true(false, false, true));
    static_assert(cpp17_style::any_true(false, false, true));
```
3. 二項右畳み込み
```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 61

    namespace cpp14_style {  // c++14までのスタイル
    template <typename T>
    constexpr int sum(T arg)
    {
        return arg;
    }
    template <typename T, typename... Args>
    constexpr int sum(T arg, Args... args)
    {
        return arg + sum(args...);
    }

    }  // namespace cpp14_style

    namespace cpp17_style {  // 畳み込み式を使用したスタイル
    template <typename... Ts>
    constexpr int sum(Ts... args)
    {
        return (args + ... + 0);  // 二項右畳み込み (初期値: 0)
    }
    }  // namespace cpp17_style

    static_assert(cpp14_style::sum(1, 2, 3));
    static_assert(cpp17_style::sum(1, 2, 3));
```
4. 二項左畳み込み
```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 89

    namespace cpp14_style {  // c++14までのスタイル
    template <typename T>
    constexpr int product(T arg)
    {
        return arg;
    }
    template <typename T, typename... Args>
    constexpr int product(T arg, Args... args)
    {
        return arg * product(args...);
    }
    }  // namespace cpp14_style

    namespace cpp17_style {  // 畳み込み式を使用したスタイル
    template <typename... Ts>
    constexpr int product(Ts... args)
    {
        return (1 * ... * args);  // 二項左畳み込み (初期値: 1)
    }
    }  // namespace cpp17_style

    static_assert(cpp14_style::product(2, 3, 4));
    static_assert(cpp17_style::product(2, 3, 4));
```

上記したような単純な例では、畳み込み式の効果はわかりづらいため、
もっと複雑なで読解が困難な再帰構造を持ったコードを以下に示す。

```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 117
    template <typename T, typename U, typename... Us>
    struct is_same_some_of {
        static constexpr bool value{std::is_same_v<T, U> ? true : is_same_some_of<T, Us...>::value};
    };

    template <typename T, typename U>
    struct is_same_some_of<T, U> {
        static constexpr bool value{std::is_same_v<T, U>};
    };
```
```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 128

    static_assert(is_same_some_of<int, int, double, char>::value);
    static_assert(!is_same_some_of<int, double, char>::value);
    static_assert(is_same_some_of<std::string, std::string, int>::value);
```

畳み込み式を使うことで、この問題をある程度緩和したコードを下記する。

```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 140
    template <typename T, typename U, typename... Us>
    struct is_same_some_of {
        static constexpr bool value = (std::is_same_v<T, U> || ... || std::is_same_v<T, Us>);
    };
```
```cpp
    //  example/core_lang_spec/flold_expression_ut.cpp 146

    static_assert(is_same_some_of<int, int, double, char>::value);
    static_assert(!is_same_some_of<int, double, char>::value);
    static_assert(is_same_some_of<std::string, std::string, int>::value);
```

### ジェネリックラムダ <a id="SS_6_11_6"></a>
ジェネリックラムダとは、C++11のラムダ式のパラメータの型にautoを指定できるようにした機能で、
C++14で導入された。

この機能により関数の中で関数テンプレートと同等のものが定義できるようになった。

ジェネリックラムダで定義されたクロージャは、通常のラムダと同様にオブジェクトであるため、
下記のように使用することもできる便利な記法である。

```cpp
    //  example/core_lang_spec/generic_lambda_ut.cpp 4

    template <typename PUTTO>
    void f(PUTTO&& p)
    {
        p(1);
        p(2.71);
        p("str");
    }

    TEST(Template, generic_lambda)
    {
        std::ostringstream oss;

        f([&oss](auto const& elem) { oss << elem << std::endl; });

        ASSERT_EQ("1\n2.71\nstr\n", oss.str());
    }
```

なお、上記のジェネリックラムダは下記クラスのインスタンスの動きと同じである。

```cpp
    //  example/core_lang_spec/generic_lambda_ut.cpp 23

    class Closure {
    public:
        Closure(std::ostream& os) : os_(os) {}

        template <typename T>
        void operator()(T&& t)
        {
            os_ << t << std::endl;
        }

    private:
        std::ostream& os_;
    };

    TEST(Template, generic_lambda_like)
    {
        std::ostringstream oss;

        Closure closure(oss);
        f(closure);

        ASSERT_EQ("1\n2.71\nstr\n", oss.str());
    }
```

### クラステンプレートのテンプレート引数の型推論 <a id="SS_6_11_7"></a>
C++17から、
「コンストラクタに渡される値によって、クラステンプレートのテンプレート引数を推論する」
機能が導入された。

この機能がないC++14までは以下のように記述する必要があった。

```cpp
    //  example/core_lang_spec/template_ut.cpp 14

    auto a = std::vector<int>{1, 2, 3};

    static_assert(std::is_same_v<decltype(a), std::vector<int>>);
```

これに対して、この機能により、以下のようにシンプルに記述できるようになった。

```cpp
    //  example/core_lang_spec/template_ut.cpp 25

    auto a = std::vector{1, 2, 3};

    static_assert(std::is_same_v<decltype(a), std::vector<int>>);  // テンプレート引数がintと推論
```

### CTAD(Class Template Argument Deduction) <a id="SS_6_11_8"></a>
CTAD（Class Template Argument Deduction、クラステンプレート実引数推論）は、C++17で導入された機能である。
この機能により、クラステンプレートのインスタンス化時にテンプレート引数を明示的に指定せず、
コンストラクタの引数から自動的に型を推論できるようになる。
クラステンプレートの型推論が不十分な場合、[テンプレートの型推論ガイド](#SS_6_11_9)を追加することにより、
型推論を強化することができる。


### テンプレートの型推論ガイド <a id="SS_6_11_9"></a>
[CTAD(Class Template Argument Deduction)](#SS_6_11_8)による型推論をカスタマイズするために、型推論ガイドを定義できる。
特にコンストラクタがテンプレートである場合など、暗黙の型推論では不十分な場合に有用である。

```cpp
    //  example/core_lang_spec/deduction_guide_ut.cpp 8

    template <typename T>  // Tが整数型の場合、暗黙の型変換を許可
    struct S {
        // T が整数型でない場合に有効なコンストラクタ
        template <typename U = T, std::enable_if_t<!std::is_integral_v<U>>* = nullptr>
        explicit S(U x) : value{x}
        {
        }

        // T が整数型の場合に有効な非explicitコンストラクタ
        template <typename U = T, std::enable_if_t<std::is_integral_v<U>>* = nullptr>
        S(U x) : value{x}
        {
        }

        T value;
    };

```

上記のクラステンプレートは、型推論ガイドがない場合、コンストラクタがテンプレートであるため、
[CTAD(Class Template Argument Deduction)](#SS_6_11_8)による型推論ができない。
そのため、以下のように明示的にテンプレート引数を指定する必要がある。

```cpp
    //  example/core_lang_spec/deduction_guide_ut.cpp 31

    // 型推論ガイドがないため、下記はコンパイルできない
    // S s1{42};   // エラー: テンプレート引数を推論できない
    // S s2{1.0};  // エラー: テンプレート引数を推論できない

    // 上記の問題を回避するためには型推論ガイドを定義するか、テンプレート引数を指定しなければならない
    S<int>    s1{42};   // 明示的にテンプレート引数を指定
    S<double> s2{1.0};  // 明示的にテンプレート引数を指定
```

以上に示したクラステンプレートに以下の型推論ガイドを追加することにより、
テンプレート引数を型推論できるようになる。

```cpp
    //  example/core_lang_spec/deduction_guide_ut.cpp 44

    template <typename T>
    S(T) -> S<T>;
```
```cpp
    //  example/core_lang_spec/deduction_guide_ut.cpp 52

    S s1{42};   // 推論ガイドの効果
    S s2{1.0};  // 推論ガイドの効果
    S s3 = 42;  // OK: S<int>のコンストラクタが非explicitのため、暗黙の変換が可能
    // S    s4 = 1.0;  // S<double>のコンストラクタがexplicitであるため、暗黙の変換不可
```

多くの場合、コンパイラは暗黙の型推論ガイドを生成するため、明示的に型推論ガイドを書く必要はない。
明示的な型推論ガイドが必要なのは、 上記の例のようにコンストラクタがテンプレートである場合や、
特殊な推論ルールが必要な場合である。

### 変数テンプレート <a id="SS_6_11_10"></a>
変数テンプレートとは、下記のコード示したような機能である。

```cpp
    //  example/core_lang_spec/template_ut.cpp 33

    template <typename T>
    struct is_void {
        static constexpr bool value = false;
    };

    template <>
    struct is_void<void> {
        static constexpr bool value = true;
    };

    static_assert(is_void<void>::value);
    static_assert(!is_void<int>::value);
    // 以上はC++14以前のスタイル

    // 以下はC++17から導入された
    template <typename T>
    constexpr bool is_void_v = is_void<T>::value;

    static_assert(is_void_v<void>);
    static_assert(!is_void_v<int>);
```

なお、変数テンプレートはconstexprと定義されるが、
「定数テンプレート」ではなく変数テンプレートである。


### エイリアステンプレート <a id="SS_6_11_11"></a>
エイリアステンプレート(alias templates)とはC++11から導入され、
下記のコード例で示したようにテンプレートによって型の別名を定義する機能である。

```cpp
    //  example/core_lang_spec/template_ut.cpp 57

    using IntVector = std::vector<int>;  // std::vector<int> のエイリアスを定義

    template <typename T>  //エイリアステンプレートを定義
    using Vec = std::vector<T>;

    static_assert(std::is_same_v<IntVector, Vec<int>>);  // Vec<int> == std::vector<int>
```

### constexpr if文 <a id="SS_6_11_12"></a>
C++17で導入された[constexpr if文](https://cpprefjp.github.io/lang/cpp17/if_constexpr.html)とは、
文を条件付きコンパイルすることができるようにするための制御構文である。

まずは、この構文を使用しない例を示す。

```cpp
    //  example/core_lang_spec/constexpr_if_ut.cpp 9

    // 配列のサイズ
    template <typename T>
    auto Length(T const&) -> std::enable_if_t<std::is_array_v<T>, size_t>
    {
        return std::extent_v<T>;
    }

    // コンテナのサイズ
    template <typename T>
    auto Length(T const& t) -> decltype(t.size())
    {
        return t.size();
    }

    // その他のサイズ
    size_t Length(...) { return 0; }
```
```cpp
    //  example/core_lang_spec/constexpr_if_ut.cpp 31

    uint32_t a[5];
    auto     v = std::vector{0, 1, 2};
    struct SizeTest {
    } t;

    ASSERT_EQ(5, Length(a));
    ASSERT_EQ(3, Length(v));
    ASSERT_EQ(0, Length(t));

    // C++17で、Lengthと同様の機能の関数テンプレートがSTLに追加された
    ASSERT_EQ(std::size(a), Length(a));
    ASSERT_EQ(std::size(v), Length(v));
```

このような場合、[SFINAE](#SS_6_11_1)によるオーバーロードが必須であったが、
この文を使用することで、下記のようにオーバーロードを使用せずに記述できるため、
条件分岐の可読性の向上が見込める。

```cpp
    //  example/core_lang_spec/constexpr_if_ut.cpp 52

    struct helper {
        template <typename T>
        auto operator()(T const& t) -> decltype(t.size());
    };

    template <typename T>
    size_t Length(T const& t)
    {
        if constexpr (std::is_array_v<T>) {  // Tが配列の場合
            // Tが配列でない場合、他の条件のブロックはコンパイル対象外
            return std::extent_v<T>;
        }
        else if constexpr (std::is_invocable_v<helper, T>) {  // T::Lengthが呼び出せる場合
            // T::Lengthが呼び出せない場合、他の条件のブロックはコンパイル対象外
            return t.size();
        }
        else {  // それ以外
            // Tが配列でなく且つ、T::Lengthが呼び出ない場合、他の条件のブロックはコンパイル対象外
            return 0;
        }
    }
```

この構文は[パラメータパック](#SS_6_11_4)の展開においても有用な場合がある。

```cpp
    //  example/core_lang_spec/constexpr_if_ut.cpp 93

    // テンプレートパラメータで与えられた型のsizeofの値が最も大きな値を返す。
    template <typename HEAD>
    constexpr size_t MaxSizeof()
    {
        return sizeof(HEAD);
    }

    template <typename HEAD, typename T, typename... TAILS>
    constexpr size_t MaxSizeof()
    {
        return std::max(sizeof(HEAD), MaxSizeof<T, TAILS...>());
    }
```
```cpp
    //  example/core_lang_spec/constexpr_if_ut.cpp 111

    static_assert(4 == (MaxSizeof<int8_t, int16_t, int32_t>()));
    static_assert(4 == (MaxSizeof<int32_t, int16_t, int8_t>()));
    static_assert(sizeof(std::string) == MaxSizeof<int32_t, int16_t, int8_t, std::string>());
```

C++14までの構文を使用する場合、
上記のようなオーバーロードとリカーシブコールの組み合わせが必要であったが、
constexpr ifを使用することで、やや単純に記述できる。

```cpp
    //  example/core_lang_spec/constexpr_if_ut.cpp 123

    // テンプレートパラメータで与えられた型のsizeofの値が最も大きな値を返す。
    template <typename HEAD, typename... TAILS>
    constexpr size_t MaxSizeof()
    {
        if constexpr (sizeof...(TAILS) == 0) {  // TAILSが存在しない場合
            return sizeof(HEAD);
        }
        else {
            return std::max(sizeof(HEAD), MaxSizeof<TAILS...>());
        }
    }
```

### autoパラメータによる関数テンプレートの簡易定義 <a id="SS_6_11_13"></a>
この機能は、C++20から導入された。
下記のコードで示すように簡易的に関数テンプレートを定義するための機能である。

```cpp
    //  example/core_lang_spec20/abbreviated_func_template_ut.cpp 11

    auto add(auto lhs, auto rhs)  // c++20で導入された記法
    {
        return lhs + rhs;
    }
```
```cpp
    //  example/core_lang_spec20/abbreviated_func_template_ut.cpp 21

    ASSERT_EQ(add(1, 2), 3);

    ASSERT_DOUBLE_EQ(add(1.5, 2.5), 4.0);

    using namespace std::literals::string_literals;

    ASSERT_EQ(add("hello"s, "world"s), "helloworld"s);
```

### auto <a id="SS_6_11_14"></a>
autoは、C++11で導入された型推論キーワードである。変数宣言時に明示的な型指定を省略し、
初期化式からコンパイラが型を自動的に推定する。 これにより、複雑な型やテンプレート使用時の記述が簡潔になり、
可読性と保守性が向上する。
コード例については、[decltype](#SS_6_11_15)を参照せよ。

### decltype <a id="SS_6_11_15"></a>
decltypeはオペランドに[expression](#SS_6_7_1)を取り、その型を算出する機能である。
下記のコードにあるようなautoの機能との微妙な差に気を付ける必要がある。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 13

    int32_t  x{3};
    int32_t& r{x};

    auto        a = r;  // aの型はint32_t
    decltype(r) b = r;  // bの型はint32_t&

    // std::is_sameはオペランドの型が同じか否かを返すメタ関数
    static_assert(std::is_same_v<decltype(a), int>);
    static_assert(std::is_same_v<decltype(b), int&>);
```

decltypeは、テンプレートプログラミングに多用されるが、
クロージャ型(「[ラムダ式](#SS_6_10_3)」参照)
のような記述不可能な型をオブジェクトから算出できるため、
下記例のような場合にも有用である。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 28

    //  本来ならばA::dataは、
    //      * A::Aでメモリ割り当て
    //      * A::~Aでメモリ解放
    //  すべきだが、何らかの理由でそれが出来ないとする
    struct A {
        size_t   len;
        uint8_t* data;
    };

    void do_something(size_t len)
    {
        auto deallocate = [](A* p) {
            delete[](p->data);
            delete p;
        };

        auto a_ptr = std::unique_ptr<A, decltype(deallocate)>{new A, deallocate};

        a_ptr->len  = len;
        a_ptr->data = new uint8_t[10];

        // ...
        // do something for a_ptr
        // ...

        // a_ptrによるメモリの自動解放
    }
```

### decltype(auto) <a id="SS_6_11_16"></a>
decltype(auto)はC++14から導入されたdecltypeの類似機能である。

auto、decltype、decltype(auto)では、以下に示す通りリファレンスの扱いが異なることに注意する必要がある。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 63

    int32_t  x{3};
    int32_t& r{x};

    auto           a = r;  // aの型はint32_t
    decltype(r)    b = r;  // bの型はint32_t&
    decltype(auto) c = r;  // cの型はint32_t&   C++14からサポート
                           // decltype(auto)は、decltypeに右辺の式を与えるための構文

    // std::is_sameはオペランドの型が同じか否かを返すメタ関数
    static_assert(std::is_same_v<decltype(a), int>);
    static_assert(std::is_same_v<decltype(b), int&>);
    static_assert(std::is_same_v<decltype(c), int&>);
```

### 戻り値型を後置する関数宣言 <a id="SS_6_11_17"></a>
関数の戻り値型後置構文は戻り値型をプレースホルダ(auto)にして、
実際の型を->で示して型推論させるシンタックスを指す。実際には関数テンプレートで使用されることが多い。
コード例を以下に示す。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 82

    template <typename T, typename U>
    auto add(T a, U b) -> decltype(a + b)
    {
        return a + b;
    }

    static_assert(std::is_same_v<decltype(add(1, 2)), int>);         // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(1u, 2u)), uint32_t>);  // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(std::string{"str"}, "2")),
                                 std::string>);  // addの戻り値型はstd::stringに型推論
```

この構文をC++11から導入された理由は以下のコードを見れば明らかだろう。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 97

    template <typename T, typename U>  // 戻り値型を後置する関数宣言
    decltype(std::declval<T>() + std::declval<T>()) add(T a, U b)
    {
        return a + b;
    }

    static_assert(std::is_same_v<decltype(add(1, 2)), int>);         // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(1u, 2u)), uint32_t>);  // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(std::string{"str"}, "2")),
                                 std::string>);  // addの戻り値型はstd::stringに型推論
```

### 関数の戻り値型auto <a id="SS_6_11_18"></a>
C++14から導入された機能で、関数の戻り値の型をautoキーワードで宣言することで、
コンパイラがreturn文から自動的に型を推論してくれる機能である。
これにより、複雑な型の戻り値を持つ関数でも、より簡潔に記述できるようになる
(「[autoパラメータによる関数テンプレートの簡易定義](#SS_6_11_13)」を参照)。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 114

    // 戻り値型autoが使えないと下記のような宣言が必要
    // std::vector<std::string> split(std::string_view str, char delimiter)
    auto split(std::string_view str, char delimiter)
    {
        std::vector<std::string> result;
        std::string              token;

        for (char ch : str) {
            if (ch == delimiter) {
                if (!token.empty()) {
                    result.emplace_back(std::move(token));
                }
            }
            else {
                token += ch;
            }
        }

        if (!token.empty()) {
            result.emplace_back(std::move(token));
        }

        return result;
    }
```
```cpp
    //  example/core_lang_spec/decltype_ut.cpp 144

    auto result = split("hello,world", ',');

    ASSERT_EQ(result.size(), 2);
    ASSERT_EQ(result[0], "hello");
    ASSERT_EQ(result[1], "world");
```

### 後置戻り値型auto <a id="SS_6_11_19"></a>
C++14から導入された[関数の戻り値型auto](#SS_6_11_18)と似た、
関数の戻り値の型を関数本体の後に-> autoと書くことでができる機能である。
autoプレースホルダーとし、そのプレースホルダーを修飾することで、戻り値型の推論を補助できる。

```cpp
    //  example/core_lang_spec/decltype_ut.cpp 154

    int16_t gvalue = 1;

    auto getValue(int16_t a) -> auto& { return gvalue += a; }
```
```cpp
    //  example/core_lang_spec/decltype_ut.cpp 163

    auto           ret1 = getValue(10);
    decltype(auto) ret2 = getValue(0);

    ASSERT_EQ(ret1, 11);
    ASSERT_EQ(ret2, 11);

    ASSERT_EQ(gvalue, 11);
    ret1 += 1;
    ASSERT_EQ(gvalue, 11);

    ret2 += 1;
    ASSERT_EQ(gvalue, 12);
```

## name lookupと継承構造 <a id="SS_6_12"></a>
ここではname lookupとそれに影響を与える名前空間について解説する。

### ルックアップ <a id="SS_6_12_1"></a>
このドキュメントでのルックアップとは[name lookup](#SS_6_12_2)を指す。

### name lookup <a id="SS_6_12_2"></a>
[name lookup](https://en.cppreference.com/w/cpp/language/lookup)
とはソースコードで名前が検出された時に、その名前をその宣言と関連付けることである。
以下、name lookupの例を上げる。

下記のようなコードがあった場合、

```cpp
    //  example/core_lang_spec/name_lookup_ut.cpp 5

    namespace NS_LU {
    int f() noexcept { return 0; }
    }  // namespace NS_LU
```

以下のコードでの関数呼び出しf()のname lookupは、


```cpp
    //  example/core_lang_spec/name_lookup_ut.cpp 29

    NS_LU::f();
```

1. NS_LUをその前方で宣言された名前空間と関連付けする
2. f()呼び出しをその前方の名前空間NS_LUで宣言された関数fと関連付ける

という手順で行われる。

下記のようなコードがあった場合、

```cpp
    //  example/core_lang_spec/name_lookup_ut.cpp 11

    namespace NS_LU {
    bool g(int i) noexcept { return i < 0; }

    char g(std::string_view str) noexcept { return str[0]; }

    template <typename T, size_t N>
    size_t g(T const (&)[N]) noexcept
    {
        return N;
    }
```

以下のコードでの関数呼び出しg()のname lookupは、


```cpp
    //  example/core_lang_spec/name_lookup_ut.cpp 37
    int a[3]{1, 2, 3};
    NS_LU::g(a);
```

1. NS_LUをその前方で宣言された名前空間と関連付けする
2. 名前空間NS_LU内で宣言された複数のgを見つける
3. g()呼び出しを、
   すでに見つけたgの中からベストマッチしたg(T const (&)[N])と関連付ける

という手順で行われる。

下記記のようなコードがあった場合、

```cpp
    //  example/core_lang_spec/name_lookup_ut.cpp 44

    // グローバル名前空間
    std::string ToString(int i) { return std::to_string(i) + " in Global"; }

    namespace NS_LU {
    struct X {
        int i;
    };

    std::string ToString(X const& x) { return std::to_string(x.i) + " in NS_LU"; }
    }  // namespace NS_LU

    namespace NS2 {
    std::string ToString(NS_LU::X const& x) { return std::to_string(x.i) + " in NS2"; }
    }  // namespace NS2
```

以下のコードでの関数呼び出しToString()のname lookupは、

```cpp
    //  example/core_lang_spec/name_lookup_ut.cpp 65

    auto x = NS_LU::X{1};

    ASSERT_EQ("1 in NS_LU", ToString(x));
```

1. ToString()呼び出しの引数xの型Xが名前空間NS_LUで定義されているため、
   ToStringを探索する名前空間にNS_LUを組み入れる(「[関連名前空間](#SS_6_12_6)」参照)
2. ToString()呼び出しより前方で宣言されたグローバル名前空間とNS_LUの中から、
   複数のToStringの定義を見つける
3. ToString()呼び出しを、
   すでに見つけたToStringの中からベストマッチしたNS_LU::ToStringと関連付ける

という手順で行われる。


### two phase name lookup <a id="SS_6_12_3"></a>
[two phase name lookup](https://en.cppreference.com/w/cpp/language/two-phase_lookup)
とはテンプレートをインスタンス化するときに使用される、下記のような2段階でのname lookupである。

1. テンプレート定義内でname lookupを行う(通常のname lookupと同じ)。
   この時、テンプレートパラメータに依存した名前
   ([dependent_name](https://en.cppreference.com/w/cpp/language/dependent_name))は
   name lookupの対象外となる(name lookupの対象が確定しないため)。
2. 1の後、テンプレートパラメータを展開した関数内で、
   [関連名前空間](#SS_6_12_6)の宣言も含めたname lookupを行う。

以下の議論では、

* 上記1のname lookupを1st name lookup
* 上記2のname lookupを2nd name lookup

と呼ぶことにする。

下記のようなコードがあった場合、

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 5

    namespace NS_TPLU {
    struct X {
        int i;
    };
    }  // namespace NS_TPLU

    // グローバル名前空間
    inline std::string ToType(NS_TPLU::X const&) { return "X in global"; }
    inline std::string ToType(int const&) { return "int in global"; }

    // 再びNS_TPLU
    namespace NS_TPLU {

    std::string Header(long) { return "type:"; }  //  下記にもオーバーロードあり

    template <typename T>
    std::string ToType(T const&)  //  下記にもオーバーロードあり
    {
        return "unknown";
    }

    template <typename T>
    std::string TypeName(T const& t)  // オーバーロードなし
    {
        return Header(int{}) + ToType(t);
    }

    std::string Header(int) { return "TYPE:"; }  // 上記にもオーバーロードあり

    std::string ToType(X const&) { return "X"; }      // 上記にもオーバーロードあり
    std::string ToType(int const&) { return "int"; }  // 上記にもオーバーロードあり
    }  // namespace NS_TPLU
```

以下のコードでのTypeNameのインスタンス化に伴うname lookupは、

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 44

    auto x = NS_TPLU::X{1};

    ASSERT_EQ("type:X", TypeName(x));
```

1. TypeName()呼び出しの引数xの型Xが名前空間NS_TPLUで宣言されているため、
   NS_TPLUをTypeNameを探索する[関連名前空間](#SS_6_12_6)にする。
2. TypeName()呼び出しより前方で宣言されたグローバル名前空間とNS_TPLUの中からTypeNameを見つける。
3. TypeNameは関数テンプレートであるためtwo phase lookupが以下のように行われる。
    1. TypeName内でのHeader(int{})の呼び出しは、1st name lookupにより、
       Header(long)の宣言と関連付けられる。
       Header(int)はHeader(long)よりもマッチ率が高い、
       TypeNameの定義より後方で宣言されているため、name lookupの対象外となる。
    2. TypeName内でのToType(t)の呼び出しに対しては、2nd name lookupが行われる。
       このためTypeName定義より前方で宣言されたグローバル名前空間と、
       tの型がNS_TPLU::Xであるため[関連名前空間](#SS_6_12_6)となったNS_TPLUがname lookupの対象となるが、
       グローバル名前空間内のToTypeは、
       NS_TPLU内でTypeNameより前に宣言されたtemplate<> ToTypeによって[name-hiding](#SS_6_12_9)が起こり、
       TypeNameからは非可視となるためname lookupの対象から外れる。
       このため、ToType(t)の呼び出しは、NS_TPLU::ToType(X const&)の宣言と関連付けられる。

という手順で行われる。

上と同じ定義、宣言がある場合の以下のコードでのTypeNameのインスタンス化に伴うname lookupは、

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 50

    ASSERT_EQ("type:unknown", NS_TPLU::TypeName(int{}));
```

1. NS_TPLUを名前空間と関連付けする
   (引数の型がintなのでNS_TPLUは[関連名前空間](#SS_6_12_6)とならず、NS_TPLUを明示する必要がある)。
2. TypeName()呼び出しより前方で宣言されたNS_TPLUの中からTypeNameを見つける。
3. TypeNameは関数テンプレートであるためtwo phase lookupが以下のように行われる。
    1. TypeName内でのHeader(int{})の呼び出しは、1st name lookupにより、
       前例と同じ理由で、Header(long)の宣言と関連付けられる。
    2. TypeName内でのToType(t)の呼び出しに対しては、2nd name lookupが行われる。
       tの型がintであるためNS_TPLUは[関連名前空間](#SS_6_12_6)とならず、通常のname lookupと同様に
       ToType(t)の呼び出し前方のグローバル名前空間とNS_TPLUがname lookupの対象になるが、
       グローバル名前空間内のToTypeは、
       NS_TPLU内でTypeNameより前に宣言されたtemplate<> ToTypeによって[name-hiding](#SS_6_12_9)が起こり、
       TypeNameからは非可視となるためname lookupの対象から外れる。
       また、ToType(int const&)は、TypeNameの定義より後方で宣言されているため、
       name lookupの対象外となり、
       その結果、ToType(t)の呼び出しは、NS_TPLU内のtemplate<> ToTypeの宣言と関連付けられる。

という手順で行われる。

以上の理由から、先に示した例でのToTypeの戻り値は"X"となり、
後に示した例でのToTypeの戻り値は"unknown"となる。
これはtwo phase lookupの結果であり、
two phase lookupが実装されていないコンパイラ(こういったコンパイラは存在する)では、
結果が異なるため注意が必要である
(本ドキュメントではこのような問題をできる限り避けるために、
サンプルコードを[g++](#SS_8_13_1)と[clang++](#SS_8_13_2)でコンパイルしている)。

以下に、two phase lookupにまつわるさらに驚くべきコード例を紹介する。
上と同じ定義、宣言がある場合の以下のコードの動作を考える。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 54

    ASSERT_EQ("type:long", NS_TPLU::TypeName(long{}));
```

NS_TPLU::TypeName(int{})のintをlongにしただけなので、この単体テストはパスしないが、
この単体テストコードの後(実際にはこのファイルのコンパイル単位の中のNS_TPLU内で、
且つtemplate<> ToTypeの宣言の後方であればどこでもよい)
に以下のコードを追加するとパスしてしまう。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 61

    namespace NS_TPLU {
    template <>
    std::string ToType<long>(long const&)
    {
        return "long";
    }
    }  // namespace NS_TPLU
```

この理由は、関数テンプレート内での2nd name lookupで選択された名前が関数テンプレートであった場合、
その特殊化の検索範囲はコンパイル単位内になることがあるからである
([template_specialization](https://en.cppreference.com/w/cpp/language/template_specialization)
によるとこの動作は未定義のようだが、
[g++](#SS_8_13_1)/[clang++](#SS_8_13_2)両方ともこのコードを警告なしでコンパイルする)。

TypeName(long{})内でのtwo phase name lookupは、TypeName(int{})とほぼ同様に進み、
template<> ToTypeの宣言を探し出すが、
さらに前述したようにこのコンパイル単位のNS_TPLU内からその特殊化も探し出す。
その結果、ToType(t)の呼び出しは、NS_TPLU内のtemplate<> ToType\<long>の定義と関連付けられる。

以上の議論からわかる通り、関数テンプレートとその特殊化の組み合わせは、
そのインスタンス化箇所(この場合単体テストコード内)の後方から、
name lookupでバインドされる関数を変更することができるため、
極めて分かりづらいコードを生み出す。ここから、

* 関数テンプレートとその特殊化はソースコード上なるべく近い位置で宣言するべきである
* STL関数テンプレートの特殊化は行うべきではない

という教訓が得られる。

なお、関数とその関数オーバーロードのname lookupの対象は、呼び出し箇所前方の宣言のみであるため、
関数テンプレートToType(T const& t)の代わりに、関数ToType(...)を使うことで、
上記問題は回避可能である。

次に示す例は、一見2nd name lookupで関連付けされるように見える関数ToType(NS_TPLU2::Y const&)が、
実際には関連付けされないコードである。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 71

    namespace NS_TPLU2 {
    struct Y {
        int i;
    };
    }  // namespace NS_TPLU2
```
```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 79

    // global名前空間
    template <typename T>
    std::string ToType(T const&)
    {
        return "unknown";
    }

    template <typename T>
    std::string TypeName(T const& t)
    {
        return "type:" + ToType(t);
    }

    std::string ToType(NS_TPLU2::Y const&) { return "Y"; }
```

これは先に示したNS_TPLU::Xの例と極めて似ている。本質的な違いは、
TypeNameやToTypeがグローバル名前空間で宣言されていることのみである。
だが、下記の単体テストで示す通り、
TypeName内でのname lookupで関数オーバーライドToType(NS_TPLU2::Y const&)が選択されないのである。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 100

    auto y = NS_TPLU2::Y{1};

    // ASSERT_EQ("type:Y", TypeName(y));
    ASSERT_EQ("type:unknown", TypeName(y));  // ToType(NS_TPLU2::Y const&)は使われない
```

ここまでの現象を正確に理解するには、
「two phase lookupの対象となる宣言」を下記のように、より厳密に認識する必要がある。

* TypeNameの中で行われる1st name lookupの対象となる宣言は下記の積集合である。
    * TypeNameと同じ名前空間内かグローバル名前空間内の宣言
    * TypeName定義位置より前方の宣言

* TypeNameの中で行われる2nd name lookupの対象となる宣言は下記の和集合である。
    * 1st name lookupで使われた宣言
    * TypeName呼び出しより前方にある[関連名前空間](#SS_6_12_6)内の宣言

この認識に基づくNS_TPLU2::Yに対するグローバルなTypeName内でのtwo phase name lookupは、

1. TypeName内に1st name lookupの対象がないため何もしない。
2. TypeName内の2nd name lookupに使用される[関連名前空間](#SS_6_12_6)NS_TPLU2は、
   ToType(NS_TPLU2::Y const&)の宣言を含まないため、この宣言は2nd name lookupの対象とならない。
   その結果、ToType(t)の呼び出しは関数テンプレートToType(T const&)と関連付けられる。

という手順で行われる。

以上が、TypeNameからToType(NS_TPLU2::Y const&)が使われない理由である。

ここまでで示したようにtwo phase name lookupは理解しがたく、
理解したとしてもその使いこなしはさらに難しい。

次のコードは、この難解さに翻弄されるのが現場のプログラマのみではないことを示す。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 71

    namespace NS_TPLU2 {
    struct Y {
        int i;
    };
    }  // namespace NS_TPLU2
```
```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 110

    // global名前空間
    template <typename T>
    int operator+(T const&, int i)
    {
        return i;
    }

    template <typename T>
    int TypeNum(T const& t)
    {
        return t + 0;
    }

    int operator+(NS_TPLU2::Y const& y, int i) { return y.i + i; }
```

上記の宣言、定義があった場合、operator+の単体テストは以下のようになる。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 132

    auto y = NS_TPLU2::Y{1};

    ASSERT_EQ(1, y + 0);  // 2つ目のoperator+が選択される
```

このテストは当然パスするが、次はどうだろう？

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 142

    auto y = NS_TPLU2::Y{1};

    ASSERT_EQ(1, TypeNum(y));  // g++ではoperator+(NS_TPLU2::Y const&, int i)がname lookupされる
```

これまでのtwo phase name lookupの説明では、
operator+(NS_TPLU2::Y const& y, int i)はTypeNum内でのname lookupの対象にはならないため、
このテストはエラーとならなければならないが、[g++](#SS_8_13_1)ではパスしてしまう。
2nd name lookupのロジックにバグがあるようである。

有難いことに、[clang++](#SS_8_13_2)では仕様通りこのテストはエラーとなり、
当然ながら以下のテストはパスする(つまり、g++ではエラーする)。

```cpp
    //  example/core_lang_spec/two_phase_name_lookup_ut.cpp 151

    auto y = NS_TPLU2::Y{1};

    ASSERT_EQ(0, TypeNum(y));  // clang++ではoperator+(T const&, int i)がname lookupされる
```

なお、TypeNum内のコードである

```cpp
    return t + 0;
```

を下記のように変更することで

```cpp
    return operator+(t, 0);
```

g++のname lookupはclang++と同じように動作するため、
記法に違和感があるものの、この方法はg++のバグのワークアランドとして使用できる。

また、operator+(NS_TPLU2::Y const& y, int i)をNS_TPLU2で宣言することで、
g++ではパスしたテストをclang++でもパスさせられるようになる(これは正しい動作)。
これにより、型とその2項演算子オーバーロードは同じ名前空間で宣言するべきである、
という教訓が得られる。

以上で見てきたようにtwo phase name lookupは、現場プログラマのみではなく、
コンパイラを開発するプログラマをも混乱させるほど難解ではあるが、
STLを含むテンプレートメタプログラミングを支える重要な機能であるため、
C++プログラマには、最低でもこれを理解し、出来れば使いこなせるようになってほしい。


### 実引数依存探索 <a id="SS_6_12_4"></a>
実引数依存探索とは、argument-dependent lookupの和訳語であり、
通常はその略語である[ADL](#SS_6_12_5)と呼ばれる。

### ADL <a id="SS_6_12_5"></a>
ADLとは、関数の実引数の型が宣言されている名前空間(これを[関連名前空間](#SS_6_12_6)と呼ぶ)内の宣言が、
その関数の[name lookup](#SS_6_12_2)の対象になることである。

下記のようなコードがあった場合、

```cpp
    //  example/core_lang_spec/name_lookup_adl_ut.cpp 5
    namespace NS_ADL {
    struct A {
        int i;
    };

    std::string ToString(A const& a) { return std::string{"A:"} + std::to_string(a.i); }
    }  // namespace NS_ADL
```

以下のコードでのToStringの呼び出しに対するのname lookupは、

```cpp
    //  example/core_lang_spec/name_lookup_adl_ut.cpp 18

    auto a = NS_ADL::A{0};

    ASSERT_EQ("A:0", ToString(a));  // ADLの効果により、ToStringはNS_ADLを指定しなくても見つかる
```

* ToStringの呼び出しより前方で行われているグローバル名前空間内の宣言
* ToStringの呼び出しより前方で行われているNS_ADL内の宣言

の両方を対象として行われる。
NS_ADL内の宣言がToStringの呼び出しに対するのname lookupの対象になる理由は、
ToStringの呼び出しに使われている実引数aの型AがNS_ADLで宣言されているからである。
すでに述べたようにこれをADLと呼び、この場合のNS_ADLを[関連名前空間](#SS_6_12_6)と呼ぶ。

ADLは思わぬname lookupによるバグを誘発することもあるが、
下記コードを見れば明らかなように、また、
多くのプログラマはそれと気づかずに使っていることからもわかる通り、
コードをより自然に、より簡潔に記述するための重要な機能となっている。

```cpp
    //  example/core_lang_spec/name_lookup_adl_ut.cpp 28

    // 下記operator <<は、std::operator<<(ostream&, string const&)であり、
    // namespace stdで定義されている。

    // ADLがあるため、operator <<は名前空間修飾無しで呼び出せる。
    std::cout << std::string{__func__};

    // ADLが無いと下記のような呼び出しになる。
    std::operator<<(std::cout, std::string{__func__});
```

### 関連名前空間 <a id="SS_6_12_6"></a>
関連名前空間(associated namespace)とは、
[ADL](#SS_6_12_5)(実引数依存探索)によってname lookupの対象になった宣言を含む名前空間のことである。


### 修飾付き関数呼び出し <a id="SS_6_12_7"></a>
修飾付き関数呼び出し(Qualified Call)は、
C++で関数やメンバ関数を明示的にスコープやクラス名で修飾して呼び出す方法である。
名前の曖昧性を回避し、特定の関数やクラスメンバを明確に選択する際に利用される。
これにより、意図しない[name lookup](#SS_6_12_2)を回避することができるため、可読性と安全性が向上する。
一方で、[ADL](#SS_6_12_5)が働かなくなるため、フレキシブルな[name lookup](#SS_6_12_2)ができなくなる。

```cpp
    //  example/core_lang_spec/etc_ut.cpp 40

    extern void func();  // グローバル名前空間での宣言

    struct Base {
        void func() const noexcept {}
    };

    A::func();  // 名前空間名による修飾

    struct Derived : Base {
        // void        func() { func(); /* funcの無限リカーシブコール */ }
        void        func() { Base::func(); /* クラス名での修飾 */ }
        void        func(int) { ::func(); /* グローバル修飾 */ }
        void        func(Base) { this->func(); /* thisによる修飾 */ }
        static void func(std::string) {}
    };

    Base b;
    b.func();        // 通常の関数呼び出し
    b.Base::func();  // クラス名での修飾による関数呼び出し

    Derived d;
    Derived::func("str");  // クラス名での修飾による関数呼び出し
    d.func("str");         // 通常の関数呼び出し
```

### hidden-friend関数 <a id="SS_6_12_8"></a>
hidden-friend関数(隠れたフレンド関数、あるいは単にhidden-friend)とは、

* クラスの内部で定義された、
* 名前空間スコープでの通常の[name lookup](#SS_6_12_2)できず、[ADL](#SS_6_12_5)のみでname lookupできる

friend関数のことを指す。このような性質から、non-namespace-visible friend関数と呼ばれることもある。

これにより、意図的に外部からのアクセスを制限し、
必要な場合にのみ利用されることを保証する設計が可能となる。

hidden-friend関数(隠れたフレンド関数)の目的は、

* カプセル化の強化：
  クラスの内部実装を外部から隠しつつ、特定の操作だけを許可する。
* 名前空間汚染の防止：
  関数が名前空間スコープに現れないため、他の名前と衝突しにくい。
* 最適化：
  コンパイラによる最適化を妨げることなく、特定の機能を提供する。

```cpp
    //  example/core_lang_spec/hidden_friend_ut.cpp 7

    namespace NS {
    class Person {
    public:
        Person(std::string name, uint32_t age) : name_{std::move(name)}, age_{age} {}

        // hidden-friend関数
        friend std::ostream& operator<<(std::ostream& os, const Person& person)
        {
            os << "Name:" << person.name_ << ", Age:" << person.age_;
            return os;
        }

    private:
        std::string const name_;
        uint32_t const    age_;
    };
    }  // namespace NS
```
```cpp
    //  example/core_lang_spec/hidden_friend_ut.cpp 31

    NS::Person         alice("Alice", 30);
    std::ostringstream oss;

    oss << alice;  // フレンド関数を呼び出す(ADLによって見つかる)
    ASSERT_EQ("Name:Alice, Age:30", oss.str());

    // 以下はエラー（operator<<がNS名前空間スコープで見えない）
    // NS::Person::operator<<(oss, alice);
    // 上記は以下のようなコンパイルエラーになる
    //  error: ‘operator<<’ is not a member of ‘NS::Person’
```


### name-hiding <a id="SS_6_12_9"></a>
name-hidingとは
「前方の識別子が、その後方に同一の名前をもつ識別子があるために、
[name lookup](#SS_6_12_2)の対象外になる」現象一般を指す通称である
([namespace](https://en.cppreference.com/w/cpp/language/namespace)参照)。

まずは、クラスとその派生クラスでのname-hidingの例を示す。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 4

    struct Base {
        void f() {}
    };

    struct Derived : Base {
        // void f(int) { f(); }     // f()では、Baseのf()をname lookupできないため、
        void f(int) { Base::f(); }  // Base::でf()を修飾した
    };
```

上記の関数fは一見オーバーロードに見えるが、そうではない。下記のコードで示したように、
Base::f()には、修飾しない形式でのDerivedクラス経由のアクセスはできない。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 18

    {
        auto d = Derived{};
    #if 0 
        d.f(); // コンパイルできない
    #else
        d.Base::f();  // Base::での修飾が必要
    #endif
    }
```

これは前述したように、
Base::fがその後方にあるDerived::f(int)によりname-hidingされたために起こる現象である
(name lookupによる探索には識別子が使われるため、シグネチャの違いはname-hidingに影響しない)。

下記のように[using宣言](#SS_6_12_14)を使用することで、
修飾しない形式でのDerivedクラス経由のBase::f()へのアクセスが可能となる。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 34

    struct Derived : Base {
        using Base::f;        // using宣言によりDerivedにBase::fを導入
        void f(int) { f(); }  // using Base::fの効果でfの名前修飾が不要になった
    };
```
```cpp
    //  example/core_lang_spec/name_hiding.cpp 45

    auto d = Derived{};
    d.f();  // using宣言によりコンパイルできる
```

下記コードは、名前空間でも似たような現象が起こることを示している。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 54

    // global名前空間
    void f() {}

    namespace NS_A {
    void f(int) {}

    void g()
    {
    #if 0
        f();  // NS_A::fによりname-hidingされたため、コンパイルできない
    #endif
    }
    }  // namespace NS_A
```

この問題に対しては、下記のようにf(int)の定義位置を後方に移動することで回避できる。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 70

    namespace NS_A_fixed_0 {
    void g()
    {
        // グローバルなfの呼び出し
        f();  // NS_A::fは後方に移動されたためコンパイルできる
    }

    void f(int) {}
    }  // namespace NS_A_fixed_0
```

また、先述のクラスでの方法と同様にusing宣言を使い、下記のようにすることもできる。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 82

    namespace NS_A_fixed_1 {
    void f(int) {}

    void g()
    {
        using ::f;

        // グローバルなfの呼び出し
        f();  // using宣言によりコンパイルできる
    }
    }  // namespace NS_A_fixed_1
```

当然ながら、下記のようにf()の呼び出しを::で修飾することもできる。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 96

    namespace NS_A_fixed_2 {
    void f(int) {}

    void g()
    {
        // グローバルなfの呼び出し
        ::f();  // ::で修飾すればコンパイルできる
    }
    }  // namespace NS_A_fixed_2
```

修飾の副作用として「[two phase name lookup](#SS_6_12_3)」の例で示したような
[ADL](#SS_6_12_5)を利用した高度な静的ディスパッチが使用できなくなるが、
通常のソフトウェア開発では、ADLが必要な場面は限られているため、
デフォルトでは名前空間を使用して修飾を行うことにするのが、
無用の混乱をさけるための安全な記法であると言えるだろう。

次に、そういった混乱を引き起こすであろうコードを示す。

```cpp
    //  example/core_lang_spec/name_hiding.cpp 108

    namespace NS_B {
    struct S_in_B {};

    void f(S_in_B) {}
    void f(int) {}

    namespace NS_B_Inner {
    void g()
    {
        f(int{});  // コンパイルでき、NS_B::f(int)が呼ばれる
    }

    void f() {}

    void h()
    {
        // f(int{});     // コンパイルできない
        NS_B::f(int{});  // 名前空間で修飾することでコンパイルできる

        f(S_in_B{});  // ADLによりコンパイルできる
    }
    }  // namespace NS_B_Inner
    }  // namespace NS_B
```

NS_B_Inner::g()内のf(int)の呼び出しはコンパイルできるが、
name-hidingが原因で、NS_B_Inner::h()内のf(int)の呼び出しはコンパイルできず、
名前空間で修飾することが必要になる。
一方で、ADLの効果で名前空間での修飾をしていないf(S_in_B)の呼び出しはコンパイルできる。

全チームメンバがこういったname lookupを正しく扱えると確信できないのであれば、
前述の通り、デフォルトでは名前空間を使用して修飾を行うのが良いだろう。

### ダイヤモンド継承 <a id="SS_6_12_10"></a>
ダイヤモンド継承(Diamond Inheritance)とは、以下のような構造のクラス継承を指す。

* 基底クラス(Base)が一つ存在し、その基底クラスから二つのクラス(Derived_0、Derived_1)が派生する。
* Derived_0とDerived_1からさらに一つのクラス(DerivedDerived)が派生する。
  したがって、DerivedDerivedはBaseの孫クラスとなる。

この継承は、多重継承の一形態であり、クラス図で表すと下記のようになるため、
ダイヤモンド継承と呼ばれる。

```essential/plant_uml/diamond_inheritance.pu
@startuml

class Base
class Derived_0
class Derived_1
class DerivedDerived

Derived_0 -up-> Base
Derived_1 -up-> Base
DerivedDerived -up-> Derived_1
DerivedDerived -up-> Derived_0

@enduml


```

ダイヤモンド継承は、
[仮想継承](#SS_6_12_11)(virtual inheritance)を使ったものと、使わないものに分類できる。

[仮想継承](#SS_6_12_11)を使わないダイヤモンド継承のコードを以下に示す。

```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 6

    class Base {
    public:
        int32_t get() const noexcept { return x_; }
        void    set(int32_t x) noexcept { x_ = x; }

    private:
        int32_t x_ = 0;
    };

    class Derived_0 : public Base {};

    class Derived_1 : public Base {};

    class DerivedDerived : public Derived_0, public Derived_1 {};
```
```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 26

    auto dd = DerivedDerived{};

    Base& b0 = static_cast<Derived_0&>(dd);  // Derived_0::Baseのリファレンス
    Base& b1 = static_cast<Derived_1&>(dd);  // Derived_1::Baseのリファレンス

    ASSERT_NE(&b0, &b1);  // ddの中には、Baseインスタンスが2つできる
```

これからわかるように、DerivedDerivedインスタンスの中に2つのBaseインスタンスが存在する。
この状態をオブジェクト図で表すと下記のようになる。

```essential/plant_uml/diamond_inheritance_obj.pu
@startuml
object base1 as "Base (from Derived_0)"
object base2 as "Base (from Derived_1)"
object d0 as "Derived_0"
object d1 as "Derived_1"
object dd as "DerivedDerived"

d0 -up-> base1
d1 -up-> base2
dd -up-> d0
dd -up-> d1
@enduml

```

下記コードは、それが原因で名前解決が曖昧になりコンパイルできない。

```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 36

    Base& b = dd;  // Derived_0::Base or Derived_1::Base ?

    dd.get();  // Derived_0::get or  Derived_1::get ?

    // 下記のようなエラーが発生する
    //  diamond_inheritance_ut.cpp:37:15: error: ‘Base’ is an ambiguous base of ‘DerivedDerived’
    //     37 |     Base& b = dd;  // Derived_0::Base or Derived_1::Base ?
    //        |               ^~
    //  diamond_inheritance_ut.cpp:39:8: error: request for member ‘get’ is ambiguous
    //     39 |     dd.get();  // Derived_0::get or  Derived_1::get ?
    //        |        ^~~
```

この問題に対処するには、クラス名による修飾が必要になるが、
Baseインスタンスが2つ存在するため、下記に示すようなわかりづらいバグの温床となる。

```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 53

    ASSERT_EQ(0, dd.Derived_0::get());  // クラス名による名前修飾
    ASSERT_EQ(0, dd.Derived_1::get());

    dd.Derived_0::set(1);
    ASSERT_EQ(1, dd.Derived_0::get());  // Derived_0::Base::x_は1に変更
    ASSERT_EQ(0, dd.Derived_1::get());  // Derived_1::Base::x_は0のまま

    dd.Derived_1::set(2);
    ASSERT_EQ(1, dd.Derived_0::get());  // Derived_0::Base::x_は1のまま
    ASSERT_EQ(2, dd.Derived_1::get());  // Derived_1::Base::x_は2に変更
```

次に示すのは、[仮想継承](#SS_6_12_11)を使用したダイヤモンド継承の例である。

```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 70

    class Base {
    public:
        int32_t get() const noexcept { return x_; }
        void    set(int32_t x) noexcept { x_ = x; }

    private:
        int32_t x_ = 0;
    };

    class Derived_0 : public virtual Base {};  // 仮想継承

    class Derived_1 : public virtual Base {};  // 仮想継承

    class DerivedDerived : public Derived_0, public Derived_1 {};
```
```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 90

    auto dd = DerivedDerived{};

    Base& b0 = static_cast<Derived_0&>(dd);  // Derived_0::Baseのリファレンス
    Base& b1 = static_cast<Derived_1&>(dd);  // Derived_1::Baseのリファレンス

    ASSERT_EQ(&b0, &b1);  // ddの中には、Baseインスタンスが1つできる
```

仮想継承の効果で、DerivedDerivedインスタンスの中に存在するBaseインスタンスは1つになるため、
上で示した仮想継承を使わないダイヤモンド継承での問題は解消される
(が、[仮想継承](#SS_6_12_11)による別の問題が発生する)。

```cpp
    //  example/core_lang_spec/diamond_inheritance_ut.cpp 99

    Base& b = dd;  // Baseインスタンスは1つであるため、コンパイルできる

    dd.get();  // Baseインスタンスは1つであるため、コンパイルできる

    dd.Derived_0::set(1);               // クラス名による修飾
    ASSERT_EQ(1, dd.Derived_1::get());  // Derived_1::BaseとDerived_1::Baseは同一であるため

    dd.set(2);
    ASSERT_EQ(2, dd.get());
```

この状態をオブジェクト図で表すと下記のようになる。

```essential/plant_uml/diamond_inheritance_virtual_obj.pu
@startuml
object base as "Base (single instance)"
object d0 as "Derived_0"
object d1 as "Derived_1"
object dd as "DerivedDerived"

d0 -up-> base
d1 -up-> base
dd -up-> d0
dd -up-> d1
@enduml

```

### 仮想継承 <a id="SS_6_12_11"></a>
下記に示した継承方法を仮想継承、仮想継承の基底クラスを仮想基底クラスと呼ぶ。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 9

    class Base {
    public:
        explicit Base(int32_t x = 0) noexcept : x_{x} {}
        int32_t get() const noexcept { return x_; }

    private:
        int32_t x_;
    };

    class DerivedVirtual : public virtual Base {  // 仮想継承
    public:
        explicit DerivedVirtual(int32_t x) noexcept : Base{x} {}
    };
```

仮想継承は、[ダイヤモンド継承](#SS_6_12_10)の基底クラスのインスタンスを、
その継承ヒエラルキーの中で1つのみにするための言語機能である。

仮想継承の独特の動作を示すため、
上記コードに加え、仮想継承クラス、通常の継承クラス、
それぞれを通常の継承したクラスを下記のように定義する。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 25

    class DerivedDerivedVirtual : public DerivedVirtual {  // 仮想継承を通常の継承
    public:
        // 注: DerivedDerivedVirtualのコンストラクタは、Baseのデフォルトコンストラクタを呼び出す
        explicit DerivedDerivedVirtual(int32_t x) noexcept : DerivedVirtual{x} {}
    };

    class DerivedNormal : public Base {  // 通常の継承
    public:
        explicit DerivedNormal(int32_t x) noexcept : Base{x} {}
    };

    class DerivedDerivedNormal : public DerivedNormal {  // 通常継承を通常の継承
    public:
        explicit DerivedDerivedNormal(int32_t x) noexcept : DerivedNormal{x} {}
    };
```

この場合、継承ヒエラルキーに仮想継承を含むクラスと、含まないクラスでは、
以下に示したような違いが発生する。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 46

    auto dv = DerivedVirtual{1};  // 仮想継承クラス
    auto dn = DerivedNormal{1};   // 通常の継承クラス

    ASSERT_EQ(1, dv.get());  // これは非仮想継承と同じ動作
    ASSERT_EQ(1, dn.get());

    auto ddv = DerivedDerivedVirtual{1};  // 仮想継承クラスを継承したクラス Base::Base()が呼ばれる
    auto ddn = DerivedDerivedNormal{1};   // 通常継承クラスを継承したクラス Base::Base(1)が呼ばれる

    ASSERT_EQ(0, ddv.get());  // ddvのBaseインスタンスはのデフォルトコンストラクタで初期化されている
    ASSERT_EQ(1, ddn.get());
```

この動作は、下記の仕様に起因している
(引数なしで呼び出せる基底クラスのコンストラクタがない場合はコンパイルエラー)。

__「仮想継承クラスを継承したクラスが、仮想継承クラスの基底クラスのコンストラクタを明示的に呼び出さない場合、
引数なしで呼び出せる基底クラスのコンストラクタが呼ばれる」__  

以下では、これを「仮想継承のコンストラクタ呼び出し」仕様と呼ぶことにする。

仮想継承クラスが、基底クラスのコンストラクタを呼び出したとしても、この仕様が優先されるため、
上記コードのような動作となる。

これを通常の継承クラスと同様な動作にするには、下記のようにしなければならない。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 62

    class DerivedDerivedVirtualFixed : public DerivedVirtual {  // DerivedDerivedNormalと同じように動作
    public:
        explicit DerivedDerivedVirtualFixed(int32_t x) noexcept : Base{x}, DerivedVirtual{x} {}
        //                     基底クラスのコンストラクタ呼び出し ^^^^^^^
    };
```
```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 73

    DerivedDerivedVirtual      ddv{1};   // 仮想継承クラスを継承したクラス
    DerivedDerivedVirtualFixed ddvf{1};  // 上記クラスのコンストラクタを修正したクラス
    DerivedDerivedNormal       ddn{1};   // 通常の継承クラスを継承したクラス

    ASSERT_EQ(0, ddv.get());  // 仮想継承独特の動作
    ASSERT_EQ(1, ddvf.get());
    ASSERT_EQ(1, ddn.get());
```
「仮想継承のコンストラクタ呼び出し」仕様は、
[ダイヤモンド継承](#SS_6_12_10)での基底クラスのコンストラクタ呼び出しを一度にするために存在する。

もし、この機能がなければ、下記のコードでの基底クラスのコンストラクタ呼び出しは2度になるため、
デバッグ困難なバグが発生してしまうことは容易に想像できるだろう。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 88

    int32_t base_called;

    class Base {
    public:
        explicit Base(int32_t x = 0) noexcept : x_{x} { ++base_called; }
        int32_t get() const noexcept { return x_; }

    private:
        int32_t x_;
    };

    class Derived_0 : public virtual Base {  // 仮想継承
    public:
        explicit Derived_0(int32_t x) noexcept : Base{x} { assert(base_called == 1); }
    };

    class Derived_1 : public virtual Base {  // 仮想継承
    public:
        explicit Derived_1(int32_t x) noexcept : Base{x} { assert(base_called == 1); }
    };

    class DerivedDerived : public Derived_0, public Derived_1 {
    public:
        DerivedDerived(int32_t x0, int32_t x1) noexcept : Derived_0{x0}, Derived_1{x1} {}
        // 「仮想継承のコンストラクタ呼び出し」仕様がなければ、このコンストラクタは、
        //    Base::Base -> Derived_0::Derived_0 ->
        //      Base::Base -> Derived_0::Derived_0 ->
        //        DerivedDerived::DerivedDerived
        //  という呼び出しになるため、Base::Baseが2度呼び出されてしまう。
    };
```
```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 124

    ASSERT_EQ(0, base_called);

    auto dd = DerivedDerived{2, 3};  // Base::Baseが最初に呼ばれないとassertion failする

    ASSERT_EQ(1, base_called);  // 「仮想継承のコンストラクタ呼び出し」仕様のため
    ASSERT_EQ(0, dd.get());     // Baseのデフォルトコンストラクタは、x_を0にする
```

基底クラスのコンストラクタ呼び出しは、下記のコードのようにした場合でも、
単体テストが示すように、一番最初に行われる。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 139

    class DerivedDerived : public Derived_0, public Derived_1 {
    public:
        DerivedDerived(int32_t x0, int32_t x1) noexcept : Derived_0{x0}, Derived_1{x1}, Base{1} {}
    };
```
```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 151

    ASSERT_EQ(0, base_called);

    auto dd = DerivedDerived{2, 3};  // Base::Baseが最初に呼ばれないとassertion failする

    ASSERT_EQ(1, base_called);  // 「仮想継承のコンストラクタ呼び出し」仕様のため
    ASSERT_EQ(1, dd.get());     // Base{1}呼び出しの効果
```

このため、基底クラスのコンストラクタ呼び出しは下記のような順番で行うべきである。

```cpp
    //  example/core_lang_spec/virtual_inheritance_ut.cpp 164

    class DerivedDerived : public Derived_0, public Derived_1 {
    public:
        DerivedDerived(int32_t x0, int32_t x1) noexcept : Base{1}, Derived_0{x0}, Derived_1{x1} {}
    };
```

### 仮想基底 <a id="SS_6_12_12"></a>
仮想基底(クラス)とは、[仮想継承](#SS_6_12_11)の基底クラス指す。

### ドミナンス <a id="SS_6_12_13"></a>
[ドミナンス(Dominance、支配性)](https://en.wikipedia.org/wiki/Dominance_(C%2B%2B))とは、
「探索対称の名前が継承の中にも存在するような場合の[name lookup](#SS_6_12_2)の仕様の一部」
を指す慣用句である。

以下に

* [ダイヤモンド継承を含まない場合](#SS_6_12_13_1)
* [ダイヤモンド継承かつそれが仮想継承でない場合](#SS_6_12_13_2)
* [ダイヤモンド継承かつそれが仮想継承である場合](#SS_6_12_13_3)

のドミナンスについてのコードを例示する。

この例で示したように、[ダイヤモンド継承](#SS_6_12_10)を通常の継承で行うか、
[仮想継承](#SS_6_12_11)で行うかでは結果が全く異なるため、注意が必要である。

#### ダイヤモンド継承を含まない場合 <a id="SS_6_12_13_1"></a>

```cpp
    //  example/core_lang_spec/dominance_ut.cpp 9

    int32_t f(double) noexcept { return 0; }

    struct Base {
        int32_t f(int32_t) const noexcept { return 1; }
        int32_t f(double) const noexcept { return 2; }
    };

    struct Derived : Base {
        int32_t f(int32_t) const noexcept { return 3; }  // Base::fを隠蔽する(name-hiding)
    };

    struct DerivedDerived : Derived {
        int32_t g() const noexcept { return f(2.14); }
    };
```
```cpp
    //  example/core_lang_spec/dominance_ut.cpp 29

    Base b;

    ASSERT_EQ(2, b.f(2.14));  // オーバーロード解決により、B::f(double)が呼ばれる

    DerivedDerived dd;

    // Derivedのドミナンスにより、B::fは、DerivedDerived::gでのfのname lookupの対象にならず、
    // DerivedDerived::gはDerived::fを呼び出す。
    ASSERT_EQ(3, dd.g());
```

この[name lookup](#SS_6_12_2)については、[name-hiding](#SS_6_12_9)で説明した通りである。

#### ダイヤモンド継承かつそれが仮想継承でない場合 <a id="SS_6_12_13_2"></a>

```cpp
    //  example/core_lang_spec/dominance_ut.cpp 45

    struct Base {
        int32_t f(int32_t) const noexcept { return 1; }
        int32_t f(double) const noexcept { return 2; }
    };

    struct Derived_0 : Base {
        int32_t f(int32_t) const noexcept { return 3; }  // Base::fを隠蔽する(name-hiding)
    };

    struct Derived_1 : Base {};

    struct DerivedDerived : Derived_0, Derived_1 {
        int32_t g() const noexcept { return f(2.14); }  // Derived_0::f or Derived_1::f ?
    };

    // dominance_ut.cpp:58:41: error: reference to ‘f’ is ambiguous
    //    58 |     int32_t g() const noexcept { return f(2.14); }  // Derived_0::f or Derived_1::f ?
    //       |                                         ^
```

上記コードはコードブロック内のコメントのようなメッセージが原因でコンパイルできない。

Derived_0のドミナンスにより、DerivedDerived::gはDerived_0::fを呼び出すように見えるが、
もう一つの継承元であるDerived_1が導入したDerived_1::f(実際には、Derived_1::Base::f)があるため、
Derived_1によるドミナンスも働き、その結果として、呼び出しが曖昧(ambiguous)になることで、
このような結果となる。

#### ダイヤモンド継承かつそれが仮想継承である場合 <a id="SS_6_12_13_3"></a>

```cpp
    //  example/core_lang_spec/dominance_ut.cpp 71

    struct Base {
        int32_t f(int32_t) const noexcept { return 1; }
        int32_t f(double) const noexcept { return 2; }
    };

    struct Derived_0 : virtual Base {
        int32_t f(int32_t) const noexcept { return 3; }  // Base::fを隠蔽する(name-hiding)
    };

    struct Derived_1 : virtual Base {};

    struct DerivedDerived : Derived_0, Derived_1 {
        int32_t g() const noexcept { return f(2.14); }
    };
```
```cpp
    //  example/core_lang_spec/dominance_ut.cpp 92

    DerivedDerived dd;

    // Derived_0のドミナンスと仮想継承の効果により、
    // B::fは、DerivedDerived::gでのfのname lookupの対象にならず、
    // DerivedDerived::gはDerived_0::fを呼び出す。
    ASSERT_EQ(3, dd.g());
```

これまでと同様にDerived_0のドミナンスによりBase::fは[name-hiding](#SS_6_12_9)されることになる。
この時、Derived_0、Derived_1がBaseから[仮想継承](#SS_6_12_11)した効果により、
この継承ヒエラルキーの中でBaseは１つのみ存在することになるため、
Derived_1により導入されたBase::fも併せて[name-hiding](#SS_6_12_9)される。
結果として、曖昧性は排除され、コンパイルエラーにはならず、このような結果となる。

### using宣言 <a id="SS_6_12_14"></a>
using宣言とは、"using XXX::func"のような記述である。
この記述が行われたスコープでは、この記述後の行から名前空間XXXでの修飾をすることなく、
funcが使用できる。

```cpp
    //  example/core_lang_spec/namespace_ut.cpp 6
    namespace XXX {
    void func() noexcept {}
    void gunc() noexcept {}
    }  // namespace XXX
```
```cpp
    //  example/core_lang_spec/namespace_ut.cpp 12

    // global namespace
    void using_declaration() noexcept
    {
        using XXX::func;  // using宣言

        func();       // XXX::不要
        XXX::gunc();  // XXX::必要
    }

```

### usingディレクティブ <a id="SS_6_12_15"></a>
usingディレクティブとは、"using namespace XXX"のような記述である。
この記述が行われたスコープでは、下記例のように、この記述後から名前空間XXXでの修飾をすることなく、
XXXの識別子が使用できる。

```cpp
    //  example/core_lang_spec/namespace_ut.cpp 6
    namespace XXX {
    void func() noexcept {}
    void gunc() noexcept {}
    }  // namespace XXX
```
```cpp
    //  example/core_lang_spec/namespace_ut.cpp 24

    // global namespace
    void using_directive() noexcept
    {
        using namespace XXX;  // usingディレクティブ

        func();  // XXX::不要
        gunc();  // XXX::不要
    }
```

より多くの識別子が名前空間の修飾無しで使えるようになる点において、
[using宣言](#SS_6_12_14)よりも危険であり、また、
下記のように[name-hiding](#SS_6_12_9)された識別子の導入には効果がない。

```cpp
    //  example/core_lang_spec/namespace_ut.cpp 6
    namespace XXX {
    void func() noexcept {}
    void gunc() noexcept {}
    }  // namespace XXX
```
```cpp
    //  example/core_lang_spec/namespace_ut.cpp 35

    namespace XXX_Inner {
    void func(int) noexcept {}
    void using_declaration() noexcept
    {
    #if 0
        using namespace XXX;  // name-hidingのため効果がない
    #else
        using XXX::func;  // using宣言
    #endif

        func();  // XXX::不要
    }
```

従って、usingディレクティブの使用は避けるべきである。


## エクセプション安全性の保証 <a id="SS_6_13"></a>
関数のエクセプション発生時の安全性の保証には以下の3つのレベルが規定されている。

* [no-fail保証](#SS_6_13_1)
* [強い安全性の保証](#SS_6_13_2)
* [基本的な安全性の保証](#SS_6_13_3)

### no-fail保証 <a id="SS_6_13_1"></a>
「no-fail保証」を満たす関数はエクセプションをthrowしない。
no-failを保証する関数は、
[noexcept](#SS_6_13_4)を使用してエクセプションを発生させないことを明示できる。

標準テンプレートクラスのパラメータとして使用するクラスのメンバ関数には、
正確にnoexceptの宣言をしないと、
テンプレートクラスのメンバ関数によってはパフォーマンスを起こしてしまう可能性がある。

### 強い安全性の保証 <a id="SS_6_13_2"></a>
「強い保証」を満たす関数は、この関数がエクセプションによりスコープから外れた場合でも、
この関数が呼ばれなかった状態と同じ(プログラムカウンタ以外の状態は同じ)であることを保証する。
従って、この関数呼び出しは成功したか、完全な無効だったかのどちらかになる。

### 基本的な安全性の保証 <a id="SS_6_13_3"></a>
「基本的な安全性の保証」を満たす関数は、この関数がエクセプションによりスコープから外れた場合でも、
メモリ等のリソースリークは起こさず、
オブジェクトは(変更されたかもしれないが)引き続き使えることを保証する。

### noexcept <a id="SS_6_13_4"></a>
C++11で導入されたnoexceptキーワードには、以下の2つの意味がある。

* C++03までのthrowキーワードによるエクセプション仕様の代替。
  関数がどのエクセプションを送出する可能性があるかを列挙するのではなく、
  エクセプションを送出する可能性があるかないかのみを指定する。

* sizeofと同じような形式で使用されるのような演算子としてのnoexceptは、
  noexcept(expression)の形式使用され、
  expressionがエクセプションを送出しないと宣言されている場合(noexceptと宣言された関数の呼び出し)、
  noexcept(expression)は静的にtrueとなる。

以下に上記のコード例を示す。

```cpp
    //  example/core_lang_spec/noexcept_ut.cpp 11

    std::string f_noexcept() noexcept  // エクセプションを発生させない
    {
        return "No exceptions here!";
    }

    std::string f_except() noexcept(false)  // エクセプションを発生させる
    {
        throw std::runtime_error{"always throw"};

        return "No exceptions here!";
    }

    // noexcept or noexcept(false)と宣言しない限りnoexceptでない
    std::string f_except2()  // エクセプションを発生させる
    {
        throw std::runtime_error{"always throw"};

        return "No exceptions here!";
    }
```
```cpp
    //  example/core_lang_spec/noexcept_ut.cpp 37

    static_assert(noexcept(f_noexcept()));  // エクセプションを発生させる可能性の確認
    static_assert(!noexcept(f_except()));   // エクセプションを発生させない可能性の確認
    static_assert(!noexcept(f_except2()));  // エクセプションを発生させない可能性の確認

    ASSERT_EQ(f_noexcept(), "No exceptions here!");  // 動作確認
    ASSERT_THROW(f_except(), std::runtime_error);    // エクセプションの発生確認
    ASSERT_THROW(f_except2(), std::runtime_error);   // エクセプションの発生確認
```

演算子としてのnoexceptはテンプレートで頻繁に使用されるため、以下にそのような例を示す。

```cpp
    //  example/core_lang_spec/noexcept_ut.cpp 50

    class PossiblyThrow {  // オブジェクト生成でエクセプションの発生可能性あり
    public:
        PossiblyThrow() {}
    };

    // テンプレート型Tがnoexceptで生成可能なら、関数もnoexceptにする
    template <typename T>
    void t_f(T const&) noexcept(std::is_nothrow_constructible_v<T>)
    {
        // Tを生成して、何らかの処理を行う
    }
```
```cpp
    //  example/core_lang_spec/noexcept_ut.cpp 67

    auto i = int{};
    auto p = PossiblyThrow{};

    static_assert(!std::is_nothrow_constructible_v<PossiblyThrow>);
    static_assert(std::is_nothrow_constructible_v<decltype(i)>);
    static_assert(noexcept(t_f(i)));
    static_assert(!noexcept(t_f(p)));
```

### exception-unfriendly <a id="SS_6_13_5"></a>
以下のような関数  

* 初期化に関連する関数やコンストラクタ
    * 静的または thread_local な変数を初期化する関数やコンストラクタ
* 特殊メンバ関数
    * すべてのデストラクタ
    * すべてのエクセプションオブジェクトのコピーコンストラクタ
    * すべてのムーブコンストラクタ
    * すべてのムーブ代入演算子
* 特定の名前を持つ関数
    * "swap" という名前のすべての関数
* C言語との互換性を持つ関数
    * Cとのリンケージを持つすべての関数

の呼び出しでエクセプションがthrowされると、[未定義動作](#SS_6_14_3)や[未規定動作](#SS_6_14_4)が発生するため、
exception-unfriendly(エクセプションに不向き)であるとされる。
従って上記の関数は暗黙的または明示的に`noexcept`であることが求められる。


## 言語仕様の定義要素 <a id="SS_6_14"></a>
### ill-formed <a id="SS_6_14_1"></a>
[標準規格と処理系](https://cpprefjp.github.io/implementation-compliance.html)に詳しい解説があるが、

* [well-formed](#SS_6_14_2)(適格)とはプログラムが全ての構文規則・診断対象の意味規則・
  単一定義規則を満たすことである。
* ill-formed(不適格)とはプログラムが適格でないことである。

プログラムがwell-formedになった場合、そのプログラムはコンパイルできる。
プログラムがill-formedになった場合、通常はコンパイルエラーになるが、
対象がテンプレートの場合、事情は少々異なり、[SFINAE](#SS_6_11_1)によりコンパイルできることもある。

### well-formed <a id="SS_6_14_2"></a>
「[ill-formed](#SS_6_14_1)」を参照せよ。

### 未定義動作 <a id="SS_6_14_3"></a>
未定義動作(Undefined Behavior)とは、
C++標準が特定の操作や状況に対して一切の制約を設けないケースである。
未定義動作が発生すると、プログラムの実行結果が予測できなくなり、
何が起こるかはコンパイラや環境によって異なる。
未定義動作を含むコードは、クラッシュやセキュリティの問題を引き起こす可能性がある。

```cpp
    //  example/core_lang_spec/undefined_ut.cpp 14

    int a = 42;
    int b = 0;
    int c = a / b;  // 未定義動作 - ゼロ除算

    int arr[]{1, 2, 3};
    int x = arr[index];  // 未定義動作 - index>2の場合、配列範囲外アクセス

```

### 未規定動作 <a id="SS_6_14_4"></a>
未規定動作(Unspecified Behavior)とは、C++標準がある操作の動作を完全には決めておらず、
複数の許容可能な選択肢がある場合でのコードの動作を指す。
未規定動作は、実装ごとに異なる可能性があり、標準は少なくとも「何らかの合理的な結果」を保証する。
つまり、動作が特定の範囲で予測可能だが、正確な挙動が処理系の実装に依存することになる。

```cpp
    //  example/core_lang_spec/undefined_ut.cpp 35

    enum class MyEnum : int { Value1 = 1, Value2 = 256 };
    int value = static_cast<int8_t>(MyEnum::Value2);  // 未規定 - 256はint8_tとして表現できない

    auto a      = int{5};
    auto lambda = [](auto a0, auto a1) { return a0 / a1; };
    auto result = lambda(a++, a++);  // 未規定 - 引数評価の順序が決まっていない
```

### 未定義動作と未規定動作 <a id="SS_6_14_5"></a>
| 種類            |定義                                                               | 例                               | 結果                           |
|-----------------|-------------------------------------------------------------------|----------------------------------|--------------------------------|
|[未定義動作](#SS_6_14_3)|C++標準が全く保証しない動作                                        | ゼロ除算、配列範囲外アクセス     | 予測不能(クラッシュなど)       |
|[未規定動作](#SS_6_14_4)|C++標準が動作を定めていないが、いくつかの選択肢が許容されている動作| `int8_t` に収まらない値のキャスト| 実装依存(異なるが合理的な動作) |


### 被修飾型 <a id="SS_6_14_6"></a>
被修飾型(unqualified type)とは、変数の宣言において付加される修飾子(const、
volatile など)やポインタやリファレンスなどの間接指定子を除いた素の型を指す。

修飾子(const、volatile)に注視しい場合、cv-被修飾型(cv-unqualified type)という場合もある。

例えば: 

|定義         |被修飾型|
|-------------|:------:|
|const A& a   |A       |
|volatile B& b|B       |
|const T* C   |C       |
|const D d    |D       |

見た目が類似する[修飾付き関数呼び出し](#SS_6_12_7)とは無関係である。

### 実引数/仮引数 <a id="SS_6_14_7"></a>
引数(もしくは実引数、argument)、仮引数(parameter)とは下記のように定義される。

```cpp
    //  example/core_lang_spec/argument.cpp 2

    int f0(int a, int& b) noexcept  // a, bは仮引数
    {
        // ...
    }

    void f1() noexcept
    {
        // ...

        f0(x, y);  // x, yは実引数
    }
```

### 単純代入 <a id="SS_6_14_8"></a>
代入は下記のように分類される。

* 単純代入(=)
* 複合代入(+=，++ 等)


### one-definition rule <a id="SS_6_14_9"></a>
「[ODR](#SS_6_14_10)」を参照せよ。

### ODR <a id="SS_6_14_10"></a>
ODRとは、One Definition Ruleの略語であり、下記のようなことを定めている。

* どの翻訳単位でも、テンプレート、型、関数、またはオブジェクトは、複数の定義を持つことができない。
* プログラム全体で、オブジェクトまたは非インライン関数は複数の定義を持つことはできない。
* 型、テンプレート、外部インライン関数等、いくつかのものは複数の翻訳単位で定義することができる。

より詳しい内容がが知りたい場合は、
[https://en.cppreference.com/w/cpp/language/definition](https://en.cppreference.com/w/cpp/language/definition)
が参考になる。

### 型特性キーワード <a id="SS_6_14_11"></a>
アライメントとは、
データが効率的にアクセスされるために特定のメモリアドレス境界に配置される規則である。
C++03までの規約では、アライメントのコントロールは実装依存した#pragmaなどで行っていた。

[alignas](#SS_6_14_11_2)、
[alignof](#SS_6_14_11_1)によりコンパイラの標準的な方法でアライメントのコントロールできるようになった。

#### alignof <a id="SS_6_14_11_1"></a>
C++11で導入されたキーワードで、型のアライメント要求を取得するために使用する。

```cpp
    //  example/core_lang_spec/aliging_ut.cpp 12

    struct alignas(16) AlignedStruct {  // メモリ上で16バイト境界にアライメントされる
        char   a;
        double x;
        double y;
    };

    AlignedStruct a;

    uintptr_t address = reinterpret_cast<uintptr_t>(&a);  // aのアドレスを取得

    ASSERT_EQ(address % 16, 0);             // アドレスが16の倍数であることを確認
    ASSERT_EQ(alignof(AlignedStruct), 16);  // アライメントが正しいか確認
```

#### alignas <a id="SS_6_14_11_2"></a>
C++11で導入されたキーワードで、メモリのアライメントを指定するために使用する。

```cpp
    //  example/core_lang_spec/aliging_ut.cpp 27

    ASSERT_EQ(alignof(long double), 16);  // アライメントが正しいか確認
    ASSERT_EQ(alignof(long long), 8);     // アライメントが正しいか確認
    ASSERT_EQ(alignof(void*), 8);         // アライメントが正しいか確認
    ASSERT_EQ(alignof(int), 4);           // アライメントが正しいか確認
```

#### addressof <a id="SS_6_14_11_3"></a>
addressofは、オブジェクトの「実際の」
アドレスを取得するために使用されるC++標準ライブラリのユーティリティ関数である。
通常、オブジェクトのアドレスを取得するには&演算子を使うが、
operator& がオーバーロードされている場合には、
&演算子ではオブジェクトのメモリ上の実際のアドレスを取得できない場合があり得る。
そのような場合にstd::addressofすることにより、
オーバーロードを無視して元のアドレスを確実に取得できる。

```cpp
    //  example/core_lang_spec/aliging_ut.cpp 38

    class X {
    public:
        explicit X(int v) : v_{v} {}

        X* operator&()
        {                    // `operator&` をオーバーロードしてアドレス取得の挙動を変更
            return nullptr;  // 意図的に nullptr を返す
        }
        operator int() const noexcept { return v_; }

    private:
        int v_;
    };
```
```cpp
    //  example/core_lang_spec/aliging_ut.cpp 54

    X obj{42};

    X* p0 = &obj;  // &演算子で取得するアドレス(オーバーロードされているためnullptr が返る)
    ASSERT_EQ(p0, nullptr);

    // std::addressofとほぼ同じ実装であるラムダ
    auto addressof = [](auto& arg) noexcept {
        return reinterpret_cast<std::remove_reference_t<decltype(arg)>*>(
            &const_cast<char&>(reinterpret_cast<const volatile char&>(arg)));
    };

    // ラムダaddressofを使用して強引にobjのアドレスを取得
    X* p1 = addressof(obj);
    ASSERT_NE(p1, nullptr);

    int* i_ptr = reinterpret_cast<int*>(p1);  // 処理系依存だが、通常の32/64bit環境なら通る
    ASSERT_EQ(42, *i_ptr);

    X* p2 = std::addressof(obj);
    ASSERT_EQ(p1, p2);
```

### 演算子のオペランドの評価順位 <a id="SS_6_14_12"></a>

C++17で、演算子のオペランドに対する評価順序が明確に規定された。
それに対し、C++14までは、演算子のオペランド部分式の評価順序は[未規定動作](#SS_6_14_4)であった。
以下の表で示す演算子に関しては、オペランドaがオペランドbよりも先に評価される。

| 演算子               |説明                                                                   |
|:---------------------|:----------------------------------------------------------------------|
| a.b                  |メンバアクセス演算子                                                   |
| a->b                 |ポインタメンバアクセス演算子                                           |
| a->\*b               |メンバポインタアクセス演算子                                           |
| a(b1,  b2, b3)       |関数呼び出し、引数リストの評価順序は規定外)                            |
| b @= a               |代入演算子 = や複合代入演算子。@は+,-,/,&,\|など                       |
| a[b]                 |配列アクセス                                                           |
| a << b               |ビットシフト左演算子                                                   |
| a >> b               |ビットシフト右演算子                                                   |

C++11以前では、以下のコードの評価順序は未規定であったが、上記の通り定義された。

```cpp
    //  example/core_lang_spec/etc_ut.cpp 74

    int i = 0;
    int y = (i = 1) * x + (i = 2);

    a(b1, b2, b3);  // b1, b2, b3の評価順序は規定外
```

関数呼び出しにおける引数の式の評価順序は、上記の例a(b1, b2, b3)での評価順序は、
不定順で序列化される。これは、b1, b2, b3 が特定の順序で評価される保証はなく、
例えば b3, b2, b1 の順に評価されたり、
b2, b3, b1 で評価される可能性があることを意味する。
一方で一度評価が開始された場合、部分式間でインターリーブ（交差実行されることはない。
つまり、b1 の評価が完全に終わる前に b2 や b3 の評価が開始されることはない。

条件演算子式`condition ? expr1 : expr2`については、
最初の部分であるconditionがまず評価される。
conditionの評価結果に基づき、expr1または expr2 のどちらかが選択され、選択された側だけが評価される。  

```cpp
    //  example/core_lang_spec/etc_ut.cpp 83

    int a      = 1;
    int b      = 2;
    int result = (a < b) ? func1() : func2();
```

なお、単項演算子のオペランドは1つであるため、優先順位の定義は不要である。

## その他 <a id="SS_6_15"></a>
### RVO(Return Value Optimization) <a id="SS_6_15_1"></a>
関数の戻り値がオブジェクトである場合、
戻り値オブジェクトは、その関数の呼び出し元のオブジェクトにcopyされた後、すぐに破棄される。
この「オブジェクトをcopyして、その後すぐにそのオブジェクトを破棄する」動作は、
「関数の戻り値オブジェクトをそのままその関数の呼び出し元で使用する」ことで効率的になる。
RVOとはこのような最適化を指す。

なお、このような最適化は、
[C++17から規格化](https://cpprefjp.github.io/lang/cpp17/guaranteed_copy_elision.html)された。


### トライグラフ <a id="SS_6_15_2"></a>
トライグラフとは、2つの疑問符とその後に続く1文字によって表される、下記の文字列である。

```
    ??=  ??/  ??'  ??(  ??)  ??!  ??<  ??>  ??-
```


<!-- essential/md/stdlib_and_concepts.md -->
# 標準ライブラリとプログラミングの概念 <a id="SS_7"></a>
この章では、C++標準ライブラリやそれによって導入されたプログラミングの概念等の紹介を行う。

___

__この章の構成__

&emsp;&emsp; [ユーティリティ](#SS_7_1)  
&emsp;&emsp;&emsp; [std::move](#SS_7_1_1)  
&emsp;&emsp;&emsp; [std::forward](#SS_7_1_2)  

&emsp;&emsp; [type_traits](#SS_7_2)  
&emsp;&emsp;&emsp; [std::integral_constant](#SS_7_2_1)  
&emsp;&emsp;&emsp; [std::true_type](#SS_7_2_2)  
&emsp;&emsp;&emsp; [std::false_type](#SS_7_2_3)  
&emsp;&emsp;&emsp; [std::is_same](#SS_7_2_4)  
&emsp;&emsp;&emsp; [std::enable_if](#SS_7_2_5)  
&emsp;&emsp;&emsp; [std::conditional](#SS_7_2_6)  
&emsp;&emsp;&emsp; [std::is_void](#SS_7_2_7)  
&emsp;&emsp;&emsp; [std::is_copy_assignable](#SS_7_2_8)  
&emsp;&emsp;&emsp; [std::is_move_assignable](#SS_7_2_9)  

&emsp;&emsp; [並列処理](#SS_7_3)  
&emsp;&emsp;&emsp; [std::thread](#SS_7_3_1)  
&emsp;&emsp;&emsp; [std::mutex](#SS_7_3_2)  
&emsp;&emsp;&emsp; [std::atomic](#SS_7_3_3)  
&emsp;&emsp;&emsp; [std::condition_variable](#SS_7_3_4)  

&emsp;&emsp; [ロック所有ラッパー](#SS_7_4)  
&emsp;&emsp;&emsp; [std::lock_guard](#SS_7_4_1)  
&emsp;&emsp;&emsp; [std::unique_lock](#SS_7_4_2)  
&emsp;&emsp;&emsp; [std::scoped_lock](#SS_7_4_3)  

&emsp;&emsp; [スマートポインタ](#SS_7_5)  
&emsp;&emsp;&emsp; [std::unique_ptr](#SS_7_5_1)  
&emsp;&emsp;&emsp;&emsp; [std::make_unique](#SS_7_5_1_1)  

&emsp;&emsp;&emsp; [std::shared_ptr](#SS_7_5_2)  
&emsp;&emsp;&emsp;&emsp; [std::make_shared](#SS_7_5_2_1)  
&emsp;&emsp;&emsp;&emsp; [std::enable_shared_from_this](#SS_7_5_2_2)  

&emsp;&emsp;&emsp; [std::weak_ptr](#SS_7_5_3)  
&emsp;&emsp;&emsp; [std::auto_ptr](#SS_7_5_4)  

&emsp;&emsp; [Polymorphic Memory Resource(pmr)](#SS_7_6)  
&emsp;&emsp;&emsp; [std::pmr::memory_resource](#SS_7_6_1)  
&emsp;&emsp;&emsp; [std::pmr::polymorphic_allocator](#SS_7_6_2)  
&emsp;&emsp;&emsp; [pool_resource](#SS_7_6_3)  

&emsp;&emsp; [コンテナ](#SS_7_7)  
&emsp;&emsp;&emsp; [シーケンスコンテナ(Sequence Containers)](#SS_7_7_1)  
&emsp;&emsp;&emsp;&emsp; [std::forward_list](#SS_7_7_1_1)  

&emsp;&emsp;&emsp; [連想コンテナ(Associative Containers)](#SS_7_7_2)  
&emsp;&emsp;&emsp; [無順序連想コンテナ(Unordered Associative Containers)](#SS_7_7_3)  
&emsp;&emsp;&emsp;&emsp; [std::unordered_set](#SS_7_7_3_1)  
&emsp;&emsp;&emsp;&emsp; [std::unordered_map](#SS_7_7_3_2)  
&emsp;&emsp;&emsp;&emsp; [std::type_index](#SS_7_7_3_3)  

&emsp;&emsp;&emsp; [コンテナアダプタ(Container Adapters)](#SS_7_7_4)  
&emsp;&emsp;&emsp; [特殊なコンテナ](#SS_7_7_5)  

&emsp;&emsp; [std::optional](#SS_7_8)  
&emsp;&emsp;&emsp; [戻り値の無効表現](#SS_7_8_1)  
&emsp;&emsp;&emsp; [オブジェクトの遅延初期化](#SS_7_8_2)  

&emsp;&emsp; [std::variant](#SS_7_9)  
&emsp;&emsp; [オブジェクトの比較](#SS_7_10)  
&emsp;&emsp;&emsp; [std::rel_ops](#SS_7_10_1)  
&emsp;&emsp;&emsp; [std::tuppleを使用した比較演算子の実装方法](#SS_7_10_2)  

&emsp;&emsp; [その他](#SS_7_11)  
&emsp;&emsp;&emsp; [SSO(Small String Optimization)](#SS_7_11_1)  
&emsp;&emsp;&emsp; [heap allocation elision](#SS_7_11_2)  
  
  

[インデックス](#SS_1_2)に戻る。  

___


## ユーティリティ <a id="SS_7_1"></a>
### std::move <a id="SS_7_1_1"></a>
std::moveは引数を[rvalueリファレンス](#SS_6_8_2)に変換する関数テンプレートである。

|引数                 |std::moveの動作                                    |
|---------------------|---------------------------------------------------|
|非const [lvalue](#SS_6_7_1_1)|引数を[rvalueリファレンス](#SS_6_8_2)にキャストする      |
|const [lvalue](#SS_6_7_1_1)  |引数をconst [rvalueリファレンス](#SS_6_8_2)にキャストする|

この表の動作仕様を下記ののコードで示す。

```cpp
    //  example/stdlib_and_concepts/utility_ut.cpp 10

    uint32_t f(std::string&) { return 0; }         // f-0
    uint32_t f(std::string&&) { return 1; }        // f-1
    uint32_t f(std::string const&) { return 2; }   // f-2
    uint32_t f(std::string const&&) { return 3; }  // f-3
```
```cpp
    //  example/stdlib_and_concepts/utility_ut.cpp 21

    std::string       str{};
    std::string const cstr{};

    ASSERT_EQ(0, f(str));               // strはlvalue → f(std::string&)
    ASSERT_EQ(1, f(std::string{}));     // 一時オブジェクトはrvalue → f(std::string&&)
    ASSERT_EQ(1, f(std::move(str)));    // std::moveでrvalueに変換 → f(std::string&&)
    ASSERT_EQ(2, f(cstr));              // cstrはconst lvalue → f(std::string const&)
    ASSERT_EQ(3, f(std::move(cstr)));   // std::moveでconst rvalueに変換 → f(std::string const&&)
```

std::moveは以下の２つの概念ときわめて密接に関連しており、

* [rvalueリファレンス](#SS_6_8_2)
* [moveセマンティクス](#SS_8_5_3)

これら3つが組み合わさることで、不要なコピーを避けた高効率なリソース管理が実現される。

### std::forward <a id="SS_7_1_2"></a>
std::forwardは、下記の２つの概念を実現するための関数テンプレートである。

* [forwardingリファレンス](#SS_6_8_3)
* [perfect forwarding](#SS_6_8_5)

std::forwardを適切に使用することで、引数の値カテゴリを保持したまま転送でき、
move可能なオブジェクトの不要なコピーを避けることができる。

## type_traits <a id="SS_7_2"></a>
type_traitsは、型に関する情報をコンパイル時に取得・変換するためのメタ関数群で、
型特性の判定や型操作を静的に行うために用いられる。

以下に代表的なものをいくつか説明する。

- [std::integral_constant](#SS_7_2_1)
- [std::true_type](#SS_7_2_2)/[std::false_type](#SS_7_2_3)
- [std::is_same](#SS_7_2_4)
- [std::enable_if](#SS_7_2_5)
- [std::conditional](#SS_7_2_6)
- [std::is_void](#SS_7_2_7)
- [std::is_copy_assignable](#SS_7_2_8)
- [std::is_move_assignable](#SS_7_2_9)

### std::integral_constant <a id="SS_7_2_1"></a>
std::integral_constantは「テンプレートパラメータとして与えられた型とその定数から新たな型を定義する」
クラステンプレートである。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 13

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


### std::true_type <a id="SS_7_2_2"></a>
`std::true_type`(と`std::false_type`)は真/偽を返す標準ライブラリの[メタ関数](#SS_6_11_2)群の戻り型となる型エイリアスであるため、
最も使われるテンプレートの一つである。

これらは、下記で確かめられる通り、後述する[std::integral_constant](#SS_7_2_1)を使い定義されている。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 32

    // std::is_same_vの2パラメータが同一であれば、std::is_same_v<> == true
    static_assert(std::is_same_v<std::integral_constant<bool, true>, std::true_type>);
    static_assert(std::is_same_v<std::integral_constant<bool, false>, std::false_type>);
```

それぞれの型が持つvalue定数は、下記のように定義されている。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 39

    static_assert(std::true_type::value, "must be true");
    static_assert(!std::false_type::value, "must be false");
```

これらが何の役に立つのか直ちに理解することは難しいが、
true/falseのメタ関数版と考えれば、追々理解できるだろう。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 48

    // 引数の型がintに変換できるかどうかを判定する関数
    // decltypeの中でのみ使用されるため、定義は不要
    constexpr std::true_type  IsCovertibleToInt(int);  // intに変換できる型はこちら
    constexpr std::false_type IsCovertibleToInt(...);  // それ以外はこちら
```

上記の単体テストは下記のようになる。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 59

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

### std::false_type <a id="SS_7_2_3"></a>
[std::true_type](#SS_7_2_2)を参照せよ。

### std::is_same <a id="SS_7_2_4"></a>

すでに上記の例でも使用したが、std::is_sameは2つのテンプレートパラメータが

* 同じ型である場合、std::true_type
* 違う型である場合、std::false_type

から派生した型となる。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 99

    static_assert(std::is_same<int, int>::value);
    static_assert(std::is_same<int, int32_t>::value);   // 64ビットg++/clang++
    static_assert(!std::is_same<int, int64_t>::value);  // 64ビットg++/clang++
    static_assert(std::is_same<std::string, std::basic_string<char>>::value);
    static_assert(std::is_same<typename std::vector<int>::reference, int&>::value);
```

また、 C++17で導入されたstd::is_same_vは、定数テンプレートを使用し、
下記のように定義されている。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 90

    template <typename T, typename U>
    constexpr bool is_same_v{std::is_same<T, U>::value};
```

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 108

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
    //  example/stdlib_and_concepts/type_traits_ut.cpp 117

    static_assert(std::is_base_of_v<std::true_type, std::is_same<int, int>>);
    static_assert(std::is_base_of_v<std::false_type, std::is_same<int, char>>);
```

### std::enable_if <a id="SS_7_2_5"></a>
std::enable_ifは、bool値である第1テンプレートパラメータが

* trueである場合、型である第2テンプレートパラメータをメンバ型typeとして宣言する。
* falseである場合、メンバ型typeを持たない。

下記のコードはクラステンプレートの特殊化を用いたstd::enable_ifの実装例である。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 124

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
    //  example/stdlib_and_concepts/type_traits_ut.cpp 148

    static_assert(std::is_same_v<void, std::enable_if_t<true>>);
    static_assert(std::is_same_v<int, std::enable_if_t<true, int>>);
```

実装例から明らかなように

* std::enable_if\<true>::typeは[well-formed](#SS_6_14_2)
* std::enable_if\<false>::typeは[ill-formed](#SS_6_14_1)

となるため、下記のコードはコンパイルできない。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 155

    // 下記はill-formedとなるため、コンパイルできない。
    static_assert(std::is_same_v<void, std::enable_if_t<false>>);
    static_assert(std::is_same_v<int, std::enable_if_t<false, int>>);
```

std::enable_ifのこの特性と後述する[SFINAE](#SS_6_11_1)により、
様々な静的ディスパッチを行うことができる。


### std::conditional <a id="SS_7_2_6"></a>

std::conditionalは、bool値である第1テンプレートパラメータが

* trueである場合、第2テンプレートパラメータ
* falseである場合、第3テンプレートパラメータ

をメンバ型typeとして宣言する。

下記のコードはクラステンプレートの特殊化を用いたstd::conditionalの実装例である。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 164

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
    //  example/stdlib_and_concepts/type_traits_ut.cpp 189

    static_assert(std::is_same_v<int, std::conditional_t<true, int, char>>);
    static_assert(std::is_same_v<char, std::conditional_t<false, int, char>>);
```

### std::is_void <a id="SS_7_2_7"></a>
std::is_voidはテンプレートパラメータの型が

* voidである場合、std::true_type
* voidでない場合、std::false_type

から派生した型となる。

以下に簡単な使用例を示す。

```cpp
    //  example/stdlib_and_concepts/type_traits_ut.cpp 82

    static_assert(std::is_void<void>::value);
    static_assert(!std::is_void<int>::value);
    static_assert(!std::is_void<std::string>::value);
```

### std::is_copy_assignable <a id="SS_7_2_8"></a>
std::is_copy_assignableはテンプレートパラメータの型(T)がcopy代入可能かを調べる。
Tが[CopyAssignable要件](#SS_8_5_5)を満たすためには`std::is_copy_assignable<T>`がtrueでなければならないが、
その逆が成立するとは限らない。


### std::is_move_assignable <a id="SS_7_2_9"></a>
std::is_move_assignableはテンプレートパラメータの型(T)がmove代入可能かを調べる。
Tが[MoveAssignable要件](#SS_8_5_4)を満たすためには`std::is_move_assignable<T>`がtrueでなければならないが、
その逆が成立するとは限らない。


## 並列処理 <a id="SS_7_3"></a>

### std::thread <a id="SS_7_3_1"></a>
クラスthread は、新しい実行のスレッドの作成/待機/その他を行う機構を提供する。

```cpp
    //  example/stdlib_and_concepts/thread_ut.cpp 9

    struct Conflict {
        void     increment() { ++count_; }  // 非アトミック（データレースの原因）
        uint32_t count_ = 0;
    };
```
```cpp
    //  example/stdlib_and_concepts/thread_ut.cpp 19

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

### std::mutex <a id="SS_7_3_2"></a>
mutex は、スレッド間で使用する共有リソースを排他制御するためのクラスである。 

| メンバ関数 | 動作説明                                                                                    |
|:-----------|---------------------------------------------------------------------------------------------|
| lock()     | lock()が即時リターンするスレッドはただ一つ。そうでない場合、unlock()が呼ばれるまでブロック  |
| unlock()   | lock()でブロックされていたスレッドの中から一つが動き出す                                    |


以下のコード例では、メンバ変数のインクリメントがスレッド間の競合を引き起こす(こういったコード領域を
[クリティカルセクション](#SS_8_12_4)と呼ぶ)が、std::mutexによりこの問題を回避している。

```cpp
    //  example/stdlib_and_concepts/thread_ut.cpp 48

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
    //  example/stdlib_and_concepts/thread_ut.cpp 66

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
mutexは通常、[std::lock_guard](#SS_7_4_1)と組み合わせて使われる。

### std::atomic <a id="SS_7_3_3"></a>
atomicクラステンプレートは、型Tをアトミック操作するためのものである。
[組み込み型](#SS_6_1_2)に対する特殊化が提供されており、それぞれに特化した演算が用意されている。
[std::mutex](#SS_7_3_2)で示したような単純なコードではstd::atomicを使用して下記のように書く方が一般的である。

```cpp
    //  example/stdlib_and_concepts/thread_ut.cpp 92

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
    //  example/stdlib_and_concepts/thread_ut.cpp 107

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

### std::condition_variable <a id="SS_7_3_4"></a>
condition_variable は、特定のイベントが発生するまでスレッドの待ち合わせを行うためのクラスである。
最も単純な使用例を以下に示す(「[Spurious Wakeup](#SS_8_12_11)」参照)。
```cpp
    //  example/stdlib_and_concepts/thread_ut.cpp 135

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
    //  example/stdlib_and_concepts/thread_ut.cpp 162

    std::thread t1{[]() { wait(); /* 通知待ち */ }};
    std::thread t2{[]() { wait(); /* 通知待ち */ }};

    notify();  // 通知待ちのスレッドに通知

    t1.join();
    t2.join();
```

## ロック所有ラッパー <a id="SS_7_4"></a>
ロック所有ラッパーとはミューテックスのロックおよびアンロックを管理するための以下のクラスを指す。

- [std::lock_guard](#SS_7_4_1)
- [std::unique_lock](#SS_7_4_2)
- [std::scoped_lock](#SS_7_4_3)


### std::lock_guard <a id="SS_7_4_1"></a>
std::lock_guardを使わない問題のあるコードを以下に示す。

```cpp
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 14

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
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 63

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
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 19
    {
        mtx_.lock();  // ++count_の排他のためのロック

        ++count_;

        mtx_.unlock();  // 上記のアンロック
    }
```

オリジナルのコードで指摘したすべてのリスクが、わずか一行の変更で解決されている。

```cpp
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 68
    {
        std::lock_guard<std::mutex> lock{mtx_};  // lockオブジェクトのコンストラクタでmtx_.lock()が呼ばれる
                                                 // ++count_の排他
        ++count_;

    }  // lockオブジェクトのデストラクタでmtx_.unlock()が呼ばれる
```

### std::unique_lock <a id="SS_7_4_2"></a>
std::unique_lockとは、ミューテックスのロック管理を柔軟に行えるロックオブジェクトである。
std::lock_guardと異なり、ロックの手動解放や再取得が可能であり、特にcondition_variable::wait()と組み合わせて使用される。
wait()は内部でロックを一時的に解放し、通知受信後に再取得する。

下記の例では、IntQueue::push()、 IntQueue::pop_ng()、
IntQueue::pop_ok()の中で行われるIntQueue::q_へのアクセスで発生する競合を回避するためにIntQueue::mtx_を使用する。

下記のコード例では、[std::lock_guard](#SS_7_4_1)の説明で述べたようにmutex::lock()、mutex::unlock()を直接呼び出すのではなく、
std::unique_lockやstd::lock_guardによりmutexを使用する。

```cpp
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 112

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
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 168

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

一般に条件変数には、[Spurious Wakeup](#SS_8_12_11)という問題があり、std::condition_variableも同様である。

上記の抜粋である下記のコード例では[Spurious Wakeup](#SS_8_12_11)の対策が行われていないため、
意図通り動作しない可能性がある。

```cpp
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 127

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
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 141

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

### std::scoped_lock <a id="SS_7_4_3"></a>
std::scoped_lockとは、複数のミューテックスを同時にロックするためのロックオブジェクトである。
C++17で導入され、デッドロックを回避しながら複数のミューテックスを安全にロックできる。

複数のミューテックスを扱う際、異なるスレッドが異なる順序でロックを取得しようとすると、
デッドロックが発生する可能性がある。下記の例では、2つの銀行口座間で送金を行う際に、
両方の口座を同時にロックする必要がある。

```cpp
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 205

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
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 254

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

```essential/plant_uml/mutex_deadlock.pu
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
    //  example/stdlib_and_concepts/lock_ownership_wrapper_ut.cpp 225

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

## スマートポインタ <a id="SS_7_5"></a>
スマートポインタは、C++標準ライブラリが提供するメモリ管理クラス群を指す。
生のポインタの代わりに使用され、リソース管理を容易にし、
メモリリークや二重解放といった問題を防ぐことを目的としている。

スマートポインタは通常、所有権とスコープに基づいてメモリの解放を自動的に行う。
C++標準ライブラリでは、主に以下の3種類のスマートポインタが提供されている。

* [std::unique_ptr](#SS_7_5_1)
    - [std::make_unique](#SS_7_5_1_1)
* [std::shared_ptr](#SS_7_5_2)
    - [std::make_shared](#SS_7_5_2_1)
    - [std::enable_shared_from_this](#SS_7_5_2_2)
    - [std::weak_ptr](#SS_7_5_3)
* [std::auto_ptr](#SS_7_5_4)

### std::unique_ptr <a id="SS_7_5_1"></a>
std::unique_ptrは、C++11で導入されたスマートポインタの一種であり、std::shared_ptrとは異なり、
[オブジェクトの排他所有](#SS_8_4_1)を表すために用いられる。所有権は一つのunique_ptrインスタンスに限定され、
他のポインタと共有することはできない。ムーブ操作によってのみ所有権を移譲でき、
スコープを抜けると自動的にリソースが解放されるため、メモリ管理の安全性と効率性が向上する。

#### std::make_unique <a id="SS_7_5_1_1"></a>
[std::make_unique\<T\>(Args...)](https://cpprefjp.github.io/reference/memory/make_unique.html)は、
クラスTをダイナミックに生成し、そのポインタを保持するshared_ptrオブジェクトを生成する。

使用例については、「[オブジェクトの排他所有](#SS_8_4_1)」を参照せよ。

### std::shared_ptr <a id="SS_7_5_2"></a>
std::shared_ptrは、同じくC++11で導入されたスマートポインタであり、[オブジェクトの共有所有](#SS_8_4_2)を表すために用いられる。
複数のshared_ptrインスタンスが同じリソースを参照でき、
内部の参照カウントによって最後の所有者が破棄された時点でリソースが解放される。
[std::weak_ptr](#SS_7_5_3)は、shared_ptrと連携して使用されるスマートポインタであり、オブジェクトの非所有参照を表す。
参照カウントには影響せず、循環参照を防ぐために用いられる。weak_ptrから一時的にshared_ptrを取得するにはlock()を使用する。

#### std::make_shared <a id="SS_7_5_2_1"></a>
[std::make_shared\<T\>(Args...)](https://cpprefjp.github.io/reference/memory/make_shared.html)は、
クラスTをダイナミックに生成し、そのポインタを保持するshared_ptrオブジェクトを生成する。

使用例については、「[オブジェクトの共有所有](#SS_8_4_2)」を参照せよ。

#### std::enable_shared_from_this <a id="SS_7_5_2_2"></a>
`std::enable_shared_from_this`は、`shared_ptr`で管理されているオブジェクトが、
自分自身への`shared_ptr`を安全に取得するための仕組みである。

この`std::enable_shared_from_this`が存在しない場合に発生するであろう問題のあるコードを以下に示す。

```cpp
    //  example/stdlib_and_concepts/enable_shared_from_this_ut.cpp 7

    class A {
    public:
        void register_self(std::vector<std::shared_ptr<A>>& vec) { vec.push_back(std::shared_ptr<A>{this}); }
    };
```
```cpp
    //  example/stdlib_and_concepts/enable_shared_from_this_ut.cpp 17

    auto sp1 = std::make_shared<A>();  // Aのポインタを管理するshared_ptr(sp1)が作られる
                                       // sp1が管理するポインタを便宜上、sp1_pointerと呼ぶことにする

    std::vector<std::shared_ptr<A>> vec;

    sp1->register_self(vec);  // vecに登録されるのはsp1_pointerを管理するshared_ptrであるが、
                              // vecに保持された「sp1_pointerを管理するshared_ptr」は、
                              // sp1と個別に生成されたため、sp1とuseカウンタを共有しない

    // ここまで来ると、
    // * sp1がスコープアウトするため、sp1がsp1_pointerを解放する。
    // * vecがスコープアウトするため、vecが保持するshared_ptrが、sp1_pointerを解放する。

    // 以上によりsp1_pointer二重解放されるため、未定義動作につながる
```

std::enable_shared_from_thisを継承し、`shared_from_this()`メソッドを使用し、この問題を解決したコード例を以下に示す。

std::enable_shared_from_thisは、内部にweak_ptrメンバを持っている。shared_ptrでオブジェクトが初めて管理される際、
shared_ptrのコンストラクタがenable_shared_from_thisの存在を検出し、内部のweak_ptrに制御ブロックへの参照を設定する。

`shared_from_this()`メソッドはこの内部のweak_ptrをlock()することで、
元のshared_ptrと制御ブロックを共有する新しいshared_ptrを生成する。
これにより、同一オブジェクトへの複数のshared_ptrが正しく参照カウントを共有できる。

```cpp
    //  example/stdlib_and_concepts/enable_shared_from_this_ut.cpp 38

    class A : public std::enable_shared_from_this<A> {
    public:
        void register_self(std::vector<std::shared_ptr<A>>& vec) { vec.push_back(shared_from_this()); }
    };
```
```cpp
    //  example/stdlib_and_concepts/enable_shared_from_this_ut.cpp 48

    auto sp1 = std::make_shared<A>();  // Aのポインタを管理するstd::shread_ptr(sp1)が作られる
                                       // sp1が管理するポインタを便宜上、sp1_pointerと呼ぶことにする

    std::vector<std::shared_ptr<A>> vec;

    sp1->register_self(vec);  // shared_from_this()により、
                              // sp1と同じuseカウンタを共有する新しいshared_ptrが生成されvecに格納される。

    // スコープアウト時には参照カウントが正しく管理されているため、
    // 最後のshared_ptrが破棄されるまでオブジェクトは解放されない
```

**[使用上の注意点]**

1. コンストラクタ内での使用禁止  
   コンストラクタ内でshared_from_this()を呼び出してはならない。なぜなら、コンストラクタ実行時点ではまだshared_ptrによる管理が完了しておらず、内部のweak_ptrが初期化されていないためである。この場合、std::bad_weak_ptr例外がスローされる。
2. shared_ptrでの管理が必須  
   オブジェクトがshared_ptrで管理されていない状態(例えばスタック上のオブジェクトや生のnew)でshared_from_this()を呼び出すと、std::bad_weak_ptr例外がスローされるか、未定義動作となる。
3. make_sharedの使用推奨  
   std::enable_shared_from_thisを継承したクラスのインスタンスは、必ずstd::make_sharedまたはshared_ptrのコンストラクタで生成する必要がある。

C++17以降では、`weak_from_this()`メソッドも提供されている。これはshared_from_this()と同様の仕組みだが、
weak_ptrを返すため[オブジェクトの循環所有](#SS_8_4_3)を避けたい場合に有用である。

### std::weak_ptr <a id="SS_7_5_3"></a>
std::weak_ptrは、スマートポインタの一種である。

std::weak_ptrは参照カウントに影響を与えず、[std::shared_ptr](#SS_7_5_2)とオブジェクトを共有所有するのではなく、
その`shared_ptr`インスタンスとの関連のみを保持するのため、[オブジェクトの循環所有](#SS_8_4_3)の問題を解決できる。

[オブジェクトの循環所有](#SS_8_4_3)で示した問題のあるクラスの修正版を以下に示す
(以下の例では、Xは前のままで、Yのみ修正した)。

```cpp
    //  example/stdlib_and_concepts/weak_ptr_ut.cpp 9

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

なお、上記コードは[初期化付きif文](#SS_6_9_5_3)を使うことで、
生成した`std::shared_ptr<X>`オブジェクトのスコープを最小に留めている。

```cpp
    //  example/stdlib_and_concepts/weak_ptr_ut.cpp 63
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
    //  example/stdlib_and_concepts/weak_ptr_ut.cpp 82

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

### std::auto_ptr <a id="SS_7_5_4"></a>
`std::auto_ptr`はC++11以前に導入された初期のスマートポインタであるが、異常な[copyセマンティクス](#SS_8_5_2)を持つため、
多くの誤用を生み出し、C++11から非推奨とされ、C++17から規格から排除された。


## Polymorphic Memory Resource(pmr) <a id="SS_7_6"></a>
Polymorphic Memory Resource(pmr)は、
動的メモリ管理の柔軟性と効率性を向上させるための、C++17から導入された仕組みである。

[std::pmr::polymorphic_allocator](#SS_7_6_2)はC++17で導入された標準ライブラリのクラスで、
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

* [std::pmr::memory_resource](#SS_7_6_1)  
* [std::pmr::polymorphic_allocator](#SS_7_6_2)  
* [pool_resource](#SS_7_6_3)

### std::pmr::memory_resource <a id="SS_7_6_1"></a>
std::pmr::memory_resourceは、
ユーザー定義のメモリリソースをカスタマイズし、
[std::pmr::polymorphic_allocator](#SS_7_6_2)を通じて利用可能にする[インターフェースクラス](#SS_6_4_11)である。

std::pmr::memory_resourceから派生した具象クラスの実装を以下に示す。

```cpp
    //  example/stdlib_and_concepts/pmr_memory_resource_ut.cpp 64

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

### std::pmr::polymorphic_allocator <a id="SS_7_6_2"></a>
std::pmr::polymorphic_allocatorはC++17で導入された標準ライブラリのクラスで、
C++のメモリリソース管理を抽象化するための機能を提供する。
[std::pmr::memory_resource](#SS_7_6_1)を基盤とし、
コンテナやアルゴリズムにカスタムメモリアロケーション戦略を容易に適用可能にする。
std::allocatorと異なり、型に依存せず、
ポリモーフィズムを活用してメモリリソースを切り替えられる点が特徴である。

すでに示したmemory_resource_variable([std::pmr::memory_resource](#SS_7_6_1))の単体テストを以下に示すことにより、
polymorphic_allocatorの使用例とする。

```cpp
    //  example/stdlib_and_concepts/pmr_memory_resource_ut.cpp 208

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

### pool_resource <a id="SS_7_6_3"></a>
pool_resourceは[std::pmr::memory_resource](#SS_7_6_1)を基底とする下記の2つの具象クラスである。

* std::pmr::synchronized_pool_resourceは下記のような特徴を持つメモリプールである。
    * 非同期のメモリプールリソース
    * シングルスレッド環境での高速なメモリ割り当てに適する
    * 排他制御のオーバーヘッドがない
    * 以下に使用例を示す。

```cpp
    //  example/stdlib_and_concepts/pool_resource_ut.cpp 10

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
    //  example/stdlib_and_concepts/pool_resource_ut.cpp 38

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


## コンテナ <a id="SS_7_7"></a>
データを格納し、
効率的に操作するための汎用的なデータ構造を提供するC++標準ライブラリの下記のようなクラス群である。

* [シーケンスコンテナ(Sequence Containers)](#SS_7_7_1)
* [連想コンテナ(Associative Containers)(---)
* [無順序連想コンテナ(Unordered Associative Containers)](#SS_7_7_3)
* [コンテナアダプタ(Container Adapters)](#SS_7_7_4)
* [特殊なコンテナ](#SS_7_7_5)

### シーケンスコンテナ(Sequence Containers) <a id="SS_7_7_1"></a>
データが挿入順に保持され、順序が重要な場合に使用する。

| コンテナ                 | 説明                                                                |
|--------------------------|---------------------------------------------------------------------|
| `std::vector`            | 動的な配列で、ランダムアクセスが高速。末尾への挿入/削除が効率的     |
| `std::deque`             | 両端に効率的な挿入/削除が可能な動的配列                             |
| `std::list`              | 双方向リスト。要素の順序を維持し、中間の挿入/削除が効率的           |
| [std::forward_list](#SS_7_7_1_1) | 単方向リスト。軽量だが、双方向の操作はできない                      |
| `std::array`             | 固定長配列で、サイズがコンパイル時に決まる                          |
| `std::string`            | 可変長の文字列を管理するクラス(厳密には`std::basic_string`の特殊化) |

#### std::forward_list <a id="SS_7_7_1_1"></a>

```cpp
    //  example/stdlib_and_concepts/container_ut.cpp 14

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

### 連想コンテナ(Associative Containers) <a id="SS_7_7_2"></a>
データがキーに基づいて自動的にソートされ、検索が高速である。

| コンテナ           | 説明                                             |
|--------------------|--------------------------------------------------|
| `std::set`         | 要素がソートされ、重複が許されない集合           |
| `std::multiset`    | ソートされるが、重複が許される集合               |
| `std::map`         | ソートされたキーと値のペアを保持。キーは一意     |
| `std::multimap`    | ソートされたキーと値のペアを保持。キーは重複可能 |

### 無順序連想コンテナ(Unordered Associative Containers) <a id="SS_7_7_3"></a>
ハッシュテーブルを基盤としたコンテナで、順序を保証しないが高速な検索を提供する。

| コンテナ                  | 説明                                                   |
|---------------------------|--------------------------------------------------------|
| [std::unordered_set](#SS_7_7_3_1) | ハッシュテーブルベースの集合。重複は許されない         |
| `std::unordered_multiset` | ハッシュテーブルベースの集合。重複が許される           |
| [std::unordered_map](#SS_7_7_3_2) | ハッシュテーブルベースのキーと値のペア。キーは一意     |
| `std::unordered_multimap` | ハッシュテーブルベースのキーと値のペア。キーは重複可能 |
| [std::type_index](#SS_7_7_3_3)    | 型情報型を連想コンテナのキーとして使用するためのクラス |

#### std::unordered_set <a id="SS_7_7_3_1"></a>

```cpp
    //  example/stdlib_and_concepts/container_ut.cpp 32

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

#### std::unordered_map <a id="SS_7_7_3_2"></a>

```cpp
    //  example/stdlib_and_concepts/container_ut.cpp 52

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

#### std::type_index <a id="SS_7_7_3_3"></a>
std::type_indexはコンテナではないが、
型情報型を連想コンテナのキーとして使用するためのクラスであるため、この場所に掲載する。

```cpp
    //  example/stdlib_and_concepts/container_ut.cpp 74

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


### コンテナアダプタ(Container Adapters) <a id="SS_7_7_4"></a>
特定の操作のみを公開するためのラッパーコンテナ。

| コンテナ              | 説明                                     |
|-----------------------|------------------------------------------|
| `std::stack`          | LIFO(後入れ先出し)操作を提供するアダプタ |
| `std::queue`          | FIFO(先入れ先出し)操作を提供するアダプタ |
| `std::priority_queue` | 優先度に基づく操作を提供するアダプタ     |

### 特殊なコンテナ <a id="SS_7_7_5"></a>
上記したようなコンテナとは一線を画すが、特定の用途や目的のために設計された一種のコンテナ。

| コンテナ             | 説明                                                       |
|----------------------|------------------------------------------------------------|
| `std::span`          | 生ポインタや配列を抽象化し、安全に操作するための軽量ビュー |
| `std::bitset`        | 固定長のビット集合を管理するクラス                         |
| `std::basic_string`  | カスタム文字型をサポートする文字列コンテナ                 |

## std::optional <a id="SS_7_8"></a>
C++17から導入されたstd::optionalには、以下のような2つの用途がある。
以下の用途2から、
このクラスがオブジェクトのダイナミックなメモリアロケーションを行うような印象を受けるが、
そのようなことは行わない。
このクラスがオブジェクトのダイナミックな生成が必要になった場合、プレースメントnewを実行する。
ただし、std::optionalが保持する型自身がnewを実行する場合は、この限りではない。

1. 関数の任意の型の[戻り値の無効表現](#SS_7_8_1)を持たせる
2. [オブジェクトの遅延初期化](#SS_7_8_2)する(初期化処理が重く、
   条件によってはそれが無駄になる場合にこの機能を使う)

### 戻り値の無効表現 <a id="SS_7_8_1"></a>
```cpp
    //  example/stdlib_and_concepts/optional_ut.cpp 11

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
    //  example/stdlib_and_concepts/optional_ut.cpp 28

    auto ret0 = file_extension("xxx.yyy");

    ASSERT_TRUE(ret0);  // 値を保持している
    ASSERT_EQ("yyy", *ret0);

    auto ret1 = file_extension("xxx");

    ASSERT_FALSE(ret1);  // 値を保持していない
    // ASSERT_THROW(*ret1, std::exception);  // 未定義動作(エクセプションは発生しない)
    ASSERT_THROW(ret1.value(), std::bad_optional_access);  // 値非保持の場合、エクセプション発生
```

### オブジェクトの遅延初期化 <a id="SS_7_8_2"></a>
```cpp
    //  example/stdlib_and_concepts/optional_ut.cpp 43

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
    //  example/stdlib_and_concepts/optional_ut.cpp 64

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

## std::variant <a id="SS_7_9"></a>
std::variantは、C++17で導入された型安全なunionである。
このクラスは複数の型のうち1つの値を保持することができ、
従来のunionに伴う低レベルな操作の安全性の問題を解消するために設計された。

std::variant自身では、オブジェクトのダイナミックな生成が必要な場合でも通常のnewを実行せず、
代わりにプレースメントnewを用いる
(以下のコード例のようにstd::variantが保持する型自身がnewを実行する場合は、この限りではない)。

以下にstd::variantの典型的な使用例を示す。

```cpp
    //  example/stdlib_and_concepts/variant_ut.cpp 13

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

std::variantとstd::visit([Visitor](#SS_3_2_5)パターンの実装の一種)を組み合わせた場合の使用例を以下に示す。

```cpp
    //  example/stdlib_and_concepts/variant_ut.cpp 37

    void output_from_variant(std::variant<int, double, std::string> const& var, std::ostringstream& oss)
    {
        std::visit([&oss](auto&& arg) { oss.str().empty() ? oss << arg : oss << "|" << arg; }, var);
    }
```
```cpp
    //  example/stdlib_and_concepts/variant_ut.cpp 47

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

## オブジェクトの比較 <a id="SS_7_10"></a>
### std::rel_ops <a id="SS_7_10_1"></a>
クラスに`operator==`と`operator<`の2つの演算子が定義されていれば、
それがメンバか否かにかかわらず、他の比較演算子 !=、<=、>、>= はこれらを基に自動的に導出できる。
std::rel_opsでは`operator==`と`operator<=` を基に他の比較演算子を機械的に生成する仕組みが提供されている。

次の例では、std::rel_opsを利用して、少ないコードで全ての比較演算子をサポートする例を示す。

```cpp
    //  example/stdlib_and_concepts/comparison_stdlib_ut.cpp 12

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
    //  example/stdlib_and_concepts/comparison_stdlib_ut.cpp 32

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

なお、std::rel_opsはC++20から導入された[<=>演算子](#SS_6_6_4_1)により不要になったため、
非推奨とされた。

### std::tuppleを使用した比較演算子の実装方法 <a id="SS_7_10_2"></a>
クラスのメンバが多い場合、[==演算子](#SS_6_6_3)で示したような方法は、
可読性、保守性の問題が発生する場合が多い。下記に示す方法はこの問題を幾分緩和する。

```cpp
    //  example/stdlib_and_concepts/comparison_stdlib_ut.cpp 56

    struct Point {
        int x;
        int y;

        bool operator==(const Point& other) const noexcept { return std::tie(x, y) == std::tie(other.x, other.y); }

        bool operator<(const Point& other) const noexcept { return std::tie(x, y) < std::tie(other.x, other.y); }
    };
```
```cpp
    //  example/stdlib_and_concepts/comparison_stdlib_ut.cpp 70

    auto a = Point{1, 2};
    auto b = Point{1, 3};
    auto c = Point{1, 2};

    using namespace std::rel_ops;  // std::rel_opsを使うために名前空間を追加

    ASSERT_TRUE(a == c);
    ASSERT_TRUE(a != b);
    ASSERT_TRUE(a < b);
    ASSERT_FALSE(a > b);
```

## その他 <a id="SS_7_11"></a>
### SSO(Small String Optimization) <a id="SS_7_11_1"></a>
一般にstd::stringで文字列を保持する場合、newしたメモリが使用される。
64ビット環境であれば、newしたメモリのアドレスを保持する領域は8バイトになる。
std::stringで保持する文字列が終端の'\0'も含め8バイト以下である場合、
アドレスを保持する領域をその文字列の格納に使用すれば、newする必要がない(当然deleteも不要)。
こうすることで、短い文字列を保持するstd::stringオブジェクトは効率的に動作できる。

SOOとはこのような最適化を指す。

### heap allocation elision <a id="SS_7_11_2"></a>
C++11までの仕様では、new式によるダイナミックメモリアロケーションはコードに書かれた通りに、
実行されなければならず、ひとまとめにしたり省略したりすることはできなかった。
つまり、ヒープ割り当てに対する最適化は認められなかった。
ダイナミックメモリアロケーションの最適化のため、この制限は緩和され、
new/deleteの呼び出しをまとめたり省略したりすることができるようになった。

```cpp
    //  example/stdlib_and_concepts/heap_allocation_elision_ut.cpp 4

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



<!-- essential/md/cpp_idioms.md -->
# C++慣用語句 <a id="SS_8"></a>
この章では、C++慣用言句ついて解説を行う。

___

__この章の構成__

&emsp;&emsp; [イディオム](#SS_8_1)  
&emsp;&emsp;&emsp; [ガード節(Early Return)](#SS_8_1_1)  
&emsp;&emsp;&emsp; [RAII(scoped guard)](#SS_8_1_2)  
&emsp;&emsp;&emsp; [Copy-And-Swap](#SS_8_1_3)  
&emsp;&emsp;&emsp; [CRTP(curiously recurring template pattern)](#SS_8_1_4)  
&emsp;&emsp;&emsp; [Accessor](#SS_8_1_5)  
&emsp;&emsp;&emsp; [Immutable](#SS_8_1_6)  
&emsp;&emsp;&emsp; [NVI(non virtual interface)](#SS_8_1_7)  

&emsp;&emsp; [実装パターン](#SS_8_2)  
&emsp;&emsp;&emsp; [Pimpl](#SS_8_2_1)  
&emsp;&emsp;&emsp; [lightweight Pimpl](#SS_8_2_2)  
&emsp;&emsp;&emsp; [BitmaskType](#SS_8_2_3)  
&emsp;&emsp;&emsp; [Future](#SS_8_2_4)  
&emsp;&emsp;&emsp; [Null Object](#SS_8_2_5)  
&emsp;&emsp;&emsp; [Cでのクラス表現](#SS_8_2_6)  

&emsp;&emsp; [オブジェクト指向](#SS_8_3)  
&emsp;&emsp;&emsp; [is-a](#SS_8_3_1)  
&emsp;&emsp;&emsp; [has-a](#SS_8_3_2)  
&emsp;&emsp;&emsp; [is-implemented-in-terms-of](#SS_8_3_3)  
&emsp;&emsp;&emsp;&emsp; [public継承によるis-implemented-in-terms-of](#SS_8_3_3_1)  
&emsp;&emsp;&emsp;&emsp; [private継承によるis-implemented-in-terms-of](#SS_8_3_3_2)  
&emsp;&emsp;&emsp;&emsp; [コンポジションによる(has-a)is-implemented-in-terms-of](#SS_8_3_3_3)  

&emsp;&emsp; [オブジェクトの所有権](#SS_8_4)  
&emsp;&emsp;&emsp; [オブジェクトの排他所有](#SS_8_4_1)  
&emsp;&emsp;&emsp; [オブジェクトの共有所有](#SS_8_4_2)  
&emsp;&emsp;&emsp; [オブジェクトの循環所有](#SS_8_4_3)  

&emsp;&emsp; [copy/moveと等価性のセマンティクス](#SS_8_5)  
&emsp;&emsp;&emsp; [等価性のセマンティクス](#SS_8_5_1)  
&emsp;&emsp;&emsp; [copyセマンティクス](#SS_8_5_2)  
&emsp;&emsp;&emsp; [moveセマンティクス](#SS_8_5_3)  
&emsp;&emsp;&emsp; [MoveAssignable要件](#SS_8_5_4)  
&emsp;&emsp;&emsp; [CopyAssignable要件](#SS_8_5_5)  

&emsp;&emsp; [関数設計のガイドライン](#SS_8_6)  
&emsp;&emsp;&emsp; [関数の引数と戻り値の型](#SS_8_6_1)  
&emsp;&emsp;&emsp; [サイクロマティック複雑度のクライテリア](#SS_8_6_2)  
&emsp;&emsp;&emsp; [関数の行数のクライテリア](#SS_8_6_3)  

&emsp;&emsp; [クラス設計のガイドライン](#SS_8_7)  
&emsp;&emsp;&emsp; [ゼロの原則(Rule of Zero)](#SS_8_7_1)  
&emsp;&emsp;&emsp; [五の原則(Rule of Five)](#SS_8_7_2)  
&emsp;&emsp;&emsp; [クラス凝集性のクライテリア](#SS_8_7_3)  

&emsp;&emsp; [Modern CMake project layout](#SS_8_8)  
&emsp;&emsp;&emsp; [Modern CMake project layoutのカスタマイズ](#SS_8_8_1)  

&emsp;&emsp; [コーディングスタイル](#SS_8_9)  
&emsp;&emsp;&emsp; [AAAスタイル](#SS_8_9_1)  
&emsp;&emsp;&emsp; [east-const](#SS_8_9_2)  
&emsp;&emsp;&emsp; [west-const](#SS_8_9_3)  

&emsp;&emsp; [オブジェクトのコピー](#SS_8_10)  
&emsp;&emsp;&emsp; [シャローコピー](#SS_8_10_1)  
&emsp;&emsp;&emsp; [ディープコピー](#SS_8_10_2)  
&emsp;&emsp;&emsp; [スライシング](#SS_8_10_3)  

&emsp;&emsp; [C++注意点](#SS_8_11)  
&emsp;&emsp;&emsp; [オーバーライドとオーバーロードの違い](#SS_8_11_1)  
&emsp;&emsp;&emsp; [danglingリファレンス](#SS_8_11_2)  
&emsp;&emsp;&emsp; [danglingポインタ](#SS_8_11_3)  
&emsp;&emsp;&emsp; [Most Vexing Parse](#SS_8_11_4)  

&emsp;&emsp; [ソフトウェア一般](#SS_8_12)  
&emsp;&emsp;&emsp; [ヒープ](#SS_8_12_1)  
&emsp;&emsp;&emsp; [スレッドセーフ](#SS_8_12_2)  
&emsp;&emsp;&emsp; [リエントラント](#SS_8_12_3)  
&emsp;&emsp;&emsp; [クリティカルセクション](#SS_8_12_4)  
&emsp;&emsp;&emsp; [スピンロック](#SS_8_12_5)  
&emsp;&emsp;&emsp; [ミックスイン](#SS_8_12_6)  
&emsp;&emsp;&emsp; [ハンドル](#SS_8_12_7)  
&emsp;&emsp;&emsp; [フリースタンディング環境](#SS_8_12_8)  
&emsp;&emsp;&emsp; [サイクロマティック複雑度](#SS_8_12_9)  
&emsp;&emsp;&emsp; [凝集性](#SS_8_12_10)  
&emsp;&emsp;&emsp;&emsp; [凝集性の欠如](#SS_8_12_10_1)  
&emsp;&emsp;&emsp;&emsp; [LCOM](#SS_8_12_10_2)  

&emsp;&emsp;&emsp; [Spurious Wakeup](#SS_8_12_11)  
&emsp;&emsp;&emsp; [Static Initialization Order Fiasco(静的初期化順序問題)](#SS_8_12_12)  
&emsp;&emsp;&emsp; [副作用](#SS_8_12_13)  
&emsp;&emsp;&emsp; [Itanium C++ ABI](#SS_8_12_14)  

&emsp;&emsp; [C++コンパイラ](#SS_8_13)  
&emsp;&emsp;&emsp; [g++](#SS_8_13_1)  
&emsp;&emsp;&emsp; [clang++](#SS_8_13_2)  

&emsp;&emsp; [非ソフトウェア用語](#SS_8_14)  
&emsp;&emsp;&emsp; [セマンティクス](#SS_8_14_1)  
&emsp;&emsp;&emsp; [割れ窓理論](#SS_8_14_2)  
&emsp;&emsp;&emsp; [車輪の再発明](#SS_8_14_3)  
  
  

[インデックス](#SS_1_2)に戻る。  

___

## イディオム <a id="SS_8_1"></a>

### ガード節(Early Return) <a id="SS_8_1_1"></a>
ガード節とは、
「可能な場合、処理を早期に打ち切るために関数やループの先頭に配置される短い条件文(通常はif文)」
であり、以下のような利点がある。

* 処理の打ち切り条件が明確になる。
* 関数やループのネストが少なくなる。

まずは、ガード節を使っていない例を上げる。

```cpp
    //  example/cpp_idioms/guard_ut.cpp 24

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
    //  example/cpp_idioms/guard_ut.cpp 77

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
    //  example/cpp_idioms/guard_ut.cpp 48

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
    //  example/cpp_idioms/guard_ut.cpp 94

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


### RAII(scoped guard) <a id="SS_8_1_2"></a>
RAIIとは、「Resource Acquisition Is Initialization」の略語であり、
リソースの確保と解放をオブジェクトの初期化と破棄処理に結びつけるパターンもしくはイデオムである。
特にダイナミックにオブジェクトを生成する場合、
RAIIに従わないとメモリリークを防ぐことは困難である。

下記は、関数終了付近でdeleteする素朴なコードである。

```cpp
    //  example/cpp_idioms/raii_ut.cpp 19

    // Aは外部の変数をリファレンスcounter_として保持し、
    //  * コンストラクタ呼び出し時に++counter_
    //  * デストラクタタ呼び出し時に--counter_
    // とするため、生成と解放が同じだけ行われれば外部の変数の値は0となる
    class A {
    public:
        A(uint32_t& counter) noexcept : counter_{++counter} {}
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
    //  example/cpp_idioms/raii_ut.cpp 72

    auto object_counter = 0U;

    // 第1引数が5なのでエクセプション発生
    ASSERT_THROW(not_use_RAII_for_memory(5, object_counter), std::exception);

    // 上記のnot_use_RAII_for_memoryではエクセプションが発生し、メモリリークする
    ASSERT_EQ(1, object_counter);
```

以下は、std::unique_ptrによってRAIIを導入し、この問題に対処した例である。

```cpp
    //  example/cpp_idioms/raii_ut.cpp 84

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
    //  example/cpp_idioms/raii_ut.cpp 101

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
    //  example/cpp_idioms/raii_ut.cpp 112

    // RAIIをしない例
    // 複数のclose()を書くような関数は、リソースリークを起こしやすい。
    void not_use_RAII_for_socket()
    {
        auto fd = socket(AF_INET, SOCK_STREAM, 0);

        try {
            // Do something
            // ...
        }
        catch (std::exception const& e) {  // エクセプションはconstリファレンスで受ける。
            close(fd);                     // NG RAII未使用
            // Do something to recover
            // ...

            return;
        }
        // ...
        close(fd);  // NG RAII未使用
    }
```

エクセプションを扱うために関数の2か所でソケットをcloseしている。
この程度であれば大きな問題にはならないだろうが、実際には様々な条件が重なるため、
リソースの解放コードは醜悪にならざるを得ない。

このような場合には、下記するようなリソース解放用クラス

```cpp
    //  h/scoped_guard.h 7

    /// @brief RAIIのためのクラス。コンストラクタ引数の関数オブジェクトをデストラクタから呼び出す
    ///
    #if __cplusplus >= 202002L   // c++20

    template <std::invocable F>  // Fが呼び出し可能であることを制約
    #else  // c++17

    template <typename F>
    #endif
    class ScopedGuard {
    public:
        explicit ScopedGuard(F&& f) noexcept : f_{f}
        {
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
    //  example/cpp_idioms/raii_ut.cpp 139

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

        // Do something
    }
```

クリティカルセクションの保護をlock/unlockで行うstd::mutex等を使う場合にも、
std::lock_guard<>によってunlockを行うことで、同様の効果が得られる。


### Copy-And-Swap <a id="SS_8_1_3"></a>
メンバ変数にポインタやスマートポインタを持つクラスに

* copyコンストラクタ
* copy代入演算子
* moveコンストラクタ
* move代入演算子

が必要になった場合、コンパイラが生成するデフォルトの
[特殊メンバ関数](#SS_6_6_1)では機能が不十分であることが多い。

下記に示すコードは、そのような場合の上記4関数の実装例である。

```cpp
    //  example/cpp_idioms/no_copy_and_swap_ut.cpp 8

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

* copy代入演算子には、[エクセプション安全性の保証](#SS_6_13)がない。
* 上記4関数は似ているにも関わらず、微妙な違いがあるためコードクローンとなっている。

ここで紹介するCopy-And-Swapはこのような問題を解決するためのイデオムである。

実装例を以下に示す。

```cpp
    //  example/cpp_idioms/copy_and_swap_ut.cpp 6

    class CopyAndSwap final {
    public:
        explicit CopyAndSwap(char const* name0, char const* name1)
            : name0_{name0 == nullptr ? "" : name0}, name1_{name1 == nullptr ? "" : name1}
        {
        }

        CopyAndSwap(CopyAndSwap const& rhs) : name0_{rhs.name0_}, name1_{rhs.name1_} {}

        CopyAndSwap(CopyAndSwap&& rhs) noexcept : name0_{std::exchange(rhs.name0_, nullptr)}, name1_{std::move(rhs.name1_)}
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
これにより[エクセプション安全性の保証](#SS_6_13)を持つ4関数をコードクローンすることなく実装できる。


### CRTP(curiously recurring template pattern) <a id="SS_8_1_4"></a>
CRTPとは、

```cpp
    //  example/cpp_idioms/crtp_ut.cpp 12

    template <typename T>
    class Base {
        // ...
    };

    class Derived : public Base<Derived> {
        // ...
    };
```

のようなテンプレートによる再帰構造を用いて、静的ポリモーフィズムを実現するためのパターンである。
以下にこのパターンを使用した[ミックスイン](#SS_8_12_6)の例を示す。

```cpp
    //  example/cpp_idioms/crtp_ut.cpp 25

    std::atomic<uint32_t> DerivedClass_Count = 0;  // Counterの派生クラスのインスタンス数

    template <typename T>
    class Counter {  // 派生クラスのインスタンスを計測するミックスイン
    public:
        Counter() { ++DerivedClass_Count; }
        Counter(const Counter&) { ++DerivedClass_Count; }
        ~Counter() { --DerivedClass_Count; }
    };

    class A : public Counter<A> {
        // クラスAの実装
        // ...
    };

    class B : public Counter<B> {
        // クラスBの実装
        // ...
    };
```
```cpp
    //  example/cpp_idioms/crtp_ut.cpp 50

    A a0;
    B b0;

    ASSERT_EQ(2, DerivedClass_Count);  // インスタンスが２個のテスト

    {
        auto a1 = a0;
        ASSERT_EQ(3, DerivedClass_Count);  // コピーによりインスタンスの増加のテスト
    }
    ASSERT_EQ(2, DerivedClass_Count);  // a1のスコープアウトによりインスタンスが減少
```

なお、このパターンは、[std::enable_shared_from_this](#SS_7_5_2_2)の使用において前提知識となっている。

### Accessor <a id="SS_8_1_5"></a>
publicメンバ変数とそれにアクセスするソースコードは典型的なアンチパターンであるため、
このようなコードを禁じるのが一般的なプラクティスである。

```cpp
    //  example/cpp_idioms/accessor_ut.cpp 8

    class A {  // アンチパターン
    public:
        int32_t a_{0};
    };

    void f(A& a) noexcept
    {
        a.a_ = 3;

        // Do something
        // ...
    }
```

とはいえ、ソフトウェアのプラクティスには必ずといってほど例外があり、
製品開発の現場において、オブジェクトのメンバ変数にアクセスせざるを得ないような場面は、
稀にではあるが発生する。
このような場合に適用するがのこのイデオムである。

```cpp
    //  example/cpp_idioms/accessor_ut.cpp 28

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
        // ...
    };

    void f(A& a) noexcept
    {
        a.SetA(3);

        // Do something
        // ...
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
    //  example/cpp_idioms/accessor_ut.cpp 62

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
            // ...
        }
        // ...
    };

    void f(A& a) noexcept
    {
        if (a.GetA() != 3) {
            a.SetA(3);
            a.Change(true);
        }

        // ...
    }

    void g(A& a) noexcept
    {
        if (!a.IsChanged()) {
            return;
        }

        a.Change(false);
        a.DoSomething();  // a.IsChanged()がtrueの時に実行する。

        // ...
    }
```

上記ソースコードは、オブジェクトaのA::a\_が変更された場合、
その後、それをもとに何らかの動作を行うこと(a.DoSomething)を表しているが、
本来オブジェクトaの状態が変わったかどうかはオブジェクトa自体が判断すべきであり、
a.DoSomething()の実行においても、それが必要かどうかはオブジェクトaが判断すべきである。
この考えに基づいた修正ソースコードを下記に示す。

```cpp
    //  example/cpp_idioms/accessor_ut.cpp 130

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
            // ...

            is_changed_ = false;  // 状態変更の取り消し
        }
        // ...
    };

    void f(A& a) noexcept
    {
        a.SetA(3);

        // ...
    }

    void g(A& a) noexcept
    {
        a.DoSomething();  // DoSomethingは無条件で呼び出す。
                          // 実際に何かをするかどうかは、オブジェクトaが決める。
        // ...
    }
```

setterを使用する場合、上記のように処理の隠蔽化には特に気を付ける必要がある。


### Immutable <a id="SS_8_1_6"></a>
クラスに対するimmutable、immutabilityの定義を以下のように定める。

* immutable(不変な)なクラスとは、初期化後、状態の変更ができないクラスを指す。
* immutability(不変性)が高いクラスとは、
  状態を変更するメンバ関数(非constなメンバ関数)が少ないクラスを指す。

immutabilityが高いほど、そのクラスの使用方法は制限される。
これにより、そのクラスやそのクラスを使用しているソースコードの可読性やデバッグ容易性が向上する。
また、クラスがimmutableでなくても、そのクラスのオブジェクトをconstハンドル経由でアクセスすることで、
immutableとして扱うことができる。

一方で、「[Accessor](#SS_8_1_5)」で紹介したsetterは、クラスのimmutabilityを下げる。
いつでも状態が変更できるため、ソースコードの可読性やデバッグ容易性が低下する。
また、マルチスレッド環境においてはこのことが競合問題や、
それを回避するためのロックがパフォーマンス問題やデッドロックを引き起こしてしまう。

従って、クラスを宣言、定義する場合、immutabilityを出来るだけ高くするべきであり、
そのクラスのオブジェクトを使う側は、
可能な限りimmutableオブジェクト(constオブジェクト)として扱うべきである。


### NVI(non virtual interface) <a id="SS_8_1_7"></a>
NVIとは、「virtualなメンバ関数をpublicにしない」という実装上の制約である。

下記のようにクラスBaseが定義されているとする。

```cpp
    //  example/cpp_idioms/nvi_ut.cpp 7

    class Base {
    public:
        virtual bool DoSomething(int something) const noexcept
        {
            // ...
        }

        virtual ~Base() = default;

    private:
        // ...
    };
```

これを使うクラスはBase::DoSomething()に依存する。
また、このクラスから派生した下記のクラスDerivedもBase::DoSomething()に依存する。

```cpp
    //  example/cpp_idioms/nvi_ut.cpp 26

    class Derived : public Base {
    public:
        virtual bool DoSomething(int something) const noexcept override
        {
            // ...
        }

    private:
        // ...
    };
```

この条件下ではBase::DoSomething()へ依存が集中し、この関数の修正や機能追加の作業コストが高くなる。
このイデオムは、この問題を軽減する。

これを用いた上記2クラスのリファクタリング例を以下に示す。

```cpp
    //  example/cpp_idioms/nvi_ut.cpp 57

    class Base {
    public:
        bool DoSomething(int something) const noexcept { return do_something(something); }
        virtual ~Base() = default;

    private:
        virtual bool do_something(int something) const noexcept
        {
            // ...
        }

        // ...
    };

    class Derived : public Base {
    private:
        virtual bool do_something(int something) const noexcept override
        {
            // ...
        }

        // ...
    };
```

オーバーライド元の関数とそのオーバーライドのデフォルト引数の値は一致させる必要がある。

それに従わない下記のようなクラスとその派生クラス

```cpp
    //  example/cpp_idioms/nvi_ut.cpp 105

    class NotNviBase {
    public:
        virtual std::string Name(bool mangled = false) const { return mangled ? typeid(*this).name() : "NotNviBase"; }

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
    //  example/cpp_idioms/nvi_ut.cpp 126

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
    //  example/cpp_idioms/nvi_ut.cpp 145
    class NviBase {
    public:
        std::string Name(bool mangled = false) const { return name(mangled); }
        virtual ~NviBase() = default;

    private:
        virtual std::string name(bool mangled) const { return mangled ? typeid(*this).name() : "NviBase"; }
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
    //  example/cpp_idioms/nvi_ut.cpp 167

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


## 実装パターン <a id="SS_8_2"></a>
### Pimpl <a id="SS_8_2_1"></a>
このパターンは、「クラスA(a.cpp、a.hで宣言、定義)を使用するクラスにAの実装の詳細を伝搬させたくない」
ような場合に使用する。
そのため[オープン・クローズドの原則(OCP)](#SS_2_2)の実装方法としても有用である。

一般的に、STLライブラリのパースは多くのCPUタイムを消費する。
クラスAがSTLクラスをメンバに使用し、a.hにそのSTLヘッダファイルがインクルードされた場合、
a.hをインクルードするファイルをコンパイルする度にそのSTLヘッダファイルはパースされる。
これはさらに多くのCPUタイムの消費につながり、ソースコード全体のビルドは遅くなる。
こういった問題をあらかじめ避けるためにも有効な手段ではあるが、
そのトレードオフとして実行速度は若干遅くなる。

下記は、Pimplイデオム未使用の、std::stringに依存したクラスStringHolderOldの例である。

```cpp
    //  example/cpp_idioms/string_holder_old.h 3
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
    //  example/cpp_idioms/string_holder_old.cpp 1

    #include "string_holder_old.h"

    StringHolderOld::StringHolderOld() : str_{std::make_unique<std::string>()} {}

    void StringHolderOld::Add(char const* str) { *str_ += str; }

    char const* StringHolderOld::GetStr() const { return str_->c_str(); }
```


下記は、上記クラスStringHolderOldにPimplイデオムを適用したクラスStringHolderNewの例である。

```cpp
    //  example/cpp_idioms/string_holder_new.h 3
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
    //  example/cpp_idioms/string_holder_new.cpp 1
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

```essential/plant_uml/pimpl_pattern.pu
@startuml

scale max 750 width

rectangle "Not Pimpl" as Not_Pimpl {
    agent "string_holder_old.h" as string_holder_old_h
    agent "string_holder_old.cpp" as string_holder_old_cpp
    agent "client_old.cpp" as client_old_cpp

    string_holder_old_cpp -up-> string_holder_old_h
    client_old_cpp -up-> string_holder_old_h
}

rectangle "Pimpl" as Pimpl {
    agent "string_holder_new.h" as string_holder_new_h
    agent "string_holder_new.cpp" as string_holder_new_cpp
    agent "client_new.cpp" as client_new_cpp

    string_holder_new_cpp -up->  string_holder_new_h
    client_new_cpp -up-> string_holder_new_h
}

agent "std::string" as string

string_holder_old_h -up-> string
string_holder_new_cpp -up->  string

note top of string_holder_old_h
string_holder_old.hは、
std::stringに依存しているため、
string_holder_old.hを使用する
ファイル(client_old.cpp)に
std::stringへの依存を強要する。
end note

note top of string_holder_new_h
string_holder_new.hは、
std::stringに依存していないので、
string_holder_new.hを使用する
ファイル(client_new.cpp)に
std::stringへの依存を強要しない。
end note

@enduml
```

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

```essential/plant_uml/widget_ng.pu
@startuml
scale max 700 width

agent "gtest/gtest.h" as gtest_h

rectangle "Lib" as Lib {
    agent "h/widget.h" as widget_h
    agent "src/widget.cpp" as widget_cpp
    agent "ut/widget_ut.cpp" as widget_ut_cpp
}

agent client

widget_h -left-> gtest_h
widget_cpp -up-> widget_h
widget_ut_cpp -up-> widget_h
client -up-> widget_h

@enduml
```

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

```essential/plant_uml/widget_ok.pu
@startuml
scale max 700 width

agent "gtest/gtest.h" as gtest_h

rectangle "Lib" as Lib {
    agent "h/widget.h" as widget_h
    agent "src/widget.cpp" as widget_cpp
    agent "src/widget_internal.h" as widget_internal_h
    agent "ut/widget_ut.cpp" as widget_ut_cpp
}

agent client

widget_cpp -up-> widget_internal_h
widget_ut_cpp -up-> gtest_h
widget_ut_cpp -up-> widget_internal_h
widget_internal_h -right-> widget_h
client -up-> widget_h

@enduml
```

### lightweight Pimpl <a id="SS_8_2_2"></a>
[Pimpl](#SS_8_2_1)の解説で示したように依存関係をシンプルに保つには極めて有効なパターンではあるが、
このパターンで実装されたクラスのインスタンス化のたびに一回以上のヒープからのアロケーションが必要になるため、
このオーバーヘッドが気になるような場合に備えて、アロケーションを少なくするテクニックを以下に示す
(なお、lightweight Pimplとは筆者の造語であり、ここで紹介するパターンはPimplの一種である)。

```cpp
    //  example/cpp_idioms/light_pimpl.h 8

    class LightPimpl {
    public:
        LightPimpl(std::string const& name);
        ~LightPimpl();
        LightPimpl(LightPimpl const&)            = delete;  // コピーは禁止
        LightPimpl& operator=(LightPimpl const&) = delete;  // コピーは禁止

        std::vector<uint8_t> const& GetVector() const;
        std::string const&          GetName() const;

        static constexpr size_t BufferLen = 10;
        uint8_t (&GetBuffer())[BufferLen];
        uint8_t const (&GetBuffer() const)[BufferLen];  // const を追加

    private:
        // Impl_tをプレースメントnewでインスタンス化する時に使用するメモリ
        alignas(std::max_align_t) uint8_t memory_[48];  // 配列長はsizeof(Impl_t)以上になるよう調整
        struct Impl_t;
        struct Impl_t* pimpl_;
    };
```

このクラスの実装を以下に示す。

```cpp
    //  example/cpp_idioms/light_pimpl_ut.cpp 5

    namespace {
    bool constructor_called = false;  // テスト用フラグであるため、実装には無関係
    bool destructor_called  = false;  // テスト用フラグであるため、実装には無関係
    }  // namespace

    struct LightPimpl::Impl_t {
        Impl_t(std::string const& name) : name_{name} { constructor_called = true; /* コンストラクタが呼ばれたマーク */ }
        std::vector<uint8_t> vect_{};
        std::string          name_{};
        uint8_t              buffer_[BufferLen]{};

        ~Impl_t() { destructor_called = true; /* デストラクタが呼ばれたマーク */ }
    };

    LightPimpl::LightPimpl(std::string const& name) : pimpl_{new (memory_) Impl_t{name}}  // プレースメントnew
    {
        static_assert(sizeof(Impl_t) <= sizeof(memory_), "Buffer size mismatch");
        static_assert(sizeof(memory_) - sizeof(Impl_t) < 16, "Buffer has excessive padding");
        static_assert(alignof(Impl_t) <= alignof(std::max_align_t), "Buffer alignment mismatch");
    }

    LightPimpl::~LightPimpl() { pimpl_->~Impl_t(); }  // Impl_tのデストラクタを直接呼び出す

    std::vector<uint8_t> const& LightPimpl::GetVector() const { return pimpl_->vect_; }
    std::string const&          LightPimpl::GetName() const { return pimpl_->name_; }

    uint8_t (&LightPimpl::GetBuffer())[LightPimpl::BufferLen] { return pimpl_->buffer_; }

    uint8_t const (&LightPimpl::GetBuffer() const)[LightPimpl::BufferLen] { return pimpl_->buffer_; }
```

ヒープ以外のメモリからnewするための[プレースメントnew](#SS_6_6_9)を使用しているため、
上記の抜粋である以下のコードはやや見慣れないかもしれない。

```cpp
    //  example/cpp_idioms/light_pimpl_ut.cpp 21

    LightPimpl::LightPimpl(std::string const& name) : pimpl_{new (memory_) Impl_t{name}}  // プレースメントnew
    {
        static_assert(sizeof(Impl_t) <= sizeof(memory_), "Buffer size mismatch");
        static_assert(sizeof(memory_) - sizeof(Impl_t) < 16, "Buffer has excessive padding");
        static_assert(alignof(Impl_t) <= alignof(std::max_align_t), "Buffer alignment mismatch");
    }
```

プレースメントnewで構築したオブジェクトの解放にはdeleteは使えない。
オブジェクトがその上で構築されているメモリはヒープのものではないため、deleteすると未定義動作につながる。

deleteを使わずにプレースメントnewで構築したオブジェクトの各メンバのデストラクタを呼び出さなければ、
リソースリークにつながる。この問題を解決するためのコードは、上記の抜粋である以下のようなものになる。

```cpp
    //  example/cpp_idioms/light_pimpl_ut.cpp 30

    LightPimpl::~LightPimpl() { pimpl_->~Impl_t(); }  // Impl_tのデストラクタを直接呼び出す
```

上記のクラスの動作を以下の単体テストにより示す。

```cpp
    //  example/cpp_idioms/light_pimpl_ut.cpp 48

    {
        ASSERT_FALSE(constructor_called);
        LightPimpl lp{"lp"};

        ASSERT_EQ(lp.GetName(), "lp");
        ASSERT_EQ(lp.GetVector().size(), 0);
        ASSERT_EQ(lp.GetBuffer()[0], 0x0);

        ASSERT_TRUE(constructor_called);
        ASSERT_FALSE(destructor_called);
    };  // この行で、lpは解放される

    ASSERT_TRUE(destructor_called);
```

**[ 通常のPimplとの比較 ]**

| 特徴                 | 通常のPimpl                   | Lightweight Pimpl           |
|----------------------|-------------------------------|-----------------------------|
| メモリ確保           | ヒープ                        | スタック(オブジェクト内)    |
| アロケーション回数   | インスタンス毎に1回以上       | 0回                         |
| パフォーマンス       | new/deleteのオーバーヘッド    | 通常のPimplより良い         |
| 実装の複雑さ         | シンプル                      | やや複雑(プレースメントnew) |
| メモリサイズの柔軟性 | 高い                          | 低い(コンパイル時に固定)    |

### BitmaskType <a id="SS_8_2_3"></a>
下記のようなビットマスク表現は誤用しやすいインターフェースである。
修正や拡張等に関しても脆弱であるため、避けるべきである。

```cpp
    //  example/cpp_idioms/enum_operator.h 6

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
        // ...
    };
```

```cpp
    //  example/cpp_idioms/enum_operator_ut.cpp 13

    Animal dolphin{Animal::PhisicalAbility::Swim};  // OK
    ASSERT_EQ(Animal::PhisicalAbility::Swim, dolphin.GetPhisicalAbility());

    Animal uma{0xff};  // NG 誤用だが、コンストラクタの仮引数の型がuint32_tなのでコンパイル可能
```

上記のような誤用を防ぐために、
enumによるビットマスク表現を使用して型チェックを強化した例を以下に示す。
このテクニックは、STLのインターフェースとしても使用されている強力なイデオムである。

```cpp
    //  example/cpp_idioms/enum_operator.h 30

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
    constexpr Animal::PhisicalAbility operator&(Animal::PhisicalAbility x, Animal::PhisicalAbility y) noexcept
    {
        return static_cast<Animal::PhisicalAbility>(static_cast<uint32_t>(x) & static_cast<uint32_t>(y));
    }

    constexpr Animal::PhisicalAbility operator|(Animal::PhisicalAbility x, Animal::PhisicalAbility y) noexcept
    {
        return static_cast<Animal::PhisicalAbility>(static_cast<uint32_t>(x) | static_cast<uint32_t>(y));
    }

    inline Animal::PhisicalAbility& operator&=(Animal::PhisicalAbility& x, Animal::PhisicalAbility y) noexcept
    {
        return x = x & y;
    }

    // ...
```

```cpp
    //  example/cpp_idioms/enum_operator_ut.cpp 28

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


### Future <a id="SS_8_2_4"></a>
[Future](https://ja.wikipedia.org/wiki/Future_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)とは、
並行処理のためのデザインパターンであり、別スレッドに何らかの処理をさせる際、
その結果の取得を、必要になるまで後回しにする手法である。

C++11では、std::future, std::promise, std::asyncによって実現できる。

まずは、C++03以前のスタイルから示す。

```cpp
    //  example/cpp_idioms/future_ut.cpp 11

    int do_something(std::string_view str0, std::string_view str1) noexcept
    {
        // ...

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
    //  example/cpp_idioms/future_ut.cpp 45

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



### Null Object <a id="SS_8_2_5"></a>
オブジェクトへのポインタを受け取った関数が
「そのポインタがnullptrでない場合、そのポインタが指すオブジェクトに何かをさせる」
というような典型的な条件文を削減するためのパターンである。

```cpp
    //  example/cpp_idioms/null_object_ut.cpp 7

    class A {
    public:
        // ...
        bool Action() noexcept
        {
            // do something
            // ...
            return result;
        }
        // ...
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
    //  example/cpp_idioms/null_object_ut.cpp 41

    class A {
    public:
        // ...
        bool Action() noexcept { return action(); }

    private:
        virtual bool action() noexcept
        {
            // do something
            // ...
            return result;
        }
        // ...
    };

    class ANull final : public A {
        // ...
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


### Cでのクラス表現 <a id="SS_8_2_6"></a>
このドキュメントは、C++でのソフトウェア開発を前提としているため、
ここで示したコードもC++で書いているが、

* 何らかの事情でCを使わざるを得ないプログラマがデザインパターンを使用できるようにする
* クラスの理解が曖昧なC++プログラマの理解を助ける(「[ポリモーフィックなクラス](#SS_6_4_8)」参照)

ような目的のためにCでのクラスの実現方法を例示する。

下記のような基底クラスPointとその派生クラスPoint3Dがあった場合、

```essential/plant_uml/class_c.pu
@startuml

class Point {
    + GetXY() const
    + SetXY()
    + {abstract} Quantity() const  // 仮想関数
    + {abstract} Multipy()         // 仮想関数
}

class Point3D {
    + GetXYZ() const
    + SetXYZ()
    + Quantity() const  // オーバーライド
    + Multipy()         // オーバーライド
}

Point <|-down- Point3D

@enduml
```

C++では、Pointのコードは下記のように表すことが一般的である。

```cpp
    //  example/cpp_idioms/class_ut.cpp 7

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
    //  example/cpp_idioms/class_ut.cpp 42

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
    //  example/cpp_idioms/class_ut.cpp 124

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
    //  example/cpp_idioms/class_ut.cpp 164

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
    //  example/cpp_idioms/class_ut.cpp 65

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
    //  example/cpp_idioms/class_ut.cpp 98

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
    //  example/cpp_idioms/class_ut.cpp 188

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
    //  example/cpp_idioms/class_ut.cpp 221

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

## オブジェクト指向 <a id="SS_8_3"></a>
### is-a <a id="SS_8_3_1"></a>
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

bird::flyのオーバーライド関数(penguin::fly)について、[リスコフの置換原則(LSP)](#SS_2_3)に反した例を下記する。

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
kyukanchoとstd::stringの関係を[has-a](#SS_8_3_2)の関係と呼ぶ。


### has-a <a id="SS_8_3_2"></a>
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

### is-implemented-in-terms-of <a id="SS_8_3_3"></a>
「is-implemented-in-terms-of」の関係は、
オブジェクト指向プログラミング（OOP）において、
あるクラスが別のクラスの機能を内部的に利用して実装されていることを示す概念である。
これは、あるクラスが他のクラスのインターフェースやメンバ関数を用いて、
自身の機能を提供する場合に使われる。
[has-a](#SS_8_3_2)の関係は、is-implemented-in-terms-of の関係の一種である。

is-implemented-in-terms-ofは下記の手段1-3に示した方法がある。

* 手段1.[public継承によるis-implemented-in-terms-of](#SS_8_3_3_1)  
* 手段2.[private継承によるis-implemented-in-terms-of](#SS_8_3_3_2)  
* 手段3.[コンポジションによる(has-a)is-implemented-in-terms-of](#SS_8_3_3_3)  

手段1-3にはそれぞれ、長所、短所があるため、必要に応じて手段を選択する必要がある。
以下の議論を単純にするため、下記のようにクラスS、C、CCを定める。

* S(サーバー): 実装を提供するクラス
* C(クライアント): Sの実装を利用するクラス
* CC(クライアントのクライアント): Cのメンバを使用するクラス

コード量の観点から考えた場合、手段1が最も優れていることが多い。
依存関係の複雑さから考えた場合、CはSに強く依存する。
場合によっては、この依存はCCからSへの依存間にも影響をあたえる。
従って、手段3が依存関係を単純にしやすい。
手段1は[is-a](#SS_8_3_1)に見え、以下に示すような問題も考慮する必要があるため、
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


#### public継承によるis-implemented-in-terms-of <a id="SS_8_3_3_1"></a>
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
[private継承によるis-implemented-in-terms-of](#SS_8_3_3_2)や、
[コンポジションによる(has-a)is-implemented-in-terms-of](#SS_8_3_3_3)
と比べコードがシンプルになる。 

#### private継承によるis-implemented-in-terms-of <a id="SS_8_3_3_2"></a>
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

この方法は、[public継承によるis-implemented-in-terms-of](#SS_8_3_3_1)が持つデストラクタ問題は発生せす、
[is-a](#SS_8_3_1)と誤解してしまう問題も発生しない。


#### コンポジションによる(has-a)is-implemented-in-terms-of <a id="SS_8_3_3_3"></a>
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

## オブジェクトの所有権 <a id="SS_8_4"></a>
### オブジェクトの排他所有 <a id="SS_8_4_1"></a>
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
std::unique_ptr、std::move()、[rvalue](#SS_6_7_1_2)の関係を解説する。

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

### オブジェクトの共有所有 <a id="SS_8_4_2"></a>
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
std::shared_ptr、std::move()、[rvalue](#SS_6_7_1_2)の関係を解説する。

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
* 下記のようなコードはstd::shared_ptrの仕様が想定する[セマンティクス](#SS_8_14_1)に沿っておらず、
  [未定義動作](#SS_6_14_3)に繋がる。

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


### オブジェクトの循環所有 <a id="SS_8_4_3"></a>
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

X、Yオブジェクトへの[ハンドル](#SS_8_12_7)を完全に失った状態であり、X、Yオブジェクトを解放する手段はない。

## copy/moveと等価性のセマンティクス <a id="SS_8_5"></a>
### 等価性のセマンティクス <a id="SS_8_5_1"></a>
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

組み込みの==やオーバーロード[==演算子](#SS_6_6_3)のこのような性質をここでは「等価性のセマンティクス」と呼ぶ。

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

この問題は、「[RTTI](#SS_6_4_9)」使った下記のようなコードで対処できる。

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
[オープン・クローズドの原則(OCP)](#SS_2_2)にも対応した柔軟な構造を実現している。

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
文字列リテラルからstd::stringへの[暗黙の型変換](#SS_6_6_2_2)が起こるために成立する。

以上で見てきたように、等価性のセマンティクスを守ったoperator==の実装には多くの観点が必要になる。

### copyセマンティクス <a id="SS_8_5_2"></a>
copyセマンティクスとは以下を満たすようなセマンティクスである。

* a = bが行われた後に、aとbが等価である。
* a = bが行われた前後でbの値が変わっていない。

従って、これらのオブジェクトに対して[等価性のセマンティクス](#SS_8_5_1)
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
「[等価性のセマンティクス](#SS_8_5_1)」で示した最後の例も、copyセマンティクスを満たしていない。

```cpp
    //  example/cpp_idioms/semantics_ut.cpp 364

    auto b = Base{1};
    auto d = Derived{1};

    b = d;  // スライシングが起こる

    ASSERT_FALSE(b == d);  // copyセマンティクスを満たしていない
```

原因は、copy代入で[スライシング](#SS_8_10_3)が起こるためである。


### moveセマンティクス <a id="SS_8_5_3"></a>
moveセマンティクスとは以下を満たすようなセマンティクスである(operator==が定義されていると前提)。

* パフォーマンス要件  
    move代入の実行コスト <= copy代入の実行コスト(通常はmove代入の方が高速)

* 意味的要件  
    a == b が true の時に、c = std::move(a) を実行すると、  
    * b == c が true になる（値が保存される）
    * a == c は true にならなくても良い（aはmove後に不定状態になり得る）

* リソース管理   
    必須ではないが、aがポインタ等のリソースを保有している場合、
     move代入後にはそのリソースはcに移動していることが一般的である(「[rvalue](#SS_6_7_1_2)」参照)

* エクセプション安全性  
    [no-fail保証](#SS_6_13_1)をする(noexceptと宣言し、エクセプションをthrowしない)

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

### MoveAssignable要件 <a id="SS_8_5_4"></a>
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
   これは、リソースの複製を避けることで達成される(「[moveセマンティクス](#SS_8_5_3)」参照)。

5. デフォルト実装  
   move代入演算子が明示的に定義されていない場合でも、
   クラスが一定の条件(例: move不可能なメンバが存在しないこと)を満たしていれば、
   コンパイラがデフォルトの実装(「[特殊メンバ関数](#SS_6_6_1)」参照)を生成する。

### CopyAssignable要件 <a id="SS_8_5_5"></a>
CopyAssignable要件は、C++において型がcopy代入をサポートするために満たすべき条件を指す。

1. 動作が定義されていること  
   代入操作は未定義動作を引き起こしてはならない。自己代入（同じオブジェクトを代入する場合）においても正しく動作し、
   リソースリークを引き起こさないことが求められる。

2. 値の保持  
   代入後、代入先のオブジェクトの値は代入元のオブジェクトの値と一致していなければならない。

3. 正しいセマンティクス  
   copy代入によって代入元のオブジェクトが変更されてはならない(「[copyセマンティクス](#SS_8_5_2)」参照)。
   代入先のオブジェクトが保持していたリソース(例: メモリ)は適切に解放される必要がある。

4. デフォルト実装  
   copy代入演算子が明示的に定義されていない場合でも、
   クラスが一定の条件(例: copy不可能なメンバが存在しないこと)を満たしていれば、
   コンパイラがデフォルトの実装(「[特殊メンバ関数](#SS_6_6_1)」参照)を生成する。

## 関数設計のガイドライン <a id="SS_8_6"></a>
### 関数の引数と戻り値の型 <a id="SS_8_6_1"></a>
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

[注] `templat<typename T> f(T&&)`の`T&&`は[forwardingリファレンス](#SS_6_8_3)である。  

[注] 以下のような引数型は避けるべきである。  

* `X const*`
* `X*`
* `X&`


### サイクロマティック複雑度のクライテリア <a id="SS_8_6_2"></a>
関数構造の適・不適については、[サイクロマティック複雑度](#SS_8_12_9)によって下記テーブルのように定義する。

| サイクロマティック複雑度(CC) | 複雑さの状態                                     |
| :--------------------------: | :----------------------------------------------- |
|            CC <= 10          | 非常に良い構造(適)                               |
|       11 < CC <  30          | やや複雑(概ね適)                                 |
|       31 < CC <  50          | 構造的なリスクあり(場合により不適)               |
|       51 < CC                | テスト不可能、デグレードリスクが非常に高い(不適) |

### 関数の行数のクライテリア <a id="SS_8_6_3"></a>
C++の創始者であるビャーネ・ストラウストラップ氏は、
  [プログラミング言語C++ 第4版](https://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9EC-%E7%AC%AC4%E7%89%88-%E3%83%93%E3%83%A3%E3%83%BC%E3%83%8D%E3%83%BB%E3%82%B9%E3%83%88%E3%83%A9%E3%82%A6%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97-ebook/dp/B01BGEO9MS)
  の中で、下記のように述べている。

```
    約 40 行を関数の上限にすればよい。 
    私自身は、もっと小さい平均 7 行程度を理想としている。 
```

## クラス設計のガイドライン <a id="SS_8_7"></a>
### ゼロの原則(Rule of Zero) <a id="SS_8_7_1"></a>
「ゼロの原則」は、リソース管理を直接クラスで行わず、
リソース管理を専門とするクラス
(例: 標準ライブラリの[RAII(scoped guard)](#SS_8_1_2)クラス)に任せる設計ガイドラインを指す。
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

### 五の原則(Rule of Five) <a id="SS_8_7_2"></a>
「五の原則」は、
クラスがリソース(例: 動的メモリやファイルハンドルなど)を管理する場合、
デフォルトコンストラクタを除く[特殊メンバ関数](#SS_6_6_1)、
つまり以下の5つの関数をすべて適切に定義する必要があるという設計ガイドラインを指す。

* デストラクタ
* コピーコンストラクタ
* コピー代入演算子
* ムーブコンストラクタ
* ムーブ代入演算子

特殊メンバ関数の挙動を正しく定義しないと、
リソースの不適切な管理(例: メモリリーク、リソースの二重解放)を招く可能性がある。
自動生成されるメンバ関数では、
複雑なリソース管理の要件を満たせないことがある(「[シャローコピー](#SS_8_10_1)」参照)。

なお、「五の原則」は、「六の原則」と呼ばれることもある。
その場合、この原則が対象とする関数は、
[特殊メンバ関数](#SS_6_6_1)のすべてとなる。

このガイドラインに従って、コピーやムーブを実装する場合、

* [等価性のセマンティクス](#SS_8_5_1)
* [copyセマンティクス](#SS_8_5_2)
* [moveセマンティクス](#SS_8_5_3)

に従わなけならない。

### クラス凝集性のクライテリア <a id="SS_8_7_3"></a>
クラス構造の適・不適については、[LCOM](#SS_8_12_10_2)によって下記テーブルのように定義する。

| 凝集性の欠如(LCOM)  |  クラスの状態              |
|:-------------------:|:--------------------------:|
|       `LCOM <= 0.4` | 理想的な状態(適)           |
|`0.4 <  LCOM <  0.6` | 要注意状態(場合により不適) |
|`0.6 <= LCOM`        | 改善必須状態(不適)         |


* `LCOM <= 0.4`  
  クラスが非常に凝集しており、[単一責任の原則(SRP)](#SS_2_1)を強く遵守している状態であるため、
  通常、デザインの見直しは不要である。

* `0.4 < LCOM < 0.6`  
  クラスの凝集性がやや弱くなり始めている。
  デザイン見直しの必要な時期が迫りつつあると考えるべきだろう。
  このタイミングであればリファクタリングは低コストで完了できるだろう。

* `0.6 <= LCOM`  
  クラス内のメンバ関数間の関連性が低く、凝集性が不十分である。
  メンバ関数が異なる責務にまたがっている可能性が高いため、
  一刻も早くデザインの見直しを行うべきだろう。

## Modern CMake project layout <a id="SS_8_8"></a>
[Modern CMake project layout](https://cliutils.gitlab.io/modern-cmake/chapters/basics/structure.html)
はパッケージ単位でディレクトリを分割し、各パッケージが独立したビルド単位となる構造である。
このような構造はビルドツールに[CMake](https://cliutils.gitlab.io/modern-cmake/)を使用する場合は特に有効であるが、
makeプロジェクトにおいても有効である。  

[注]
この節でのパッケージとはUMLでのパッケージとは同じソフトウェアの構造の単位であるが、
CMakeでの`find_package`でのパッケージとは意味が異なる。


__[主な特徴]__  

* 公開ヘッダと実装ファイルの明確な分離
* 各パッケージに独自のCMakeLists.txtを配置
* テストコードを各パッケージに併置
* target_include_directories()のPUBLIC/PRIVATEでAPI境界を制御

この構造により、パッケージ間の依存関係が明示化され、モジュール性とテスタビリティが向上する。

__[ディレクトリ構造例]__  

```
    project/
    ├── CMakeLists.txt
    ├── app/
    │   └── main.cpp
    ├── core/
    │   ├── CMakeLists.txt
    │   ├── include/                # 公開ヘッダ
    │   │   └── core/
    │   │     ├── engine.h
    │   │     └── logger.h 
    │   ├── src/                    # 実装ファイル
    │   │   ├── engine.cpp
    │   │   └── internal.h          # 内部ヘッダ
    │   └── tests/                  # 単体テスト
    │       └── engine_test.cpp
    └── logger/
        ├── CMakeLists.txt
        ├── include/
        │   └── logger/
        │       └── logger.h
        ├── src/
        │   └── logger.cpp
        └── tests/
            └── logger_test.cpp
```

ディレクトリ構造例のcore/include/coreの構造は一見冗長に見えるが、
コンパイラに指定するインクルードパスを各パッケージのincludeディレクトリを指定することにより、
パッケージ外部の実装ファイルのインクルードセクションは以下のように記述される。

```cpp
  // インクルードセクション
  #include "core/logger.h"          // パッケージcoreからのインポート
  #include "logger/logger.h"        // パッケージloggerからのインポート
```

このような記述には以下のようなメリットがある。

- ヘッダ名の衝突を避けることができる
- main.cppのインクルードセクションの可読性が向上する

  
__[core/CMakeLists.txt例]__  

```
    # coreライブラリの定義
    add_library(core STATIC
        src/engine.cpp
    )

    # インクルードディレクトリの設定
    # PUBLIC: このライブラリを使う側にも公開されるヘッダパス
    # PRIVATE: このライブラリ内部でのみ使用するヘッダパス
    target_include_directories(core
        PUBLIC 
            ${CMAKE_CURRENT_SOURCE_DIR}/include
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/src
    )

    # 単体テストの定義
    add_executable(core_test tests/engine_test.cpp)

    # テストがcoreライブラリに依存することを宣言
    target_link_libraries(core_test PRIVATE core)
```

__[トップレベルCMakeLists.txt例]__  

```
    cmake_minimum_required(VERSION 3.15)
    project(MyProject)

    # 各コンポーネントをサブディレクトリとして追加
    add_subdirectory(core)
    add_subdirectory(logger)

    # アプリケーション実行ファイルの定義
    add_executable(app app/main.cpp)

    # アプリケーションが依存するライブラリを指定
    # PRIVATE: appの実装内部でのみ使用（他のターゲットにはヘッダパスを公開しない）
    target_link_libraries(app PRIVATE core logger)
```

### Modern CMake project layoutのカスタマイズ <a id="SS_8_8_1"></a>
このドキュメントでは、以下の方針に基づいて[Modern CMake project layout](#SS_8_8)の構成をカスタマイズすることを推奨する。

- パス名が過度に長くなることを避ける。
- `tests`（または `test`）という語は統合テストを指す場合もあるため、
  曖昧さを避ける目的で、単体テストには `ut`（unit test）という語を使用する。

そのため、以下のような置き換えを推奨する。

| オリジナル       | カスタマイズ |
|------------------|--------------|
| include/         | h/           |
| tests/           | ut/          |
| xxx_test.cpp     | xxx_ut.cpp   |


__[置き換え後のディレクトリ構造例]__  

```
    project/
    ├── CMakeLists.txt
    ├── app/
    │   └── main.cpp
    ├── core/
    │   ├── CMakeLists.txt
    │   ├── h/                      # 公開ヘッダ
    │   │   └── core/
    │   │     ├── engine.h
    │   │     └── logger.h 
    │   ├── src/                    # 実装ファイル
    │   │   ├── engine.cpp
    │   │   └── internal.h          # 内部ヘッダ
    │   └── ut/                     # 単体テスト
    │       └── engine_ut.cpp
    └── logger/
        ├── CMakeLists.txt
        ├── h/
        │   └── logger/
        │       └── logger.h
        ├── src/
        │   └── logger.cpp
        └── ut/
            └── logger_ut.cpp
```

## コーディングスタイル <a id="SS_8_9"></a>
### AAAスタイル <a id="SS_8_9_1"></a>
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
  [DRYの原則](#:~:text=Don't%20repeat%20yourself%EF%BC%88DRY,%E3%81%A7%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8%E3%82%92%E5%BC%B7%E8%AA%BF%E3%81%99%E3%82%8B%E3%80%82)
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
 
### east-const <a id="SS_8_9_2"></a>
east-constとは、`const`修飾子を修飾する型要素の右側(east＝右)に置くコーディングスタイルのこと。
つまり「`const`はどの対象を修飾するか」を明確にするため、被修飾対象の直後に const を書くのが特徴である。

このスタイルは、C言語由来の「`const`を左に置く」スタイル([west-const](#SS_8_9_3))に比べ、
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

### west-const <a id="SS_8_9_3"></a>
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

## オブジェクトのコピー <a id="SS_8_10"></a>
### シャローコピー <a id="SS_8_10_1"></a>
シャローコピー(浅いコピー)とは、暗黙的、
もしくは=defaultによってコンパイラが生成するようなcopyコンストラクタ、
copy代入演算子が行うコピーであり、[ディープコピー](#SS_8_10_2)と対比的に使われる概念である。

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

### ディープコピー <a id="SS_8_10_2"></a>
ディープコピーとは、[シャローコピー](#SS_8_10_1)が発生させる問題を回避したコピーである。

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


### スライシング <a id="SS_8_10_3"></a>
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
スライシングが起こった場合、そうならないことが問題である(「[等価性のセマンティクス](#SS_8_5_1)」参照)。

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


## C++注意点 <a id="SS_8_11"></a>
### オーバーライドとオーバーロードの違い <a id="SS_8_11_1"></a>
下記例では、Base::g()がオーバーロードで、Derived::f()がオーバーライドである
(Derived::g()はオーバーロードでもオーバーライドでもない(「[name-hiding](#SS_6_12_9)」参照))。


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
(「[ポリモーフィックなクラス](#SS_6_4_8)」参照)。

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

### danglingリファレンス <a id="SS_8_11_2"></a>
Dangling リファレンスとは、破棄後のオブジェクトを指しているリファレンスを指す。
このようなリファレンスにアクセスすると、[未定義動作](#SS_6_14_3)に繋がるに繋がる。

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

### danglingポインタ <a id="SS_8_11_3"></a>
danglingポインタとは、[danglingリファレンス](#SS_8_11_2)と同じような状態になったポインタを指す。


### Most Vexing Parse <a id="SS_8_11_4"></a>
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

[初期化子リストコンストラクタ](#SS_6_6_1_1)の呼び出しでオブジェクトの初期化を行うことで、
このような問題を回避できる。

## ソフトウェア一般 <a id="SS_8_12"></a>
### ヒープ <a id="SS_8_12_1"></a>
ヒープとは、プログラム実行時に動的メモリ割り当てを行うためのメモリ領域である。
malloc、calloc、reallocといった関数を使用して必要なサイズのメモリを確保し、freeで解放する。
スタックとは異なり、プログラマが明示的にメモリ管理を行う必要があり、解放漏れはメモリリークを引き起こす。
ヒープ領域はスタックよりも大きく、動的なサイズのデータ構造や長寿命のオブジェクトに適しているが、
アクセス速度はスタックより遅い。また、断片化（フラグメンテーション）が発生しやすく、
連続的な割り当てと解放により利用可能なメモリが分散する課題がある。適切なヒープ管理は、
C/C++プログラミングにおける重要なスキルの一つである。

### スレッドセーフ <a id="SS_8_12_2"></a>
スレッドセーフとは「複数のスレッドから同時にアクセスされても、
排他制御などの機構([std::mutex](#SS_7_3_2))により共有データの整合性が保たれ、正しく動作する性質」である。

### リエントラント <a id="SS_8_12_3"></a>
リエントラントとは「実行中に同じ関数が再度呼び出されても、グローバル変数や静的変数に依存せず、
ローカル変数のみで動作するため正しく動作する性質」である。

一般に、リエントラントな関数は[スレッドセーフ](#SS_8_12_2)であるが、逆は成り立たない。


### クリティカルセクション <a id="SS_8_12_4"></a>
複数のスレッドから同時にアクセスされると競合状態を引き起こす可能性があるコード領域をクリティカルセクションと呼ぶ。
典型的には、共有変数や共有データ構造を読み書きするコード部分がこれに該当する。
クリティカルセクションは、[std::mutex](#SS_7_3_2)等の排他制御機構によって保護し、
一度に一つのスレッドのみが実行できるようにする必要がある。

### スピンロック <a id="SS_8_12_5"></a>
スピンロックとは、
スレッドがロックを取得できるまでCPUを占有したままビジーループで待機する排他制御方式である。
スリープを伴わずカーネルを呼び出さないため、短時間の競合では高速に動作するが、
長時間の待機ではCPUを浪費しやすい。リアルタイム処理や割り込み制御に適する。

C++11では、スピンロックは[std::atomic](#SS_7_3_3)を使用して以下のように定義できる。

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

以下の単体テスト(「[std::mutex](#SS_7_3_2)」の単体テストを参照)
に示したように[std::scoped_lock](#SS_7_4_3)のテンプレートパラメータとして使用できる。

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

### ミックスイン <a id="SS_8_12_6"></a>
ミックスインとは、オブジェクト指向プログラミングにおいて、
複数のクラスに対して特定の機能やメソッドを提供するための設計パターンである。
「混ぜ込む（mix in）」という名称が示すとおり、既存のクラスに機能を追加する目的で使用される。

C++では[CRTP(curiously recurring template pattern)](#SS_8_1_4)や通常の継承によってミックスインを実現する。

### ハンドル <a id="SS_8_12_7"></a>
CやC++の文脈でのハンドルとは、ポインタかリファレンスを指す。

### フリースタンディング環境 <a id="SS_8_12_8"></a>
[フリースタンディング環境](https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AA%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E7%92%B0%E5%A2%83)
とは、組み込みソフトウェアやOSのように、その実行にOSの補助を受けられないソフトウエアを指す。

### サイクロマティック複雑度 <a id="SS_8_12_9"></a>
[サイクロマティック複雑度](https://ja.wikipedia.org/wiki/%E5%BE%AA%E7%92%B0%E7%9A%84%E8%A4%87%E9%9B%91%E5%BA%A6)
とは関数の複雑さを表すメトリクスである。


### 凝集性 <a id="SS_8_12_10"></a>
[凝集性(凝集度)](https://ja.wikipedia.org/wiki/%E5%87%9D%E9%9B%86%E5%BA%A6)
とはクラス設計の妥当性を表す尺度の一種であり、
「[凝集性の欠如](#SS_8_12_10_1)(LCOM)」というメトリクスで計測される。

* [凝集性の欠如](#SS_8_12_10_1)メトリクスの値が1に近ければ凝集性は低く、この値が0に近ければ凝集性は高い。
* メンバ変数やメンバ関数が多くなれば、凝集性は低くなりやすい。
* 凝集性は、クラスのメンバがどれだけ一貫した責任を持つかを示す。
* 「[単一責任の原則(SRP)](#SS_2_1)」を守ると凝集性は高くなりやすい。
* 「[Accessor](#SS_8_1_5)」を多用すれば、振る舞いが分散しがちになるため、通常、凝集性は低くなる。
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
(ただし、「[Immutable](#SS_8_1_6)」の観点からは、QuadraticEquation::Set()がない方が良い)。
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

#### 凝集性の欠如 <a id="SS_8_12_10_1"></a>
[凝集性](#SS_8_12_10)の欠如(Lack of Cohesion in Methods/LCOM)とは、
クラス設計の妥当性を表す尺度の一種であり、`0 ～ 1`の値で表すメトリクスである。

LCOMの値が大きい(1か1に近い値)場合、「クラス内のメンバ関数が互いに関連性を持たず、
それぞれが独立した責務やデータに依存するため、クラス全体の統一性が欠けている」ことを表す。

クラスデザイン見直しの基準値としてLCOMを活用する場合、[クラス凝集性のクライテリア](#SS_8_7_3)に具体的な推奨値を示す。

#### LCOM <a id="SS_8_12_10_2"></a>
[凝集性の欠如](#SS_8_12_10_1)とはLack of Cohesion in Methodsの和訳であり、LCOMと呼ばれる。

### Spurious Wakeup <a id="SS_8_12_11"></a>
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

### Static Initialization Order Fiasco(静的初期化順序問題) <a id="SS_8_12_12"></a>
静的初期化順序問題とは、
グローバルや名前空間スコープの静的オブジェクトの初期化順序が翻訳単位間で未定義であることに起因する不具合である。
あるオブジェクトAが初期化時に別のオブジェクトBに依存していても、Bがまだ初期化されていない場合、
Aの初期化は未定義の状態となり、不正アクセスやクラッシュを引き起こす可能性がある。

原因は、C++標準が同じ翻訳単位内の静的オブジェクトの初期化順序は保証するが、
異なる翻訳単位間の順序は保証しないことにある。さらに、動的初期化を必要とするオブジェクトでは、
初期化順序の依存関係が問題を起こす。

C++20からこの問題の対策として、[constinit](#SS_6_5_8)が導入された。

### 副作用 <a id="SS_8_12_13"></a>
プログラミングにおいて、式の評価による作用には、
主たる作用とそれ以外の
[副作用](https://ja.wikipedia.org/wiki/%E5%89%AF%E4%BD%9C%E7%94%A8_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0))
(side effect)とがある。
式は、評価値を得ること(関数では「引数を受け取り値を返す」と表現する)が主たる作用とされ、
それ以外のコンピュータの論理的状態(ローカル環境以外の状態変数の値)を変化させる作用を副作用という。
副作用の例としては、グローバル変数や静的ローカル変数の変更、
ファイルの読み書き等のI/O実行、等がある。


### Itanium C++ ABI <a id="SS_8_12_14"></a>
ItaniumC++ABIとは、C++コンパイラ間でバイナリ互換性を確保するための規約である。
関数呼び出し規約、クラスレイアウト、仮想関数テーブル、例外処理、
名前修飾(マングリング)などC++のオブジェクト表現と呼び出し方法に関する標準ルールを定めている。

もともとはIntelItanium(IA-64)プロセッサ向けに策定されたが、
[g++](#SS_8_13_1)や[clang++](#SS_8_13_2)はx86/x86-64やARM64など多くのプラットフォームでもItaniumC++ABI準拠の規約を採用している。
そのため異なるコンパイラ間でもオブジェクトファイルやライブラリのリンクが可能である。
また、typeid(...).name()をデマングルした場合、
constがeast-const形式(T const)で表示されるのもこのABIの規約によるものである。

| ABI               | 主な対象プラットフォーム  | マングリング規則    | クラスレイアウト  | 例外処理    |
| ----------------- | ------------------------- | ------------------- | ----------------- | ----------- |
| **ItaniumC++ABI** | IA-64, x86, x86-64, ARM64 | east-const形式      | Itanium規則       | Itanium規則 |
| **MSVC C++ABI**   | Windows x86/x64           | 独自形式            | 独自規則          | 独自規則    |
| **ARM C++ABI**    | AArch32, AArch64          | 基本的にItanium準拠だが例外あり         | ARM規則     |


## C++コンパイラ <a id="SS_8_13"></a>
本ドキュメントで使用するg++/clang++のバージョンは以下のとおりである。

### g++ <a id="SS_8_13_1"></a>
```
    g++ (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
    Copyright (C) 2021 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### clang++ <a id="SS_8_13_2"></a>
```
    Ubuntu clang version 14.0.0-1ubuntu1
    Target: x86_64-pc-linux-gnu
    Thread model: posix
    InstalledDir: /usr/bin
```

## 非ソフトウェア用語 <a id="SS_8_14"></a>
### セマンティクス <a id="SS_8_14_1"></a>
シンタックスとは構文論のことであり、セマンティクスとは意味論のことである。
セマンティクス、シンタックスの違いをはっきりと際立たせる以下の有名な例文により、
セマンティクスの意味を直感的に理解することができる。

```
    Colorless green ideas sleep furiously(直訳:無色の緑の考えが猛烈に眠る)
```

この文は文法的には正しい(シンタックス的に成立している)が、意味的には不自然で理解不能である
(セマンティクス的には破綻している)。ノーム・チョムスキーによって提示されたこの例文は、
構文が正しくても意味が成立しないことがあるという事実を示しており、構文と意味の違いを鮮やかに浮かび上がらせる。


### 割れ窓理論 <a id="SS_8_14_2"></a>
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


### 車輪の再発明 <a id="SS_8_14_3"></a>
[車輪の再発明](https://ja.wikipedia.org/wiki/%E8%BB%8A%E8%BC%AA%E3%81%AE%E5%86%8D%E7%99%BA%E6%98%8E)
とは、広く受け入れられ確立されている技術や解決法を（知らずに、または意図的に無視して）
再び一から作ること」を指すための慣用句である。
ソフトウェア開発では、STLのような優れたライブラリを使わずに、
それと同様なライブラリを自分たちで実装するような非効率な様を指すことが多い。



<!-- ./md/sample_code.md -->
# Sample Code <a id="SS_9"></a>
## C++ <a id="SS_9_1"></a>
### example/dynamic_memory_allocation/malloc_ut.cpp <a id="SS_9_1_1"></a>
```cpp
          1 #include <sys/unistd.h>
          2 
          3 #include <cassert>
          4 #include <cstdint>
          5 #include <mutex>
          6 
          7 #include "gtest_wrapper.h"
          8 
          9 #include "dynamic_memory_allocation_ut.h"
         10 #include "spin_lock.h"
         11 #include "utils.h"
         12 
         13 // @@@ sample begin 0:0
         14 
         15 extern "C" void* sbrk(ptrdiff_t __incr);
         16 // @@@ sample end
         17 
         18 namespace MallocFree {
         19 // @@@ sample begin 1:0
         20 
         21 namespace {
         22 
         23 struct header_t {
         24     header_t* next;
         25     size_t    n_units;  // header_tが何個あるか
         26 };
         27 
         28 header_t*        header{nullptr};
         29 SpinLock         spin_lock{};
         30 constexpr size_t unit_size{sizeof(header_t)};
         31 
         32 inline bool sprit(header_t* header, size_t n_units, header_t*& next) noexcept
         33 {
         34     // @@@ ignore begin
         35     assert(n_units > 1);  // ヘッダとバッファなので最低でも2
         36 
         37     next = nullptr;
         38 
         39     if (header->n_units == n_units || header->n_units == n_units + 1) {
         40         next = header->next;
         41         return true;
         42     }
         43     else if (header->n_units > n_units) {
         44         next            = header + n_units;
         45         next->n_units   = header->n_units - n_units;
         46         next->next      = header->next;
         47         header->n_units = n_units;
         48         return true;
         49     }
         50 
         51     return false;
         52     // @@@ ignore end
         53 }
         54 
         55 inline void concat(header_t* front, header_t* rear) noexcept
         56 {
         57     // @@@ ignore begin
         58     if (front + front->n_units == rear) {  // 1枚のメモリになる
         59         front->n_units += rear->n_units;
         60         front->next = rear->next;
         61     }
         62     else {
         63         front->next = rear;
         64     }
         65     // @@@ ignore end
         66 }
         67 
         68 header_t* set_back(void* mem) noexcept { return static_cast<header_t*>(mem) - 1; }
         69 
         70 static_assert(sizeof(header_t) == alignof(std::max_align_t));
         71 
         72 void* malloc_inner(size_t size) noexcept
         73 {
         74     // @@@ ignore begin
         75     // size分のメモリとヘッダ
         76     auto n_units = (Roundup(unit_size, size) / unit_size) + 1;
         77     auto lock    = std::lock_guard{spin_lock};
         78 
         79     auto curr = header;
         80     for (header_t* prev = nullptr; curr != nullptr; prev = curr, curr = curr->next) {
         81         header_t* next;
         82 
         83         if (!sprit(curr, n_units, next)) {
         84             continue;
         85         }
         86 
         87         if (prev == nullptr) {
         88             header = next;
         89         }
         90         else {
         91             prev->next = next;
         92         }
         93         break;
         94     }
         95 
         96     if (curr != nullptr) {
         97         ++curr;
         98     }
         99 
        100     return curr;
        101     // @@@ ignore end
        102 }
        103 }  // namespace
        104 // @@@ sample end
        105 // @@@ sample begin 2:0
        106 
        107 void free(void* mem) noexcept
        108 {
        109     header_t* mem_to_free = set_back(mem);
        110 
        111     mem_to_free->next = nullptr;
        112 
        113     auto lock = std::lock_guard{spin_lock};
        114 
        115     if (header == nullptr) {
        116         header = mem_to_free;
        117         return;
        118     }
        119     // @@@ sample end
        120     // @@@ sample begin 2:1
        121 
        122     if (mem_to_free < header) {
        123         concat(mem_to_free, header);
        124         header = mem_to_free;
        125         return;
        126     }
        127 
        128     auto curr = header;
        129     for (; curr->next != nullptr; curr = curr->next) {
        130         if (mem_to_free < curr->next) {  // 常に curr < mem_to_free
        131             concat(mem_to_free, curr->next);
        132             concat(curr, mem_to_free);
        133             return;
        134         }
        135     }
        136 
        137     concat(curr, mem_to_free);
        138     // @@@ sample end
        139     // @@@ sample begin 2:2
        140 }
        141 // @@@ sample end
        142 // @@@ sample begin 3:0
        143 
        144 void* malloc(size_t size) noexcept
        145 {
        146     void* mem = malloc_inner(size);
        147     // @@@ sample end
        148     // @@@ sample begin 3:1
        149 
        150     if (mem == nullptr) {
        151         auto const add_size = Roundup(unit_size, 1024 * 1024 + size);  // 1MB追加
        152 
        153         header_t* add = static_cast<header_t*>(sbrk(add_size));
        154         add->n_units  = add_size / unit_size;
        155         free(++add);
        156         mem = malloc_inner(size);
        157     }
        158     // @@@ sample end
        159     // @@@ sample begin 3:2
        160 
        161     return mem;
        162 }
        163 // @@@ sample end
        164 
        165 namespace {
        166 TEST(NewDelete_Opt, malloc)
        167 {
        168     {
        169         void* mem = malloc(1024);
        170 
        171         ASSERT_NE(nullptr, mem);
        172         free(mem);
        173 
        174         void* ints[8]{};
        175 
        176         constexpr auto n_units = Roundup(unit_size, unit_size + sizeof(int)) / unit_size;
        177 
        178         for (auto& i : ints) {
        179             i = malloc(sizeof(int));
        180 
        181             header_t* h = set_back(i);
        182             ASSERT_EQ(h->n_units, n_units);
        183         }
        184 
        185         for (auto& i : ints) {
        186             free(i);
        187         }
        188     }
        189 
        190     // @@@ sample begin 4:0
        191 
        192     void* mem[1024];
        193 
        194     for (auto& m : mem) {  // 32バイト x 1024個のメモリ確保
        195         m = malloc(32);
        196     }
        197 
        198     // memを使用した何らかの処理
        199     // @@@ ignore begin
        200     // @@@ ignore end
        201 
        202     for (auto i = 0U; i < ArrayLength(mem); i += 2) {  // 512個のメモリを解放
        203         free(mem[i]);
        204     }
        205     // @@@ sample end
        206 
        207     for (auto i = 1U; i < ArrayLength(mem); i += 2) {
        208         free(mem[i]);
        209     }
        210 }
        211 }  // namespace
        212 }  // namespace MallocFree
```

### example/dynamic_memory_allocation/mpool_variable.h <a id="SS_9_1_2"></a>
```cpp
          1 #pragma once
          2 #include <cassert>
          3 #include <cstdint>
          4 #include <mutex>
          5 #include <optional>
          6 
          7 #include "mpool.h"
          8 #include "spin_lock.h"
          9 #include "utils.h"
         10 
         11 namespace Inner_ {
         12 
         13 struct header_t {
         14     header_t* next;
         15     size_t    n_units;  // header_tが何個あるか
         16 };
         17 
         18 constexpr auto unit_size = sizeof(header_t);
         19 
         20 inline std::optional<header_t*> sprit(header_t* header, size_t n_units) noexcept
         21 {
         22     assert(n_units > 1);  // ヘッダとバッファなので最低でも2
         23 
         24     if (header->n_units == n_units || header->n_units == n_units + 1) {
         25         return header->next;
         26     }
         27     else if (header->n_units > n_units) {
         28         auto next       = header + n_units;
         29         next->n_units   = header->n_units - n_units;
         30         next->next      = header->next;
         31         header->n_units = n_units;
         32         return next;
         33     }
         34 
         35     return std::nullopt;
         36 }
         37 
         38 inline void concat(header_t* front, header_t* rear) noexcept
         39 {
         40     if (front + front->n_units == rear) {  // 1枚のメモリになる
         41         front->n_units += rear->n_units;
         42         front->next = rear->next;
         43     }
         44     else {
         45         front->next = rear;
         46     }
         47 }
         48 
         49 inline header_t* set_back(void* mem) noexcept { return static_cast<header_t*>(mem) - 1; }
         50 
         51 static_assert(sizeof(header_t) == alignof(std::max_align_t));
         52 
         53 template <uint32_t MEM_SIZE>
         54 struct buffer_t {
         55     alignas(std::max_align_t) uint8_t buffer[Roundup(sizeof(header_t), MEM_SIZE)];
         56 };
         57 }  // namespace Inner_
         58 
         59 // @@@ sample begin 0:0
         60 
         61 template <uint32_t MEM_SIZE>
         62 class MPoolVariable final : public MPool {
         63 public:
         64     // @@@ sample end
         65     // @@@ sample begin 0:1
         66     MPoolVariable() noexcept : MPool{MEM_SIZE}
         67     {
         68         header_->next    = nullptr;
         69         header_->n_units = sizeof(buff_) / Inner_::unit_size;
         70     }
         71     // @@@ sample end
         72     // @@@ sample begin 0:2
         73 
         74     class const_iterator {
         75     public:
         76         explicit const_iterator(Inner_::header_t const* header) noexcept : header_{header} {}
         77         const_iterator(const_iterator const&) = default;
         78         const_iterator(const_iterator&&)      = default;
         79 
         80         const_iterator& operator++() noexcept  // 前置++のみ実装
         81         {
         82             assert(header_ != nullptr);
         83             header_ = header_->next;
         84 
         85             return *this;
         86         }
         87 
         88         Inner_::header_t const* operator*() noexcept { return header_; }
         89 
         90         // clang-format off
         91 
         92     #if __cplusplus <= 201703L  // c++17
         93         bool operator==(const_iterator const& rhs) noexcept { return header_ == rhs.header_; }
         94         bool operator!=(const_iterator const& rhs) noexcept { return !(*this == rhs); }
         95     #else  // c++20
         96 
         97         auto operator<=>(const const_iterator&) const = default;
         98     #endif
         99         // clang-format on
        100 
        101     private:
        102         Inner_::header_t const* header_;
        103     };
        104 
        105     const_iterator begin() const noexcept { return const_iterator{header_}; }
        106     const_iterator end() const noexcept { return const_iterator{nullptr}; }
        107     const_iterator cbegin() const noexcept { return const_iterator{header_}; }
        108     const_iterator cend() const noexcept { return const_iterator{nullptr}; }
        109     // @@@ sample end
        110     // @@@ sample begin 0:3
        111 
        112 private:
        113     using header_t = Inner_::header_t;
        114 
        115     Inner_::buffer_t<MEM_SIZE> buff_{};
        116     header_t*                  header_{reinterpret_cast<header_t*>(buff_.buffer)};
        117     mutable SpinLock           spin_lock_{};
        118     size_t                     unit_count_{sizeof(buff_) / Inner_::unit_size};
        119     size_t                     unit_count_min_{sizeof(buff_) / Inner_::unit_size};
        120 
        121     virtual void* alloc(size_t size) noexcept override
        122     {
        123         // @@@ ignore begin
        124         // size分のメモリとヘッダ
        125         auto n_units = (Roundup(Inner_::unit_size, size) / Inner_::unit_size) + 1;
        126 
        127         auto lock = std::lock_guard{spin_lock_};
        128 
        129         auto curr = header_;
        130 
        131         for (header_t* prev{nullptr}; curr != nullptr; prev = curr, curr = curr->next) {
        132             auto opt_next = std::optional<header_t*>{sprit(curr, n_units)};
        133 
        134             if (!opt_next) {
        135                 continue;
        136             }
        137 
        138             auto next = *opt_next;
        139             if (prev == nullptr) {
        140                 header_ = next;
        141             }
        142             else {
        143                 prev->next = next;
        144             }
        145             break;
        146         }
        147 
        148         if (curr != nullptr) {
        149             unit_count_ -= curr->n_units;
        150             unit_count_min_ = std::min(unit_count_, unit_count_min_);
        151             ++curr;
        152         }
        153 
        154         return curr;
        155         // @@@ ignore end
        156     }
        157 
        158     virtual void free(void* mem) noexcept override
        159     {
        160         // @@@ ignore begin
        161         header_t* to_free = Inner_::set_back(mem);
        162 
        163         to_free->next = nullptr;
        164 
        165         auto lock = std::lock_guard{spin_lock_};
        166 
        167         unit_count_ += to_free->n_units;
        168         unit_count_min_ = std::min(unit_count_, unit_count_min_);
        169 
        170         if (header_ == nullptr) {
        171             header_ = to_free;
        172             return;
        173         }
        174 
        175         if (to_free < header_) {
        176             concat(to_free, header_);
        177             header_ = to_free;
        178             return;
        179         }
        180 
        181         header_t* curr = header_;
        182 
        183         for (; curr->next != nullptr; curr = curr->next) {
        184             if (to_free < curr->next) {  // 常に curr < to_free
        185                 concat(to_free, curr->next);
        186                 concat(curr, to_free);
        187                 return;
        188             }
        189         }
        190 
        191         concat(curr, to_free);
        192         // @@@ ignore end
        193     }
        194 
        195     virtual size_t get_size() const noexcept override { return 1; }
        196     virtual size_t get_count() const noexcept override { return unit_count_ * Inner_::unit_size; }
        197     virtual size_t get_count_min() const noexcept override { return unit_count_min_ * Inner_::unit_size; }
        198 
        199     virtual bool is_valid(void const* mem) const noexcept override
        200     {
        201         return (&buff_ < mem) && (mem < &buff_.buffer[ArrayLength(buff_.buffer)]);
        202     }
        203     // @@@ sample end
        204     // @@@ sample begin 0:4
        205 };
        206 // @@@ sample end
```



