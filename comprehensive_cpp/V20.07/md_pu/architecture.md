<!-- ./md/architecture.md -->
# アーキテクチャ <a id="SS_10"></a>
この章ではソフトウェアアーキテクチャについて考察する。

以下の[wikipedia](https://ja.wikipedia.org/wiki/%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3)
からの引用にあるように、

```
    ソフトウェアアーキテクチャ（英: Software Architecture）は、
    ソフトウェアコンポーネント、それらの外部特性、またそれらの相互関係から構成される。
    また、この用語はシステムのソフトウェアアーキテクチャの文書化を意味することもある。 

    ... 中略 ...

    ただし、今までのところ、「ソフトウェアアーキテクチャ」という用語に関して、
    万人が合意した厳密な定義は存在しない。
```

プログラマは、ソフトウェアアーキテクチャ(以下、単にアーキテクチャ)について、
ある一定のイメージを持っているが、一元的な概念としては捉えていないと思われる。
したがって、アーキテクチャについて語る前に、ここで定義を明確にしておく必要がある。

このドキュメントの内容はアカデミックなものではなく、
日々行われるC++での開発の実践に即したものになるように努めてきたため、
アーキテクチャの定義もそのようになるべきだろう。

商業的に成功したソフトウェアは開発が継続され、その期間は10年を超えることが珍しくない。
そういった事情から、多くのプログラマには開発初期からソフトウェアを作った経験はなく、
その結果、開発前段で行われるアーキテクチャへの考察を行った経験もない。

このように考えると、彼らにとってのアーキテクチャは、目の前のソースコードが作り出す構造となるだろう。
目の前のソースコードが作り出す構造になるだろう。

___

__この章の構成__

&emsp;&emsp; [アーキテクチャの定義](architecture.md#SS_10_1)  
&emsp;&emsp; [アーキテクチャの設計](architecture.md#SS_10_2)  
&emsp;&emsp;&emsp; [パッケージ図例](architecture.md#SS_10_2_1)  
&emsp;&emsp;&emsp; [シーケンス図例](architecture.md#SS_10_2_2)  

&emsp;&emsp; [アーキテクチャとファイル構造](architecture.md#SS_10_3)  
&emsp;&emsp;&emsp; [Modelの非同期処理](architecture.md#SS_10_3_1)  
&emsp;&emsp;&emsp; [Viewの非同期処理](architecture.md#SS_10_3_2)  

&emsp;&emsp; [アーキテクチャの見直し](architecture.md#SS_10_4)  
&emsp;&emsp;&emsp; [パッケージが大きくなりすぎる](architecture.md#SS_10_4_1)  
&emsp;&emsp;&emsp; [当初、想定していない依存関係が必要になる](architecture.md#SS_10_4_2)  
&emsp;&emsp;&emsp; [コードクローンが避けられない](architecture.md#SS_10_4_3)  
&emsp;&emsp;&emsp; [当初、想定していない非同期処理が必要になる](architecture.md#SS_10_4_4)  

&emsp;&emsp; [アーキテクチャの再構築](architecture.md#SS_10_5)  
&emsp;&emsp;&emsp; [アーキテクチャ再構築の準備](architecture.md#SS_10_5_1)  
&emsp;&emsp;&emsp; [アーキテクチャ再構築のチーム編成](architecture.md#SS_10_5_2)  
&emsp;&emsp;&emsp; [アーキテクチャ再構築の手順](architecture.md#SS_10_5_3)  
  
  
  
[このドキュメントの構成](introduction.md#SS_1_7)に戻る。  

___

## アーキテクチャの定義 <a id="SS_10_1"></a>
以上の考察からここでのアーキテクチャやそれにまつわる概念を以下のように定義する。

* アーキテクチャとは「ソースコードをいくつかに分割したパッケージと、それらの依存関係」を指す。
* パッケージとは、ソフトウェア構成要素（型、関数、enum、定数、変数など）の集まりを指し、通常、
  ディレクトリ単位で管理される。
  パッケージはライブラリ（\*.lib、\*.dll、\*.a、\*.so等）を生成することが一般的である。
  また、サブパッケージを持つこともある。
* パッケージの依存関係とは、あるパッケージが別のパッケージの構成要素を使用していること、
  もしくは使用していないことを指す。
  従って「パッケージAがパッケージBに依存する」とは、
  パッケージAがパッケージBの構成要素を使用していることを指す。
  UMLでは、この依存関係を下記のように表す。

```plant_uml/dependency.pu
@startuml
scale max 730 width
rectangle "app" as app
rectangle "dependency" as dependency
rectangle "file_utils" as file_utils
rectangle "lib" as lib
rectangle "logging" as logging

app "1" -[#green]-> dependency
app "4" -[#green]-> file_utils
app "3" -[#green]-> lib
app "1" -[#green]-> logging
dependency "24" -[#green]-> file_utils
dependency "4" -[#green]-> lib
file_utils "1" -[#green]-> lib
file_utils "1" -[#green]-> logging
logging "3" -[#green]-> lib

@enduml
```

この定義により、アーキテクチャはUMLのパッケージ図/クラス図を使って視覚化できる。

## アーキテクチャの設計 <a id="SS_10_2"></a>
アーキテクチャ設計は、以下のような思考プロセスを繰り返すことで進められる。

1. 要求仕様を理解する。
2. 要求仕様からアーキテクチャに強い影響を与えると予想される下記のような要素について考察する。
    * OS(windows、linux、RTOS、OSを使わない等)は何か?
    * 外部のコンポーネント(GUI等のフレームワークや、データベース等)を使用するか?
    * 並行・並列処理は必要か?
    * 非同期処理はあるか
      (GUIを含む非同期処理インターフェースを持つアプリケーションには
      [MVC](design_pattern.md#SS_9_23)系のアーキテクチャが適していることが多い)?
    * その非同期処理にアボートや、サスペンド/レジュームは必要か?

3. 非機能要件を掘り起こす。
    * 拡張性、セキュリティのレベル、トラブル解析機能、性能
    * 開発の効率化のための[ログの取得](debug.md#SS_15_6_1)機能や[モニター](debug.md#SS_15_6_2)
    * テストの自動化(「[アジャイル系プロセスのプラクティスとインフラ](process_and_infra.md#SS_11_2)」参照)

4. 下記を考慮したパッケージを定義し、上記の内容を分割して、パッケージに割り当てる。
    * 各パッケージの責務
    * パケージ間の依存関係

5. 下記のようなシナリオのプロトタイピングをする。
    * なるべく多くのパッケージを使用する含むシナリオ
    * アーキテクチャに強い影響を与える(非同期処理やそのアボート等)シナリオ

この繰り返しの中で、新たな要求仕様や非機能要件が見つかることはよくあることである。
その場合、当然その新規要件も要求仕様書に書き加える。

上記4の成果物として、下記のようなパッケージ図/クラス図を作る。
この場合のクラスは、概念を表すためのものであるため、
各パッケージの代表的なもののみを記述すればよい。

### パッケージ図例 <a id="SS_10_2_1"></a>

```plant_uml/arch_pkg_example.pu
@startuml
package Model as ModelPkg {
    class Model {
        notify()
    }

    class Observer {
        Update(const& Model);
    }
}

package Controller as ControllerPkg {
    class Controller
}

package View as ViewPkg {
    class View {
        Update(const& Model);
    }
}

package GuiFrameWork { }

View -up-|> Observer
Model-left->Observer
Controller->Model
View->GuiFrameWork
Controller->GuiFrameWork

@enduml


```

この時点で、パッケージ間に相互依存や循環依存があれば、
まず間違いなくそのアーキテクチャは使い物にならないため再考する。

[コンウェイの法則](software_practice.md#SS_2_9)で述べたように、
「組織に属する者はその組織構造を投射したアーキテクチャが正しいと思ってしまうバイアスを持つ」
ことに注意することも必要である。

このフェーズでパッケージの名前が決定されるが、適切な名前を選ぶことは大変難しい。
最適と思えるものが思い浮かばなければ、
後から修正することを前提に適当な名前を付けることがベストな戦略となり得るが、
パッケージの概念が固まっていない証拠ともなり得るため、難しい判断が求められる。

上記5の成果物として、
プロトタイピングで使用したシナリオを表す下記のような概念的なシーケンス図やアクティビティ図等を作る。

### シーケンス図例 <a id="SS_10_2_2"></a>

```plant_uml/arch_seq_example.pu
@startuml

actor "User" as user 

user            ->  GuiFrameWork    : "OK"をクリック
GuiFrameWork    ->  Controller      : 通知
Controller      ->  Model           : 命令の実行
View            <<- Model           : 命令完了後、状態変更の通知
View            ->  Model           : 表示データの取得
View            ->  GuiFrameWork    : 描画命令
user            <-  GuiFrameWork    : 表示

@enduml
```

上記のようなダイアグラムは、

* 繰り返し修正する
* 概念を表すことが目的である

ため、

* 詳細なものを作るのは時間の無駄である。
* 修正前後の違いが簡単にわかるものでなければならない
  (修正前後の違いがdiffで簡単に表示できるため、当ドキュメントでのダイアグラムの記述には、
  [plant uml](http://www.plantuml.com/)を使用している)。

このようにしなければ、ダイアグラムのドローイング作業は無限に工数を吸収する沼となるだろう。

上記のステップを複数回、試行することにで、いくつかのプロトタイプコードが出来る。
この試行は[アジャイル系プロセス](process_and_infra.md#SS_11_1_2)と相性が良い。
一方で、[ウォーターフォールモデル、V字モデル](process_and_infra.md#SS_11_1_1)や、プロセスを決めない試行は、
沼にはまり込み大きく時間をロスする可能性が高い。

[deps](deps.md#SS_17)等のリバースエンジニアリングツールを使用し、
プロトタイプコードから生成したパッケージ図/クラス図が、
上記5の最終版のパッケージ図/クラス図と一致するのであれば、
一旦アーキテクチャの設計は終了し次のフェーズに進む。

## アーキテクチャとファイル構造 <a id="SS_10_3"></a>
プロトタイピングで開発したコードやビルドツールの設定を開発の起点にするためには、
下記のような、もうひと手間が必要である。

* プロトタイプコードが「[パッケージとその構成ファイル](programming_convention.md#SS_3_7)」で述べた規則に沿うように修正する。
* パッケージをライブラリ(\*.lib、\*.dll、\*.a、\*.so等)としてビルドできるように、
  make等のビルドツールを修正する。
* パッケージから生成されたライブラリに対する単体テストを作る。
  単体テストは各パッケージごとに実行形式ファイルを生成できるようにビルドツールを修正する。
  これにより[自動単体テスト](process_and_infra.md#SS_11_2_1)が実行できるようになる。

この作業の完了時、パッケージ図は下記のようになっているだろう。

```
    architecture
    ├── CMakeLists.txt
    ├── app
    │   └── main.cpp
    ├── controller
    │   ├── CMakeLists.txt              # controller.aのビルドcmake
    │   ├── h
    │   │   └── controller
    │   │       └── controller.h        # controller.aの機能の公開ヘッダ
    │   ├── src                         # controller.aの実装ファイル(*.h *.cpp)
    │   │   └── controller.cpp
    │   └── ut                          # controller.aの単体テスト
    │       └── controller_ut.cpp
    ├── model
    │   ├── CMakeLists.txt              # model.aのビルドcmake
    │   ├── h                           # model.aの機能の公開ヘッダ 
    │   │   └── model
    │   │       ├── model.h
    │   │       └── observer.h
    │   ├── src                         # model.aの実装ファイル(*.h *.cpp)
    │   │   ├── model.cpp
    │   │   └── observer.cpp
    │   │   └── x.cpp
    │   │   └── x.h
    │   └── ut                          # model.aの単体テスト
    │       └── model_ut.cpp
    └── view
        ├── CMakeLists.txt              # view.aのビルドcmake
        ├── h                           # view.aの機能の公開ヘッダ 
        │   └── view
        │       └── view.h
        ├── src                         # view.aの実装ファイル(*.h *.cpp)
        │   └── view.cpp
        └── ut                          # view.aの単体テスト
            └── view_ut.cpp
```

h/<パケージ名>に配置されたヘッダファイルは、
パッケージの外部からアクセスできるソフトウェア構成物を宣言、
定義する。その他に配置されたヘッダファイルは、パッケージ自身の実装用か、単体テスト用である。
ここで例示したアプリケーションは[MVC](design_pattern.md#SS_9_23)構造であるため、
ディレクトリの依存関係は、下記の様になるはずである。

```plant_uml/arch_dir_dep.pu
@startuml

rectangle app {
    rectangle  src as app_src
}

rectangle controller {
    rectangle  "h" as controller_h
    rectangle  src as controller_src
    rectangle  ut as controller_ut
}

rectangle model {
    rectangle  "h" as model_h
    rectangle  src as model_src
    rectangle  ut as model_ut
}

rectangle view {
    rectangle  "h" as view_h
    rectangle  src as view_src
    rectangle  ut as view_ut
}


app_src         -[#green]down-> controller_h
app_src         -[#green]down-> model_h
app_src         -[#green]down-> view_h

controller_src  -[#green]up-> controller_h
controller_h    -[#green]up-> model_h
controller_ut   -[#green]up-> controller_h

model_src       -[#green]up-> model_h
model_ut        -[#green]up-> model_h

view_src        -[#green]up-> view_h
view_h          -[#green]up-> model_h
view_ut         -[#green]up-> view_h


@enduml

```

循環や相互依存が残ってしまう場合、「[SOLID](solid.md#SS_8)」に記載したコードのパターンや
「[デザインパターン](design_pattern.md#SS_9)」が役立つはずである。

[#includeで指定するパス名](programming_convention.md#SS_3_7_7)でのルールに従うことで、パケージの依存関係は、

```cpp
    //  example/architecture/model/src/model.cpp 6

    #include <iterator>  // stdの使用

    #include "./x.h"             // ローカルヘッダの使用
    #include "logging/logger.h"  // logger.aの使用
    #include "model/model.h"     // model.aの使用
```

のようにコードに投影されるため、メンテナンス性や可読性が向上する。

従って、
各ライブラリのビルド毎にインクルードパスを設定できないようなビルドツールやIDEを使うべきではない
(「[エディタ/IDE](dev_tools.md#SS_16_3)」参照)。

### Modelの非同期処理 <a id="SS_10_3_1"></a>
前記した[パッケージ図例](architecture.md#SS_10_2_1)、[シーケンス図例](architecture.md#SS_10_2_2)で示した通り、
GUIのボタン押下などによるControllerの呼び出しから、
呼び出されるModelオブジェクトのメンバ関数は非同期処理となることが求められることが多い。
このため、Modelクラスの構造はアクティブオブジェクトを生成できるようにスレッドを内包することになる。
こういった構造は定型となるため、そのコードを以下に例示する。

```cpp
    //  example/architecture/model/h/model/model.h 15

    class Model {
    public:
        class Observer {
        public:
            virtual void Update(Model const& model) = 0;
            virtual ~Observer()                     = default;
        };

        struct msg_t {
            msg_t() : exec([] {}) {}
            msg_t(std::function<void()> exec) : exec{std::move(exec)} {}
            std::function<void()> exec;
        };

        Model() : worker_{&Model::worker_function, this} {}
        ~Model();

        bool ExecAsync(std::function<void()> exec);  // 非同期リクエスト
        bool IsBusy() const noexcept { return busy_; }

        void Sync();  // 非同期要求の完了待ち
        void Attach(std::unique_ptr<Observer>&& observer);

    private:
        std::thread       worker_;            // 非同期処理を実現するためのワーカスレッド
        std::atomic<bool> busy_ = false;      // ExecAsyncを受け付けるか否か
        std::atomic<bool> stop_ = false;      // worker_functionの終了変数
        void              worker_function();  // スレッドのメイン関数。msg_cv_でウエイト
        void              notify();           // observer::Updateの呼び出し

        std::list<Model::msg_t> msgs_{};     // 非同期要求はmsg_tとしてリスト化される
        std::mutex              msg_mtx_{};  // リスト処理の競合の保護
        std::condition_variable msg_cv_{};   // msgs_に追加されたことの通知

        std::list<std::unique_ptr<Model::Observer>> observers_{};
    };
```

Modelクラスに[Pimpl](design_pattern.md#SS_9_3)を適用することでこのクラスの内部構造を隠蔽した方が良い場合もあるが、
ここでは例示するコードを単純にすることを優先する。

非同期処理のためのコードを以下に示す。

```cpp
    //  example/architecture/model/src/model.cpp 34

    bool Model::ExecAsync(std::function<void()> exec)  // Modelに対する非同期要求
    {
        // 非同期要求のキューイングはしないが、キューイング可能に変更は容易
        if (busy_) {
            return false;
        }

        {
            std::unique_lock<std::mutex> lock{msg_mtx_};
            msgs_.emplace_back(std::move(exec));
            busy_ = true;
        }
        msg_cv_.notify_one();

        return true;
    }
```

```cpp
    //  example/architecture/model/src/model.cpp 53

    void Model::worker_function()  // スレッドのメイン関数
    {
        for (;;) {
            msg_t msg;
            {
                std::unique_lock<std::mutex> lock{msg_mtx_};
                msg_cv_.wait(lock, [&msgs = msgs_, &stop = stop_] { return !msgs.empty() || stop; });
                if (stop_ && msgs_.empty()) {
                    return;
                }

                msg = std::move(msgs_.front());
                msgs_.pop_front();
            }

            msg.exec();  // ExecAsync(exec)で渡された関数オブジェクトの非同期呼び出し
            busy_ = false;

            notify();  // オブザーバーへの通知処理
        }
    }
```

```cpp
    //  example/architecture/model/src/model.cpp 77

    void Model::Attach(std::unique_ptr<Observer>&& observer)  // オブザーバーのアタッチ
    {
        observers_.emplace_back(std::move(observer));
    }

    void Model::notify()
    {
        for (auto const& observer : observers_) {
            observer->Update(*this);
        }
    }
```


以下に、単体テストによりModelの動作を示す。

```cpp
    //  example/architecture/model/ut/model_ut.cpp 17

    class TestObserver : public Model::Observer {  // テスト用オブザーバー
    public:
        void          Update(const Model& model) override { ++update_counter_; }
        std::uint32_t update_counter_ = 0;
    };
```
```cpp
    //  example/architecture/model/ut/model_ut.cpp 28

    Model         model{};
    int           exec_counter{};
    TestObserver* to = new TestObserver;  // 下のunique_ptrで管理

    model.Attach(std::unique_ptr<TestObserver>{to});  // オブザーバの登録

    ASSERT_FALSE(model.IsBusy());  // ビジーでないことの確認

    model.ExecAsync([&exec_counter]() {  // 非同期要求のテスト開始
        ++exec_counter;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        LOGGER("in ExecAsync");
    });

    ASSERT_TRUE(model.IsBusy());        // ラムダ内で100ms待つため、ビジーとなる
    ASSERT_EQ(to->update_counter_, 0);  // まだラムダが実行されていないはず

    ASSERT_FALSE(model.ExecAsync([&exec_counter]() {  // まだラムダが実行されていないはず
        ++exec_counter;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        LOGGER("in ExecAsync");
    }));

    model.Sync();  // 非同期要求の完了待ち
    ASSERT_EQ(exec_counter, 1);
    ASSERT_EQ(to->update_counter_, 1);  // オブザーバーのUpdateが呼ばれたことの確認

    model.ExecAsync([&exec_counter]() {
        ++exec_counter;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        LOGGER("in ExecAsync");
    });
```

以上からわかる通り、Modelはインスタンスごとにスレッドを持つため、
Observer::Updateはメインスレッドとはべつの様々なスレッドから呼び出されることになる。

### Viewの非同期処理 <a id="SS_10_3_2"></a>
[Observer](design_pattern.md#SS_9_22)デザインパターンでは、Observerが監視しているSubjectの状態に変更があった場合、
Subject::notifyが呼び出され、その延長でObserver::Updateが呼び出されるような構造を持つ。
Subjectの状態変更や、Subjectのメンバ関数の戻り値をObserver::Updateの処理の一部として、
GUIや標準出力の更新をすることが一般的である。

[MVC](design_pattern.md#SS_9_23)のような構造を持つアプリケーションでは、
ModelオブジェクトやViewオブジェクトを複数必要とする。
通常のViewオブジェクトは、GUIや標準出力はアプリケーション毎に唯一存在するため、
これら表示用リソースは複数のViewオブジェクトに共有されることになる。


以上の考察から明らかなったViewオブジェクトの制約を以下にまとめる。

* Viewオブジェクト複数、生成される。
* Viewオブジェクトは出力用リソースを共有する。
* View::Updateは様々なスレッドから呼び出される。

この結果、Viewオブジェクトに共有されるは出力用リソースへのアクセスは、
それを防ぐための特別な構造を持たたないと競合を起こしてしまう。
競合を防ぐためにロックを多用するとコードが複雑になってしまうため、
出力用リソースへのアクセスは、
1つのスレッドにすることが競合を防ぐための最もシンプルな解になることが多い。

このようなクラス構造は、
[Viewの非同期処理](architecture.md#SS_10_3_2)の例で示したクラス内と同じような構造となることが多いが、
また、出力リソースがアプリケーションに唯一であることから、出力を受け持つクラスを、
[Singleton](design_pattern.md#SS_9_12)にすることが理にかなっているだろう。

これまでの考察から明らかになったViewの典型的なコードを以下に例示する。

```cpp
    //  example/architecture/view/h/view/view.h 11

    class ViewCore {  // すべてのviewから保持される非同期出力オブジェクトを生成するためのシングルトン
    public:
        static ViewCore& Inst()
        {
            static ViewCore inst;
            return inst;
        }

        void ShowAsync(std::string&& msg);  // 非同期出力
        void Sync();                        // 非同期出力の同期待ち

        void SetOStream(std::ostream& ostream) { ostream_ = &ostream; }  // テスト用出力切り替え

    private:
        ViewCore(const ViewCore&) = delete;
        ViewCore(ViewCore&&)      = delete;
        ViewCore() : ostream_{&std::cout}, worker_{&ViewCore::worker_function, this} {}
        ~ViewCore();

        std::thread       worker_;        // 非出力を実現するためのワーカスレッド
        bool              busy_ = false;  // 非出力完了待ちに使用
        std::atomic<bool> stop_ = false;  // worker_functionの終了変数

        void show_msg(std::string const& msg)  // 非同期にmsgを出力
        {
            *ostream_ << msg;
            busy_ = false;
        }
        void worker_function();

        std::list<std::string>  msgs_{};
        std::condition_variable msg_cv_{};
        std::mutex              msg_mtx_{};

        std::ostream* ostream_;
    };
```

```cpp
    //  example/architecture/view/h/view/view.h 51

    class View : public Model::Observer {
    public:
        View() : view_core_{ViewCore::Inst()} {}
        ~View() = default;
        void ShowAsync(std::string&& msg) { view_core_.ShowAsync(std::move(msg)); }
        void Sync() { view_core_.Sync(); }
        void Update(Model const& model) override { view_core_.ShowAsync("View updated"); }

    private:
        ViewCore& view_core_;  // すべての出力をViewCoreに委譲
    };
```

```cpp
    //  example/architecture/view/src/view.cpp 16

    void ViewCore::ShowAsync(std::string&& msg)  // 非同期出力
    {
        {
            std::unique_lock<std::mutex> lock{msg_mtx_};
            msgs_.push_back(std::move(msg));
            busy_ = true;
        }
        msg_cv_.notify_one();
    }

    void ViewCore::worker_function()
    {
        for (;;) {
            {
                std::unique_lock<std::mutex> lock{msg_mtx_};
                msg_cv_.wait(lock, [&msgs = msgs_, &stop = stop_] { return !msgs.empty() || stop; });
                if (stop_ && msgs_.empty()) {
                    return;
                }

                std::string msg = std::move(msgs_.front());

                LOGGER("Processing message", msg, ":busy", b2str(busy_));
                msgs_.pop_front();
                show_msg(msg);
            }
        }
    }

    void ViewCore::Sync()
    {
        for (;;) {
            if (!busy_) {  // busy_のポーリング
                return;
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    }

    ViewCore::~ViewCore()
    {
        stop_ = true;
        msg_cv_.notify_one();
        worker_.join();
    }
```

以下の単体テストでviewの使用例を以下に示す。

```cpp
    //  example/architecture/view/ut/view_ut.cpp 27

    std::ostringstream out;
    View               view{};

    ViewCore::Inst().SetOStream(out);  // 出力の切り替え
    const auto* str = "Output string to View";

    view.ShowAsync(str);  // 非同期出力
    view.Sync();          // 出力待ち
    ASSERT_EQ(out.str(), str);
```




## アーキテクチャの見直し <a id="SS_10_4"></a>
ソフトウェアの成長に伴いアーキテクチャに下記のような綻びが発見されることは珍しいことではない。
このような綻びがプロジェクトの破綻を引き起こす前に手を入れなければならないことは言うまでもない。

* [パッケージが大きくなりすぎる](architecture.md#SS_10_4_1)
* [当初、想定していない依存関係が必要になる](architecture.md#SS_10_4_2)
* [コードクローンが避けられない](architecture.md#SS_10_4_3)
* [当初、想定していない非同期処理が必要になる](architecture.md#SS_10_4_4)

### パッケージが大きくなりすぎる <a id="SS_10_4_1"></a>
初期のアーキテクチャのパッケージ分割が不十分であることはよくあることである。
その場合、大きくなった、もしくは間違いなく大きくなると想定されるパッケージに対しては、
「[アーキテクチャの設計](architecture.md#SS_10_2)」の手順を適用し、そのパッケージを分割する。

分割されたパッケージは、一旦、元のパッケージのサブパッケージとするが、
そのサブパッケージの中で、外部のパッケージから使用される機会の多いものや、
元のパッケージとの関係が少ないものは、元のパッケージから出し、単独のパッケージをするべきだろう。

こういったリファクタリングをその効果に見合った工数で行うためには、
「[開発プロセスとインフラ](process_and_infra.md#SS_11)」で述べたように[自動単体テスト](process_and_infra.md#SS_11_2_1)や
[自動統合テスト](process_and_infra.md#SS_11_2_3)が必要となる。

自動単体テストや自動統合テストがない場合、
このような修正にはデグレードが多発するため多くの工数ロスは避けがたいが、
放置すれば状態は、より悪化する。

### 当初、想定していない依存関係が必要になる <a id="SS_10_4_2"></a>
初期のアーキテクチャの依存関係は、その設計に用いたシナリオが必要とするもののみとなっているため、
ソフトウェアの成長に伴い新たな依存間が必要になることは当然である。
このような場合、下記のようなことに気を付けて新たな依存関係を追加すべきだろう。

* 不要な依存関係を作らない。 
* 循環、相互依存を作らない。
* [依存関係逆転の原則(DIP)](solid.md#SS_8_5)に反した依存関係を作らない。

すでに述べたように、循環や相互依存の解消には、「[SOLID](solid.md#SS_8)」に記載したコードのパターンや
「[デザインパターン](design_pattern.md#SS_9)」が有用である。

### コードクローンが避けられない <a id="SS_10_4_3"></a>
コードクローンの原因はいくつも存在するが、その対処方法は常に、
一連のコードクローンを一つの関数やクラスにして、適切な場所に配置することである。

例えばある基底クラスから派生したクラス群のいくつかがほぼ処理の等しいメンバ関数を持つのであれば、
そのメンバ関数を統一して、基底クラスに移動すれば良い。

この方法と同様に、ほぼ処理の等しい関数やクラスが複数のパッケージに存在し、
それらが「[Nstdライブラリの開発](template_meta_programming.md#SS_13_2)」で述べたような汎用的なものであれば、
プロジェクト全域からアクセスを許可するパッケージを用意し、そこに配置すればよい。

汎用的ではない場合、おそらくパッケージの分割が不十分であったために、
具現化されていないパッケージの処理が複数のパッケージに散乱してしまっていることがことが考えられる。
具現化されていないパッケージを具現化するために、
「[アーキテクチャの設計](architecture.md#SS_10_2)」の手順を再実行すべきだろう。

### 当初、想定していない非同期処理が必要になる <a id="SS_10_4_4"></a>
「[リファクタリングの例](process_and_infra.md#SS_11_2_2_3)」で述べたように、
同期処理を前提としたソフトウェアに非同期処理を追加すると、ソースコードは腐敗を始める。

以下のような事項が腐敗の原因となる。

* 非同期処理のプログラミングは、同期処理のプログラミングよりもかなり難しい。
    * マルチスレッド化が必要になる。
    * マルチスレッド化には競合回避が必要になる。
    * マルチスレッドのデバッグは難しいため、リファクタリングをしなくなる。
    * プロジェクトで使用していなかった新たなシステムコールを使用しなければならなくなる。
* 今までとは逆向きの依存関係が必要になる。

これらに関しては、

* マルチスレッドで必要なシステムコールを熟知する
* [MVC](design_pattern.md#SS_9_23)系の構造を取り入れる

ことで対処できる(「[並行処理](concurrency.md#SS_12)」参照)が、レベルの高いプログラマの工数をかなり消費するため、
避けるべきアーキテクチャ変更である。初期のアーキテクチャの設計時に、
非同期処理が不要であることに対して、絶対の自信がないのであれば、
非同期処理が必要であるという前提で設計すべきだろう。

## アーキテクチャの再構築 <a id="SS_10_5"></a>
多くのプログラマが、日々、スパゲティコードに向かい合い悪戦苦闘している。
そうなった理由は以下のようなことが原因となっている。

1. ソフトウェア開発プロセス(「[開発プロセスとインフラ](process_and_infra.md#SS_11)」参照)の未成熟
2. アーキテクチャの不備
3. プログラマのスキル不足

このような状況を改善・改革するための活動をここでは「アーキテクチャの再構築」と呼ぶことにする。

このような環境の中でのプログラマは、以下のいずれかの行動を選択する。

* その組織から離れる。
* その状態を受け入れる。
* 「アーキテクチャの再構築」に向けた活動を始める。

ここでの議論は、最後の選択をするプログラマのためのものである。
以下では、このようなプログラマを改善プログラマと呼ぶ。

改善プログラマは、その行動様式から原因1、2、3の改善を行おうとするだろうが、
このプログラマがチームの運営方針や予算に影響を与えることができる立場でないのであれば、
原因1、2の対処は出来ないため、原因3の対処のみに注力する以外の改善策はない。

### アーキテクチャ再構築の準備 <a id="SS_10_5_1"></a>
上記のような議論から改善プログラマは以下のようなことをすることになる。

* アーキテクチャの再構築に必要と思われる下記のようなスキルの獲得や向上
    * プログラミング
    * UML、オブジェクト指向、デザインパターン
    * [CI(継続的インテグレーション)](process_and_infra.md#SS_11_2_5)のための知識や言語

* 周りのプログラマのスキル向上
* 今よりもコード品質が悪化しないための施策  
    例えば、「機能追加時にその機能のみに単体テストを導入する」ことや
    「jenkinsよる自動ビルドを行う」こと等は、
    コードのレベルを上げる効果のみにとどまらず、アーキテクチャの再構築のための知識習得に役立つ。

このような改善活動を行いながら、
ソフトウェアを大きく変えざるを得ないようなプロジェクトが企画されることを待つことになるが、
時が来た時に組織に影響を与えられる立場にいなければならない。
従って、改善プログラマにはそのような立場へのプロモーションも必要となる。

以上をまとめると、スパゲティコードの改善には以下のような条件が必要になる。

* 改善プログラマがアーキテクチャの再構築に必要なスキルを獲得する。
* 改善プログラマが組織に影響を与えられる立場を獲得する(ここでの立場とは、
  公式なもののみではなく、権限者の意思決定に影響を与えられる非公式なものでもよい)。
* 何人かのプログラマが改善プログラマのフォロワーとなり、スキルの改善をする。
* ソフトウェアを大きく変えざるを得ないようなプロジェクトが企画される。

### アーキテクチャ再構築のチーム編成 <a id="SS_10_5_2"></a>
ソフトウェア開発プロセス、アーキテクチャ設計、プログラミングに対する知識は、
良書を読み、それを実践することで始めて身につく類のものであるため、
残念なことであるが、日々行うプログラミングを除いて、
アーキテクチャ再構築のための十分な知識をチームが身に着けることは難しい。
ソフトウェア開発プロセスやアーキテクチャ設計の知識は外部から調達せざるを得ないため、
スパゲティコードを立て直すプロジェクトが開始できる目途が付けば、
そのようなコンサルティング業者を探さなければならない。
こういったことを行える業者の数は多くはないが、見つけることは不可能ではない。
運よく見つかった場合でも、その業者が派遣するコンサルタントを何の疑いもなく受け入れてはならない。
コンサルタントのスキルレベルを問いただす必要がある。
間違いなく必要なのは、ソフトウェア開発プロセス導入やアーキテクチャ設計の実績である。
多くのエビデンスはないが、
[ウォーターフォールモデル、V字モデル](process_and_infra.md#SS_11_1_1)のみを提案するコンサルタントや、
[アジャイル系プロセス](process_and_infra.md#SS_11_1_2)を薦めながらテストの自動化を提案しないコンサルタントは、
十分な知識を持っていないと判断してよいと思う。

良いコンサルタントが見つからない場合、改善プログラマが中心になり、
ソフトウェア開発プロセスの導入やアーキテクチャの再設計を行うことになる。
良いコンサルタントが見つかった場合でも、
そのコンサルタントがこれから再構築するソフトウェアの要求仕様を熟知していることはないので、
アーキテクチャ設計を完全に委託することはできず、
結局、アーキテクチャ設計は自力で行わなければならない。
ということで、仮にコンサルタントが見つからなかったとしても、
レビューアーが足りない程度のインパクトである(と思う他ない)。

様々な障害があるだろうが、兎に角それらを乗り越えて、改善プロジェクトが開始できたとしよう。
コンサルタントが見つかった場合の初期のチーム構成は以下の様になる。

|人員                      |ロール                                                       |
|--------------------------|-------------------------------------------------------------|
|改善プログラマ            |リーダ、アーキテクト                                         |
|数人のフォロワープログラマ|UMLダイヤグラムやプロトタイプコード等の開発者                |
|コンサルタント            |知見提供、UMLダイヤグラムやプロトタイプコード等のレビューアー|

コンサルタントが見つからなかった場合、他のメンバにこのロールを振り分けることになる。
助っ人なしではやや不安だろうが、時には蛮勇も必要である。改善に向けて踏み出そう。

### アーキテクチャ再構築の手順 <a id="SS_10_5_3"></a>
アーキテクチャの再構築は、

1. [現在のソースコードをベースに再構築するかどうかを判断する](architecture.md#SS_10_5_3_1)
2. [パッケージ間の依存関係を整理する](architecture.md#SS_10_5_3_2)
3. [依存関係が整理されたパッケージ毎に単体テストを作る](architecture.md#SS_10_5_3_3)
4. [統合テストプログラムを作る](architecture.md#SS_10_5_3_4)
5. [単体テストや統合テストを自動実行できる環境を整える](architecture.md#SS_10_5_3_5)
6. [リファクタリングを行う](architecture.md#SS_10_5_3_6)

のような手順で行うことになる。

この一連の活動は、実際には上から順次実行できるわけではなく、反復する必要がある。
また、この活動後のチーム全体へのプロセスの導入にもスムーズに移行できるため、
[アジャイル系プロセス](process_and_infra.md#SS_11_1_2)を選択するべきである。

このプロセスの定義には、「[開発プロセスとインフラ](process_and_infra.md#SS_11)」や、
「[プロセス・プラクティス](bibliography.md#SS_22_1)」で紹介した書籍が参考になるだろう
(改善プログラマならば、この時点でこれらのドキュメントには精通しているはずである)。

具体的なプロセスを選択した後は、上記の作業を細分化し、プロセスに合わせこむ必要があるが、
この作業は一回のミーティングで完了できる。後から多少の不備が見つかるだろうが、
その都度、見直せばよい。
多くの[アジャイル系プロセス](process_and_infra.md#SS_11_1_2)には、そのための振り返りミーティングが設けられている。

#### 現在のソースコードをベースに再構築するかどうかを判断する <a id="SS_10_5_3_1"></a>
この活動の目的は、今のソースコードと同じ動作をする、きれいななソースコードを作ることであり、
[リファクタリング](process_and_infra.md#SS_11_2_2)がキーファクターとなる。
リファクタリングを行うためには、単体テストが不可欠であるため、
新アーキテクチャには、そのための構造が必要になる。

従って、現在のソースコードをベースに再構築するかどうかを判断するためには、
現在のパッケージの依存関係が循環していないか、
循環していた場合、現実的な工数とデグレードリスクで
「[アーキテクチャとファイル構造](architecture.md#SS_10_3)」で示したクラス図のように修正できるかを調査する必要がある。

循環が修正できない場合、現在のソースコードをベースにすることはできない。
この場合、古いコードの修正はあきらめ、新しいコードをスクラッチから作ることになるため、
手順は「要求仕様を理解する」ことが不要な「[アーキテクチャの設計](architecture.md#SS_10_2)」となる。

#### パッケージ間の依存関係を整理する <a id="SS_10_5_3_2"></a>
パッケージの依存関係が循環していなかった場合、このフェーズでやることはない。

循環を修正する場合、
「[SOLID](solid.md#SS_8)で示したコードパターン」や「[デザインパターン](design_pattern.md#SS_9)」が役に立つだろう。

修正が完了した時点で、手作業による簡単な統合テストを行い、クリティカルなデグレードを修正する。

#### 依存関係が整理されたパッケージ毎に単体テストを作る <a id="SS_10_5_3_3"></a>
「[アーキテクチャとファイル構造](architecture.md#SS_10_3)」で述べたようにビルド環境を整える。

これで単体テストを記述するための環境はできたことになる。
これを使い、各パッケージのいくつかのクラスや関数の単体テストを書く。

この時点で、プロジェクトの起点となるソースコードが出来ているはずである。

メンバを増やし、彼らに単体テストのカバレッジを上げる仕事をさせることになる。
新規メンバには、このプロジェクトのプロセスに従ってもらい、
「[TDD](process_and_infra.md#SS_11_2_4)」で述べたようなワークフローで作業してもらうのが理にかなっている。
もし、コンサルタントが雇えていないのであれば、
このタイミングでアジャイル系プロセスの導入をサポートしてくれるコンサルタントを迎え入れても良い。

独力で行うにしても、助成を頼むにしても、
増員後のチームへのプロセスの導入には細心の注意が必要である。
細かく規定すぎると、「鳥網、精緻にして一鳥もかからず」の例えにある通り、
誰もそのルールには従わなくなる。
逆に、自然に任せれば、せっかく作り上げたアーキテクチャは破壊される。

#### 統合テストプログラムを作る <a id="SS_10_5_3_4"></a>
上記の手順により、ある程度整理されたソースコードに対し、
[自動統合テスト](process_and_infra.md#SS_11_2_3)用プログラムを開発する。
GUI系のアプリケーションでは、
GUIオブジェクト(ボタンやテキストボックス等)を直接操作する統合テストの開発は困難であるが、
その場合は、「[アーキテクチャとファイル構造](architecture.md#SS_10_3)」で示したmodel部分を評価する統合テストを開発する。

統合テストの開発のために、アーキテクチャ再構築中のソフトウェアに新機能の追加
(「[自動統合テストのための仕様追加](process_and_infra.md#SS_11_2_3_2)」参照)や、
さらなるアーキテクチャ変更が発生することがあるが、多くの場合ここで妥協すべきではない。

#### 単体テストや統合テストを自動実行できる環境を整える <a id="SS_10_5_3_5"></a>
上記までで用意した単体テストと統合テストを
[バージョン管理システム](process_and_infra.md#SS_11_2_5_1)と連動させて自動実行するための環境を整える。

典型的には「[CI(継続的インテグレーション)](process_and_infra.md#SS_11_2_5)」で述べたように、

* テストの自動実行を行うツールはJenkins
* バージョン管理システムはgitかgitのクラウドサービス

を使うことになるだろう。
この環境により、例えばgit pushが行われるたびに単体テストと統合テストが自動実行される。
これに合わせて「[コード解析](code_analysis.md#SS_4)」で述べたような解析ツールを導入すると、
この後行うリファクタリングが捗る。

#### リファクタリングを行う <a id="SS_10_5_3_6"></a>
上記までの開発でリファクタリングを行う環境は整ったことになるため、
リファクタリングを開始する。

初期のリファクタリングは、

* 「[パッケージ間の依存関係を整理する](architecture.md#SS_10_5_3_2)」フェーズで修正しきれなかった循環依存の修正
* 巨大なファイルの分割
* [サイクロマティック複雑度](term_explanation.md#SS_19_21_2)の値が高い関数の分割
* 巨大なクラスや、[凝集度](term_explanation.md#SS_19_21_3)の低いクラス分割

になる。
依存関係の整理(循環依存や不要インクルード)は、コンパイル時間短縮にも効果があるため、
なるべく早い時期に取り掛かるのが良いだろう。


#### まとめ <a id="SS_10_5_3_7"></a>
アーキテクチャ(もしくはソースコード)とプロセスは共生関係にあり、
どちらか一方のみを改善することはできないため、アーキテクチャの再構築には、
これまで述べたように

* コードの整理
* プロセスの整備
* 開発インフラの整備、開発

等、多岐にわたる知識が必要なため難易度が高い。
また、これによりチーム活動にも多大なインパクトを与えるため苦渋に満ちたものになるだろう。
従って、このような活動はプロダクトライフタイムで最多でも一回に留めるべきであることは言うまでもない。


