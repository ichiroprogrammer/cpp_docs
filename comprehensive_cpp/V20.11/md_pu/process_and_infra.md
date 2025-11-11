<!-- ./md/process_and_infra.md -->
# 開発プロセスとインフラ <a id="SS_11"></a>
ソフトウェア開発を効率よく行うためには、以下の三要素をレベル高く保つことが重要である。

* プログラマ
* 開発プロセス(以下、単にプロセスと呼ぶ)
* 開発をサポートするためのインフラ(以下、単にインフラと呼ぶ)

この章では後ろ２つの要素(プロセスとそれを支えるインフラ)について、
アジャイル、CIに軸足を置いて説明する。

___

__この章の構成__

&emsp;&emsp; [プロセス](process_and_infra.md#SS_11_1)  
&emsp;&emsp;&emsp; [ウォーターフォールモデル、V字モデル](process_and_infra.md#SS_11_1_1)  
&emsp;&emsp;&emsp; [アジャイル系プロセス](process_and_infra.md#SS_11_1_2)  
&emsp;&emsp;&emsp; [ウォーターフォール vs アジャイル](process_and_infra.md#SS_11_1_3)  

&emsp;&emsp; [アジャイル系プロセスのプラクティスとインフラ](process_and_infra.md#SS_11_2)  
&emsp;&emsp;&emsp; [自動単体テスト](process_and_infra.md#SS_11_2_1)  
&emsp;&emsp;&emsp; [リファクタリング](process_and_infra.md#SS_11_2_2)  
&emsp;&emsp;&emsp; [自動統合テスト](process_and_infra.md#SS_11_2_3)  
&emsp;&emsp;&emsp; [TDD](process_and_infra.md#SS_11_2_4)  
&emsp;&emsp;&emsp; [CI(継続的インテグレーション)](process_and_infra.md#SS_11_2_5)  

&emsp;&emsp; [まとめ](process_and_infra.md#SS_11_3)  
  
  

[インデックス](introduction.md#SS_1_4)に戻る。  

___

## プロセス <a id="SS_11_1"></a>
本ドキュメントでは、プロセスを下記の3つに分類する。

* [ウォーターフォールモデル、V字モデル](process_and_infra.md#SS_11_1_1)
* 反復型
* [アジャイル系プロセス](process_and_infra.md#SS_11_1_2)

上から順に初期計画順守的であり、逆に下から順に状況適応的である。
状況適応的であることは、無計画であることを意味しない。
ただ単にプライオリティの問題として、
計画に従うことより状況に適応・対処することを選択するということである。

ほとんどのアジャイル系のプロセスは、繰り返し構造を持つため、
「アジャイル ⊆ 反復型」と分類されることもある(が、本ドキュメントではそうしない)。

### ウォーターフォールモデル、V字モデル <a id="SS_11_1_1"></a>
ウォーターフォールモデルもしくはV字モデルと呼ばれるプロセスでは、
「要件分析」→「基本設計」→「機能設計」→「詳細設計」→「プログラミング」
といった工程でソフトウェアを作り、その後
「単体テスト(UT)」→「結合テスト(IT)」→「システムテスト」→「受入テスト(運用テスト)」
といった工程でテストを行う。

```plant_uml/v_model.pu
@startditaa

+----+                                                        +-----+
|    |                                                        |     |
|要件分析| <-=--------------------------------------------------> |受入テスト|
|cRED|                                                        |cRED |
+--+-+                                                        +--+--+
   |                                                             ^
   |  +----+                                           +-------+ |
   |  |    |                                           |       | |
   +->|基本設計| <-=-------------------------------------> |システムテスト+-+
      |cBLU|                                           |cBLU   |
      +--+-+                                           +---+---+
         |                                                 ^
         |   +----+                             +-----+    |
         |   |    |                             |     |    |
         +-->|機能設計| <-=-----------------------> |結合テスト+----+
             |cGRE|                             |cGRE |
             +--+-+                             +--+--+
                |                                  ^
                |    +----+              +-----+   |
                |    |    |              |     |   |
                +--->|詳細設計| <-=--------> |単体テスト+---+
                     |cPNK|              |cPNK |
                     +--+-+              +--+--+
                        |                   ^
                        |      +------+     |
                        |      |      |     |
                        +----->|コーディング+-----+
                               |      |
                               +------+

'日本語でカラムがずれる
@endditaa
```

設計・開発の各フェーズ(上図の左側)は、同じ高さにあるテストの各フェーズ
(上図の右側)にそれぞれ対応する。
ソフトウェアの機能はそれが定義された設計・開発フェーズに対応するテストフェーズで評価される。

設計・開発フェーズではトップダウンで作業を行うことで実装漏れや手戻りを防ぎ、
テストフェーズではその逆にボトムアップで作業を行うことにより、
細かいバグによる全体進捗の妨げを防ぐことを意図している。

長い歴史を持った手法であるため、安定したプロセスであるが、下記するような問題を持っている。

* プロダクトへの学習が進んでないプロジェクト初期に、
  下記のようなリスクの高い意思決定をせざるを得ない。
    * プロジェクトの計画
    * [アーキテクチャの設計](architecture.md#SS_10_2)

* 設計・開発フェーズでの手戻りを無くすために多くのレビューを繰り返すが、
  多くの仕様上のバグは実装時に発見される(実装することで仕様バグは発見しやすくなる)。
* 設計・開発の各フェーズで一定以上のバグが見つかった場合、
  そのフェーズを中止し、前のフェーズに戻らなければならい。
  これにはコストがかかりすぎるため、このルールの順守は容易ではない。
* 自然言語やコンピュータ言語、数式等を使って以下のようなソフトウェアを仕様化することや、
  その仕様書をレビューすることは困難である。
    * ルック&フィールが重要なリッチなGUI
    * トライ&エラーを繰り返しながら開発するアルゴリズム  

* ソフトウェア開発は短くても数か月必要であるため、その間に要求仕様が不変であることは稀であり、
  開発途中での仕様変更は避けがたいが、このプロセスに従った要求仕様の変更、
  追加はコストがかかりすぎるため現実的には不可能である。
* 要求仕様の変更、追加が困難であるため、プロジェクトの初期に必要性の不確かな機能が大量に要求される。
* 実装が終わるのは通常全体日程の7割～8割を消化した頃である。
  その時期まで開発の進捗や品質はわからない。
  わかるのは「消費した工数」と、「希望的観測により作られた進捗率」である。

### アジャイル系プロセス <a id="SS_11_1_2"></a>
アジャイル系プロセスとは、
敏捷(==agile)かつ適応的にソフトウェア開発を行う軽量な開発手法群の総称である。

以前、アジャイルが意味するものは誤用・乱用され、今もってその状態が解消されたとは言い難いため、
あえて下記の通り注意喚起する。

* 無計画なソフトウェア開発はアジャイルではない。
* [カウボーイコーディング](https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%B8%E3%83%A3%E3%82%A4%E3%83%AB%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E9%96%8B%E7%99%BA#%E3%82%AB%E3%82%A6%E3%83%9C%E3%83%BC%E3%82%A4%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0)
  はアジャイルでない。
* 要求変更を受け入れるだけではアジャイルではない。
* アジャイルは、フレデリック・ブルックスがいうところの「銀の弾」ではない。

英単語の「agile(アジャイル)」には「繰り返し」という意味は含まれていないが、
実際には、その代表格であるスクラムやXPを含め、ほとんどのアジャイル系プロセスは、
下記のような繰り返し(イテレーション)構造を持つ。

```plant_uml/agile.pu
@startuml
:初期計画;
note right
    アジャイル系プロセスであっても、ソフトウェアの
    * 機能リスト(重要なユースケース程度)
    * ラフなリリース日程(初期計画)
    は必要。
    イテレーションを繰り返し、理解が進むことにより
    要求仕様や計画を正確にしていく必要がある。
end note

while(開発すべき機能がある?) is (yes)

    partition イテレーション {
        :計画;
            note right
                当イテレーションで開発する機能や
                計画の決定する。
            end note
        :要求分析;
            note right
                全体の要求機能にフィードバック。
            end note
        :設計;
        :コーディング;
            note right
                コーディングと同時に
                * 単体テスト
                * 自動実行が可能な統合テスト
                の実装を行う。
            end note
        :テスト;
            note right
                単体テスト、自動統合テスト、
                自動化できないテストを行う。
            end note
        :振り返り;
            note right
                イテレーションを振り返り、改善する。
                他者に新規機能の評価を行ってもらう。
                全体計画にフィードバックする。
            end note
        }

endwhile (no)

:システムテスト/受入テスト;
:リリース;
@enduml

```

こういったプロセスは、ウォーターフォールが持つ欠点への反省と克服のために作られた(と言って良い)ため、
多くのウォーターフォールの欠点を軽減、回避しているが、
一方でウォーターフォールが持っていない下記のような欠点を持っている。

* 比較的小さいプロジェクトに向いている(大規模プロジェクトでは難しい)。
* 要求仕様の全項目の完了時期を約束しない
  (ウォーターフォールでは約束するが、約束が守られるとは限らない。
  また、無理に守ろうとするため、しばしばデスマーチが発生し、返って完成が遅れる)。
* ほとんどのアジャイル系プロセスは、
  チームが様々なサブプロセスやプラクティスを実行することを前提としている。
* プログラマが多能工であることを前提している。
    * 要求分析→設計→コーディング→単体テスト(UT)→統合テスト(IT)を各人ができなければならない。
    * 各人は、プロダクト開発言語のみではなく、
      単体テストフレームワークや各種自動化用言語を理解する必要がある。

### ウォーターフォール vs アジャイル <a id="SS_11_1_3"></a>
ウォーターフォールとアジャイルの対比を下記する。

|                |ウォーターフォール          |アジャイル                        |
|:---------------|:--------------------------:|:--------------------------------:|
|計画            |無謬が前提なので硬直的に従う|誤りが前提なので修正しながら進める|
|進捗計測        |ほぼ不可能                  |実測ベース                        |
|要求技能        |OOD/C++                     |OOD/C++/TDD etc                   |
|自動化          |通常は未実施                |自動化前提                        |
|プロジェクト規模|規模とは関係小              |大規模は難しい                    |

アジャイル系プロセスは開発チーム全員による議論を要求するので、
１チーム１０人程度以下でなければ運営が効率的ではない。
それ以上の人数が必要な場合、１０人以下のチームを複数個作り、
「各チームのリーダーが参加するイテレーション毎の計画ミーティング」
でソフトウェア開発全体の計画作りと各チームへのタスクの割り振りを行うことになる。
先に述べた理由から、このミーティングの参加者も１０人程度以下が望ましい。
以上のような考察から、
１００人を超えるような大規模開発にはアジャイル系プロセスは不向きであるというのが常識的な結論である。
逆にそれほどの規模でないプロジェクトでウォーターフォールを選ぶ理由はないと思われる。

## アジャイル系プロセスのプラクティスとインフラ <a id="SS_11_2"></a>
多くのアジャイル系プロセスは、下記のようなサブプロセスやプラクティスの実施を前提とする。

* [自動単体テスト](process_and_infra.md#SS_11_2_1)
* [リファクタリング](process_and_infra.md#SS_11_2_2)
* [自動統合テスト](process_and_infra.md#SS_11_2_3)
* [TDD](process_and_infra.md#SS_11_2_4)
* [CI(継続的インテグレーション)](process_and_infra.md#SS_11_2_5)
* [コードインスペクション](process_and_infra.md#SS_11_2_5_1_2)

このプロセスでは前イテレーションまでに作られたテスト済のソースコードを何度も修正することになる。
これにより、

* ソースコードを修正すると再帰テストが必要になるが、
  これを手作業で行えば、プロジェクトの工数が圧迫されるため、
  テストの自動化はアジャイル系プロセスにとって必須である
* 汚いソースコードへの機能追加は困難・非効率であるため、リファクタリングが必要であり、
  リファクタリングには単体テストが必須である

という理由から、自動単体テストとリファクタリングは特に重要なプラクティスである。

### 自動単体テスト <a id="SS_11_2_1"></a>

#### 自動単体テストとは？ <a id="SS_11_2_1_1"></a>
一般に、単体テスト(UT)とは、個々のクラスや関数といったソフトウェア構成要素の機能が正確に
動作することを検証するためのテストを指す。
原理的には、デバッガ等を利用して手作業で単体テストを実行することは可能であるが、

* 工数が膨大になる
* テストの再現性が低い
* 高速な操作のテストが困難である

等の問題がある(V字モデルであれば可能かもしれないが)ため、現実的ではない。

自動単体テスト(以下単に単体テストやUTと呼ぶこともある)とは、この問題に対処するためのもので、
ワンコマンド(もしくはワンクリック)でクラスや関数の単体テストを行うプログラムである。

下記にstd::vectorの単体テストを例示する。

```cpp
    //  example/etc/ut.cpp 7

    TEST(UT, std_vector)
    {
        auto v0 = std::vector{3, 2, 1};

        ASSERT_EQ(3, v0.size());
        ASSERT_EQ(3, v0[0]);
        ASSERT_EQ(2, v0[1]);
        ASSERT_EQ(1, v0[2]);
        ASSERT_THROW(v0.at(3), std::out_of_range);  // エクセプション発生

        // sortのテスト
        std::sort(v0.begin(), v0.end());
        ASSERT_EQ((std::vector{1, 2, 3}), v0);

        // transformのテスト
        auto v1 = std::vector<int>{};
        std::transform(v0.begin(), v0.end(), std::back_inserter(v1), [](auto x) { return x * 2; });
        ASSERT_EQ((std::vector{2, 4, 6}), v1);
    }
```

このようなプログラムを書くことを「単体テストを書く(を作る)」、
このようなプログラムを実行する(実行してバグを取り除く)ことを「単体テストを行う(をする)」という。
通常、単体テストソースコードのビルドや単体テストの実行は、
その対象ソースコードと同じビルドシステム(makeやVisual Studioのソリューション等)に組み込まれる。
単体テストを書き、それをビルドシステムから実行できるようにすることで、
ほとんど工数をかけることなく何度でも単体テストを繰り返し実行できる
(つまり単体テストを持つクラスの回帰テストのコストをほぼ0にできる)。

#### 単体テストのメリット <a id="SS_11_2_1_2"></a>
単体テストを行うメリットは、

* バグが単体テストで検出可能である場合、
  そのバグを統合テストで検出・デバッグするよりも、単体テストで検出・デバッグする方が効率的である。
* 自動単体テストは工数をほとんどロスすることなしに何度でも実行できるため、
  機能追加、バグ修正、リファクタリング等のソースコード修正後の回帰テストが容易になる。
* ソースコードカバレッジを計測できるため、テストの網羅性を定量化できる。
* 統合テスト以降では実施が難しいテスト(エラーハンドリング等)であっても、
  単体テストであれば比較的容易に実施できる。

一方で単体テストを行うデメリットは、

* 単体テストが可能なクラス設計には、人員のスキルの向上が必要(OOD、デザインパターン等)である。
* 単体テストのコーディングに時間がかかる(一見そう見えるが、
  単体テストにより統合テストやシステムテストの時間が短縮されるので、
  期間トータルでは問題ないことが多い)。

単体テストのメリット、デメリットを比べれば明らかな通り、単体テストを行わない合理的理由はない
(そもそも一般的な意味での単体テストを行わないプロセスはおそらく存在しない)。

#### アーキテクチャと単体テスト <a id="SS_11_2_1_3"></a>
プログラムとその単体テストのパッケージの構造(「[アーキテクチャ](architecture.md#SS_10)」参照)を説明するために、
以下のような特徴を持つAppliというプログラムを想定する。

* 「[パッケージとその構成ファイル](programming_convention.md#SS_3_7)」で定めたルールに従っている。
* 各パッケージはライブラリとして実装され、それらをリンクすることによりAppliが生成される。
* 下記パッケージ図のような構造を持つ。

```plant_uml/arch_and_lib.pu
@startuml

allow_mixing

rectangle Appli {
    package A {
        class A_0
        class A_1
        class A_2
    }
    package B {
        class B_0
        class B_1
    }
    package C
    package D
    package E
}

B_0 -up-> A_0
C -up-> A_1
C -up-> A_2
D -up-> B
D -up-> C
E -up-> C

note bottom of A_0 
class A_0は
* a_0.h
* a_0.cpp
で宣言、定義される。
他も同様。
end note

note top of Appli
A-Dの各パッケージは
それぞれがライブラリ
としてAppliにリンクされる
end note

@enduml
```

この場合、下記図のように各パッケージ(ライブラリ)毎に単体テスト実行プログラムを作るのが一般的である
(「[ファイル名](naming_practice.md#SS_6_2_2)」で述べたように、\*.cppに対しては\*\_ut.cppとする)。

```plant_uml/arch_and_lib_ut.pu
@startuml

allow_mixing

rectangle "A_ut.exe" as A_ut_exe {
    package A {
        class A_0
        class A_1
        class A_2
    }

    package A_ut {
        class A_0_ut
        class A_1_ut
        class A_2_ut
    }
}

rectangle "B_ut.exe" as B_ut_exe {
    class A_0_stub
    package B {
        class B_0
        class B_1
    }
    package B_ut {
        class B_0_ut
        class B_1_ut
    }
}

rectangle "C_ut.exe" as C_ut_exe {
    package C
    package C_ut
}

A_0 <-up- A_0_ut
A_1 <-up- A_1_ut
A_2 <-up- A_2_ut

B_0 <-down- B_0_ut
B_1 <-down- B_1_ut
A_0_stub <-down- B_0

A_0 <.down. A_0_stub : A_0_stubのヘッダファイルはa_0.h

C <-up- C_ut

note right of A_0_stub : class A_0の代わり

note as UT_EXE_A
X_ut.exeは
Xライブラリの
UTの実行プログラム
(D、Eは省略)
end note

UT_EXE_A .down. A_ut_exe
UT_EXE_A .down. C_ut_exe

@enduml
```

パッケージ間に無駄な依存関係や相互依存、循環依存があると、
単体テスト用のモックやスタブを大量に作らざるを得なくなる場合が多く、
最悪の場合、単体テスト用のリンクができないこともある。

単体テストの開発を行うかどうかに関係なく、
効率の良いソフトウェア開発を行うためにはこのように整理されたパッケージ構造を持つことが好ましいが、
単体テストの開発を行う場合、このような構造は特に重要となる
(「[アーキテクチャとファイル構造](architecture.md#SS_10_3)」参照)。

#### 単体テストのサポートツール <a id="SS_11_2_1_4"></a>
C++をサポートする単体テストフレームワークとしては、

* cUnit
* [google test(gtest)](http://opencv.jp/googletestdocs/primer.html)
* MSTest
* C++Test

等がある。

単体テスト用の実行形式バイナリはビルドを行うOS上で実行するため、
組み込みソフトウェア開発のようにクロスコンパイラを使用している場合、
単体テストのビルドにそのクロスコンパイラを使用することはできない。
そのような場合、単体テスト用にはg++やclang++を使用することが一般的である。
ネイティブなコンパイラを使用しているプロジェクトでは、
単体テストのビルドにもそのコンパイラを使用する。

多くのビルド環境では下記のようなテストカバレッジ(g++/clang++とlcov)を出力できる。
単体テストが十分かどうかは、それを見て判断できる。

```image/fake.pu
マークダウンに<img src="data:image/png;base64, ...>
を埋め込むとAIによるレビューをしようとすると、
そのセッションがストールしてしまいレビューができなくなる。

マークダウンに<img src="data:image/png;base64, ...>
を埋め込む代わりに、わりに下記のようなコードを埋め込む仕様とした。

    ```plantuml
        plant umlのソースコード
    ```
```
```image/fake.pu
マークダウンに<img src="data:image/png;base64, ...>
を埋め込むとAIによるレビューをしようとすると、
そのセッションがストールしてしまいレビューができなくなる。

マークダウンに<img src="data:image/png;base64, ...>
を埋め込む代わりに、わりに下記のようなコードを埋め込む仕様とした。

    ```plantuml
        plant umlのソースコード
    ```
```

### リファクタリング <a id="SS_11_2_2"></a>
リファクタリングとは、ソフトウェア(や、その構成物であるクラスや関数等)
の外部に対する振る舞いを変えることなしに、その内部構造を改善することである。
従って、リファクタリングには、

* リファクタリングの前後で動作の違いがないことを確認できる
* ソースコードの問題点に気づき、それをより良いソースコードに改善できる

ことが必要である。

通常、リファクタリングは下図に示すようなワークフローとしてプロセスに組み込まれ、
日々の開発業務の一環として行われる。

```plant_uml/refactoring.pu
@startuml

:コードインスペクション;
    note right
        * これから機能追加/修正するソースコード
        * コミット前の自作ソースコード
        * サイクロマティック複雑度が高い関数
        * 凝集度の低いクラス
        等に対して行う。
    end note

while(ソースコードに問題がある?) is (yes)

    :ソースコード修正;

    :修正前後で動作の違いがないことを確認;
        note right
            通常は、UT等の回帰テストを
            パスさせることで確認する。
        end note

endwhile(no)

if(ソースコードを修正した) then (yes)
:commit;
else (no)

endif

stop

@enduml

```

#### リファクタリングのための回帰テスト <a id="SS_11_2_2_1"></a>
すでに述べたように、リファクタリング後には回帰テストが必要である。
通常、この回帰テストは、改善したソースコードをカバーする自動実行可能な単体テストや統合テスト等の、
エンジニアの工数をほとんどロスしない方法で行われる。
もし、多くの回帰テストが手作業で行われるならば、
プロジェクトがその工数負担に耐えられなくなり、以下のいずれかが発生する。

1. リファクタリングがほとんど行われなくなる。
2. ソースコード改善後、十分な回帰テストが行われなくなる。
3. 一度に大量のソースコード改善を行うようになる(回帰テストの回数を減らす)。

ソースコードの構造を改善し、自動テストを組み込めるようにするために、
上記3の方法は効果的である場合もある
(すなわち、方法3はそのソースコードのライフサイクルの中で一度だけ施行が許される)。
他の方法ではリファクタリングをプロセスに組み込むことはできない。

以上の考察から、リファクタリングのための回帰テストは、自動単体テストか自動統合テストのいずれか、
もしくは両方にならざるを得ない。
プロジェクトの進捗とともに自動統合テストは数時間～数日を要するようになるので、
実践的に考えると、自動統合テストはリファクタリングのための回帰テストには不向きである。
その結果、リファクタリング後の回帰テストには、
「修正したソースコードやその周辺をカバーする自動単体テスト」以外の選択肢はないと考えられる。

```plant_uml/refactoring_ut.pu
@startuml

:コードインスペクション;

while(ソースコードに問題がある?) is (yes)

    :ソースコード修正;
        note right
            対象ソースコードにUTがある
            ことが前提。
            ない場合は先にUTを作る。
        end note

    :UTをパスさせる;

endwhile(no)

if(ソースコードを修正した) then (yes)
:commit;
else (no)

endif

stop

@enduml


```

#### ソースコードの改善 <a id="SS_11_2_2_2"></a>
良いプログラマが書いたソースコードは、無駄がなく機能的である。
それが機能美として目に映ることもあるため、
自分や自分のチームにはそのようなソースコードは書けないと思う人がいる。
他方で、良いソースコードとはどのようなものかも知らずに、
自信満々にリファクタリングをやりたいという人もいる。

どちらの考え方も間違っている。
「[コードインスペクション](process_and_infra.md#SS_11_2_5_1_2)」で述べた観点に沿ってソースコードを読み、
その違反を確実に修正できることが、ソースコード改善の第一歩である。

これは前者が思うほど難しくもなく、後者が思うほど簡単でもない。

#### リファクタリングの例 <a id="SS_11_2_2_3"></a>
ソースコードに多くの問題があった場合でも、一度に多くの視点からの修正をしてはならない。
ステップバイステップで少しずつ改善させることを心掛けるべきである。

例えば大きすぎる関数を分割するリファクタリングを行う場合は、その分割のみに集中すべきで、
その最中に別の問題を見つけても、その修正を行ってはならない。
まずは、仕掛中のリファクタリングを終了させ、その後(コミットした後)、次の問題点に取り掛かるべきである。

以下では、そういったステップバイステップのリファクタリングを例示する。

##### オリジナルのソースコード <a id="SS_11_2_2_3_1"></a>
まずはリファクタリング前のオリジナルのソースコードを示す。

```cpp
    //  example/ref_org/main.cpp 8

    int main(int, char**)
    {
        auto strings = std::vector<std::string>{};

        for (;;) {
            auto buffer = std::string{};

            if (std::getline(std::cin, buffer)) {
                switch (buffer.at(0)) {
                case '+': {
                    auto result = std::string{do_heavy_algorithm(buffer.substr(1))};
                    strings.emplace_back(result);
                    for (auto i = 0U; i < strings.size(); i++) {
                        std::cout << strings[i] << std::endl;
                    }
                    break;
                }
                case '.':
                    // do nothing
                    break;
                case '=':
                    return 0;
                default:
                    return 1;  // error exit
                }
            }
        }

        return 0;
    }
```

上記プログラムは、

1. 標準入力から文字列を受け取り、
2. 文字列をパースし、コマンドと引数文字列に分離し、
3. 引数文字列を、時間のかかるアルゴリズムで別の文字列に変換し、
4. 変換文字列を保存し、
5. 保存した全ての変換文字列をstd::coutに出力する。

ソースコードの品質は高くないので、
すくなくとも機能追加するタイミングではリファクタリングが必要になる。

##### 機能追加によるソースコード品質劣化 <a id="SS_11_2_2_3_2"></a>
時間のかかるアルゴリズムがプログラムをブロックしてしまうので、
下記のように、この処理を(不十分ながら)非同期化した。

```cpp
    //  example/ref_async_org/main.cpp 15

    int main(int, char**)
    {
        auto         strings = std::vector<std::string>{};
        std::thread* thd     = nullptr;

        for (;;) {
            auto buffer = std::string{};

            if (std::getline(std::cin, buffer)) {
                switch (buffer.at(0)) {
                case '+': {
                    if (thd != nullptr) {
                        thd->join();
                        delete thd;
                    }

                    thd = new std::thread{[&strings, input = buffer.substr(1)] {
                        auto result = std::string{do_heavy_algorithm(input)};
                        strings.emplace_back(result);

                        for (auto i = 0U; i < strings.size(); i++) {
                            std::cout << strings[i] << std::endl;
                        }
                    }};
                    break;
                }
                case '.':
                    // ...
                }
            }
        }

        return 0;
    }
```

一般に、同期処理をそのまま非同期に変更するとソースコードは腐敗を始める。
上記ソースコードもその例に漏れず、かなり醜悪になった。

##### 小規模なリファクタリング <a id="SS_11_2_2_3_3"></a>
Null ObjectパターンやRAIIの導入で肥大化したmain関数を改善する小規模なリファクタリングを行う。

```cpp
    //  example/ref_async_r0/main.cpp 13

    int main(int, char**)
    {
        auto strings = std::vector<std::string>{};
        auto thd     = std::make_unique<std::thread>([] {});        // Null Object & RAII
        auto sg      = Nstd::ScopedGuard{[&thd] { thd->join(); }};  // RAII

        for (;;) {
            auto buffer = std::string{};

            if (std::getline(std::cin, buffer)) {
                switch (buffer[0]) {
                case '+': {
                    thd->join();
                    thd = std::make_unique<std::thread>([&strings, input = buffer.substr(1)] {
                        auto result = std::string{do_heavy_algorithm(input)};
                        strings.emplace_back(result);
                        for (auto const& str : strings) {  // 範囲for文
                            std::cout << str << std::endl;
                        }
                    });
                    break;
                }
                case '.':
                    // ...
                }
            }
        }

        return 0;
    }
```

上記例のScopedGuardは、汎用性が高くプロジェクト全体で使用できるため、別のファイルとして、
下記のように宣言、定義する(汎用性が高いクラスや関数をプロジェクト全体で共有することは良い習慣である)。

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

##### 構造のリファクタリング <a id="SS_11_2_2_3_4"></a>
前記レベルでは不十分であるため、ブロックを関数化するリファクタリングを行う。

```cpp
    //  example/ref_async_r1/main.cpp 9

    namespace {
    int main_loop()
    {
        auto strings = std::vector<std::string>{};
        auto thd     = std::thread{[] {}};                         // NullObject & RAII
        auto sg      = Nstd::ScopedGuard{[&thd] { thd.join(); }};  // RAII

        for (;;) {
            auto buffer = std::string{};

            if (std::getline(std::cin, buffer)) {
                if (auto exit_code = dispatch(thd, strings, buffer)) {
                    return *exit_code;
                }
            }
        }

        assert(false);
        return 0;
    }
    }  // namespace

    int main(int, char**) { return main_loop(); }
```

メインループ関数は、main()と同じファイルに残すが、他の関数は下記のように他のファイルで定義する。
これにより、部分的だが単体テストが導入できる。

```cpp
    //  example/ref_async_r1/lib.cpp 6

    namespace {
    void convert_store_async(std::thread& thd, std::vector<std::string>& strings, std::string const& input)
    {
        thd.join();

        thd = std::thread{[&strings, input = input] {
            auto result = std::string{do_heavy_algorithm(input)};
            strings.emplace_back(result);
            for (auto const& str : strings) {
                std::cout << str << std::endl;
            }
        }};
    }
    }  // namespace

    std::optional<int> dispatch(std::thread& thd, std::vector<std::string>& strings, std::string const& command)
    {
        switch (command[0]) {
        case '+':
            convert_store_async(thd, strings, command.substr(1));
            return std::nullopt;
        case '.':
            // do nothing
            return std::nullopt;
        case '=':
            return 0;
        default:
            return 1;
        }
    }
```

##### 単体テストの開発 <a id="SS_11_2_2_3_5"></a>
前述したように、関数やファイルを分割したことにより、
不十分なレベルではあるが単体テストを開発、実行できるようになった。

```cpp
    //  example/ref_async_r1/lib_ut.cpp 10

    TEST(RefAsyncR1, dispatch)
    {
        auto actual = std::vector<std::string>{};

        {
            auto thd = std::thread{[] {}};                   // NullObject & RAII
            auto sg  = ScopedGuard{[&thd] { thd.join(); }};  // RAII

            {
                auto exit_code = dispatch(thd, actual, "+abc");
                ASSERT_FALSE(exit_code);
            }
            {
                auto exit_code = dispatch(thd, actual, "+defg");
                ASSERT_FALSE(exit_code);
            }
            {
                auto exit_code = dispatch(thd, actual, ".");
                ASSERT_FALSE(exit_code);
            }
            {
                auto exit_code = dispatch(thd, actual, "+hijkl");
                ASSERT_FALSE(exit_code);
            }
            {
                auto exit_code = dispatch(thd, actual, "=");
                ASSERT_TRUE(exit_code);
                ASSERT_EQ(0, *exit_code);
            }
            {
                auto exit_code = dispatch(thd, actual, "?");
                ASSERT_TRUE(exit_code);
                ASSERT_NE(0, *exit_code);
            }
        }

        ASSERT_EQ((std::vector<std::string>{"ABC", "DEFG", "HIJKL"}), actual);
    }
```

scoped_guard.hに関しても、以下のように単体テストを追加する。
バグが発生しそうにないこのようなクラスに対しても単体テストを行うことは一見無駄なように見えるが、
単体テストカバレッジの管理、コードクローンの撲滅、
「[割れ窓理論](https://ja.wikipedia.org/wiki/%E5%89%B2%E3%82%8C%E7%AA%93%E7%90%86%E8%AB%96)」
等の観点から重要である。

```cpp
    //  example/programming_convention/scoped_guard_ut.cpp 8

    TEST(ScopedGuard, scoped_guard)
    {
        auto a = 0;

        {
            auto sg = ScopedGuard{[&a]() noexcept { a = 99; }};
            ASSERT_NE(99, a);  // ~ScopedGuardは呼ばれていない
        }
        ASSERT_EQ(99, a);  // ~ScopedGuardは呼ばれた
    }
```

##### クラスの導入 <a id="SS_11_2_2_3_6"></a>
このプログラムは非同期処理が必要であるため、
そういったアプリケーションとの相性が良い[MVC](design_pattern.md#SS_9_24)の導入によるリファクタリングを行う
(この程度の規模のソフトウェアにMVCを導入する必要はないが、
その導入を例示するためリファクタリングを行う)。

まずは、コマンドの非同期処理を行うクラス(== ビジネスロジック == Model)を導入する
(例としての分かりやすさを優先するためにクラス名もModelとする)。

```cpp
    //  example/ref_async_r2/main.cpp 6

    namespace {
    int main_loop()
    {
        auto model = Model{};

        for (;;) {
            auto buffer = std::string{};

            if (std::getline(std::cin, buffer)) {
                if (auto exit_code = dispatch(model, buffer)) {
                    return *exit_code;
                }
            }
        }

        assert(false);
        return 0;
    }
    }  // namespace

    int main(int, char**) { return main_loop(); }
```

以下のファイルで、Modelの宣言、定義を行う。

```cpp
    //  example/ref_async_r2/lib.h 8

    class Model {
    public:
        Model() : thd_{[] {}}, strings_{} {}
        ~Model() { thd_.join(); }
        void ConvertStoreAsync(std::string const& input);

    private:
        std::thread              thd_;
        std::vector<std::string> strings_;
    };
```

```cpp
    //  example/ref_async_r2/lib.cpp 6

    void Model::ConvertStoreAsync(std::string const& input)
    {
        thd_.join();

        thd_ = std::thread{[&sv = strings_, input = input] {
            sv.emplace_back(do_heavy_algorithm(input));

            for (auto const& str : sv) {
                std::cout << str << std::endl;
            }
        }};
    }

    std::optional<int> dispatch(Model& model, std::string const& command)
    {
        // ...
    }
```

##### 単体テストの変更 <a id="SS_11_2_2_3_7"></a>
このリファクタリングにより単体テストは以下のようになる
(以下のModelのデザインは不十分であるため、妥当な単体テストはできない)。

```cpp
    //  example/ref_async_r2/lib_ut.cpp 7

    TEST(RefAsyncR2, Model)
    {
        auto model = Model{};  // Modelのデザインが悪いために適切な単体テストは書けない

        model.ConvertStoreAsync("hehe");
    }

    TEST(RefAsyncR2, dispatch)
    {
        auto model = Model{};

        {
            auto exit_code = dispatch(model, "+abc");
            ASSERT_FALSE(exit_code);
        }
        {
            auto exit_code = dispatch(model, "+defg");
            ASSERT_FALSE(exit_code);
        }
        {
            auto exit_code = dispatch(model, ".");
            ASSERT_FALSE(exit_code);
        }
        {
            auto exit_code = dispatch(model, "+hijkl");
            ASSERT_FALSE(exit_code);
        }
        {
            auto exit_code = dispatch(model, "=");
            ASSERT_TRUE(exit_code);
            ASSERT_EQ(0, *exit_code);
        }
        {
            auto exit_code = dispatch(model, "?");
            ASSERT_TRUE(exit_code);
            ASSERT_NE(0, *exit_code);
        }
    }
```

##### MVCの導入 <a id="SS_11_2_2_3_8"></a>
非同期関数であるModel::ConvertStoreAsync()の完了がクラス外から捕捉できないことを一因として、
上記例のModelへの十分な単体テストができなかった。
この問題を解決し、単体テストのカバレッジを上げるために「[MVC](design_pattern.md#SS_9_24)」の構造を導入する。

```cpp
    //  example/ref_async_r3/main.cpp 5

    int main(int, char**)
    {
        auto view  = View{};
        auto model = Model{};
        model.Attach(view);
        auto controller = Controller{model};

        return controller.WatchInput();
    }
```

以下のファイルで、Modelの宣言、定義を行う。

```cpp
    //  example/ref_async_r3/model.h 10

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
        Model() : thd_{[] {}}, strings_{}, observers_{} {}
        ~Model() { thd_.join(); }
        void                            ConvertStoreAsync(std::string const& input);
        void                            Attach(Observer& observer);
        void                            Detach(Observer& observer);
        std::vector<std::string> const& GetStrings() const { return strings_; }

    private:
        void notify() const;

        std::thread              thd_;
        std::vector<std::string> strings_;
        std::list<Observer*>     observers_;
    };
```

```cpp
    //  example/ref_async_r3/model.cpp 4

    void Model::ConvertStoreAsync(std::string const& input)
    {
        thd_.join();

        thd_ = std::thread{[this, input = input] {
            strings_.emplace_back(do_heavy_algorithm(input));
            notify();
        }};
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

以下のファイルで、Viewの宣言、定義を行う。

```cpp
    //  example/ref_async_r3/view.h 7

    class View : public Observer {
    private:
        virtual void update(Model const& model) override;
    };
```

```cpp
    //  example/ref_async_r3/view.cpp 3

    void View::update(Model const& model)
    {
        for (auto const& str : model.GetStrings()) {
            std::cout << str << std::endl;
        }
    }
```

以下のファイルで、Controllerの宣言、定義を行う。

```cpp
    //  example/ref_async_r3/controller.h 7

    class Controller {
    public:
        explicit Controller(Model& model) : model_{model} {}

        int WatchInput();

    private:
        std::optional<int> dispatch(std::string const& command);

        Model& model_;
    };
```

```cpp
    //  example/ref_async_r3/controller.cpp 6

    int Controller::WatchInput()
    {
        for (;;) {
            auto buffer = std::string{};

            if (std::getline(std::cin, buffer)) {
                if (auto exit_code = dispatch(buffer)) {
                    return *exit_code;
                }
            }
        }

        assert(false);
        return 0;
    }

    std::optional<int> Controller::dispatch(std::string const& command)
    {
        // ...
    }
```

##### 単体テストの変更(単体テスト用クラス導入) <a id="SS_11_2_2_3_9"></a>
Observerから派生した下記のテスト用クラスViewTestを使うことにより、
ConvertStoreAsync()の完了が捕捉できるようになった。

```cpp
    //  example/h/ref_async_mock.h 10

    class ViewTest : public Observer {
    public:
        void WaitUpdate(uint32_t num) noexcept  // num回、updateが呼び出されるまでブロック
        {
            while (update_counter_ != num) {  // ポーリングは避けるべきだが、単体テストなら問題ない
                org_msec_sleep(100);
            }
        }

        uint32_t GetCount() const noexcept { return update_counter_; }

    private:
        virtual void update(Model const&) noexcept override { ++update_counter_; }

        std::atomic<uint32_t> update_counter_{0};
    };
```

これにより、Modelの単体テストは十分なレベルになったが、
下記の通り、ControllerやViewがstd::coutやstd::cinに依存しているために、
これらの単体テストの開発は困難である。

```cpp
    //  example/ref_async_r3/model_ut.cpp 10

    TEST(RefAsyncR3, Model)
    {
        auto view_test = ViewTest{};

        auto model = Model{};
        model.Attach(view_test);

        auto const input_model = std::vector<std::string>{"abc", "defg", "hijkl"};

        for (auto const& s : input_model) {
            model.ConvertStoreAsync(s);
        }

        view_test.WaitUpdate(input_model.size());

        ASSERT_EQ((std::vector<std::string>{"ABC", "DEFG", "HIJKL"}), model.GetStrings());
    }
```

```cpp
    //  example/ref_async_r3/view_ut.cpp 6

    TEST(RefAsyncR3, View)
    {
        auto view = View{};  // オブジェクト生成程度の単体テストしかできない
    }
```

```cpp
    //  example/ref_async_r3/controller_ut.cpp 8

    TEST(RefAsyncR3, Controller)
    {
        auto model      = Model{};
        auto controller = Controller{model};  // オブジェクト生成程度の単体テストしかできない
    }
```

##### DIの導入 <a id="SS_11_2_2_3_10"></a>
[DI(dependency injection)](design_pattern.md#SS_9_12)を導入することで、
Controller、Viewのstd::coutやstd::cinへの直接の依存を回避する。

下図は、DI導入前後でControllerによる「std::cinからの文字列読み込み」がどのように変更されたかを示す。

```plant_uml/refactoring_with_di.pu
@startuml

hide footbox

participant main
participant Controller
participant "std::cin"

alt not use DI

    create Controller
    main -> Controller : 生成
    Controller -> "std::cin" : getline

else use DI

    create xxxstream
    main -> xxxstream : 生成
    note right : cin, ifstream, \nistringstream等

    create Controller
    main -> Controller : 生成(xxxstream)
    
    Controller -> xxxstream : getline

end
@enduml
```

DIの導入によりmain()は以下のようになる。

```cpp
    //  example/ref_async_r4/main.cpp 5

    int main(int, char**)
    {                                                   //   修正前のソースコード
        auto view  = View{std::cout};                   // > auto view  = View{};
        auto model = Model{};                           //   auto model = Model{};
        model.Attach(view);                             //   model.Attach(view);
        auto controller = Controller{model, std::cin};  // > auto controller = Controller{model};

        return controller.WatchInput();
    }
```

Modelについては、std::cout、std::cinへの依存はないので変更しない。
Viewについては、以下のようにstd::coutへの依存を削除する。

```cpp
    //  example/ref_async_r4/view.h 7

    class View : public Observer {
    public:
        explicit View(std::ostream& os) : Observer{}, os_{os} {}

    private:
        virtual void update(Model const& model) override;

        std::ostream& os_;
    };
```

```cpp
    //  example/ref_async_r4/view.cpp 3

    void View::update(Model const& model)
    {                                                 //   修正前のソースコード
        for (auto const& str : model.GetStrings()) {  //   for (auto const& str : model.GetStrings()) {
            os_ << str << std::endl;                  // >     std::cout << str << std::endl;
        }                                             //   }
    }
```

Controllerについても、以下のようにstd::cinへの依存を削除する。

```cpp
    //  example/ref_async_r4/controller.h 7

    class Controller {
    public:
        explicit Controller(Model& model, std::istream& is) : model_{model}, is_{is} {}

        int WatchInput();

    private:
        std::optional<int> dispatch(std::string const& command);

        Model&        model_;
        std::istream& is_;
    };
```

```cpp
    //  example/ref_async_r4/controller.cpp 6

    int Controller::WatchInput()
    {
        for (;;) {
            auto buffer = std::string{};

            //                                //  修正前のソースコード
            if (std::getline(is_, buffer)) {  //  if (std::getline(std::cin, buffer)) {
                if (auto exit_code = dispatch(buffer)) {
                    return *exit_code;
                }
            }
        }

        assert(false);
        return 0;
    }

    std::optional<int> Controller::dispatch(std::string const& command)
    {
        // ...
    }
```

以上のように、

* Controllerは、インスタンスstd::cinへの依存から、std::istream型への依存へ
* Viewは、インスタンスstd::coutへの依存から、std::ostream型への依存へ

と改善された(一般にグローバルオブジェクトへの依存よりも型への依存の方が柔軟性に勝る)。
なお、std::cin、std::cout、std::istream、std::ostream等の継承関係は以下の通りであるため、
このような変更が可能となった。

```plant_uml/basic_ios.pu
@startuml
scale max 700 width

class ios_base
class basic_ios
class istream
note left : std::cinの型

class ifstream

class ostream
note right : std::coutの型

class ofstream

class iostream
class stringstream
class istringstream
class ostringstream
class fstream

basic_ios -up-|> ios_base
istream -up-|> basic_ios
ostream -up-|> basic_ios
iostream -up-|> istream
iostream -up-|> ostream

ifstream -up-|> istream
istringstream -up-|> istream
ofstream -up-|> ostream
ostringstream -up-|> ostream

fstream -up-|> iostream
stringstream -up-|> iostream


@enduml

```

##### 全クラスの単体テスト <a id="SS_11_2_2_3_11"></a>
これまでの改善によりModel、View、Controllerすべてに妥当な単体テストをすることが可能となった。

```cpp
    //  example/ref_async_r4/model_ut.cpp 11

    TEST(RefAsyncR4, Model)
    {
        auto view_test   = ViewTest{};
        auto ss_view     = std::ostringstream{};
        auto view_normal = View{ss_view};
        auto model       = Model{};

        model.Attach(view_normal);
        model.Attach(view_test);

        auto const input_model = std::vector<std::string>{"abc", "defg", "hijkl"};

        for (auto const& s : input_model) {
            model.ConvertStoreAsync(s);
        }

        view_test.WaitUpdate(input_model.size());

        ASSERT_EQ((std::vector<std::string>{"ABC", "DEFG", "HIJKL"}), model.GetStrings());

        auto ss_expect = std::ostringstream{};  // viewのテスト
        ss_expect << "ABC" << std::endl;
        ss_expect << "ABC" << std::endl << "DEFG" << std::endl;
        ss_expect << "ABC" << std::endl << "DEFG" << std::endl << "HIJKL" << std::endl;

        ASSERT_EQ(ss_expect.str(), ss_view.str());
    }
```

```cpp
    //  example/ref_async_r4/view_ut.cpp 4

    TEST(RefAsyncR4, View)
    {
        // model/controllerの単体テストで代用
    }
```

```cpp
    //  example/ref_async_r4/controller_ut.cpp 11

    TEST(RefAsyncR4, Controller)
    {
        auto view_test   = ViewTest{};
        auto ss_view     = std::ostringstream{};
        auto view_normal = View{ss_view};
        auto model       = Model{};

        model.Attach(view_test);
        model.Attach(view_normal);

        auto ss = std::stringstream{};

        ss << "+abc" << std::endl;
        ss << "+defg" << std::endl;
        ss << "." << std::endl;
        ss << "+hijkl" << std::endl;
        ss << "=" << std::endl;

        auto controller = Controller{model, ss};

        ASSERT_EQ(0, controller.WatchInput());

        auto const exp_model = std::vector<std::string>{"ABC", "DEFG", "HIJKL"};
        view_test.WaitUpdate(exp_model.size());

        ASSERT_EQ(exp_model, model.GetStrings());

        auto ss_expect = std::ostringstream{};
        ss_expect << "ABC" << std::endl;
        ss_expect << "ABC" << std::endl << "DEFG" << std::endl;
        ss_expect << "ABC" << std::endl << "DEFG" << std::endl << "HIJKL" << std::endl;

        ASSERT_EQ(ss_expect.str(), ss_view.str());

        // エラー入力テスト
        ss << "?" << std::endl;
        ASSERT_NE(0, controller.WatchInput());
    }
```

### 自動統合テスト <a id="SS_11_2_3"></a>

#### 自動統合テストとは？ <a id="SS_11_2_3_1"></a>
一般に、統合テスト(IT)とは、クラスや関数、
ライブラリ等のソフトウェア構成要素すべてを結合したプログラムの動作が、
要求仕様に沿っていることを検証するためのテストである。
統合テストはテストエンジニアやプログラマの手作業で行われることが慣例になっているが、
プログラムに少しの工夫を加えることで、その多くを自動化することができる
(プログラムにもよるが100%自動化は困難である)。
この自動化された統合テストを本ドキュメントでは自動統合テストと呼ぶ。

以下のようなテストを手作業で行うことはほぼ不可能であるが、
これらの項目を統合テストから外すこともできないため、
すべてのソフトウェア開発において自動統合テストは必須である。

* 長時間オペレーションで不具合(メモリリーク等)が出ないことの検証
* 手作業では難しい高速入力

#### 自動統合テストのための仕様追加 <a id="SS_11_2_3_2"></a>
リファクタリングの説明に使用したソースコード(「[リファクタリング](process_and_infra.md#SS_11_2_2)」参照)は、

* 複数の小さなファイルに分割され、
* MVC構造を導入され、
* すべてのクラスは十分にコンパクトで、
* すべてのクラスは単体テストを実行できる

ように改善された。
単体テストのラインカバレッジは100％に近く、動作品質という観点からも改善したが、
未だに統合テストは手作業で行わなければならない(現在の仕様では統合テストを自動化することは難しい)。

このプログラムの統合テストの自動化を難しくさせている原因は、
「標準入出力を利用し、ユーザとインタラクティブなやり取りを行う」
からである。この問題を解決するために、
「コマンド引数によりダイナミックに、標準入出力をファイル入出力へ切り替えられる」ように変更を行う
(このようなテスト機能の実現のために、#if/#endif等のプリプロセッサ命令を利用することは誤りである)。

コマンド引数の仕様(このプログラム名はref_async_r5)は下記のとおりである。

```
    ref_async_r5 [OPTIONS]
       -i <input-file>      std::cinの代わりに、<input-file>を使用する。
       -o <output-file>     std::coutの代わりに、<output-file>を使用する。
```

#### 自動統合テストのためのソースコード変更 <a id="SS_11_2_3_3"></a>
前述したオプションを備えた実装は、以下のようになる。

```cpp
    //  example/ref_async_r5/main.cpp 10

    namespace {

    void how_to_use(std::string_view program)
    {
        std::cerr << program << " [OPTIONS]" << std::endl;
        std::cerr << "   -i <input-file>" << std::endl;
        std::cerr << "   -o <output-file>" << std::endl;
    }
    }  // namespace

    int main(int argc, char** argv)
    {
        auto ret = getopt(argc, argv);
        if (!ret) {
            how_to_use(argv[0]);
            return __LINE__;
        }

        auto ios = IOStreamSelector{std::move(ret->ifile), std::move(ret->ofile)};

        if (!ios.Open()) {
            how_to_use(argv[0]);
            return __LINE__;
        }
        //                                                      //   修正前のソースコード
        auto view  = View{ios.GetOStream()};                    // > auto view  = View{std::cout};
        auto model = Model{};                                   //   auto model = {};
        model.Attach(view);                                     //   model.Attach(view);
        auto controller = Controller{model, ios.GetIStream()};  // > auto controller
                                                                //       = Controller{model, std::cin};

        return controller.WatchInput();
    }
```
```cpp
    //  example/ref_async_r5/arg.h 5

    struct opt_result {
        std::string ifile;
        std::string ofile;
    };

    std::optional<opt_result> getopt(int argc, char* const* argv);
```
```cpp
    //  example/ref_async_r5/arg.cpp 7

    std::optional<opt_result> getopt(int argc, char* const* argv)
    {
        auto opt   = int{};
        auto ifile = std::string{};
        auto ofile = std::string{};

        // ...
        return opt_result{std::move(ifile), std::move(ofile)};
    }
```

IOStreamSelectorと単体テスト用に導入した「[DI(dependency injection)](design_pattern.md#SS_9_12)」構造により、
std::istream、std::ostreamのインスタンスを選択できるようになった。

IOStreamSelectorは以下のようになる。

```cpp
    //  example/ref_async_r5/arg.h 14

    class IOStreamSelector {
    public:
        IOStreamSelector(std::string ifile, std::string ofile)
            : ifile_{std::move(ifile)}, ifs_{}, is_{nullptr}, ofile_{std::move(ofile)}, ofs_{}, os_{nullptr}
        {
        }

        bool          Open();
        std::istream& GetIStream();
        std::ostream& GetOStream();

    private:
        // ...
    };
```
```cpp
    //  example/ref_async_r5/arg.cpp 36

    namespace {
    template <typename FSTREAM, typename IOSTREAM>
    bool select_iostream(std::string const& filename, FSTREAM& fs, IOSTREAM& cin_cout, IOSTREAM*& output)
    {
        output = &cin_cout;

        if (filename.size() != 0) {
            fs.open(filename);
            if (!fs) {
                return false;
            }
            output = &fs;
        }

        return true;
    }
    }  // namespace

    bool IOStreamSelector::Open()
    {
        if (!select_iostream(ifile_, ifs_, std::cin, is_)) {
            return false;
        }

        return select_iostream(ofile_, ofs_, std::cout, os_);
    }

    std::istream& IOStreamSelector::GetIStream()
    {
        assert(is_ != nullptr);

        return *is_;
    }

    std::ostream& IOStreamSelector::GetOStream()
    {
        assert(os_ != nullptr);

        return *os_;
    }
```

#### 自動統合テスト用ソースコード変更のための単体テスト <a id="SS_11_2_3_4"></a>
追加機能に対する単体テストを以下に示す。
なお、新規単体テストはファイルの生成、書き込み、読み込みを行うため、

* 単体テストの実行前に、結果に影響を与えるファイルを削除する
* 単体テストの実行後に、単体テストで生成したファイルを削除する

を行う必要がある。

* 前者を行うのがSetUp()
* 後者を行うのがTearDown()

である。

```cpp
    //  example/ref_async_r5/arg_ut.cpp 18

    class Refactorin_5 : public ::testing::Test {  // google testクラス
    protected:
        virtual void SetUp() noexcept override
        {
            remove_file(ofilename);  // ファイルがあると、テストがエラーするので。
            remove_file(ifilename);
        }

        virtual void TearDown() noexcept override
        {
            remove_file(ofilename);  // ローカルリポジトリにゴミを残さない。
            remove_file(ifilename);
        }

        static void remove_file(std::string const& filename) noexcept
        {
            if (std::filesystem::exists(filename)) {
                std::filesystem::remove(filename);
            }
        }
    };

    TEST_F(Refactorin_5, IOStreamSelector)
    {
        {
            auto ios = IOStreamSelector{"", ofilename};

            ASSERT_TRUE(ios.Open());
            ASSERT_TRUE(&std::cin == &ios.GetIStream());
        }
        ASSERT_TRUE(std::filesystem::exists(ofilename));

        {
            {  // テスト用ファイルの作成
                auto ofs = std::ofstream{};

                ofs.open(ifilename);
                ASSERT_TRUE(ofs);

                ofs << "test";
            }
            ASSERT_TRUE(std::filesystem::exists(ifilename));

            auto ios = IOStreamSelector{ifilename, ""};

            ASSERT_TRUE(ios.Open());
            ASSERT_TRUE(&std::cout == &ios.GetOStream());

            auto file_contents = std::string{};

            ios.GetIStream() >> file_contents;
            ASSERT_EQ("test", file_contents);
        }
    }

    TEST_F(Refactorin_5, getopt)
    {
        {
            char        p[]    = "p";
            char* const argv[] = {p};

            auto ret = getopt(array_length(argv), argv);

            ASSERT_TRUE(ret);
            ASSERT_EQ("", ret.value().ifile);
            ASSERT_EQ("", ret.value().ofile);
        }
        // ...
    }
```

#### 自動統合テストの実装 <a id="SS_11_2_3_5"></a>
ref_async_r5に追加された機能をスクリプト言語(下記例ではbash)等から利用することで、
下記のような自動統合テスト(非手作業統合テスト)を開発することができる。
入力文字列や入力タイミングのバリエーションを増やすこと等によってこの方法を発展させれば、
堅固な自動統合テストにすることも可能である。

```sh
    //  example/ref_it/it.sh 45

    # $IFILEの作成
    cat << IFILE_END > $IFILE
    +abcdef
    +ddd
    +ffff
    =
    IFILE_END

    # expectの生成
    gen_expect "ABCDEF" "DDD" "FFFF" > $OFILE_EXP

    $TARGET -i $IFILE -o $OFILE_ACT

    declare -r diff_result1=$(diff $OFILE_EXP $OFILE_ACT)

    # $TARGETが正常動作すれば、文字列diff_result1の長さは0
    [[ -n "$diff_result1" ]] && exit $LINENO
```

### TDD <a id="SS_11_2_4"></a>
この章の考察に従って、単体テストをプロセスに組み込むのであれば、
ほとんどのクラス、関数は統合テスト前までに単体テストを実施されデバッグされることになる。
もしそうであるならば、この作業の流れ(クラスや関数の開発→単体テスト)
はTest driven development(TDD)を使うことでさらに効率的になる。

TDDとは、下図に示すようなプログラマのワークフローである。

```plant_uml/tdd.pu
@startuml

:実装する機能を決定;

if(新規クラスを作る) then (yes)
    :設計;
        note right
            新規クラスを宣言する("*.h"を書く)。
            その前にクラス図を描いても良い。
        end note

    :UT新規作成;
        note right
            "*.cpp"の中身がないため
            リンクエラーは解消できない。
        end note

    :"*.cpp"を書く;
        note right
            ビルドできるまで、
            UTと.cppを修正。
        end note

else(no(既存クラスの修正))
    :設計;
        note right
            該当するクラス宣言
            ("*.h")の修正を行う。
        end note

    :UTの追加;
        note right
            新規関数が追加された場合
            リンクエラーは解消できない。
        end note

    :"*.cpp"の修正;
        note right
            ビルドできるまで、
            UTと.cppを修正。
        end note
endif

if(UTはエラーするか？) then (no)
    :エラーするUTを追加;
        note right
            エラーすることでこの新規UTが
            実行されていることを確認する。
        end note
else(yes)

endif

while(UTはパスするか?) is (no)
    :UTがパスするまでデバッグ;
        note right
            UTのカバレッジが不十分ならば、
            UTの追加も行う。
        end note
endwhile(yes)

while(新規ソースコードのインスペクションを行う) is (問題あり)
    :リファクタリングを行う;
endwhile(問題なし)

:commit;

@enduml

```

これは極めて強力なプラクティスであり、TDDを習慣化することで生産性の大幅な向上が見込める。

### CI(継続的インテグレーション) <a id="SS_11_2_5"></a>
CI(continuous integration == 継続的インテグレーション)は、バージョン管理システムやそのウェブサービス、
ブランチ運用等と密接な関係を持つため、まずはこれらの説明を行う。

#### バージョン管理システム <a id="SS_11_2_5_1"></a>
バージョン管理システムは、ソフトウェア開発にとって最も重要なインフラの一つである。
従って、多彩なバージョン管理システムから何を選ぶかは、
プロジェクトの成否に大きく影響する重大な意思決定である。

機能、性能、今後の発展、情報入手の容易さ等を総合的に考えると、

* バージョン管理システムにはgit
* そのウェブサービスにはGitHub

がベストな選択であると思われる。
社内ルール等によりでGitHubが使えない場合、
GitHubと同等なgitウェブサービスをイントラネット内に構築することを推奨する。

##### gitのブランチモデル <a id="SS_11_2_5_1_1"></a>
gitは極めて自由度の高いバージョン管理システムであるため、
ブランチ運用については細心の注意が必要である。
特別な理由がない限り
[git-flow](https://nvie.com/posts/a-successful-git-branching-model/)
(A successful Git branching model)
等の世界的に評価の高い運用モデルを使用すべきである。

単純化したgit-flowを下記する。
```plant_uml/git_branching.pu
@startditaa

/-------\                                          next base code
|       |  base code(tag 1.0)                      (tag 2.0)
|master +------\ -=------------------------------------ +-------->
|cBLU   |      |                                        ^
\-------/      |                                        |
               |                                        |
               |                                        |merge
/-------\      |                                test &  |
|       |      |                                bug-fix |
|release+--=-  | -=--------------------------- *--*--*--/ -=----->
|cGRE   |      |                               ^  product release
\-------/      |                               |
               |                               |
               |branch                         |merge
/-------\      |                               |              
|       |      v       branch                  |
|develop+------*---*---+-----+-----*-----*-----/ -=-------------->
|cYEL   |              |     |     ^     ^
\-------/              |     |     |     |
                       |     |  pull-request & merge
                       v     |     |     |
        /---------\ /-----\  |     |     |       
        |         | | xxx +--|-----/     |
        |         | \-----/  v           |   
        |         |       /-----\        |     |
        |features/|       | yyy +--------/     |
        |         |       \-----/              |
        |         |             /-----\        |
        |cRED     |             | ... +-- -=---/
        \---------/             \-----/
@endditaa
```

このモデルにおける特に大切なポイントは、プロジェクト全体でシェアされる開発用ブランチdevelopと、
個別の機能開発用ブランチ(features/xxx, yyy等)を分けたことである。これにより、

* 中途半端な機能の追加によりdevelopブランチの動作が不安定になることを軽減できる。
* 上記の問題回避のために、プログラマのローカルブランチにソースコードが滞留し続けることを回避できる。
* featureブランチからdevelopブランチへのマージ前にpull-requestすることで、
  コードインスペクションの実施やその履歴管理が容易になる。

等のメリットを享受できる。

##### コードインスペクション <a id="SS_11_2_5_1_2"></a>
GitHubのようなシステムを前提とするプロセスでは、
コードインスペクションはpull-requestをトリガーとして行われる。
pull-requestとは、featureブランチをdevelopブランチへマージする直前に行われる、
ブランチ開発者からインスペクタへの依頼である。
インスペクタはこの依頼を受けると、対象コミットのコードインスペクションを行い、

* 問題ない品質であると判断した場合、pull-requestを承認する。
* 問題がある場合は、その部分を指摘し、pull-requestを却下する。

pull-requestが承認されれば、ブランチ開発者はfeatrueブランチをdevelopブランチにマージする。

ブランチ開発者は、pull-request前にその対象のコミットが、
以下のコミットクライテリアを満たしていることを保証しなければならない。

* 最新のdevelopブランチはそのfeatureブランチにマージされている
  (マージされてないと、
  この後のfeatureブランチからdevelopブランチへのマージで多くのコンフリクションが発生し、
  インスペクションが無駄になることがある)。
* 新規のクラスや関数の単体テスト、新規機能の統合テストは作られていて、パスしている。
* コミットは十分に小さい
  (様々な目的のソースコードを一度のコミットに混在させるべきではない)。

コードインスペクションは、以下のような観点で行われる。

* コミットクライテリアをクリアしているか(単体テストや自動統合テストが作られているかどうかの確認)？
* 設計上の問題点はないか？
    * [SOLID](solid.md#SS_8)等の原則に従っているか？
    * デザインパターンの使用は適切か([Accessor](design_pattern.md#SS_9_5)や[Singleton](design_pattern.md#SS_9_13)の多用は認められない等)？
* [プログラミング規約](programming_convention.md#SS_3)に従っているか？
    * 不要な依存関係はないか？ 依存関係の方向は問題ないか？
    * クラス、関数は大きすぎないか？
    * コードクローンや同型のcase文はないか？
    * 識別子やファイル名等の名前は適切か？

#### CIとは？ <a id="SS_11_2_5_2"></a>
内容を具体化、単純化するためこれまで述べてきたように、今後の説明も下記項目を前提とする
(この前提でなければCIができないという意味ではない。当然ながらsubversion等でもCIの運用は可能である)。

* バージョン管理システムにgitを使用する。
* gitウェブサービスにはGitHubか、それと同等のものを使用する。
* gitの運用は、git-flowに従う (「[gitのブランチモデル](process_and_infra.md#SS_11_2_5_1_1)」参照)。

[CI](https://ja.wikipedia.org/wiki/%E7%B6%99%E7%B6%9A%E7%9A%84%E3%82%A4%E3%83%B3%E3%83%86%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3)
とは、「すべてのプログラマは、
1日1回以上の頻度で、featrueブランチをdevelopブランチへマージしなければならない」
というプラクティスである。
developブランチが更新され次第、ビルド、単体テスト、
統合テスト等を自動で行うシステムとの併用が前提となるため、
本ドキュメントのCIとは、本来の意味に加えてこの自動システムの運用も含めた概念であると定義する
(一般にも、そのように定義していると思われる)。
また、そのシステムをCIサーバ、CIサーバが実行するジョブ項目を単にCI項目と呼ぶ。
CIサーバにはクラウドサービスを含めて様々なものがあるが、代表的なものはJenkinsである。

CIの技術的優位性は、「枝分かれしてから長時間が経過したブランチは統合(マージ)が困難である」
という前提から発生している。この前提は明らかに正しいが、
こうしないプロジェクトにはこうしない理由がある。
マージするとdevelopブランチの動作品質が下がり、チーム全体の作業が滞るからである。
この問題の対抗策がビルド、単体テスト、統合テスト等の自動実行であるため、
これらの自動化ができていないチームが、
featureブランチからdevelopブランチへのマージを頻繁に行うと悲惨な結果になる。
一方で、developブランチへのマージを頻繁に行わないチームは、いずれ困難なマージを行わざるを得なくなる。
この作業は多くのデグレードを引き起こすため、これも悲惨な結果となる。

以上をまとめると、

* developブランチへのマージを頻繁に行った方が、効率よくソフトウェア開発ができる
* そのためには、ビルド、単体テスト、統合テストの自動化ができていなければならない

ということになる。従って、

* CIは効率よいソフトウェア開発を行うための重要なファクターである

というのが結論である。

#### CIとワークフロー <a id="SS_11_2_5_3"></a>
アジャイル系プロセスに下記プラクティス

* TDD
* git-flow
* コードインスペクション(pull-request)
* CI

を組み込んだ場合、プログラマの典型的なワークフローは下図のようになる。

```plant_uml/agile_workflow.pu
@startuml

|開発者|


:featureブランチ上でのTDDによる機能開発;

repeat :pull-request前作業\n* 自己インスペクション\n* develop→featrueへのマージ\n* コード修正後には必ず全UT\n* インスペクション指摘修正;

    :pull-request;

|他の開発者|

    :インスペクション;

repeat while (pull-request承認?) is (却下)

|開発者|

:pull-request承認後、\nfeatrueブランチから\ndevelopブランチへのマージ;

|CIサーバー|

if(build/UT/IT) then (OK)
    stop
    note :機能追加完
else (ERROR)

endif
        
:チーム全員にエラー通知;

|開発者|

:問題点修正/コミット取り消し\n(CIのエラーは、チーム全体の最優先課題\nであるため解決は誰が行っても良い) ;
stop

@enduml
```

多くのアジャイル系プロセスは、このように洗練されたワークフローを前提としている。
逆にこのようなワークフローを行えないチームのアジャイル系プロセスは機能しない。
アジャイル導入の失敗例のほとんどは、こう言った問題が原因となっている。

このようなプラクティス、特に自動単体テストや自動統合テストを実践できていないチームが、
いきなりこのワークフローを身に着けることは極めて困難である。
イテレーション毎に決定される開発項目、改善項目の中にワークフローの向上に必要な項目を入れ、
ステップバイステップで改善し続けることが重要である。

#### CI項目実行の長時間化と分割 <a id="SS_11_2_5_4"></a>
CI項目には前述した

* ビルド
* 単体テスト
* 統合テスト

に加えて、

* ソースコードの静的解析(「[コード解析](code_analysis.md#SS_4)」参照)
* 各種メトリクスの計測([サイクロマティック複雑度](cpp_idioms.md#SS_21_9_8)、[凝集性の欠如](cpp_idioms.md#SS_21_9_9_1)等)
* リリースパッケージの作成

等がある。

developブランチの更新をトリガーとして行われるCI項目は、
長くても30分程度で完了できるようにするのが理想的である。
一方で、機能開発の進捗とともに、この時間制限を超えてしまう項目が出てくる
(フルビルドですら30分を超えることはめずらしくない)。

こういった場合に行われるのが、CI項目の分割である。
以下のテーブルのように、実行タイミング毎にCI項目を分けることで効率の良い運用ができる。

|実行タイミング  |develop更新後           |深夜              |週末                 |
|:---------------|:----------------------:|:----------------:|:-------------------:|
|実行時間        |30分程度                |深夜～翌朝        |金曜日深夜～月曜日朝 |
|ビルド          |差分                    |フル              |同左                 |
|単体テスト      |差分                    |あり              |同左                 |
|統合テスト      |なし/20分以内程度       |あり              |あり(長期動作系)     |
|静的解析        |なし/20分以内程度       |あり              |同左                 |
|pgk作成         |なし          　　　　　|あり              |同左                 |

#### CI項目の例 <a id="SS_11_2_5_5"></a>
CIの環境として、

* CIサーバとしてJenkins
* Jenkinsのジョブ記述にbash
* コンパイラに[g++](cpp_idioms.md#SS_21_10_1)
* ビルドツールにmake

を使用すると前提とする。この場合、

* 差分ビルド

```
    > make -j
```

* フルビルド

```
    > make clean
    > make -j
```

* 単体テスト

```
    > make ut           # sanitizerをオンにしてビルドするとより効果的
```

* 統合テスト

```
    > make it           # sanitizerをオンにしてビルドするとより効果的
```

* 静的解析

```
    > make clang        # gccの他にclangでコンパイルすることで、clangの警告機能を使う
    > scan-build make   # clangベースの静的解析ツール
```

をJenkinsジョブ記述用テキストボックスに記述すればよい(「[コード解析](code_analysis.md#SS_4)」参照)。
つまり、CIで重要なことはテスト等の項目をコマンド化することである
(従って、ビルドや単体テストをコマンドによって駆動できないIDEを使用してはならない)。

## まとめ <a id="SS_11_3"></a>
産業は、労働集約型と知識集約型に二分できる。
一般に労働集約型産業の就労者の生産性には大差がなく、
知識集約型産業の就労者の生産性には大きな差がある。
ソフトウェア産業は知識集約型であるにもかかわらず、
プログラマの月単価のような労働集約的な基準で生産性が語られることが慣行となっているが、
これはプログラマの生産性に大差がないという考えから発した誤りである。

ただし、以下のように前提することで、この誤りにも、ある程度の正当性が与えられる。

* プログラマの生産性の違いが発揮されるフェーズはプログラミングのみである。
* V字モデルでは、このフェーズの工数は全工数から見れば少ない。
* テストは、マウスをひたすらクリックするような手作業で行われるため、
  これは労働集約的な作業である。
* V字モデルでのこのフェーズの工数は、プログラミングの工数と同程度になる。

この章で解説した「ほとんどのテストはプログラミングにより自動化できる」ことを理解すれば、
この前提が成り立たないことは明らかだろう。

このことに気づいている組織は知識集約型のアプローチで、
気づかない組織は労働集約型のアプローチでソフトウェア開発を行うことになる。
どちらの生産性が高いかを議論する余地はない。

こういったことをマネージャ、リーダはよく理解するべきだろう。

[演習-プロセス分類](exercise_q.md#SS_22_10_1)  
[演習-V字モデル](exercise_q.md#SS_22_10_2)  
[演習-アジャイル](exercise_q.md#SS_22_10_3)  
[演習-自動化](exercise_q.md#SS_22_10_4)  
[演習-単体テスト](exercise_q.md#SS_22_10_5)  
[演習-リファクタリングに付随する活動](exercise_q.md#SS_22_10_6)  
[演習-リファクタリング対象コード](exercise_q.md#SS_22_10_7)  
[演習-CI](exercise_q.md#SS_22_10_8)  


