<!-- ./md/solid.md -->
# SOLID <a id="SS_5"></a>
SOLIDとは、オブジェクト指向(OOD/OOP)プログラミングにおいて特に重要な下記の5つの原則である。

* [単一責任の原則(SRP)](solid.md#SS_5_1)
* [オープン・クローズドの原則(OCP)](solid.md#SS_5_2)
* [リスコフの置換原則(LSP)](solid.md#SS_5_3)
* [インターフェース分離の原則(ISP)](solid.md#SS_5_4)
* [依存関係逆転の原則(DIP)](solid.md#SS_5_5)

[インデックス](essential_intro.md#SS_1_2)に戻る。  

___

## 単一責任の原則(SRP) <a id="SS_5_1"></a>
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


## オープン・クローズドの原則(OCP) <a id="SS_5_2"></a>
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
後述する「[依存関係逆転の原則(DIP)](solid.md#SS_5_5)」にも反している。

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
(実際には、TransactorIFから派生する具象クラスの生成用Factory関数(「[Factory](design_pattern.md#SS_6_17)」参照)
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
[Pimpl](design_pattern.md#SS_6_3)のようにラッピングを使用するパターンも有用である。


## リスコフの置換原則(LSP) <a id="SS_5_3"></a>
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
ところが実際にはオブジェクトの[スライシング](cpp_idioms.md#SS_4_7_3)という別の問題を引き起こす。  

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


## インターフェース分離の原則(ISP) <a id="SS_5_4"></a>
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


## 依存関係逆転の原則(DIP) <a id="SS_5_5"></a>
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


## まとめ <a id="SS_5_6"></a>
以上で述べたように、SOLIDはオブジェクト指向(OOD/OOP)プログラミングにおいて極めて重要な原則である。
この逸脱はソースコードを劣化させ、ソフトウェアの品質低下や開発費増大に直結するため、
厳守することが求められる。



