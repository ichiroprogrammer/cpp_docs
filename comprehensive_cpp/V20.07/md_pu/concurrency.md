<!-- ./md/concurrency.md -->
# 並行処理 <a id="SS_12"></a>
03以前のC++は、並行処理に関して十分な機能を備えていなかったため、
多くのソフトウェア開発ではOSネイティブなAPIを使用せざるを得なかった。
11以降のC++は、下記するような言語拡張、
STLの大幅な機能追加等により、この問題の軽減に成功している。

* [ラムダ式](term_explanation.md#SS_19_8_3)
* std::futre、std::async、std::promiseによる[Future](design_pattern.md#SS_9_10)パターンのサポート
* std::unique_lock、std::condition_variableによるイベント通知
* ロック機構のRAIIのサポート(「[RAII(scoped guard)](design_pattern.md#SS_9_9)」参照)
* std::atomic等によるアトミック処理の簡易化

本章では、「[自動統合テスト](process_and_infra.md#SS_11_2_3)」で開発したref_async_r5を改善することによって、
これらを用いたC++11での並行プログラミングを例示する。

なお、本来であればこの章は「[デザインパターン](design_pattern.md#SS_9)」に含めるべきだろうが、
サンプルコードの説明の都合上ここに掲載することとした。

___

__この章の構成__

&emsp;&emsp; [ref_async_r5改善プログラムの要件](concurrency.md#SS_12_1)  
&emsp;&emsp;&emsp; [Controller](concurrency.md#SS_12_1_1)  
&emsp;&emsp;&emsp; [View](concurrency.md#SS_12_1_2)  
&emsp;&emsp;&emsp; [Model](concurrency.md#SS_12_1_3)  

&emsp;&emsp; [非同期処理とその管理](concurrency.md#SS_12_2)  
&emsp;&emsp;&emsp; [TwoPhaseTaskIF(TwoPhaseTaskPtr)](concurrency.md#SS_12_2_1)  
&emsp;&emsp;&emsp; [Dispatcher](concurrency.md#SS_12_2_2)  
&emsp;&emsp;&emsp; [TwoPhaseTaskPtrキュー管理機構](concurrency.md#SS_12_2_3)  

&emsp;&emsp; [ref_async_r6の構造](concurrency.md#SS_12_3)  
&emsp;&emsp; [まとめ](concurrency.md#SS_12_4)  
  
  

[このドキュメントの構成](introduction.md#SS_1_7)に戻る。  

___

## ref_async_r5改善プログラムの要件 <a id="SS_12_1"></a>
「[自動統合テスト](process_and_infra.md#SS_11_2_3)」で開発したref_async_r5は、
少なくとも以下のような並行処理にまつわる問題を持っている。

1. メインスレッドのメインループがstd::getline()でブロックしてしまうため、
   ネットワーク等の複数種類の同時入力には対応できない。
2. ref_async_r5のModel(ref_async_r5のModelはref_async_r3のModelと同じ)
   は2つ以上のスレッドを同時実行できない。

問題1に関しては、複数種類の同時入力に対応できる構造への改善のみを行う
(本章の目的から逸脱するため、複数種類の入力への実際の対応は行わない)。
問題2に関しては、Modelが開始できるスレッドの上限を持たないような改善を行う。
この変更により、ref_async_r5では起こらなかったViewからの出力が競合する問題が発生するため、
その対処も行う。

以上を踏まえ、ref_async_r5改善プログラムは以下のようなものになる。

* プログラム名をref_async_r6(不適切だが、名前の継承とわかり易さを優先する)。
* ref_async_r6のModelは、同時に実行できるスレッド数の上限を持たない。
* ref_async_r5と同じ統合テスト項目
  (「[自動統合テストのための仕様追加](process_and_infra.md#SS_11_2_3_2)」参考)をパスしなければならない。
    * コマンド処理が終了したときの出力が競合してはならない。
    * ref_async_r5と同様にコマンド処理の順番はファースト・イン・ファースト・アウトとする。
* 複数種類の同時入力に対応できる構造にする(メインスレッドがstd::getline()でブロックしない構造)。

以上の条件を満たすref_async_r6の概念的なシーケンス図を下記する。

```plant_uml/ref_async_r6_seq_concept.pu
@startuml
participant Controller
participant View
participant Model
participant MainThread

MainThread ->> Controller : 入力監視用スレッド起動
MainThread -> MainThread : Wait
note right : 終了まで待つ
activate MainThread

Controller -> Controller : getline
activate Controller

[->> Controller : コマンド入力
deactivate Controller

Controller ->> Model:ConvertStoreAsync
activate Model

note right 
ConvertStoreAsyncは
上限なく同時実行できる
end note

Model->View : Update
activate View

note left 
Modelの
内容を表示
end note

deactivate View
deactivate Model

@enduml
```

### Controller <a id="SS_12_1_1"></a>
上記したようにref_async_r6は、メインスレッドでstd::getline()を実行することができないため、
Controllerがその内部スレッドからstd::getline()を呼び出すことで、
コマンド入力に対応することにする。

std::geline()により受信したコマンドのエラーコードは、ref_async_r6のexitコードになるため、
そのエラーコードをController外部から取り出せる必要がある。
その取り出しが簡単に実現できるため、
スレッド生成にはstd::thread()ではなく、std::async()を使用する。

なお、std::async()の戻り値であるstd::future<>のデストラクタは、
管理対象スレッドの終了を待つため、そのスレッドが終了しない場合ハングアップを引き起こす。
これに対処するためには、プログラムが終了手続きに入る前に
(典型的にはexit()を呼び出すか、main()がreturnする前に)スレッドを終了させる必要がある。
このことは、旧来のstd::threadを使用する場合、
スレッドが終了しないことによってthread::join()が永久にリターンしないことと同様である。

以上のような条件から、Controllerは以下のようになる。

```cpp
    //  example/ref_async_r6/controller.h 8

    class Controller {
    public:
        explicit Controller(Model& model, std::istream& is) : model_{model}, is_{is}, future_{} {}

        /// @brief 入力を受け取るスレッドを起動する
        void WatchInput();

        /// @brief 上記スレッドが終わるまで待ち合わせて、スレッドのリターンコードを返す。
        int GetExitCode();

    private:
        std::optional<int> dispatch(std::string const& command);
        int                watch_input();  // WatchInputが開始するスレッドの中身

        Model&           model_;
        std::istream&    is_;
        std::future<int> future_;
    };
```

```cpp
    //  example/ref_async_r6/controller.cpp 7

    void Controller::WatchInput()
    {
        future_ = std::async(std::launch::async, [this] { return watch_input(); });
    }

    /// @brief Controllerのメインループ。std::istreamからコマンド文字列を受け取る。
    /// @return ループ終了の原因がエラーであるならば非0。そうでなければ0。
    ///         この値は、GetExitCode()により取得できる。
    int Controller::watch_input()
    {
        for (;;) {
            auto buffer = std::string{};

            if (std::getline(is_, buffer)) {
                if (auto exit_code = dispatch(buffer)) {
                    return *exit_code;
                }
            }
        }

        assert(false);
        return 0;
    }

    /// @brief 受け取った文字列をパースして、ディスパッチする
    /// @param std::istreamから受け取った文字列
    /// @return プログラムを終了する場合、exitコードを返す
    std::optional<int> Controller::dispatch(std::string const& command)
    {
        switch (command.at(0)) {
        case '+':
            model_.ConvertStoreAsync(command.substr(1));
            return std::nullopt;
        case '.':
            // do nothing
            return std::nullopt;
        case '=':
            Dispatcher::Inst().Stop();  // プログラム終了処理
            return 0;
            // ...
        }
    }

    int Controller::GetExitCode() { return future_.get(); }
```

上記ソースコードで使用しているDispatcherについては「[Dispatcher](concurrency.md#SS_12_2_2)」で解説する。

### View <a id="SS_12_1_2"></a>
「出力が競合してはならない」という要件は、以下のどちらかの方法で対処できる。

1. std::istreamに対する一連の出力をロック(std::mutex)により排他制御する。
2. std::istreamへの出力を行う一連の処理を特定の単一スレッドで行う(これにより処理が直列になる)。

ref_async_r6程度の単純なソフトウェアであれば上記1がシンプルな解となるが、
GUI APIを使用するような、ある程度複雑なアプリケーションの実装では、
上記2を選択するのが一般的である
(ちなみにWindowsアプリケーションの処理系であるWPFでは、
GUI操作はメインスレッドのみに限定されている)。

ref_async_r6では、上記1を選択し、
「スレッドセーフでない処理(Viewの出力)を特定の単一スレッドで行うことにより、その競合を回避する」
例を示す。

[MVC](design_pattern.md#SS_9_23)の構造により、Viewの出力は、Modelの状態変更(メンバー変数の変更)
をトリガーとして(通常はそのコンテキスト上で)行われるため、
Viewの出力が競合するのであれば、その前段のModelのメンバ変数変更も競合する。
Viewの改善では、この両競合を同時に回避することはできないため、
「スレッドセーフでない処理を特定の単一スレッドで行うことにより、その競合を回避する」
機構はView以外の場所で作るべきであると判断できる。
よって、Viewには、ほぼ変更する必要がない。

```cpp
    //  example/ref_async_r6/view.h 7

    class View : public Observer {
    public:
        explicit View(std::ostream& os) noexcept : Observer{}, os_{os} {}

    private:
        virtual void update(Model const& model) override;

        std::ostream& os_;
    };
```

```cpp
    //  example/ref_async_r6/view.cpp 3

    void View::update(Model const& model)
    {
        for (auto const& str : model.GetStrings()) {  //   コメントを除き
            os_ << str << std::endl;                  //   ref_async_r4/view.cppと同じ
        }
    }
```

### Model <a id="SS_12_1_3"></a>
Modelの要件は、以下のようなものである。

1. Controllerから渡された文字列をModel::ConvertStoreAsync()により非同期に処理する。
2. Model::ConvertStoreAsync()は渡された文字列をdo_heavy_algorithm()によって別の文字列に変換する。
3. 変換された文字列をModel::strings\_に保存し、Model::notify()を呼び出す。
4. Model::notify()は、Observerを経由してView::Update()を呼び出す。

この動作の制約条件として、

1. Modelは、同時実行されるModel::ConvertStoreAsync()の個数の上限値を持たない
   (複数個のスレッドを管理できなければならない)。
2. Model::ConvertStoreAsync()の並行呼び出しにより生成されたそれぞれの文字列は、
   それに対応するModel::ConvertStoreAsync()の呼び出し順序のまま保存されなければならない。
3. ViewからのModelの状態表示は、別の状態表示と競合してはならない。

制約条件1から、Modelは複数個のスレッドを管理する必要がある(他のクラスに委譲しても良い)。
制約条件2、3からModel::ConvertStoreAsync()で起動されたスレッドのコンテキスト上で、
変換された文字列をModel::strings\_に保存することや、View::Update()を呼び出すことはできない
(「[View](concurrency.md#SS_12_1_2)」参照)。こうしなければ競合が発生してしまう。

このような制約を回避するため、スレッド管理を行う以下の2つのクラスを導入する。

* [TwoPhaseTaskIF(TwoPhaseTaskPtr)](concurrency.md#SS_12_2_1)
* [Dispatcher](concurrency.md#SS_12_2_2)

これらは「スレッドセーフでない処理を特定の単一スレッドで行うことにより、その競合を回避する」
機構も内包している。

まずは、この2つのクラスを使用して改善したModelのソースコードを以下に示す。

```cpp
    //  example/ref_async_r6/model.h 10

    class Observer {
    public:
        Observer() = default;
        void Update(Model const& model) { update(model); }
        virtual ~Observer() = default;

    private:
        virtual void update(Model const& model) = 0;
    };

    class Model {
    public:
        Model()  = default;
        ~Model() = default;
        void                            ConvertStoreAsync(std::string&& input);
        void                            Attach(Observer& observer);
        void                            Detach(Observer& observer);
        std::vector<std::string> const& GetStrings() const noexcept { return strings_; }

    private:
        void notify() const;

        std::vector<std::string> strings_{};
        std::list<Observer*>     observers_{};
    };
```

```cpp
    //  example/ref_async_r6/model.cpp 5

    void Model::ConvertStoreAsync(std::string&& input)
    {
        TwoPhaseTaskPtr task = MakeTwoPhaseTaskPtr([str = std::move(input)] { return do_heavy_algorithm(str); },
                                                   [this](auto&& str) {
                                                       strings_.emplace_back(std::move(str));
                                                       notify();
                                                   });

        Dispatcher::Inst().Invoke(std::move(task));
    }

    void Model::Attach(Observer& observer) { observers_.emplace_back(&observer); }
    void Model::Detach(Observer& detach)
    {
        observers_.remove_if([&detach](Observer* observer) { return &detach == observer; });
    }

    void Model::notify() const
    {
        for (auto* observer : observers_) {
            observer->Update(*this);
        }
    }
```

Model::ConvertStoreAsync()を除いて、ref_async_r5で使用したModelとほぼ同じである。
なお、上記TwoPhaseTaskPtrは、

```cpp
    //  example/ref_async_r6/lib.h 13

    /// @typedef TwoPhaseTaskPtr
    /// @brief std::unique_ptr<TwoPhaseTaskIF>オブジェクトを便利に使うためのエイリアス。
    using TwoPhaseTaskPtr = std::unique_ptr<TwoPhaseTaskIF>;
```

と定義されている。

## 非同期処理とその管理 <a id="SS_12_2"></a>
Model::ConvertStoreAsync()の処理は、以下の2つから成立している。

1. Model::ConvertStoreAsync()で行う処理を2つのラムダ式にして、
   それらを引数にしてMakeTwoPhaseTaskPtr()を呼び出し、TwoPhaseTaskPtrオブジェクトを生成する。
2. そのTwoPhaseTaskPtrオブジェクトを引数にしてDispatcher::Invoke()を呼び出す。

そのソースコードから推測できるように、Model::ConvertStoreAsync()は、

* その処理の実行をTwoPhaseTaskPtrオブジェクトに委譲する。
* TwoPhaseTaskPtrオブジェクトの管理等をDispatcherに委譲する。

以下にその詳細を説明する。

### TwoPhaseTaskIF(TwoPhaseTaskPtr) <a id="SS_12_2_1"></a>
ModelからDispatcherへ委譲されるラムダ式を管理するための基底クラスとして、
以下のようなTwoPhaseTaskIFを定義する。

```cpp
    //  example/ref_async_r6/lib.h 20

    /// @brief Dispatcherに代理実行するためのタスクを定義するためのクラスのインターフェース。
    ///        TwoPhaseTask<>のベースクラス。
    class TwoPhaseTaskIF {
    public:
        TwoPhaseTaskIF() = default;

        void DoPreTask() { do_pre_task(); }
        bool IsPreTaskDone() const { return is_pre_task_done_; }
        void PreTaskDone() { is_pre_task_done_ = true; }
        bool DoPostTask() { return do_post_task(); }
        virtual ~TwoPhaseTaskIF() = default;

        // ...

    private:
        bool is_pre_task_done_{false};

        virtual void do_pre_task()  = 0;
        virtual bool do_post_task() = 0;
    };
```

TwoPhaseTaskIFから派生する以下のような具象クラス`TwoPhaseTask<PRE, POST>`を定義する。

```cpp
    //  example/ref_async_r6/lib.h 93

    /// @brief Dispatcherが管理するタスクを管理するTwoPhaseTaskIFの具象クラス
    /// @tparam PRE  非同期に行われる処理を記述したラムダ式の型。重い処理を行う。
    /// @tparam POST PREの実行の結果をModelに保存するラムダ式の型。
    ///               この処理は、スレッドセーフでないため、単一のスレッドで行う。
    ///               ブロックしたり、重い処理を行ってはならない。
    template <typename PRE, typename POST>
    class TwoPhaseTask final : public TwoPhaseTaskIF {
    public:
        using Result = decltype(std::declval<PRE>()());  // PRE()の戻り値型

        // POSTは、bool post(T)のような関数型でなければならない。
        static_assert(std::is_same_v<bool, decltype(std::declval<POST>()(Result()))>);

        TwoPhaseTask(PRE pre_task, POST post_task) : pre_task_{pre_task}, post_task_{post_task}, result_{} {}

        virtual ~TwoPhaseTask() override = default;

    private:
        /// @brief PREを非同期実行し、終了をDispatcherに通知
        virtual void do_pre_task() override
        {
            result_ = std::async(std::launch::async, [this] {
                auto ret = Result{pre_task_()};
                Dispatcher::Inst().Notify(*this);
                return ret;
            });
        }

        /// @brief PREの戻り値を添えてPOSTを同期実行
        virtual bool do_post_task() override { return post_task_(result_.get()); }

        PRE                 pre_task_;
        POST                post_task_;
        std::future<Result> result_;
    };
```

すでに掲載したが、念のため再度TwoPhaseTaskPtrの定義を示す。

```cpp
    //  example/ref_async_r6/lib.h 13

    /// @typedef TwoPhaseTaskPtr
    /// @brief std::unique_ptr<TwoPhaseTaskIF>オブジェクトを便利に使うためのエイリアス。
    using TwoPhaseTaskPtr = std::unique_ptr<TwoPhaseTaskIF>;
```

TwoPhaseTaskPtrオブジェクト(TwoPhaseTaskIFオブジェクトとほぼ等価)
の生成を行うファクトリ関数を以下のように定義する。

```cpp
    //  example/ref_async_r6/lib.h 132

    /// @brief TwoPhaseTaskIFオブジェクトを生成するファクトリ関数
    /// @tparam PRE       TwoPhaseTaskのPRE
    /// @tparam POST_BODY TwoPhaseTaskのPOSTの中身で、戻り値はvoid
    template <typename PRE, typename POST_BODY>
    TwoPhaseTaskPtr MakeTwoPhaseTaskPtr(PRE pre_task, POST_BODY post_body)
    {
        using T        = decltype(std::declval<PRE>()());
        auto post_task = [post_body](T&& pre_result) {
            post_body(std::move(pre_result));
            return true;
        };

        return std::make_unique<TwoPhaseTask<PRE, decltype(post_task)>>(pre_task, post_task);
    }
```

TwoPhaseTask<>は以下のような前提を持つ。

* コンストラクタの第1引数(pre_task)で渡されたラムダ式は、
  ある程度の期間、ブロックしてしまうような時間のかかる処理である可能性がある。
* コンストラクタの第2引数(post_task)で渡されたラムダ式は、短時間で処理できる。

DispatcherやTwoPhaseTaskPtrオブジェクトは以上の前提から、以下のような処理を行う。

* TwoPhaseTaskPtrオブジェクトのDoPreTask()が呼び出されると、
  新しいスレッドを起動し、そのコンテキスト上でpre_taskを実行し、その完了をDispatcherに通知する。
* 通知を受けたDispatcherは、
  メインスレッド上で呼び出されたDispatcher::ExecUntilStop()のコンテキスト上で、
  通知をしたTwoPhaseTaskPtrオブジェクトのDoPostTask()を呼び出す。
* TwoPhaseTaskPtrオブジェクトのDoPostTask()は、
  そのTwoPhaseTaskPtrオブジェクトのDoPreTask()で生成された結果を引数としてpost_taskを実行する
  (この処理はメインスレッドのコンテキスト上で順次処理されるため排他の必要がない)。

### Dispatcher <a id="SS_12_2_2"></a>
Dispatcherは、「[TwoPhaseTaskIF(TwoPhaseTaskPtr)](concurrency.md#SS_12_2_1)」で説明した動作に加え、
以下のような特徴、前提を持つ。

* Dispatcherは、[Singleton](design_pattern.md#SS_9_12)として実装され、
  ref_async_r6のどこからでもそのpublic関数を呼び出すことができる。
* Dispatcher::ExecUntilStop()は、メインスレッド上でイベント待ちループを形成し、
  Dispatcher::Stop()が呼び出されると、そのループを抜ける。
* Dispatcher::Invoke()は、TwoPhaseTaskPtrオブジェクトを自分のキューにプッシュし、
  そのオブジェクトのDoPreTask()を呼び出す。
* Dispatcherは、TwoPhaseTaskPtrオブジェクトからのDoPreTask()完了イベント通知を受け、
  Dispatcher::ExecUntilStop()のコンテキスト上で、
  そのオブジェクトのDoPostTask()を呼び出す。
  この処理は特定の単一スレッド(メインスレッド)で実行される(直列化される)ため、
  スレッドセーフでない処理はここで処理されることを前提としている。

Dispatcherのクラス宣言、定義を下記する。

```cpp
    //  example/ref_async_r6/lib.h 49

    /// @brief InvokeされたTwoPhaseTaskPtrの
    ///         * PreTaskを非同期に呼び出し、終了時自分に通知する。
    ///         * PreTask終了通知をトリガーに、PreTaskの結果を引数にしてPostTaskを
    ///           ExecUntilStop()のコンテキスト上で呼び出す。
    ///        ExecUntilStop()は、Stop()が呼び出されるまでリターンしない。
    class Dispatcher {
    public:
        static Dispatcher& Inst();

        /// @brief TwoPhaseTaskPtrを登録してPreTaskを非同期実行。
        /// @param TwoPhaseTaskPtrオブジェクトのrvalue。
        void Invoke(TwoPhaseTaskPtr&&);

        /// @brief 登録されているTaskの処理が終わったら、ExecUntilStop()がリターンする。
        void Stop();

        /// @brief PreTaskがその終了を通知する
        void Notify(TwoPhaseTaskIF& task);

        /// @brief 終了したPreTaskの対のPostTaskをPreTaskの戻り値を添えて呼び出す。
        void ExecUntilStop();

        // ...

    private:
        Dispatcher() = default;
        TwoPhaseTaskPtr pop_task();
        void            push_task(TwoPhaseTaskPtr&& task, bool stop);

        std::mutex mutex_{};

        std::queue<TwoPhaseTaskPtr> two_phase_tasks_{};
        std::condition_variable     pre_task_done_{};
        bool                        stoped_{false};
    };
```

Dispatcherのメンバ関数定義は、次節に掲載する。

### TwoPhaseTaskPtrキュー管理機構 <a id="SS_12_2_3"></a>
これまでの説明やソースコードからわかるように、ref_async_r6の並行処理は、
TwoPhaseTaskPtrのキュー管理機構によって実現されている。
TwoPhaseTaskPtrのキュー管理機構は、
下記表に示したDispatcher内部のSTLクラスにより実装されている。
ここでは、その詳細について説明を行う。

|  型                           | インスタンス                  | 役割                         |
|:------------------------------|:------------------------------|:-----------------------------|
| `std::queue<TwoPhaseTaskPtr>` | Dispatcher::two_phase_tasks\_ | TwoPhaseTaskPtrキュー        |
| std::condition_variable       | Dispatcher::pre_task_done\_   | イベント待ち、イベント通知   |
| std::mutex                    | Dispatcher::mutex\_           | TwoPhaseTaskPtrキューの排他  |
| `std::unique_lock<std::mutex>`| 関数ローカル                  | イベント待ち解除時の排他     |
| `std::lock_guard<std::mutex>` | 関数ローカル                  | mutex\_のRAII                |

なお、std::condition_variableを用いたイベント待ちに、

```cpp
    std::condition_variable::wait(lock)
```

を使用する場合、「[Spurious Wakeup](term_explanation.md#SS_19_21_4)」への対処が必要になるが、

```cpp
    std::condition_variable::wait(lock, 関数オブジェクト)
```

にはその対処が含まれているため、前者を非推奨とし、ここでは後者を使用する。

TwoPhaseTaskPtrキュー管理機構はDispatcher::Invoke()が呼び出されることを起点にして、 
以下のようなプッシュ処理を行う。

1. MakeTwoPhaseTaskPtr()により生成されたTwoPhaseTaskPtrオブジェクトを引数にして、
   Dispatcher::Invoke()が呼び出される。
2. Dispatcher::Invoke()はその仮引数であるTwoPhaseTaskPtrオブジェクトを引数にして、
   Dispatcher::push_task()を呼び出す。
3. Dispatcher::push_task()は、Dispatcher::mutex\_によって排他されたセクションで
   (pop_task()との競合があり得る)、
   TwoPhaseTaskPtrオブジェクトをDispatcher::two_phase_tasks\_へプッシュする
   (その後、そのオブジェクトのDoPreTask()を実行し、非同期処理を開始させる)。

```cpp
    //  example/ref_async_r6/lib.cpp 13

    void Dispatcher::Invoke(TwoPhaseTaskPtr&& task) { push_task(std::move(task), false); }

    void Dispatcher::push_task(TwoPhaseTaskPtr&& task, bool stop)
    {
        auto* st = task.get();
        assert(st != nullptr);
        {
            auto lock = std::lock_guard{mutex_};
            if (stoped_) {
                return;
            }
            stoped_ = stop;
            two_phase_tasks_.push(std::move(task));
        }
        st->DoPreTask();
    }
```

TwoPhaseTaskPtrキュー管理機構は以下のようにしてTwoPhaseTaskPtrオブジェクトのポップ処理を行う。

1. Dispatcher::ExecUntilStop()は、Dispatcher::pop_task()の中で、
   Dispatcher::pre_task_done\_.wait()によりイベント待ちを行う。
2. イベント待ち解除はDispatcher::Notify()中から、
   pre_task_done\_.notify_all()が呼び出されることによって行われる。
3. 「pre_task_done\_.notify_all()が呼び出され」且つ、
   「Dispatcher::two_phase_tasks\_の先頭TwoPhaseTaskPtrオブジェクトの非同期処理が完了」
   していれば、Dispatcher::pop_task()のイベント待ち状態は解除される。
4. Dispatcher::pop_task()のイベント待ち解除時に発生するクリティカルセクションは、
   `std::unique_lock<mutex>`によって保護される(push_task()との競合があり得る)。
5. このクリティカルセクションの中で、
   Dispatcher::two_phase_tasks\_からTwoPhaseTaskPtrオブジェクトがポップされることで、
   そのTwoPhaseTaskPtrオブジェクトはキューの管理対象外となる
   (その後、そのTwoPhaseTaskPtrオブジェクトがスコープアウトした時点で自動deleteされる)。

```cpp
    //  example/ref_async_r6/lib.cpp 43

    void Dispatcher::ExecUntilStop()
    {
        for (;;) {
            auto task = TwoPhaseTaskPtr{pop_task()};

            if (!task->DoPostTask()) {
                assert(two_phase_tasks_.empty());
                stoped_ = false;
                break;
            }
        }
    }

    void Dispatcher::Notify(TwoPhaseTaskIF& task)
    {
        auto lock = std::lock_guard{mutex_};

        task.PreTaskDone();
        pre_task_done_.notify_all();  // pop_taskでのイベント待ち解除
    }

    TwoPhaseTaskPtr Dispatcher::pop_task()
    {
        auto lock = std::unique_lock{mutex_};

        pre_task_done_.wait(lock, [this]() noexcept {  // イベント待ち
            return !two_phase_tasks_.empty() && two_phase_tasks_.front()->IsPreTaskDone();
        });

        // キューからのTwoPhaseTaskPtrオブジェクトのポップ
        auto task = TwoPhaseTaskPtr{std::move(two_phase_tasks_.front())};
        two_phase_tasks_.pop();

        return task;
    }
```

## ref_async_r6の構造 <a id="SS_12_3"></a>
ここまでで説明したように主に以下の5つのクラスがref_async_r6を構成する。

* [Controller](concurrency.md#SS_12_1_1)
* [View](concurrency.md#SS_12_1_2)
* [Model](concurrency.md#SS_12_1_3)
* [TwoPhaseTaskIF(TwoPhaseTaskPtr)](concurrency.md#SS_12_2_1)
* [Dispatcher](concurrency.md#SS_12_2_2)

まずは、ref_async_r6のクラス図によりそれらの依存関係を示す。

```plant_uml/ref_async_r6_class.pu
@startuml
package Model as ModelPkg {
    class Model {
        notify()
    }

    class Observer {
        Update(const& Model);
    }

    class TwoPhaseTaskPtr
    class Dispatcher
}

class View {
    Update(const& Model);
}

class Controller

note top of TwoPhaseTaskPtr : 非同期処理スレッド
note top of Dispatcher : TwoPhaseTaskPtr管理

View -up-|> Observer
Model-up->TwoPhaseTaskPtr : Modelが\nConvertStoreAsync()の\n処理の実行を\nTwoPhaseTaskPtrに\n委譲するための依存関係。
Model-up->Dispatcher : Modelが\nTwoPhaseTaskPtrの\n管理をDispatcherに\n委譲するための依存関係。
Model-left->Observer
Controller-up->Dispatcher : Controllerが\nDispatcherの\nメインループを終了\nさせるための依存関係。
Controller->Model
TwoPhaseTaskPtr <-right->Dispatcher

@enduml

```

すでに定義したref_async_r6の動作仕様を改めて下記する。

1. 標準入力から文字列を受け取り、
2. 文字列をパースし、コマンドと引数文字列に分離し、
3. 引数文字列を、時間のかかるアルゴリズムで別の文字列に変換し、
4. 変換文字列を記録し、
5. 記録した全ての変換文字列をstd::coutに出力する。

上記クラスを使い、この動作仕様を実現するシーケンス図を下記する。

```plant_uml/ref_async_r6_seq.pu
@startuml
scale max 700 width

participant Controller
participant View
participant Model
participant MainThread
participant Dispatcher
participant TwoPhaseTaskPtr

MainThread ->> Controller : WaitInput
Controller -> Controller : watch_input
activate Controller
Controller -> Controller : getline
activate Controller

MainThread -> Dispatcher : ExecUntilStop
activate Dispatcher
Dispatcher -> Dispatcher : pop_task
activate Dispatcher
note right: codition_variable\nでイベント待ち

[-> Controller : コマンド入力
deactivate Controller

Controller -> Model:ConvertStoreAsync
activate Model

create TwoPhaseTaskPtr
Model -> TwoPhaseTaskPtr : MakeTwoPhaseTaskPtr\n(pre_task, post_task)

Model -> Dispatcher::Invoke(TwoPhaseTaskPtr)
activate Dispatcher

Dispatcher -> Dispatcher::push_task
note left
TwoPhaseTaskPtr
オブジェクトを
キューへプッシュ
end note

Dispatcher ->> TwoPhaseTaskPtr : DoPreTask
note right: pre_task\n非同期実行

activate TwoPhaseTaskPtr
deactivate Dispatcher
deactivate Model

TwoPhaseTaskPtr -> TwoPhaseTaskPtr : do_pre_task
TwoPhaseTaskPtr -> Dispatcher : Notify
deactivate TwoPhaseTaskPtr

Dispatcher --> Dispatcher : pop_task
deactivate Dispatcher
note left
TwoPhaseTaskPtr
オブジェクトを
キューからポップ
end note

Dispatcher -> TwoPhaseTaskPtr : DoPostTask
activate Dispatcher
note right
競合する処
理の直列化
end note

activate TwoPhaseTaskPtr
TwoPhaseTaskPtr -> Model

activate Model
note left: pre_taskの\n戻り文字列を\nstrings_に追加
Model -> Model : notify

Model->View : Update
activate View

note left 
Modelの
内容を表示
end note

deactivate View

Model --> TwoPhaseTaskPtr
deactivate Model

TwoPhaseTaskPtr --> Dispatcher
deactivate Dispatcher
deactivate TwoPhaseTaskPtr
destroy TwoPhaseTaskPtr

@enduml
```

## まとめ <a id="SS_12_4"></a>
本章では、C++03から大幅に改善されたC++11以降の機能を使い、並行処理プログラミングについて解説したが、
文脈に沿わなかったことにより、説明を割愛した事項もあるため、以下に改めて注意点をまとめる。

* C++11以降では、以下のような方法で競合回避のための排他制御ができる。
    1. std::atomicにより、基本型の演算をアトミックに行う。
    2. std::mutexにより、クリティカルセクションを保護する。
    3. スレッドセーフでないな処理を特定の単一スレッドで行う。

* 一般に、組み込み型演算の競合回避には排他制御1が、オブジェクト操作等の競合回避には排他制御2が、
  それより複雑な競合回避(GUI API内部での競合回避等)には排他制御3が向いている。

* [注意] volatileはメモリアクセスの最適化を防ぐためのものであり、
  std::atomicは異なるコンテキストからのメモリのアクセス競合を防ぐものである。
  従って、全く用途が異なる。

* 排他制御1を使用し、スピンロックを実装できる(「[固定長メモリプール](dynamic_memory_allocation.md#SS_14_2_1)」参照)。

* 排他制御2を使用する場合、[RAII(scoped guard)](design_pattern.md#SS_9_9)を使用する。
    * lock()/unlock()を直接ソースコードに書かない。代わりに`std::lock_guard<std::mutex>`を使用する。

* 排他制御3を使用する場合、アーキテクチャに大きな影響を与えるため、
  それが必要になるのであれば、できるだけ早期に対応する。

* より直感的な記述ができるため、std::thread(とstd::promiseやstd::packaged_task)
  よりstd::asyncを優先して使用する(「[Future](design_pattern.md#SS_9_10)」参照)。
    * std::asyncを使用する場合、第1引数にはstd::launch::asyncを指定する。
    * std::thread、std::asyncから起動されるスレッドのエントリー関数オブジェクトは、
      プログラムが終了手続きに入る前にreturnさせる。
      そうしなければ、終了時にプログラムがクラッシュするか、ハングアップする。
    * std::asyncは処理を非同期に行うための機構であり、
      従ってその内部処理が排他制御のロック(std::mutex等)を行わないようにする。

* OSネイティブなAPIよりも、C++STLを優先して使用する。
    * イベント待ちには、std::condition_variableを優先して使用する
      (ビジーループは、よほどの理由がない限り使用しない)。

並行処理はそれ自体が複雑であり、その実装やデバッグは難しい。
一方でハードウェア性能を十分に引き出すソフトウェアの開発には絶大な効果を発揮する方法であるため、
多くのプログラマにとって、避けて通ることはできない、時間を投資するに値する技術である。
そのことを良く心得て、実践に当たってほしい。


