<!-- deep/md/term_explanation.md -->
# 用語解説 <a id="SS_19"></a>

この章では、このドキュメントで使用する用語の解説をする。

___

__この章の構成__

&emsp;&emsp; [組み込み型とインスタンス](term_explanation.md#SS_19_1)  
&emsp;&emsp;&emsp; [基本型](term_explanation.md#SS_19_1_1)  
&emsp;&emsp;&emsp; [組み込み型](term_explanation.md#SS_19_1_2)  
&emsp;&emsp;&emsp; [算術型](term_explanation.md#SS_19_1_3)  
&emsp;&emsp;&emsp; [汎整数型](term_explanation.md#SS_19_1_4)  
&emsp;&emsp;&emsp; [整数型](term_explanation.md#SS_19_1_5)  
&emsp;&emsp;&emsp; [算術変換](term_explanation.md#SS_19_1_6)  
&emsp;&emsp;&emsp; [汎整数型昇格](term_explanation.md#SS_19_1_7)  
&emsp;&emsp;&emsp; [汎整数型拡張](term_explanation.md#SS_19_1_8)  
&emsp;&emsp;&emsp; [浮動小数点型昇格](term_explanation.md#SS_19_1_9)  
&emsp;&emsp;&emsp; [デフォルト引数昇格](term_explanation.md#SS_19_1_10)  
&emsp;&emsp;&emsp; [縮小型変換](term_explanation.md#SS_19_1_11)  
&emsp;&emsp;&emsp; [浮動小数点型](term_explanation.md#SS_19_1_12)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点型のダイナミックレンジ](term_explanation.md#SS_19_1_12_1)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点の誤差](term_explanation.md#SS_19_1_12_2)  
&emsp;&emsp;&emsp;&emsp; [イプシロン](term_explanation.md#SS_19_1_12_3)  
&emsp;&emsp;&emsp;&emsp; [浮動小数点の演算エラー](term_explanation.md#SS_19_1_12_4)  

&emsp;&emsp; [enum](term_explanation.md#SS_19_2)  
&emsp;&emsp;&emsp; [enum class](term_explanation.md#SS_19_2_1)  
&emsp;&emsp;&emsp; [スコープドenum](term_explanation.md#SS_19_2_2)  
&emsp;&emsp;&emsp; [underlying type](term_explanation.md#SS_19_2_3)  
&emsp;&emsp;&emsp; [std::byte](term_explanation.md#SS_19_2_4)  
&emsp;&emsp;&emsp; [using enum](term_explanation.md#SS_19_2_5)  

&emsp;&emsp; [型とインスタンス](term_explanation.md#SS_19_3)  
&emsp;&emsp;&emsp; [特殊メンバ関数](term_explanation.md#SS_19_3_1)  
&emsp;&emsp;&emsp;&emsp; [ゼロの原則(Rule of Zero)](term_explanation.md#SS_19_3_1_1)  
&emsp;&emsp;&emsp;&emsp; [五の原則(Rule of Five)](term_explanation.md#SS_19_3_1_2)  

&emsp;&emsp;&emsp; [トリビアル型](term_explanation.md#SS_19_3_2)  
&emsp;&emsp;&emsp; [トリビアルに破壊可能な型](term_explanation.md#SS_19_3_3)  
&emsp;&emsp;&emsp; [標準レイアウト型](term_explanation.md#SS_19_3_4)  
&emsp;&emsp;&emsp; [集成体](term_explanation.md#SS_19_3_5)  
&emsp;&emsp;&emsp; [POD](term_explanation.md#SS_19_3_6)  
&emsp;&emsp;&emsp; [不完全型](term_explanation.md#SS_19_3_7)  
&emsp;&emsp;&emsp; [完全型](term_explanation.md#SS_19_3_8)  
&emsp;&emsp;&emsp; [ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)  
&emsp;&emsp;&emsp; [オーバーライドとオーバーロードの違い](term_explanation.md#SS_19_3_10)  
&emsp;&emsp;&emsp; [RTTI](term_explanation.md#SS_19_3_11)  
&emsp;&emsp;&emsp;&emsp; [dynamic_cast](term_explanation.md#SS_19_3_11_1)  
&emsp;&emsp;&emsp;&emsp; [typeid](term_explanation.md#SS_19_3_11_2)  
&emsp;&emsp;&emsp;&emsp; [std::type_info](term_explanation.md#SS_19_3_11_3)  

&emsp;&emsp;&emsp; [Run-time Type Information](term_explanation.md#SS_19_3_12)  
&emsp;&emsp;&emsp; [インターフェースクラス](term_explanation.md#SS_19_3_13)  
&emsp;&emsp;&emsp; [constインスタンス](term_explanation.md#SS_19_3_14)  

&emsp;&emsp; [constexpr](term_explanation.md#SS_19_4)  
&emsp;&emsp;&emsp; [constexpr定数](term_explanation.md#SS_19_4_1)  
&emsp;&emsp;&emsp; [constexpr関数](term_explanation.md#SS_19_4_2)  
&emsp;&emsp;&emsp; [コア定数式](term_explanation.md#SS_19_4_3)  
&emsp;&emsp;&emsp; [リテラル型](term_explanation.md#SS_19_4_4)  
&emsp;&emsp;&emsp; [constexprインスタンス](term_explanation.md#SS_19_4_5)  
&emsp;&emsp;&emsp; [consteval](term_explanation.md#SS_19_4_6)  
&emsp;&emsp;&emsp; [constexprラムダ](term_explanation.md#SS_19_4_7)  

&emsp;&emsp; [オブジェクトと生成](term_explanation.md#SS_19_5)  
&emsp;&emsp;&emsp; [リスト初期化](term_explanation.md#SS_19_5_1)  
&emsp;&emsp;&emsp; [一様初期化](term_explanation.md#SS_19_5_2)  
&emsp;&emsp;&emsp; [初期化子リストコンストラクタ](term_explanation.md#SS_19_5_3)  
&emsp;&emsp;&emsp; [継承コンストラクタ](term_explanation.md#SS_19_5_4)  
&emsp;&emsp;&emsp; [委譲コンストラクタ](term_explanation.md#SS_19_5_5)  
&emsp;&emsp;&emsp; [非静的なメンバ変数の初期化](term_explanation.md#SS_19_5_6)  
&emsp;&emsp;&emsp;&emsp; [NSDMI](term_explanation.md#SS_19_5_6_1)  
&emsp;&emsp;&emsp;&emsp; [初期化子リストでの初期化](term_explanation.md#SS_19_5_6_2)  
&emsp;&emsp;&emsp;&emsp; [コンストラクタ内での非静的なメンバ変数の初期値の代入](term_explanation.md#SS_19_5_6_3)  

&emsp;&emsp;&emsp; [オブジェクトの所有権](term_explanation.md#SS_19_5_7)  
&emsp;&emsp;&emsp;&emsp; [オブジェクトの排他所有](term_explanation.md#SS_19_5_7_1)  
&emsp;&emsp;&emsp;&emsp; [オブジェクトの共有所有](term_explanation.md#SS_19_5_7_2)  
&emsp;&emsp;&emsp;&emsp; [オブジェクトの循環所有](term_explanation.md#SS_19_5_7_3)  
&emsp;&emsp;&emsp;&emsp; [std::weak_ptr](term_explanation.md#SS_19_5_7_4)  

&emsp;&emsp;&emsp; [オブジェクトのライフタイム](term_explanation.md#SS_19_5_8)  
&emsp;&emsp;&emsp; [オブジェクトのコピー](term_explanation.md#SS_19_5_9)  
&emsp;&emsp;&emsp;&emsp; [シャローコピー](term_explanation.md#SS_19_5_9_1)  
&emsp;&emsp;&emsp;&emsp; [ディープコピー](term_explanation.md#SS_19_5_9_2)  
&emsp;&emsp;&emsp;&emsp; [スライシング](term_explanation.md#SS_19_5_9_3)  

&emsp;&emsp; [リテラル](term_explanation.md#SS_19_6)  
&emsp;&emsp;&emsp; [生文字列リテラル](term_explanation.md#SS_19_6_1)  
&emsp;&emsp;&emsp; [2進数リテラル](term_explanation.md#SS_19_6_2)  
&emsp;&emsp;&emsp; [数値リテラル](term_explanation.md#SS_19_6_3)  
&emsp;&emsp;&emsp; [ワイド文字列](term_explanation.md#SS_19_6_4)  
&emsp;&emsp;&emsp; [16進浮動小数点数リテラル](term_explanation.md#SS_19_6_5)  
&emsp;&emsp;&emsp; [ユーザー定義リテラル](term_explanation.md#SS_19_6_6)  
&emsp;&emsp;&emsp;&emsp; [ユーザ定義リテラル演算子](term_explanation.md#SS_19_6_6_1)  
&emsp;&emsp;&emsp;&emsp; [std::string型リテラル](term_explanation.md#SS_19_6_6_2)  
&emsp;&emsp;&emsp;&emsp; [std::chronoのリテラル](term_explanation.md#SS_19_6_6_3)  
&emsp;&emsp;&emsp;&emsp; [std::complexリテラル](term_explanation.md#SS_19_6_6_4)  

&emsp;&emsp;&emsp; [==演算子](term_explanation.md#SS_19_6_7)  
&emsp;&emsp;&emsp;&emsp; [メンバ==演算子](term_explanation.md#SS_19_6_7_1)  
&emsp;&emsp;&emsp;&emsp; [非メンバ==演算子](term_explanation.md#SS_19_6_7_2)  

&emsp;&emsp;&emsp; [比較演算子](term_explanation.md#SS_19_6_8)  
&emsp;&emsp;&emsp;&emsp; [std::rel_ops](term_explanation.md#SS_19_6_8_1)  
&emsp;&emsp;&emsp;&emsp; [std::tuppleを使用した比較演算子の実装方法](term_explanation.md#SS_19_6_8_2)  
&emsp;&emsp;&emsp;&emsp; [<=>演算子](term_explanation.md#SS_19_6_8_3)  
&emsp;&emsp;&emsp;&emsp; [三方比較演算子](term_explanation.md#SS_19_6_8_4)  
&emsp;&emsp;&emsp;&emsp; [spaceship operator](term_explanation.md#SS_19_6_8_5)  

&emsp;&emsp; [構文](term_explanation.md#SS_19_7)  
&emsp;&emsp;&emsp; [属性構文](term_explanation.md#SS_19_7_1)  
&emsp;&emsp;&emsp; [関数tryブロック](term_explanation.md#SS_19_7_2)  
&emsp;&emsp;&emsp; [範囲for文](term_explanation.md#SS_19_7_3)  
&emsp;&emsp;&emsp; [構造化束縛](term_explanation.md#SS_19_7_4)  
&emsp;&emsp;&emsp; [初期化付きif/switch文](term_explanation.md#SS_19_7_5)  
&emsp;&emsp;&emsp;&emsp; [初期化付きfor文(従来のfor文)](term_explanation.md#SS_19_7_5_1)  
&emsp;&emsp;&emsp;&emsp; [初期化付きwhile文(従来のwhile文)](term_explanation.md#SS_19_7_5_2)  
&emsp;&emsp;&emsp;&emsp; [初期化付きif文](term_explanation.md#SS_19_7_5_3)  
&emsp;&emsp;&emsp;&emsp; [初期化付きswitch文](term_explanation.md#SS_19_7_5_4)  

&emsp;&emsp; [言語機能](term_explanation.md#SS_19_8)  
&emsp;&emsp;&emsp; [コルーチン](term_explanation.md#SS_19_8_1)  
&emsp;&emsp;&emsp;&emsp; [co_await](term_explanation.md#SS_19_8_1_1)  
&emsp;&emsp;&emsp;&emsp; [co_return](term_explanation.md#SS_19_8_1_2)  
&emsp;&emsp;&emsp;&emsp; [co_yield](term_explanation.md#SS_19_8_1_3)  

&emsp;&emsp;&emsp; [モジュール](term_explanation.md#SS_19_8_2)  
&emsp;&emsp;&emsp; [ラムダ式](term_explanation.md#SS_19_8_3)  
&emsp;&emsp;&emsp;&emsp; [クロージャ](term_explanation.md#SS_19_8_3_1)  
&emsp;&emsp;&emsp;&emsp; [クロージャ型](term_explanation.md#SS_19_8_3_2)  
&emsp;&emsp;&emsp;&emsp; [一時的ラムダ](term_explanation.md#SS_19_8_3_3)  
&emsp;&emsp;&emsp;&emsp; [transient lambda](term_explanation.md#SS_19_8_3_4)  

&emsp;&emsp;&emsp; [指示付き初期化](term_explanation.md#SS_19_8_4)  

&emsp;&emsp; [プログラミング概念と標準ライブラリ](term_explanation.md#SS_19_9)  
&emsp;&emsp;&emsp; [スマートポインタ](term_explanation.md#SS_19_9_1)  
&emsp;&emsp;&emsp; [コンテナ](term_explanation.md#SS_19_9_2)  
&emsp;&emsp;&emsp;&emsp; [シーケンスコンテナ(Sequence Containers)](term_explanation.md#SS_19_9_2_1)  
&emsp;&emsp;&emsp;&emsp; [連想コンテナ(Associative Containers)](term_explanation.md#SS_19_9_2_2)  
&emsp;&emsp;&emsp;&emsp; [無順序連想コンテナ(Unordered Associative Containers)](term_explanation.md#SS_19_9_2_3)  
&emsp;&emsp;&emsp;&emsp; [コンテナアダプタ(Container Adapters)](term_explanation.md#SS_19_9_2_4)  
&emsp;&emsp;&emsp;&emsp; [特殊なコンテナ](term_explanation.md#SS_19_9_2_5)  

&emsp;&emsp;&emsp; [std::optional](term_explanation.md#SS_19_9_3)  
&emsp;&emsp;&emsp;&emsp; [戻り値の無効表現](term_explanation.md#SS_19_9_3_1)  
&emsp;&emsp;&emsp;&emsp; [オブジェクトの遅延初期化](term_explanation.md#SS_19_9_3_2)  

&emsp;&emsp;&emsp; [std::variant](term_explanation.md#SS_19_9_4)  

&emsp;&emsp; [name lookupと名前空間](term_explanation.md#SS_19_10)  
&emsp;&emsp;&emsp; [ルックアップ](term_explanation.md#SS_19_10_1)  
&emsp;&emsp;&emsp; [name lookup](term_explanation.md#SS_19_10_2)  
&emsp;&emsp;&emsp; [two phase name lookup](term_explanation.md#SS_19_10_3)  
&emsp;&emsp;&emsp; [実引数依存探索](term_explanation.md#SS_19_10_4)  
&emsp;&emsp;&emsp; [ADL](term_explanation.md#SS_19_10_5)  
&emsp;&emsp;&emsp; [関連名前空間](term_explanation.md#SS_19_10_6)  
&emsp;&emsp;&emsp; [修飾付き関数呼び出し](term_explanation.md#SS_19_10_7)  
&emsp;&emsp;&emsp; [hidden-friend関数](term_explanation.md#SS_19_10_8)  
&emsp;&emsp;&emsp; [name-hiding](term_explanation.md#SS_19_10_9)  
&emsp;&emsp;&emsp; [ダイヤモンド継承](term_explanation.md#SS_19_10_10)  
&emsp;&emsp;&emsp; [仮想継承](term_explanation.md#SS_19_10_11)  
&emsp;&emsp;&emsp; [仮想基底](term_explanation.md#SS_19_10_12)  
&emsp;&emsp;&emsp; [ドミナンス](term_explanation.md#SS_19_10_13)  
&emsp;&emsp;&emsp;&emsp; [ダイヤモンド継承を含まない場合](term_explanation.md#SS_19_10_13_1)  
&emsp;&emsp;&emsp;&emsp; [ダイヤモンド継承かつそれが仮想継承でない場合](term_explanation.md#SS_19_10_13_2)  
&emsp;&emsp;&emsp;&emsp; [ダイヤモンド継承かつそれが仮想継承である場合](term_explanation.md#SS_19_10_13_3)  

&emsp;&emsp;&emsp; [using宣言](term_explanation.md#SS_19_10_14)  
&emsp;&emsp;&emsp; [usingディレクティブ](term_explanation.md#SS_19_10_15)  

&emsp;&emsp; [template強化機能](term_explanation.md#SS_19_11)  
&emsp;&emsp;&emsp; [SFINAE](term_explanation.md#SS_19_11_1)  
&emsp;&emsp;&emsp; [コンセプト](term_explanation.md#SS_19_11_2)  
&emsp;&emsp;&emsp; [畳み込み式](term_explanation.md#SS_19_11_3)  
&emsp;&emsp;&emsp; [ジェネリックラムダ](term_explanation.md#SS_19_11_4)  
&emsp;&emsp;&emsp; [クラステンプレートのテンプレート引数の型推論](term_explanation.md#SS_19_11_5)  
&emsp;&emsp;&emsp; [テンプレートの型推論ガイド](term_explanation.md#SS_19_11_6)  
&emsp;&emsp;&emsp; [変数テンプレート](term_explanation.md#SS_19_11_7)  
&emsp;&emsp;&emsp; [エイリアステンプレート](term_explanation.md#SS_19_11_8)  
&emsp;&emsp;&emsp; [constexpr if文](term_explanation.md#SS_19_11_9)  
&emsp;&emsp;&emsp; [autoパラメータによる関数テンプレートの簡易定義](term_explanation.md#SS_19_11_10)  

&emsp;&emsp; [型推論](term_explanation.md#SS_19_12)  
&emsp;&emsp;&emsp; [AAAスタイル](term_explanation.md#SS_19_12_1)  
&emsp;&emsp;&emsp; [decltype](term_explanation.md#SS_19_12_2)  
&emsp;&emsp;&emsp; [decltype(auto)](term_explanation.md#SS_19_12_3)  
&emsp;&emsp;&emsp; [戻り値型を後置する関数宣言](term_explanation.md#SS_19_12_4)  
&emsp;&emsp;&emsp; [関数の戻り値型auto](term_explanation.md#SS_19_12_5)  
&emsp;&emsp;&emsp; [後置戻り値型auto](term_explanation.md#SS_19_12_6)  

&emsp;&emsp; [explicit](term_explanation.md#SS_19_13)  
&emsp;&emsp;&emsp; [暗黙の型変換](term_explanation.md#SS_19_13_1)  
&emsp;&emsp;&emsp; [暗黙の型変換抑止](term_explanation.md#SS_19_13_2)  
&emsp;&emsp;&emsp; [explicit type operator()](term_explanation.md#SS_19_13_3)  
&emsp;&emsp;&emsp; [explicit(COND)](term_explanation.md#SS_19_13_4)  

&emsp;&emsp; [expressionと値カテゴリ](term_explanation.md#SS_19_14)  
&emsp;&emsp;&emsp; [expression](term_explanation.md#SS_19_14_1)  
&emsp;&emsp;&emsp; [lvalue](term_explanation.md#SS_19_14_2)  
&emsp;&emsp;&emsp; [rvalue](term_explanation.md#SS_19_14_3)  
&emsp;&emsp;&emsp;&emsp; [xvalue](term_explanation.md#SS_19_14_3_1)  
&emsp;&emsp;&emsp;&emsp; [prvalue](term_explanation.md#SS_19_14_3_2)  

&emsp;&emsp;&emsp; [rvalue修飾](term_explanation.md#SS_19_14_4)  
&emsp;&emsp;&emsp; [lvalue修飾](term_explanation.md#SS_19_14_5)  
&emsp;&emsp;&emsp; [リファレンス修飾](term_explanation.md#SS_19_14_6)  

&emsp;&emsp; [リファレンス](term_explanation.md#SS_19_15)  
&emsp;&emsp;&emsp; [ユニバーサルリファレンス](term_explanation.md#SS_19_15_1)  
&emsp;&emsp;&emsp; [forwardingリファレンス](term_explanation.md#SS_19_15_2)  
&emsp;&emsp;&emsp; [perfect forwarding](term_explanation.md#SS_19_15_3)  
&emsp;&emsp;&emsp; [リファレンスcollapsing](term_explanation.md#SS_19_15_4)  
&emsp;&emsp;&emsp; [danglingリファレンス](term_explanation.md#SS_19_15_5)  
&emsp;&emsp;&emsp; [danglingポインタ](term_explanation.md#SS_19_15_6)  

&emsp;&emsp; [エクセプション安全性の保証](term_explanation.md#SS_19_16)  
&emsp;&emsp;&emsp; [no-fail保証](term_explanation.md#SS_19_16_1)  
&emsp;&emsp;&emsp; [強い安全性の保証](term_explanation.md#SS_19_16_2)  
&emsp;&emsp;&emsp; [基本的な安全性の保証](term_explanation.md#SS_19_16_3)  
&emsp;&emsp;&emsp; [noexcept](term_explanation.md#SS_19_16_4)  
&emsp;&emsp;&emsp; [exception-unfriendly](term_explanation.md#SS_19_16_5)  

&emsp;&emsp; [シンタックス、セマンティクス](term_explanation.md#SS_19_17)  
&emsp;&emsp;&emsp; [等価性のセマンティクス](term_explanation.md#SS_19_17_1)  
&emsp;&emsp;&emsp; [copyセマンティクス](term_explanation.md#SS_19_17_2)  
&emsp;&emsp;&emsp; [moveセマンティクス](term_explanation.md#SS_19_17_3)  
&emsp;&emsp;&emsp; [MoveAssignable要件](term_explanation.md#SS_19_17_4)  
&emsp;&emsp;&emsp; [CopyAssignable要件](term_explanation.md#SS_19_17_5)  

&emsp;&emsp; [C++その他](term_explanation.md#SS_19_18)  
&emsp;&emsp;&emsp; [型特性キーワード](term_explanation.md#SS_19_18_1)  
&emsp;&emsp;&emsp;&emsp; [alignof](term_explanation.md#SS_19_18_1_1)  
&emsp;&emsp;&emsp;&emsp; [alignas](term_explanation.md#SS_19_18_1_2)  
&emsp;&emsp;&emsp;&emsp; [addressof](term_explanation.md#SS_19_18_1_3)  

&emsp;&emsp;&emsp; [演算子のオペランドの評価順位](term_explanation.md#SS_19_18_2)  
&emsp;&emsp;&emsp; [実引数/仮引数](term_explanation.md#SS_19_18_3)  
&emsp;&emsp;&emsp; [単純代入](term_explanation.md#SS_19_18_4)  
&emsp;&emsp;&emsp; [ill-formed](term_explanation.md#SS_19_18_5)  
&emsp;&emsp;&emsp; [well-formed](term_explanation.md#SS_19_18_6)  
&emsp;&emsp;&emsp; [未定義動作](term_explanation.md#SS_19_18_7)  
&emsp;&emsp;&emsp; [未規定動作](term_explanation.md#SS_19_18_8)  
&emsp;&emsp;&emsp; [未定義動作と未規定動作](term_explanation.md#SS_19_18_9)  
&emsp;&emsp;&emsp; [被修飾型](term_explanation.md#SS_19_18_10)  
&emsp;&emsp;&emsp; [one-definition rule](term_explanation.md#SS_19_18_11)  
&emsp;&emsp;&emsp; [ODR](term_explanation.md#SS_19_18_12)  
&emsp;&emsp;&emsp; [RVO(Return Value Optimization)](term_explanation.md#SS_19_18_13)  
&emsp;&emsp;&emsp; [SSO(Small String Optimization)](term_explanation.md#SS_19_18_14)  
&emsp;&emsp;&emsp; [heap allocation elision](term_explanation.md#SS_19_18_15)  
&emsp;&emsp;&emsp; [Most Vexing Parse](term_explanation.md#SS_19_18_16)  
&emsp;&emsp;&emsp; [トライグラフ](term_explanation.md#SS_19_18_17)  

&emsp;&emsp; [C++コンパイラ](term_explanation.md#SS_19_19)  
&emsp;&emsp;&emsp; [g++](term_explanation.md#SS_19_19_1)  
&emsp;&emsp;&emsp; [clang++](term_explanation.md#SS_19_19_2)  

&emsp;&emsp; [ソフトウェア一般](term_explanation.md#SS_19_20)  
&emsp;&emsp;&emsp; [フリースタンディング環境](term_explanation.md#SS_19_20_1)  
&emsp;&emsp;&emsp; [サイクロマティック複雑度](term_explanation.md#SS_19_20_2)  
&emsp;&emsp;&emsp; [凝集度](term_explanation.md#SS_19_20_3)  
&emsp;&emsp;&emsp;&emsp; [凝集度の欠如](term_explanation.md#SS_19_20_3_1)  
&emsp;&emsp;&emsp;&emsp; [LCOMの評価基準](term_explanation.md#SS_19_20_3_2)  

&emsp;&emsp;&emsp; [Spurious Wakeup](term_explanation.md#SS_19_20_4)  
&emsp;&emsp;&emsp; [副作用](term_explanation.md#SS_19_20_5)  
&emsp;&emsp;&emsp; [is-a](term_explanation.md#SS_19_20_6)  
&emsp;&emsp;&emsp; [has-a](term_explanation.md#SS_19_20_7)  
&emsp;&emsp;&emsp; [is-implemented-in-terms-of](term_explanation.md#SS_19_20_8)  
&emsp;&emsp;&emsp;&emsp; [public継承によるis-implemented-in-terms-of](term_explanation.md#SS_19_20_8_1)  
&emsp;&emsp;&emsp;&emsp; [private継承によるis-implemented-in-terms-of](term_explanation.md#SS_19_20_8_2)  
&emsp;&emsp;&emsp;&emsp; [コンポジションによる(has-a)is-implemented-in-terms-of](term_explanation.md#SS_19_20_8_3)  

&emsp;&emsp; [非ソフトウェア用語](term_explanation.md#SS_19_21)  
&emsp;&emsp;&emsp; [割れ窓理論](term_explanation.md#SS_19_21_1)  
&emsp;&emsp;&emsp; [車輪の再発明](term_explanation.md#SS_19_21_2)  
  
  

[このドキュメントの構成](introduction.md#SS_1_7)に戻る。  

___

## 組み込み型とインスタンス <a id="SS_19_1"></a>

### 基本型 <a id="SS_19_1_1"></a>
基本型(fundamental types)は、C++の標準で定義されている型で、
特別なキーワードを使用して直接宣言できる型の総称である。
[組み込み型](term_explanation.md#SS_19_1_2)とも呼ばれることもある。

基本型は以下のに示した型によって構成される。

* [算術型](term_explanation.md#SS_19_1_3)
* [汎整数型](term_explanation.md#SS_19_1_4)
* [浮動小数点型](term_explanation.md#SS_19_1_12)
* void
* 上記した型のポインタ型

注:  
リファレンスは基本型に含まれない。

### 組み込み型 <a id="SS_19_1_2"></a>
組み込み型(built-in types)は[基本型](term_explanation.md#SS_19_1_1)(fundamental types)の別称。

### 算術型 <a id="SS_19_1_3"></a>
算術型とは下記の型の総称である。

* [汎整数型](term_explanation.md#SS_19_1_4)(bool, char, int, unsigned int, long long等)
* [浮動小数点型](term_explanation.md#SS_19_1_12)(float、double、long double)

算術型のサイズは下記のように規定されている。

* 1 == sizeof(bool) == sizeof(char)
* sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)
* 4 <= sizeof(long)
* 8 <= sizeof(long long)
* 4 == sizeof(float)
* 8 == sizeof(double) <= sizeof(long double)

### 汎整数型 <a id="SS_19_1_4"></a>
汎整数型とは下記の型の総称である。

* 論理型(bool)
* 文字型(char、wchar_t等)
* [整数型](term_explanation.md#SS_19_1_5)(int、unsigned int、long等)

### 整数型 <a id="SS_19_1_5"></a>
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

### 算術変換 <a id="SS_19_1_6"></a>
C++における算術変換とは、算術演算の1つのオペランドが他のオペランドと同じ型でない場合、
1つのオペランドを他のオペランドと同じ型に変換するプロセスのことを指す。

算術変換は、[汎整数型昇格](term_explanation.md#SS_19_1_7)と通常算術変換に分けられる。

```cpp
    //  example/term_explanation/integral_promotion_ut.cpp 11

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

[一様初期化](term_explanation.md#SS_19_5_2)を使用することで、
変数定義時の算術変換による意図しない値の変換([縮小型変換](term_explanation.md#SS_19_1_11))を防ぐことができる。

```cpp
    //  example/term_explanation/integral_promotion_ut.cpp 62

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
    //  example/term_explanation/integral_promotion_ut.cpp 81

    int          i{-1};
    unsigned int ui{1};

    // ASSERT_TRUE(i < ui);
    ASSERT_TRUE(i > ui);  // 算術変換の影響で、-1 < 1が成立しない

    signed short   s{-1};
    unsigned short us{1};

    ASSERT_TRUE(s < us);  // 汎整数拡張により、-1 < 1が成立
```

### 汎整数型昇格 <a id="SS_19_1_7"></a>
bool、char、signed char、unsigned char、short、unsigned short型の変数が、
算術のオペランドとして使用される場合、

* その変数の型の取り得る値全てがintで表現できるのならば、int型に変換される。
* そうでなければ、その変数はunsigned int型に変換される。

この変換を汎整数型昇格(integral promotion)と呼ぶ。

従って、sizof(short) < sizeof(int)である処理系では、
bool、char、signed char、unsigned char、short、unsigned short型の変数は、
下記のようにintに変換される。

```cpp
    //  example/term_explanation/integral_promotion_ut.cpp 100

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

### 汎整数型拡張 <a id="SS_19_1_8"></a>
汎整数型拡張とは[汎整数型昇格](term_explanation.md#SS_19_1_7)と同じ概念を指す。

### 浮動小数点型昇格 <a id="SS_19_1_9"></a>
浮動小数点型昇格とは、float型とdouble型の演算で、
float型オブジェクトがdoulbe型に変換されることを指す。

```cpp
    //  example/term_explanation/integral_promotion_ut.cpp 126

    double d = 0.05;  // 0.05は循環少数
    float  f = 0.05f;

    bool b1 = d == f;  // fはdoubleに昇格
    ASSERT_FALSE(b1);  // 0.05は循環少数であるため、0.5と0.5fは異なる。

    bool b2 = std::abs(d - f) <= std::numeric_limits<decltype(d - f)>::epsilon();
    ASSERT_FALSE(b2);  // dとfの差はdoubleのイプシロンには収まらない。
```

### デフォルト引数昇格 <a id="SS_19_1_10"></a>
デフォルト引数昇格(Default Argument Promotions)とは、可変長引数`(...)`や、
プロトタイプを持たない関数に[算術型](term_explanation.md#SS_19_1_3)引数を渡す際に適用される昇格ルールの総称である。

デフォルト引数昇格には以下が含まれる。

- [汎整数型昇格](term_explanation.md#SS_19_1_7)
- [浮動小数点型昇格](term_explanation.md#SS_19_1_9)

### 縮小型変換 <a id="SS_19_1_11"></a>
縮小型変換(Narrowing Conversion) とは、あるデータ型から別のデータ型に変換する際に、
変換先の型が元の型の表現範囲を完全にカバーしていない場合に発生する変換を指す。
主に[整数型](term_explanation.md#SS_19_1_5)や[浮動小数点型](term_explanation.md#SS_19_1_12)などの値を小さな範囲の型に変換する際に起こる。

```cpp
    //  example/term_explanation/etc_ut.cpp 43

    int32_t large  = 300;
    int8_t  small  = large;  // 縮小型変換
    bool    b      = large;
    double  d      = large;  // 単単なる型変換(縮小ではない)
    int32_t large2 = d;      // 縮小型変換

    // large = int32_t{d};   縮小型変換回避のためリスト初期化の使用。コンパイルエラー
```

[リスト初期化](term_explanation.md#SS_19_5_1)を使うことで、このような変換によるバグの発生を防ぐことができる。


### 浮動小数点型 <a id="SS_19_1_12"></a>
浮動小数点型は以下の型の総称である。

* `float`
* `double`
* `long double`

浮動小数点の仕様は、IEEE 754標準に準拠している。
この標準は、浮動小数点演算の表現方法、精度、丸め方法、および例外処理を規定しており、
広く使用されている。

#### 浮動小数点型のダイナミックレンジ <a id="SS_19_1_12_1"></a>

| 型                          | 正の最小値                    | 正の最大値                    |
|:----------------------------|:------------------------------|:------------------------------|
| `float`                     | 1.175494351 e-38              | 3.402823466 e+38              |
| `double`                    | 2.2250738585072014 e-308      | 1.7976931348623158 e+308      |
| `long double`               | 3.36210314311209350626 e-4932 | 1.18973149535723176502 e+4932 |
| `int32_t`                   | -2,147,483,648                | 2,147,483,647                 |
| `int64_t`                   | -9,223,372,036,854,775,808    | 9,223,372,036,854,775,807     |

ここで`long double`の最小値と最大値は、システムやコンパイラに依存して異なる場合がある点に留意する。

#### 浮動小数点の誤差 <a id="SS_19_1_12_2"></a>
浮動小数点変数の10進数の表現が2進数では循環小数となる場合があり、
正確に表現できないことがある。これにより、計算結果がわずかに異なる値を返す場合がある。
浮動小数点誤差は、特に計算の繰り返しや桁数の多い計算で顕著になる。

以下のコードにより誤差が容易に発生することを示す。

```cpp
    //  example/term_explanation/float_ut.cpp 12

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    //  ASSERT_EQ(0.05F, a + b);  // NG  a + b == 0.05Fは一般には成立しない。
    ASSERT_NE(0.05F, a + b);
```

#### イプシロン <a id="SS_19_1_12_3"></a>
イプシロン(epsilon)とは、ある浮動小数点数に対して「1」を加えた時に、
異なる値として識別できる最小の差分を指す。
つまり、イプシロンは浮動小数点数の精度を示す尺度である。

任意の浮動小数点変数a, bがあり、`|a - b| <= epsilon`であった場合、
浮動小数点の仕組みではa、bの差が無いものと考えて、aとbが同値であると考えることが一般的である。

イプシロンを使用した浮動小数点変数の同値判定のコード例を以下に示す。

```cpp
    //  example/term_explanation/float_ut.cpp 24

    // 下記の0.01は2進数では循環小数となるため、実数の0.01とは異なる。
    constexpr auto a = 0.01F;  // 0.0000001010001111...
    constexpr auto b = 0.04F;  // 0.0000101000111101...

    bool is_equal = 0.05F == (a + b);
    ASSERT_FALSE(is_equal);  // is_equalはtrueにはならない

    bool is_nearly_equal = std::abs(0.05F - (a + b)) <= std::numeric_limits<float>::epsilon();
    ASSERT_TRUE(is_nearly_equal);  // 浮動小数点の同値はこのように判定する
```

#### 浮動小数点の演算エラー <a id="SS_19_1_12_4"></a>
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
    //  example/term_explanation/float_ut.cpp 43

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

## enum <a id="SS_19_2"></a>
C++03までのenumは定数を分かりやすい名前で定義するための記法である。
このドキュメントでは、[スコープドenum](term_explanation.md#SS_19_2_2)に対して、C++03までのenumを非スコープドenum、
通常のenum、あるいは単にenumと呼ぶことがある。
C++03までのenumには、以下のような問題があった。

* スコープの制限: 名前付きスコープ内に定義するためには、クラスのメンバとして定義しなければならない。
* 型安全性: enumの値は整数型と暗黙の変換が行われてしまう。
* 名前空間の汚染: グローバルスコープに定義されたenumは、名前空間を汚染する。

```cpp
    //  example/term_explanation/enum_ut.cpp 14

    enum DayOfWeek { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

    ASSERT_TRUE(1 == Monday);  // intへの暗黙の変換

    enum Color { Red, Green, Blue };

    ASSERT_TRUE(Green == Monday);  // 別のenumが比較できてしまう
```

### enum class <a id="SS_19_2_1"></a>
enum classは通常の[enum](term_explanation.md#SS_19_2)の問題を解決するためにC++11から導入された。

```cpp
    //  example/term_explanation/enum_ut.cpp 29

    enum class DayOfWeek { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

    // ASSERT_TRUE(1 == Monday);  // intへの暗黙の変換できないため、コンパイルエラー
    ASSERT_TRUE(1 == static_cast<int>(DayOfWeek::Monday));

    enum class Color { Red, Green, Blue };

    // ASSERT_TRUE(Green == Monday);  // 別のenumが比較できないため、コンパイルエラー
    ASSERT_TRUE(static_cast<DayOfWeek>(Color::Green) == DayOfWeek::Monday);
```

```cpp
    //  example/term_explanation/enum_ut.cpp 41

    // DayOfWeek d0 {0}; intからの暗黙の型変換は許可されないため、コンパイルエラー
    DayOfWeek d0{static_cast<DayOfWeek>(0)};
    DayOfWeek d1{};  // デフォルト初期化
    ASSERT_EQ(d1, DayOfWeek::Sunday);

    DayOfWeek d2{DayOfWeek::Tuesday};  // 値あり初期化
```

### スコープドenum <a id="SS_19_2_2"></a>
[enum class](term_explanation.md#SS_19_2_1)はスコープドenum(scoped enum)と呼ばれることがある。


### underlying type <a id="SS_19_2_3"></a>
underlying typeとは、enumやenum classの[汎整数型](term_explanation.md#SS_19_1_4)を指定できるようにするために、
C++11で導入されたシンタックスである。enumのサイズをユーザが定義できるため、
特定のバイナリプロトコルとの互換性が必要な場合や、特定のハードウェアと連携する際に特に有効である。

```cpp
    //  example/term_explanation/enum_ut.cpp 54

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
C++17から導入された[std::byte](term_explanation.md#SS_19_2_4)の利便性のため、
underlying typeを指定したenumやenum class変数のunderlying typeインスタンスによる初期化が認められるようになった。

```cpp
    //  example/term_explanation/enum_ut.cpp 80

    enum class Color : int { Red, Green, Blue };

    // Color red{0}; C++14まではコンパイルエラー

    Color red{0};  // underlying typeの効果でC++17からコンパイルできる。

    long a{1};
    // Color green{a};  // 縮小型変換が発生するため、コンパイルエラー

```

上記コードにもあるが、underlying typeインスタンスによる初期化を行う場合は、
意図しない縮小型変換によるバグの発生を防ぐためにも、
[一様初期化](term_explanation.md#SS_19_5_2)を使用するべきだろう。

一部の例外を除くとunderlying typeを指定しないenumやenum classはコンパイル時にサイズが確定できないため、
前方宣言できないが、underlying typeを指定したenum、enum classは前方宣言することができる。

```cpp
    //  example/term_explanation/enum_ut.cpp 97

    // in calender.h
    enum class DayOfWeek : int8_t;  // DayOfWeekの前方宣言

    bool calender(DayOfWeek);  // 前方宣言の効果でこのヘッダでの#include "day_of_week.h"が不要

    // in day_of_week.h
    enum class DayOfWeek : int8_t { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
```

### std::byte <a id="SS_19_2_4"></a>
C++17で導入されたstd::byte型は、バイト単位のデータ操作に使用され、
[整数型](term_explanation.md#SS_19_1_5)としての意味を持たないため、型安全性を確保する。
uint8_t型と似ているが、uint8_t型の演算による[汎整数型昇格](term_explanation.md#SS_19_1_7)を発生させないため、
可読性、保守性の向上が見込める。

```cpp
    //  example/term_explanation/enum_ut.cpp 113

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

### using enum <a id="SS_19_2_5"></a>
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
    //  example/term_explanation/enum_ut.cpp 158

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
    //  example/term_explanation/enum_ut.cpp 194

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
    //  example/term_explanation/enum_ut.cpp 213

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
    //  example/term_explanation/enum_ut.cpp 229

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

## 型とインスタンス <a id="SS_19_3"></a>
### 特殊メンバ関数 <a id="SS_19_3_1"></a>
特殊メンバ関数とは下記の関数を指す。

* デフォルトコンストラクタ
* copyコンストラクタ
* copy代入演算子
* moveコンストラクタ
* move代入演算子
* デストラクタ

以下のメンバ関数は特殊関数ではないが、C++20から特殊関数と同様に`=default`とすることで自動生成される。

* [==演算子](term_explanation.md#SS_19_6_7)  
  クラス内のすべてのメンバが==をサポートしている場合、`= default`とすることで自動生成される。
* [<=>演算子](term_explanation.md#SS_19_6_8_3)  
  すべてのメンバが[<=>演算子](term_explanation.md#SS_19_6_8_3)での比較可能である場合、`= default`とすることで自動生成される。 

ユーザがこれらを一切定義しない場合、または一部のみを定義する場合、
コンパイラは、下記のテーブル等で示すルールに従い、特殊関数メンバの宣言、定義の状態をを定める。

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

|user-defined     |default ctor |dtor       |copy ctor      |copy assign    |move ctor   |move assign |`==`        |`<=>`       |
|:---------------:|:-----------:|:---------:|:-------------:|:-------------:|:----------:|:----------:|:----------:|:----------:|
|undeclared       | = default   | = default | = default     | = default     | = default  | = default  | undeclared | undeclared |
|non-default ctor | undeclared  | = default | = default     | = default     | = default  | = default  | undeclared | undeclared |
|default ctor     | -           | = default | = default     | = default     | = default  | = default  | undeclared | undeclared |
|dtor             | = default   | -         | ~~= default~~ | ~~= default~~ | undeclared | undeclared | undeclared | undeclared |
|copy ctor        | undeclared  | = default | -             | ~~= default~~ | undeclared | undeclared | undeclared | undeclared |
|copy assign      | = default   | = default | ~~= default~~ | -             | undeclared | undeclared | undeclared | undeclared |
|move ctor        | undeclared  | = default | = delete      | = delete      | -          | undeclared | undeclared | undeclared |
|move assign      | = default   | = default | = delete      | = delete      | undeclared | -          | undeclared | undeclared |
|`==`             | -           | -         | -             | -             | -          | -          | -          | undeclared |
|`<=>`            | -           | -         | -             | -             | -          | -          | undeclared | -          |

**テーブル注**  

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

* [ゼロの原則(Rule of Zero)](term_explanation.md#SS_19_3_1_1)
* [五の原則(Rule of Five)](term_explanation.md#SS_19_3_1_2)

この2つの原則(ガイドライン)の使い分けに関しては、

* リソース管理を外部([RAII(scoped guard)](design_pattern.md#SS_9_9)クラス)に任せられる場合: ゼロの法則を採用し、特殊メンバ関数を明示的に定義しない。
* リソースをクラス内で直接管理する場合: 五の法則を採用し、すべての特殊メンバ関数を適切に定義する。

とすることで安全で保守性性の高いコードを設計できる。

#### ゼロの原則(Rule of Zero) <a id="SS_19_3_1_1"></a>
「ゼロの原則」は、リソース管理を直接クラスで行わず、
リソース管理を専門とするクラス
(例: 標準ライブラリの[RAII(scoped guard)](design_pattern.md#SS_9_9)クラス)に任せる設計ガイドラインを指す。
この法則に従うと、自身で特殊メンバ関数を定義する必要がななくなる。

```cpp
    //  example/term_explanation/rule_of_zero_ut.cpp 9

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
    //  example/term_explanation/rule_of_zero_ut.cpp 26

    auto z = RuleZero(std::list<std::string>{"1", "2", "3"}, "str");

    auto coied = z;             // コピーは自動生成に任せる(ゼロの原則)
    auto moved = std::move(z);  // ムーブも自動生成に任せる(ゼロの原則)

    ASSERT_EQ(coied.GetStr(), moved.GetStr());
    ASSERT_EQ(coied.GetStrs(), moved.GetStrs());
```

クラスがリソースを直接管理する場合、メモリリークや二重解放などのリスクを伴う。
上記のように信頼性の高いクラスに特殊メンバ関数の処理を任せることにより、
クラス自体にリソース管理の責任を持たせる必要がなくなる。

#### 五の原則(Rule of Five) <a id="SS_19_3_1_2"></a>
「五の原則」は、
クラスがリソース(例: 動的メモリやファイルハンドルなど)を管理する場合、
デフォルトコンストラクタを除く[特殊メンバ関数](term_explanation.md#SS_19_3_1)、
つまり以下の5つの関数をすべて適切に定義する必要があるという設計ガイドラインを指す。

* デストラクタ
* コピーコンストラクタ
* コピー代入演算子
* ムーブコンストラクタ
* ムーブ代入演算子

特殊メンバ関数の挙動を正しく定義しないと、
リソースの不適切な管理(例: メモリリーク、リソースの二重解放)を招く可能性がある。
自動生成されるメンバ関数では、
複雑なリソース管理の要件を満たせないことがある(「[シャローコピー](term_explanation.md#SS_19_5_9_1)」参照)。

なお、「五の原則」は、「六の原則」と呼ばれることもある。
その場合、この原則が対象とする関数は、
[特殊メンバ関数](term_explanation.md#SS_19_3_1)のすべてとなる。

このガイドラインに従って、コピーやムーブを実装する場合、

* [等価性のセマンティクス](term_explanation.md#SS_19_17_1)
* [copyセマンティクス](term_explanation.md#SS_19_17_2)
* [moveセマンティクス](term_explanation.md#SS_19_17_3)

に従わなけならない。


### トリビアル型 <a id="SS_19_3_2"></a>
トリビアル型とは、

* 全ての[特殊メンバ関数](term_explanation.md#SS_19_3_1)がデフォルトである。
* バーチャル関数や仮想継承を持たない。
* 基底クラスがある場合、基底クラスもトリビアルである。

である。その結果、トリビアル型とは、[トリビアルに破壊可能な型](term_explanation.md#SS_19_3_3)となる。

「型Tがトリビアルであること」と「以下の行がコンパイルできること」は等価である。

```cpp
    static_assert(std::is_trivial_v<T>);
```

下記のコードはその使用例である。

```cpp
    //  example/term_explanation/trivial_ut.cpp 63

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

### トリビアルに破壊可能な型 <a id="SS_19_3_3"></a>
「トリビアルに破壊可能な型(Trivially Destructible)」とは、以下の条件を満たす型を指す。

* デストラクタがユーザー定義されていない
  (つまりコンパイラが生成したデフォルトのデストラクタを使用している)。
* 型に含まれるすべてのメンバ変数や基底クラスも「トリビアルに破壊可能」である。

```cpp
    //  example/term_explanation/trivial_ut.cpp 84

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

### 標準レイアウト型 <a id="SS_19_3_4"></a>
「型Tが標準レイアウトであること」と「以下の行がコンパイルできること」は等価である。

```cpp
    static_assert(std::is_standard_layout_v<T>);
```

下記のコードはその使用例である。

```cpp
    //  example/term_explanation/trivial_ut.cpp 42

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

### 集成体 <a id="SS_19_3_5"></a>
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

### POD <a id="SS_19_3_6"></a>
PODとは、 Plain Old Dataの略語であり、
「型TがPODであること」と「以下の行がコンパイルできること」は等価である。

```cpp
    static_assert(std::is_pod_v<T>);  // is_podはC++20から非推奨
```

「型が[トリビアル型](term_explanation.md#SS_19_3_2)且つ[標準レイアウト型](term_explanation.md#SS_19_3_4)であること」と
「型が[POD](term_explanation.md#SS_19_3_6)であること」は等価であるため、C++20では、
[PODという用語は非推奨](https://cpprefjp.github.io/lang/cpp20/deprecate_pod.html)となった。
従って、std::is_pod_vは以下のように置き換えられるべきである。

```cpp
    //  example/term_explanation/trivial_ut.cpp 9

    template <typename T>  // std::is_povはC++20から非推奨
    constexpr bool is_pod_v = std::is_trivial_v<T>&& std::is_standard_layout_v<T>;
```

下記のコードは置き換えられたstd::is_pod_vの使用例である。

```cpp
    //  example/term_explanation/trivial_ut.cpp 18

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


### 不完全型 <a id="SS_19_3_7"></a>
不完全型とは、型のサイズや構造が不明な型を指す。
以下のis_completeで示したテンプレート定数で、不完全型か否かを判定できる。

```cpp
    //  example/term_explanation/incomplete_type_ut.cpp 4

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
    //  example/term_explanation/incomplete_type_ut.cpp 21

    class A;  // Aの前方宣言
              // これ以降、Aは不完全型となる

    // auto a = sizeof(A);  Aが不完全型であるため、コンパイルエラー
    static_assert(!is_complete_v<A>);
```
```cpp
    //  example/term_explanation/incomplete_type_ut.cpp 31

    class A {  // この宣言により、この行以降はAは完全型になる
    public:
        // 何らかの宣言
    };

    auto a = sizeof(A);  // Aが完全型であるため、コンパイル可能
    static_assert(is_complete_v<A>);
```

### 完全型 <a id="SS_19_3_8"></a>
[不完全型](term_explanation.md#SS_19_3_7)ではない型を指す。

### ポリモーフィックなクラス <a id="SS_19_3_9"></a>
ポリモーフィックなクラスとは仮想関数を持つクラスや、
ポリモーフィックなクラスから派生したクラスを指す。
なお、純粋仮想関数を持つクラスは、
仮想クラスと呼ばれれる(「[インターフェースクラス](term_explanation.md#SS_19_3_13)」参照)。
ポリモーフィックなクラスと、
非ポリモーフィックなクラスは[RTTI](term_explanation.md#SS_19_3_11)との組み合わせで動作の違いが顕著となる。

非ポリモーフィックなクラスは非静的なメンバ変数が定義された順にメモリ上に配置されたレイアウトを持つ
(CPUアーキテクチャに依存したパディング領域が変数間に挿入されることもある)。
このようなクラスは[POD](term_explanation.md#SS_19_3_6)
(C++20では、[PODという用語は非推奨](https://cpprefjp.github.io/lang/cpp20/deprecate_pod.html)
となり、[トリビアル型](term_explanation.md#SS_19_3_2)と[標準レイアウト型](term_explanation.md#SS_19_3_4)に用語が分割された)とも呼ばれ、
C言語の構造体のレイアウトと互換性を持つことが一般的である。

ポリモーフィックなクラスは、
仮想関数呼び出しを行う(「[オーバーライドとオーバーロードの違い](term_explanation.md#SS_19_3_10)」参照)
ためのメモリレイアウトが必要になる。
それを示すために、まずは下記のようにクラスX、Y、Zを定義する。

```cpp
    //  example/term_explanation/class_layout_ut.cpp 4

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

<!-- pu:deep/plant_uml/class_layout.pu--><p><img src="data:image/png;base64,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" /></p>

各クラスがvtblへのポインタを保持するため、このドキュメントで使用している[g++](term_explanation.md#SS_19_19_1)では、
sizeof(X)は8ではなく16、sizeof(Y)は16ではなく24、sizeof(Z)は24ではなく32となる。

g++の場合、以下のオプションを使用し、クラスのメモリレイアウトをファイルに出力することができる。

```cpp
    //  example/term_explanation/Makefile 28

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
    //  example/term_explanation/class_layout_ut.cpp 40

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

### オーバーライドとオーバーロードの違い <a id="SS_19_3_10"></a>
下記例では、Base::g()がオーバーロードで、Derived::f()がオーバーライドである
(Derived::g()はオーバーロードでもオーバーライドでもない(「[name-hiding](term_explanation.md#SS_19_10_9)」参照))。


```cpp
    //  example/term_explanation/override_overload_ut.cpp 5

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

<!-- pu:deep/plant_uml/vtbl.pu--><p><img src="data:image/png;base64,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" /></p>

vtblとは仮想関数テーブルとも呼ばれる、仮想関数ポインタを保持するための上記のようなテーブルである
(「[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)」参照)。

Base::f()、Derived::f()の呼び出し選択は、オブジェクトの表層の型ではなく、実際の型により決定される。
Base::g()、Derived::g()の呼び出し選択は、オブジェクトの表層の型により決定される。

```cpp
    //  example/term_explanation/override_overload_ut.cpp 29

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

### RTTI <a id="SS_19_3_11"></a>
RTTI(Run-time Type Information)とは、プログラム実行中のオブジェクトの型を導出するための機能であり、
具体的には下記の3つの要素を指す。

* [dynamic_cast](term_explanation.md#SS_19_3_11_1)
* [typeid](term_explanation.md#SS_19_3_11_2)
* [std::type_info](term_explanation.md#SS_19_3_11_3)


#### dynamic_cast <a id="SS_19_3_11_1"></a>
dynamic_castは、実行時の型チェックと安全なダウンキャストを行うためのキャスト演算子であるため、
[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)とは密接な関係を持つ。


下記のような[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)に対しては、

```cpp
    //  example/term_explanation/rtti_ut.cpp 8

    class Polymorphic_Base {  // ポリモーフィックな基底クラス
    public:
        virtual ~Polymorphic_Base() = default;
    };

    class Polymorphic_Derived : public Polymorphic_Base {  // ポリモーフィックな派生クラス
    };
```

dynamic_castは下記のように振舞う。

```cpp
    //  example/term_explanation/rtti_ut.cpp 25

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


一方で、下記のような非[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)に対しては、

```cpp
    //  example/term_explanation/rtti_ut.cpp 102

    class NonPolymorphic_Base {  // 非ポリモーフィックな基底クラス
    };

    class NonPolymorphic_Derived : public NonPolymorphic_Base {  // 非ポリモーフィックな派生クラス
    };
```

dynamic_castは下記のように振舞う。

```cpp
    //  example/term_explanation/rtti_ut.cpp 115

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

#### typeid <a id="SS_19_3_11_2"></a>
typeidは[RTTI](term_explanation.md#SS_19_3_11)オブジェクトの型情報
([std::type_info](term_explanation.md#SS_19_3_11_3))を実行時に取得するための演算子である。
dynamic_castとは違い、
typeidのオペランドは[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)のインスタンスでなくても良い。
以下の例では[基本型](term_explanation.md#SS_19_1_1)に対するtypeidが返す[std::type_info](term_explanation.md#SS_19_3_11_3)の振る舞いを表す。

```cpp
    //  example/term_explanation/rtti_ut.cpp 52

    int   i{};
    long  j{};
    auto& i_ref = i;

    auto const& type_info_i     = typeid(i);
    auto const& type_info_i_ref = typeid(i_ref);

    ASSERT_NE(typeid(i), typeid(j));
    ASSERT_EQ(type_info_i, type_info_i_ref);
    ASSERT_STREQ(type_info_i.name(), "i");  // 実装定義の型名(clang++/g++ではintはi)
```

下記のような[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)のインスタンスに関して、

```cpp
    //  example/term_explanation/rtti_ut.cpp 8

class Polymorphic_Base {  // ポリモーフィックな基底クラス
public:
    virtual ~Polymorphic_Base() = default;
};

class Polymorphic_Derived : public Polymorphic_Base {  // ポリモーフィックな派生クラス
};
```

typeidが返す[std::type_info](term_explanation.md#SS_19_3_11_3)オブジェクトは下記のように振舞う。

```cpp
    //  example/term_explanation/rtti_ut.cpp 65

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

一方で、下記のような非[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)に対しては、

```cpp
    //  example/term_explanation/rtti_ut.cpp 102

    class NonPolymorphic_Base {  // 非ポリモーフィックな基底クラス
    };

    class NonPolymorphic_Derived : public NonPolymorphic_Base {  // 非ポリモーフィックな派生クラス
    };
```

typeidが返す[std::type_info](term_explanation.md#SS_19_3_11_3)オブジェクトは下記のように振舞う。

```cpp
    //  example/term_explanation/rtti_ut.cpp 139

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

[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)のオブジェクトをオペランドとするtypeidの実行は、
そのオペランドの実際のオブジェクトの型を取得することはすでに示した。
このような場合、オペランド式は実行時に評価される。以下のコードはそのことを表している。

```cpp
    //  example/term_explanation/rtti_ut.cpp 87

    Polymorphic_Base    base;
    Polymorphic_Derived derived;
    Polymorphic_Base*   base_ptr = &derived;

    ASSERT_EQ(typeid(Polymorphic_Derived), typeid(*base_ptr));
    ASSERT_EQ(typeid(Polymorphic_Base), typeid(*(base_ptr = &base)));  // 注意

    // ポリモーフィックなクラスは対しては、typeid内の式が実行される
    ASSERT_EQ(base_ptr, &base);  // base_ptr = &baseが実行される
```


一方、非[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)のオブジェクトをオペランドとするtypeidのオペランド式は、
コンパイル時に処理されるため、その式は実行されない。以下のコードはそのことを表している。

```cpp
    //  example/term_explanation/rtti_ut.cpp 161

    NonPolymorphic_Base    base;
    NonPolymorphic_Derived derived;
    NonPolymorphic_Base*   base_ptr = &derived;

    ASSERT_NE(typeid(NonPolymorphic_Derived), typeid(*base_ptr));
    ASSERT_EQ(typeid(NonPolymorphic_Base), typeid(*(base_ptr = &base)));  // 注意

    // 非ポリモーフィックなクラスに対しては、typeid内の式は実行されない
    ASSERT_EQ(base_ptr, &derived);  // base_ptr = &baseは実行されない
```

#### std::type_info <a id="SS_19_3_11_3"></a>
type_infoクラスは、[typeid](----)演算子によって返される、型の情報が格納された型である。

std::type_infoはコンパイラの実装で定義された型名を含んでいる。
以下のコードで示したように`std::type_info::name()`によりその型名を取り出すことができる。

```cpp
    //  example/term_explanation/rtti_ut.cpp 179

    auto s = std::string{"str"};
    auto v = std::string_view{"str"};
    auto b = std::byte{0b1001};

    ASSERT_STREQ(typeid(s).name(), "Ss");       // 実装定義の型名
    ASSERT_STREQ(typeid(b).name(), "St4byte");  // 実装定義の型名
    ASSERT_STREQ(typeid(v).name(), "St17basic_string_viewIcSt11char_traitsIcEE");
```

`std::type_info::name()`が返すCスタイルの文字列リテラルを、
「人間が認知できる元の型名に戻す関数」を通常のコンパイラは独自に提供する。
このドキュメントのコードのコンパイルに使用している[g++](term_explanation.md#SS_19_19_1)/[clang++](term_explanation.md#SS_19_19_2)では、
そのような関数は、`abi::__cxa_demangle`である。

`std::type_info::name()`と`abi::__cxa_demangle`を利用して、
オブジェクトの[被修飾型](term_explanation.md#SS_19_18_10)名をstd::stringオブジェクトとして取り出す関数とその使用例を以下に示す。

```cpp
    //  example/term_explanation/rtti_ut.cpp 191

    #include <cxxabi.h>  // g++/clang++実装依存ヘッダ abi::__cxa_demangleの宣言

    #include <memory>
    #include <string>

    template <typename T>
    std::string type2str(T&& obj)
    {
        int status;

        // objに基づく型情報を取得
        auto demangled = std::unique_ptr<char, decltype(&std::free)>{
            abi::__cxa_demangle(typeid(obj).name(), 0, 0, &status), &std::free};

        return demangled ? demangled.get() : "unknown";
    }
```
```cpp
    //  example/term_explanation/rtti_ut.cpp 213

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
    ASSERT_EQ(type2str(b_ref_b), "Polymorphic_Base");  // b_ref_bの実際の型はPolymorphic_Base
```

### Run-time Type Information <a id="SS_19_3_12"></a>
「[RTTI](term_explanation.md#SS_19_3_11)」を参照せよ。


### インターフェースクラス <a id="SS_19_3_13"></a>
インターフェースクラスとは、純粋仮想関数のみを持つ抽象クラスのことを指す。
インターフェースクラスは、クラスの実装を提供することなく、
クラスのインターフェースを定義するために使用される。
インターフェースクラスは、クラスの仕様を定義するために使用されるため、
多くの場合、抽象基底クラスとして使用される。

```cpp
    //  example/term_explanation/interface_class.cpp 8

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

### constインスタンス <a id="SS_19_3_14"></a>
constインスタンスは、ランタイムまたはコンパイル時に初期化され、
その後、状態が不変であるインスタンスである。
必ずしも以下に示すようにconstインスタンスがコンパイル時に値が定まっているわけではない。
[constexprインスタンス](term_explanation.md#SS_19_4_5)はconstインスタンスである。
C++03までのコンパイラに、
最適化の一環で`static const`インスタンスを[constexprインスタンス](term_explanation.md#SS_19_4_5)と扱うものもあった。


```cpp
    //  example/term_explanation/const_xxx_ut.cpp 13

    using namespace std;
    auto const str = string{"str"};  // strはプログラムがこの行を通過するときに初期化

    char const* c_str = str.c_str();

    static_assert(!is_const_v<decltype(c_str)>);
    c_str = nullptr;  // c_strは変数としてconstではない
    static_assert(is_const_v<remove_reference_t<decltype(*c_str)>>);  // *cは_strはconst
    static_assert(is_same_v<char const&, decltype(*c_str)>);  // *c_strはconstリファレンス

    char const* const cc_str = c_str;

    static_assert(is_const_v<decltype(cc_str)>);
    // cc_str = nullptr;  // cc_strは変数としてconstであるためコンパイルエラー
    static_assert(is_const_v<remove_reference_t<decltype(*cc_str)>>);  // *cc_strはconst
    static_assert(is_same_v<char const&, decltype(*cc_str)>);  // *cc_strはconstリファレンス

    constexpr int c_int = 1;
    static_assert(is_const_v<decltype(c_int)>);  // c_intはcons
```

## constexpr <a id="SS_19_4"></a>
constexprはC++11で導入されたキーワードで、
関数や変数をコンパイル時に評価可能にする。
これにより、定数計算がコンパイル時に行われ、
実行時のパフォーマンスが向上し、コンパイル時にエラーを検出できることがある。

### constexpr定数 <a id="SS_19_4_1"></a>
C++11以前で定数を定義する方法は、

* マクロ定数
* [enum](term_explanation.md#SS_19_2)
* static const(定数となるか否かは、コンパイラの実装依存に依存する)

の方法があったが、それぞれの方法には下記のような問題がある。

* マクロにはスコープが無く、`#undef`できてしまう。
* enumには整数の定義に限られる。
* static constに関しては、コンパイラの実装依存に依存する。

こういった問題を解決できるのがconstexpr定数である。constexpr定数とは下記のような定数を指す。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 40

    template <int N>
    struct Templ {
        static constexpr auto value = N;  // valueは定数
    };
```
```cpp
    //  example/term_explanation/const_xxx_ut.cpp 49

    constexpr int a = 5;  // aは定数であるためかきのような使い方ができる
    static_assert(a == 5);

    constexpr int b = 5;  // bは定数でないため、下記のような使い方ができない
    // static_assert(b == 5);  // コンパイルエラー

    constexpr double PI{3.14159265358979323846};  // PIはconstexpr

    auto templ = Templ<a>{};  // aはconstexprなのでaの初期化が可能

    static_assert(templ.value == 5);
```

constexpr定数がif文のオカレンスになる場合、[constexpr if文](term_explanation.md#SS_19_11_9)することで、
[ill-formed](term_explanation.md#SS_19_18_5)を使用した場合分けが可能になる。


### constexpr関数 <a id="SS_19_4_2"></a>
関数に`constexpr`をつけて宣言することで定数を定義することができる。
constexpr関数の呼び出し式の値がコンパイル時に確定する場合、
その値はconstexpr定数となるため、関数呼び出しが発生しないため、実行効率が向上する。
一方で、constexpr関数の呼び出し式の値が、コンパイル時に確定しない場合、
通常の関数呼び出しと同じになる。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 68

    constexpr int f(int a) noexcept { return a * 3; }  // aがconstexprならばf(a)もconstexpr
    int g(int a) noexcept { return a * 3; }            // aがconstexprであってもg(a)は非constexpr
```
```cpp
    //  example/term_explanation/const_xxx_ut.cpp 78

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
    //  example/term_explanation/const_xxx_ut.cpp 148

    constexpr uint64_t bit_mask(uint32_t max)
    {
        return max == 0 ? 0 : (1ULL << (max - 1)) | bit_mask(max - 1);
    }
    constexpr uint64_t bit_mask_0 = bit_mask(4);  // C++11ではコンパイルエラー
    static_assert(0b1111 == bit_mask_0);
```
このため、可読性、保守性があったため、C++14で制約が緩和され、
さらにC++17では for/if文などの一般的な制御構文も使えるようになった。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 157

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

### コア定数式 <a id="SS_19_4_3"></a>
コア定数式(core constant expression)とは以下の条件を満たす式である。

1. 以下のいずれかに該当する式であること  
   - リテラル
   - constexpr変数への参照
   - 定数式で初期化された参照
   - constexprサブオブジェクトへの参照
   - constexpr関数呼び出し
   - sizeof演算子の適用結果
   - typeid演算子の適用結果(式の値が[ポリモーフィックなクラス](term_explanation.md#SS_19_3_9)である場合を除く)

2. 以下のすべてを満たすこと:  
   - 浮動小数点の比較演算を含まない
   - インクリメント/デクリメント演算を含まない
   - 代入演算を含まない
   - 動的メモリ割り当てを含まない
   - 仮想関数の呼び出しを含まない
   - 未定義動作を引き起こさない
   - 例外を投げない
   - アドレス取得演算子の使用が定数式の評価に限定される

3. その式の評価において:  
   - すべてのサブ式も定数式である
   - 使用されるすべての変数は定数式で初期化されている
   - 呼び出されるすべての関数はconstexpr関数である

このドキュメントでは慣用的に[constexpr定数](term_explanation.md#SS_19_4_1)と呼んでいる概念が、コア定数式である。

### リテラル型 <a id="SS_19_4_4"></a>
constexpr導入後のC++11の標準では、下記の条件を満たすクラスは、

* constexprコンストラクタを持つ
* すべてのメンバ変数がリテラル型である
* 仮想関数や仮想基底クラスを持たない

constexpr定数もしくはconstexprインスタンスをコンストラクタに渡すことにより、
[constexprインスタンス](term_explanation.md#SS_19_4_5)を生成できる。

このようなクラスは慣習的にリテラル型(literal type)と呼ばれる。

以下にリテラル型を例示する。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 94

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
    //  example/term_explanation/const_xxx_ut.cpp 112

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

### constexprインスタンス <a id="SS_19_4_5"></a>
[constexpr定数](term_explanation.md#SS_19_4_1)を引数にして、[リテラル型](term_explanation.md#SS_19_4_4)のconstexprコンストラクタを呼び出せば、
constexprインスタンスを生成できる。このリテラル型を使用して下記のように[ユーザー定義リテラル](term_explanation.md#SS_19_6_6)
を定義することで、constexprインスタンスをより簡易に使用することができるようになる。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 130

    constexpr Integer operator"" _i(unsigned long long int value)  // ユーザ定義リテラルの定義
    {
        return Integer(static_cast<int32_t>(value));
    }
```
```cpp
    //  example/term_explanation/const_xxx_ut.cpp 140

    constexpr auto i = 123_i;
    static_assert(i == 123);
    static_assert(std::is_same_v<decltype(i), Integer const>);
```

### consteval <a id="SS_19_4_6"></a>
constevalはC++20 から導入されたキーワードであり、
常にコンパイル時に評価されることを保証する関数を定義するために使用される。
このキーワードを使用すると、引数や関数内の処理がコンパイル時に確定できなければ、
コンパイルエラーが発生する。constexprと異なり、ランタイム評価が許されないため、
パフォーマンスの最適化やコンパイル時のエラー検出に特化した関数を作成する際に便利である。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 187

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
    //  example/term_explanation/const_xxx_ut.cpp 209

    static_assert(0b1111'1111 == bit_mask(8));

    // auto i = 8UL;         // bit_maskがconstevalであるため、コンパイルエラー
    constexpr auto i = 8UL;  // iがconstexpであるためbit_maskががコンパイル時評価されるため、
    auto bm = bit_mask(i);   // bit_mask(i)の呼び出しは効率的になる
                             // bmをconsexprにするとさらに効率的になる

    ASSERT_EQ(0b1111'1111, bm);
```

### constexprラムダ <a id="SS_19_4_7"></a>
constexprラムダはC++17から導入された機能であり、以下の条件を満たした[ラムダ式](term_explanation.md#SS_19_8_3)である。

* 引数やラムダ式内の処理がコンパイル時に評価可能である必要がある。
  すべての処理はconstexpr関数のようにコンパイル時に確定する必要があり、
  動的な処理やランタイムでしか決定できないものは含めることができない。

* ラムダ内で使用される関数や式もconstexprでなければならない。
  たとえば、関数の呼び出しや算術演算は、コンパイル時に評価可能なものであることが求められる。

* ラムダキャプチャはconstexprに適合している必要がある。
  キャプチャする変数もコンパイル時に確定できるものに限られる。
  動的な変数をキャプチャすると、コンパイルエラーとなる。

* 例外処理 (try/catch/throw) が禁止されている。
  constexprラムダでは、例外処理を含むことはできない。

* 動的メモリの割り当て(new/delete) が禁止されている。
  これらの操作はコンパイル時には行えないため、constexprラムダでは使用できない。

```cpp
    //  example/term_explanation/const_xxx_ut.cpp 226

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
    //  example/term_explanation/const_xxx_ut.cpp 243

    constexpr auto factorial = [](auto self, int n) -> int {  // リカーシブconstexprラムダ
        return (n <= 1) ? 1 : n * self(self, n - 1);
    };

    constexpr int fact_5 = factorial(factorial, 5);  // コンパイル時の評価
    static_assert(fact_5 == 120);
```

## オブジェクトと生成 <a id="SS_19_5"></a>
### リスト初期化 <a id="SS_19_5_1"></a>
リスト初期化とは、C++11で導入された`{}`を使ったオブジェクトの初期化構文を指す。
以下にコード例を示す。

```cpp
    //  example/term_explanation/uniform_initialization_ut.cpp 12

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
    //  example/term_explanation/uniform_initialization_ut.cpp 34

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

### 一様初期化 <a id="SS_19_5_2"></a>
一様初期化(Uniform Initialization)は 、
[リスト初期化](term_explanation.md#SS_19_5_1)による初期化方法がC++における初期化を統一的に扱えるように設計された概念を指さす。

### 初期化子リストコンストラクタ <a id="SS_19_5_3"></a>
初期化子リストコンストラクタ([リスト初期化](term_explanation.md#SS_19_5_1)用のコンストラクタ)とは、
{}による[リスト初期化](term_explanation.md#SS_19_5_1)をサポートするためのコンストラクタである。
下記コードでは、 E::E(std::initializer_list\<uint32_t>)が初期化子リストコンストラクタである。

```cpp
    //  example/term_explanation/constructor_ut.cpp 6

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

### 継承コンストラクタ <a id="SS_19_5_4"></a>
継承コンストラクタとは、基底クラスで定義したコンストラクタ群を、
派生クラスのインターフェースとしても使用できるようにするための機能である。
下記コードのように、継承コンストラクタは派生クラス内でusingを用いて宣言される。

```cpp
    //  example/term_explanation/constructor_ut.cpp 40

    class Base {
    public:
        explicit Base(int32_t b) noexcept : b_{b} {}
        virtual ~Base() = default;
        ...
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
        ...
    }
```

### 委譲コンストラクタ <a id="SS_19_5_5"></a>
委譲コンストラクタとは、コンストラクタから同じクラスの他のコンストラクタに処理を委譲する機能である。
以下のコード中では、委譲コンストラクタを使い、
A::A(uint32_t)の処理をA::A(std::string const&)へ委譲している。

```cpp
    //  example/term_explanation/constructor_ut.cpp 72

    class A {
    public:
        explicit A(std::string str) : str_{std::move(str)}
        {
            ...
        }

        explicit A(uint32_t num) : A{std::to_string(num)}  // 委譲コンストラクタ
        {
        }

    private:
        std::string str_;
    };
```

### 非静的なメンバ変数の初期化 <a id="SS_19_5_6"></a>
非静的なメンバ変数の初期化には下記の3つの方法がある。

* [NSDMI](term_explanation.md#SS_19_5_6_1)
* [初期化子リストでの初期化](term_explanation.md#SS_19_5_6_2)
* [コンストラクタ内での非静的なメンバ変数の初期値の代入](term_explanation.md#SS_19_5_6_3)

同一変数に対して、
「[NSDMI](term_explanation.md#SS_19_5_6_1)」と「[初期化子リストでの初期化](term_explanation.md#SS_19_5_6_2)」
が行われた場合、その変数に対するNSDMIは行われない。

#### NSDMI <a id="SS_19_5_6_1"></a>
NSDMIとは、non-static data member initializerの略語であり、
下記のような非静的なメンバ変数の初期化子を指す。

```cpp
    //  example/term_explanation/nsdmi.cpp 9

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

#### 初期化子リストでの初期化 <a id="SS_19_5_6_2"></a>
「非静的メンバ変数をコンストラクタの本体よりも前に初期化する」言語機能である。
メンバ変数は宣言された順序で初期化されるため、
初期化子リストでの順序は、実際の初期化の順序とは関係がない。

この機能を使うことで、メンバ変数の初期化処理が簡素に記述できる。
constメンバ変数は、初期化子リストでの初期化か[NSDMI](term_explanation.md#SS_19_5_6_1)でしか初期化できない。

```cpp
    //  example/term_explanation/nsdmi.cpp 25

    class A {
    public:
        A(int a, int b) : a_{a}, v_{a, b, 3}  // 非静的なメンバ初期化子による初期化
        {
        }

    private:
        int              a_;
        std::vector<int> v_;
    };
```

#### コンストラクタ内での非静的なメンバ変数の初期値の代入 <a id="SS_19_5_6_3"></a>
この方法は単なる代入でありメンバ変数の初期化ではない。

[NSDMI](term_explanation.md#SS_19_5_6_1)、
[初期化子リストでの初期化](term_explanation.md#SS_19_5_6_2)で初期化できない変数を未初期化でない状態にするための唯一の方法である。

```cpp
    //  example/term_explanation/nsdmi.cpp 40

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

### オブジェクトの所有権 <a id="SS_19_5_7"></a>
オブジェクトxがオブジェクトaの解放責務を持つ場合、
xはaの所有権を持つ(もしくは、所有する) という。

定義から明らかな通り、ダイナミックに生成されたaをxが所有する場合、
xはa(へのポインタ)をdeleteする責務を持つ。

xがaを所有し、且つxがaを他のオブジェクトと共有しない場合、「xはaを排他所有する」という。

オブジェクト群x0、x1、...、xNがaを所有する場合、
「x0、x1、...、xNはaを共有所有する」という。

x0、x1、...、xNがaを共有所有する場合、x0、x1、...、xN全体で、a(へのポインタ)をdeleteする責務を持つ。

下記で示したような状況では、
ダイナミックに生成されたオブジェクトの所有権の所在をコードから直ちに読み取ることは困難であり、
その解放責務も曖昧となる。

```cpp
    //  example/term_explanation/ambiguous_ownership_ut.cpp 11

    class A {
        // 何らかの宣言
    };

    class X {
    public:
        explicit X(A* a) : a_{a} {}
        A* GetA() { return a_; }

    private:
        A* a_;
    };

    auto* a = new A;
    auto  x = X{a};
    // aがxに排他所有されているのか否かの判断は難しい

    auto x0 = X{new A};
    auto x1 = X{x0.GetA()};
    // x0生成時にnewされたオブジェクトがx0とx1に共有所有されているのか否かの判断は難しい
```

こういった問題に対処するためのプログラミングパターンを以下の
「[オブジェクトの排他所有](term_explanation.md#SS_19_5_7_1)」と「[オブジェクトの共有所有](term_explanation.md#SS_19_5_7_2)」で解説する。

#### オブジェクトの排他所有 <a id="SS_19_5_7_1"></a>
オブジェクトの排他所有や、それを容易に実現するための
[std::unique_ptr](https://cpprefjp.github.io/reference/memory/unique_ptr.html)
の仕様をを説明するために、下記のようにクラスA、Xを定義する。

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 7

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
        void Move(std::unique_ptr<A>&& ptr) noexcept { ptr_ = std::move(ptr); }

        // ptr_から外部への所有権の移動
        std::unique_ptr<A> Release() noexcept { return std::move(ptr_); }

        A const* GetA() const noexcept { return ptr_ ? ptr_.get() : nullptr; }

    private:
        std::unique_ptr<A> ptr_{};
    };
```

下記に示した上記クラスの単体テストにより、
オブジェクトの所有権やその移動、
std::unique_ptr、std::move()、[rvalue](term_explanation.md#SS_19_14_3)の関係を解説する。

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 48

    // ステップ0
    // まだ、クラスAオブジェクトは生成されていないため、
    // A::LastConstructedNum()、A::LastDestructedNum()は初期値である-1である。
    ASSERT_EQ(-1, A::LastConstructedNum());     // まだ、A::A()は呼ばれてない
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 57

    // ステップ1
    // a0、a1がそれぞれ初期化される。
    auto a0 = std::make_unique<A>(0);           // a0はA{0}を所有
    auto a1 = std::make_unique<A>(1);           // a1はA{1}を所有

    ASSERT_EQ(1,  A::LastConstructedNum());     // A{1}は生成された
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

<!-- pu:deep/plant_uml/unique_ownership_1.pu--><p><img src="data:image/png;base64,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EEhMTHSV/wTMVY6M63fF9zEEa9asEfHOnTt36dLl7bffRiMoKGjmzJlbtmxp1qxZTEzMuHHjcNQXX3whMrFc7du37xtvvCE/DhYD4ljxOTKQv/mydOlSLLEnTpyYkJDQu3fvFi1aXLp0yevIyrBiZG2NPfDAAzgcjokDkSx7P/zwQ7SHDh2KrtatW+P6xZ1DGdDrlZSWfxsBhw8fPjwuLg5XLodVzo5Hinr16mmDvq5Hm+O1HRsb2759exEE7733Xv369bUf+9QuLto37dtpmCl02BOM46GHHtIGT58+DduFlbjKkXGvuxKsSUUchtupUyesKEeMGAHXGzhwoNvtfv7555s2bYqF+aRJk+QI06ZNQ9pdd90lvicnh0Jm165dsYTPzs6WyaXlX6Tr2LEjHCo6Ojo9Pb20/IvP+pGVYUt1Bnrq1KmHH364UaNGUVFR8fHx4eHhsnfBggUdOnTA4Y888oj87qB+QP2VCHDna9WqFbx71KhR8uMR5eyl5b8nqQ36uh5tjtf2kSNHcOvduHGjiGOQIUOGiHYg4KJ9076dhi2F7mTS0tLknUACz9UH/WDs2LG4heA2fODAgZCQkH379qkZtYft7dsrtO/rqCnOwDlCJ8a5cuVKv3799u/fjzXg1KlT1e5ahfZN+3YczhE6sTe0b9q343CO0Im9oX3Tvh2Hc4RO7A3tm/btOJwjdGJvaN+0b8fhHKETe0P7pn07DucIndgb2jft23E4R+jE3tC+ad+OIzIy0kWI9QkLC5NGFhERoXbbFO2sad9OxO12Z2VlZWZmbt26NTU1dRUh1kT7N9cFTlA1/9K8o+07Ly8vJycHt+6MjAzoYD0h1gTqhYah5JwbOEHV2lmjltXytiO0bw/5+fl45srOzoYCcA/fTYg1gXqhYSj5wg2coGrtrFHLannbEdq3h8LCQty08d7j7o3nr2OEWBOoFxqGkvNu4ARVa2eNWlbL247Qvj0UFRXhXcd9G2+/2+2WKxdCrAXUCw1DyYU3cIKqtbNGLavlbUdo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYklo34QQYkm82DchhBALQfsmhBBLQvsmhBBL8v8Bd8qC/hsMX6MAAAAASUVORK5CYII=" /></p>

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 67

    // ステップ2
    // xが生成され、オブジェクトA{0}の所有がa0からxへ移動する。
    ASSERT_EQ(0, a0->GetNum());                 // a0はA{0}を所有
    auto x = X{std::move(a0)};                  // xの生成と、a0からxへA{0}の所有権の移動
    ASSERT_FALSE(a0);                           // a0は何も所有していない
```

<!-- pu:deep/plant_uml/unique_ownership_2.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeoAAAGkCAIAAABxXfFxAAA6xElEQVR4Xu3dCXRURd428E5YAgRCIKIIKAYUBz4GxIGJg/MqLgOIqPPqwUHgE0QUzgyLYDTfDIIgghFBHHaisiPD8uIoLwFRQSCAIkIggAoBpiEaEBMaAlkgy/eYgupLdXfs9Jaue5/f6eOpW7e6+t7O/z5d3WmDrYyIiDRkUzuIiEgHjG8iIi0547uUiIjCHuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvn1x7NixTp06jR49Wt1BRBQqJonvwsLCNQarV6/euXOn3JuVlfWqi8OHDxsmqMjPP/986NChAwcOZGRk7N+/Pz09HXfv3r1706ZNxYCTJ09u2LBhz549196PiCiITBLfSNj69evHxsY2atSoWbNm9erVa9KkSUlJidiLpH7Yxe7du6+d4xd4GVC7SksnTZpkcxETE5Oamir2VqtWTXR27dr10qVL6v2JiILAJPFtdPny5ZYtW77++uuy55AH586dk2O+/PLLXbt2IfrxSoDNv/zlL5MnTxa7cnNzjx49arfbsYrPzs4+c+bMf/3Xfw0ePBi7Tp8+3bBhQyz28/Pz161bhwTfsmWLnJOIKHhMGN/z5s2Ljo4WKQxYDl+zbDb44IMPxJgjR47UqFFjzZo1t9xyS2JiInqaN2+enJws5zTKy8urU6fO0qVLxWZRUZFo4O6//e1vkfXOoUREQWO2+N67dy+yVUSw9ONVEyZMaNy4sdzEklmOGT58+B133PH+++8//fTTWJVHRER8/PHHhjmcZs6cWbduXePK/eTJk1itP/nkk2fPnjUMJCIKIlPF9+7du5s0aRIfH4/V9/r169XdpaUvvPBCx44d1d5yx48fnzVr1uXLl9F+4403atasmZOTow4qLT1w4EBsbOyrr74qezZu3Ni2bVu3D0dEFDwmie/i4uKUlBSsu7t3737x4kWssmvUqKFE6p49e+Li4rDL2KkoKChAdkdGRo4bN07ZdeHChWnTptWvX79Hjx7y95OZmZl4qUC//NILjuTa+xERBYUZ4js3N/fOO++sXr362LFjxfIZEhMTEay7du0qLU/exx57DKH86KOPItyvubPBiy++2KhRo9q1a0+cONHYj7Du378/grtevXpIf+N3Sz7++GPl83TjBzJERMFjhviGGTNmHDx40NhTUlKCNP/xxx/FJtbmGzduNA5wtXTp0nfeeef06dPqjtLSKVOmYAaHw6HuICKqIiaJbyIiq2F8ExFpifFNRKQlxjcRkZYY30REWmJ8ExFpifFNRKQlxjcRkZYY30REWjJVfMfFxSn/CzuRN1A5ajF5jVVHvvGn6gRTxTeeEXkWRN5D5Tgcjry8vPz8/KKiokr93TFWHfnGn6oTnFPJljpEH7yQyDeoHLvdnp2dnZOTg8tJ/hMc3mDVkW/8qTrBOZVsqUP0wQuJfIPKycjIOHLkSFZWFq6lSv3ZSFYd+cafqhOcU8mWOkQfvJDIN6ictLS09PR0XEtYDWEppNaWZ6w68o0/VSc4p5ItdYg+eCGRb1A5qampuJawGsL72Ur9ZWBWHfnGn6oTnFPJljpEH7yQyDeonOXLl2/YsGHXrl1YCrn9d/I8YdWRb/ypOsE5lWypQ/TBC4l848+FxKoj3/hTdYJzKtlSh+gjTC6kpKSkL7/8Uu0lD4qKik6fPq32hpY/FxKrTke6V53gnEq21CH6CM2FdOrUqQMHDqi9BjiMOXPmqL2BgGkPHjyo9obWr55+ZY0fPx7P2KFDh9QdIeTPhcSqC4FfPf3K0r3qBOdUsqUO0UdoLqTo6OiKr5PgXUjBm9l7v3r6nnzzzTdqV3mxxcfHV69e/eWXX1Z2ff/993l5eUpnkPhzIbHqQuBXT98Ts1ad4JxKttQh+gjShbR58+aFCxeKF+qlS5fiUfr06YNi+umnn+SYixcvrl27dsWKFdnZ2V6Wu7KoMW6inZmZuWfPniVLlqSmpl66dEkOMyosLMTP/oMPPjh27Ni//vWv9PR00V/BzOIuOE4sZ+QAt3Cvw4cPb9q0admyZUePHhWdbk8fbRzA119/PWPGDOf9DbZt23bvvfe2bNlS3VFWhvkx4RNPPNGkSZPi4mLjrmnTpl133XVTpkzJz8839geDPxcSq070VzAzq84tf6pOcE4lW+oQfQTjQho2bJitXERExOTJk5s3by42AaUjxvz444+tWrUSnTExMbarF5LokVO5bhqvN+Mm2m3atBHjoVOnTpcvX1bG4Ifdvn17MSAqKqpu3brGu7udGaXfrl07cRcc586dO+UYVxjTtGlTMbhmzZq4XNHp9vTRHjlyJJ6fnj17XjNFWRnGdOvWDQMeeuih3bt3K3uhX79+ONOtW7fayr9EZdx17ty5cePG1a9f/8Ybb5w5c2ZRUZFxb2DZ/LiQbKw6l6mMm6w6T2x+VJ3gnEq21CH6sAXhQkKBDh069OzZs3Pnzj1z5kyZS5nCM88807BhQxQKho0YMUIOEAUnh7luui130a5Xr95HH32EJQCWQtj85JNPlDFDhgxp0KABlhg///zzc889p9zd7cy4C649rFkyMjKaNWt29913yzGucC8sQ7Zs2eJwODB/bGwsykv0K6ePHtQ6LgZjrWMd9+c//xm77r///u3btxuGO+FSqVOnTnJyMn52LVq06NWrlzqirCw3N/cf//gHfgq4hhcvXqzuDhCbHxeS8WcaKKw6Vp03nFPJljpEH8YyDZQuXbrcdNNNWAXIN1mulYQBSUlJoo23nK4D3PJU7qI9YcIE0cYKCJspKSnKmFtuueWll14yjvnVCwl3efbZZ+eUe/jhhyMjIytYXOBeKHHRPnnyJDZRZ6Lf9UIaPHiwsaes/A0vVkatW7fGm3FllzRv3jzcd8yYMZjwvvvuw2oOl406qKzs/PnzWGdh5B/+8Ad1X4DY/LiQbKy6cp5mZtV5YvOj6gTnVLKlDtGHLQgXEn60w4cPr127dkJCQkFBQZm7SoqOjp46darcdB3glqdyr2CXsb+CB/V0dyw6bNfCakUOUxgnuXDhAjaxIlP65cjZs2cbewRcQrhccTk99thjbn+DdNddd117OLZZs2YZB+ASmjhxItaYWLXhQT19Gus/mx8Xko1V59I2brLqPLH5UXWCcyrZUofowxaEC0msFPbv34/JV65cWeaukjp06PDII4+INt7Mug5wC2X95ptvivb69euN91JmkJvGfuOD7tu3z7jL08x4D7to0SLRX1JSYvwlmCvc64UXXhDt1NRUbIqvFbuenWuP0c6dO/FOFmP69+9v7P/222+VO955550dO3aUmxs3bsQldMMNN0ybNq2wsFD2B4PNjwvJxqor52lmVp0nNj+qTnBOJVvqEH3YAn0hbdu2rVGjRomJiUOHDrVd/SgQC5Bu3bq99tpr4hc7gOoUhTJu3Dj87I11bzwkZRPl1bhxY1Q85secxqpSKsw4oeyXDzp+/HgcpHGXp5kXLFiABd2IESPw/rRz584Yg4XG1QdR2cp/b/b888+/8cYbGPn73/++tLxcXE9fOVq3Nm/e/PTTTxt78B68WrVqxot58uTJmEp+vRcnOGnSJCzB5IDgsflxIRl/pgHBqmPVeck5lWypQ/RhLNOAcDgcqKQGDRrUr19/5MiRonPs2LFYaNx+++3Gr0mhCJo2bYqraODAgRjszYV0/Pjxrl271q1bNz4+HhUTExNTqQuprPxB8f4OD9e7d2/jrgpmRqNVq1a1atXCu/KtW7fKqVxhQlwwmAHz9OjR4+TJk6Lf9fSVo/JGcXExLs4HH3zQ2HnixAlcurj4jZ2h4c+FxKoT/RXMzKpzy5+qE5xTyZY6RB8Bv5A04kM1C3NciLe6Pk+oI38uJFad2usFteZYdZWsOsE5lWypQ/TBC0nt9YLNxQ033CD6fZtQRzY/LiQbq67yrq24X7DqKlV1gnMq2VKH6MNm4Qtp8ODBFb8trayATxjO/LmQWHVqrx8CPmE486fqBOdUsqUO0YeVLyTyhz8XEquOfONP1QnOqWRLHaIPXkjeOHjw4NKlS9euXSu+UExl/l1IrDpv5ObmLlq0qMr/cmFY8afqBOdUsqUO0QcvpIrhKRoyZIjtqvj4eBSNOsiS/LmQWHUVw0KhR48etWrVslnpc21v+FN1gnMq2VKH6IMXklFmZubixYuNfzru3XffxVP05ptvYim0Y8eO5s2b33PPPdfeyaL8uZBYdUauVYdFd9++fSdMmMD4VvhTdYJzKtlSh+iDF5I0derUyMhIscpOSEgQ11Lnzp27dOkix6xatQp7v/vuO+fdrMqfC4lVJ7mtOgHPKuNb4U/VCc6pZEsdog9eSAIum379+g0YMOCnn35avXo1nha8gUV/TEzMuHHj5LDTp09j14cffui8p1X5cyGx6gRPVScwvl35U3WCcyrZUofogxeShGdj/fr1SUlJ4n+Nmzt3LjqjoqLeeecdOaawsBC7Fi5c6LybVflzIbHqpFJ3VScwvl35U3WCcyrZUofogxeSNHz48GrVqj3wwAODBg2Sl018fPyoUaPkmMOHD2PXxo0bnXezKn8uJFad5LbqBMa3K3+qTnBOJVvqEH3wQpLq168/evRoNI4ePSovm4EDBzZt2lT+OZ5XXnmlTp06DofDeEdr8udCYtVJbqtOYHy78qfqBOdUsqUO0QcvJKlNmzZt27Z966230IiIiJg4cSI6MzIyatWq1b59++Tk5CFDhkRGRlbJX+oJQ/5cSKw6yW3VCYxvV/5UneCcSrbUIfrghSR9+eWXrVu3xuJ6wIAB3bp1k/8e4ObNmzt16hQVFdWkSROsvuWf37Q4fy4kVp3kqerKGN/u+FN1gnMq2VKH6IMXEvnGnwuJVUe+8afqBOdUsqUO0QcvJPKNPxcSq45840/VCc6pZEsdog9eSOQbfy4kVh35xp+qE5xTyZY6RB+8kMg3/lxIrDryjT9VJzinki11iD54IZFv/LmQWHXkG3+qTnBOJVvqEH3wQiLf+HMhserIN/5UneCcSrbUIfrghUS+8edCYtWRb/ypOsE5lWypQ/TBC4l848+FxKoj3/hTdYJzKtlSh+iDFxL5xp8LiVVHvvGn6gTnVLKlDtFHXFycjajyoqOjfb6QWHXkG3+qTjBVfIPD4bDb7RkZGWlpaampqcstzFb+2k5eQrWgZlA5qB9UkVpYFWLVSay6SvGn6krNF995eXnZ2dl4KUtPT8fzssHCcCGpXeQZqgU1g8pB/aCK1MKqEKtOYtVVij9VV2q++M7Pz8d7kKysLDwjeE3bZWG4kNQu8gzVgppB5aB+UEVqYVWIVSex6irFn6orNV98FxUV4UUMzwVezfB+5IiF4UJSu8gzVAtqBpWD+kEVqYVVIVadxKqrFH+qrtR88V1cXIxnAa9jeDocDkeOheFCUrvIM1QLagaVg/pBFamFVSFWncSqqxR/qq7UfPFNEi4ktYsoyFh1ocT4Ni1eSBR6rLpQYnybFi8kCj1WXSgxvk2LFxKFHqsulBjfpsULiUKPVRdKjG/T4oVEoceqCyXGt2nxQqLQY9WFEuPbtHghUeix6kKJ8W1avJAo9Fh1ocT4Ni1eSBR6rLpQYnybFi8kCj1WXSgxvk2LFxKFHqsulBjfpsULiUKPVRdKjG/T4oVEoceqCyXGt2nxQqLQY9WFEuPbPNq1a2fzALvU0USBwKqrQoxv80hOTlYvoKuwSx1NFAisuirE+DYPu90eGRmpXkM2GzqxSx1NFAisuirE+DaVLl26qJeRzYZOdRxR4LDqqgrj21RSUlLUy8hmQ6c6jihwWHVVhfFtKrm5uVFRUcarCJvoVMcRBQ6rrqowvs3m8ccfN15I2FRHEAUaq65KML7NZvXq1cYLCZvqCKJAY9VVCca32RQUFDRo0EBcRWhgUx1BFGisuirB+DahQYMGiQsJDXUfUXCw6kKP8W1CmzZtEhcSGuo+ouBg1YUe49uESkpKbiqHhrqPKDhYdaHH+DanpHJqL1EwsepCjPFtTvvKqb1EwcSqCzHGNxGRlhjf5JVLly7JzzSNbSKqKoxv8orNZps9e7ZruwLZ2dkZGRlqLxEFCOObvOJDfEdHR3szjIh8w/i2IqTqkSNHvvnmm8WLF69bt66oqEj2HzhwwDhMblYQ32h///33n3/++dKlSzMzM0XnkiVLMKxPnz7Ye/r0aTHs6NGju3btmj59urwvEfmM8W1FCNY2bdqI/8kCOnXqdOnSJdFvzGVPke06rGnTpmKqmjVrLlu2DJ3NmzeX8yOyxbCRI0dGRET07NlT3peIfMb4tiIkab169f79739fvHgRC3BsbtiwQfT7Ft/XXXfdF198cfbs2eeeey42Nvbnn392O+zGG2/csmVLYWGh7CQinzG+rQhJ+tprr4k21t3YnDdvnuj3Lb7feOMN0T5x4gQ2169f73bY4MGD5SaZUnRstM1c4uLi1JMMG4xvK7K5BKvY9NRfQVvZzMvLwyZW9G6HzZo1S26SKeGnPO/oPDPdcEYOhwOFnZ+fX1RUVFxcrJ5z1WF8W5FrsIrNOnXqyH8dPDU11VNku979hRdeEO1169Zhc+fOnW6HGTfJlEwZ33a7PTs7OycnByEuf88fDhjfVuQpWO+///7GjRsjwRMTE6Ojf3kX7DayXe8eERHx/PPPT5o0CXf//e9/L/6nHszQrVu38ePHu/29KJmSKeM7IyPjyJEjWVlZSHCswdVzrjqMbytyzV+xeezYsa5du9atWzc+Pn7ixIkxMTFuI9v17ohp3AV37NGjx4kTJ0T/2LFjsZy//fbbxbcPGd9WYMr4TktLS09PR4JjDY4FuHrOVYfxTf5iLpNkyvhOTU1FgmMNbrfbHQ6Hes5Vh/FN/mJ8k2TK+F6+fPmGDRt27dqFBXhOTo56zlWH8U3+Gjx48JYtW9ResiTGdygxvokoYAIb37O+mzVl1xTX/rlH5k7PmO7aL+818+BM137fboxvIrKEwMb3Iy88ggnHfTLO2NnrH72q16zeokML2TNtz7Rnpjwjh6EdWS0SAyqIeO9vjG8isoQAxvfczLnX3XQdgrjb892M/XVi6nQbfKXnb+/+rW2XtjWiauBx+07oK8dM2jIJPc9Nf8512sreGN9EZAkBjO9Ry0Zhtju73xl7Q+ycw3NkvzGpsdBOeCzhsVGPKfGtDPPnxvgmIksIYHwn/DnhxltvTPxXIuYcNn+Y7HfN5QmbJrh2uvb4dmN8E5ElBCq+/7nvnzVr13z85cfFRyi/6/E70T/jwAw8BBbdxsFu47tGrRq9/tHLdebK3hjfVAVeffVVtYsoyAIV3/0m9sNUDw99GKF8+123V69Zfdqeaei/56l76sTUmbR1knGw2/hOeCwh9obYN3e86Tp5pW6Mb6oCKDu1iyjIAhXfLTq0sF3rqfFPof/RkY9Wq15tbOpY42C38Y3Qb/abZm9/87br5JW62RjfFHo2xjeFnC0Q8T1+43gljm/+Pzc3/21zNGZ/Pxu7nk5+2jjebXwj5Xu/2tvY49uN8U1VgPFNoReQ+O76XNfIapFTvnb+DztP/L8nMPOrG16d5+53km7j27XHtxvjm6oA45tCz//4nnN4TkyjmNZ3tzZ2JqclR0REINbnuctlxjfj22z4q0sKPf/j+1dv0bHR9z1936xvZ7nuEje8AIxZNwZHMnjmYNe9lb0xvonIEkIQ331f71snpk7ztr98FO721n9y/8hqka3/2HrmoQD85RPGNxFZQgjiW9yM/x+mcpubORc3137fboxvIrKEkMV3yG6MbyKyBMZ3KDG+TYu/uqTQY3yHEuPbtGz84iCFHOM7lBjfpsX4ptBjfIcS49u0GN8UeozvUGJ8mxbjm0KP8R1KjG/T4q8uKfQY36HE+CaigGF8hxLjm4gChvEdSoxvIgoYxncoMb6JKGAY36HE+DYt/uqSQo/xHUqMb9PiFwcp9BjfocT4Ni3GN4Ue4zuUGN+mxfim0GN8hxLj27QY3xR6jO9QYnybFn91SaHH+A4lxjcRBQzjO5QY30QUMIzvUGJ8E1HAxMXF2cwlOjqa8U1EluBwOOx2e0ZGRlpaWmpq6nL94SxwLjgjnBfOTj3hqsP4Ni3+6pKqRF5eXnZ2Nhaq6enpSL0N+sNZ4FxwRjgvnJ16wlWH8W1aNn5xkKpCfn5+Tk5OVlYW8g4r1l36w1ngXHBGOC+cnXrCVYfxbVqMb6oSRUVFWKIi6bBWtdvtR/SHs8C54IxwXjg79YSrDuPbtBjfVCWKi4uRcVilIuwcDkeO/nAWOBecEc4LZ6eecNVhfJsW45vI3BjfpsVfXRKZG+ObiEhLjG8iIi0xvomItMT4JiLSEuPbtPirSyJzY3ybFr84SGRupopvHf/aGY5ZPY0AsTG+iUzNVPGNwJJnoQscc5D+ny7GN5G5OWNEttQh+tA0voP0FxUY30Tm5owR2VKH6EPT+A7S3zPjry6JzM0ZI7KlDtGHpvEdtn9NmIjCmTNGZEsdog9N4zts/y0PIgpnzhiRLXWIPjSN7+Xh+i/pEVE4c8aIbKlD9MH4JiLrcMaIbKlD9MH4NuKvLonMzRkjsqUO0Qfj24hfHCQyN2eMyJY6RB+MbyPGN5G5OWNEttQh+ghqfK9cuXL+/Pml5U/Z+fPn58yZs337dnVQ5TG+icg3zhiRLXWIPoIa38uWLcP87777LtrDhg2Ljo7OzMxUB1Ue45uIfOOMEdlSh+gjqPENf/7znxs2bPi///u/kZGRM2bMUHf7JHjxzV9dEpmbM0ZkSx2ij2DH96lTp+Li4pDd9957b6nhufNH8OKbiMzNGSOypQ7RR7DjG/70pz/hUSZOnKju8BXjm4h844wR2VKH6CPY8b1w4UI8xN133127du3Dhw+ru33C+CYi3zhjRLbUIfoIanyfOHGifv36Tz311Llz55o0aYIQLykpUQdVHuObiHzjjBHZUofoI3jxjckffPDB2NjYU6dOYXPNmjV4rKlTp6rjKi948c1fXRKZmzNGZEsdoo/gxXfwBC++bfziIJGpOWNEttQh+mB8GzG+iczNGSOypQ7RB+PbiPFNZG7OGJEtdYg+GN9GJovv4uLi8+fPq70VKiwsvHjxotpLZBbOGJEtdYg+GN9GGv3q8tNPP509e/bRo0dlT1FR0bx58xYsWFBSUoLNKVOmREVF/eEPf3Dex50DBw4sWbLk448/Fv9k6KJFi6pVq4Z7VTb3ibTgjBHZUofog/GtKcRunTp1OnbseOnSJdHz97//Hc/M3LlzxWZsbGxSUpLzDi6Q8kOGDLFdFR8ff/jwYfQfO3ZMPMPqHYj054wR2VKH6IPxHTIrVqx4//33xdL43LlzWDunpaWpgyrj3XffxVMxduxYtDEVVs1PPfWU3ItdeAi5iScKK+t169ZhkS56UlJSMCY5ORlP4Pbt25s3b37PPfe4vS+RaThjRLbUIfpgfIfM0qVLceQITbTF31/EwStjVq5cee+1+vTpo4wx6tu3b/Xq1T/99NMWLVq0atUKrwpylzGCp0yZEhkZKVbZCQkJIsE7d+7cpUsXOR4Pjb3ffvutcl8iM3HGiGypQ/TB+A4l8fcX165dizCdPn26uru0dPPmzSOuNWHCBHWQwfnz52+77Tasu2vVqrV3717Zf+HCBTxLCxcuLC3/TLxfv34DBgw4ffr0qlWr0P/xxx+jPyYmxvhZ/6lTp7BrzZo1aNeuXRuJL3cRmYYzRmRLHaKPuLg4sSjTCNatQYrvYP/qMjs7W/79RfEpiuLMmTP7r/X999+rg641dOhQPCd33HHH5cuXZefgwYNjY2OPHz8uNvFYqampSUlJvXv3xuA5c+agMyoqatq0afIuBQUF2LVgwYLS8kV906ZNT548KfcSmYOp4hscDofdbs/IyEhLS8NFvjxAbOVr5CDBceJoccw4chy/ekq+sgX/i4Pi7y++/vrr6o5yb7/9tvGFClq2bKkOMli/fn1ERMT999+PkX//+99l//jx42vUqLFv3z6xOXz4cKzQH3jggUGDBtmufjASHx8/atQoeRe8TmDXJ598gvZ9993Xrl07vJbIvUTmYLb4zsvLw6oQy9j09HRk4oYAQRaoXYGD48TR4phx5Dh+9ZR8ZQtyfGNta7v69xfdLqtPnTq161pYgKuDrvrhhx8aNWrUoUOHoqKi/v37I8eR5mIXevBA7733ntisX7/+6NGj0cjMzJTxPXDgQCyx5bP3yiuv1KlT5+zZs2gj+v/5z3+KfiIzMVt85+fn5+TkZGVlIQ2xnlXiw2eICbUrcHCcOFocM45cfGE5IIIa33ijIP7+It4uiL+/WFxcrA7yGu7bpUuXqKgoPBWl5V9ladGiBdIcz4kYIGMa2rRp07Zt28mTJ6OBlBdrf7ww1KpVq3379m+88caQIUMiIyMTExNd70tkJmaLb6zUsARDDmIli4g5EiCIALUrcHCcOFocM45cfhPOf8GL75KSEvH3F3HY2Pyf//kfPJY/vx4cO3YsZkAiyx7x3cF7771XfAhujOCdO3e2bt0ai+sBAwZ069atZ8+eon/Tpk2dOnXCawBeTrD6ll8hZ3yTWZktvrGOQwJiDYsoxMIwJ0AQAWpX4OA4cbQ4Zhy5P2tYRbB/dRlKDRs2HDZsWEFBgbqjQoj+9PR0/OxWrlyp7iPSn9niO0iCt5Ilb8yZMweL/d/97nfqjgrNnz+/evXqf/rTnwL4kRRR+GB8e4XxHQ6M3yb0Rkk5tZfILBjfXmF8E1G4YXx7hfFNROGG8e0VHePbTL+6JCJXjG+v6BjfOh4zEXmP8e0VHaNQx2MmIu8xvr2iYxTqeMxE5D3Gt1d0jEIdj5mIvMf49oqOUchfXRKZG+PbKzrGNxGZG+PbK4xvIgo3jG+vML6JKNwwvr3C+CaicMP49oqO8c1fXRKZG+PbvXbt2tk8wC51dHjQ8ZiJyGeMb/eSk5PVCLwKu9TR4UHHYyYinzG+3bPb7ZGRkWoK2mzoxC51dHjQ8ZiJyGeMb4+6dOmiBqHNhk51XDjR8ZiJyDeMb49SUlLUILTZ0KmOCyc6HjMR+Ybx7VFubm5UVJQxB7GJTnVcONHxmInIN4zvijz++OPGKMSmOiL86HjMROQDxndFVq9ebYxCbKojwo+Ox0xEPmB8V6SgoKBBgwYiB9HApjoi/Oh4zETkA8b3rxg0aJCIQjTUfeFKx2MmospifP+KTZs2iShEQ90XrnQ8ZiKqLMb3rygpKbmpHBrqvnCl4zETUWUxvn9dUjm1N7zpeMxEVCmM71+3r5zaG950PGYiqhTGNxGRlhjfRERaYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8e2VmjVjxP+GbhpxcXHqSRKRVhjfXkHe9er1qZluOCOHw5GXl5efn19UVFRcXKyeMxGFN8a3V0wZ33a7PTs7OycnByGOBFfPmYjCG+PbK6aM74yMjCNHjmRlZSHBsQZXz5mIwhvj2yumjO+0tLT09HQkONbgWICr50xE4Y3x7RVTxndqaioSHGtwu93ucDjUcyai8Mb49oop43v58uUbNmzYtWsXFuA5OTnqORNReGN8e4XxTUThhvHtlcDG91NPfT5o0BbX/ief/Oz//t9Nrv3yXn37fu7a79uN8U2kO8a3VwIb3ytWHMXz/MILO4ydixZ9f+lSyfffO2TPyJE7pk/PSE7e26fPL6k9Y8aBkpJSDKgg4r2/Mb6JdMf49koA4/vJJz89fTq/uLj03//+j7H/woXL//73cTlm48aT8ieC8cOGbUf/X/+ahs1p0/a7TlvZG+ObSHcyIhjfFQlgfI8btxtP8pdfns7NLfzLXz6T/ehMSflWtOfOPYTNpUsPDxjwxejRu376qeDQoVzXYf7cGN9EupOhzfiuSADje+vWH0+evDB27Nd4qidN2iP7jbn83XeOAweu5DVuU6fuw94RI35ZgBuH+XNjfBPpToY247sigYrvp5/eXFhYvHTpkSef/PTUqfwdO06J/n79NuGZnznzgNjMz7+8cuVRea9Bg7Zg7+TJ6WgXFZUsWvS968yVvTG+iXTH+PZKoOJ73rxfPhVZvfoYVtBYX1+6VDJgwBfo37gx68KFy3/96zYxDP0LFjgzuk+fz8uuhvvWrdk5OYWDB291nbxSN8Y3ke4Y314JVHwfPuyQz7Pw3nu/fBLyr39lFheXvvjiTjHs9On8tWvt8l7Dh2/HyAkTvkEbof+f/+QNHPhL6PtzY3wT6U7GCOO7IgGJ7xde2FF27SfXx46dz8w8h0bv3p9h1+zZB0X/pk0/YIndr9+VLwhitV5YWNy//2a0kfLz53/nOnllb4xvIt0xvr0SkPj+6KP/lJSUPvus83/YWbLkMJ7wUaN++QJ4mSHZR43aeelSyX/+c37p0iMbN57EAXz88ZVvGRqH+XNjfBPpToY247si/sf3X/7y2dmzRfv35xg7hwzZhh+BiGYll8eN242FOUI8N7cQq28sz0U/45uIBMa3V/yP71+95eVdSk09If4HS7c3vAAkJu7ED2jq1H2ueyt7Y3wT6Y7x7ZUQxHdKyqELFy4fPfrLR+Fub7NmHSwuLt23L6eCiPf+xvgm0h3j2yshiG9xM/5/mMrtySd/ubn2+3ZjfBPpjvHtlZDFd8hujG8i3TG+vcL4JqJww/j2CuObiMIN49srjG8iCjeMb68wvoko3DC+vcL4JqJww/j2CuObiMIN49srjG8iCjeMb68wvoko3DC+vcL4JqJww/j2CuObiMIN49srjG8iCjeMb68wvoko3DC+vcL4JqJww/j2CuObiMIN49srjG8iCjeMb68wvoko3DC+vcL4JqJww/j2CuObiMIN49srjG8iCjeMb6/ExcXZzCU6OprxTaQ1xre3HA6H3W7PyMhIS0tLTU1drj+cBc4FZ4TzwtmpJ0xE4Y3x7a28vLzs7GwsVNPT05F6G/SHs8C54IxwXjg79YSJKLwxvr2Vn5+fk5OTlZWFvMOKdZf+cBY4F5wRzgtnp54wEYU3xre3ioqKsERF0mGtarfbj+gPZ4FzwRnhvHB26gkTUXhjfHuruLgYGYdVKsLO4XDk6A9ngXPBGeG8cHbqCRNReGN8ExFpifFNRKQlxjcRkZYY30REWmJ8ExFpifFNRKQlxjcRkZYY30REWjJVfL/66qvGP6qHTe7lXu7l3or36stU8U1EZB2MbyIiLTG+iYi0xPgmItIS45uISEuMbyIiLTG+iYi0xPgmItIS45uISEuMbyIiLTG+iYi0xPgmItIS45uISEuM7yvi4uKMf5OMSFOoZAtWtfGsrYPxfQUqQD4DRPpCJTscjry8vPz8fOtUtfGsi4qKiouL1SvcjJynL1vqEGuwTqGTuaGS7XZ7dnZ2Tk6OdaraeNYIcSS4eoWbkfP0ZUsdYg3WKXQyN1RyRkbGkSNHsrKyrFPVxrNGgmMNrl7hZuQ8fdlSh1iDdQqdzA2VnJaWlp6ejiyzTlUbzxprcCzA1SvcjJynL1vqEGuwTqGTuaGSU1NTkWVYjVqnqo1nbbfbHQ6HeoWbkfP0ZUsdYg3WKXQyN1Ty8uXLN2zYsGvXLutUtfGssQDPyclRr3Azcp6+bKlDrME6hU7mxvhmfFtOFRZ6UVHR6dOn1V4KtKSkpC+//FLtDY7p06evWLFi48aN6o7gY3wzvi2nCgt9/PjxePRDhw6pOzx44okn/MyFU6dOHThwQOm8ePFiamrq/Pnz161bl5eXp+z1k9tH9Jlvs+FJnjNnjmijsWDBglLDBSA6Dx48aOzxzbx5866//no8k40aNTpz5oy6O8hMH9+5ubmLFi1SflKM7yvUIdZQVYWOh46Pj69evfrLL7+s7vPAGEO+iY6OVmZAZCNxbFfVrVsX6WYc4CfXR/SHb7MZnzdxmpMmTfI0wGcOh6NBgwYpKSlot27devTo0eqIIDMGWVVVdZCsXbu2R48etWrVcv1JGc+a8W05VVXomzZtwkNjQd2kSZPi4mJ1tzuutStlZmYuXrwYi+hLly7Jzs2bNy9cuFCu7pcuXYoZ+vTpg0l++ukn9OzduzcqKqp79+779+/Hunv37t3dunW7++67scwpK/9s57PPPluxYsUPP/wg5ywrX6vi4fbs2bNkyZLKPiIax44d+/rrr2fMmCE2jYspZRMHgHcbmOTEiRNl7mYTCgsLcfXiOLE2l514S4FrHp3Z2dlKfDdr1qxatWqff/65HCwHeDoeNL766qtly5bhSRbfTsPMH330UX5+vhz89ttvI74LCgrQxssDXhTlrtAwcXxj0d23b98JEya4XgKM7yvUIdZQVYXer1+/Nm3abN261Vb+zSfRaSsnx7huuo3vqVOnRkZGisEJCQkiT4cNGyZ6IiIiJk+ejJ7mzZuLHkCAoufxxx9v0aKFSBzFzz//3LFjRzEYa941a9bIXejBkcupOnXqdPny5TLvHhGNkSNHYkDPnj3FpvGMjJtnzpzp0KGDuG/NmjVxAK6zAXK8Xbt2ojMmJmbnzp3o/PHHH1u1aiU7bdfGN3L2xhtvvOGGG+TLkhxgHKn0432SmLBx48byEeW5wwMPPIAXY9Hetm0b9vrwOY8/bOaNb0F8n53xXcr4lqqk0M+dO1enTp3k5GQcAAK0V69eol+Eghzmuuka3whrvBIMGDAAQbZ69WqMwaoT/XXr1h06dOjZs2fnzp0rP4dVZoiLi/P00c1f//pXBN/27duR44888ghGOhwOsQuT1KtXT6w9sQDH5ieffFLm3SNiE9GJFy2srN3ulZtDhgyJjY3FNYnzQjJi0e06Xgxr3749VvQZGRlYVuOtAzqfeeaZhg0b4s0EDmbEiBHGe6GdkpKCtz5YgP/xj38U4SsHeDoeNG699VakA94NoI3XBrvdjhddtBEcYjDOa/z48aKN08euDz/8UE4VAjbGN+Pbaqqk0OfNm4fHHTNmDGrxvvvui4qKEp9XVMy1dgWcxfr165OSknr37o0xSE90dunS5aabbvrggw+Mn8woM9SoUQMrd7lpdPPNNycmJoq2uGxkTqGNt7GijfizlQdimXePiM3BgwdXsFduGg+gsLDQdYBwyy23PPvss3PKPfzww3gXghcGHAaeDTEAL2/Ge8nn5/XXX0f7xRdfRBtR/qvx/c4776BRUlKC9rRp02RbnHtZ+ZM5ffp00RYP+v7771+ZKCRsjG/Gt9VUSaHfddddtmvNmjVLHeTCtXaF4cOHI4CwRB00aJAcg9cD9NeuXTshIUF+PKLMgIU/sk9ulpXXgAjf6OhomewXLlzAHbHQFpvKJJV6RGzOnj3buOl2qrJrD0ByfQbwJubKM3hVZmamcl/jvWQbZ9qjRw9s4pWvfv36vxrfrjMobaz35W9EserHrhUrVojN0LAxvhnfVhP6Qv/222+VKrzzzjs7duxoGOKea+0KSB/xPYejR4/KMeLTif3796Nn5cqVYqQyw0svvVSzZk2MkT2TJ0++7bbbsrKy7rjjjv/+7/8WneJTAvnVaWWSSj2isonwffPNN0UbMWrci+fk0UcfFe1Dhw7t2LGjzOXu0L59+0WLFok2lsPiV5odOnR45JFHROfu3buN9zK2canfXA5LeNHp6Xg8zaAcMF4+RVv8b+vbt28Xm6FhY3wzvq0m9IWO0MRi2fjdCYSmrfw3XbZyst91U3zvQli1apXob9OmTdu2bd966y00IiIiJk6cuG3btkaNGiUmJg4dOtR29bPpsvIlbbdu3V577TXxme+5c+dwx3r16o0cOfKdd9558sknMVgE3/z589F+5plnMNv111/fuXPn0qtFo1xCYtPLR1Tue//99zdu3BiJiTtipHGv+FS9b9++2NusWTOcGt4WKLPBggULsN4fMWJEcnIyDhKznT9/HoGO+/bv33/cuHFYFBunVQ7gq6++wguY7PR0PJ5mMLaTkpLwbka033vvvVq1asnPfELDxvhmfFtNiAsdGYSAePDBB42dJ06cQOwiMmzlZL/bTQkLT9GPdXHr1q2xchwwYADSrWfPng6H4/nnn2/QoAEW5ohmOcPYsWMx7Pbbb5dfj8PIUaNG3XTTTVFRUb/5zW+QXGIRDQh05FFsbGyvXr2MLzY2d/Ht5SMq9z1+/HjXrl3r1q0bHx8/adKkmJgY496ZM2e2bNkSd3/ooYfEdwddj7+s/Ft9rVq1QlwmJCRs3bpVdOIVsWnTpsjugQMHys9GylwOoKz8/5OUnZ6Ox3gvT+3vvvsOr8qfffYZ2pikd+/eoj9kbIxvxrfVmLLQyZP169eLVwIjZK5rpw+GDBmCl5D09PQaNWrs3btX3R1kpo9vtxjfV6hDrME6hU7BVlBQ0L1791deeWXMmDHqvuBjfDO+Lcc6hU7mxvhmfFuOdQqdzI3xzfi2HOsUOpkb45vxbTnWKXQyN8Y349tyrFPoZG6Mb8a35cTFxdmI9BcdHS2DLDY2Vt1tUsazZnxbkcPhsNvtGRkZaWlpqampy4n0ZPw31wUrVDX/pXlLx3deXl52djZeutPT01EHG4j0hOpFDaOSs6+yQlUbzxrXsnp5mxHj2yk/Px/vubKyslABeA3fRaQnVC9qGJWcc5UVqtp41riW1cvbjBjfV/CzbzKH2NhYu92OFShSzDpVbTxrLL2LiorUK9yMGN9X2CzzO3oyN1SyDDLrVLXxrBnflmOdQidzY3wzvi3HOoVO5oZKlp8CW6eqjWfNz74txzqFTuaGSpbfwbBOVRvPmt88sRzrFDqZGypZfgPaOlVtPGt+79tyqqrQi4qKTp8+rfaSr5KSkuS/xhlU06dPP3HixObNmzdu3Kjuq1I2/k/z/L8uraaqCn38+PF46EOHDqk7PHjiiSf8zItTp04dOHBAbs4pN3fu3MWLF2/ZsiU/P98wthKUaf3n24S2q/+MFv67YMGCUkOJi07jv6/ms3nz5l1//fVnzpxZtWpVo0aN0FBHVB3Tx3dubu6iRYuUnyPj+wp1iDVUSaHjcePj46tXr/7yyy+r+zyQ8eSz6Oho4wy2a8XGxk6ePNkw3FvKtP7zbUL5/IjTmTRpktu9/sAb8wYNGqSkpIjN1q1bjx49+tohVclm3vheu3Ztjx49atWq5fpzNJ4149tyqqTQN23ahMfFgrpJkybFxcXqbndcC1fKzMzECjo1NfXSpUuyE+/uFy5cKFf3S5cutV39h+rFvzssJ8zLy/v666//9re/RUREvPLKK3KGwsJCXBUrVqzAclh2ll07s+u0ZeVL3WPHjmHOGTNmiE3lXxaWm0VFRXhLgUnkPzXpdkJPR3Lx4kVc2OjPzs6Wp4NGs2bNqlWr9vnnn8uRxmfP0/Gg8dVXXy1btgxPpvglGGb+6KOP5PuSt99+G/FdUFAgNvEKgZW4nKfKmTi+seju27fvhAkTXK8CxvcV6hBrqJJC79evX5s2bbZu3Wor/8WL6LSVk2NcN93G99SpUyMjI8XghIQEkeDDhg0TPUhksaZu3ry56AEEa5m7CcePH483BEgutBGd7dq1E+NjYmJ27twpxigzu05bVj7zyJEjMaBnz55i0/hAcvPMmTMdOnQQ961Zs+aaNWvK3B2npyP58ccfW7VqJftthvhGzt5444033HDDDz/8oDyo0jZuooHTFxM2btxYPminTp0uX76MAQ888ABeceUdt23bhr0+fM4TJDbzxrcgvlHD+C5lfEuhL/Rz587VqVMnOTkZj96iRYtevXqJfhEWcpjrpmt8I6zxSjBgwABk3OrVqzEGq1H0161bd+jQoWfPnp07d678fFaZwXVCBCI6MU9Z+T+a3r59eyyiMzIysJi9++67xRjXmV3nQQ/SEy9OWFy7DpCbeIjY2FhcdTh4JCNW3MoAwdORPPPMMw0bNty9ezcOZsSIEfJeaKSkpOD9DRbgf/zjH0XyGuf0dDxo3HrrrYgAvCFAG68NdrsdL65oIx0wACeFVzh5R5w+dn344Yeyp2rZGN+Mb6sJfaHPmzcPDzpmzBgU4n333RcVFZWbm6sOcuFauAJOYf369UlJSb1798YYpCo6u3TpctNNN33wwQfGT2Y8xZZUWFiIzoULF6J9yy23PPvss3PKPfzww1jgiyx2ndl1HvQMHjzYuOn2cW+++ebExETRiYd2HSB4OhIcBs5ajMHLmLyXfBJef/11tF988UW0EeVyTk/Hg8Y777yDRklJCdrTpk2TbfF5d40aNaZPny7vKB70/ffflz1Vy6ZPfN922202D7BLHX0V41tynr5sqUOswRbyQr/rrruUkp01a5Y6yIVr4QrDhw9HNmH1OmjQIDkGrwfor127dkJCgvysVpnBdcKvvvoKnV988QXaeH9wzSHabJmZmWXuZnadBz2zZ882brp93Ojo6KlTp8p+SRnv6UiUu8t7yQZ+uD169MAmXt7q16/vTXy7HSPbWOwbfyOKVT92rVixQvZULZs+8e0bxrfkPH3ZUodYQ4gL/dtvv1VK8M477+zYsaNhiHuuhSsgmMT3H44ePSrHiPXp/v370bNy5Uox0lNsCchlvK5gqSuW1e3bt1+0aJHYhRWo/C2i68yuB6b0IH/ffPNN0UaSyr048UcffVT0Hzp0aMeOHaKt3N3TkXTo0OGRRx4R7d27d8t7Ge+Oi/nmcjgv2enpeIx3dNvGAeM1UnSC+L9jtm/fLnuqlo3xzfi2mhAX+ksvvYTFsswgmDx5sq38N2C2crLfdVN8H0NYtWqV6G/Tpk3btm3feustNCIiIiZOnLht27ZGjRolJiYOHToU9/rkk0/ESCxXu3Xr9tprr8mPg8WEuK/4HBnk//myYMECLLFHjBiRnJzcuXPnxo0bnz9/3u3MyrRiZuM1dv/99+PuSEzcEYPl3iVLlqDdt29f7GrWrBmOX7xyKBO6PZKy8m8j4O79+/cfN24cjlxOqzw63lLUrFnT2OnpeIxj3LaTkpJatGghOuG9996rVauW8WOfqmVjfDO+rSaUhY54QnA8+OCDxs4TJ04gdhEltnKy3+2mhDWp6Efgtm7dGivKAQMGIPV69uzpcDief/75Bg0aYGE+cuRIOcPYsWMx7Pbbbxffk5NTYWS7du2whM/KypKDy8q/SNeqVSskVEJCwtatW8vKv/jsOrMybZlLgB4/frxr165169aNj4+fNGlSTEyM3Dtz5syWLVvi7g899JD87qDrhK5HIuCVr2nTpsjugQMHyo9HlEcvK///JI2dno7HOMZt+7vvvsNL72effSb6MUnv3r1FOxzYGN+Mb6sxZaFb2fr16+UrgYTMde30wZAhQ/ASgpfh/fv316hRY+/eveqIqmP6+HaL8X2FOsQarFPo5L+CgoLu3bvv27cPa8AxY8aou6sU45vxbTnWKXQyN8Y349tyrFPoZG6Mb8a35Vin0MncGN+Mb8uxTqGTuTG+Gd+WY51CJ3NjfDO+Lcc6hU7mxvhmfFuOdQqdzI3xzfi2nLi4OBuR/qKjo2WQxcbGqrtNynjWjG8rcjgcdrs9IyMjLS0tNTV1OZGejP/mumCFqua/NG/p+M7Ly8vOzsZLd3p6OupgA5GeUL2oYVRy9lVWqGrjWeNaVi9vM2J8O+Xn5+M9V1ZWFioAr+G7iPSE6kUNo5JzrrJCVRvPGteyenmbEePbqaioCC/a+Nnj1Rvvv44Q6QnVixpGJeddZYWqNp41rmX18jYjxrdTcXExfup43caP3+FwyJULkV5QvahhVHLRVVaoauNZ41pWL28zYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8U1EpCXGNxGRlhjfRERaYnwTEWmJ8U1EpCU38U1ERBphfBMRaYnxTUSkpf8PG/giw2o9DLUAAAAASUVORK5CYII=" /></p>

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 75

    // ステップ3
    // オブジェクトA{1}の所有がa1からxへ移動する。
    // xは以前保持していたA{0}オブジェクトへのポインタをdeleteするため
    // (std::unique_ptrによる自動delete)、A::LastDestructedNum()の値が0になる。
    ASSERT_EQ(1, a1->GetNum());                 // a1はA{1}を所有
    x.Move(std::move(a1));                      // xによるA{0}の解放
                                                // a1からxへA{1}の所有権の移動
    ASSERT_EQ(0, A::LastDestructedNum());       // A{0}は解放された
    ASSERT_FALSE(a1);                           // a1は何も所有していない
    ASSERT_EQ(1, x.GetA()->GetNum());           // xはA{1}を所有
```
<!-- pu:deep/plant_uml/unique_ownership_3.pu--><p><img src="data:image/png;base64,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" /></p>

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 88

    // ステップ4
    // x.ptr_はstd::unique_ptr<A>であるため、ステップ3の状態では、
    // x.ptr_はA{1}オブジェクトのポインタを保持しているが、
    // x.Release()はそれをrvalueに変換し戻り値にする。
    // その戻り値をa2で受け取るため、A{1}の所有はxからa2に移動する。
    std::unique_ptr<A> a2{x.Release()};         // xからa2へA{1}の所有権の移動
    ASSERT_EQ(nullptr, x.GetA());               // xは何も所有していない
    ASSERT_EQ(1, a2->GetNum());                 // a2はA{1}を所有
```

<!-- pu:deep/plant_uml/unique_ownership_4.pu--><p><img src="data:image/png;base64,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" /></p>

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 99

    // ステップ5
    // a2をstd::move()によりrvalueに変換し、ブロック内のa3に渡すことで、
    // A{1}の所有はa2からa3に移動する。
    {
        std::unique_ptr<A> a3{std::move(a2)};
        ASSERT_FALSE(a2);                       // a2は何も所有していない
        ASSERT_EQ(1, a3->GetNum());             // a3はA{1}を所有
```

<!-- pu:deep/plant_uml/unique_ownership_5.pu--><p><img src="data:image/png;base64,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" /></p>

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 109

        // ステップ6
        // このブロックが終了することで、std::unique_ptrであるa3のデストラクタが呼び出される。
        // これはA{1}オブジェクトへのポインタをdeleteする。
    }                                      // a3によるA{1}の解放
    ASSERT_EQ(1, A::LastDestructedNum());  // A{1}が解放されたことの確認
```

<!-- pu:deep/plant_uml/unique_ownership_6.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhIAAAE0CAIAAAD2Qk1eAAAzAUlEQVR4Xu3dCXAVVboH8A5bgIQQyCDIIgRn4JGyYODBxHGpp+gIIjgzOjwpoIbFBeoNEvMEU/UcEJBdtofsT9lFEZ4zYpGgJTuCAkIgiI5sLxiJke1CIBtZ3p97htMnp+8N6eTeG273/1eWdfr01+d233znfN25STDKiIiIKs3QO4iIiPxj2SAiIhvMslFKRETkB8sGERHZwLJBREQ2sGwQEZENLBtERGQDywYREdnAskFERDawbBARkQ0sG0REZAPLBhER2cCyQURENrBsEBGRDSwbRERkA8sGERHZwLJBREQ2sGwQEZENLBtERGQDywYREdnAskFERDawbBARkQ0sG0REZAPLBhER2cCyQURENrBsEBGRDSwbRERkA8sGERHZwLJBREQ2sGxUxenTp3v06PH666/rO4iInM4hZaOgoOAjxcaNG/ft2yf3ZmVlvWHx/fffKwNU5MKFC8ePHz927FhGRsbRo0fT09NxeO/evVu1aiUC8vLydu3atX///pKSkvKHEhE5jUPKBlb2xo0bx8bGNmvWrHXr1o0aNWrZsqVcxFEhnrI4ePBg+TFuQvnRu0pLp06daljExMSkpqZi7w8//NCxY0fR+ac//Uk/mIjIWRxSNlQ3bty49957J0+eLHuO+3HlyhUZ8+WXX+JxASUHFQibzz333MyZM8WuS5cunTp1KjMzE08t2dnZ58+ff/jhh0eMGCH2vvjii6NGjfJ4PP/3f/935swZOSARkSM5sGwsXbo0KipKrP5QVFRU/jnBtG7dOhFz4sSJunXrfvTRR+3atRszZgx62rZtO336dDmmKjc3t2HDhmvXrhWbnTp1wtPMli1bDh06VD6QiMiBnFY2Dh8+jDVdLP3SuVvefPPNFi1ayM28vDwZM3r06F//+tfvvvvun//8ZzyFREREbNq0SRnDtGDBgujoaPmkghJVq1YtUYf69u2LZ53y4UREjuKosnHw4MGWLVvGx8djKU9LS9N3l5a+8sor3bt313u9zpw5s3DhQrHoT5s2rV69ehcvXtSDSkuPHTsWGxv7xhtvyB48lyQnJ1+/fn337t2oHDt27FDCiYicxiFlo7i4eNmyZXjO6N27N1ZwPFXUrVtXqxyHDh2Ki4vDLrVTk5+fj5qBp4cJEyZou65duzZ37tzGjRv36dOnqKhI9uPJJjExcc2aNUlJSTiw8j+gRUQUjpxQNi5dutStW7c6deqMHz9efo8IqzmeOfbv31/qXfF///vfY01/+umnUVTKHax49dVXmzVr1qBBgylTpqj9KBJDhgxBwWjUqBGqjlozSr2DDx8+vEmTJvfcc8/y5cvVXUREzuOEsgFvv/32N998o/aUlJSgipw7d05s4lnks88+UwOs1q5dO2/evJycHH1HaemsWbMwgsfj0XcQEbmMQ8oGERGFBssGERHZwLJBREQ2sGwQEZENLBtERGQDywYREdnAskFERDawbBARkQ0sG0REZIOjykZcXFy5P4xOVDnIHD2ZKk3NOvVvXAI2lRfhXu4tt7c6WVezHFU28LWRV0FUecgcj8eTm5ubl5dXWFhYXFys55Z/OFbvIqqE8M0cc+LIlh4SPlg2qGqQOZmZmdnZ2RcvXkTxQOXQc8u/8J38VLPCN3PMiSNbekj4YNmgqkHmZGRknDhxIisrC5VD/fe7bit8Jz/VrPDNHHPiyJYeEj5YNqhqkDl79uxJT09H5cAzBx449NzyL3wnP9Us7dOOMGJOHNnSQ8IHywZVDTInNTUVlQPPHJmZmbb+Qn74Tn6iqjEnjmzpIeGDZYOqBpnz/vvvb9myZf/+/Xjg8PnvARORYE4c2dJDwgfLBlUNywZR5ZkTR7b0kPBxh5SNlJSUL7/8Uu8lPwoLC3NycvTe0HJA2UDW7du3T+8lPwoKCn766Se9lyrHnDiypYeEj9CUDWTbsWPH9F4FTmPx4sV6byBg2G+++UbvDa3bXr5dEydOxDt2/PhxfUcI3fllIzs7OyMjQ+9V4BIWLVqk9wYChsVXXO8Nrdtevl0TJkzAO6b9S9IhFr6fipkTR7b0kPARmrIRFRVVcVUIXtkI3siVd9vL9+frr7/Wu7zJFh8fX6dOnddee03b9Y9//CM3N1frDJLqlI3QTH687RVXheCVjeCNXHm3vXx/Dh48qHeVlpaUlMis03Z99913V69e1TqDxAjbn8EzJ45s6SHhI0hlY/v27StXrhS3w2vXrsWrDBw4EEvnzz//LGOuX7/+ySefrF+/HrdFlVzctUcHdRPtkydPHjp0aM2aNampqUVFRTJMhQdtrHTr1q07ffr0Bx98kJ6eLvorGFkcgvPEQ4MM8AlHff/999u2bXvvvfdOnTolOn1ePto4gQMHDrz99tvm8Yrdu3f/27/927333qvvKCvD+Bjw2WefbdmyZXFxsbpr7ty5v/jFL2bNmpWXl6f2B0N1ykaQJj/emRUrVojbYaSBeNuxdObk5MiYa9eubdq0CV/6c+fOVXJx1x4d1E20ce2o7qtXr968ebO/33nMz89PS0sTWYE37fDhw6K/gpHFIThPzA4Z4BOOwu3C1q1bkWmYAqLT5+WjjRPA12v+/Pnm8Ypdu3aJrNN3lJZifJl1N27cUHfNmTMHWffWW29hRqv9wRCkzAkBc+LIlh4SPoJRNl5++WXDKyIiYubMmW3bthWbgIVSxGDSdujQQXTGxMQYt8qG6JFDWTfV6qJuop2QkCDioUePHkhuLQZLW5cuXURAZGRkdHS0erjPkbHQd+7cWRyC89y3b5+MsUJMq1atRHC9evVQnNDp8/LRTk5OxvvTt2/fckOUlSGmV69eCHjyySdx36fthcGDB+NKMcMN74/AqruuXLkyYcKExo0b33333QsWLMAqpu4NLOMOKxtq1s2YMUN923GGIubHH3/Usk6UDdEjh7JuqtVF3TQsWYf7FS3mwoULWtaph/scGQu9mnV79+6VMVZG+axDcUKnz8s3lKwrN0RpKWJk1iEDtb0gsm7nzp2IQYFUd3k8Hjw+iqzDbRBus9S9gWUEIXNCw5w4sqWHhA8jCGUDE2PUqFGXL19esmTJ+fPnyyyLMgwbNqxp06ZYFhGWlJQkA0SiyzDrps/FXbQbNWr08ccf40Zb3Gp9+umnWszIkSObNGmCG3nM5BdffFE73OfIOARzHk8GGRkZrVu3fvDBB2WMFY7CbRemFiYSxo+NjcViKvq1y0cP5hiWfnVlx63iH/7wB+zq2bPnF198oYSbUBgaNmw4ffp0fO3at2/fv39/PaKs7NKlS//1X/+FrwLWDtwF67sDxLjDyobIOlz7Yu9TXallUQaRdVgWESayrvplA1n397//HTfaeKuxiTdEixFZh6815oLIutuWDZF1eDI4evSoyDoZY2V4s27Hjh2YSiLrkN6iX7t8w5t1yE91ZcfXTmbdnj17lHAT8hlZN23atJKSEpF1ekRpKRJAZt2qVav03QGifl3CizlxZEsPCR9GEMrGI4880qZNG9xry2+hGJZ1EwEpKSmijRs0a4BPWpi6ifabb74p2njOwOayZcu0mHbt2o0dO1aNuW3ZwCHPP//8Yq+nnnqqVq1aFdzC4ygs6KL9ww8/GN5FRPRby8aIESPUnjLvt7NwJ9ipU6dDhw5pu6SlS5fi2HHjxmHARx99FHevWAH1oLKyq1ev4r4Skb/97W/1fQFi3GFlQ2Qd7rXlt1AMy7opsk608XW0BvikhambaE+aNEm0RRrjC6TFiKxTY25bNkTWLfISWVfBLTyOwoIu2mfPnsVmWlqa6LeWDWSd2lPq/XaWyLqvv/5a2yXh/s/wZh0GFFnn88uNexqZdfq+AAnNp2LBYE4c2dJDwocRhLKBhWz06NENGjRITEzMz88v87VuRkVFzZ49W25aA3zSwtRNf7vU/gpe1N/huMkyysMzgQzTqINcu3YNm5iTWr+MxAxUewQUDCwTmMa///3vfX4efv/995c/HWPhwoVqAArGlClTcE+Nu1S8qL/PeKrPqEbZCMbkxwnIrBN/IEu8yWoMEmDWrFly0xrgkxambvrbpfZX8KL+DrdmHd5hGaZRB8nNzcUmnnu0fhmJbFF7BGSazDqfn4dbs27BggVqAArG5MmTRdbhRf19xuNm5sSRLT0kfBhBKBvifhzP1xj8ww8/LPO1bnbt2rVfv36ijUy1BviE6TRjxgzRxi2VepQ2gtxU+9UXPXLkiLrL38hdunTBE7foxxO6+pG+FY565ZVXRDs1NRWb4pdRrFdn7VHt27evZ8+eiBkyZIja/+2332oHduvWrXv37nLzs88+w9Rt3rz53LlzcX8q+4PBqEbZCAZxPy6+rOvXry/1tW6KBBDtAwcOWAN8kt8VBPFlve26r/arL5qenq7u8jcysm7lypWiH4/s6kf6ViLrRHvz5s3YFL+MYr06a49q7969MuvU/uPHj2sHiqyTm59++qnIujlz5uA2UfaTypw4sqWHhA8j0GVj9+7dzZo1GzNmzKhRo4xbHzDghqtXr154nBcfUwPWYpGgEyZMQM4ZyiqvnpK2ibRu0aIF1neMjzHlUSLytmVDvujEiRNxkuoufyOvWLECN7BJSUmY3g888ABicDt/60V0hvfz2JdeemnatGmI/M1vflPqTRfr5Wtn69P27dv//Oc/qz1jx46tXbu2WrpmzpyJoeQvheACp06digcdGRA8xp1UNnbt2qVmnfiAQbzt+FqLj6kBa7FIADzuiKyTq7zh/7MNkRtIAJkbtsqGfFGkusg6ucvfyMuXLxdZh0QSWYfb+VsvojNuZR2+9CLrcH9T6uvytbP1adu2bcg6tUdknVq6ME0M798/Fpu4QDzg2vpbli5kThzZ0kPChxHosuHxeJDBTZo0ady4cXJysugcP348bqw6duyo/pArlrxWrVph9g4fPhzBlSkbZ86ceeKJJ6Kjo+Pj4zFJYmJibJWNMu+L4jkaLzdgwAB1VwUjo9GhQ4f69esnJiZieZJDWWFATFSMgHH69Onzww8/iH7r5WtnVRm468Si8Pjjj6udZ8+exZKBRUftDA3jTiobly9fVrNOdMq3Xf0hVyx5atZVpmycPn1a5gbWR+SGrbJR6n1RNevkrgpGRkNm3c6dO+VQVlrWISVEv/XytbOqDNzoiKxTOzMzM0XWqZ1UMXPiyJYeEj6MQJeNMGLYX7uFxRbiG1lVHjAcGXdS2QgjVVi7hUUW4htZVR4wHAXjU7HQMCeObOkh4YNlQ++thJv3ouU1b95c9FdtwHBkVKNshO/krz6jqqu8lnKGN+tEf9UGDEdGEH4GLzTMiSNbekj4MFxcNkaMGFHxN53sCviAdzKjGmUjfCd/9SFJKv6mk10BH/BOFr6ZY04c2dJDwoebywZVB8sGhV74Zo45cWRLDwkfLBu3lZubu2nTplWrVvFPu6tYNoLqwoULGzZsWLNmzZEjR/R9Lha+mWNOHNnSQ8IHy0bFtm3bFhsba9zSr18/7a8HuhbLRvCsW7dO/MZfLa9BgwYh6/QgVwrfT8XMiSNbekj4YNlQnTx5cvXq1eof0H3ooYcSExO//fbbvLy8efPm4e365JNPyh/kUtUpG+E7+YMB7x6eZeUf0L1+/fp99933zDPPiB+lFX89UPy9EApf5sSRLT0kfLBsSLNnz8adnXiqQKmQlUP+urXH48Gujz76yDzGxapTNkiaNWuWmnWicuDZQv59DvE3FDZt2lTuMAo35sSRLT0kfLBsCCgSgwcPHjp06M8//7xx40brU0V+fv6gQYPatGkj/qYvsWxUH2qDyLqcnJwNGzao5eH06dPJycnPPfdcdHT0H/7wB/6Vp3BnThzZ0kPCB8uGhHcjLS0tJSVF/CrvkiVL5C7c8SUkJDz88MNZWVnKEa7GshEQJSUlqampMusWL14s+o8cOYJ8a9u2bfPmzd3zaxkOZk4c2dJDwgfLhjR69OjatWs/9thjL7zwgpjAon/58uVRUVEzZszADC9/hKuxbASElnXWCvHOO++gv+J/qck9wvdTMXPiyJYeEj5YNqTGjRu//vrraJw6dUqWjf/93/+tV6+e9o/oUVn1ykb4Tv6AE1mHxsmTJ0XZKCgo+J//+R/5twtzcnLQv3bt2nKHuZURtj+DZ04c2dJDwgfLhpSQkHDfffe99dZbaEREREyZMiUvL69Zs2Y9evRQ//zUBx98oB/pStUpG+E7+QNOZN3MmTNF1k2ePBnvZ2Rk5K9+9atJkyahv1u3bnjYzczM1I90pfDNHHPiyJYeEj5YNqQvv/yyU6dODRs2HDp0aK9evfr27ZudnW1YdOzYUT/SlQyWjUDYt2+flnWl3n8L5Mknn4zxevjhh3fs2KEf5lbhmznmxJEtPSR8GCwbVCUsGxR64Zs55sSRLT0kfLBsUNWwbFDohe+nYubEkS09JHywbFDVVKdshO/kJ6oac+LIlh4SPlg2qGqqUzaI3MacOLKlh4QPlg2qGpYNosozJ45s6SHhg2WDqoZlg6jyzIkjW3pI+GDZoKph2aDQC99PxcyJI1t6SPhg2aCqqU7ZCN/JTzUrfH8Gz5w4sqWHhA+WDaqa6pSN8J38VLPCN3PMiSNbekj4iIuLM4jsi4qKqnLZkFmnPXZgU30J7uVebS8yR+0MI44qG+DxeDIzMzMyMvbs2ZOamvq+ixneO2iqJGQLcgaZg/xBFumJRZVjhO0dNFWe08pGbm5udnY2bhjT09OxCmxxMUxgvYv8Q7YgZ5A5yB9kkZ5YVDksG27gtLKRl5d38eLFrKwszH/cOe53MUxgvYv8Q7YgZ5A5yB9kkZ5YVDksG27gtLJRWFiIW0XMfNwzZmZmnnAxTGC9i/xDtiBnkDnIH/6rpVXGsuEGTisb4t+7x90iJr/H47noYpjAehf5h2xBziBzkD/IIj2xqHJYNtzAaWWDJE5gCj1mnRuwbDgWJzCFHrPODVg2HIsTmEKPWecGLBuOxQlMocescwOWDcfiBKbQY9a5AcuGY3ECU+gx69yAZcOxOIEp9Jh1bsCy4VicwBR6zDo3YNlwLE5gCj1mnRuwbDgWJzCFHrPODVg2HIsTmEKPWecGLBuOxQlMocescwOWDcfiBKbQY9a5AcuGY3ECU+gx69yAZcOxOIEp9Jh1bsCy4RydO3c2/MAuPZooEJh1LsSy4RzTp0/XJ+4t2KVHEwUCs86FWDacIzMzs1atWvrcNQx0YpceTRQIzDoXYtlwlEceeUSfvoaBTj2OKHCYdW7DsuEoy5Yt06evYaBTjyMKHGad27BsOMqlS5ciIyPV2YtNdOpxRIHDrHMblg2neeaZZ9QJjE09gijQmHWuwrLhNBs3blQnMDb1CKJAY9a5CsuG0+Tn5zdp0kTMXjSwqUcQBRqzzlVYNhzohRdeEBMYDX0fUXAw69yDZcOBtm3bJiYwGvo+ouBg1rkHy4YDlZSUtPFCQ99HFBzMOvdg2XCmFC+9lyiYmHUuwbLhTEe89F6iYGLWuQTLBhER2cCyQZVSVFQkv2ettomCh1l3Z2LZoEoxDGPRokXWdgWys7MzMjL0XqJKY9bdmVg2qFKqMIGjoqIqE0bkD7PuzsSy4UaYVydOnPj6669Xr169efPmwsJC2X/s2DE1TG5WMIHR/sc//rF169a1a9eePHlSdK5ZswZhAwcOxN6cnBwRdurUqf3798+fP18eS+7BrHMMlg03wtRKSEgwbunRo0dRUZHoV2emv0lrDWvVqpUYql69eu+99x4627ZtK8fHpBVhycnJERERffv2lceSexjMOqdg2XAjzKVGjRr9/e9/v379Om79sLllyxbRX7UJ/Itf/GLHjh2XL19+8cUXY2NjL1y44DPs7rvv3rlzZ0FBgewk92DWOQbLhhthLk2aNEm0cceHzaVLl4r+qk3gadOmifbZs2exmZaW5jNsxIgRcpPchlnnGCwbbmSdWmLTX38FbW0zNzcXm7iX9Bm2cOFCuUluY80HZl2YYtlwI+vUEpsNGzacPn266ExNTfU3aa2Hv/LKK6K9efNmbO7bt89nmLpJbuMvH5h1YYdlw438Ta2ePXu2aNECc3jMmDFRUVH+Jq318IiIiJdeemnq1Kk4/De/+Y34tSyM0KtXr4kTJ/r85JPcxpo2zLowxbLhRtYZKDZPnz79xBNPREdHx8fHT5kyJSYmxuektR6OiYpDcGCfPn3Onj0r+sePH48byY4dO4qfp+QEdjlr2jDrwhTLBlUXZyaFHrOuBrFsUHVxAlPoMetqEMsGVdeIESN27typ9xIFE7OuBrFsEBGRDSwbRERkA8sGERHZwLJBREQ2sGwQEZENLBtERGQDywYRBUxcXNwbb7yh9mDTUITdXlyRuotKWTaIKICwzupdYc55V1R9LBtEFDDOW2Sdd0XVx7JBRAHjvEXWeVdUfSwbRBQw2ocEDsCyYcWyQUTkl/MKYfWxbBARkQ0sG0REZAPLBhHdoQoKCn766Se9t7S0uLj46tWreu8tOOr69et67x0pJSVF/BPo/hQVFYl/7PaOwrJBRAET2E8CJkyYYBjGN998o3bOmjUrMjLyt7/9rey5ePHiypUrxb8CC6tWrapduzYCKigtdwjjdv/Y1G0DIDs7OyMjQ+8NJpYNIgqYAP7cEe6y4+Pj69Sp89prr6n9sbGxuEkX7U2bNvXp06d+/fra8nr69Gn0vP/++7KnygJbCDW3rQq3DYCoqKjbxgQWywYRBUwAy8bWrVsx2rPPPtuyZcsbN27IfnUlxUPGoEGDJk2aZF1erT1VE8ArEq5du4Zq98EHH5w7d049yfz8/LS0NPTj6UEGa1dhjVmzZg1iBg4ciLCcnBx/YYHFskFEARPARXbw4MEJCQk7d+7EmJs3b5b91nrw/fffWzutPVUTwCuCH3/8sUOHDoZXTEyMPEms+J07d5b9e/fuFfHqVfiMadu2reiB/fv3+wsLLJYNIgoYI0CLrMfjadiw4bRp00pKStq3b9+/f3/Rj1t1vAQeMtRgn2WjQYMGs2bNUnuqJlBXJAwbNqxp06YHDhy4dOlSUlKSPO2RI0d26dLl1KlTR48ebd269YMPPiji1euqTEwFYQHEskFEAROoTwKWLFmC1XDcuHFYEB999NHIyMiLFy+if8SIEbGxsWfOnFGDfZaNQYMGtWrV6ocfflA7qyCwZaNNmzbyg5nCwkJ52u3atXv++ecXeT311FO1atUqKCgoLV8SKhNTQVgAsWwQ0R3n/vvv936XxbRgwQL0T5w4sW7dukeOHFGDfZYNFJvOnTufP39e7ayCQBVCISoqSn0GkqeNRyvtek+cOKEGVDKmgrAAYtkgojvL8ePHtaWwW7du3bt3L711h/7OO++Y0X7KBqrLf//3f6s9d4KuXbv269dPtA8cOCBPu0uXLvI7b8XFxfLDbfW6KhNTQVgAsWwQ0Z1l7NixtWvXVte7GTNmYHEUv51grRA+y4a1506ABR0nNmTIEDzENG3aVJ7k8uXLGzRokJSUNG3atAceeKBFixZXrlwpLX8V/mLwBNOrVy88hxUVFVUQFkAsG0R0B7lx4wZWuscff1ztzMzMjIiIGDNmTKmvehBGZaPUWwJbtWqFmjF8+PDGjRvLk0SjQ4cO9evXT0xM3Llzp+jUrsJnzPjx4xs2bNixY0f5C48+wwKIZYOIAiawnwT4hAX35Zdfzs/P13fcgsKTnp6OBffDDz/U91EgsGwQUcAYAf25I58WL14cGxv7r//6r/qOW5YvX16nTp3f/e53eXl5+j77QlAIww7LBhEFTAjKhqD+3rimxEvvraqQXVEYYdkgooBx3iLrvCuqPpYNIgoY5y2yzrui6mPZIKKAcd4nASwbViwbRER+Oa8QVh/LBhER2cCyQURENrBsEBGRDSwbRBQw/CTADVg2iChgnPdzRyyEViwbRBQwzisbzrui6mPZIKKAcd4i67wrqj6WDSIKGOctss67oupj2SCigHHeJwEsG1YsG0REfjmvEFYfywYREdnAskFERDawbBARkQ0sG0QUMPwkwA1YNogoYJz3c0cshFYsG0QUMM4rG867oupj2SCigImLi8M6q92hY9NQhNdeXJHaT6UsG0REZAvLBhER2cCyQURENrBsEBGRDSwbRERkA8sGERHZwLJBREQ2sGwQEZENLBtERGQDywYREdnAskFERDawbBARkQ0sG0REZIOjykYl/6Ql93Iv93IvVZmjygYREQUbywYREdnAskFERDawbBARkQ0sG0REZAPLBhER2cCyQURENrBsEBGRDSwbRERkA8sGERHZwLJBREQ2sGwQEZENLBtERGQDy8Y/xcXFqX8jkyhMIZNdmNXqVVOwsWz8EzJPvgNE4QuZ7PF4cnNz8/Ly3JPV6lUXFhYWFxfrM5wCx3zbZUsPcQf3TDByNmRyZmZmdnb2xYsX3ZPV6lWjeKBy6DOcAsd822VLD3EH90wwcjZkckZGxokTJ7KystyT1epVo3LgmUOf4RQ45tsuW3qIO7hngpGzIZP37NmTnp6ONdQ9Wa1eNZ458MChz3AKHPNtly09xB3cM8HI2ZDJqampWENx9+2erFavOjMz0+Px6DOcAsd822VLD3EH90wwcjZk8vvvv79ly5b9+/e7J6vVq8YDx8WLF/UZToFjvu2ypYe4g3smGDkbywbLRrCZb7ts6SHuUIMTrLCwMCcnR++lQEtJSfnyyy/13uCYP3/++vXrP/vsM31H8LFssGwEm/m2y5Ye4g41OMEmTpyIVz9+/Li+w49nn322muvRTz/9dOzYMa3z+vXrqampy5cv37x5c25urra3mny+YpVVbTS8yYsXLxZtNFasWFGqTADR+c0336g9VbN06dK77roL72SzZs3Onz+v7w4yx5eNS5curVq1SvtKsWyEkvm2y5Ye4g41NcHw0vHx8XXq1Hnttdf0fX6oy1/VREVFaSOgVGClM26Jjo7GqqoGVJP1FaujaqOp75u4zKlTp/oLqDKPx9OkSZNly5ah3alTp9dff12PCDJ1Aa2prA6STz75pE+fPvXr17d+pdSrZtkINvNtly09xB1qaoJt27YNL40HiJYtWxYXF+u7fbHOGenkyZOrV6/GQ0NRUZHs3L59+8qVK+XTzNq1azHCwIEDMcjPP/+MnsOHD0dGRvbu3fvo0aN4zjh48GCvXr0efPBB3NaVeb+H9vnnn69fv/7HH3+UY5Z5783xcocOHVqzZo3dV0Tj9OnTBw4cePvtt8WmevOobeIE8HSFQc6ePVvmazShoKAAqwbOE88ishOPUFhr0Jmdna2VjdatW9euXXvr1q0yWAb4Ox80vvrqq/feew9vsvgpT4z88ccf5+XlyeA5c+agbOTn56ONsoRiLHeFhoPLBh4yBg0a9Oabb1qnAMtGKJlvu2zpIe5QUxNs8ODBCQkJu3btMrw/QSg6DS8ZY930WTZmz55dq1YtEZyYmCjW8Zdffln0REREzJw5Ez1t27YVPYCFGz3PPPNM+/btxUqnuXDhQvfu3UUw7vE/+ugjuQs9OHM5VI8ePW7cuFFWuVdEIzk5GQF9+/YVm+oVqZvnz5/v2rWrOLZevXo4AetogPrRuXNn0RkTE7Nv3z50njt3rkOHDrLTKF82sL7ffffdzZs3l+VQBqiRWj+eC8WALVq0kK8orx0ee+wx3ASI9u7du7G3Ct9Pqw7DuWVDEL+PwrJRg8y3Xbb0EHeokQl25cqVhg0bTp8+HSeAhbt///6iXyxGMsy6aS0bKBKoQEOHDsUCunHjRsTgLhv90dHRo0aNunz58pIlS+T32bUR4uLi/H2L7D/+4z+w4H7xxReoH/369UOkx+MRuzBIo0aNxL02Hjiw+emnn5ZV7hWxiSUbxRJPEj73ys2RI0fGxsZiLcB1YUXGQ4Y1XoR16dIFTzAZGRl4jMCjEjqHDRvWtGlTPDzhZJKSktSj0F62bBke9fDA8dBDD4lFXwb4Ox80fvnLX2JVwtMP2qhJmZmZKPZoY8ESwbiuiRMnijYuH7v+9re/yaFCwGDZYNkIMvNtly09xB1qZIItXboUrztu3DjMgUcffTQyMlJ8X6hi1jkj4CrS0tJSUlIGDBiAGKza6HzkkUfatGmzbt069Ttg2gh169bFk4rcVN1zzz1jxowRbTFd5fqI9ptvvinaWHYN70JcVrlXxOaIESMq2Cs31RMoKCiwBgjt2rV7/vnnF3s99dRTeOpCQcJp4N0QASir6lHy/Zk8eTLar776KtooIbctG/PmzUOjpKQE7blz58q2uPYy75s5f/580RYv+u677/5zoJAwWDZYNoLMfNtlSw9xhxqZYPfff79R3sKFC/UgC+ucEUaPHo2FD7fkL7zwgoxBHUJ/gwYNEhMT5behtBHwoIM1V26WeXNALPpRUVGyoly7dg0H4sFCbGqD2HpFbC5atEjd9DlUWfkTkKzvAB7a/vkO3nLy5EntWPUo2caV9unTB5uouI0bN75t2bCOoLXxfCM/acdTDnatX79ebIaGwbLBshFk5tsuW3qIO4R+gn377bda9nfr1q179+5KiG/WOSNg1RM/t3Pq1CkZI74LdPToUfR8+OGHIlIbYezYsfXq1UOM7Jk5c+avfvWrrKysX//613/84x9Fp/hujPzVB20QW6+obWLRnzFjhmhj+Vb34j15+umnRfv48eN79+4tsxwOXbp0WbVqlWjj9l98VN61a9d+/fqJzoMHD6pHqW0sMfd44ZFFdPo7H38jaCeMsi3a4s97fPHFF2IzNAyWDZaNIDPfdtnSQ9wh9BMMizUeDtSfBcJibXg/QTW8ZL91U/wckbBhwwbRn5CQcN9997311ltoRERETJkyZffu3c2aNRszZsyoUaOMW589lHlv4Xv16jVp0iTxPf0rV67gwEaNGiUnJ8+bN+/f//3fESwW3OXLl6M9bNgwjHbXXXc98MADpbeSRpu6YrOSr6gd27NnzxYtWmClxoGIVPeKT00GDRqEva1bt8al4TFIGw1WrFiB55ukpKTp06fjJDHa1atXUUhw7JAhQyZMmICHAHVY7QS++uorFE7Z6e98/I2gtlNSUvD0JtrvvPNO/fr15ffWQsNg2WDZCDLzbZctPcQdQjzBsPZhYXr88cfVzrNnz2K5x1JleMl+n5sSbrRFP54DOnXqhDvloUOHYlXt27evx+N56aWXmjRpggcRlAQ5wvjx4xHWsWNH+WOmiPzP//zPNm3aREZG/su//AtWTPHQACgkWAdjY2P79++vFjnDV9mo5Ctqx545c+aJJ56Ijo6Oj4+fOnVqTEyMunfBggX33nsvDn/yySfFz+Baz7/M+9OxHTp0wDKdmJi4a9cu0YlK3KpVK9SM4cOHy+9BlVlOoMz7e92y09/5qEf5a3/33Xe4G/j888/RxiADBgwQ/SFjsGywbASZ+bbLlh7iDo6cYORPWlqaqEAqrPXWzioYOXIkSld6enrdunUPHz6s7w4yx5cNn1g2Qsl822VLD3EH90wwCrb8/PzevXv/9a9/HTdunL4v+Fg2WDaCzXzbZUsPcQf3TDByNpYNlo1gM9922dJD3ME9E4ycjWWDZSPYzLddtvQQd3DPBCNnY9lg2Qg2822XLT3EHdwzwcjZWDZYNoLNfNtlSw9xB/dMMHI2lg2WjWAz33bZ0kPcIS4uziAKf1FRUXIBjY2N1Xc7lHrVLBvBxrJh8ng8mZmZGRkZe/bsSU1NfZ8oPCF7kcPI5Mxb3JDV6lVjLuvTmwKHZcOUm5ubnZ2NW5X09HTk3xai8ITsRQ4jk7NvcUNWq1eNuaxPbwoclg1TXl4enm2zsrKQebhn2U8UnpC9yGFk8sVb3JDV6lVjLuvTmwKHZeOf+NkGOUNsbGxmZibuuLF6xjVqpO92KPWq8ahRWFioz3AKHJaNfzJc8zMn5GzIZLmA3szqDz90w3/qVbNsBJuZbLKlh7gDywY5A8sGy0awmckmW3qIO7BskDMgk+V3+V1VNvjZRsiYySZbeog7sGyQMyCT5c8Uuaps8CepQsZMNtnSQ9yBZYOcAZksf4PBVWWDv7cRMmayyZYe4g41VTYKCwtzcnL0XqqqlJQU+a+dB9X8+fPPnj27ffv2zz77TN9Xowztj4tYVlhH/qdeNX9LPNjMZJMtPcQdaqpsTJw4ES99/PhxfYcfzz77bDXXqZ9++unYsWNyc7HXkiVLVq9evXPnzry8PCXWBm3Y6qvagMatfy4U/1+xYkWpkuKiU/13ZKts6dKld9111/nz5zds2NCsWTM09Iia4/iycWnFilV/+cs3c+aonSwboWQmm2zpIe5QI2UDrxsfH1+nTp3XXntN3+eHXBarLCoqSh3BKC82NnbmzJlKeGVpw1Zf1QaU74+4nKlTp/rcWx0ej6dJkybLli0Tm506dXr99dfLh9Qkw7ll45OUlD5du9avW/fm1/HFF9Vd6lWzbASbmWyypYe4w80JFnLbtm3D6+IBomXLlsXFxfpuXypY+E6ePIknhtTU1KKiItm5ffv2lStXyqeZtWvXYoSBAwdikJ9//rlMGTA3N/fAgQN/+ctfIiIi/vrXv8oRCgoKMBvXr1+P23/ZWVZ+ZOuwZd5b+9OnT2PMt99+W2yqd/rqZmFhIR6hMIj8p7x9DujvTK5fv/7JJ5+gPzs7W14OGq1bt65du/bWrVtlpPru+TsfNL766qv33nsPb6b4cBUjf/zxx/I5bM6cOSgb+fn5YhOVCU8ecpwa5+CygYeMQQ8//OZzz7Fs1Cwz2WRLD3GHGikbgwcPTkhI2LVrl+H9QE90Gl4yxrrps2zMnj27Vq1aIjgxMVFUjpdffln0oBKIZ4i2bduKHsCCXuZrwIkTJ+IBCCsm2liyO3fuLOJjYmL27dsnYrSRrcOWeUdOTk5GQN++fcWm+kJy8/z58127dhXH1qtX76OPPirzdZ7+zuTcuXMdOnSQ/YZSNrC+33333c2bN//xxx+1F9Xa6iYauHwxYIsWLeSL9ujR48aNGwh47LHHUOnlgbt378beKnw/LUgM55YN8d+J+fNvfrFYNmqOmWyypYe4w80JFlpXrlxp2LDh9OnT8ert27fv37+/6BeLlAyzblrLBooEKtDQoUOxtm7cuBExuPtGf3R09KhRoy5fvrxkyRL5/XdtBOuAWIjRiXHQHjlyZJcuXfDQkJGRgZv3Bx98UMRYR7aOgx6s2iiKeJiwBshNvERsbCxmO04eKzKeMLQAwd+ZDBs2rGnTpgcPHsTJJCUlyaPQWLZsGZ7n8MDx0EMPiRVfHdPf+aDxy1/+EksPHoDQRk3KzMxEUUcbqxICcFGorPJAXD52/e1vf5M9Nctg2WDZCDIz2WRLD3GHmxMstJYuXYoXHTduHFarRx99NDIy8tKlS3qQhbbYSbiEtLS0lJSUAQMGIAarOTofeeSRNm3arFu3Tv0OmL/lUiooKEDnypUr0W7Xrt3zzz+/2Oupp57CA42oAdaRreOgZ8SIEeqmz9e95557xowZIzrx0tYAwd+Z4DRw1SIG5VMeJd+EyZMno/3qq6+ijRIix/R3PmjMmzcPjZKSErTnzp0r2+LzjLp1686fP18eKF703XfflT01y2DZYNkIMjPZZEsPcYebEyy07r//fqO8hQsX6kEWNyeMr7IxevRorIm4W3/hhRdkDOoQ+hs0aJCYmCi/F6+NYB3wq6++QueOHTvQxvNQuVM0jJMnT5b5Gtk6DnoWLVqkbvp83aioqNmzZ8t+SYv3dyba4fIo2cAXt0+fPthEWW3cuHFlyobPGNnGw436STuecrBr/fr1sqdmGSwbLBtBZiabbOkh7nBzgoXQt99+qy1b3bp16969uxLim3aUhAVR/DzPqVOnZIy4Hz969Ch6PsTs8vK3XAqoB6hnuLUXjxFdunRZtWqV2IU7bvnptHVk64lpPVj3Z8yYIdpYweVeXPjTTz8t+o8fP753717R1g73dyZdu3bt16+faB88eFAepR6OReQeL1yX7PR3PuqBPts4YdRm0Qnit+q++OIL2VOzDJYNlo0gM5NNtvQQd7g5wUJo7NixeDiQax/MnDnT8H6yanjJfuum+PkiYcOGDaI/ISHhvvvue+utt9CIiIiYMmXK7t27mzVrNmbMmFGjRuGoTz/9VETi9rxXr16TJk2S3+4XA+JY8TkByN+YW7FiBR4pkpKSpk+f/sADD7Ro0eLq1as+R9aGFSOr637Pnj1xOFZqHIhguXfNmjVoDxo0CLtat26N8xcVSxvQ55mgH7UEhw8ZMmTChAk4czms9up4hKpXr57a6e981Bif7ZSUlPbt24tOeOedd+rXr69+e61mGSwbLBtBZiabbOkh7nBzgoUKlkUsWI8//rjaefbsWSz3WMIML9nvc1PCPbjox0LfqVMn3EEPHToUq23fvn09Hs9LL73UpEkTPIgkJyfLEcaPH4+wjh07ip83lUMhsnPnznhkycrKksFl3h9I7dChA1bGxMTEXbt2lXl/ccE6sjZsmWXhPnPmzBNPPBEdHR0fHz916tSYmBi5d8GCBffeey8Of/LJJ+XP4FoHtJ6JgIrbqlUr1Izhw4fLb0Npr17m/b1utdPf+agxPtvfffcdSv7nn38u+jHIgAEDRPtOYLBssGwEmZlssqWHuMPNCUYOkpaWJiuQhLXe2lkFI0eOROlC+T969GjdunUPHz6sR9Qcx5cNn/+xbISSmWyypYe4A8sGVV5+fn7v3r2PHDmC549x48bpu2sUywbLRrCZySZbeog7sGyQM7BssGwEm5lssqWHuAPLBjkDywbLRrCZySZbeog7sGyQM7BssGwEm5lssqWHuAPLBjkDywbLRrCZySZbeog7sGyQM7BssGwEm5lssqWHuAPLBjkDywbLRrCZySZbeog7sGyQM7BssGwEm5lssqWHuENcXJxBFP6ioqLkAhobG6vvdij1qlk2go1lw+TxeDIzMzMyMvbs2ZOamvo+UXhC9iKHkcmZt7ghq9WrxlzWpzcFDsuGKTc3Nzs7G7cq6enpyL8tROEJ2YscRiZn3+KGrFavGnNZn94UOCwbpry8PDzbZmVlIfNwz7KfKDwhe5HDyOSLt7ghq9WrxlzWpzcFDsuGqbCwEDcpyDncreA59wRReEL2IoeRybm3uCGr1avGXNanNwUOy4apuLgY2Yb7FKSdx+ORd2pE4QXZixxGJhfe4oasVq8ac1mf3hQ4LBtERGQDywYREdnAskFERDawbBARkQ0sG0REZAPLBhER2cCyQURENrBsEBGRDSwbRERkA8sGERHZwLJBREQ2sGwQEZENLBtERGQDywYREdnAskFERDawbBARkQ0sG0REZAPLBhER2cCyQURENrBsEBGRDSwbRERkA8sGERHZwLJBREQ2sGwQEZENLBtERGQDywYREdngo2wQERHdFssGERHZwLJBREQ2/D/ufLX/rhjd6wAAAABJRU5ErkJggg==" /></p>


また、以下に見るようにstd::unique_ptrはcopy生成やcopy代入を許可しない。

```cpp
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 123

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
    //  example/term_explanation/unique_ptr_ownership_ut.cpp 161

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

#### オブジェクトの共有所有 <a id="SS_19_5_7_2"></a>
オブジェクトの共有所有や、それを容易に実現するための
[std::shared_ptr](https://cpprefjp.github.io/reference/memory/shared_ptr.html)
の仕様をを説明するために、下記のようにクラスA、Xを定義する。

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 7

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
std::shared_ptr、std::move()、[rvalue](term_explanation.md#SS_19_14_3)の関係を解説する。

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 47

    // ステップ0
    // まだ、クラスAオブジェクトは生成されていないため、
    // A::LastConstructedNum()、A::LastDestructedNum()は初期値である-1である。
    ASSERT_EQ(-1, A::LastConstructedNum());     // まだ、A::A()は呼ばれてない
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 56

    // ステップ1
    // a0、a1がそれぞれ初期化される。
    auto a0 = std::make_shared<A>(0);           // a0はA{0}を所有
    auto a1 = std::make_shared<A>(1);           // a1はA{1}を所有
    ASSERT_EQ(1, a0.use_count());               // A{0}の共有所有カウント数は1
    ASSERT_EQ(1, a1.use_count());               // A{1}の共有所有カウント数は1

    ASSERT_EQ(1,  A::LastConstructedNum());     // A{1}は生成された
    ASSERT_EQ(-1, A::LastDestructedNum());      // まだ、A::~A()は呼ばれてない
```

<!-- pu:deep/plant_uml/shared_ownership_1.pu--><p><img src="data:image/png;base64,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" /></p>


```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 68

    // ステップ2
    // x0が生成され、オブジェクトA{0}がa0とx0に共同所有される。
    ASSERT_EQ(0, a0->GetNum());                 // a0はA{0}を所有
    ASSERT_EQ(1, a0.use_count());               // A{0}の共有所有カウントは1
    auto x0 = X{a0};                            // x0の生成と、a0とx0によるA{0}の共有所有
    ASSERT_EQ(2, a0.use_count());               // A{0}の共有所有カウント数は2
    ASSERT_EQ(2, x0.UseCount());
    ASSERT_EQ(x0.GetA(), a0.get());
```

<!-- pu:deep/plant_uml/shared_ownership_2.pu--><p><img src="data:image/png;base64,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DrEHh+mFfuuttyolu2DBAnWQD9/CFUaPHo1swu512LBhcgzeD9DfoEGD5ORk+V2tMoPvhF988QU6//GPf6CNzwdXnKLDkZOTU+FvZt950LNw4ULjXb/PGxcXN2vWLNkvKeMDnYnycPko2cAfbt++fXEXb29NmjQJJr79jpFtbPaNfyOKXT8OrVq1SvZElkOf+A4N41vyLl+21CH2YHKhf/3110oJ3nLLLd27dzcM8c+3cAUEk/j5h6NHj8oxYn+6b98+9KxevVqMDBRbAnIZ7yvY6optddeuXVesWCEOYQcq/xbRd2bfE1N6kL+vvvqqaCNJ5VEs/MEHHxT9Bw8e3LFjh2grDw90Jt26dXvggQdEe/fu3fJRxofjYr7eA+uSnYHOx/hAv22cMN4jRSeIfx2zfft22RNZDsY349tuTC705557DptlmUEwY8YMh+dvwBwest/3rvh5DGHNmjWiv1OnTp07d37ttdfQqFWr1rRp07Zt29a8efPx48ePHDkSj/roo4/ESGxXe/fu/dJLL8mvg8WEeKz4Hhnkv3xZtmwZtthjxoxJTU3t2bNnixYtfvzxR78zK9OKmY3X2F133YWHIzHxQAyWR99++220Bw4ciEOtW7fG+Yt3DmVCv2dS4flpBDx88ODBkydPxpnLaZVnx0eKevXqGTsDnY9xjN92SkpKu3btRCe88cYb9evXN37tE1kOxjfj227MLHTEE4LjnnvuMXYeP34csYsocXjIfr93JexJRT8Ct2PHjthRDhkyBKnXr18/l8v19NNPN23aFBvzsWPHyhkmTZqEYTfddJP4OTk5FUZ26dIFW/jc3Fw5uMLzg3QdOnRAQiUnJ2/durXC84PPvjMr01b4BOi333577733NmrUKCkpafr06fHx8fLo/Pnz27dvj4ffd9998mcHfSf0PRMB73ytWrVCdg8dOlR+PaI8e4Xn30kaOwOdj3GM3/ahQ4fw1vvJJ5+IfkwyYMAA0Y4GDsY349tuLFnodrZhwwb5TiAhc307QzBixAi8heBteN++fXXr1t27d686InIsH99+Mb4vUYfYg30KncJXXFzcp0+fr776CnvAiRMnqocjivHN+LYd+xQ6WRvjm/FtO/YpdLI2xjfj23bsU+hkbYxvxrft2KfQydoY34xv27FPoZO1Mb4Z37Zjn0Ina2N8M75txz6FTtbG+GZ8205iYqKDSH9xcXEyyBISEtTDFmVcNePbjlwul9PpzM7OzszMzMjIWEmkJ+P/c12wQ1Xz/zRv6/guLCzMy8vDW3dWVhbqYCORnlC9qGFUct5ldqhq46pxLauXtxUxvr2KiorwmSs3NxcVgPfwXUR6QvWihlHJ+ZfZoaqNq8a1rF7eVsT49nK73XjTxp893r3x+esIkZ5QvahhVHLhZXaoauOqcS2rl7cVMb69SktL8aeO92388btcLrlzIdILqhc1jEp2X2aHqjauGteyenlbEeObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi0xvomItMT4JiLSEuObiEhLjG8iIi35iW8iItII45uISEuMbyIiLf1/efGDsCzmC2kAAAAASUVORK5CYII=" /></p>

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 79

    // ステップ３
    // x1が生成され、オブジェクトA{0}の所有がa0からx1へ移動する。
    auto x1 = X{std::move(a0)};                 // x1の生成と、a0からx1へA{0}の所有権の移動
    ASSERT_EQ(x1.GetA(), x1.GetA());            // x0、x1がA{0}を共有所有
    ASSERT_EQ(2, x0.UseCount());                // A{0}の共有所有カウント数は2
    ASSERT_EQ(2, x1.UseCount());
    ASSERT_FALSE(a0);                           // a0は何も所有していない
```

<!-- pu:deep/plant_uml/shared_ownership_3.pu--><p><img src="data:image/png;base64,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" /></p>

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 89

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

<!-- pu:deep/plant_uml/shared_ownership_4.pu--><p><img src="data:image/png;base64,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" /></p>

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 110

    // ステップ５
    // 現時点でx1はA{1}オブジェクトを保持している。
    // x1::Moveに空のstd::shared_ptrを渡すことにより、A{1}を解放する。
    x1.Move(std::shared_ptr<A>{});              // x1に空のstd::shared_ptr<A>を代入することで、
                                                // A{1}を解放
    ASSERT_EQ(nullptr, x1.GetA());              // x1は何も保持していない
    ASSERT_EQ(1, A::LastDestructedNum());       // A{1}が解放された
```

<!-- pu:deep/plant_uml/shared_ownership_5.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnYAAAGkCAIAAAAzKP8XAABHoElEQVR4Xu3deXQUVd4+8GZNSFgCkTUgBH1x4PWQgR8YhZkRcUEjuL4oA4wsIslxQECjnDMIsggEFFF2UFkkiCzjxhAWBWQRFFAjAZTV6RgJCAkNgWxk+T30ldvF7e5Q6U53uqqfz8kft27dqu5Kf+s+fbNaSomIiMgHLGoHERERVQRGLBERkU84IraEiIiIvMaIJSIi8glGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYj1x8uTJzp07jxkzRt1BRER0jUkiNj8//2ONtWvX7tmzR+7NyMh4zcnRo0c1JyjLuXPnDh8+fPDgwbS0tAMHDqSmpuLwBx98MCoqCnv3798vH3ffvn3qwUREFKxMErFIwXr16kVERDRs2LB58+Z16tRp1qxZcXGx2Is0fdgJovH6c1yFqFa7SkqmTJlicVK3bt2UlBTs7dmzp+zs16+fejAREQUrk0Ss1pUrV2655ZbXX39d9hx248KFC3LMN998s3fvXsQz0hqbTz/99PTp08Wu7OzsEydOWK1WrIYzMzPPnj3717/+NT4+XuyNiYlZt26dPA8REZFgwohduHBheHi4SEooLCzULD6v8+GHH4oxx44dq1Gjxscff9yqVavExET0tGzZMikpSZ5TKycnJywsLDk5WWw2aNBg06ZN69ev//HHH68fSEREQc1sEfvDDz8g/0RMSqeumTRpUpMmTeRmbm6uHPPCCy/8+c9/fv/995955hmsbqtUqfL5559rzuEwZ86c2rVrixXw5cuXtZn9+OOPYw2tHkBEREHJVBG7f//+Zs2aRUdHYxW7YcMGdXdJyciRIzt16qT22v3yyy9z584VATl16tSaNWtmZWWpg0pKDh48GBER8dprr8keDLt06VJBQcHmzZuRsjt27NAMJyKi4GWSiC0qKlq0aBHWrw8++CBWllit1qhRQ0nZ77//PjIyEru0nYq8vDzka9WqVcePH6/sQo7OnDmzXr16cXFxhYWFovP06dP/+Mc/3nrrrY8++ighIaFatWrHjh27/jgiIgpSZojY7Ozsjh07Vq9efdy4cfLrtImJiVjL7t27t8Sejo8++iiC85FHHkEAX3ewxksvvdSwYcNatWpNnjxZ249AHTBgAMK1Tp06SGiZr8L06dOxbg4JCWnbtu2qVau0u4iIKJiZIWJh9uzZhw4d0vYUFxcjcU+dOiU2scbdvHmzdoCz5OTkt99++8yZM+qOkpI333wTZ7DZbOoOIiIiN0wSsURERIGGEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHzCVBEbGRmp/b83RDqhctRi0o1VR57xpurIKEwVsahaeRVE+qFybDZbTk5Obm5uQUFBUVGRWlvuserIM95UHRmF4+WWLXWIcXCyI8+gcqxWa2ZmZlZWFqY8zHdqbbnHqiPPeFN1ZBSOl1u21CHGwcmOPIPKSUtLO3bsWEZGBuY7rCrU2nKPVUee8abqyCgcL7dsqUOMg5MdeQaVs2vXrtTUVMx3WFVgSaHWlnusOvKMN1VHRuF4uWVLHWIcnOzIM6iclJQUzHdYVVit1nL910JWHXnGm6ojo3C83LKlDjEOTnbkGVTOypUrN27cuHfvXiwpsrKy1Npyj1VHnvGm6sgoHC+3bKlDjIOTHXnGm8mOVUee8abqyCgcL7dsqUOMI3Amu9GjR3/zzTdqrz7eHKuTHx5Cp4KCgjNnzqi9fufNZMeq08kPD6GTCaqOjMLxcsuWOsQ4/DbZnT59+uDBg2qvBp7J/Pnz1V59vDlWJ48f4oYXXl4TJkzAkzl8+LC6w7+8mexYdTp5/BA3vPDyMkHVkVE4Xm7ZUocYh98mu/Dw8LInC49nk1LvjtXJ44e44YW7891336ld9kqLjo6uXr36K6+8ouw6cuRITk6O0uk73kx2rDqdPH6IG164OyauOjIKx8stW+oQ4/DdZLdt27alS5eKt73Jycl4oL59++K2//333+WYy5cvr1u3btWqVZmZmfpnE+2ZBXHs999/v3z58pSUlMLCQrnr+PHjH3zwgbYTI0+ePLlv377Zs2fLYfn5+bhv8Uzw9l92luvpYe/Ro0e3bt26YsWKEydOiE6XF+7yCWjt3Lnz7rvvvuWWW9QdpaU4P0745JNPNmvWrKioSLtr5syZN91005tvvpmbm6vt9xFvJjtWncCqKy9vqo6MwvFyy5Y6xDh8NNkNHz7cYlelSpXp06e3bNlSbAJucjHm1KlTbdq0EZ1169a1XJtNRI88lbKpnFmOwdQg+qFz585XrlxB/4wZM6pWrSo6Y2NjxXyH9qhRo3B4z549xeGYhtq3by+G4Zns2bOn1P3TcwcDoqKixPiaNWt++OGH6HR54RanJyBhTI8ePTDgoYce2r9/v7IX+vfv365dux07dljsv72g3XXhwoXx48fXq1evadOmc+bMKSgo0O6tcBYvJjsLq45V5xGLF1VHRuF4uWVLHWIcFt9MdrVr1x42bNj58+cXLFhw9uzZUvu9oUwWgwYNatCgAW5pDBsxYoQcIKYGOUzZdD6zGFOnTp1PP/0Ub6WxpMDmpk2bMLVhahg4cCDmsrVr16ITiwMxGNMB5gs5HSQkJMTExOA9flpaWvPmzbt27Vrq/um5gwF4O799+3abzfbcc89FRETg/hf9yoHOT6DUvu557LHHsKt79+5ff/21ZrgDprOwsLCkpCS8cK1bt+7du7c6orQ0Ozv7X//6Fz5LmGexkFJ3VxyLF5Od9gWtQM614fzJd/ey2quMVeeCaaqOjMLxcsuWOsQ4tPNIBerWrVuLFi3wnlp+Wcn5nseA0aNHizYmJucBLjmfudR+8kmTJok2VhLYXLRoUan9ddmwYQMepU+fPujE/CgGx8fHy2OhVatWzz777Hy7hx9+GEsQTEPlfXoYgGlItH/99VdsYiIQ/c6TnfIESu1f3MMKo23btt9//72yS1q4cCGOHTt2LE54zz33hISEYGpTB5WWXrx4EesVjLzrrrvUfRXHm8mOVVfKqvOIN1VHRuF4uWVLHWIcPprscBO+8MILtWrVio2NzcvLK3V1z4eHh8+YMUNuOg9wyfnMpU7Hyk2MrFat2r333jtkyBDZica8efPkYMCbdMv18O6+vE9PO+DSpUvYxMpG6ZcjlScgYJrDVIsp79FHH3X5Uyd33nnndc/SYpk7d652AKa5yZMnYxmEVREeVPvdwQpn8WKys7DqWHUesXhRdWQUjpdbttQhxmHxzWQnvhh14MABnH/16tWlru75Dh069OrVS7T379/vPMAl5zOXOp1cbtarV2/MmDFonDhxQnY6P1BMTMyyZctEu7i4WPyESHmfHgaMHDlStFNSUrApfqPR+UDnHq09e/Z0794dYwYMGKDt/+mnn5QDO3bs2KlTJ7m5efNmTHONGzeeOXNmfn6+7PcRixeTnYVVx6rziMWLqiOjcLzcsqUOMQ6LDya7nTt3NmzYMDExcdiwYRb7N6hK7auHHj16TJw4UfxICGB+Ebf0+PHjcZdqJyPts9JuujyzGONysmvXrt3tt9/+xhtvoIH36Xiv7TwYlixZggXKiBEjkpKSunTp0qRJE7wxd/f03LHYfxZm6NChU6dOxRnuuOOOEnutOF/4DU9Vav/51WeeeUbb8/LLL2NtpP3J2OnTp+NU8tcf8YSnTJmCpYwc4FMWLyY77etbUVzWhvMn393LerXIWHWmrjoyCsfLLVvqEOPQTisVxWaz4Z6vX78+3s6PGjVKdI4bNy4sLOy22247dOiQHInbNSoqClPJ4MGDMfiGk53LM4sxLic7vKNv27YtHnfgwIGYccTPUrqca9DTpk2b0NDQ2NjYHTt2iE6XT88dnBYPER0dXbt27bi4uF9//VX0O1+4yydQtqKiIkyg9913n7YzPT0d0yumfm2n33gz2bHqBFZdeXlTdWQUjpdbttQhxuGLyc7c5jsRX+7zYAozNG8mO1Zdeak1x6orf9WRUThebtlShxgHJ7vysi9vrtO4cWPRz8lOJwurrpyUkrOw6spfdWQUjpdbttQhxmHhZFdB4uPj5df6goE3kx2rrqKw6tTaIuNzvNyypQ4xDk525BlvJjtWHXnGm6ojo3C83LKlDjEOTnZ6HDp0KDk5ed26dfJ3IsmbyY5Vp0d2dvayZcu0P6hF3lQdGYXj5ZYtdYhxcLIrGz5FCQkJlmuio6NxY6uDgpI3kx2rrmx4MxcXFxcaGmoJsm+13pA3VUdG4Xi5ZUsdYhyc7LSc/0HKu+++i0/RtGnTsKTYvXt3y5Yt//a3v11/UJDyZrJj1Wk5Vx0Wr/369Zs0aRIjVuFN1ZFROF5u2VKHGAcnO8nlP0jp0qVLt27d5Jg1a9Zg788//+w4LFh5M9mx6iSXVSfgs8qIVXhTdWQUjpdbttQhxsHJTnD3D1Lq1q07fvx4OezMmTPY9cknnziODFbeTHasOsFd1QmMWGfeVB0ZhePlli11iHFwspNKXP2DlJCQkLfffluOyc/Px66lS5c6DgtW3kx2rDqpxFXVCYxYZ95UHRmF4+WWLXWIcXCyk1z+g5To6OgXX3xRjjl69Ch2bd682XFYsPJmsmPVSS6rTmDEOvOm6sgoHC+3bKlDjIOTneTyH6QMHjw4KipK/pXzV199NSwszGazaQ8MTt5Mdqw6yWXVCYxYZ95UHRmF4+WWLXWIcXCyk1z+g5S0tLTQ0NCYmJikpKSEhISqVatW1h9ADzTeTHasOsll1QmMWGfeVB0ZhePlli11iHFwspNc/oOUUvt/+OrcuXNISEizZs2wipX/HSzIeTPZseokd1VXyoh1xZuqI6NwvNyypQ4xDk525BlvJjtWHXnGm6ojo3C83LKlDjEOTnbkGW8mO1YdecabqiOjcLzcsqUOMQ5OduQZbyY7Vh15xpuqI6NwvNyypQ4xDk525BlvJjtWHXnGm6ojo3C83LKlDjEOTnbkGW8mO1YdecabqiOjcLzcsqUOMQ5OduQZbyY7Vh15xpuqI6NwvNyypQ4xDk525BlvJjtWHXnGm6ojo3C83LKlDjEOTnbkGW8mO1YdecabqiOjcLzcsqUOMQ5OduQZbyY7Vh15xpuqI6NwvNyypQ4xjsjISAtR+YWHh3s82bHqyDPeVB0ZhakiFmw2m9VqTUtL27VrV0pKysogZrG/RyadUC2oGVQO6gdVpBZWmVh1EquuXLypOjIEs0VsTk5OZmYm3hKmpqaidjcGMUx2ahe5h2pBzaByUD+oIrWwysSqk1h15eJN1ZEhmC1ic3Nzs7KyMjIyULV4b7g3iGGyU7vIPVQLagaVg/pBFamFVSZWncSqKxdvqo4MwWwRW1BQgDeDqFe8K7RarceCGCY7tYvcQ7WgZlA5qB9UkVpYZWLVSay6cvGm6sgQzBaxRUVFqFS8H0TJ2my2rCCGyU7tIvdQLagZVA7qB1WkFlaZWHUSq65cvKk6MgSzRSxJmOzULiIfY9URaTFiTYuTHfkfq45IixFrWpzsyP9YdURajFjT4mRH/seqI9JixJoWJzvyP1YdkRYj1rQ42ZH/seqItBixpsXJjvyPVUekxYg1LU525H+sOiItRqxpcbIj/2PVEWkxYk2Lkx35H6uOSIsRa1qc7Mj/WHVEWoxY0+JkR/7HqiPSYsSaFic78j9WHZEWI9a0ONmR/7HqiLQYsabFyY78j1VHpMWINY/27dtb3MAudTRRRWDVEZWBEWseSUlJ6iR3DXapo4kqAquOqAyMWPOwWq1Vq1ZV5zmLBZ3YpY4mqgisOqIyMGJNpVu3bupUZ7GgUx1HVHFYdUTuMGJNZdGiRepUZ7GgUx1HVHFYdUTuMGJNJTs7OyQkRDvTYROd6jiiisOqI3KHEWs2TzzxhHayw6Y6gqiiseqIXGLEms3atWu1kx021RFEFY1VR+QSI9Zs8vLy6tevL2Y6NLCpjiCqaKw6IpcYsSY0ZMgQMdmhoe4j8g1WHZEzRqwJbd26VUx2aKj7iHyDVUfkjBFrQsXFxS3s0FD3EfkGq47IGSPWnEbbqb1EvsSqI1IwYs3pRzu1l8iXWHVECkYsERGRTzBiSZfCwkL5PTZtm8h3WHVkdIxY0sViscybN8+5XYbMzMy0tDS1l0g3Vh0ZHSOWdPFgsgsPD9czjMgdVh0ZHSM2GGEOOnbs2HfffffBBx+sX7++oKBA9h88eFA7TG6WMdmhfeTIkS1btiQnJx8/flx0Ll++HMP69u2LvWfOnBHDTpw4sXfv3lmzZsljKXiw6igIMWKDEaahdu3aWa7p3LlzYWGh6NfOYu4mOOdhUVFR4lQ1a9ZcsWIFOlu2bCnPjwlODBs1alSVKlV69uwpj6XgYWHVUfBhxAYjzDt16tT59NNPL1++jCUFNjdu3Cj6PZvsbrrppq+++ur8+fPPPfdcRETEuXPnXA5r2rTp9u3b8/PzZScFD1YdBSFGbDDCvDNx4kTRxkoCmwsXLhT9nk12U6dOFe309HRsbtiwweWw+Ph4uUnBhlVHQYgRG4ycpyGx6a6/jLaymZOTg02sUVwOmzt3rtykYONcD6w6Mj1GbDBynobEZlhYWFJSkuhMSUlxN8E5Hz5y5EjRXr9+PTb37Nnjcph2k4KNu3pg1ZGJMWKDkbtpqHv37k2aNMF8l5iYGB4e7m6Ccz68SpUqQ4cOnTJlCg6/4447xJ8IwBl69OgxYcIElz/VQsHGuWxYdWR6jNhg5Dxbic2TJ08+8MADtWvXjo6Onjx5ct26dV1OcM6HY1LDITgwLi4uPT1d9I8bNw4LlNtuu038DgYnuyDnXDasOjI9Rix5i7MY+R+rjgyBEUve4mRH/seqI0NgxJK34uPjt2/frvYS+RKrjgyBEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glTRWxkZKTFXHBF6kVSgGHVEZE7popYzA7yKswBV2Sz2XJycnJzcwsKCoqKitRrpsrGqiMidxy3lWypQ4zDlJOd1WrNzMzMysrClIf5Tr1mqmysOiJyx3FbyZY6xDhMOdmlpaUdO3YsIyMD8x1WFeo1U2Vj1RGRO47bSrbUIcZhyslu165dqampmO+wqsCSQr1mqmysOiJyx3FbyZY6xDhMOdmlpKRgvsOqwmq12mw29ZqpsrHqiMgdx20lW+oQ4zDlZLdy5cqNGzfu3bsXS4qsrCz1mqmyseqIyB3HbSVb6hDj4GRH/seqIyJ3HLeVbKlDjIOTHfkfq46I3HHcVrKlDjEOP092hw4dSk5OXrduXV5enrqvgnCyC3x+rrrs7Oxly5ah9tQdFYdVR1RRHLeVbKlDjMNvkx0eKyEhwXJNdHQ0ZiJ1UEXgZBf4/FZ1eDMXFxcXGhqKR5w/f766u+Kw6ogqiuO2ki11iHH4YrJbvXr14sWLS+yfqYsXL2Jq+/rrr99991081rRp07Ck2L17d8uWLf/2t7+pR1YETnaBz29Vh8Vrv379Jk2axIglMgrHbSVb6hDj8MVkt2LFCpwWmYr28OHDw8PDjx8/3qVLl27duskxa9aswZiff/7ZcVgF4WQX+PxWdWIXyoARS2QUjttKttQhxuGLyQ4ee+yxBg0a/Oc//6laters2bPRU7du3fHjx8sBZ86cwUN/8sknjmMqCCe7wOe3qhMYsUQG4ritZEsdYhw+muxOnz4dGRmJme7uu+8usX/KQkJC3n77bTkgPz8fD7106VLHMRWEk13g81vVCYxYIgNx3FaypQ4xDh9NdnD//ffj5JMnTxab0dHRL774otx79OhR7N28ebPsqSic7AKf36pOYMQSGYjjtpItdYhx+Giyw/IUZ+7atWutWrWQpugZPHhwVFTUpUuXxIBXX301LCzMZrNdd1hF4GQX+PxWdQIjlshAHLeVbKlDjMMXk116enq9evX+/ve/X7hwoVmzZpjyiouL09LSQkNDY2JikpKSEhISqlatmpiYqB5ZETjZBT6/VZ3YxYglMhDHbSVb6hDjqPDJDue87777IiIiTp8+jc2PP/4YDzFjxgy0t23b1rlz55CQEMyAWMVeuXJFPbgicLILfP6sulJGLJGhOG4r2VKHGEeFT3aVjpNd4GPVEZE7jttKttQhxsHJjvyPVUdE7jhuK9lShxgHJzvyP1YdEbnjuK1kSx1iHJzsyP9YdUTkjuO2ki11iHFwsiP/Y9URkTuO20q21CHGwcmO/I9VR0TuOG4r2VKHGAcnO/I/Vh0RueO4rWRLHWIcnOzI/1h1ROSO47aSLXWIcXCyI/9j1RGRO47bSrbUIcYRGRlpMZfw8HBOdgGOVUdE7pgqYsFms1mt1rS0tF27dqWkpKysIBb7+/pKgavAteCKcF24OvWCKQCw6ojIJbNFbE5OTmZmJt56p6amYo7YWEEw2ald/oKrwLXginBduDr1gikAsOqIyCWzRWxubm5WVlZGRgZmB7wH31tBMNmpXf6Cq8C14IpwXbg69YIpALDqiMgls0VsQUEB3nRjXsC7b6vVeqyCYLJTu/wFV4FrwRXhunB16gVTAGDVEZFLZovYoqIizAh4342pwWazZVUQTHZql7/gKnAtuCJcF65OvWAKAKw6InLJbBHrI5js1C4iH2PVERkdI1YXTnbkf6w6IqNjxOrCyY78j1VHZHSMWF042ZH/seqIjI4RqwsnO/I/Vh2R0TFideFkR/7HqiMyOkasLpzsyP9YdURGx4jVhZMd+R+rjsjoGLG6cLIj/2PVERkdI1YXTnbkf6w6IqNjxOrCyY78j1VHZHSMWF042ZH/seqIjI4RqwsnO/I/Vh2R0TFideFkR/7HqiMyOkasLpzsyP9YdURGx4jVhZMd+R+rjsjoGLG6cLIj/2PV+cI777xjtVrVXh1Gjx69Z88etVcfb47Vzz+PckP5+fmnT59We8ujqKjo3Llzly9flj1bt27dtGmTZohhMGJ14WRH/meaqsvKylq6dOnBgwfVHXbz5s1buHBhcXGxtnPHjh3od3eIxxYsWNCoUaPff/9d3WGXmZmZlpam9l6DlwNPSe3Vx5tj9fP4Ucq+8PIaP348nsmhQ4fUHfq8+eabISEht956a7Vq1e66666LFy+ic/Xq1Q0bNnT3wgUyRqwuppnsyEBMUHWff/55XFxcaGhoGbO/xW7z5s2yB3GLGbaMQzxz/vz5+vXrI87VHdeEh4eX8YjePB9vjtXP40cp+8LLsH//fqUHr110dHT16tVfeeUVZdfPP/8s8rJsERERWI6jcfLkSVzRypUrRX/btm3HjBlz3VAjYMTqYoLJjgzHWFW3atWq999/XyxGL1y4gCl7165dWLz269dv4sSJZcz+2FW3bt3/+7//kz2IW6xgmjRpohySn5//xRdffPTRRxkZGaJn0aJFKSkpcsCyZcv+85//oJGXl7dhwwaMxPpM7p0xYwYiNjc3V2xu3bp1yZIlcrG1fPlyPJO+ffviQc+cOSM6L126hHcJOM+pU6fKuASFcuaSa+H33XffffDBB+vXry8oKJC7jh07hqetdGLwiRMn9u7dO2vWLNHj8opKyvMMsevIkSNbtmxJTk4+fvy47He+cOdHd7Zjx4677777lltuUfpxfpztySefbNas2ZUrV7S73nrrrZtuuumNN97QfgXYmfYqtO3Jkyc3atTIMc4gGLG6GGuyI3MwVtVh4sYTRuahPXz4cCyMEB5i19GjR8uY/bHrnnvuqVGjhgyP3r17d+vWDXO09pCzZ8926tTJYoeT//vf/0bnI488EhkZKcJJPArmceRE+/btxUiE9+7du8UZ7r33Xkz9oo1nKAZUqVJl2rRp6GnZsqXoAaQLen777bc2bdrI81iuXYLoEedx3nQ+sxiDNBL90Llz58LCwhL7F0WrVq0qOmNjY2XKYnPUqFE4Q8+ePbHp7orcPUOXsDcqKkoMrlmz5ooVK0S/84Vbrn90Bcb06NEDYx566KF9+/Ype/v379+uXbvt27djAN43aHfZbLbXXnutXr16TZs2nT17Nt4wafdK2qvQthHq2KzAL2j7ByNWF4uhJjsyB8NV3WOPPdagQYN169YhNrQLoBtGLKIIEYtlCjZPnz6NAHjnnXdq1aqlPeT5559HimBljKzt1asXkvX8+fOfffYZDhcrV6yVQ0JCsDchISEmJgbrsAMHDjRv3rxr167iDJjZx48fL9q1a9ceNmxYdnb2/Pnz5Xf4lCc5aNAgXA5SBMNGjBgh99rDyG3EujtznTp1PvnkEyzgsJDF5saNGxGoCKSBAwciQdesWYNOrEfleDxbBJXIIXdX5O4ZuoS9WER+9dVX+Lw999xzERER586dk7u0ByqPLuE9E15i7O3evTteCO0uASEaFhY2derU4uLi1q1b462SOsL+jfl//etf+Cwh2rF8V/ZiUY7zL126VGyiBvAuRLTxycSujz/+2DHaCBixumhvISL/MFzVYRmK5EO+3n333dofX7phxCKNsL6Mjo7GUZigEbFiPtUecvPNNycmJoq2OOGGDRuuXLmClVm/fv3Q+b//+799+vRBo1WrVs8+++w8u4cffhjPR0QFUhzJLc6AVXKLFi2wktN+MVN5RAwQ3xQExGEZl6Dl7sx4ByDaWL9iU3xLGNebkpKCR8EzF58HOT4+Pl4e7u6KyvUMsRefW9FOT08Xn0C5S4lY7aNLy5cvx9K2bdu23333nbrPbsGCBTh27NixONs999yDdzwIVHWQ/fsIWCVj5F133aXswuMi+3/55RexiVcWr++vv/5acu0C33vvvesOCHiMWF0sRpvsyASMWHX3338/nvbrr7+u7bxhxGLXpk2b0NixY8ef/vSnv//977JfDgsPD5cLmpycHOzFchDtMWPGYEn07bffoueLL75ADxZSluuJL1ljwScWyiX2tdQLL7yARVJsbKz87mwZj+i81x09Z5abGFmtWrV77713yJAh2jFoz507V453d0XleobavdpPoLJLbGofXQvhioxH0D766KPOP+t05513XvcsLZY5c+ZoByBcURt4IbAWxyNqv/0sTJgwAe+EfvzxR7GJnG7fvv3Zs2fRxkodJ/zoo4+uOyDgMWJ1sRhwsiOjM1zVLVmyBM+5a9euCJgjR47Ifj0RK7602LdvX2xu27ZN9sthf/7znx9//HHRXr9+PfaK3wE9ceIEZvzOnTvjcLF0jomJkV9pLCoqkj+71LFjRySZaItVIKZynGfVqlWiU3nEDh069OrVS7T37dtXxiVo6Tmz3KxXr574Kdnjx49rxyjj3V1RuZ4h9o4cOVK0tZ9Ascvl03Nn9+7d3bt3x7ABAwbIzsOHDysH4hPeqVMnuYl3UQjXxo0bv/XWW3l5ebJfS1mqar/wcODAAexy+QXqQMaI1cVitMmOTMBYVWe1WhEYWIDabLZmzZohaBEGYpfLiJ137dde5a4pU6ZgSXfbbbeJAcoh77//PnoGDRqEZVCjRo26dOkivxZ93333WTRL58WLFyPjR4wYMXXqVAxr0qQJFk8l9r/MgBgusf/gTMOGDRMTE4cNG2axf1tUHIhFYY8ePbCQEj+LhFQTKfLaa68hG+TzsdiJQ5RNd2dWrkVutmvX7vbbb58+fToaeKMgL0EZ7+6K3D1Dlyz2n8AaOnQoPs84wx133CE/gcqFl30eaevWrc8884zcfPnll/HyyfiHadOmWTQ/oIRnO3nyZCyg5QCXtI+ubb/77ruhoaHusjlgMWJ1kbcQkd8YqOowWSPnIiIixE8F//vf/8aTl1/DdBmxskc2cCzmUCxxlAHSzJkzkZF4lN69e2un8o8++giTu/xNnhJ7frdp0wZni42N3b59u+j86aefMOyLL744f/48kqZ+/fp4TzBq1Ch51Lhx48LCwpDx8k9eICSioqKQXoMHD8bgG0asuzMr1yI3sY5s27YtHnTgwIEIOfkTvM7X7vKKStw8Q5dwTjxEdHR07dq14+Li0tPT5S7lwp0f/YauXLmC2EYNaDvxrguhLr+DrpP20bXtBx54QHyv3VgYsbpo7ygi/wiSqktJSXH5Fw3d9XsjISEBEaX8vqbJzHMivsjsQXBWCrxdGD58+KVLl1JTU/GcV69eXWL/wnuNGjW+//57dXTAY8TqEiSTHQUUVl2Fy83NffDBBzF3qztMxL6ovk7jxo1FvyEidv78+REREa1atapevfr9998vfmQMz3zs2LHqUCNgxOpi4WRHfseqowoUHx+v/QpzgCssLFT+bLVBMWJ14WRH/seqIzI6RqwunOzI/1h1REbHiNWFkx35H6uOyOgYsbpwsiP/Y9URGR0jVhdOduR/rDoio2PE6sLJjvyPVUdkdIxYXTjZkf+x6oiMjhGrCyc78j9WHZHRMWJ14WRH/seqIzI6RqwunOzI/1h1REbHiNWFkx35H6uOyOgYsbpwsiP/Y9URGR0jVhdOduR/rDoio2PE6sLJjvygffv2FjewSx1NRAGPEauLhRFLvpeUlKRG6zXYpY4mooDHiNXFwogl37NarVWrVlXT1WJBJ3apo4ko4DFidbEwYskvunXrpgasxYJOdRwRGQEjVhcLI5b8YtGiRWrAWizoVMcRkREwYnWxMGLJL7Kzs0NCQrT5ik10quOIyAgYsbowYslvnnjiCW3EYlMdQUQGwYjVhRFLfrN27VptxGJTHUFEBsGI1YURS36Tl5dXv359ka9oYFMdQUQGwYjVhRFL/jRkyBARsWio+4jIOBixujBiyZ+2bt0qIhYNdR8RGQcjVhdGLPlTcXFxCzs01H1EZByMWF0YseRno+3UXiIyFEasLoxY8rMf7dReIjIURqxr/J8nRETkJUasa/yfJ2QyhYWF8ju72jYR+Q4j1jX+zxMyGVTvvHnznNtlyMzMTEtLU3uJSDdGrFv8nydkJpbyR2x4eLieYUTkDiPWLf7PEwpYSL5jx4599913H3zwwfr16wsKCmT/wYMHtcPkpsV9xKJ95MiRLVu2JCcnHz9+XHQuX74cw/r27Yu9Z86cEcNOnDixd+/eWbNmyWOJqAyMWLf4P08oYKEa27VrJyuzc+fOhYWFol+bndpNd22xGRUVJU5Vs2bNFStWoLNly5by/IhVMWzUqFFVqlTp2bOnPJaIysCILQv/5wkFJlRjnTp1Pv3008uXL2Mhi82NGzeKfs8i9qabbvrqq6/Onz//3HPPRUREnDt3zuWwpk2bbt++PT8/X3YSURkYsWXh/zyhwIRqnDhxomhj/YrNhQsXin7PInbq1KminZ6ejs0NGza4HBYfHy83ieiGGLFl4f88ocDkHH5i011/GW1lMycnB5tYGbscNnfuXLlJRDfEiL0B/s8TCkDO4Sc2w8LC5O9tp6SkuItV58NHjhwp2uvXr8fmnj17XA7TbhLRDTFib4D/84QCkLvw6969e5MmTZCyiYmJ4eHh7mLV+fAqVaoMHTp0ypQpOPyOO+4Qf5gCZ+jRo8eECRNc/iwVEd0QI/YG+D9PKAA5Z6TYPHny5AMPPFC7du3o6OjJkyfXrVvXZaw6H44oxSE4MC4uLj09XfSPGzcOy+LbbrtN/OYPI5aovBixN8b/eULmxuwk8hFG7I3xf56QuTFiiXyEEUsU7OLj47dv3672EpHXGLFEZH6jR48WPybtDv/7EPkCI5aIzO+GXwy/4YAS/ushKj9GLBGZ3w0T9IYDSvivh6j8GLFEZE6XLl36/PPPP/roo1OnTmkTNC8vb8OGDejHqlQOViLWeYzzvx5yOYxIixFLRCb022+/tWnTxmJXt25dmaBIx/bt28v+3bt3i/HaiHU5xvlfD7kcRqTFiCUiExo0aFCDBg327duXnZ09YsQImaAJCQkxMTEnTpw4cOBA8+bNu3btKsbLATrHlDGMSGLE6lKz5tV3wWYSGRmpXiQFGLxGeKVee+01bSc2ta+jsfb6s+patGgh/2JMQUGB5Vo6tmrV6tlnn51n9/DDD1etWlX8bz45QOeYMoYRSYxYXXBr9e79hZk+cEU2my0nJyc3NxcTUFFRkXrNVNnwGqldBufPKwoPD3/zzTflpkzHsLAwkffSsWPHtAN0jiljGJHEiNXFYsaItVqtmZmZWVlZCFqkrHrNVNksfgwk/1BWtz7VoUOHXr16ifa+ffss19IxJiZm6dKloh/vLOUPLskBOseUMYxIYsTqYsqITUtLw5vujIwMpCzWsuo1U2XzZyCZD8IPRT5gwAB8Ghs0aCDTcfHixbVq1RoxYsTUqVO7dOnSpEmTCxculFwfn+7GKP96yN0wIokRq4spI3bXrl2pqalIWaxlsZBVr5nI4KZNmxYVFYV8HTx4cL169WSCotGmTZvQ0NDY2Fj5lyOVFarLMcq/HnI3jEhixOpiyohNSUlBymIta7VabTabes1EROQdRqwupozYlStXbty4ce/evVjIZmVlqddMRETeYcTqwogl8h6/u0zBhhGrS8VG7N//vmXIkO3O/U899eU//rHVuV8e1a/fFud+zz4YsYGvYgMpPz//9OnTaq/9R2EvXryo9l6Doy5fvqz2espiup+RJiobI1aXio3YVatO4PM8cuRubeeyZUcKC4uPHLHJnlGjds+alZaU9EPfvleTdfbsg8XFJRhQRgzr/2DEBr6KDaTx48fjhIcOHdJ2vvnmmyEhIXfddZfsQSUsXbpU/jjPsmXLqlWrhgFlxLB+FXtFRIGPEatLBUbsU099ceZMblFRyaef/lfbf+nSlU8//UWO2bz5V/mKYPzw4V+j//nnd2Fz5swDzqct7wcjNvBVYCAVFxdHR0dXr179lVde0fZHRETIP4H0+eefx8XFhYaGWq7/2dqTJ0+KapE9HqvAKyIyBDmNM2LLUoERO378fnySv/nmTHZ2/tNPfyn70blo0U+ivWDBYWwmJx8dOPCrMWP2/v573uHD2c7DvPlgxAa+CgykLVu24GxPPvlks2bNrly5Ivu1aYrFa79+/SZOnKhErDLMGxV4RUSGIIOVEVuWCozYHTtO/frrpXHj9uFTPWXK97Jfm50//2w7ePCPTMXHjBk/Yu+IEVcXstph3nwwYgNfBQZS//7927Vrt337dpxz/fr1st85O48ePerc6dzjmYr97jJR4JPByogtS0VF7DPPbMvPL0pOPvbUU1+cPp27e/dp0d+//1Z85ufMOSg2c3OvrF59Qh41ZMh27J0+PRXtgoLiZcuOOJ+5vB+M2MBXUYFks9nCwsKmTp1aXFzcunXr3r17i/5Lly6hDOSfABRcRmytWrW0f++XiHRixOpSURG7cOHVrwCvXXsSK1GsUwsLiwcO/Ar9mzdnXLp05fnnd4ph6F+yxJGjfftuKb0WwDt2ZGZl5cfH73A+ebk+GLHBY8GCBXi5x44di+C85557QkJCxMsdHx8fERHxyy+/aAe7jNh+/fpFRUX9+uuv2k4iuiFGrC4VFbFHj9rk51l4772rX/X96KPjRUUlL720Rww7cyZ33TqrPOqFF77GyEmTvkMbwfzf/+YMHnw1mL35YMQGjzvvvNNyvTlz5qB/woQJNWrU+PHHH7WDXUYsgrl9+/Znz57VdhLRDcmpnhFblgqJ2JEjd5de/53UkycvHj9+AY0+fb7ErnnzDon+rVt/w1K1f/8/fjkHq978/KIBA7ahjSRevPhn55OX94MRGyQOHz6sRGbHjh07depUcu2/qL733nuO0W4iFkn8zjvvaHuISA9GrC4VErGfffbf4uKSZ591/NGJ5cuP4hP+4otXf0G2VJO+L764p7Cw+L//vZicfGzz5qtfnfv88z9+w0c7zJsPRmyQePnll6tVq6b9P2vTpk2z2P/PUomrn2NyGbHOPZ6pqO8uExmFDFZGbFm8j9inn/7y/PmCAweytJ0JCTvxEoj4VLJz/Pj9WOAiaLOz87GKxTJX9DNig4f3gXTlypUmTZrcd9992k6r1VqlSpXExMQSV9np04i1VNzPSBMZAiNWF+8j9oYfOTmFKSnp4g85ufxASCcm7sELNGPGj857y/vBiA18fgikBg0aDB8+PC8vT91xDUI6NTUVz2T16tXqvvLzwxURBRRGrC5+iNhFiw5funTlxImr35p1+TF37qGiopIff8wqI4b1fzBiA58fAmn+/PkRERH/7//9P3XHNYsXL65evfr999+fm5ur7is/P1wRUUBhxOrih4gVH9q/96R8PPXU1Q/nfs8+GLGBz2+BpP17T4piO7XXU367IqIAwYjVxW8R67cPRmzgM18gef/dZSJjYcTqwogl/2MgERkdI1YXRiwREZUXI1YXRiwREZUXI1YXRiwREZUXI1YXRiyR9/jdZQo2jFhdGLHkf+YLJPP9jDRR2RixujBiyf/MF0jmuyKisjFidWHEkv+ZL5DMd0VEZWPE6sKIJf8zXyCZ74qIysaI1YURS/5nvkAy33eXicrGiNWFEUv+x0AiMjpGrC6MWCIiKi9GrC6MWCIiKi9GrC6MWCIiKi9GrC6MWCLv8bvLFGwYsbowYsn/zBdI5vsZaaKyMWJ1YcSS/5kvkMx3RURlY8Tqwogl/zNfIJnviojKxojVhRFL/me+QDLfFRGVjRGrS2RkpMVcwsPDGbEBTqk65Vuz2DTiXu0mkekxYvWy2WxWqzUtLW3Xrl0pKSkrjQ9XgWvBFeG6cHXqBRMRkXcYsXrl5ORkZmZiwZeamopk2mh8uApcC64I14WrUy+YiIi8w4jVKzc3NysrKyMjA5mEld9e48NV4FpwRbguXJ16wURE5B1GrF4FBQVY6iGNsOazWq3HjA9XgWvBFeG6cHXqBRMRkXcYsXoVFRUhh7DaQyDZbLYs48NV4FpwRbguXJ16wURE5B1GLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glTRewN/8sH93Iv93KvspfId0wVsURERIGDEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixf4iMjNT+Lw4ig0IlB2FVa6+aKHAwYv+Au1R+BoiMC5Vss9lycnJyc3ODp6q1V11QUFBUVKTe4USVwVGisqUOCQ7BMxmRuaGSrVZrZmZmVlZW8FS19qoRtEhZ9Q4nqgyOEpUtdUhwCJ7JiMwNlZyWlnbs2LGMjIzgqWrtVSNlsZZV73CiyuAoUdlShwSH4JmMyNxQybt27UpNTUXeBE9Va68aa1ksZNU7nKgyOEpUttQhwSF4JiMyN1RySkoK8garuuCpau1VW61Wm82m3uFElcFRorKlDgkOwTMZkbmhkleuXLlx48a9e/cGT1VrrxoL2aysLPUOJ6oMjhKVLXVIcAieyYjMjRHLiKXA4ShR2VKHBIdKnIwKCgrOnDmj9lJFGz169DfffKP2+sasWbNWrVq1efNmdYfvMWIZsRQ4HCUqW+qQ4FCJk9GECRPw6IcPH1Z3uPHkk096OXefPn364MGDSufly5dTUlIWL168fv36nJwcZa+XXD6ixzw7Gz7J8+fPF200lixZUqK5AUTnoUOHtD2eWbhwYaNGjfCZbNiw4dmzZ9XdPmb6iM3Ozl62bJnySjFiKTA5SlS21CHBobImIzx0dHR09erVX3nlFXWfG9qo8Ex4eLhyBsQqUsFyTe3atZFA2gFecn5Eb3h2Nu3nTVzmlClT3A3wmM1mq1+//qJFi9Bu27btmDFj1BE+pg2byqpqH1m3bl1cXFxoaKjzK6W9akYsBQ5HicqWOiQ4VNZktHXrVjw0FqbNmjUrKipSd7viPL9Ix48f/+CDD7AYLSwslJ3btm1bunSpXCUnJyfjDH379sVJfv/9d/T88MMPISEhDz744IEDB7B+3b9/f48ePbp27YrlQqn969hffvnlqlWrfvvtN3nOUvuaDw/3/fffL1++vLyPiMbJkyf37ds3e/ZssaldlCibeAJYteMk6enppa7OJuTn52OGxfPEGld2YmmOeRmdmZmZSsQ2b968WrVqW7ZskYPlAHfPB41vv/12xYoV+CSL3wzBmT/77LPc3Fw5+K233kLE5uXloY0IxxsXucs/TByxWLz269dv0qRJzrcAI5YCk6NEZUsdEhwqazLq379/u3btduzYYbH/1oHotNjJMc6bLiN2xowZVatWFYNjY2NF5g0fPlz0VKlSZfr06ehp2bKl6AGEHHqeeOKJ1q1bi1RQnDt3rlOnTmIw1o4ff/yx3IUePHN5qs6dO1+5cqVU3yOiMWrUKAzo2bOn2NRekXbz7NmzHTp0EMfWrFkTT8D5bICsbd++veisW7funj170Hnq1Kk2bdrITsv1EYssbNq0aePGjeVbBzlAO1Lpr169ujhhkyZN5CPKa4d7770Xb5hEe+fOndjrwde0vWExb8QK4vd9GbFkCI4SlS11SHColMnowoULYWFhSUlJeAIIud69e4t+MXHLYc6bzhGLQEVaDxw4EGGzdu1ajMHqDf21a9ceNmzY+fPnFyxYIL8vqJwhMjLS3Zepn3/+eYTT119/jazt1asXRtpsNrELJ6lTp45Yw2Ehi81NmzaV6ntEbCLe8MYCK1SXe+VmQkJCREQE5k1cF9ILi1fn8WJYTEwMVsZpaWlYnmIJjs5BgwY1aNAAi3I8mREjRmiPQnvRokVbt27FQvYvf/mLCEg5wN3zQePWW2/FDI5VNdrIb6vVijdGaGNyF4NxXRMmTBBtXD52ffLJJ/JUfmBhxDJiKWA4SlS21CHBoVImo4ULF+Jxx44di/ninnvuCQkJEV+bLZvz/CLgKjZs2DB69Og+ffpgDBIOnd26dWvRosWHH36o/Sq0coYaNWpgBSw3tW6++ebExETRFlObzBK0J02aJNqIKIs9tEr1PSI24+Pjy9grN7VPID8/33mA0KpVq2effXa+3cMPP4zVPMIbTwOfDTEAb0G0R8nPz+uvv472Sy+9hDbi9oYR+/bbb6NRXFyM9syZM2VbXHup/ZM5a9Ys0RYP+v777/9xIr+wMGIZsRQwHCUqW+qQ4FApk9Gdd95pud7cuXPVQU6c5xfhhRdeQEhgqTdkyBA5BpmN/lq1asXGxsovBStnwAIa+SQ3S+01IAIyPDxcpu+lS5dwIBasYlM5SbkeEZvz5s3Tbro8Ven1T0By/gyEhYX98Rm85vjx48qx2qNkG1caFxeHTbw7qVev3g0j1vkMShvrZvlTVFg9Y9eqVavEpn9YGLGMWAoYjhKVLXVIcPD/ZPTTTz8pM0XHjh07deqkGeKa8/wiICHEz6+eOHFCjhFfiT1w4AB6Vq9eLUYqZ3j55Zdr1qyJMbJn+vTp//M//5ORkfHnP//58ccfF53iK6LyV0uVk5TrEZVNBOS0adNEG1Gn3YvPySOPPCLahw8f3r17d6nT4RATE7Ns2TLRxrJS/BhUhw4devXqJTr379+vPUrbxnR8sx2WwqLT3fNxdwblCeMtjmiLP2H49ddfi03/sDBiGbEUMBwlKlvqkODg/8kIwYZFp/ZnYhFsFvtPx1jsZL/zpvh5WmHNmjWiv127drfffvsbb7yBRpUqVSZPnrxz586GDRsmJiYOGzbMcu17paX2pWGPHj0mTpwovgd54cIFHFinTp1Ro0a9/fbbTz31FAaLcFq8eDHagwYNwtkaNWrUpUuXkmtFo0xzYlPnIyrHdu/evUmTJkg1HIiR2r3iu7z9+vXD3ubNm+PSsLxWzgZLlizBunnEiBFJSUl4kjjbxYsXEbo4dsCAAePHj8fiUnta5Ql8++23eJMhO909H3dn0LZHjx7dunVr0X7vvfdCQ0Pl17f9w8KIZcRSwHCUqGypQ4KDnycj5AQm8fvuu0/bmZ6ejmjEtG6xk/0uNyUs4EQ/1pdt27bFCmzgwIFIoJ49e9pstqFDh9avXx8LXMSnPMO4ceMw7LbbbpO/moKRL774YosWLUJCQv70pz8hXcRiFBC6yIyIiIjevXtr3xBYXEWszkdUjv3ll18eeOCB2rVrR0dHT5kypW7dutq9c+bMueWWW3D4Qw89JH5vx/n5l9p/o6ZNmzaItNjY2B07dohOvGuJiopCvg4ePFh+HbjU6QmU2v8ek+x093y0R7lr//zzz3jn9OWXX6KNk/Tp00f0+42FEcuIpYDhKFHZUocEB1NORuTOhg0bRFprIRedOz2QkJCAmE9NTa1Ro8YPP/yg7vYx00esS4xYCkyOEpUtdUhwCJ7JiHwtLy/vwQcffPXVV8eOHavu8z1GLCOWAoejRGVLHRIcgmcyInNjxDJiKXA4SlS21CHBIXgmIzI3RiwjlgKHo0RlSx0SHIJnMiJzY8QyYilwOEpUttQhwSF4JiMyN0YsI5YCh6NEZUsdEhyCZzIic2PEMmIpcDhKVLbUIcEhMjLSQmR84eHhMmwiIiLU3SalvWpGLAUORqyDzWazWq1paWm7du1KSUlZSWRMqF7UMCrZek0wVLX2qnEvq7c3UWVgxDrk5ORkZmbiLXBqairu1Y1ExoTqRQ2jkjOvCYaq1l417mX19iaqDIxYh9zc3KysrIyMDNyleC+8l8iYUL2oYVRy1jXBUNXaq8a9rN7eRJWBEfsHfi+WzCEiIsJqtWIlh6SJrFNH3W1S2qvGEragoEC9w4kqAyP2D5ag+dlLMjdUsgybq1W9enUwfGivmhFLgcNxY8qWOiQ4MGLJHBixjFgKHI4bU7bUIcGBEUvmgEqW35UMqojl92IpADluTNlShwQHRiyZAypZ/mxtUEUsf6KYApDjxpQtdUhwYMSSOaCS5W+IBlXE8vdiKQA5bkzZUocEh8qK2IKCgjNnzqi95KnRo0d/8803aq8PzJo1Kz09fdu2bZs3b1b3VSqL8gcUndLIlB/aq+Zfd6LA4bgxZUsdEhwqK2InTJiAhz58+LC6w40nn3zSyzn99OnTBw8elJvz7RYsWPDBBx9s3749NzdXM7YclNN6z7MT4pOJyym1X9eSJUtKNCUuOg8dOqTt8czChQsbNWp09uzZNWvWNGzYEA11ROUxfcRmL1my7J//PPTWW9pORiwFJseNKVvqkOBQKRGLx42Ojq5evforr7yi7nNDRojHwsPDtWewXC8iImL69Oma4Xopp/WeZyeUnx9xOVOmTHG51xs2m61+/fqLFi0Sm23bth0zZsz1QyqTxbwRu2706LgOHUJr1Lj6Oj73nHaX9qoZsRQ4HDembKlDgsPVycjvtm7disfFwrRZs2ZFRUXqblfKCInjx49jJZqSklJYWCg7t23btnTpUrlKTk5Oxhn69u2Lk/z++++lmhPm5OTs27fvn//8Z5UqVV599VV5hvz8fMxcq1atwrJSdpZef2bn05bal4wnT57EOWfPni02tStI7WZBQQGW5jhJenq66HF5QnfP5PLly+vWrUN/ZmamvBw0mjdvXq1atS1btsiR2s+eu+eDxrfffrtixQp8MsUPzuDMn332mVzfv/XWW4jYvLw8sYkUx4pWnqfSmThisXjt99e/Tnr6aUYsGYXjxpQtdUhwqJSI7d+/f7t27Xbs2GGx/7CG6LTYyTHOmy4jdsaMGVWrVhWDY2NjRcoOHz5c9CA1xdq0ZcuWogcQfqWuTjhhwgQsrJEuaCPe2rdvL8bXrVt3z549YoxyZufTltrPPGrUKAzo2bOn2NQ+kNw8e/Zshw4dxLE1a9b8+OOPS109T3fP5NSpU23atJH9Fk3EIgubNm3auHHj3377TXlQpa3dRAOXL07YpEkT+aCdO3e+cuUKBtx77714VyQP3LlzJ/Z68DVtH7GYN2LFx7FZs66+WIxYMgLHjSlb6pDgcHUy8q8LFy6EhYUlJSXh0Vu3bt27d2/RLyZ0Ocx50zliEahI64EDByKH1q5dizFY1aG/du3aw4YNO3/+/IIFC+T3C5UzOJ8QoYVOnAfthISEmJgYLEbT0tKwKOzatasY43xm5/OgBwmHNxBYpDoPkJt4iIiICMyMePJIL6xclQGCu2cyaNCgBg0a7N+/H09mxIgR8ig0Fi1atHXrVixk//KXv4h01J7T3fNB49Zbb8U0jYU12shvq9WKN0BoYwbHAFwU3oXIA3H52PXJJ5/InsplYcQyYilgOG5M2VKHBIerk5F/LVy4EA86duxYzOz33HNPSEhIdna2OsiJEgwSLmHDhg2jR4/u06cPxiD50NmtW7cWLVp8+OGH2q9Cu4sWKT8/H51Lly5Fu1WrVs8+++x8u4cffhgLZZGXzmd2Pg964uPjtZsuH/fmm29OTEwUnXho5wGCu2eCp4GrFmPwVkMeJT8Jr7/+OtovvfQS2ohbeU53zweNt99+G43i4mK0Z86cKdvi+681atSYNWuWPFA86Pvvvy97KpeFEcuIpYDhuDFlSx0SHK5ORv515513Wq43d+5cdZCTq5OLq4h94YUXkB9YBQ4ZMkSOQWajv1atWrGxsfJ7h8oZnE/47bffovOrr75CG+vs656ixXL8+PFSV2d2Pg965s2bp910+bjh4eEzZsyQ/ZIy3t0zUQ6XR8kGXty4uDhs4i1IvXr19ESsyzGyjUWz9qeosHrGrlWrVsmeymVhxDJiKWA4bkzZUocEh6uTkR/99NNPyhTfsWPHTp06aYa4phwlITzEz7WeOHFCjhHrvAMHDqBnNWYiO3fRIiA7kf1YMorlaUxMzLJly8QurOTkTx45n9n5iSk9yMhp06aJNtJO7sWFP/LII6L/8OHDu3fvFm3lcHfPpEOHDr169RLt/fv3y6O0h2PCvdkO1yU73T0f7YEu23jCeB8jOkH8hYevv/5a9lQuCyOWEUsBw3FjypY6JDhcnYz86OWXX8aiU+YETJ8+3WL/qRmLnex33hQ/ZyusWbNG9Ldr1+72229/44030KhSpcrkyZN37tzZsGHDxMTEYcOG4ahNmzaJkVj29ejRY+LEifLbk+KEOFZ8XxPkX29YsmQJlqojRoxISkrq0qVLkyZNLl686PLMymnFmbUZ2b17dxyOVMOBGCz3Ll++HO1+/fphV/PmzfH8RborJ3T5TNCP3MXhAwYMGD9+PJ65PK3y6Fia16xZU9vp7vlox7hsjx49unXr1qIT3nvvvdDQUO2XuCuXhRHLiKWA4bgxZUsdEhyuTkb+ggjB5H7fffdpO9PT0xGNmO4tdrLf5aaEtZ3oRyi2bdsWK7OBAwcimXr27Gmz2YYOHVq/fn0scEeNGiXPMG7cOAy77bbbxO+oyFNhZPv27bEUzsjIkINL7b/E0qZNG6RIbGzsjh07Su2/GOp8ZuW0pU4h98svvzzwwAO1a9eOjo6eMmVK3bp15d45c+bccsstOPyhhx6Sv7fjfELnZyLg3UlUVBTydfDgwfJLwcqjl9r/HpO2093z0Y5x2f7555/x9ujLL78U/ThJnz59RDsQWBixjFgKGI4bU7bUIcHh6mREJrJhwwaZ1hJy0bnTAwkJCYh5vFU6cOBAjRo1fvjhB3VE5TF9xLr8YMRSYHLcmLKlDgkOjFjSLy8v78EHH/zxxx+xrh07dqy6u1IxYhmxFDgcN6ZsqUOCAyOWzIERy4ilwOG4MWVLHRIcGLFkDoxYRiwFDseNKVvqkODAiCVzYMQyYilwOG5M2VKHBAdGLJkDI5YRS4HDcWPKljokODBiyRwYsYxYChyOG1O21CHBgRFL5sCIZcRS4HDcmLKlDgkOjFgyB0YsI5YCh+PGlC11SHCIjIy0EBlfeHi4DJuIiAh1t0lpr5oRS4GDEetgs9msVmtaWtquXbtSUlJWEhkTqhc1jEq2XhMMVa29atzL6u1NVBkYsQ45OTmZmZl4C5yamop7dSORMaF6UcOo5MxrgqGqtVeNe1m9vYkqAyPWITc3NysrKyMjA3cp3gvvJTImVC9qGJWcdU0wVLX2qnEvq7c3UWVgxDoUFBTgzS/uT7wLtlqtx4iMCdWLGkYl51wTDFWtvWrcy+rtTVQZGLEORUVFuDPx/he3qM1mkysAImNB9aKGUckF1wRDVWuvGveyensTVQZGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHyCEUtEROQTjFgiIiKfYMQSERH5BCOWiIjIJxixREREPsGIJSIi8glGLBERkU8wYomIiHzCRcQSERFRBWLEEhER+QQjloiIyCf+P92lUbsBe/7hAAAAAElFTkSuQmCC" /></p>


```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 120

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

<!-- pu:deep/plant_uml/shared_ownership_6.pu--><p><img src="data:image/png;base64,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keEwgr2FNKxXr96nn356/fp1LISxuX37dlFftQj+j//4jz179ly+fPkf//hHRETEb7/95rLZ3XffvXfv3sLCQllJRIbDCPYW0nDatGmijPUvNpcsWSLqqxbBb7/9tiifO3cOm9u2bXPZbOTIkXKTiAyKEewt53AUm+7qKykrm3l5edjEytplswULFshNIjIoRrC3nMNRbNapU0f+reXExER3set8+KuvvirKX3zxBTYPHjzospl2k4gMihHsLXfh+OijjzZt2hQpPGHChPDwcHex63x4tWrVXn755bfeeguH//d//7f4xQ2coVevXlOnTnX5WR8RGRQj2FvOGSo2z5w588QTT9StWzcqKmrGjBn169d3GbvOhyNqcQgO7NOnz7lz50T95MmTsaxu06aN+GYbI5jIHBjBwYXZShRSGMHBhRFMFFIYwcFl5MiRe/fuVWuJyKQYwUREumEEExHphhFMRKQbRjARkW4YwUREumEEExHphhFMRKQbRjARkW4YwUREumEEm9Ybb7yhVhFRkGEEm5bFYlGriCjIMIJNixFMFPwYwabFCCYKfoxg02IEEwU/RrBp8eM4ouDHCCYi0g0jmIhIN4xgIiLdMIKJiHTDCDYtfhxHFPwYwabFL6URBT9GsGkxgomCHyPYtBjBRMGPEWxajGCi4McINi1+HEcU/BjBRES6YQQTEemGEUxEpBtGMBHdWmxs7MGDB9VaXf373/+2Wq1qrXu7du368ssv1Vq9hWgEX716dcuWLStXrgzAqDp69Ojq1as/++yz/Px8dZ8/8eM40/jtt982btyIUXTkyBF1n+9kZ2dnZGSotTdZLJaFCxeqtfpZvHhxkyZNfv31V3WHhjL1NmzY0Lhx48oPCbxQjOCdO3dGRERYburXr9+NGzfURr5QWlo6atQoeUNRUVEnT55UG/kNv5RmDh999FGdOnXwaFa3Gzx4cElJidrIF8LDwysJWUswRfDly5cbNmy4ZMkSdcdN7qZe27ZtJ06cqLbWlckjeP369cuWLcPjgfKVK1cwhpKTkx955JHo6Ojjx49fv359zpw5eITwPKkeeTtc3grK8fHxOHlcXFxOTs7+/ftbtWr15z//WTnWfxjBhuM8kLBceOihh/r373/u3DlU7t27Fw/rtm3b1CNvH16Vr1ix4tixY2ITq0Wc+YUXXsCNXrx4UVReu3YN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" /></p>


```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 142

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

<!-- pu:deep/plant_uml/shared_ownership_7.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcIAAAGICAIAAABduXcYAAA3G0lEQVR4Xu3dB3wU1b4H8A0tkEAIxFACGAIKF/SBcEG8YAGkieBVuDwR/FwQFXgKIhjlvncpQVpAEaQ36REpYkEC+gTpSFFiQpP6EgMBgbAQSCPl/dwjZ4ezu7BkNltmf9+PHz9nzpyZ3dn85zdnNkvWVEhERDqY1A4iIroXjFEiIl2sMVpAREROY4wSEenCGCUi0oUxSkSkC2OUiEgXxigRkS6MUSIiXRijRES6MEaJiHRhjBIR6cIYJSLShTFKRKQLY5SISBfGKBGRLoxRIiJdGKNERLowRomIdGGMEhHpwhglItKFMUpEpAtjlIhIF8YoEZEujFEiIl0Yo0REujBGiYh0YYwSEenCGCUi0oUxWhSnT59u3rz5v//9b3UFEfkfg8Rodnb2Oo21a9fu2bNHrk1NTR1t4/jx45od3MmlS5eOHDly6NChpKSkxMTEhIQEbN6pU6caNWpgz9rHXb9+vboxERmdQWIUSVexYsXQ0NDw8PCaNWtWqFAhIiIiPz9frEViPmvjwIEDt+/jD4hjtaugYMKECSYbISEh8fHxq1ev1nYiWNWNicjoDBKjWjdv3qxbt+64ceNkzxEHrl69Ksf8+OOP+/btQwQjkbH44osvTp48WaxKT08/depUcnIy5p5paWkXL1584oknBgwYILeFvLy8pk2bzpkzR9tJRP7AgDE6b9684OBgkYaQm5urnTBqffrpp2LMiRMnSpcujbvy2rVrR0dHoycyMjI2NlbuUysjIyMoKGjFihXaTjxo48aNEabaTiLyB0aL0YMHDyLjRBRK524ZO3ZstWrV5GJmZqYc89Zbbz3yyCOffPLJP//5T8xSAwICvv76a80+rGbOnFm+fHntTDY7O7tWrVqff/65ZhQR+QtDxeiBAwciIiKioqIwG924caO6uqDg7bffbtasmdprcebMmVmzZt28eRPtiRMnlilT5vLly+qggoJDhw6FhoaOHj1a24nwxeyVU1Ei/2SQGEWEzZ8/H/PQTp063bhxA7NO3KQrSfrzzz+HhYVhlbZTkZWVhQwtUaJETEyMsur69etTp06tWLFi586dc3NztaseffRRJViJyH8YIUbT09ObNm1aqlSpUaNGiekk4L4ec9J9+/YVWBLw73//O8LxueeeQ8jetrHGO++8Ex4eXq5cufHjx2v7EZp9+vRBgFaoUAEprGQoprEmk0k8EBH5ISPEKMyYMePw4cPanvz8fKTquXPnxCLmqt999512gK0VK1ZMmzbtwoUL6oqCgg8//BB7MJvN6goi8nsGiVEiIk9hjBIR6cIYJSLShTFKRKQLY5SISBfGKBGRLoxRIiJdGKNERLowRomIdDFUjIaFhal/C8/H4YjUgyQiL2OoGEXuyKMwBhyR2WzOyMjIzMzMycnhH5Ei8kLWE1a21CG+w5AxmpycnJaWdvnyZYQpklQ9ZiLyNOsJK1vqEN9hyBhNSko6ceJEamoqklT7d6aJyEtYT1jZUof4DkPG6M6dOxMSEpCkmJNiQqoeMxF5mvWElS11iO8wZIzGx8cjSTEnxd09/1IfkReynrCypQ7xHYaM0ZUrV27atGnfvn2YkNr9XhMi8izrCStb6hDfwRglIveznrCypQ7xHYxRInI/6wkrW+oQ3+HmGD18+PCKFSvWr1+flZWlrnMRxiiR97OesLKlDvEdbotRPNbAgQNNt0RFRSHj1EGuwBgl8n7WE1a21CG+ozhidPXq1YsWLSqwvFLXrl2bM2fOrl27FixYgMeaNGlSenr67t27IyMjn3zySXVLV2CMEnk/6wkrW+oQ31EcMRoXF4fdIjfRHjx4cHBw8MmTJ1u2bNm6dWs5Zs2aNRhz7Ngx62Yuwhgl8n7WE1a21CG+ozhiFJ5//vnKlSt/8803JUqUmDFjBnpCQkJiYmLkgAsXLuChv/jiC+s2LsIYJfJ+1hNWttQhvqOYYvT8+fNhYWHI0KeeeqrA8pIFBgZOmzZNDsjOzsZDL1myxLqNizBGibyf9YSVLXWI7yimGIX27dtj5+PHjxeLUVFRw4YNk2uPHz+Otd99953scRXGKJH3s56wsqUO8R3FFKOYZmLPrVq1KleuHBITPf369atRo8b169fFgBEjRgQFBZnN5ts2cwXGKJH3s56wsqUO8R3FEaMpKSkVK1Z86aWXrl69GhERgTDNz89PSkoqW7Zs48aNY2NjBw4ciPv96OhodUtXYIwSeT/rCStb6hDf4fIYxT7btWsXGhp6/vx5LK5btw4PMWXKFLR/+OGH5s2bBwYGIlsxG71586a6sSswRom8n/WElS11iO9weYx6HGOUyPtZT1jZUof4DsYoEbmf9YSVLXWI72CMEpH7WU9Y2VKH+A7GKBG5n/WElS11iO9gjBKR+1lPWNlSh/gOxigRuZ/1hJUtdYjvYIwSkftZT1jZUof4DsYoEbmf9YSVLXWI72CMEpH7WU9Y2VKH+I6wsDCTsQQHBzNGibycoWIUzGZzcnJyUlLSzp074+PjV7qIyTIr9Ah+Tz2RlzNajGZkZKSlpWHilpCQgPTZ5CKIUbXLXXAUOBYcEY4LR6ceMBF5mtFiNDMzE3e+qampyB3M4Pa5CGJU7XIXHAWOBUeE48LRqQdMRJ5mtBjNycnBlA2Jg7kb7oJPuAhiVO1yFxwFjgVHhOPC0akHTESeZrQYzcvLQ9Zg1obQMZvNl10EMap2uQuOAseCI8Jx4ejUAyYiTzNajBYTxKjaRURkwRh1CmOUiBxhjDqFMUpEjjBGncIYJSJHGKNOYYwSkSOMUacwRonIEcaoUxijROQIY9QpjFEicoQx6hTGKBE5whh1CmOUiBxhjDqFMUpEjjBGncIYJSJHGKNOYYwSkSOMUacwRonIEcaoUxijROQIY9S+Ro0amRzAKnU0Efkxxqh9sbGxanzeglXqaCLyY4xR+5KTk0uUKKEmqMmETqxSRxORH2OMOtS6dWs1RE0mdKrjiMi/MUYdmj9/vhqiJhM61XFE5N8Yow6lp6cHBgZqMxSL6FTHEZF/Y4zeSbdu3bQxikV1BBH5Pcbonaxdu1Ybo1hURxCR32OM3klWVlalSpVEhqKBRXUEEfk9xuhdvPbaayJG0VDXERExRu9qy5YtIkbRUNcRETFG7yo/P7+WBRrqOiIixqgzhluovUREFozRu/vFQu0lIrJgjBIR6cIY9YDc3Fz5Tqu2TUS+iDHqASaTafbs2bbtO0hLS0tKSlJ7icgLMEY9oAgxGhwc7MwwInI/xqheSLcTJ0789NNPy5Yt27BhQ05Ojuw/dOiQdphcvEOMov3rr79u3rx5xYoVJ0+eFJ3Lly/HsF69emHthQsXxLBTp07t27dv+vTpclsi8gjGqF4IuIYNG4qP6EPz5s1zc3NFvzYfHUWn7bAaNWqIXZUpUyYuLg6dkZGRcv+ITjFs6NChAQEBXbp0kdsSkUcwRvVColWoUOHLL7+8ceMGJqRY3LRpk+gvWozed999W7duvXLlyuuvvx4aGnrp0iW7w6pXr75t27bs7GzZSUQewRjVC4n2/vvvizbmoVicN2+e6C9ajE6cOFG0U1JSsLhx40a7wwYMGCAXiciDGKN62QacWHTUf4e2spiRkYFFzHDtDps1a5ZcJCIPYozqZRtwYjEoKEh+h2h8fLyj6LTd/O233xbtDRs2YHHPnj12h2kXiciDGKN6OQq4tm3bVqtWDUkaHR0dHBzsKDptNw8ICOjfv/+ECROw+aOPPio+nI89dOzYccyYMXZ/f0VEHsQY1cs2B8Xi6dOnO3ToUL58+aioqPHjx4eEhNiNTtvNEZfYBBt27tw5JSVF9I8aNQrT2/r164tPTTFGibwHY9S7MB+JfA5j1LswRol8DmPUuwwYMGDbtm1qLxF5McaoEdy8efP333/Py8tTV9i4cePG5cuXCywfcVXXEd0jFp5g8BjNz8/fvn376tWr8cNW11lMmTLlX//6l9qrgW3XrFlz7NgxL/xzdmfPnu3fv//58+d//vlnk8l0+vRpdYSNCRMm1KxZMyYm5vHHHzdkQXuWsetNYuEpjByj2dnZHTp0MFmEhITs3r1bHVFQ0KhRo27duon2okWLRowYcfv6gqeeekrsoVq1aq+//vqvv/6qDBDOnDkTHR39t7/9rUGDBm3bto2NjTWbzeogVxs7dmzlypWzsrLuUM0nT578WmPAgAEVK1acN28exn/wwQcZGRnqBlRUhq83iYWnMHKMTpo0KTAwcOPGjampqS1atEAFy1XXrl07evToV199hR/qP/7xD/yYcQ6MHj26dOnS2sJFaY4cOXL//v3ffPMNajo8PNxuWa9atapcuXKokocffvj+++9/9dVXg4KCIiMjjxw5og51nZycnNq1az/44IPvvPPOP//5TxwInuE7t8hPSk2ePLlkyZJht1SoUAEj5eLx48dv3ysVnbHrTWLh2TJIjK5bt+7LL78UbVwhFy9enJmZ2axZs5deekl0fvvtt/gpopTFopw1mCx/SAn/x4X96tWrERERqHIxBjChwKr/+7//E4t23wPas2cPTobevXtj80GDBmFqUGC5FNeqVatevXryT4dcuXIFJ098fLz2j4mgvWXLFjx53CXJTkxScHnfunUr7u9OnTqFnri4uB07doi1OEUx4Ny5c2PGjClbtmxHi5YtW+J5Pvnkk2IR5OmHam7cuLHcufj3VHjcgwcPXrx4UfbTPfHyekOF4Oe7du3azz77DKWC6vr888+1NWZbeMuW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" /></p>

以上で示したstd::shared_ptrの仕様の要点をまとめると、以下のようになる。

* std::shared_ptrはダイナミックに生成されたオブジェクトを保持する。
* ダイナミックに生成されたオブジェクトを保持するstd::shared_ptrがスコープアウトすると、
  共有所有カウントはデクリメントされ、その値が0ならば保持しているオブジェクトはdeleteされる。
* std::shared_ptrを他のstd::shared_ptrに、
    * moveすることことで、保持中のオブジェクトの所有権を移動できる。
    * copyすることことで、保持中のオブジェクトの所有権を共有できる。
* 下記のようなコードはstd::shared_ptrの仕様が想定するセマンティクスに沿っておらず、
  [未定義動作](term_explanation.md#SS_19_18_7)に繋がる。

```cpp
    //  example/term_explanation/shared_ptr_ownership_ut.cpp 162

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


#### オブジェクトの循環所有 <a id="SS_19_5_7_3"></a>
[std::unique_ptr](https://cpprefjp.github.io/reference/memory/unique_ptr.html)の使い方を誤ると、
以下のコード例が示すようにメモリーリークが発生する。

なお、この節の題名である「オブジェクトの循環所有」という用語は、
この前後の節がダイナミックに確保されたオブジェクトの所有の概念についての解説しているため、
この用語を選択したが、文脈によっては、「オブジェクトの循環参照」といった方がふさわしい場合もある。

まずは、リークが発生しないstd::unique_ptrの正しい使用例を示す。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 8

    class Y;
    class X final {
    public:
        explicit X() noexcept { ++constructed_counter; }
        ~X() { --constructed_counter; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<Y> y_{};
    };
    uint32_t X::constructed_counter;

    class Y final {
    public:
        explicit Y() noexcept { ++constructed_counter; }
        ~Y() { --constructed_counter; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<X> x_{};
    };
    uint32_t Y::constructed_counter;
```

上記のクラスの使用例を示す。下記をステップ1とする。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 39

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

<!-- pu:deep/plant_uml/shared_each_1.pu--><p><img src="data:image/png;base64,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5KNHj1KoWbOm/X9NgQh/tSQlJWXkyJFo6H333efXvqAnoEuWLGnYsCHqPGHCBH8Vx9/l0bt373r16ply+NdLHJCDo6H9+vVzqoJhMiqEyFIkoxHp2bNnuXLlzK+GHDly5IYbbrj//vspb9q0yayRkTDW5sioTVQNSCFCVtRjyJAhJ06c8NfOmzevfPnyKGDLli03btzor4KYmJjQq/1TdOjQwe/DXrVq1brooosifYgqGRUiO5GM/nZYTfft29e+cPczfPjwyZMnHzhwwK0IBrds2TJw4MCtW7e6FR6HDh3aGkZSUpLfhzy3ffv28fHxfqOfqVOnzpo1y7UKIbIGyagQQkSFZFQIIaJCMiqEEFEhGRVCiKiQjAohRFRIRoUQIioko0IIERWSUSGEiArJqBBCREWuktESJUq4/48yh0OL3EYKIc4zcpWMoju2FbkDWpScnJySknL48OFjx445f+JECHE+EApYW3Jdcg65UkYTEhISExP37duHmNo/7SyEOH8IBawtuS45h1wpo/Hx8d9///2OHTtQUnJSt81CiHNNKGBtyXXJOeRKGY2NjY2Li0NJyUnDf8hECHHOCQWsLbkuOYdcKaMxMTEoKTkpq/vwv98shDjnhALWllyXnEOulNHXX3998eLFq1atIiF1fiJUCHE+EApYW3Jdcg6SUSFE9hMKWFtyXXIOklHh5+TJk7/88otrFWkxYcKEzZs3u9bTOXLkyIYNG1zrecaxY8fs7+BywadXZhWhgLUl1yXnkM0yypCaPXv2+++/z91y6zKJvCyjW7ZsmT59umvNMNyU1q1blytXLjk5+dtvvx0wYIDzo1hvvfXWqx6TJ09+5ZVX7j+dtWvXWs8nnnjiX//6l2/X30Kke+dcFZs///zzTz/9tHPnzoSEhE2bNu3evdtUYZw2bdrKlSutM5MEls8++8xa/Dz00EMZvOxevXox0q644orExERjiYuL++GHH/w+f//731u0aFG0aNEvv/zSb88IXbp0efbZZ11rGPfdd180d3zkyJHjx4+/8847X3zxxb/85S9Ezd/+9jfz+2lZTShgbcl1yTlkm4xyro4dOwZOUalSJTTOdcoMcrGMkjLs2bPHtXq88cYbf/zjH/Ply0fz3brTIezvvvvumjVrOr9M9fHHH994440XX3zxrFmzYmNje/TowaHw9CendevWrVix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" /></p>


上記の続きを以下に示し、ステップ2とする。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 55
        // ステップ2

        auto x1 = x0;
        auto y1 = y0;

        ASSERT_EQ(X::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない
        ASSERT_EQ(Y::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない

        ASSERT_EQ(x1.use_count(), 2);  // コピーしたため、参照カウントが増えた
        ASSERT_EQ(y1.use_count(), 2);  // コピーしたため、参照カウントが増えた
```

<!-- pu:deep/plant_uml/shared_each_2.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAjAAAAEmCAIAAADz9D0jAAA3MklEQVR4Xu3deXwURd4G8OYSEAiRS4kglyzKGVwQAbkUEJEVQS4vXAXkUkBBUZFjBUJgQeRc7msBRS5FCYeKGrOABDEQRAQCDoQEDAnJhisQ5n0fu97UVGoyoZGeyUze5/uHn57qmp7pmunfUzUzRON/iIiI/IChNxAREeUFBhIREfkFVyA5iYiIfI6BREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGBREREfoGB9GccP368cePGo0aN0ncQEdGflU8C6cqVKxsU69at27Vrl9wbHx8/1s2RI0eUA+Tm3Llzhw4dOnjwYGxs7IEDB2JiYnD3Dh063H333aLDqVOntm7dum/fvuz3IyKim5BPAgmZUbp06eDg4PLly1eqVKlUqVIhISHXr18Xe5E9T7jZu3dv9mP8AcGmNzmdYWFhhpugoKCIiAixt1ChQqKxffv2V69e1e9PREQW5JNAUl27dq1GjRoTJkyQLYc8SEtLk3127969Z88ehBmyDTd79uw5ZcoUsSslJSUuLs7hcGCllZiYmJSU1KJFi/79+2PX2bNny5QpgwXZpUuXNm/ejEz67rvv5DGJiMi6fBhI8+fPL1GihMgVwJIl29JGsXr1atHn6NGjRYoU2bBhQ9WqVUeMGIGWKlWqhIeHy2Oq0tPTb7/99pUrV4qbGRkZYgN3r1evHtLL1ZWIiCzLb4H0008/IS1EqEgJWcaPH3/XXXfJm1jWyD5DhgwJDQ1dvHhx7969sXIqUKDApk2blGO4zJ49u2TJkurq6tSpU1hR9ejR4/z580pHIiK6CfkqkPbu3RsSElKtWjWskLZs2aLvdjqHDRvWqFEjvdV04sSJOXPmXLt2DduTJk267bbbkpOT9U5O58GDB4ODg8eOHStbtm/fXrdu3RwfjoiIrMsngZSZmblgwQKsjTp06HDx4kWshIoUKaKFxL59+8qWLYtdaqPm8uXLSKOCBQuOGzdO23XhwoXp06eXLl26Y8eO8pcLx44dQ/ihXf7AD88k+/2IiMiS/BBIKSkpDzzwQOHChceMGSOWODBixAhExZ49e5xmlnTu3Bkx8+STTyKust1ZMXz48PLlyxcvXnzixIlqO+LnxRdfRBSVKlUKeab+jm7Tpk3a91Lqx4BERGRdfggkmDVr1s8//6y2XL9+HfmUkJAgbmL9tH37drWDu5UrV3744Ydnz57VdzidU6dOxRFSU1P1HUREZJN8EkhERBToGEhEROQXGEhEROQXGEhEROQXGEhEROQXGEhEROQXGEhEROQXGEhEROQXGEhEROQX8lUglS1bVvtDPoEOZ6SfpE9wJInI9/JVIKHuyLPIH3BGqamp6enply5dysjI8NlfbuVIEpHvuS5YuaV3CRz5sow6HI7ExMTk5GQUU/k/A/Q2jiQR+Z7rgpVbepfAkS/LaGxs7NGjR+Pj41FJffanxDmSROR7rgtWbuldAke+LKNRUVExMTGopJjdY2qvn7N3cCSJyPdcF6zc0rsEjnxZRiMiIlBJMbt3OBw++/9fcCSJyPdcF6zc0rsEjnxZRj/66KOtW7fu2bMHU/sc/6/q3sCRJCLfc12wckvvEjhYRu3CkSQi33NdsHJL7xI4WEbtwpGkXBw5ciQlJUVv/X8vLCxs8+bNemuWCxcubNq0SW+1wKu/CL1uio6OvnLlSmZm5qVLl06ePKl38iHXBSu39C6Bw8dl9Oeff165cuXnn39++fJlfZ9N8qqM+ngkUd2WL1+O8dR32CevRjJvXb16VW8yORyOzz77bNeuXShG+j4T2n/88cdff/1V3+F0btiwoXjx4itWrDh37lynTp127twpdw0bNuw505w5c2pkJ2vxiRMn7r77brwK8l5W4BI7c+bMf//7X2xHRkb+9ttvWoeffvpJO9nDhw/jqX7yySerV6/Guwv/lbu+++67tWvXypuownhvxMTEyBZp6tSpDRs21FtzsmTJEsN0/Phx3JwxY8aOHTvk3qVLl957771lypSZN2+ebLQCr1Tp0qW3b9+u78jy5ZdfYjxzfz8jacQ/eNB3OJ3du3f/+OOPCxUqNGbMmIcffnjLli3FihVDOKl9kpKS8Hr5ZgriumDllt4lcPisjOKxBgwYIN5/UK1aNdQ4vZMd8qqM+mwkEecdO3bENYBH/Ne//qXvtk9ejWQeatOmDU5Zb3U6P/zwQxQg8dZt27ate2ilpqZ26NDhwQcfFLVVwty5W7duuFdoaOg//vGPwYMHo1bitUPRFx2qVKnSv3//v/71r2+++SYqPh5l9uzZKKZly5Zdt26d6HPw4EEcYe/eva7jKhCEL730UpcuXR555BEcp2bNmhUqVChatKh4tiid6IPn/Mwzz6j3wvPEXjUAYPz48UWKFMEz/Mtf/nL77bcXLFhQxhgiDc9t/vz54ubw4cODg4PFXrwx4uPjcaYIzri4uDfeeKNcuXII5kOHDp0/f170j4iIqF69etWqVXG+lStXRh5UrFixRIkSeA7vvvuu01zTNGjQADfr16+/ceNGp5l5rVu3xjN/5ZVXxEEsGjlyJI6D8Rw7diwyA8N79uxZtQOSHh1+//13tVHCc37ttdfuuOMOMYCYGeAqk3txqObNmzdu3BiDU69evZ49ew4cOLBSpUofmOR44nQwRDjN//znP/K+XuK6YOWW3iVwGF4oo7jYMPdxmiOFCRpeTrwqCxcuxGNNnjwZswbMEPG+bNmypX5POxh5VEZ9NpKYumJCjdphBFogYcYtC5zcRnHHQ/zwww/qygNT+y+++OLUqVOyxR0KCrL5l19+URuxBEHtw0xftuT4oNjAwb///nt0TktLE3u/+uornPKQIUNwWHl3p/nBEarntGnTLl68iFcEfdxn308++STKk/sPEbGGaNKkSbt27QoXLoxyjPo4d+7c0aNHI0JEB1wIeA54Qbt27YqeqHQYCjwK+kdFRYk++/btw4OivruOm12vXr369u373nvvzZo1q0WLFlhV4HLDmmb37t0iEh566CHUTe1e991334gRI7RGp7k4eOedd+68807tNJEcQUFBWH/g+kU5lusnnLuo3e6wKBR99u/f/9Zbb+GweJLICWQz3sA4R6SF6wGczq+//hprjlGjRombP//8MxaOaocbOn36NKI0JCSkdu3aWKhhPA3zMlH75BJIeP/gjnil8LiYN+Ac33//faT70KFDRQe8tTp37ozBwREQ21jv4r1Rp04dDDtaMHFRj4bzRTZjxNRG27kuWLmldwkchhfK6KpVq3BYXBLYxlwD86Bjx441a9YM8x3ZB5NB9MGr67qbTQy7y6hFPhtJsQunJq60bHewle0jiQPKKia3//a3v/1RugwDqwexCw+H2TdacL6eJpjoI+awBQoUkNP2n376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" /></p>


上記の続きを以下に示し、ステップ3とする。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 67
        // ステップ3

        auto x2 = std::move(x1);
        auto y2 = std::move(y1);

        ASSERT_EQ(x1.use_count(), 0);  // ムーブしたため、参照カウントが0に
        ASSERT_EQ(y1.use_count(), 0);  // ムーブしたため、参照カウントが0に

        ASSERT_EQ(x0.use_count(), 2);  // x0からムーブしていないので参照カウントは不変
        ASSERT_EQ(y0.use_count(), 2);  // x0からムーブしていないので参照カウントは不変
```

<!-- pu:deep/plant_uml/shared_each_3.pu--><p><img src="data:image/png;base64,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bdu2taa+HEql3g8AAPcg+BszcuRIa/DLod4DAABXIfgbs2bNGmvwy6HeAwAAVyH4G3PmzJnOnTur1JeCHOo9AABwFYL/Ih555BEV/FLQ2wAAcBuC/yK2bNmigl8KehsAAG5D8F9EXV1dvI/645sAALgawX9xT/rotQAAuBDBf3G7ffRaAABciOAHAMBDCH4AADyE4P9Oamtrjx49WlNTozcEmDZt2nPPPafX+hQVFT3//POX9EsCTpw4UVpaqteeV15eXlFRodcCAEDwNyI/P/+DDz4wDz/55JONGzda2r917NgxwzA+++wza+XXX3+9f//+vXv3FhQU7NmzZ9euXVlZWeozgZLxVVVVQ4YMWbp0aXV1tXSW+4YuXbr07Nlz7Nix1gdp3BNPPJGcnKzKgR83kIcaN26cVgkAQD3B34g///nPV1xxRV5enpQPHjwYFRUlaS1l+Tc9PT0tLS01NXXGjBkS57/61a+efvrpDz/8UJ04b948FfMa9VDHjx//9a9/HRMTI2F/6NAhqcnNzZ00adI777xjPnXj5MYiNja2a9eu/fr1++EPf9i9e/fMzExrB4IfABAMwd8YyfVevXqVl5ffcsst//7v/64qx48ff8cdd9x555133333VVddJYk+YMCAoUOHrl+/XnUoKysrLCyUzX1xcXFJScmJEycGDhwoNweq9csvv6ytrS0tLX311VdVjWz6+/fv//e//10dZmVlLb6Q9l39Rx99VF7VokWLli1btnLlymuuuWbBggXWDhL8o0aNUt9RAADAiuBvTE1NjWR2QkJCnz59KisrtVbZo19xxRUS/J988onWZHXy5Mn27duvXr1aHcpDXXnllbLpl5sDVfPggw9K5dmzZ9Wh3EOkpKTEx8d37NgxxUd9Y0BZu3Ztq1atzF8juGfPnsjIyCNHjpgd6n3BL69KnnTQoEHz58+X+w9rKwDAywj+i5CNtYTo008/rdUvXLhQUn/OnDnSun37dq3VKiMjIzY29tSpU+pQtu+/+93vJM7V9/Zl3y9Bnp+ff8E5vp8X3HHHHVqleOihh+QBzcPRo0ffc889lvZvSfCPGTNmw4YNTz755A033NC1a9dQ/vshAMALCP7GHD58WDJ76tSpbdu23bFjh6r86quvRo0a1a5du8zMTAlU84f3DZIdeUxMTHp6ut7g+095L7/8suzXX3nlFb0tePDX1taa5TfffFNOD7zt0H7Gf/ToUUsjAMDTCP6gJNT/+Z//+d/+7d+k/Pjjj/fq1auioqK6uloKSUlJ5u/yM4L8/Z7KysoXXnhBUn/EiBHWtK73Rf7GjRtvv/12uZ94/fXXrU3y+Ed9ZsyYccstt6hy4Gfz5AHlwSX1n3nmGa2pPiD4AQAwEfxB/ed//mePHj3KysqkfObMmX/6p3/62c9+JuXPP/9cfedcQjclJUWC3/xmgCLhLdEb45OWlnbu3Dlr69q1a+Pj4yWzR44cuX//fmuTyMnJ8X8M4LyJEyda+8hZ/fr1a926dbBfDEDwAwCCIfgv3/bt22fOnGn+53yr559//o033jh58qTeUF9fWFg4d+7cw4cP6w0+VVVVhwOcOHHC2qeysnL8+PEFBQXWSqslS5ZkZWXptQAAEPwAAHgKwQ8AgIcQ/AAAeAjBDwCAhxD87lBSUtLI/+ZTvvnmm/Xr12dmZgZ+sh8AAIXgd4eoqKiFCxfqtRabN2+OjY01PwE4bNgw7WOEAADUey34JTv37t3b4OGWLVuWLVu2b98+s7Xe9/H93NzcVatWyYbbWt+g6urqjRs3Ll++vKioyFq5adMmeQTrL8xv5GVI+eDBgzt37szKysrOzla/wF8eU7J8zJgx0nrs2DHzRKtbb701JSVl//79VVVVGRkZ0v/dd9/VOwEAPM9bwS9xaN03m4ePPfaY2ihHRESYvxVHIrZv376qPiYmxvyruw06fvz4TTfdpDq3adNm7dq1UnnixIn+/furStmyq8r64C9DlRMTE9UpIjk5uaampmfPnmaN+cuC1KH5IPW+2xRVKC8vlybz6QAAMBH83x5GR0dPnjy5rKzstddekwhXrZMmTUpKSiosLNyzZ0+PHj0GDhxonhhIOsfGxn788cdyu3DXXXfJ7rze9/dz5Y4hPz9f7gCGDRsWFxcnkVwf/GWocseOHdetWycbd9n0y+GGDRsCT1E1WvArp0+fHjt2bHx8vHkhAACYCP5vDwcNGiRJuXLlSuvPxa+//vpx48Yt9Ln//vsjIyMb+Qv311133fTp01XZ3HlbKw8cOCBPl5ubWx/8Zajy7NmzVVn9BaBFixYFnhLMJ598kpiYeNttt/3tb3/T2wAAIPjVYWlp6ZQpU9q3b5+SkiI7ZtXaoUMHtas2HTx40DxXExUVNX/+/EYqKysr5RHUb9IN9jIaadLqG7RkyRJ5xvT0dO1vAgEAYPJW8EuWm38hV/05HJWmaiu/e/duqVm9erXqkJSUlJmZqcoSpcH+V51y8803Dx8+XJX37du3bds2KfTr12/EiBGqMjs7Wx5cfdAu2MuoDwj40IN/zZo1bdq0kWfRGwAAsPBW8A8ePLhbt24SutOnT5fNsUrTvLy8Ll26SM3kyZON8z9TF0uXLm3fvv3UqVPT0tIGDBggJzb4R3cU9fP4sWPHyoP36NEjMTHx3LlzsgWXyocffnju3Lldu3aVB6mrq6sP8jLU4wQLfuk2dOjQWbNmqT8MqJqM8z/jr6qqkktITk5eaPHWW2+ZjwMAgOKt4D98+PCQIUOio6MTEhJSU1NjYmIkIMvLyydMmNC5c+dOnTpNmzbN2l9ab7zxxnbt2qWkpGzdutXaFGjBggW9e/eW3fy9995rfqIvIyOjV69esbGxo0ePNr9n0ODLUE3Bgn/mzJnyyH369DE/+GcN/qNHj6pDK+lsPg4AAIq3gv87su6nFfNnAQAAuALBfwn0PbVhXH311XonAACaMYIfAAAPIfgBAPAQgh8AAA8h+AEA8BCCHwAADyH4AQDwEIIfAAAPaVHBHxcXp3/Q3uXkivSLdAQjCecx6wBntKjgl3eaeRUtg1xRRUVFZWXl6dOnz54969if3WMk4TxmHeAM/xQ1S3oX92iRC0dRUVFJSUlpaaksH7J26NccHowknMesA5zhn6JmSe/iHi1y4SgoKDh48GBxcbGsHbJv0K85PBhJOI9ZBzjDP0XNkt7FPVrkwpGfn79r1y5ZO2TfIJsG/ZrDg5GE85h1gDP8U9Qs6V3co0UuHDk5ObJ2yL6hqKiooqJCv+bwYCThPGYd4Az/FDVLehf3aJELx1tvvbVhw4YdO3bIpqG0tFS/5vBgJOE8Zh3gDP8UNUt6F/dg4bALI3kZysrKfv7zn+u1CBmzDnCGf4qaJb2Le7Bw2IWRvFSbN2+Oj4+XZ9EbEDJmHeAM/xQ1S3oX93B44di3b9+KFSv++Mc/njlzRm+zSVMtHE6OZGVl5bvvvvvmm29+9NFHept9wjeS8tV/4oknIiMjDR+9OTwWLly4aNGiuro6a2VeXp7U792711rpIk7OOlFWViazTt7FeoN9wjfrWrCSkpKCggK9NoDM8+XLl8vSwWclLoN/ipolvYt7OLZwyHNNmjRJLfQiISFB3tV6Jzs01cLh2Ehu2bIlNjbWHMlhw4bV1tbqnewQppHcvXt33759zddvOBX86rnee+89s0ZuAr73ve9JpWS/paObGE7NOrlZv++++9q1ayfP+Nprr+nN9jHCM+tatqioqMbnsEx1bfk9cOCA3gmN8k9Rs6R3cY9wLBxLly5dt26debhy5Uo5fOONN+S5nnvuOdk0fPjhhz179rz99tstJ9mmqRYOx0by1ltvTUlJ+etf/yq37S+99JI8ryzKlpNsY/tIyuozf/78tm3bmguQovcLD3mimJiYUaNGmTVyE9CqVatu3bpZF83q6upNmzatWrWquLjYrFy8eHFOTo55KLveP/3pT/W+b13k5uZKZ9lyma1OMpyadXLJY8eOnTNnjtFyg1/73o/1UO62ly1btm/fPrO1/hK/+jKvNm7cKBvuoqIia2XgZGvkZUhZxmTnzp1ZWVnZ2dnqtxvJY8qgjRkzRlqPHTtmnmglE1j6pKeny3hu27ZNLb96JzTKP0XNkt7FPcKxcPziF7+QxV1mmJQPHTokT5GWljZgwIBBgwaZff7whz9I/eeff+4/zSZNtXA4NpJSlvVCdaioqJDKt99+23qWXewdSVnvBg8e/G3OB9C7hoc80Z133tm6dWtzmR49erTMye7du5vBf+LEif79+6tXJbuotWvXqvrhw4fHxcWpdVa2StL64osvyiJrfutCbinkdlZ1dpLh4KwTMg2Mlhv8xoXf+zEPH3vsMfVVjoiIkK2Lar2kr/7x48dvuukm1blNmzZqXgWbbEaQl6HKiYmJ6hSRnJxcU1MjKW7WyKCZPQ3LO0stv+bh73//e2mVzYNZg4vyT1GzpHdxDyMMC8df/vIXediXX35Zyk899ZQsIjLv5b3x7LPPmn3kbSN93nnnHf9pNjGaaOFwbCTNVtlwyCYsPj5eVhD/OfaxcSRl12j98YRG7x0ehu8bThL8qampcvjVV1/JEixj2759e3NhffTRR2Wi5ufny5AOGzZMwr68vFzq169fL6erXf7s2bPlCyEdJk2alJSUVFhYuGfPnh49egwcONDybA4xnJ113gz+6OjoyZMnl5WVyYXLUKjWS/rqS2eZ/x9//LGse3fddZfszuuDT7ZgL0OVO3bsuG7duqqqKtn0y6EMVOApqsawvLPkiZ555hnzUCa/4dswmDW4KP8UNUt6F/cIx8Ih5O5Sbofl8eVuVMJJamT5eOmll8wOsmeVp87MzPSfY5OmWjgcG0nl008/lXv/2267rbi42NLdTjaOZOPBf0luuOEG/dFDY/gS66c//WlCQkJdXZ3sYiX4ZR03LIvmddddN336dFVWO/vc3Fwpnzt37tprr5Xxl/IPfvCDhx56SArXX3/9uHHjFvrcf//9kZGRMqv//8kuhVyRdo2XRP+y2SHYrPNm8MtoyO21zGGZBmbrJX31rfNK7tcDK62TLdjLUGW571Rl2evL4aJFiwJPCSTLb0ZGhnkor0FOWbZsmaULLsI/Rc2S3sU9wrRwqB3SggULDN8v4JQaWW1/85vfmB3URH/vvff859ikqRYOx0byH76fwkZFRcn+VQLswu52snckm8O3+mVx3LhxoxTy8vK+//3vq18hoOpVHxnV+fPnq3JlZaU0yb5KHc6YMUN2frJpk8pNmzZJTYcOHS64DMOQUVKdHWM4OOv+4dXgl9cwZcqU9u3bp6SkmP8f/pK++tZ51WCldbIFexmNNGn1gdTyax5+8cUXcoq8FyxdcBH+KWqW9C7uYYRn4aj37WO6du0q+wZV88tf/lL2TKdOnVKHTz31lLxzKioq/OfYxGiihcOxkVy7dq1sVXNyci7saD/bR7LJ/3OfLI7yGnr16jVmzBg5fP/998161adfv34jRoxQ5ezsbGnavn27OiwsLIyIiEhOTpbT1WcCk5KSMjMzVWttbW2w/1cVVoZTs05p2cEvK1J6eroqy/vLnBhqK797926pWb16tepwSV/9m2++efjw4aq8b9++bdu21QefbMFeRn1AwJuHWn0gtfyaf/hALb/qJwsIkX+KmiW9i3uEaeEQr7zyijz466+/rg4LCgratWsn7xaZ05MmTYqMjJw+ffqFZ9ijqRYOZ0ZSNhxdunSR+HnNYtWqVfo5dgjTSDbhx/nU4jhv3rxWrVr16dNHqxdLliyRw4cffnju3LkSewMGDLB+7v/uu++WVmlSh0uXLpVd4NSpU9X/Xe3WrdvJkyfNzs4wHJl1ppYd/IMHD5YvoixQsjTJdlxNjLy8PHnHSc3kyZON8z9Tr7/Er776efzYsWPlwXv06JGYmHju3Llgk63Bl6Eex1q2Hkq3oUOHzpo1q6amxmwyLO+sPXv2qOVXXq25/JqtCIV/ipolvYt7hG/h+K//+q+YmBi5xzRrZIMliSUbvu7du8stp0x9S3fbNNXC4cxIlpSUqLe0lWSYfo4djLCNZJP8Ah/j/CopYyiL4IsvvqjVKxkZGbKnj42NHT16tLaNkxssuWPQPnl14403yqOlpKRs3brV0tchhiOzztSyg//w4cNDhgyJjo5OSEhITU2Vy5evr2yLJ0yY0Llz506dOk2bNs3a/5K++gsWLOjdu7fss++9917zE30NTrYGX4Zq0uaqeThz5kx5ZFkHzA/+Bb6ztmzZYl1+zVsEhMg/Rc2S3sU9wrFwHDlyZM6cOW3atHn88cf1tvBrqoWDkbxUDv/K3pycHOtHqC9a7wrMuuZjYQDzZwFoAfxT1CzpXdwjHAuH3LFGRET85Cc/kZtlvS38mmrhYCQvA3+k5zti1jUfvj32Ba6++mq9E1zLP0XNkt7FPYwwLBzi7NmzepVTjCZaOBhJOI9ZBzjDP0XNkt7FPcK0cDShplo4GEk4j1kHOMM/Rc2S3sU9WDjswkjCecw6wBn+KWqW9C7uwcJhF0YSzmPWAc7wT1GzpHdxDxYOuzCScB6zDnCGf4qaJb2Le7Bw2IWRhPOYdYAz/FPULOld3IOFwy6MJJzHrAOc4Z+iZknv4h5xcXFGyxIVFdUkCwcjCecx6wBntKjgFxUVFUVFRQUFBfn5+Tk5OW/ZxPDduTcJuQq5FrkiuS65Ov2Cw4aRhPOYdYADWlrwV1ZWlpSUyM31rl275P22wSaG7w9aNAm5CrkWuSK5LvMPUjmAkYTzmHWAA1pa8J8+fbq0tLS4uFjeaXKXvcMmsnDoVU6Rq5BrkSuS6zL/frYDGEk4j1kHOKClBf/Zs2fltlreY3J/XVRUdNAmsnDoVU6Rq5BrkSuS65Kr0y84bBhJOI9ZBzigpQV/bW2tvLvkzlreZhUVFaU2kYVDr3KKXIVci1yRXJdcnX7BYcNIwnnMOsABLS34w8Rw6s+ttniMJJzHrAOsCP6QsHDYhZGE85h1gBXBHxIWDrswknAesw6wIvhDwsJhF0YSzmPWAVYEf0hYOOzCSMJ5zDrAiuAPCQuHXRhJOI9ZB1gR/CFh4bALIwnnMesAK4I/JCwcdmEk4TxmHWBF8IeEhcMujCScx6wDrAj+kLBw2IWRhPOYdYAVwR8SFg67MJJwHrMOsCL4Q8LCYRdGEs5j1gFWBH9IWDjswkjCecw6wIrgDwkLh10YSTiPWQdYEfwhYeGwCyMJ5zHrACuCPyQsHHZhJOGAvn37GkFIk94b8BiCPyQGcWUTRhIOSE9P1wP/PGnSewMeQ/CHxCCubMJIwgFFRUWRkZF65huGVEqT3hvwGII/JAZxZRNGEs4YNGiQlvpCKvV+gPcQ/CExiCubMJJwxuLFi/XYNwyp1PsB3kPwh8QgrmzCSMIZZWVlbdu2taa+HEql3g/wHoI/JMSVXRhJOGbkyJHW4JdDvQfgSQR/SCIiIqwrCC5bXFycPrhAeKxZs8Y69+RQ7wF4EsEfEoN9KuA2Z86c6dy5s0p9Kcih3gPwJII/JAQ/4EaPPPKICn4p6G2AVxH8ISH4ATfasmWLCn4p6G2AVxH8ISH4ATeqq6uL95GC3gZ4FcEfEoIfcKknffRawMMI/pAQ/IBL7fbRawEPI/hDQvADAFoGgj8kBD/gHTU1Neb/CbCWgZaB4A8JwQ94h7zfFy5cGFhuRElJSUFBgV4LNEsEf0gIfsA7LiP4o6KiQukGNAcEf0gIfsClJI8PHjy4c+fOrKys7Ozss2fPmvV79+61djMPGwl+KX/xxRebN29esWLFoUOHVOXy5cul25gxY6T12LFjqlthYeGOHTteeeUV81ygmSD4Q0LwAy4lb97ExETjvOTk5JqaGlVvTfRgYR/Y7dprr1UP1aZNm5UrV0plz549zceXsFfdpk2bFhER8cADD5jnAs0EwR8Sg+AH3EnevB07dly3bl1VVZVs+uVww4YNqv7ygv+qq6764IMPysvLx48fHxsb+/XXXzfY7Zprrtm6dWt1dbVZCTQTBH9ICH7ApeTNO3v2bFWWvb4cLlq0SNVfXvCnpaWp8pEjR+QwNze3wW4TJ040D4FmheAPCcEPuFRgJKvDYPWNlLXDyspKOczKymqw26uvvmoeAs0KwR8Sgh9wqcBIVocdOnRIT09XlTk5OcHCPvD0xx9/XJWzs7PlcPv27Q12sx4CzQrBHxKCH3CpYJE8ePDgbt26SfZPnz49KioqWNgHnh4RETFhwoR58+bJ6T/+8Y/Vr/eRRxg6dOisWbMa/J+DQLNC8IeE4AdcKjC51eHhw4eHDBkSHR2dkJCQmpoaExPTYNgHni4BL6fIiffdd9+RI0dU/cyZMzt06NCnTx/1mUCCH80ZwR8Sgh9APYmOFoHgDwnBD6Ce4EeLQPA3rG/fvkYQ0qT3BuANEydO3Lp1q14LuArB37D09HQ98M8z/ycwAACuQ/A3rKioKDIyUs98w5BKadJ7AwDgEgR/UIMGDdJj3zCkUu8HAIB7EPxBLV68WI99w5BKvR8AAO5B8AdVVlbWtm1ba+rLoVTq/QAAcA+CvzEjR460Br8c6j0AAHAVgr8xa9assQa/HOo9AABwFYK/MWfOnOncubNKfSnIod4DAABXIfgv4pFHHlHBLwW9DQAAtyH4L2LLli0q+KWgtwEA4DYE/0XU1dXF+6g/vgkAgKsR/Bf3pI9eCwCACxH8F7fbR68FAMCFCH4AADyE4AcAwEMI/stXW1t79OjRmpoavSHAtGnTnnvuOb3Wp6io6Pnnn7+k3xBw4sSJ0tJSvfa88vLyiooKvRYAAB+CP6iPP/7Y+hG+Q4cOrVu37ty5c2bNsWPHDMP47LPPzBrx9ddf79+/f+/evQUFBXv27Nm1a1dWVpb6QKBkfFVV1ZAhQ5YuXVpdXS2d5b6hS5cuPXv2HDt2rPVBGvfEE08kJyercuBnDeShxo0bp1UCAKAQ/EH97//+7xVXXPH+++/X+36FX2Ji4pQpUySz09PT09LSUlNTZ8yYIXH+q1/96umnn/7www/VWfPmzVMxr8nLy5PW48eP//rXv46JiZGwlzsJqcnNzZ00adI777xjeebGyI1FbGxs165d+/Xr98Mf/rB79+6ZmZnWDgQ/AKARBH9jnnzyyd69e586deq3v/2tBP/p06fHjx9/xx133HnnnXffffdVV10liT5gwIChQ4euX79enVJWVlZYWCib++Li4pKSkhMnTgwcOFBuDlTrl19+WVtbW1pa+uqrr6oa2fT379//73//uzrMyspafCHtu/qPPvpor169Fi1atGzZspUrV15zzTULFiywdpDgHzVqlPqOAgAAGoK/MRKfSUlJDzzwQPv27bVv6cse/YorrpDg/+STT6z1mpMnT8q5q1evVod9+vS58sorZdMvNweq5sEHH5TKs2fPqkO5h0hJSYmPj+/YsWOKj/rGgLJ27dpWrVqZP4DYs2dPZGTkkSNHzA71vuCXVyVPOmjQoPnz58v9h7UVAOBxBP9F7N69W3L02WeftVYuXLhQUn/OnDnStH37dmuTJiMjIzY29tSpU+pQtu+/+93vJM7V9/Zl3y9Bnp+ff8E5vp8X3HHHHVqleOihh+QBzcPRo0ffc889lvZvSfCPGTNmw4YNTz755A033NC1a9dQ/vshAMAjCP6Lk3R/++23Vfmrr74aNWpUu3btMjMzJVDNH943SHbkMTEx6enpeoPvP+W9/PLLsl9/5ZVX9LbgwV9bW2uW33zzTTk98LZD+xn/0aNHLY0AAK8j+C/ODP7q6upevXolJSWZv8jPCPLHeyorK1944QVJ/REjRljTut4X+Rs3brz99tvbtm37+uuvW5vk8Y/6zJgx45ZbblHlwM/myQPKg0vqP/PMM1pTfUDwAwBgRfBfnHXH//nnn6vvnEvopqSkSNOOHTusnSW8JXpjfNLS0qwf/6v3/ZA+Pj5eMnvkyJH79++3NomcnJz//wyAxcSJE6195Kx+/fq1bt062C8GIPgBAI0g+C/uwIEDsoPXKrdv3z5z5kzzP+dbPf/882+88cbJkyf1hvr6wsLCuXPnHj58WG/wqaqqOhzgxIkT1j7ySsaPH19QUGCttFqyZElWVpZeCwCAD8EPAICHEPwAAHgIwQ8AgIcQ/AAAeAjBDwCAhxD8AAB4CMEPAICHEPwAAHgIwQ8AgIcQ/AAAeAjBDwCAhxD8AAB4CMEPAICHEPwAAHgIwQ8AgIcQ/AAAeAjBDwCAhxD8AAB4CMEPAICHEPwAAHgIwQ8AgIcQ/AAAeAjBDwCAhxD8AAB4CMEPAICHEPwAAHgIwQ8AgIc0EPwAAKDFI/gBAPAQgh8AAA/5PxzvFUXYISX6AAAAAElFTkSuQmCC" /></p>


上記の続きを以下に示し、ステップ4とする。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 79

    }  // この次の行で、x0、x2、y0、y2はスコープアウトし、X、Yオブジェクトは解放される

    ASSERT_EQ(X::constructed_counter, 0);  // Xオブジェクトの解放の確認
    ASSERT_EQ(Y::constructed_counter, 0);  // Yオブジェクトの解放の確認
```

<!-- pu:deep/plant_uml/shared_each_4.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAjAAAADuCAIAAACoOKpOAAAvUElEQVR4Xu2debxN1fvHD4lyTRVlKlRSSOobDZIhJCmlNKdJLhEKzUnkUmkwFs1IkyRlaCA00EVkKmNRkUyVZMr5/d7Oet1l333OPvfc6xzn2D7vP3rtvdbaw3r23p/P8+yzrwL/J4QQQqQAAXeDEEIIkQxkSEIIIVKCfYYUFEIIIQ44MiQhhBApgQxJCCFESiBDEkIIkRLIkIQQQqQEMiQhhBApgQxJCCFESiBDEkIIkRLIkIQQQqQEMiQhhBApgQxJCCFESiBDEkIIkRLIkIQQQqQEMiQhhBApgQxJCCFESiBDEkIIkRLIkIQQQqQEMiQhhBApgQxJCCFESiBDEkIIkRLIkIQQQqQEMiQhhBApgQxJCCFESiBDEkIIkRLIkIQQQqQEMiQhhBApgQxJCCFESiBDygurVq2qVavWww8/7O4QQgiRV3xiSDt27BjrYMyYMTNnzrS9v/7662NhLFu2zLGDaGzcuHHJkiWLFi1auHDhggUL5s+fz+ZNmzYtV66cHbNlyxaOu337dsd2QgghcoFPDAnPKF68eIkSJUqVKlW+fPmiRYuWLVt2z549phfvuTSMOXPmZN/HXjA2d1MwmJGREQijWLFiEydONAM4UIsWLQoWLLh27drsmwohhIgVnxiSk927d5900klPPPGEbVniwV9//WXHzJo1KzMzEzPD21i99tprn3rqKdO1efPmlStXrl69mkpr3bp1GzZsqFu3bnp6ut22d+/e7du3P/zww2VIQgiRZ3xoSMOGDUtLSzO+Art27XJXN1mMHj3ajFm+fDl2Mnbs2IoVK3br1o2WChUq9OvXz+7TydatWwsXLjxq1Ciz+tlnn1WrVm3Lli3sUIYkhBB5xm+GNG/ePNzCmIplbRaUMqVLl7ar//77rx3TqVOnmjVrvvLKK61bt6Zyypcv3/jx4x372MfgwYOLFCliqqtffvkF61qwYIGxPRmSEELkGV8Z0pw5c8qWLVupUiUqpEmTJrm7g8EuXbqcffbZ7tYQP/3005AhQ3bv3s1y3759CxYsuGnTJvegYHDRokUlSpR47LHHzOpNN92E/50UAkNq1KgRjph9CyGEEDHhE0P677//hg8fjjc0bdp027ZtVEKHH364y5O+++67Y445hi5no4vt27fjRvnz5+/Zs6er659//nnuueeKFy/erFkz6iHTOGPGjNEhRo0ahSG98MIL69aty76dEEKImPCDIW3evPmss84qUKBAjx49TIkD3bp1o07KzMwMhrykRYsW2Mzll1+OXWXb2EHXrl1LlSp15JFH9unTx9mO/dxyyy1YUdGiRfEz60auMXplJ4QQ+4MfDAkGDRq0ePFiZ8uePXvwJ+sQ1E+ffvqpc0A4VDnPP//8+vXr3R3BYP/+/dnDn3/+6e4QQggRJ3xiSEIIIQ52ZEhCCCFSAhmSEEKIlECGJIQQIiWQIQkhhEgJZEhCCCFSAhmSEEKIlECGJIQQIiWQIQkhhEgJ/GlIjz32mPN/M2H/LdSDt/cA81iIKOdzMPYKIVIcfxqS2E9Qc3fTQY7MSYjUx1eGJNGJF/4zJP/NSAj/4StD8p/oJMti/RdJ/81ICP8hQ0ppkjWjZB03cfhvRkL4DxlSSpOsGSWrMkscyYqkECJ2ZEgpjf9mlCz8Z7FC+A9fGZL/REeGJIQ4dPCVIfkP/1ms8AHLli3bvHmzu/WQJyMjY8KECe7WLP7555/x48e7W2Ng586d7qb4sSfE7Nmzd+zY8d9///37779r1qxxDzqAyJDyzqJFi0aOHMlNxlV094mY+fvvvz/88MPXX3995syZ7j6xf+zatcvdFGLLli0ff/wxN7C7IwtEau7cuUuXLnV3BINjx4498sgjR4wYsXHjxubNm3/zzTe2q0uXLjeGGDJkyEnZsVr8008/lStXLjMz024VC9u3b//999+5VVieMWPGzz//7Bowb94812R//PFHTvXdd98dPXr0G2+8wX9t1/Tp09977z27yvP71ltvzZ8/37ZY+vfvf+aZZ7pbI/Hqq68GQqxatYrVAQMGTJ061fa+9tprJ5988tFHH/3iiy/axlhYvXp18eLFP/30U3dHFp999hnx3LRpk7vDAU6zbt26iGNatWr19ttvH3bYYT169LjgggsmTZp0xBFHYE7OMRs2bOB6HZgURIaUF3hc27VrZ+4/qFSpEjmje9DBzAGrzKZMmVKiRAkbycsuu2z37t3uQSJPNGjQAJ11twaDKGbZsmWJdr58+V5++WV3dzD4559/Nm3atHbt2kZbLeTOV199NRvWrFnz8ccf79ChA1qJfiH6ZkCFChXS09P/97//de/eHcVH5gYPHoyYHnPMMWPGjDFjcEH2MGfOnH37dcCTddttt1155ZUNGzZkP5UrVz722GMLFSpkbg+kkzGNGjW6/vrrnVtxnvQ6DQB69+59+OGHc4annHJK4cKF8+fPb20MS+Pchg0bZla7du3KTWh6Ue1ff/2VmWKcK1euvPfee0uWLIkxL1myBBc34ydOnHjiiSdWrFiR+R5//PH4QZkyZdLS0jiHhx56KBiqac444wxWa9So8cEHHwRDnle/fn3OvG3btmYnMXL//fezH+LJI4lnEN7169c7B+D0DPjjjz+cjRbO+e677z7qqKNMAMkMXnjhBdvLrurUqVOrVi2Cc/rpp1977bXt27cvX778syFsPJkOIWKaX3/9td02QciQcuCdd9555ZVXeE5Y/uuvv4YOHfrVV18NHz6cq9uvXz9uXy4S9+WFF17o3vJgJpCA364iRpKk7JxzzuFp37Zt23PPPcdx8/ZaI0fibrFk3Fbg7DJJ+uTJk7/99lszTQOpPeXIL7/8YlvCQVA++uijH374wdlICYL2kenblogHZYGdf/nllwwmsKb3888/J5idOnVit3Zzw6233oowIbuoD1YRXkVdfvnlyBO25GqnhuBiNW7cuECBAsgx+shFfPTRR7EQM4AHgXOgQmrZsiUjUTpCgV0xnmttxnz33XecGFd8336zc91117Vp0+aRRx4ZNGhQ3bp1qSpeeuklappZs2YZSzj33HM5c9dWp556ardu3VyNwVBx8OCDDx533HGuIgPnKFasGPUHFR5ybOsn5m60OxyKQjPm+++/v++++9gtJ8l9hTdjfswRt9h3gFCyxe398MMPm9XFixdTODoH5Mhvv/2GlZI9VK1alUKNeHIaTkcJRjUk7h825EpxXPIG5tirVy/cvXPnzmYAt1aLFi0IDnvAtql3cdZq1aoRdlqef/55596YL95MxJyNccdXhhR30YFRo0ZxbXAglsk1yIOWL19+/vnnk+/YMTxyjHGpyUFNIAGGFDGSwdDbGDMAuWHA+++/79wqXsR9RuzQqphdpsIz4kX1YLoyMzNNCch8vRJMxpgclpLFpu3z5s0rVaqUaezfv79pjHhQFshezXFxGqydxnr16tkWMyaQFQGSevOkoEc0IvSm3YCM0jh79mxnI7zxxhvFs6C8MMWH5dJLLw2GDIl29J0SB4fAnBBuBlMo2NfaM2fOZP/h79zCGTBg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zZFLNmHDZs2arVmzxrT36NGDQqFKlSrmi2dfymh4KBRJIUSMyJDij/QxXiiSQhxSyJDij2Q0XiiSQhxSyJDiT3p6+vTp092tIvcokkIcUsiQhBBCpAQyJCGEECmBDEkIIURKIEMSQgiREsiQhBBCpAQyJCGEECmBrwzpsRABB6y6Bhx0vUkn+ukdLL2uAUKIFMRXhoT0uJsOcpIlo8k6buLw370hhP+QIaU0yZpRso6bOPw3IyH8hwwppUnWjJJ13MThvxkJ4T9kSClNsmaUrOMmDv/NSAj/4StD0i8f8SJZx00c/rs3hPAfvjIk/5EsGU3WcYUQhzIyJCGEECmBDEkIkQN79uz5+++/3a0iEi+++OKyZcvcrdnZvn374sWL3a0pxs6dO3ft2mWWOeHsnYlChpR3Fi1aNHLkyPHjx//777/uPhEzKN2HH374+uuvz5w5090n9hu8ZMaMGe++++4ff/zh7osNxKhVq1bly5f/888/f/jhh969e+/evds5gJ0PDPHSSy89//zz12bnu+++syPvuOOOZ5991rFpXti0aZO7KYTrrFjdsmULs/7tt99Wr179448//v7776aLxldffXXWrFl2MDchLdOmTbMtTm688cYYT/v+++8PBALHHXfcunXrTMv8+fNXrFjhHNOxY8cWLVoUK1bs22+/dbbHQocOHbp16+ZuDePKK6987bXX3K0x88wzzwwdOvTiiy9+6KGHrrrqqsmTJ99+++1cSve4BOArQzpgv3zwkLdr1y6QRaVKlXLMiUREpkyZUqJECRvJyy67zCUr8eKA3RsHHtLY9evXu1tD7Nixo0mTJia2KOA333zjHpEFAtqsWbMzzjhj4cKFzvbPP//8zDPPLFiw4IgRI7766quuXbuyK0Y6C6ZzzjmnYsWKp5122jHHHENiUa9evSOPPLJz58533XUXgz/55BM7sly5cjw4dtXFxIkTOcqgQYOeeOKJ++67Lz09/brrruNYderUqV69+hdffGGGIY7VqlXLvmnwlVdeKVmypDM15Lj2vjKcffbZpovn96KLLuJsrUl36tSJOTq900nZsmVvueUWZwsmhze0b9+ek2zbtm2bNm04q9tuu61y5coc6NRTT8ULzcgLL7wwX758l1xyyZdffmla3nrrLY5Vu3btxo0b79tjDHCVCxUqhENwjfC5uXPncnXcg0Iw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" /></p>


このような動作により、`std::make_shared<>`で生成されたX、Yオブジェクトは解放される。

次にshare_ptrを使用し、循環する参照を作ったためにオブジェクトが解放されないコード例を示す。
まずはクラスの定義から。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 91

    class Y;
    class X final {
    public:
        explicit X() noexcept { ++constructed_counter; }
        ~X() { --constructed_counter; }

        void Register(std::shared_ptr<Y> y) { y_ = y; }

        std::shared_ptr<Y> const& ref_y() const noexcept { return y_; }

        bool DoSomething() { return true; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<Y> y_{};
    };
    uint32_t X::constructed_counter;

    class Y final {
    public:
        explicit Y() noexcept { ++constructed_counter; }
        ~Y() { --constructed_counter; }

        void Register(std::shared_ptr<X> x) { x_ = x; }

        std::shared_ptr<X> const& ref_x() const noexcept { return x_; }

        bool DoSomething() { return x_ ? x_->DoSomething() : false; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<X> x_{};
    };
    uint32_t Y::constructed_counter;
```

上記のクラスの動作を以下に示したコードで示す。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 134

    {
        ASSERT_EQ(X::constructed_counter, 0);
        ASSERT_EQ(Y::constructed_counter, 0);

        auto x0 = std::make_shared<X>();

        ASSERT_EQ(x0.use_count(), 1);
        ASSERT_EQ(x0->ref_y().use_count(), 0);  // X::y_は何も管理していない

        ASSERT_EQ(X::constructed_counter, 1);  // Xオブジェクトは1つ生成された
```

x0のライフタイムに差を作るために新しいスコープを導入し、そのスコープ内で、y0を生成し、
X::Register`、`Y::Register`を用いて、循環を作ってしまう例(メモリーリークを起こすバグ)を示す。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 147

        {
            auto y0 = std::make_shared<Y>();

            ASSERT_EQ(Y::constructed_counter, 1);  // Yオブジェクトは1つ生成された
            ASSERT_EQ(y0.use_count(), 1);
            ASSERT_EQ(y0->ref_x().use_count(), 0);  // Y::x_は何も管理していない

            ASSERT_FALSE(y0->DoSomething());  // Y::DoSomethingの処理をX::DoSomethingに委譲

            x0->Register(y0);  // これによりx0とy0が互いに所有し合う(循環参照)
            y0->Register(x0);  // これによりx0とy0が互いに所有し合う(循環参照)
            ASSERT_EQ(X::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない
            ASSERT_EQ(Y::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない

            ASSERT_TRUE(y0->DoSomething());  // Y::DoSomethingの処理をX::DoSomethingに委譲
```

<!-- pu:deep/plant_uml/shared_cyclic.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAD8CAIAAACw6lscAAAeOklEQVR4Xu3de2wVVeIH8KEoBQu1BUHFViwESYhbqqFhKQoVeWhcjRBxBXZNFFBE5CGubIIi8mohkAqN5WUfVhtkpQKyFNAFViwQILKFCw0LFFOsFCj0QWlLS9vf77v3LGemp9PrmO2dub33+/mDnDnnzMy5lznfOdPbh/Z/RETNaGoFERGjgYhM6dHQSEQBj9FARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkgtFARCYYDURkInCjYfz48aWlpWotEbkFbjRomhYZGblnzx61gYgCPBogKChozpw5NTU1ajNRYAv0aBCio6OPHz+u9iAKYIyG/woODl6xYkVDQ4PajyggMRqaGD58eGFhodqVKPAwGlRhYWFZWVlqb6IA43PR0K1bN3Wy2ss0GhwfVavDK1JeI5GRz0UDrlq1yjvUueLW0gMFmuT74x/wisrLyysrK6urq2tra+vr69XXTIFNv1RkSe1iL82haPD8ZUi/jAaEYHFx8bVr1xAQSAf1NVNg0y8VWVK72MuRaPjVDy/9MhpcLtfZs2eLioqQDlg7qK+ZApt+qciS2sVeNkeDxW958stoyM3NzcvLQzpg7YCFg/qaKbDpl4osqV3sZWc0WP9Gab+MhpycHKQD1g54sigvL1dfMwU2/VKRJbWLvWyLht/041V+GQ0bN27ctWvXkSNHsHDAM4X6mimw6ZeKLKld7GVbNPwmjAYKNPqlIktqF3sxGuzBaCDP9EtFltQu9mI0wKlTp7744ovt27fX1NSoba2E0eCI4uJil8ul1hpcv35927ZtGRkZhw4dUtvspV8qsqR2sVeARwPONXXqVO22qKgozFu1U2tgNDgiJCQkJSVFrb1tz549YWFh8n//ueeeu3XrltrJLvqlIktqF3tpARMNf/vb39LS0hrd/we4V6xZs+bAgQMbNmzAuZYtW1ZaWnrw4MFevXoNHTpU3bM12B8NqampW7ZskZtYFhk3fxPMrpMnT5pu7t27Nz09Hcsu2QpYfO3cufPLL7/ETdtY39zNmzd37979+eefK98Ui/rvvvsORygq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" /></p>

下記のコードでは、y0がスコープアウトするが、そのタイミングでは、x0はまだ健在であるため、
Yオブジェクトの参照カウントは1になる(x0::y_が存在するため0にならない)。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 165

            ASSERT_EQ(x0.use_count(), 2);  // x0、y0が相互に参照するので参照カウントが2に
            ASSERT_EQ(y0->ref_x().use_count(), 2);
            ASSERT_EQ(y0.use_count(), 2);  // x0、y0が相互に参照するので参照カウントが2に
            ASSERT_EQ(x0->ref_y().use_count(), 2);
        }  //ここでy0がスコープアウトする

        ASSERT_EQ(x0->ref_y().use_count(), 1);  // y0がスコープアウトしたため、
                                                // Yオブジェクトの参照カウントが減った
```

<!-- pu:deep/plant_uml/shared_cyclic_2.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAAD8CAIAAADVB6ljAAAgkklEQVR4Xu3de3RNV+IH8CseiVcERT1Cxag1po3HyKRiSqi3MmXoeMx0rXoVVY9q6VTReiVMjGKJZ4hoRpV4jpC2oggGi0FQRWJFU0EkEhHPJL/ft3ePk5N9c69zSM65ufl+/rDO2Xufc/a9uft79743ciz/R0Skk0UuICJ6GgYHEemWHxx5REQOMTiISDcGBxHpxuAgIt0YHESkG4ODiHRjcBCRbgwOItKNwUFEujE4iEg3BgcR6cbgICLdGBxEpBuDg4h0Y3AQkW4MDiLSjcFBRLoxOIhINwYHEenG4CAi3RgcRKQbg4OIdGNwEJFuDA4i0o3BQUS6ld7gGDRoUHp6ulxKRBqU3uCwWCze3t579+6VK4joaUp1cICbm9ukSZPu378vVxORfaU9OARfX9/Tp0/LLYjIDgbH/7i7u4eEhOTm5srtiMgGg6OATp06JSUlyU2JqCAGh8zLyysyMlJuTUQqThccNWvWlIeysQoNDtN7VeTwiKTHSKSd0wUHXtNyUfGQR5KVvaUKqpTnxzXgEWVkZGRlZd27d+/hw4c5OTnyYyayL/+FpGzJTYxlMSk4HH846pLBgYhMSUlJS0tDfCA75MdMZF/+C0nZkpsYy5TgeOrXsS4ZHPHx8ZcuXUpOTkZ2YN4hP2Yi+/JfSMqW3MRYBgeHxl8Ac8ngiIuLO3XqFLID8w5MOuTHTGRf/gtJ2ZKbGMvI4ND+K+cuGRzR0dHIDsw7sGbJyMiQHzORffkvJGVLbmIsw4JD139yc8ng2LBhw549e44dO4ZJB1Yr8mMmsi//haRsyU2MZVhw6MLgIFLLfyEpW3ITYzE4jMHgoOeR/0JStuQmxmJwwLlz57766qudO3fev39frisiDA5TpKSkxMfHy6UF4WcRHh5+9uxZucKZ5L+QlC25ibFKeXDgWqNGjbI80bhxY4xquVFRYHCYonLlyqGhoXLpEzt27OjZs6eHhwd+Og6aOYP8F5KyJTcxVukJjm+++WbNmjV51p/BnTt3li1bdujQoVWrVuFa8+bNS09PP3z4cKNGjdq3by8fWRSMD46wsLCtW7cqu5hSqXd1waBSvyGrd2NjY9euXYspm1ILmLjt3r3766+/xhu+utzWgwcPYmJi1q9fL/0CMcq/++47nCE5OVkpdNANbONZPXHiRERExK5du8Tv1+G0eNoHDx6M2hs3bigHKjDRGDJkyMyZMxkcupWe4IiMjMRpkRTY/uCDD/BedPny5YCAgMDAQKXNpk2b0ObChQv5hxUR44PjnXfecXd3v3XrFrZxRXRg7ty5cqMnfp1uqV4JtrvqcaXs4mkULcuUKYPwFbUYor6+vqLc09MTcawcKLl582arVq1EywoVKkRFRYny1NTUNm3aiHL8mJRyi51uiO3mzZuLQ8DPz+/Ro0d4G1BK8LSLZhabF/zFixctDA69bJ9HZ2AphuCAt956q0aNGv/+97/d3NyWLFmCEryyP//8c6UBXvS4NN6Z848pIhbDg+PkyZO46Jdffontzz77DCFS6LuuII0o291CR2yVKlXGjh2LyRqmb0gBUYulX4sWLRISEs6cOdOgQYN27dopB0rQ0svL6+jRo+jYG2+8gamBKB8zZgx+LnFxcUiQ3r1716xZ8/bt23n2uyG2q1atum3btuzsbEw6sIunutBD1I9LYHA8C9vn0RlYiic4rl+/jlchUqNDhw551h8GhhOGltIAM2RcGjPY/GOKiMXw4ABMpvDmn5ubi/dezMnlas1sh5/Yxfm9vb0xlXv8+LFS+9JLLw0bNizUqlevXni28awqtWoNGzb86KOPxLb6l4nV5WJUY+GTZ78bYhsrDrGNuQZ2V6xYYXtIoRgcz6JUBQd06dIFJ58zZ47Ybdy48YcffqjUitfQt99+q5QUFVOCA+/AuO7ixYvx78GDB+VqzeyNWDyKcePGVaxY0d/fX/nfN5UqVbIUhMerHKuGZUhISIhcWrA8KysLZ8AkIs9+NxxUSeWFYnA8C0tpCg5MJXBmTJ7xWsfLBSVDhw6tX7/+3bt3RQNM6fG6z8jIKHBYUbCYERyYazRt2rR27dqYd8h1euA5CQ4OFtvR0dHKMBNTidOnT6Nk48aNogHWKXiexXZOTo6D9VHr1q379Okjts+dO3fo0CGx3bJly759+4rtXbt24eRHjhzJs9+NPJuAYHAUu9ITHFevXq1WrdqgQYMyMzPr1auH+MC4io+P9/DwwGsdr0gsuTGvxiRZPrIomBIcsGjRIlx62bJlckVBFit7u506dXrxxRfxFOHJwXRADLMDBw7UqlULJWPHjrU8+UwB1qxZg1weP358UFBQQEAADsQTrpxKTXwYgTUUztygQYPmzZuLJU9YWBjK33333dmzZyP1cBLx5xcK7YY4lXpbvYtm3bp1++KLL7B+EeXqxyUwOJ6F7fPoDCxFHRw4Z+fOnb28vK5fv47dLVu24BILFizA9r59+/z8/Nzd3ZEmmHHgtSsfXBQsJgXH5MmTPT0979y5I1cUJI0oaTcxMbFr165VqlTByg6rPJwQw+z27dsjR46sXr064njixIlK4zzrl6Mvv/wyEhlLmP3796urJEuWLGnSpAmmEj169FB/I7tw4UIfHx/8vAYMGKDMWQrthqiSRr6yO336dJy8WbNm4otb6XEJDI5nYfs8OgNLUQeH6SyGBwfG4cyZMytUqDBhwgRREmpDWVMUK/mqRl3XleS/kJQtuYmxGBzGMD44EhISypQp06VLF+U/JYv3W7U6deoUPKhYyFc16rquJP+FpGzJTYxlYXAYwmJ4cOQ9+fCSXED+C0nZkpsYi8FhDFOCg1xG/gtJ2ZKbGIvBYQwGBz2P/BeSsiU3MRaDwxgMDnoe+S8kZUtuYiwGhzEYHPQ88l9IypbcxFgMDmMwOOh55L+QlC25ibEYHMZgcNDzyH8hKVtyE2M5Z3CULVvW4loqV67M4KBnxuDQxGK902pSUlJ8fHxcXFx0dPQGQ1is84Jiwvuq0DNjcGiCXmVlZaWkpODN+dSpUxhvewxhsf5nrWLCO7nRM2NwaIJe3bt3D/P55ORkjDS8Sx8zhMX6N+aKCe8dS8+MwaEJevXw4UO8LWOM4f0Zc/tLhrBY/+pMMeHd6umZMTg0Qa9ycnIwuvDOjGGWkZGRZghcVy4qOngUeCx4RHhceHTyYyayj8GhiVm9Muu6RI4xODQxq1dmXZfIMQaHJmb1yqzrEjnG4NDErF6ZdV0ixxgcmpjVK7OuS+QYg0MTs3pl1nWJHGNwaGJWr8y6LpFjDA5NzOqVWdclcozBoYlZvTLrukSOMTg0MatXZl2XyDEGhyZm9cqs6xI5xuDQxKxemXVdIscYHJqY1SuzrkvkGINDE7N6ZdZ1iRxjcGhiVq/Mui6RYwwOTQzrla+vr8UOVMmtiUzC4NDEsF4FBwfLgfEEquTWRCZhcGhiWK+SkpLc3NzkzLBYUIgquTWRSRgcmhjZq8DAQCk1AIVyOyLzMDg0MbJXK1eulGPDYkGh3I7IPAwOTYzsVXp6uru7uzo1sItCuR2ReRgcmhjcq379+qmDA7tyCyJTMTg0MbhXmzdvVgcHduUWRKZicGhicK/u379fvXp1kRrYwK7cgshUDA5NjO/V8OHDRXBgQ64jMhuDQxPjexUbGyuCAxtyHZHZGByaGN+r3NxcbytsyHVEZmNwaGJKr6ZYyaVEToDBoYkpvTptJZcSOQEGhybO2SsiszA4NHHOXhGZhcGhibP1Kicn59q1a48ePZIrbEycOHHevHlyqVVSUtL8+fN1/ZJIampqWlqaXPrE7du3MzIy5FJyRQwOTYzsVVxc3A8//KDsHj9+PCYmRlX/qxs3bqBLJ0+eVBfeunXr/PnzZ8+ejY+PP3PmzKlTpyIiIixWyIjs7OyuXbuuWbPmwYMHaIzcqVWrVqNGjYYMGaI+iWOTJk3y8/MT27Zf9+BUw4YNkwrJJTE4NDGyV99//325cuUOHDiA7UuXLlWuXBmjHdv4Nzg4OCgoaM6cOVOnTkWXRo8ePW3atMOHD4sD586dK2JCIk518+bN999/39PTE2Fx+fJllOzevXvUqFFbt25VLu0YgsnLy6t27dotW7Z85ZVX6tWrFx4erm7A4Cg9GByaGNwr5IKPjw9m/m3btv3b3/4mCkeMGNGhQ4eOHTt27tz5hRdeQJcCAgK6deu2fft20SA9PT0hIQGTi+Tk5JSUFCwr2rVrh3ARtVeuXMECBwuNpUuXihJMOtq0afPLL7+IXUxPVhYkrUrGjBmDXq1YsWLt2rWRkZF169ZdsmSJugGCo3///mJGQ66NwaGJwb169OgRxnzjxo2bNWuWlZUl1WKOgCkJuoRVjFSllpmZWbFixY0bN4pdnKpGjRqYdCBcRMnbb7+NwocPH4pdZJC/v7+3t3fVqlX9rcTERIiKiipbtqzya6xYCrm5uV29elVpkGcNDvQKFw0MDAwJCUF+qWvJlTA4NDG+V3hjx0WxEpHKQ0NDkRqzZs1C7ZEjR6RatYULF2JlcffuXbGL6cPq1asRB2JtgnkHgiAuLq7AMdb1DuY1UiEMHDgQJ1R2BwwY0L17d1X9rxAcgwcP3rNnz5QpU5o2bYpFjZaPb6kkYnBoYnCvEhMTMebHjx/v7u5+7NgxUXj9+nUsBDw8PMLDwzEglQ8vCoUZgaenZ6F/3zg3N3fRokWYLyxevFiusx8cWOYo2+vWrcPhtrElfcaBpZCqklwKg0MTI3uFUHjttdf++te/YnvChAk+Pj4ZGRkPHjzARosWLZTfJbXY+f9vWNosWLAAqdG3b1/1aM+zRkZMTEz79u2RR8uXL1dX4fzXrKZOndq2bVuxbfvdKk6IkyM1ZsyYIVXl2QQHuTAGhyZG9urjjz9u0KCB+FuB9+/ff/XVV//yl79g+8KFC2Lmj0GLFQe6pExGBAx+DF1Pq6CgoMePH6tro6KivL29Meb79et3/vx5dRVER0dbbLz33nvqNjiqZcuW5cuXt/eLIQyO0oPBoYlT9QprhOnTpytfjqjNnz9/1apVmZmZckVeXkJCwuzZs7EIkiussrOzE22kpqaq22AuM2LEiPj4eHWhWlhYWEREhFxKrojBoYlz9orILAwOTZyzV0RmYXBo4py9IjILg0MT5+wVkVkYHJo4Z6+IzMLg0MQ5e0VkFgaHJs7ZKyKzMDg0cc5eEZmFwaGJc/aKyCwMDk2cs1dEZmFwaOKcvSIyC4NDE+fsFZFZGByaOGeviMzC4NDEOXtFZBYGhybO2SsiszA4NHHOXhGZhcFROF9fX4sdqJJbE5UyDI7CBQcHy4HxRKF/AZioVGFwFC4pKcnNzU3ODIsFhaiSWzu3rKysNm3aiD9cqsWmTZtu374tl1rFxMTY3ucFTp06pb4JixqeLtu/h04lHYPDrsDAQDk2LBYUyu2ez7lz595XGT9+fHZ2tqj6+eefDxd04sSJgkcXbs+ePQsWLAgJCZk/f/68efM+/vhjHx+fV1999f79+127du3cuXOnTp06dOjw+uuvBwQEtGrV6ttvv8VR9+7du2NVuXLlo0ePYsM2I9zd3W3/0HGe9d5O//jHP+RSK0zQBg4cmJqaans2KrkYHHatXLlSjg2LBYVyu+fz448/Tpo0CWP7008/xfCrVq2acuPFf/7zn3VUqlev3qhRo4JHFw6R0bNnz969e/ft27d///6Ihrp16+K0OTk5ixYtCg0NXb58+YwZMzZs2ICW5cuX/+9//4ujevXqJT3YcuXKSWe2Fxx/+tOfcFqp8KeffsJ1PTw8cKqyZctu3rxZakAlF4PDrvT0dIwT9UDCrrhrQTF58803//73v8ulT8TGxqqDAxMTMUFQUzXPN3bsWOUGtEJiYiIezo0bNzANmTx5sihEcAQFBd18YseOHZ6enuqj8qzBMWjQoPXr10s3W+revbt0A2p4+PBhfHw8+rxz586RI0f26dPntdde8/f3d3znSioRGByO9OvXTx0c2JVbFJ1//etfNWrUwIiVK56QgqNdu3bqvgm2t1zE6G3QoAEmF+rCy5cvlylTBqsVrFywfhGFCA71vd3Wrl3729/+VtkVEBxDhw7F+Mc8BUse5Y5NHTt23LRpk9Js27Zt4g61eDhoiUXK0qVL8QC///776OhoBJbSkkooBocjmF2rh2XxTbYRCpUrV8Y7/O7du+W6J6TgOHHiRKyN3Nxc1RG/mjVrFo6S7iC/f/9+pMm+ffuUz1Pg4MGDly5dUnb//Oc/295dSVmqpKSkIAiU8oCAgF27dolthBdOHmu9y1xUVNQf/vAHTIVGjx5tG2pUcjE4HMG7cfXq1UVqYEN5cy5COTk5eJ+vUKFCSEjIli1bEB94uxZVx44d+5fKtGnTNH7GIaSlpU2YMKFixYoICHU5HgXWRLahoECXMEFAl06dOiVV2fuMo2fPnqtXrxbbn376abNmzUSEjRgx4pNPPlm+fDmmNgUOoBKOwfEUw4cPF8GBDbnuuSUnJ7du3bp27driDvIQGRlZqVIlvPnnWT/j7KDSokULjcGB6cCgQYNwHj8/P+kDhb179/7mN7/5/e9/jzbqciEzMxOB4u3t3bBhw5iYGLnafnAg8qpWrdqjR4/f/e539evX/89//pNnDaA6der88MMPBw4c8PDw6NSpU58+fdq2bRsWFiYfTyUNg+MpMOUWwSHm3kVuxYoV0geuq1atunLlirpEwFDH+JRLC4N3+7lz5x46dEiuyMu7evXqunXrpNvKqmFpg6vYW1Z89tln9j6hQJ+xMEEw3b17V5TgJGvWrBHXSkxMjIiICA0Nxb8XL14scCSVQAyOp8Ag9Lay/fiAqNRicDzdFCu5lKgUY3A83WkruZSoFGNwEJFuDA4i0o3BQUS6MTiISDcGBxHpxuAgIt0YHESkm9MFR82aNcWveDuVpk2bKj2cMWOGugq7qu6XmFqpAZEuThcczsn1hpmFMzt6DgwOTVxvmLneIyIjMTg0cb1h5nqPiIzE4NDE9YaZ6z0iMhKDQxPXG2au96kNGYnBoQmHGZEag4OIdGNwEJFuDA5ndPbs2fXr1+/YsePevXtyHZVkKSkp8fHxcqnKnTt3tm/fHh4e7uQ33GVwOJfc3NxRo0Ypv+LZuHHjYvrTvvzUxhSVK1e2vVemYu/evV5eXspPv3fv3g7+rLS5GByaFMcwCwsLU+6KAF999RV2xQ1rg4OD09LSDh061KhRo/bt2+cfU3SM/55o48aNeMjibz5nZmZi/MTFxcmNtMGxmJQVuhsbG7t27dpz584ptXnWW8ns3r3766+/LvSmEGoPHjyIiYnBdC8pKUkq/+6773CG5ORkpdBBN7B96dKlEydORERE7Nq16+HDhyjEafG0Dx48GLWF/rH4P/7xj/7+/ufPn8/Ozl64cCEaY9YpN3IODA5NimOYvfPOO+7u7rdu3cI2XmS4xNy5cwMCAgIDA5U233zzDcp//PHH/MOKSHE8IseQjJYnd+3+4IMP8N6rvnGcRLzlOthVv28ruzitaFmmTJl58+aJWgxRX19fUe7p6Xn48GHlQMnNmzdbtWolWlaoUCEqKkqUp6amtmnTRpSj20q5xU43xHbz5s3FIeDn5/fo0SO8DSglx44dE80sBX8Qyk2/bt++jSrlWs6GwaGJ9NMtEidPnsRpv/zyyzzr/UoQIniJ45Wtnt1cv34dbTTeTkWX4nhET/XWW2/VqFFj586dbm5u6vvU2pJGlO1uoSO2SpUqY8eOTU9PX7ZsmXIXXiz9WrRokZCQcObMmQYNGrRr1045UIKWWCkcPXoUP4g33ngDUwNRPmbMGPxcMD9CgmD5ULNmTYzqPPvdENtVq1bdtm0b5g6YdGB3z549hR6iflyKe/fuDRkyxNvb28G9hM3F4NCk0J/u88PkAm+GmL3jvQgvlDzrrdIwR1Ua4P0Hl8bcO/+YIlJMj8gxrBQw6pAaHTp0eJ771NgOP7GL5xODLTIyUv3RwEsvvTRs2LBQq169euHq0p10FQ0bNvzoo4/Etvp2n+ryixcv4nLiFr/2uiG2Z86cKbYx18DuihUrbA8p1PHjxzFbef3113/++We5zmkwODQppmGGdyScGe+9+Ffc9rFx48Yffvih0uCnn35CVaF3Y3xOxfGpjRZdunTBI5o9e7ZcoYe9EZuWljZu3LiKFSv6+/srX0hVqlTJUpC9JRKWISEhIXJpwfKsrCycAZOIPPvdcFAlldsKCwvD5YKDg3NycuQ6Z8Lg0KSYhhnedZs2bVq7dm3MO0TJ0KFD69evj1en2MUSBq97MTF2AZg6YeRgsYCxjUyUqzXDc4KhJbajo6OV0SimEqdPn0bJxo0bRQOsU8LDw8U2RmOhn0oKrVu37tOnj9g+d+6ccg/Nli1b9u3bV2zv2rULJxffldrrRp5NQGgMjs2bN1eoUAGXkCucD4PDZIsWLcKLCWtysYt1uIeHB17rQUFBWHJjXq1Mkku6pKSkatWqDRo0KCMjo169eogPB2+qFit7u506dXrxxRcxaPHk4P1ZjMYDBw7UqlULJWPHjrU8+UwB1qxZg5waP348ntKAgAAcmJmZqZxKTXwYgTUjztygQQOsF8SSB7MAlL/77ruYKCHlcRKxziq0G+JUUkAou2jWrVu3L774QtydV/24srOz0X8/P79QlQ0bNigncSoMDpNNnjzZ09Pzzp07SklsbCxePe7u7hhdmHHYu/9zyYKR1rlzZy8vL/GFaFRUFAZMoesCQUoKaTcxMbFr165VqlTBym7OnDl4AjHGMC8bOXJk9erVEU8TJ05UGudZvxx9+eWXkchYwuzfv19dJVmyZEmTJk0wlejRo4f6G9mFCxf6+Pig/wMGDFDmLIV2Q1TZC47p06fj5M2aNRNf3Kof17Vr18SuGloqJ3EqDA7T4HU5c+ZMTE0nTJgg15UO6rdWQVlTFCv5qkZd15UwOEyTkJBQpkyZLl26pKeny3XFr5g+tdFFfnu1WOrUqSM3KgbyVY26rithcGhSTMPM3veCBrAUz/dEVEowODRxvWHmeo+IjMTg0MT1hpnrPSIyEoNDE9cbZq73iMhIDA5NXG+YFdOnNlRKMDg04TAjUmNwEJFuDA59ZtjchPU5a5W70hZa6/jYIqklegYMDpNZXO7TEyoNGBwmY3BQScTgMBmDg0oiBofJGBxUEjE4TMbgoJKIwWEyBgeVRAwOkzE4qCRicJiMwUElEYPDZAwOKokYHCZjcFBJxOAwGYODSiIGh8kYHFQSMThMxuCgkojBYTIGB5VEDA6TMTioJGJwmIzBQSURg8NkDA4qiRgcJmNwUEnE4DAZg4NKIgaHyRgcVBIxOIzm6+trsQNVcmsip8TgMFpwcLAcGE+gSm5N5JQYHEZLSkpyc3OTM8NiQSGq5NZETonBYYLAwEA5NiwWFMrtiJwVg8MEK1eulGPDYkGh3I7IWTE4TJCenu7u7q5ODeyiUG5H5KwYHObo16+fOjiwK7cgcmIMDnNs3rxZHRzYlVsQOTEGhznu379fvXp1kRrYwK7cgsiJMThMM3z4cBEc2JDriJwbg8M0sbGxIjiwIdcROTcGh2lyc3O9rbAh1xE5NwaHmaZYyaVETo/BYabTVnIpkdNjcBCRbgwOItKNweGMcnJyrl279ujRI7nCxsSJE+fNmyeXWiUlJc2fP1/Xb4ikpqampaXJpU/cvn07IyNDLqVSicFhgqNHj6q/gr18+fK2bdseP36slNy4ccNisZw8eVIpgVu3bp0/f/7s2bPx8fFnzpw5depURESE+EIXGZGdnd21a9c1a9Y8ePAAjZE7tWrVatSo0ZAhQ9QncWzSpEl+fn5i2/a7Hpxq2LBhUiGVTgwOExw8eLBcuXL79u3Ls/4KafPmzceNG4cxHxwcHBQUNGfOnKlTpyIORo8ePW3atMOHD4uj5s6dK2JCcuDAAdTevHnz/fff9/T0RFggiVCye/fuUaNGbd26VXVlRxBMXl5etWvXbtmy5SuvvFKvXr3w8HB1AwYHKRgc5pgyZUqTJk3u3r37ySefIDju3bs3YsSIDh06dOzYsXPnzi+88AISISAgoFu3btu3bxeHpKenJyQkYHKRnJyckpKCZUW7du0QLqL2ypUrWOBgobF06VJRgklHmzZtfvnlF7GL6cnKgqRVyZgxY3x8fFasWLF27drIyMi6desuWbJE3QDB0b9/fzGjoVKOwWEODL8WLVq8+eabFStWlJYkmCNgPoLgOH78uLpckpmZiWM3btwodps1a1ajRg1MOhAuouTtt99G4cOHD8UuMsjf39/b27tq1ar+VmJiIkRFRZUtW1ZZQGEp5ObmdvXqVaVBnjU40CtcNDAwMCQkBPmlrqVShcFhmtOnT2Mcfv755+rC0NBQpMasWbNQdeTIEXWVZOHChVhZYM4idjF9WL16NeJArE0w70AQxMXFFTjGut7BvEYqhIEDB+KEyu6AAQO6d++uqv8VgmPw4MF79uzBdKlp06ZY1Gj5+JZcEoPDTEiHLVu2iO3r169jIeDh4REeHo4BqXx4USjMCDw9PQv948a5ubmLFi3CfGHx4sVynf3gwDJH2V63bh0Ot40t6TMOLIVUlVS6MDjMpAQHVi4+Pj5YvCi/SGqx85/fsrKyFixYgNTo27everTnWSMjJiamffv27u7uy5cvV1fh/Nespk6d2rZtW7Ft+90qToiTIzVmzJghVeXZBAeVZgwOM6lnHBcuXBAzfwxarDhQdezYMXVjDH4MXU+roKAg9de3edYPKby9vTHm+/Xrd/78eXUVREdH/+87GJX33ntP3QZHtWzZsnz58vZ+MYTBQQoGh5kuXryIGYRUiDXC9OnTlS9H1ObPn79q1arMzEy5Ii8vISFh9uzZiYmJcoVVdnZ2oo3U1FR1G/RkxIgR8fHx6kK1sLCwiIgIuZRKJQYHEenG4CAi3RgcRKQbg4OIdGNwEJFuDA4i0o3BQUS6MTiISDcGBxHpxuAgIt0YHESkG4ODiHRjcBCRbgwOItKNwUFEujE4iEg3BgcR6cbgICLdGBxEpBuDg4h0Y3AQkW4MDiLSjcFBRLoxOIhINwYHEenG4CAi3RgcRKRbIcFBRKQRg4OIdGNwEJFu/w9XaeokDAVKBgAAAABJRU5ErkJggg==" /></p>

次に、x0がスコープアウトし、そのタイミングではY::x_が健在であるため、
Xオブジェクトの参照カウントも1になる。このため、x0、y0がスコープアウトした状態でも、
X、Yオブジェクトの参照カウントは0にならず、従ってこれらのオブジェクトは解放されない
(shared_ptrは参照カウントが0->1に変化するタイミングで保持するオブジェクトを解放する)。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 176
    }  // この次の行で、x0はスコープアウトする

    ASSERT_EQ(X::constructed_counter, 1);  // Xオブジェクトは未開放であり、リークが発生
    ASSERT_EQ(Y::constructed_counter, 1);  // Yオブジェクトは未開放であり、リークが発生
```

<!-- pu:deep/plant_uml/shared_cyclic_3.pu--><p><img src="data:image/png;base64,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" /></p>

X、Yオブジェクトへのハンドルを完全に失った状態であり、X、Yオブジェクトを解放する手段はない。

#### std::weak_ptr <a id="SS_19_5_7_4"></a>
std::weak_ptrは、[スマートポインタ](term_explanation.md#SS_19_9_1)の一種である。

std::weak_ptrは参照カウントに影響を与えず、共有所有ではなく参照のみを保持するのため、
[オブジェクトの循環所有](term_explanation.md#SS_19_5_7_3)の問題を解決できる。

[オブジェクトの循環所有](term_explanation.md#SS_19_5_7_3)で示した問題のあるクラスの修正版を以下に示す
(以下の例では、Xは前のままで、Yのみ修正した)。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 188

    class Y;
    class X final {
    public:
        explicit X() noexcept { ++constructed_counter; }
        ~X() { --constructed_counter; }

        void Register(std::shared_ptr<Y> y) { y_ = y; }

        std::shared_ptr<Y> const& ref_y() const noexcept { return y_; }

        bool DoSomething() { return true; }

        static uint32_t constructed_counter;

    private:
        std::shared_ptr<Y> y_{};
    };
    uint32_t X::constructed_counter;

    class Y final {
    public:
        explicit Y() noexcept { ++constructed_counter; }
        ~Y() { --constructed_counter; }

        void Register(std::shared_ptr<X> x) { x_ = x; }

        std::weak_ptr<X> const& ref_x() const noexcept { return x_; }

        bool DoSomething()
        {
            if (auto x = x_.lock(); x) {  // weak_ptrからshared_ptrの生成
                static_assert(std::is_same_v<std::shared_ptr<X>, decltype(x)>);
                return x->DoSomething();
            }
            else {
                return false;
            }
        }

        static uint32_t constructed_counter;

    private:
        std::weak_ptr<X> x_{};
    };
    uint32_t Y::constructed_counter;
```

このコードからわかるように修正版YはXオブジェクトを参照するために、
`std::weak_ptr<X>`を使用する。
`std::weak_ptr<X>`にアクセスする必要があるときに、
下記のY::DoSomething()関数の内部処理のようにすることで、
`std::weak_ptr<X>`オブジェクトから、
それと紐づいた`std::shared_ptr<X>`オブジェクトを生成できる。

なお、上記コードは[初期化付きif文](term_explanation.md#SS_19_7_5_3)を使うことで、
生成した`std::shared_ptr<X>`オブジェクトのスコープを最小に留めている。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 218

        bool DoSomething()
        {
            if (auto x = x_.lock(); x) {  // weak_ptrからshared_ptrの生成
                static_assert(std::is_same_v<std::shared_ptr<X>, decltype(x)>);
                return x->DoSomething();
            }
            else {
                return false;
            }
        }
```

Xと修正版Yの単体テストによりメモリーリークが修正されたことを以下に示す。

```cpp
    //  example/term_explanation/weak_ptr_ut.cpp 244

    {
        ASSERT_EQ(X::constructed_counter, 0);
        ASSERT_EQ(Y::constructed_counter, 0);

        auto x0 = std::make_shared<X>();
        auto y0 = std::make_shared<Y>();

        ASSERT_EQ(x0.use_count(), 1);
        ASSERT_EQ(x0->ref_y().use_count(), 0);  // X::y_は何も管理していない

        ASSERT_EQ(X::constructed_counter, 1);  // Xオブジェクトは1つ生成された
        ASSERT_EQ(Y::constructed_counter, 1);  // Yオブジェクトは1つ生成された

        ASSERT_EQ(y0.use_count(), 1);
        ASSERT_EQ(y0->ref_x().use_count(), 0);  // Y::x_は何も管理していない

        ASSERT_FALSE(y0->DoSomething());  // Y::DoSomethingの処理をX::DoSomethingに委譲

        x0->Register(y0);  // これによりy0にy0を渡す。y0 -> x0の参照はshared_ptrによって行う
        y0->Register(x0);  // これによりx0にy0を渡すが、y0 -> x0の参照はweak_ptrによって行う
        ASSERT_EQ(X::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない
        ASSERT_EQ(Y::constructed_counter, 1);  // 新しいオブジェクトが生成されるわけではない

        ASSERT_TRUE(y0->DoSomething());  // Y::DoSomethingの処理をX::DoSomethingに委譲

        ASSERT_EQ(x0.use_count(), 1);  // Xオブジェクトはx0に所有されるが、y0には所有されない
        ASSERT_EQ(y0->ref_x().use_count(), 1);  // weak_ptr<X>::use_count
        ASSERT_EQ(y0.use_count(), 2);  // Yオブジェクトはy0とx0から共有所有されるため
        ASSERT_EQ(x0->ref_y().use_count(), 2);  // Yオブジェクトはy0とx0から共有所有されるため
    }  // この次の行で、x0、y0はスコープアウトする。

    ASSERT_EQ(X::constructed_counter, 0);  // Xオブジェクトは開放済み
    ASSERT_EQ(Y::constructed_counter, 0);  // Yオブジェクトは開放済み
```


### オブジェクトのライフタイム <a id="SS_19_5_8"></a>
オブジェクトは、以下のような種類のライフタイムを持つ。

* 静的に生成されたオブジェクトのライフタイム
* thread_localに生成されたオブジェクトのライフタイム
* newで生成されたオブジェクトのライフタイム
* スタック上に生成されたオブジェクトのライフタイム
* prvalue(「[rvalue](term_explanation.md#SS_19_14_3)」参照)のライフタイム

なお、リファレンスの初期化をrvalueで行った場合、
そのrvalueはリファレンスがスコープを抜けるまで存続し続ける。

rvalueをバインドするリファレンスが存在しない状態で、
そのrvalueがメンバ変数へのリファレンスを返す関数を呼び出し、
そのリファレンスをバインドするリファレンス変数を初期化した場合、
リファレンスが指すオブジェクトはすでにライフタイムを終了している。
このような状態のリファレンスを[danglingリファレンス](term_explanation.md#SS_19_15_5)と呼ぶ。
同様に、このような状態のポインタを[danglingポインタ](term_explanation.md#SS_19_15_6)と呼ぶ。

### オブジェクトのコピー <a id="SS_19_5_9"></a>
#### シャローコピー <a id="SS_19_5_9_1"></a>
シャローコピー(浅いコピー)とは、暗黙的、
もしくは=defaultによってコンパイラが生成するようなcopyコンストラクタ、
copy代入演算子が行うコピーであり、[ディープコピー](term_explanation.md#SS_19_5_9_2)と対比的に使われる概念である。

以下のクラスShallowOKには、コンパイラが生成するcopyコンストラクタ、
copy代入演算子と同等なものを定義したが、これは問題のないシャローコピーである
(が、正しく自動生成される関数を実装すると、メンバ変数が増えた際にバグを生み出すことがあるため、
実践的にはこのようなことはすべきではない)。

```cpp
    //  example/term_explanation/deep_shallow_copy_ut.cpp 7

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
    //  example/term_explanation/deep_shallow_copy_ut.cpp 43

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
    //  example/term_explanation/deep_shallow_copy_ut.cpp 60

    auto const s0 = ShallowNG{"s0"};

    // NG s0.str_とs1.str_は同じメモリを指すため~ShallowNG()に2重解放される。
    auto const s1 = ShallowNG{s0};

    auto s2 = ShallowNG{"s2"};

    // NG s2.str_が元々保持していたメモリは、解放できなくなる。
    s2 = s0;

    // NG s0.str_とs2.str_は同じメモリを指すため、
    //    s0、s2のスコープアウト時に、~ShallowNG()により、2重解放される。
```

#### ディープコピー <a id="SS_19_5_9_2"></a>
ディープコピーとは、[シャローコピー](term_explanation.md#SS_19_5_9_1)が発生させる問題を回避したコピーである。

以下に例を示す。

```cpp
    //  example/term_explanation/deep_shallow_copy_ut.cpp 79

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


#### スライシング <a id="SS_19_5_9_3"></a>
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
    //  example/term_explanation/slice_ut.cpp 10

    class Base {
    public:
        explicit Base(char const* name) noexcept : name0_{name} {}
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

    TEST(Slicing, reference)
    {
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
    #if 0
        ASSERT_STREQ("d1", d2.Name1());  // 本来ならこうなってほしいが、
    #else
        ASSERT_STREQ("d0", d2.Name1());  // スライシングの影響でDerived::name1_はコピーされない
    #endif
    }
```

copy代入演算子(=)によりコピーが行われた場合、=の両辺のオブジェクトは等価になるべきだが
(copy代入演算子をオーバーロードした場合も、そうなるように定義すべきである)、
スライシングが起こった場合、そうならないことが問題である(「[等価性のセマンティクス](term_explanation.md#SS_19_17_1)」参照)。

下記にこの現象の発生メカニズムについて解説する。

1. 上記クラスBase、Derivedのメモリ上のレイアウトは下記のようになる。

<!-- pu:deep/plant_uml/slicing_class.pu--><p><img src="data:image/png;base64,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" /></p>

2. 上記インスタンスd0、d1、d2、d2_refのメモリ上のレイアウトは下記のようになる。

<!-- pu:deep/plant_uml/slicing_init.pu--><p><img src="data:image/png;base64,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" /></p>

3. d2 = d0をした場合の状態は下記のようになる。

<!-- pu:deep/plant_uml/slicing_normal.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcwAAAEYCAIAAABeFlHoAAAnvElEQVR4Xu2dDVBWVf7HL5i8SCFKrppYOq6UbgtrO8YslmPZrFNJNbpaC5ogGra+EOaEWX9lQwsQs0iUaDZBHTUXW80Ri01IJTU0Y8HQEE18gbRAEnkEhPz/Ho4cjuciL/Lc+zzPfb6f+Q1z7jm/c57ruff5POc+L1flOgAAAM1Q5AoAAACWA5IFAAANaZHsbwAAACwEJAsAABoCyQIAgIZAsgAAoCGQLAAAaAgkCwAAGgLJAgCAhkCyAACgIZAsAABoCCQLAAAaAskCAICGQLIAAKAhkCwAAGgIJAsAABoCyQIAgIZAsgAAoCGQLAAAaAgkCwAAGgLJAgCAhkCyAACgIZAsAABoCCQLAAAaAskCAICGQLIAAKAhkCwAAGgIJAsAABoCyQIAgIZAsgAAoCGQLAAAaAgkCwAAGgLJAgCAhkCyAACgIYaSrLe3twKMCB1ZfpRdXDzlZgdDnA0PLw+52SER58TWMJRkaa75vwIYCTqyVVVV1dXVJpOJypMm/deRQ5qND09+iBDnpK6urqGhQbaD9Wg5jXlJTrEfIFmjQke2tLS0vLy8oqICkpVmQ20cBwxxTki15FnZDtaj5TTmJTnFfoBkjQod2cLCwhMnTpw7dw6SlWZDbRwHDHFOyLO0npXtYD1aTmNeklPsB0jWqNCRzc3Nzc/Pp2cRJCvNhto4DhjinNB6lhazsh2sR8tpzEtyiv0AyRoVOrKZmZn0LKLVCiQrzYbaOA4Y4pyUlpZWVVXJdrAeLacxL8kp9gMka1ToyG7atOnzzz/Py8uDZKXZUBvHAUOcE1rMVlRUyHawHi2nMS/JKfYDJGtUIFkxIFl1QLI6AckaFUhWDEhWHZCsTkCyRgWSFQOSVQckqxOQrFGBZMWAZNUByeoEJGtUIFkxIFl1QLI6AckaFUhWDEhWHZCsTkCyRgWSFQOSVQckqxOQrFGBZMWAZNUByeoEJGtUIFkxIFl1QLI6AckaFUhWDEhWHZCsTkCyRgWSFQOSVQckqxOQrFGBZMWAZNUByeoEJGtUIFkxIFl1QLI6AckaFUhWDEhWHZCsTkCyRgWSFQOSVQckqxOQbLtER0cfPHhQrrV5IFkxIFl1QLI6oY9k16xZ8/3338u1HeCnn346evSoXKsvNEW0/2IN/Vs2bNiwY8eOq1evivU2hT1KNipqf1JSYVzcd8HBu9WtXQl7lOzKIyvDEsNivohRN1kkIFmd0Eeyak91EA8Pj9vraEHEnacZmzVrltLM4MGD6ey8Od1WsC/JTp7836yss3znL1wwzZ37tTrttsO+JDv7o9kPjnmwu2t32tWQ2BB1gkUCktUJfSQrQsIqKSk5cuTI+vXrMzMz6+vrxdacnJy0tLSioiIq02qRdi84OJi6XLx4kedQ93Xr1ol92xizrq4uKyuLhjpz5gyvJGpra+n0+uSTT2ixLNYzampqaKFKreXl5aJkP/roI9qMj4+vrKzcv3//fffdN3r06Ju72goWkWxq6rE5c3Jfe+1gUtLRt98+8sILX/Imqv/gA7mS8l9//Zv33y+kppkz90ydmv3uuwXx8fkhIS0rU1qlLl16hOpnzNjDK1NS2BEvDg396o038i5evFpUVCnuSRfDIpIl3y3NWfrmjjenr5g+9+O5q39YzZuonladUiXlv/7p6+Erw6lp+cHlSYVJM5Nm/uPDf6z6fhXPST6WPG/tPKpf/s1yXkn5Ac8GPDv/WUgWku0ooqeoPHz4cKWZkSNHXrt2jTXNnTuXVTo5OSUkJJDCeNqhQ4dYzooVK5ydnVllQEAA86lyizF//vnnESNGsEoXF5dPP/2UDULK9vPzY/Wenp4HDhxg9YyysjJfX1/eqgg7HxgYOGbMGJ7573//m1qPHz/Oa2wHxRKSpXHOnr3Cxywp+ZUpNT39h9+anwnFxVXcs7TZ0HCj/tKlutOnq6WO4eF7eKXJdG3RojzW8fjxqqNHW6y6YsX/KCEy0mKLWWk21MbpSFDH/r/vz04MYpDfoDXFa6h+0qJJTs5OrHLwnwZzz9Kmc7cb56pnH0+fB3ykjomHEnml251u0RnR4sPFZscqkCwvySn2g2INyd51113bt283mUy08KTNL774gjXdeeedc+bMuXTpUkpKCvlR6kiQUqdMmRIaGkqWzMjIoFZab7YxJl3ae3l50TlE+WPHjqVFMRuH6v39/U+dOlVYWOjj4zNq1Cj+EERYWFjv3r0PHz5MexIZGSnuAzk3JiaGZ164cIFa//Of//Aa20F8CildkKzJ1MCWorSYpU1ahJIu9+4ty8k5T8ZMTDTbMC7uO55fXl5DV/qxsd9eN79c1bz88j5a7bKOlJCVdfb06cuzZ+fOn3/gl19qjx+/xDqScLdsOckflxa51CUhIV+9S7cX0myojdORoI5uHm5sKUqLWdqMTIskpQY8FxA4MZCMGZEcQZV0sc/zf3ff78iVr6S/QuW+g/u+s+8dWu1SmVavlDA6eLTPMJ9lXy1bsmtJr369hvx5iPhwkKz5NOYlOcV+UKwh2djYWFam9SZtpqamsk1aJA4cOHDjxo0NDQ3qjgza5127dkVHR7/wwgvUSjpmaa2Oee+99y5YsIDV19bWNo9xfdCgQeHh4WuaePrpp2lpXFdXx1tpH2h8Viati/vg6ur63nvv8Uwak1rT0tJ4je0gPoWULkh28+YSVia30iZd109qegt12bIj27b9mJtrfrMlNdVcyfLXrv2hKcGcnJbWUmYdL1407d59PjX1GMW33/5MR/Pvfze/k1Bf38g6sggO3k1dVq06Ku5MV0KaDbVxOhLUkS7hWZmWorQ5ZdkUKqeUpJA0x0WMGzl+JFWGLL2hRSpP/r/J5oQTKebymy1l1tHbx3vU5FGkUYo/PvZHWg4nH0/mDwfJmk9jXpJT7AfFGpIVvSluVlZWzps3z93dPSAggH1wLyUTlNCtWzdals6YMYO33mpMDw+PFStW8HpOjx49lJspKSnhrVIvcfDBgwfPnz+fNxUXF1NrVlYWr7EdFAtJlmyo3szMPNPY+FtBQcWXX54Tc9ot19beePnkzJmTS/UXLph27CjlDzRv3tfURMthXtPFkGZDbZyOhHKz8vjm49Med+7m/EDgA488/4iY027Zxd2FnX6cpTlL+fiQ7HVItuMoHZMsW04WFBRQ5ZYtW9TJRM+ePd944w0qnDx5krfeasyHHnromWeeYZVFRUX79+9nZX9///T0dFZubGwUP1UjRowYERQUxMqHDx8WB58+ffqAAQOuXLnxNuWbb75Jvq6qqmKbNoX4FFIsLdmammtbt56a1PTxl5jTbvn06ct8fUor3PDwG599ZWefr6ionTIlm21mZJwiHU+blsM2ux7SbKiN05GQlMc33e9yf2r2U1SgC38xp92yzzCfsMQwVkkr3MRDiXzwDyFZdhrzkpxiPyg2I9l9+/b16dOHru7nzJmjNL+pSovKcePGvfXWW/zDseHDhz/44IPLly+ngpOT07Jly9oYk70/GxISEh8f7+PjQ13YGxFr166l9XJkZGRcXFxgYGC/fv0uX77Mu5N/qde0adNiYmJ69+4tDl5YWOjm5kaOpo6zZs1ydnbmb0fYGuJTSLG0ZM+evXLmTPW6dcVUoGfExo033lIQ81stJyd/X1fXuHNn6YYNJ44fr7p0qe7FF81inT//QH19IymY6rOyztKZ+dlnp8U96WJIs6E2TkdCUh7f7P/7/vf43jNx4UQq0Dn53KvPqfNbLU9LmNbdrfvY0LETXpsw5KEhnn083y94n48PyZpPY16SU+wHxWYkS+vBl156qVevXrRWjYqKYq2LFy+mpeL999/Pf8tw8ODBYcOGUWVoaCj5d/z48eIgDHFz1apVQ4YMofwnn3xS/BYXJfj6+pIxAwIC9u7dy+sZCQkJtGIlw9LSlfZHHDwnJ2fkyJGurq733HMPrWS5/W0NSStq73Qkrt9CsosW5Z07d4UWmzk55/Pzfzl8+Gd1/q3KVCgrqyGlFhdXLV58iA8eE3O4pORXqq+srKWVrPjNsK6HNBtq43QkJOXxzYVbF5Je6do/cGLgH0b/we9xP3X+rcpU6Du4b3fX7oP/NHjB5gXiw0Gy5tOYl+QU+0HRRbJAfywiWetGatPnY2Lc9kdhFpGsdSOk6fMxMfhbDbcXkKxOQLJGxQCSlf9J5sudOnVaR8IAklVUeN7tqU7reCiQrD4okKxBEZ9Cin1K1oIhzYbaOA4YkKxOQLJGRTfJTp2aPXfu1xERe+nv88/Lb6Ru2/Yj/1lXq9F2d0uFbpJNKkyKzY6N3x9Pf9nPusQYFzFu4daF6l4d7G7ZgGR1ApI1KrpJlv3oKy/P/DU49lUBMa7f/NHZJNWtttrubqnQTbKzVpvvH+T/hD/9Fb8qwEJRfZAV80XM9Henz/5o9qoi8w0N2u5u2YBkdQKSNSq6Sfatt8y/oN216wydTpMny63XBcm2equttrtbKnSTbNT6KBr/sRcfc3J2SilJkVpFyVLr6ODRSjN3D7ybVq9td7dsQLI6AckaFd0kGx39zXXzV5KLr1ypZzVTpmTTQvXddwtmzjTfgoBLttVbbam7axG6SXbR9kU0/sSFE3v07MFqPjj6AS1UzffZOrhclOzUt6fS5oToCSuPrIzOiPYe4D304aHq7toFJKsTkKxR0U2yERF7Cwoq/vnPb/ftK6fNl17aW1ZWw/bBZDJ/iZhLttVbbS1efEjsrlHoJtn4/fEPBD4QtSHq4Wceps2EAwl9B/dVmnC7002U7JCHhvgG+PKOEavMN5dZsGmB2F3TgGR1ApI1KrpJVors7PPV1fW0Pg0Nzdm5s/S6IFmtb7XVRugmWSkC/xbo4eVB69OV360cGzpWlCw5NygyiGcm5iVS68spL6sH0SggWZ2AZI2KtST7yy9Xt237kZXZjbu4ZLW+1VYbYS3J9urfa1zEOFZe/cNqUbJ3uNzB7tHFIvlYMrWGLg9VD6JRQLI6AckaFWtJtra2IT29xaTXBclqfautNsJaknXt4Tpp0SS+KUr27oF3PxH+BG+K3W3+Ee0r6a+oB9EoIFmdgGSNirUke+rU5cOHL7Iy+1CLS1brW221EdaS7MDhA/3G3riVAftQi0t21KRRXn29kgqT2OZTs59ycXd5L/899SAaBSSrE5CsUbGWZOnynx79q6/Ktmw5WV1t/s+BuGS1vtVWG2EtyYYlhtHD/WXCX4Iigzy8PETJLtm1pLtrd59hPhNemzA6eLSTs9NfZ/5VPYJ2AcnqBCRrVKwlWYr164tpxUqGpaVrTc018ccImt5qq42wlmQpJi6cSCtWMiwtXd3vchd/jPDqxlcH+Q26w+UOSqCVrNY/8ZICktUJSNaoWFGyNhhWlKzNBiSrE5CsUYFkxYBk1QHJ6gQka1QgWTEgWXVAsjoByRoVSFYMSFYdkKxOQLJGBZIVA5JVBySrE5CsUYFkxYBk1QHJ6gQka1QgWTEgWXVAsjoByRoVSFYMSFYdkKxOQLJGBZIVA5JVBySrE97e3gowIh4eHvwp5OXlJTc7GJgNNeKcQLLaUlVVVVpaWlhYmJubm5mZuQkYBTqadEzpyJY248hHGbOhRpwT8oCsButhNMlWV1eXl5fTS1l+fj7N+OfAKNDRpGNKR7a8GUc+ypgNNeKckAdkNVgPo0nWZDLRlcK5c+doruk1LQ8YBTqadEzpyFY048hHGbOhRpwT8oCsButhNMnW1dXRixjNMr2a0VXDCWAU6GjSMaUjW92MIx9lzIYacU7IA7IarIfRJNvQ0EDzS69jNNFVVVX8dR7YO3Q06ZjSka1rxpGPMmZDjTgn5AFZDdbDaJIFAACbApIFAAANgWQBAEBDIFkAANAQSBYAADQEkgUAAA2BZAEAQEMgWQAA0BBIFoB2GDp0qFzlwGA2OgskC0A7KIoiVzkwmI3OAskC0A7Qighmo7NAsgC0A7QigtnoLJAsAO0ArYhgNjoLJAtAO0ArIpiNzgLJAtAO0IoIZqOzQLIAtAO0IoLZ6CyQLADtAK2IYDY6CyQLQDtAKyKYjc4CyQLQDtCKCGajs0CyALQDtCKC2egskCwA7QCtiGA2OgskC0A7QCsimI3OYijJDh06VLldcG8hcCsUaEUAs9FZDCVZALQAWhHBbHQWSBaAdoBWRDAbnQWSBaAdoBURzEZngWQBaAdoRQSz0VkgWQDaAVoRwWx0FkgWgHaAVkQwG50FkgVAxs/Pz/y1vtagJjnb6GA2uggkC4BMXFycrJNmqEnONjqYjS4CyQIgU1pa6uzsLBtFUaiSmuRso4PZ6CKQLACtMGbMGFkqikKVcp5jgNnoCpAsAK2QmpoqS0VRqFLOcwwwG10BkgWgFSorK11dXUWn0CZVynmOAWajK0CyALTOhAkTRK3QppzhSGA2bhtIFoDWycjIELVCm3KGI4HZuG0gWQBa5+rVq7169WJOoQJtyhmOBGbjtoFkAbglM2bMYFqhgtzmeGA2bg9IFoBbkp2dzbRCBbnN8cBs3B6QLAC3pLGxcWATVJDbHA/Mxu0ByQLQFtFNyLWOCmbjNoBkAWiL/zUh1zoqmI3bAJIFAAANgWQBAEBDIFkAANAQSBYAADQEkgUAAA2BZAEAQEMgWQAA0BBDSdbb25v97A8YDDqy/Ci7uHjKzQ6GOBseXh5ys0MizomtYSjJ0lzzfwUwEnRkq6qqqqurTSYTlSdN+q8jhzQbH578ECHOSV1dXUNDg2wH69FyGvOSnGI/QLJGhY5saWlpeXl5RUUFJCvNhto4DhjinJBqybOyHaxHy2nMS3KK/QDJGhU6soWFhSdOnDh37hwkK82G2jgOGOKckGdpPSvbwXq0nMa8JKfYD5CsUaEjm5ubm5+fT88iSFaaDbVxHDDEOaH1LC1mZTtYj5bTmJfkFPsBkjUqdGQzMzPpWUSrFUhWmg21cRwwxDkpLS2tqqqS7WA9Wk5jXpJT7AdI1qjQkd20adPnn3+el5cHyUqzoTaOA4Y4J7SYraiokO1gPVpOY16SU+wHSNaoQLJiQLLqgGR1ApI1KpCsGJCsOiBZnYBkjQokKwYkqw5IVicgWaMCyYoByaoDktUJSNaoQLJiQLLqgGR1ApI1KpCsGJCsOiBZnYBkjQokKwYkqw5IVicgWaMCyYoByaoDktUJSNaoQLJiQLLqgGR1ApI1KpCsGJCsOiBZnYBkjQokKwYkqw5IVicgWaMCyYoByaoDktUJSNaoQLJiQLLqgGR1ApI1KpCsGJCsOiBZnYBkjQokKwYkqw5IVicg2XaJjo4+ePCgXGvzQLJiQLLqgGR1Qh/Jrlmz5vvvv5drO8BPP/109OhRuVZfaIpo//lmdXX1Z599lp6ebuPmtUfJRkXtT0oqjIv7Ljh4t7q1K2GPkl15ZGVYYljMFzHqJosEJKsT+khW8lTH8fDwuL2OFkTc+ezsbC8vL6WZoKCghoaGm9NtBfuS7OTJ/83KOst3/sIF09y5X6vTbjvsS7KzP5r94JgHu7t2p10NiQ1RJ1gkIFmd0EeyIiSskpKSI0eOrF+/PjMzs76+XmzNyclJS0srKiqi8oYNG2j3goODqcvFixd5DnVft26d2LeNMevq6rKysmioM2fO8EqitraWTq9PPvmEFstiPaOmpmbHjh3UWl5eLkr2kUceCQgIOHbsmMlkeu+996iJ0m7uaitYRLKpqcfmzMl97bWDSUlH3377yAsvfMmbqP6DD+RKyn/99W/ef7+QmmbO3DN1ava77xbEx+eHhLSsTGmVunTpEaqfMWMPr0xJYUe8ODT0qzfeyLt48WpRUaW4J10Mi0iWfLc0Z+mbO96cvmL63I/nrv5hNW+ielp1SpWU//qnr4evDKem5QeXJxUmzUya+Y8P/7Hq+1U8J/lY8ry186h++TfLeSXlBzwb8Oz8ZyFZSLajiJ6i8vDhw5VmRo4cee3aNdY0d+5cVunk5JSQkHDffffxtEOHDrGcFStWODs7s0ryHfOpcosxf/755xEjRrBKFxeXTz/9lA1Cyvbz82P1np6eBw4cYPWMsrIyX19f3qrcvAwnO7NCVVUVNfExbQ3FEpKlcc6evcLHLCn5lSk1Pf2H35qfCcXFVdyztNnQcKP+0qW606erpY7h4Xt4pcl0bdGiPNbx+PGqo0dbrLpixf8oITLSYotZaTbUxulIUMf+v+/PTgxikN+gNcVrqH7SoklOzk6scvCfBnPP0qZztxvnqmcfT58HfKSOiYcSeaXbnW7RGdHiw8VmxyqQLC/JKfaDYg3J3nXXXdu3b6fFIC08afOLL75gTXfeeeecOXMuXbqUkpJCfpQ6EqTUKVOmhIaGkiUzMjKU5oXkrcacNWsWXd3TOUT5Y8eOpUUxG4fq/f39T506VVhY6OPjM2rUKP4QRFhYWO/evQ8fPkx7EhkZKe0D4+rVqyEhIQMHDmT7aYOITyGlC5I1mRrYUpQWs7RJi1DS5d69ZTk558mYiYlmG8bFfcfzy8tr6Eo/Nvbb6+aXq5qXX95Hq13WkRKyss6ePn159uzc+fMP/PJL7fHjl1hHEu6WLSf549Iil7okJOSrd+n2QpoNtXE6EmYVerixpSgtZmkzMi2SlBrwXEDgxEAyZkRyBFXSxT7P/919vyNXvpL+CpX7Du77zr53aLVLZVq9UsLo4NE+w3yWfbVsya4lvfr1GvLnIeLDQbLm05iX5BT7QbGGZGNjY1mZ1pu0mZqayjbHjBlD2tq4cSN/o1PsyKB93rVrV3R09AsvvECtpGOW1uqY995774IFC1g9X4ESgwYNCg8PX9PE008/TUvjuro63kr7QOOzMmldvQ/kX1o4P/roo+fOnRPrbQrxKaR0QbKbN5ewMrmVNum6flLTW6jLlh3Ztu3H3Fzzmy2pqeZKlr927Q9NCebktLSWMut48aJp9+7zqanHKL799mc6mn//u/mdhPr6RtaRRXDwbuqyatVRcWe6EtJsqI3TkaCOdAnPyrQUpc0py6ZQOaUkhaQ5LmLcyPEjqTJk6Q0tUnny/002J5xIMZffbCmzjt4+3qMmjyKNUvzxsT/Scjj5eDJ/OEjWfBrzkpxiPyjWkKzoLHGzsrJy3rx57u7uAQEBtFRUJxOU0K1bN1qWzpgxg7feakwPD48VK1bwek6PHj2UmykpKeGtUi9p8I8//pgS4uPjGxsbeaUNolhIsmRD9WZm5pnGxt8KCiq+/NL8MsNz2i3X1sqfE86Zk0v1Fy6Yduwo5Q80b97X1ETLYV7TxZBmQ22cjoRys/L45uPTHnfu5vxA4AOPPP+ImNNu2cXd5cb518zSnKV8fEj2OiTbcZSOSZYtJwsKCqhyy5Yt6mSiZ8+eb7zxBhVOnjzJW2815kMPPfTMM8+wyqKiov3797Oyv79/eno6K5MrxU/ViBEjRgQFBbEyLVrFwbdu3eri4pKZmdmSbauITyHF0pKtqbm2deupSU0ff4k57ZZPn77M16e0wg0Pv/HZV3b2+YqK2ilTstlmRsYp0vG0aTlss+shzYbaOB0JSXl80/0u96dmP0UFuvAXc9ot+wzzCUsMY5W0wk08lMgH/xCSZacxL8kp9oNiM5Ldt29fnz596Op+zpw5SvObqrRmHDdu3FtvvcU/HKPr9AcffHD58uVUcHJyWrZsWRtjsvdnQ0JCaOHp4+NDXdgbEWvXrqX1cmRkZFxcXGBgYL9+/S5fvsy7k3+p17Rp02JiYnr37s1HM5lMtIcjR45cI7B582be0aYQn0KKpSV79uyVM2eq160rpgI9IzZuvPGWgpjfajk5+fu6usadO0s3bDhx/HjVpUt1L75oFuv8+Qfq6xtJwVSflXWWzszPPjst7kkXQ5oNtXE6EpLy+Gb/3/e/x/eeiQsnUoHOyedefU6d32p5WsK07m7dx4aOnfDahCEPDfHs4/l+wft8fEjWfBrzkpxiPyg2I9mqqqqXXnqpV69etFaNiopirYsXL6ZL+/vvv5//luHgwYPDhg2jytDQUPLv+PHjxUEY4uaqVauGDBlC+U8++aT4LS5K8PX1dXNzCwgI2Lt3L69nJCQkDBgwgAw7ffp02h82Gvs6lwTtm9TXRlC0lOyiRXnnzl2hxWZOzvn8/F8OH/5ZnX+rMhXKympIqcXFVYsXH+KDx8QcLin5leorK2tpJSt+M6zrIc2G2jgdCeUWkl24dSHpla79AycG/mH0H/we91Pn36pMhb6D+3Z37T74T4MXbF4gPhwkaz6NeUlOsR8UXSQL9McikrVupDZ9PibGbX8UZhHJWjdCmj4fE4O/1XB7AcnqBCRrVAwgWfmfZL7cqVOndSQMIFlFhefdnuq0jocCyeqDAskaFPEppNinZC0Y0myojeOAAcnqBCRrVHST7NSp2XPnfh0RsZf+Pv+8/Ebqtm0/8p91tRptd7dU6CbZpMKk2OzY+P3x9Jf9rEuMcRHjFm5dqO7Vwe6WDUhWJyBZo6KbZNmPvvLyzF+DY18VEOP6zR+dTVLdaqvt7pYK3SQ7a/UsGt//CX/6K35VgIWi+iAr5ouY6e9On/3R7FVF5hsatN3dsgHJ6gQka1R0k+xbb5l/Qbtr1xk6nSZPlluvC5Jt9VZbbXe3VOgm2aj1UTT+Yy8+5uTslFKSIrWKkqXW0cGjlWbuHng3rV7b7m7ZgGR1ApI1KrpJNjr6m+vmryQXX7lSz2qmTMmmheq77xbMnGm+BQGXbKu32lJ31yJ0k+yi7Yto/IkLJ/bo2YPVfHD0A1qomu+zdXC5KNmpb0+lzQnRE1YeWRmdEe09wHvow0PV3bULSFYnIFmjoptkIyL2FhRU/POf3+7bV06bL720t6yshu2DyWT+CQmXbKu32lq8+JDYXaPQTbLx++MfCHwgakPUw888TJsJBxL6Du6rNOF2p5so2SEPDfEN8OUdI1aZby6zYNMCsbumAcnqBCRrVHSTrBTZ2eerq+tpfRoamrNzZ+l1QbJa32qrjdBNslIE/i3Qw8uD1qcrv1s5NnSsKFlyblBkEM9MzEuk1pdTXlYPolFAsjoByRoVa0n2l1+ubtv2IyuzG3dxyWp9q602wlqS7dW/17iIcay8+ofVomTvcLmD3aOLRfKxZGoNXR6qHkSjgGR1ApI1KtaSbG1tQ3p6i0mvC5LV+lZbbYS1JOvaw3XSokl8U5Ts3QPvfiL8Cd4Uu9v8I9pX0l9RD6JRQLI6AckaFWtJ9tSpy4cPX2Rl9qEWl6zWt9pqI6wl2YHDB/qNvXErA/ahFpfsqEmjvPp6JRUmsc2nZj/l4u7yXv576kE0CkhWJyBZo2ItydLlPz36V1+Vbdlysrra/J8DcclqfautNsJakg1LDKOH+8uEvwRFBnl4eYiSXbJrSXfX7j7DfCa8NmF08GgnZ6e/zvyregTtApLVCUjWqFhLshTr1xfTipUMS0vXmppr4o8RNL3VVhthLclSTFw4kVasZFhaurrf5S7+GOHVja8O8ht0h8sdlEArWa1/4iUFJKsTkKxRsaJkbTCsKFmbDUhWJyBZowLJigHJqgOS1QlI1qhAsmJAsuqAZHUCkjUqkKwYkKw6IFmdgGSNCiQrBiSrDkhWJyBZowLJigHJqgOS1QlI1qhAsmJAsuqAZHUCkjUqkKwYkKw6IFmdgGSNCiQrBiSrDkhWJ7y9vRVgRDw8PPhTyMvLS252MDAbasQ5gWS1paqqqrS0tLCwMDc3NzMzcxMwCnQ06ZjSkS1txpGPMmZDjTgn5AFZDdbDaJKtrq4uLy+nl7L8/Hya8c+BUaCjSceUjmx5M458lDEbasQ5IQ/IarAeRpOsyWSiK4Vz587RXNNrWh4wCnQ06ZjSka1oxpGPMmZDjTgn5AFZDdbDaJKtq6ujFzGaZXo1o6uGE8Ao0NGkY0pHtroZRz7KmA014pyQB2Q1WA+jSbahoYHml17HaKKrqqr46zywd+ho0jGlI1vXjCMfZcyGGnFOyAOyGqyH0SQLAAA2BSQL7IP/NSHXAmDzQLLAPohuQq4FwOaBZIEd0NjYOLAJKshtANg2kCywA7Kzs9kPe6ggtwFg20CywA6YMWMGkywV5DYAbBtIFtg6V69e7dWrF5MsFWhTzgDAhoFkga2TkZHBDMugTTkDABsGkgW2zoQJE0TJ0qacAYANA8kCm6aystLV1VWULG1SpZwHgK0CyQKbJjU1VTQsgyrlPABsFUgW2DRjxoyRFasoVCnnAWCrQLLAdiktLXV2dpYVqyhUSU1yNgA2CSQLbJe4uDjZr81Qk5wNgE0CyQLbxc/PT5ZrM9QkZwNgk0CywG4gt8pVANg8kCywGyBZYI9AssBugGSBPQLJArsBkgX2CCQL7AZIFtgjkCywGyBZYI9AssBugGSBPQLJArsBkgX2CCQL7AZIFtgjkCywGyBZYI9AssBugGSBPQLJArsBkgX2CCQL7AZIFtgjkCywGyBZYI9AssBugGSBPQLJthAdHX3gwAG51qLk5uamp6cfP35cbgAdAJIF9ggk2wI9h1evXs3Kly9f3r59e1pamgW1u3jxYqWJgICAxsZGuRm0ByQL7BFItgUu2d27d3t5eTEhEkFBQdeuXZOzO0/v3r3DwsKuXLliMpnkNtABIFlgjzi6ZEl5n3322ebNm8vKyrhkH3nkEVpsFhUV1dTUrFy5kuopR+4pQL1OnjyZl5eXlJTEK69evbpr1y4auby8vL6+nnJonODgYCpUVFQIvUFHgWSBPeLQkj1//ryvry9brnp6enLJ/takSFa4dOkS1W/durWlmwpKiIqKcnJyGj9+PKu5cOEC//+paGRaGrMyo6Cg4OYBQIdQIFlghzi0ZOninS7hDx06VFlZGRkZqQiSZdB1fUhIyMCBAy9evCjWS1DH/v3779mzp7a2ltXMmjXL39+flrfkUx8fn1GjRrE0aXzQKSBZYI84tGTJntHR0axcV1cnSZDkO3z48EcfffTs2bO8slWoY0REhFgzaNCg8PDw1U08/fTTzs7O5F+LS3bo0KEty2MHwNvbW54CAGweh5ash4dHYmIi31QECf7rX/+i1ri4uIaGBp5wK6hjcnKyWNOjRw9JECdOnBDHBwA4CA4t2REjRgQFBbEyrVu5BDMyMlxcXHbu3HlT9q1R29Pf3z8tLY2VSdMXLlxoNQ0AYHgcWrLkQRLftGnTlixZ0rt3bybBmpqaPn36jBw5kl3sMzZt2iR3FlDb8+OPP3Z3d4+MjHznnXcCAwP79ev366+/qtMAAIbHoSVLxMfHDxgwgAw7ffr0nj17kgTZd7kk7r//frmngNKaPanG19fXzc0tICBgz549t0oDABgbR5dspxDXtgz+ngAAALQKJNsJ5PWtovTt21dOAgAAAUgWAAA0BJIFAAANgWQBAEBDIFkAANAQSBYAADQEkgUAAA2BZAEAQEMgWQAA0BBIFgAANASSBQAADYFkAQBAQyBZAADQEEgWAAA0BJIFAAANgWQBAEBDIFkAANAQSBYAADQEkgUAAA2BZAEAQEMgWQAA0BBIFgAANASSBQAADYFkAQBAQyBZAADQEEgWAAA0pBXJAgAAsDiQLAAAaAgkCwAAGvL/Ix86VAIX3r4AAAAASUVORK5CYII=" /></p>

4. 上記の状態でd2_ref = d1をした場合の状態は下記のようになる。

<!-- pu:deep/plant_uml/slicing_slicing.pu--><p><img src="data:image/png;base64,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" /></p>

d2.name1\_の値が元のままであるが(これがスライシングである)、その理由は下記の疑似コードが示す通り、
「d2_refの表層型がクラスBaseであるためd1もクラスBase(正確にはBase型へのリファレンス)へ変換された後、
d2_refが指しているオブジェクト(d2)へコピーされた」からである。

```cpp
    d2_ref.Base::operator=(d1);   // Base::operator=(Base const&)が呼び出される
```

次に示すのは、
「オブジェクトの配列をその基底クラスへのポインタに代入し、
そのポインタを配列のように使用した場合に発生する」スライシングと類似の現象である。

```cpp
    //  example/term_explanation/slice_ut.cpp 61

    TEST(Slicing, array)
    {
        Derived d_array[]{{"0", "1"}, {"2", "3"}};
        Base*   b_ptr = d_array;  // この代入までは問題ないが、b_ptr[1]でのアクセスで問題が起こる

        ASSERT_STREQ("0", d_array[0].Name0());  // OK
        ASSERT_STREQ("0", b_ptr[0].Name0());    // OK

        ASSERT_STREQ("2", d_array[1].Name0());  // OK
    #if 0  // スライシングに類似した問題で、以下のテストは失敗する。
        ASSERT_STREQ("2", b_ptr[1].Name0());  // NG
    #else  // こうすればテストは通るが、、、
        ASSERT_STREQ("1", b_ptr[1].Name0());  // NG
    #endif
    }
```

<!-- pu:deep/plant_uml/slicing_array.pu--><p><img src="data:image/png;base64,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" /></p>


## リテラル <a id="SS_19_6"></a>
プログラムに具体的な値を与えるための基本的な即値を指す。
例えば、1, 2, 1.0, true/false, nullptr, "literal string"など。

### 生文字列リテラル <a id="SS_19_6_1"></a>
下記の例にあるように正規表現をそのまま文字列リテラルとして表現するために、
C++11から導入された導入されたリテラル。

```cpp
    //  example/term_explanation/literal_ut.cpp 15

        std::regex raw_re{R"(\d+)"};  // 生文字リテラルで正規表現パターン。\のエスケープが不要
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

### 2進数リテラル <a id="SS_19_6_2"></a>
C++14以降では、0bまたは 0B をプレフィックスとして使うことで、2進数リテラルを表現できる。

```cpp
    //  example/term_explanation/literal_ut.cpp 36

    int bin_value = 0b1101;  // 2進数リテラル  2進数1101 は10進数で 13
    ASSERT_EQ(bin_value, 13);
```

### 数値リテラル <a id="SS_19_6_3"></a>
C++14では区切り文字'を使用し、数値リテラルを記述できるようになった。

```cpp
    //  example/term_explanation/literal_ut.cpp 42

    // 区切り文字を使った数値リテラル
    int large_number = 1'000'000;  // 10進数は3桁で区切るとわかりやすい
    ASSERT_EQ(large_number, 1000000);

    int bin_with_separator = 0b1011'0010;  // 10進数は4桁で区切るとわかりやすい
    ASSERT_EQ(bin_with_separator, 178);    // 2進数 1011 0010 は 10進数で 178

    int hex_with_separator = 0x00'00'ff'ff;  // 16進数は2桁で区切るとわかりやすい
    ASSERT_EQ(hex_with_separator, 65535);    // 16進数 0x00010011 == 65535
```

### ワイド文字列 <a id="SS_19_6_4"></a>
ワイド文字列リテラルを保持する型は下記のように定義された。

* char16_t: UTF-16エンコーディングのコード単位を扱う型。 u"..." というリテラルでUTF-16文字列を表す。
* char32_t: UTF-32エンコーディングのコード単位を扱う型。 U"..." というリテラルでUTF-32文字列を表す。
* char8_t: UTF-8エンコーディングのコード単位を扱う型。 u8"..." というリテラルでUTF-8文字列を表す。

```cpp
    //  example/term_explanation/literal_ut.cpp 59

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

### 16進浮動小数点数リテラル <a id="SS_19_6_5"></a>
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
    //  example/term_explanation/literal_ut.cpp 87

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

### ユーザー定義リテラル <a id="SS_19_6_6"></a>
[ユーザ定義リテラル演算子](term_explanation.md#SS_19_6_6_1)により定義されたリテラルを指す。

#### ユーザ定義リテラル演算子 <a id="SS_19_6_6_1"></a>
ユーザ定義リテラル演算子とは以下のようなものである。

```cpp
    //  example/term_explanation/user_defined_literal_ut.cpp 4

    constexpr int32_t one_km = 1000;

    // ユーザ定義リテラル演算子の定義
    constexpr int32_t operator""_kilo_meter(unsigned long long num_by_mk) { return num_by_mk * one_km; }
    constexpr int32_t operator""_meter(unsigned long long num_by_m) { return num_by_m; }
```
```cpp
    //  example/term_explanation/user_defined_literal_ut.cpp 15

    int32_t km = 3_kilo_meter;  // ユーザ定義リテラル演算子の利用
    int32_t m  = 3000_meter;    // ユーザ定義リテラル演算子の利用

    ASSERT_EQ(m, km);
```

#### std::string型リテラル <a id="SS_19_6_6_2"></a>
"xxx"sとすることで、std::string型のリテラルを作ることができる。

```cpp
    //  example/term_explanation/user_defined_literal_ut.cpp 26

    using namespace std::literals::string_literals;

    auto a = "str"s;  // aはstd::string
    auto b = "str";   // bはconst char*

    static_assert(std::is_same_v<decltype(a), std::string>);
    ASSERT_EQ(std::string{"str"}, a);

    static_assert(std::is_same_v<decltype(b), char const*>);
    ASSERT_STREQ("str", b);
```

#### std::chronoのリテラル <a id="SS_19_6_6_3"></a>
std::chronoのリテラルは以下のコードのように使用できる。

```cpp
    //  example/term_explanation/literal_ut.cpp 109

    using namespace std::chrono_literals;

    static_assert(1s == 1000ms);  // 1秒 (1s) は 1000 ミリ秒 (1000ms) と等しい

    static_assert(1min == 60s);  // 1分 (1min) は 60秒 (60s) と等しい

    static_assert(1h == 3600s);  // 1時間 (1h) は 3600秒 (3600s) と等しい

    static_assert(1.5s == 1500ms);  // 小数点を使った時間リテラル
```

#### std::complexリテラル <a id="SS_19_6_6_4"></a>
std::complexリテラル以下のコードのように使用できる。

```cpp
    //  example/term_explanation/literal_ut.cpp 124

    using namespace std::complex_literals;  // 複素数リテラルを使うための名前空間

    auto a = 1.0 + 2.0i;  // std::complex<double>
    auto b = 3.0 + 4.0i;  // std::complex<double>

    auto result = a + b;
    EXPECT_EQ(result.real(), 4.0);
    EXPECT_EQ(result.imag(), 6.0);
    EXPECT_EQ(result, 4.0 + 6.0i);
```

### ==演算子 <a id="SS_19_6_7"></a>
クラスの==演算子の実装方法には、
[メンバ==演算子](term_explanation.md#SS_19_6_7_1)、[非メンバ==演算子](term_explanation.md#SS_19_6_7_2)の2つの方法がある。

#### メンバ==演算子 <a id="SS_19_6_7_1"></a>
メンバ==演算子には、[非メンバ==演算子](term_explanation.md#SS_19_6_7_2)に比べ、下記のようなメリットがある。

* メンバ変数へのアクセスが容易であるため、より実装が単純になりやすい。
* メンバ変数へのアクセスが容易であるため、パフォーマンスが向上する。
* インライン化し易い。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 12

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
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 232

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        bool operator==(const Integer& other) const noexcept = default;  // 自動生成

    private:
        int x_;
    };
```


#### 非メンバ==演算子 <a id="SS_19_6_7_2"></a>
非メンバ==演算子には、[メンバ==演算子](term_explanation.md#SS_19_6_7_1)に比べ、下記のようなメリットがある。

* クラスをよりコンパクトに記述できるが、その副作用として、
  アクセッサやfriend宣言が必要になることがある。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 56

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        // operator==とoperator<だけを定義
        int get() const noexcept { return x_; }

        // メンバ関数の比較演算子に見えるが、非メンバ関数
        friend bool operator==(const Integer& lhs, const Integer& rhs) noexcept
        {
            return lhs.x_ == rhs.x_;
        }

        friend bool operator<(const Integer& lhs, const Integer& rhs) noexcept
        {
            return lhs.x_ < rhs.x_;
        }

    private:
        int x_;
    };
```

* [暗黙の型変換](term_explanation.md#SS_19_13_1)を利用した以下に示すようなシンプルな記述ができる場合がある。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 84

    auto a = Integer{5};

    ASSERT_TRUE(5 == a);  // 5がInteger{5}に型型変換される
```

すべてのメンバ変数に==演算子が定義されている場合、
C++20以降より、`=default`により==演算子を自動生成させることができるようになった。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 256

    class Integer {
    public:
        Integer(int x) noexcept : x_{x} {}

        friend bool operator==(Integer const& lhs, Integer const& rhs) noexcept;

    private:
        int x_;
    };

    bool operator==(Integer const& lhs, Integer const& rhs) noexcept = default;  // 自動生成
```

### 比較演算子 <a id="SS_19_6_8"></a>
比較演算子とは、[==演算子](--)の他に、!=、 <=、>、>= <、>を指す。
C++20から導入された[<=>演算子](term_explanation.md#SS_19_6_8_3)の定義により、すべてが定義される。

#### std::rel_ops <a id="SS_19_6_8_1"></a>
クラスに`operator==`と`operator<`の2つの演算子が定義されていれば、
それがメンバか否かにかかわらず、他の比較演算子 !=、<=、>、>= はこれらを基に自動的に導出できる。
std::rel_opsでは`operator==`と`operator<=` を基に他の比較演算子を機械的に生成する仕組みが提供されている。

次の例では、std::rel_opsを利用して、少ないコードで全ての比較演算子をサポートする例を示す。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 32

    using namespace std::rel_ops;  // std::rel_opsを使うために名前空間を追加

    auto a = Integer{5};
    auto b = Integer{10};
    auto c = Integer{5};

    // std::rel_opsとは無関係に直接定義
    ASSERT_EQ(a, c);      // a == c
    ASSERT_NE(a, b);      // a != c
    ASSERT_TRUE(a < b);   // aはbより小さい
    ASSERT_FALSE(b < a);  // bはaより小さくない

    // std::rel_ops による!=, <=, >, >=の定義
    ASSERT_TRUE(a != b);   // aとbは異なる
    ASSERT_TRUE(a <= b);   // aはb以下
    ASSERT_TRUE(b > a);    // bはaより大きい
    ASSERT_FALSE(a >= b);  // aはb以上ではない
```

なお、std::rel_opsはC++20から導入された[<=>演算子](term_explanation.md#SS_19_6_8_3)により不要になったため、
非推奨とされた。

#### std::tuppleを使用した比較演算子の実装方法 <a id="SS_19_6_8_2"></a>
クラスのメンバが多い場合、[==演算子](term_explanation.md#SS_19_6_7)で示したような方法は、
可読性、保守性の問題が発生する場合が多い。下記に示す方法はこの問題を幾分緩和する。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 116

    struct Point {
        int x;
        int y;

        bool operator==(const Point& other) const noexcept
        {
            return std::tie(x, y) == std::tie(other.x, other.y);
        }

        bool operator<(const Point& other) const noexcept
        {
            return std::tie(x, y) < std::tie(other.x, other.y);
        }
    };
```
```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 136

        auto a = Point{1, 2};
        auto b = Point{1, 3};
        auto c = Point{1, 2};

        using namespace std::rel_ops;  // std::rel_opsを使うために名前空間を追加

        ASSERT_TRUE(a == c);
        ASSERT_TRUE(a != b);
        ASSERT_TRUE(a < b);
        ASSERT_FALSE(a > b);
```


#### <=>演算子 <a id="SS_19_6_8_3"></a>
「[std::tuppleを使用した比較演算子の実装方法](term_explanation.md#SS_19_6_8_2)」
で示した定型のコードはコンパイラが自動生成するのがC++規格のセオリーである。
このためC++20から導入されたのが<=>演算子`<=>`である。

```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 153

    struct Point {
        int x;
        int y;

        auto operator<=>(const Point& other) const noexcept = default;  // 三方比較演算子 (C++20)
        // 通常autoとするが、実際の戻り型はstd::strong_ordering
    };
```
```cpp
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 166

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
    //  example/term_explanation_cpp20/comparison_operator_ut.cpp 197

    struct Point {
        int x;
        int y;

        std::strong_ordering operator<=>(const Point& other) const noexcept
        {
            return std::tie(x, y) <=> std::tie(other.x, other.y);
        }

        bool operator==(const Point& other) const noexcept
        {
            return std::tie(x, y) == std::tie(other.x, other.y);
        }
    };
```

#### 三方比較演算子 <a id="SS_19_6_8_4"></a>
三方比較演算子とは[<=>演算子](term_explanation.md#SS_19_6_8_3)を指す。

#### spaceship operator <a id="SS_19_6_8_5"></a>
spaceship operatorとは[<=>演算子](term_explanation.md#SS_19_6_8_3)を指す。
この名前は`<=>`が宇宙船に見えることに由来としている。

## 構文 <a id="SS_19_7"></a>
### 属性構文 <a id="SS_19_7_1"></a>
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
    //  example/term_explanation/attr_ut.cpp 10

    // 非推奨の関数
    [[deprecated("この関数は非推奨です。代わりに newFunction を使用してください。")]]  // 
    void oldFunction();  // この関数を呼び出すと警告される
    void newFunction();
```
```cpp
    //  example/term_explanation/attr_ut.cpp 20
    void processValues()
    {
        [[maybe_unused]] int unusedValue = 42;  // 使用しない変数でも警告が出ない

        // do something
    }
```
```cpp
    //  example/term_explanation/attr_ut.cpp 28

    [[nodiscard]] int computeResult() { return 42; }

    //  example/term_explanation/attr_ut.cpp 38

    computeResult();               // 警告が出る：戻り値が無視されている
    int result = computeResult();  // これはOK
```
```cpp
    //  example/term_explanation/attr_ut.cpp 54

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

### 関数tryブロック <a id="SS_19_7_2"></a>
関数tryブロックとはtry-catchを本体とした下記のような関数のブロックを指す。

```cpp
    //  example/term_explanation/func_try_block.cpp 8

    void function_try_block()
    try {  // 関数tryブロック
        // 何らかの処理
        ...
    }
    catch (std::length_error const& e) {  // 関数tryブロックのエクセプションハンドラ
        ...
    }
    catch (std::logic_error const& e) {  // 関数tryブロックのエクセプションハンドラ
        ...
    }
```

### 範囲for文 <a id="SS_19_7_3"></a>
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
    //  example/term_explanation/range_for_ut.cpp 14

    auto list = std::list{1, 2, 3};
    auto oss  = std::stringstream{};

    for (auto a : list) {  // 範囲for文
        oss << a;
    }
    ASSERT_EQ(oss.str(), "123");
```

上記のコードは下記のように展開される。

```cpp
    //  example/term_explanation/range_for_ut.cpp 26

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
    //  example/term_explanation/range_for_ut.cpp 73

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
    //  example/term_explanation/range_for_ut.cpp 87

    delimited_string<','> delimited_str{"Hello,World"};
    std::ostringstream    oss;

    // ',' を終了文字として"Hello" だけをループして出力
    for (auto it = delimited_str.begin(); it != delimited_str.end(); ++it) {
        oss << *it;
    }

    ASSERT_EQ("Hello", oss.str());  // 結果は "Hello" になるはず
```

### 構造化束縛 <a id="SS_19_7_4"></a>
構造化束縛はC++17 から導入されたもので、std::tuppleやstd::pair、std::arrayなど、
構造体のメンバーを個別の変数に分解して簡潔に扱うことをできるようにするための機能である。

```cpp
    //  example/term_explanation/structured_binding_ut.cpp 13

        // tupleでの構造化束縛の例
        std::tuple<int, double, std::string> tobj(1, 2.5, "Hello");

        auto [i, d, s] = tobj;  // 構造化束縛を使用してタプルを分解

        ASSERT_EQ(i, 1);
        ASSERT_DOUBLE_EQ(d, 2.5);
        ASSERT_EQ("Hello", s);
```
```cpp
    //  example/term_explanation/structured_binding_ut.cpp 28

        // pairでの構造化束縛の例
        std::pair<int, std::string> pobj(42, "example");

        auto [i, s] = pobj;  // 構造化束縛を使用してペアを分解

        ASSERT_EQ(i, 42);
        ASSERT_EQ("example", s);
```
```cpp
    //  example/term_explanation/structured_binding_ut.cpp 42

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
    //  example/term_explanation/structured_binding_ut.cpp 72

        auto array = std::array<int, 3>{1, 2, 3};

        auto [x, y, z] = array;  // 構造化束縛を使って std::array の要素を分解

        ASSERT_EQ(x, 1);
        ASSERT_EQ(y, 2);
        ASSERT_EQ(z, 3);
```

### 初期化付きif/switch文 <a id="SS_19_7_5"></a>
C++17で、if文とswitc文に初期化を行う構文が導入された。
これにより、変数をそのスコープ内で初期化し、その変数を条件式の評価に使用できる。
初期化された変数は、if文やswitch文のスコープ内でのみ有効であり、他のスコープには影響を与えない。

この構文は、従来のfor文で使用されていた初期化ステートメントを、if/switch文に拡張したものである。
この類似性が理解しやすいように、本節では、 敢えて以下のコード例で同じ関数、同じクラスを使用し、
対比できるようにした。

- [初期化付きfor文(従来のfor文)](term_explanation.md#SS_19_7_5_1)
- [初期化付きwhile文(従来のwhile文)](term_explanation.md#SS_19_7_5_2)
- [初期化付きif文](term_explanation.md#SS_19_7_5_3)
- [初期化付きswitch文](term_explanation.md#SS_19_7_5_4)


#### 初期化付きfor文(従来のfor文) <a id="SS_19_7_5_1"></a>
下記の疑似コードは従来のfor文の構造を表す。

```cpp
    for (init-statement; condition; post-statement) {
        // ループ処理
    }
```
上記のと同様の実際のfor文のコードを以下に示す。

```cpp
    //  example/term_explanation/if_switch_init_ut.cpp 8

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
    //  example/term_explanation/if_switch_init_ut.cpp 36

    for (auto result = DoOperation(); result.IsError(); result = DoOperation()) {
        RecoverOperation(result.Get());  // エラー処理
    }

    // 以下、成功時の処理
```

#### 初期化付きwhile文(従来のwhile文) <a id="SS_19_7_5_2"></a>
下記の疑似コードこの節で説明しようとしているwhile文の構造を表す(従来からのwhile文)。

```cpp
    while (type-specifier-seq declarator) {
        // 条件がtrueの場合の処理
    }
```

[初期化付きif文](term_explanation.md#SS_19_7_5_3)/[初期化付きswitch文](term_explanation.md#SS_19_7_5_4)はC++17から導入されたシンタックスであるが、
それと同様のシンタックスはwhileには存在しないが、
以下のコード例のように従来の記法は広く知られているため、念とため紹介する。

```cpp
    //  example/term_explanation/if_switch_init_ut.cpp 48

    while (auto result = DoOperation()) {  // resultはboolへの暗黙の型変換が行われる
        // エラー処理
    }
    // resultはスコープアウトする
```

#### 初期化付きif文 <a id="SS_19_7_5_3"></a>
下記の疑似コードこの節で説明しようとしているif文の構造を表す。

```cpp
    if (init-statement; condition) {
        // 条件がtrueの場合の処理
    }
```

上記と同様の構造を持つ実際のif文のコードを以下に示す。

```cpp
    //  example/term_explanation/if_switch_init_ut.cpp 8

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
    //  example/term_explanation/if_switch_init_ut.cpp 59

    if (auto result = DoOperation(); !result.IsError()) {
        // 成功処理
    }
    else {
        RecoverOperation(result.Get());  // エラー処理
    }
    // resultはスコープアウトする
```

クラスの独自の[<=>演算子](term_explanation.md#SS_19_6_8_3)を定義する場合、下記のように使用することができる。

```cpp
    //  example/term_explanation/if_switch_init_ut.cpp 72

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

#### 初期化付きswitch文 <a id="SS_19_7_5_4"></a>
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
    //  example/term_explanation/if_switch_init_ut.cpp 8

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
    //  example/term_explanation/if_switch_init_ut.cpp 103

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

## 言語機能 <a id="SS_19_8"></a>
### コルーチン <a id="SS_19_8_1"></a>
コルーチンはC++20から導入された機能であり、以下の新しいキーワードによりサポートされる。

* [co_await](term_explanation.md#SS_19_8_1_1)
* [co_return](term_explanation.md#SS_19_8_1_2)
* [co_yield](term_explanation.md#SS_19_8_1_3)

#### co_await <a id="SS_19_8_1_1"></a>
co_awaitはコルーチンの非同期操作の一時停止と再開に使用される。
co_waitとco_returnを使用したコードを以下に示す。

```cpp
    //  example/term_explanation_cpp20/co_await_ut.cpp 12

    class Task {  // コルーチンが返す型
    public:
        /// @struct promise_type
        /// @brief コルーチンのライフサイクルを管理する構造体
        struct promise_type {
            /// @brief コルーチンから Task 型のオブジェクトを返す関数
            /// @return Taskオブジェクト
            Task get_return_object()
            {
                return Task{std::coroutine_handle<promise_type>::from_promise(*this)};
            }

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
    //  example/term_explanation_cpp20/co_await_ut.cpp 88

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
    //  example/term_explanation_cpp20/co_await_ut.cpp 118

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
    //  example/term_explanation_cpp20/co_await_ut.cpp 170

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

#### co_return <a id="SS_19_8_1_2"></a>
co_returnはコルーチンの終了時に値を返すために使用される。
co_returnは通常[co_await](term_explanation.md#SS_19_8_1_1)と同時に使われることが多い。

#### co_yield <a id="SS_19_8_1_3"></a>
co_yieldはコルーチンから値を返しつつ、
次の再開ポイントまで処理を中断する。これはジェネレーターの実装に便利である。

```cpp
    //  example/term_explanation_cpp20/co_yield_ut.cpp 12

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
            Generator get_return_object()
            {
                return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};
            }

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
    //  example/term_explanation_cpp20/co_yield_ut.cpp 130

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

[co_await](term_explanation.md#SS_19_8_1_1)、co_returnの例でみたように、
co_yieldを使用したコルーチンと同じ機能を持つクラスのco_yieldを使わない実装を以下に示す。

```cpp
    //  example/term_explanation_cpp20/co_yield_ut.cpp 155

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
    //  example/term_explanation_cpp20/co_yield_ut.cpp 237

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

### モジュール <a id="SS_19_8_2"></a>
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

### ラムダ式 <a id="SS_19_8_3"></a>
ラムダ式に関する言葉の定義と例を示す。

* ラムダ式とは、その場で関数オブジェクトを定義する式。
* クロージャ(オブジェクト)とは、ラムダ式から生成された関数オブジェクト。
* クロージャ型とは、クロージャオブジェクトの型。
* キャプチャとは、ラムダ式外部の変数をラムダ式内にコピーかリファレンスとして定義する機能。
* ラムダ式からキャプチャできるのは、ラムダ式から可視である自動変数と仮引数(thisを含む)。
* [constexprラムダ](term_explanation.md#SS_19_4_7)とはクロージャ型の[constexprインスタンス](term_explanation.md#SS_19_4_5)。
* [ジェネリックラムダ](term_explanation.md#SS_19_11_4)とは、C++11のラムダ式を拡張して、
  パラメータにautoを使用(型推測)できるようにした機能。

```cpp
    //  example/term_explanation/lambda.cpp 10

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

#### クロージャ <a id="SS_19_8_3_1"></a>
「[ラムダ式](term_explanation.md#SS_19_8_3)」を参照せよ。

#### クロージャ型 <a id="SS_19_8_3_2"></a>
「[ラムダ式](term_explanation.md#SS_19_8_3)」を参照せよ。

#### 一時的ラムダ <a id="SS_19_8_3_3"></a>
一時的ラムダ(transient lambda)とは下記のような使い方をするラムダ式指す慣用用語である。

複雑な初期化を必要とするconstオブジェクトの生成をするような場合に有用なテクニックである。

```cpp
    //  example/term_explanation/transient_lambda_ut.cpp 9

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

#### transient lambda <a id="SS_19_8_3_4"></a>
「[一時的ラムダ](term_explanation.md#SS_19_8_3_3)」を参照せよ。


### 指示付き初期化 <a id="SS_19_8_4"></a>
指示付き初期化(designated initialization)とは、C++20から導入されたシンタックスであり、
構造体やクラスのメンバを明示的に指定して初期化できるようにする機能である。
この構文により、コードの可読性と安全性が向上し、初期化漏れや順序の誤りを防ぐことができる。

まずは、この機能を有効に使えるクラス例を以下に示す。

```cpp
    //  example/term_explanation_cpp20/designated_init_ut.cpp 11

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
    //  example/term_explanation_cpp20/designated_init_ut.cpp 41

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

下記に示すように、[Polymorphic Memory Resource(pmr)](dynamic_memory_allocation.md#SS_14_5)のpool_resourceの初期化には、
この機能を使うと可読性の改善が期待できる。

```cpp
    //  example/term_explanation_cpp20/designated_init_ut.cpp 68

    std::pmr::unsynchronized_pool_resource pool_resource(
        std::pmr::pool_options{
            .max_blocks_per_chunk        = 10,  // チャンクあたりの最大ブロック数
            .largest_required_pool_block = 1024  // 最大ブロックサイズ
        },
        std::pmr::new_delete_resource()  // フォールバックリソース
    );

    std::pmr::vector<int> vec{&pool_resource};  // pmrを使用するベクタの定義
```

指示付き初期化を使わない以下のコード例と上記を比べれば可読性の改善に議論の余地はないだろう。

```cpp
    //  example/term_explanation_cpp20/designated_init_ut.cpp 83

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

## プログラミング概念と標準ライブラリ <a id="SS_19_9"></a>
### スマートポインタ <a id="SS_19_9_1"></a>
スマートポインタは、C++標準ライブラリが提供するメモリ管理クラス群を指す。
生のポインタの代わりに使用され、リソース管理を容易にし、
メモリリークや二重解放といった問題を防ぐことを目的としている。

スマートポインタは通常、所有権とスコープに基づいてメモリの解放を自動的に行う。
C++標準ライブラリでは、主に以下の3種類のスマートポインタが提供されている。

* **`std::unique_ptr`** 
   はダイナミックにアロケートされた[オブジェクトの排他所有](term_explanation.md#SS_19_5_7_1)を表すために用いられる。  
* **`std::shared_ptr`** 
   はダイナミックにアロケート[オブジェクトの共有所有](term_explanation.md#SS_19_5_7_2)を表現、管理するために用いられる。   
* **[std::weak_ptr](term_explanation.md#SS_19_5_7_4)**
   は`std::shared_ptr`と組み合わせて使用される補助的なスマートポインタである。
   参照カウントに影響を与えず、[オブジェクトの循環所有](term_explanation.md#SS_19_5_7_3)よるメモリリークを防ぐために用いられる。
   std::weak_ptr`はリソースへの弱い参照を保持し、リソースの有効性を確認する際に使用される。  
* `std::auto_ptr`はC++11以前に導入された初期のスマートポインタであるが、
   異常な[copyセマンティクス](term_explanation.md#SS_19_17_2)を持つため、多くの誤用を生み出し、
   C++11から非推奨とされ、C++17から規格から排除された。

### コンテナ <a id="SS_19_9_2"></a>
データを格納し、
効率的に操作するための汎用的なデータ構造を提供するC++標準ライブラリの下記のようなクラス群である。

* [シーケンスコンテナ(Sequence Containers)](term_explanation.md#SS_19_9_2_1)
* [連想コンテナ(Associative Containers)(---)
* [無順序連想コンテナ(Unordered Associative Containers)](term_explanation.md#SS_19_9_2_3)
* [コンテナアダプタ(Container Adapters)](term_explanation.md#SS_19_9_2_4)
* [特殊なコンテナ](term_explanation.md#SS_19_9_2_5)

#### シーケンスコンテナ(Sequence Containers) <a id="SS_19_9_2_1"></a>
データが挿入順に保持され、順序が重要な場合に使用する。

| コンテナ                 | 説明                                                                |
|--------------------------|---------------------------------------------------------------------|
| `std::vector`            | 動的な配列で、ランダムアクセスが高速。末尾への挿入/削除が効率的     |
| `std::deque`             | 両端に効率的な挿入/削除が可能な動的配列                             |
| `std::list`              | 双方向リスト。要素の順序を維持し、中間の挿入/削除が効率的           |
| [std::forward_list](term_explanation.md#SS_19_9_2_1_1) | 単方向リスト。軽量だが、双方向の操作はできない                      |
| `std::array`             | 固定長配列で、サイズがコンパイル時に決まる                          |
| `std::string`            | 可変長の文字列を管理するクラス(厳密には`std::basic_string`の特殊化) |

##### std::forward_list <a id="SS_19_9_2_1_1"></a>

```cpp
    //  example/term_explanation/cotainer_ut.cpp 14

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

#### 連想コンテナ(Associative Containers) <a id="SS_19_9_2_2"></a>
データがキーに基づいて自動的にソートされ、検索が高速である。

| コンテナ           | 説明                                             |
|--------------------|--------------------------------------------------|
| `std::set`         | 要素がソートされ、重複が許されない集合           |
| `std::multiset`    | ソートされるが、重複が許される集合               |
| `std::map`         | ソートされたキーと値のペアを保持。キーは一意     |
| `std::multimap`    | ソートされたキーと値のペアを保持。キーは重複可能 |

#### 無順序連想コンテナ(Unordered Associative Containers) <a id="SS_19_9_2_3"></a>
ハッシュテーブルを基盤としたコンテナで、順序を保証しないが高速な検索を提供する。

| コンテナ                  | 説明                                                   |
|---------------------------|--------------------------------------------------------|
| [std::unordered_set](term_explanation.md#SS_19_9_2_3_1) | ハッシュテーブルベースの集合。重複は許されない         |
| `std::unordered_multiset` | ハッシュテーブルベースの集合。重複が許される           |
| [std::unordered_map](term_explanation.md#SS_19_9_2_3_2) | ハッシュテーブルベースのキーと値のペア。キーは一意     |
| `std::unordered_multimap` | ハッシュテーブルベースのキーと値のペア。キーは重複可能 |
| [std::type_index](term_explanation.md#SS_19_9_2_3_3)    | 型情報型を連想コンテナのキーとして使用するためのクラス |

##### std::unordered_set <a id="SS_19_9_2_3_1"></a>

```cpp
    //  example/term_explanation/cotainer_ut.cpp 32

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

##### std::unordered_map <a id="SS_19_9_2_3_2"></a>

```cpp
    //  example/term_explanation/cotainer_ut.cpp 52

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

##### std::type_index <a id="SS_19_9_2_3_3"></a>
std::type_indexはコンテナではないが、
型情報型を連想コンテナのキーとして使用するためのクラスであるため、この場所に掲載する。

```cpp
    //  example/term_explanation/cotainer_ut.cpp 74

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


#### コンテナアダプタ(Container Adapters) <a id="SS_19_9_2_4"></a>
特定の操作のみを公開するためのラッパーコンテナ。

| コンテナ              | 説明                                     |
|-----------------------|------------------------------------------|
| `std::stack`          | LIFO(後入れ先出し)操作を提供するアダプタ |
| `std::queue`          | FIFO(先入れ先出し)操作を提供するアダプタ |
| `std::priority_queue` | 優先度に基づく操作を提供するアダプタ     |

#### 特殊なコンテナ <a id="SS_19_9_2_5"></a>
上記したようなコンテナとは一線を画すが、特定の用途や目的のために設計された一種のコンテナ。

| コンテナ             | 説明                                                       |
|----------------------|------------------------------------------------------------|
| `std::span`          | 生ポインタや配列を抽象化し、安全に操作するための軽量ビュー |
| `std::bitset`        | 固定長のビット集合を管理するクラス                         |
| `std::basic_string`  | カスタム文字型をサポートする文字列コンテナ                 |

### std::optional <a id="SS_19_9_3"></a>
C++17から導入されたstd::optionalには、以下のような2つの用途がある。
以下の用途2から、
このクラスがオブジェクトのダイナミックなメモリアロケーションを行うような印象を受けるが、
そのようなことは行わない。
このクラスがオブジェクトのダイナミックな生成が必要になった場合、プレースメントnewを実行する。
ただし、std::optionalが保持する型自身がnewを実行する場合は、この限りではない。

1. 関数の任意の型の[戻り値の無効表現](term_explanation.md#SS_19_9_3_1)を持たせる
2. [オブジェクトの遅延初期化](term_explanation.md#SS_19_9_3_2)する(初期化処理が重く、
   条件によってはそれが無駄になる場合にこの機能を使う)

#### 戻り値の無効表現 <a id="SS_19_9_3_1"></a>
```cpp
    //  example/term_explanation/optional_ut.cpp 11

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
    //  example/term_explanation/optional_ut.cpp 28

    auto ret0 = file_extension("xxx.yyy");

    ASSERT_TRUE(ret0);  // 値を保持している
    ASSERT_EQ("yyy", *ret0);

    auto ret1 = file_extension("xxx");

    ASSERT_FALSE(ret1);  // 値を保持していない
    // ASSERT_THROW(*ret1, std::exception);  // 未定義動作(エクセプションは発生しない)
    ASSERT_THROW(ret1.value(), std::bad_optional_access);  // 値非保持の場合、エクセプション発生
```

#### オブジェクトの遅延初期化 <a id="SS_19_9_3_2"></a>
```cpp
    //  example/term_explanation/optional_ut.cpp 43

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
    //  example/term_explanation/optional_ut.cpp 64

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

### std::variant <a id="SS_19_9_4"></a>
std::variantは、C++17で導入された型安全なunionである。
このクラスは複数の型のうち1つの値を保持することができ、
従来のunionに伴う低レベルな操作の安全性の問題を解消するために設計された。

std::variant自身では、オブジェクトのダイナミックな生成が必要な場合でも通常のnewを実行せず、
代わりにプレースメントnewを用いる
(以下のコード例のようにstd::variantが保持する型自身がnewを実行する場合は、この限りではない)。

以下にstd::variantの典型的な使用例を示す。

```cpp
    //  example/term_explanation/variant_ut.cpp 13

    std::variant<int, std::string, double> var = 10;
    auto var2 = var;  // コピーコンストラクタの呼び出し

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

std::variantとstd::visit([Visitor](design_pattern.md#SS_9_20)パターンの実装の一種)を組み合わせた場合の使用例を以下に示す。

```cpp
    //  example/term_explanation/variant_ut.cpp 37

    void output_from_variant(std::variant<int, double, std::string> const& var, std::ostringstream& oss)
    {
        std::visit([&oss](auto&& arg) { oss.str().empty() ? oss << arg : oss << "|" << arg; }, var);
    }
```
```cpp
    //  example/term_explanation/variant_ut.cpp 47

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

## name lookupと名前空間 <a id="SS_19_10"></a>
ここではname lookupとそれに影響を与える名前空間について解説する。

### ルックアップ <a id="SS_19_10_1"></a>
このドキュメントでのルックアップとは[name lookup](term_explanation.md#SS_19_10_2)を指す。

### name lookup <a id="SS_19_10_2"></a>
[name lookup](https://en.cppreference.com/w/cpp/language/lookup)
とはソースコードで名前が検出された時に、その名前をその宣言と関連付けることである。
以下、name lookupの例を上げる。

下記のようなコードがあった場合、

```cpp
    //  example/term_explanation/name_lookup_ut.cpp 5

    namespace NS_LU {
    int f() noexcept { return 0; }
    }  // namespace NS_LU
```

以下のコードでの関数呼び出しf()のname lookupは、


```cpp
    //  example/term_explanation/name_lookup_ut.cpp 29

    NS_LU::f();
```

1. NS_LUをその前方で宣言された名前空間と関連付けする
2. f()呼び出しをその前方の名前空間NS_LUで宣言された関数fと関連付ける

という手順で行われる。

下記のようなコードがあった場合、

```cpp
    //  example/term_explanation/name_lookup_ut.cpp 11

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
    //  example/term_explanation/name_lookup_ut.cpp 37
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
    //  example/term_explanation/name_lookup_ut.cpp 44

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
    //  example/term_explanation/name_lookup_ut.cpp 65

    auto x = NS_LU::X{1};

    ASSERT_EQ("1 in NS_LU", ToString(x));
```

1. ToString()呼び出しの引数xの型Xが名前空間NS_LUで定義されているため、
   ToStringを探索する名前空間にNS_LUを組み入れる(「[関連名前空間](term_explanation.md#SS_19_10_6)」参照)
2. ToString()呼び出しより前方で宣言されたグローバル名前空間とNS_LUの中から、
   複数のToStringの定義を見つける
3. ToString()呼び出しを、
   すでに見つけたToStringの中からベストマッチしたNS_LU::ToStringと関連付ける

という手順で行われる。


### two phase name lookup <a id="SS_19_10_3"></a>
[two phase name lookup](https://en.cppreference.com/w/cpp/language/two-phase_lookup)
とはテンプレートをインスタンス化するときに使用される、下記のような2段階でのname lookupである。

1. テンプレート定義内でname lookupを行う(通常のname lookupと同じ)。
   この時、テンプレートパラメータに依存した名前
   ([dependent_name](https://en.cppreference.com/w/cpp/language/dependent_name))は
   name lookupの対象外となる(name lookupの対象が確定しないため)。
2. 1の後、テンプレートパラメータを展開した関数内で、
   [関連名前空間](term_explanation.md#SS_19_10_6)の宣言も含めたname lookupを行う。

以下の議論では、

* 上記1のname lookupを1st name lookup
* 上記2のname lookupを2nd name lookup

と呼ぶことにする。

下記のようなコードがあった場合、

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 5

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
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 44

    auto x = NS_TPLU::X{1};

    ASSERT_EQ("type:X", TypeName(x));
```

1. TypeName()呼び出しの引数xの型Xが名前空間NS_TPLUで宣言されているため、
   NS_TPLUをTypeNameを探索する[関連名前空間](term_explanation.md#SS_19_10_6)にする。
2. TypeName()呼び出しより前方で宣言されたグローバル名前空間とNS_TPLUの中からTypeNameを見つける。
3. TypeNameは関数テンプレートであるためtwo phase lookupが以下のように行われる。
    1. TypeName内でのHeader(int{})の呼び出しは、1st name lookupにより、
       Header(long)の宣言と関連付けられる。
       Header(int)はHeader(long)よりもマッチ率が高い、
       TypeNameの定義より後方で宣言されているため、name lookupの対象外となる。
    2. TypeName内でのToType(t)の呼び出しに対しては、2nd name lookupが行われる。
       このためTypeName定義より前方で宣言されたグローバル名前空間と、
       tの型がNS_TPLU::Xであるため[関連名前空間](term_explanation.md#SS_19_10_6)となったNS_TPLUがname lookupの対象となるが、
       グローバル名前空間内のToTypeは、
       NS_TPLU内でTypeNameより前に宣言されたtemplate<> ToTypeによって[name-hiding](term_explanation.md#SS_19_10_9)が起こり、
       TypeNameからは非可視となるためname lookupの対象から外れる。
       このため、ToType(t)の呼び出しは、NS_TPLU::ToType(X const&)の宣言と関連付けられる。

という手順で行われる。

上と同じ定義、宣言がある場合の以下のコードでのTypeNameのインスタンス化に伴うname lookupは、

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 50

    ASSERT_EQ("type:unknown", NS_TPLU::TypeName(int{}));
```

1. NS_TPLUを名前空間と関連付けする
   (引数の型がintなのでNS_TPLUは[関連名前空間](term_explanation.md#SS_19_10_6)とならず、NS_TPLUを明示する必要がある)。
2. TypeName()呼び出しより前方で宣言されたNS_TPLUの中からTypeNameを見つける。
3. TypeNameは関数テンプレートであるためtwo phase lookupが以下のように行われる。
    1. TypeName内でのHeader(int{})の呼び出しは、1st name lookupにより、
       前例と同じ理由で、Header(long)の宣言と関連付けられる。
    2. TypeName内でのToType(t)の呼び出しに対しては、2nd name lookupが行われる。
       tの型がintであるためNS_TPLUは[関連名前空間](term_explanation.md#SS_19_10_6)とならず、通常のname lookupと同様に
       ToType(t)の呼び出し前方のグローバル名前空間とNS_TPLUがname lookupの対象になるが、
       グローバル名前空間内のToTypeは、
       NS_TPLU内でTypeNameより前に宣言されたtemplate<> ToTypeによって[name-hiding](term_explanation.md#SS_19_10_9)が起こり、
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
サンプルコードを[g++](term_explanation.md#SS_19_19_1)と[clang++](term_explanation.md#SS_19_19_2)でコンパイルしている)。

以下に、two phase lookupにまつわるさらに驚くべきコード例を紹介する。
上と同じ定義、宣言がある場合の以下のコードの動作を考える。

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 54

    ASSERT_EQ("type:long", NS_TPLU::TypeName(long{}));
```

NS_TPLU::TypeName(int{})のintをlongにしただけなので、この単体テストはパスしないが、
この単体テストコードの後(実際にはこのファイルのコンパイル単位の中のNS_TPLU内で、
且つtemplate<> ToTypeの宣言の後方であればどこでもよい)
に以下のコードを追加するとパスしてしまう。

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 61

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
[g++](term_explanation.md#SS_19_19_1)/[clang++](term_explanation.md#SS_19_19_2)両方ともこのコードを警告なしでコンパイルする)。

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
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 71

    namespace NS_TPLU2 {
    struct Y {
        int i;
    };
    }  // namespace NS_TPLU2
```
```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 79

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
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 100

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
    * TypeName呼び出しより前方にある[関連名前空間](term_explanation.md#SS_19_10_6)内の宣言

この認識に基づくNS_TPLU2::Yに対するグローバルなTypeName内でのtwo phase name lookupは、

1. TypeName内に1st name lookupの対象がないため何もしない。
2. TypeName内の2nd name lookupに使用される[関連名前空間](term_explanation.md#SS_19_10_6)NS_TPLU2は、
   ToType(NS_TPLU2::Y const&)の宣言を含まないため、この宣言は2nd name lookupの対象とならない。
   その結果、ToType(t)の呼び出しは関数テンプレートToType(T const&)と関連付けられる。

という手順で行われる。

以上が、TypeNameからToType(NS_TPLU2::Y const&)が使われない理由である。

ここまでで示したようにtwo phase name lookupは理解しがたく、
理解したとしてもその使いこなしはさらに難しい。

次のコードは、この難解さに翻弄されるのが現場のプログラマのみではないことを示す。

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 71

    namespace NS_TPLU2 {
    struct Y {
        int i;
    };
    }  // namespace NS_TPLU2
```
```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 110

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
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 132

    auto y = NS_TPLU2::Y{1};

    ASSERT_EQ(1, y + 0);  // 2つ目のoperator+が選択される
```

このテストは当然パスするが、次はどうだろう？

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 142

    auto y = NS_TPLU2::Y{1};

    ASSERT_EQ(1, TypeNum(y));  // g++ではoperator+(NS_TPLU2::Y const&, int i)がname lookupされる
```

これまでのtwo phase name lookupの説明では、
operator+(NS_TPLU2::Y const& y, int i)はTypeNum内でのname lookupの対象にはならないため、
このテストはエラーとならなければならないが、[g++](term_explanation.md#SS_19_19_1)ではパスしてしまう。
2nd name lookupのロジックにバグがあるようである。

有難いことに、[clang++](term_explanation.md#SS_19_19_2)では仕様通りこのテストはエラーとなり、
当然ながら以下のテストはパスする(つまり、g++ではエラーする)。

```cpp
    //  example/term_explanation/two_phase_name_lookup_ut.cpp 151

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


### 実引数依存探索 <a id="SS_19_10_4"></a>
実引数依存探索とは、argument-dependent lookupの和訳語であり、
通常はその略語である[ADL](term_explanation.md#SS_19_10_5)と呼ばれる。

### ADL <a id="SS_19_10_5"></a>
ADLとは、関数の実引数の型が宣言されている名前空間(これを[関連名前空間](term_explanation.md#SS_19_10_6)と呼ぶ)内の宣言が、
その関数の[name lookup](term_explanation.md#SS_19_10_2)の対象になることである。

下記のようなコードがあった場合、

```cpp
    //  example/term_explanation/name_lookup_adl_ut.cpp 5
    namespace NS_ADL {
    struct A {
        int i;
    };

    std::string ToString(A const& a) { return std::string{"A:"} + std::to_string(a.i); }
    }  // namespace NS_ADL
```

以下のコードでのToStringの呼び出しに対するのname lookupは、

```cpp
    //  example/term_explanation/name_lookup_adl_ut.cpp 18

    auto a = NS_ADL::A{0};

    ASSERT_EQ("A:0", ToString(a));  // ADLの効果により、ToStringはNS_ADLを指定しなくても見つかる
```

* ToStringの呼び出しより前方で行われているグローバル名前空間内の宣言
* ToStringの呼び出しより前方で行われているNS_ADL内の宣言

の両方を対象として行われる。
NS_ADL内の宣言がToStringの呼び出しに対するのname lookupの対象になる理由は、
ToStringの呼び出しに使われている実引数aの型AがNS_ADLで宣言されているからである。
すでに述べたようにこれをADLと呼び、この場合のNS_ADLを[関連名前空間](term_explanation.md#SS_19_10_6)と呼ぶ。

ADLは思わぬname lookupによるバグを誘発することもあるが、
下記コードを見れば明らかなように、また、
多くのプログラマはそれと気づかずに使っていることからもわかる通り、
コードをより自然に、より簡潔に記述するための重要な機能となっている。

```cpp
    //  example/term_explanation/name_lookup_adl_ut.cpp 28

    // 下記operator <<は、std::operator<<(ostream&, string const&)であり、
    // namespace stdで定義されている。

    // ADLがあるため、operator <<は名前空間修飾無しで呼び出せる。
    std::cout << std::string{__func__};

    // ADLが無いと下記のような呼び出しになる。
    std::operator<<(std::cout, std::string{__func__});
```

### 関連名前空間 <a id="SS_19_10_6"></a>
関連名前空間(associated namespace)とは、
[ADL](term_explanation.md#SS_19_10_5)(実引数依存探索)によってname lookupの対象になった宣言を含む名前空間のことである。


### 修飾付き関数呼び出し <a id="SS_19_10_7"></a>
修飾付き関数呼び出し(Qualified Call)は、
C++で関数やメンバ関数を明示的にスコープやクラス名で修飾して呼び出す方法である。
名前の曖昧性を回避し、特定の関数やクラスメンバを明確に選択する際に利用される。
これにより、意図しない[name lookup](term_explanation.md#SS_19_10_2)を回避することができるため、可読性と安全性が向上する。
一方で、[ADL](term_explanation.md#SS_19_10_5)が働かなくなるため、フレキシブルな[name lookup](term_explanation.md#SS_19_10_2)ができなくなる。

```cpp
    //  example/term_explanation/etc_ut.cpp 68

    A::func();  // 名前空間名による修飾

    struct Derived : Base {
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

### hidden-friend関数 <a id="SS_19_10_8"></a>
hidden-friend関数(隠れたフレンド関数、あるいは単にhidden-friend)とは、

* クラスの内部で定義された、
* 名前空間スコープでの通常の[name lookup](term_explanation.md#SS_19_10_2)できず、[ADL](term_explanation.md#SS_19_10_5)のみでname lookupできる

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
    //  example/term_explanation/hidden_friend_ut.cpp 7

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
    //  example/term_explanation/hidden_friend_ut.cpp 31

    NS::Person         alice("Alice", 30);
    std::ostringstream oss;

    oss << alice;  // フレンド関数を呼び出す(ADLによって見つかる)
    ASSERT_EQ("Name:Alice, Age:30", oss.str());

    // 以下はエラー（operator<<がNS名前空間スコープで見えない）
    // NS::Person::operator<<(oss, alice);
    // 上記は以下のようなコンパイルエラーになる
    //  error: ‘operator<<’ is not a member of ‘NS::Person’
```


### name-hiding <a id="SS_19_10_9"></a>
name-hidingとは
「前方の識別子が、その後方に同一の名前をもつ識別子があるために、
[name lookup](term_explanation.md#SS_19_10_2)の対象外になる」現象一般をを指す通称である
([namespace](https://en.cppreference.com/w/cpp/language/namespace)参照)。

まずは、クラスとその派生クラスでのname-hidingの例を示す。

```cpp
    //  example/term_explanation/name_hiding.cpp 4

    struct Base {
        void f() noexcept {}
    };

    struct Derived : Base {
        // void f(int) { f(); }     // f()では、Baseのf()をname lookupできないため、
        void f(int) noexcept { Base::f(); }  // Base::でf()を修飾した
    };
```

上記の関数fは一見オーバーロードに見えるが、そうではない。下記のコードで示したように、
Base::f()には、修飾しない形式でのDerivedクラス経由のアクセスはできない。

```cpp
    //  example/term_explanation/name_hiding.cpp 18

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

下記のように[using宣言](term_explanation.md#SS_19_10_14)を使用することで、
修飾しない形式でのDerivedクラス経由のBase::f()へのアクセスが可能となる。

```cpp
    //  example/term_explanation/name_hiding.cpp 34

    struct Derived : Base {
        using Base::f;  // using宣言によりDerivedにBase::fを導入
        void f(int) noexcept { Base::f(); }
    };
```
```cpp
    //  example/term_explanation/name_hiding.cpp 45

    auto d = Derived{};
    d.f();  // using宣言によりコンパイルできる
```

下記コードは、名前空間でも似たような現象が起こることを示している。

```cpp
    //  example/term_explanation/name_hiding.cpp 54

    // global名前空間
    void f() noexcept {}

    namespace NS_A {
    void f(int) noexcept {}

    void g() noexcept
    {
    #if 0
        f();  // NS_A::fによりname-hidingされたため、コンパイルできない
    #endif
    }
    }  // namespace NS_A
```

この問題に対しては、下記のようにf(int)の定義位置を後方に移動することで回避できる。

```cpp
    //  example/term_explanation/name_hiding.cpp 70

    namespace NS_A_fixed_0 {
    void g() noexcept
    {
        // グローバルなfの呼び出し
        f();  // NS_A::fは後方に移動されたためコンパイルできる
    }

    void f(int) noexcept {}
    }  // namespace NS_A_fixed_0
```

また、先述のクラスでの方法と同様にusing宣言を使い、下記のようにすることもできる。

```cpp
    //  example/term_explanation/name_hiding.cpp 82

    namespace NS_A_fixed_1 {
    void f(int) noexcept {}

    void g() noexcept
    {
        using ::f;

        // グローバルなfの呼び出し
        f();  // using宣言によりコンパイルできる
    }
    }  // namespace NS_A_fixed_1
```

当然ながら、下記のようにf()の呼び出しを::で修飾することもできる。

```cpp
    //  example/term_explanation/name_hiding.cpp 96

    namespace NS_A_fixed_2 {
    void f(int) noexcept {}

    void g() noexcept
    {
        // グローバルなfの呼び出し
        ::f();  // ::で修飾すればコンパイルできる
    }
    }  // namespace NS_A_fixed_2
```

修飾の副作用として「[two phase name lookup](term_explanation.md#SS_19_10_3)」の例で示したような
[ADL](term_explanation.md#SS_19_10_5)を利用した高度な静的ディスパッチが使用できなくなるが、
通常のソフトウェア開発では、ADLが必要な場面は限られているため、
デフォルトでは名前空間を使用して修飾を行うことにするのが、
無用の混乱をさけるための安全な記法であると言えるだろう。

次に、そういった混乱を引き起こすであろうコードを示す。

```cpp
    //  example/term_explanation/name_hiding.cpp 108

    namespace NS_B {
    struct S_in_B {};

    void f(S_in_B) noexcept {}
    void f(int) noexcept {}

    namespace NS_B_Inner {
    void g() noexcept
    {
        f(int{});  // コンパイルでき、NS_B::f(int)が呼ばれる
    }

    void f() noexcept {}

    void h() noexcept
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

### ダイヤモンド継承 <a id="SS_19_10_10"></a>
ダイヤモンド継承(Diamond Inheritance)とは、以下のような構造のクラス継承を指す。

* 基底クラス(Base)が一つ存在し、その基底クラスから二つのクラス(Derived_0、Derived_1)が派生する。
* Derived_0とDerived_1からさらに一つのクラス(DerivedDerived)が派生する。
  したがって、DerivedDerivedはBaseの孫クラスとなる。

この継承は、多重継承の一形態であり、クラス図で表すと下記のようになるため、
ダイヤモンド継承と呼ばれる。

<!-- pu:deep/plant_uml/diamond_inheritance.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPUAAAEVCAIAAAC34DQEAAAAKnRFWHRjb3B5bGVmdABHZW5lcmF0ZWQgYnkgaHR0cHM6Ly9wbGFudHVtbC5jb212zsofAAAA+mlUWHRwbGFudHVtbAABAAAAeJx9T0tLw0AQvs+vmGN7SNmmtpQ9SKlVYU0w2IdHGZM1rCSTso+A/95VY4sinr6Z78XMynmyPrQNQNmQc7gmp4dxo63pdfUkfu3Tn/sAACc/JuGYXH5VnUJ/kAMMyrn+X1kArDRXnycXDbHf5xn22jrTMU4nqUjnEzF6jDlFjGKJIpWzuZwtUG13+CGPYXRbZOi6YEuNlXHemufgY34MinrCh8DetFri/VGz2tx9E3jNvbEdt5o9qEN+NiwukrXxuNU2XoKHPL7wQqHxMVF2leFa4n53kywhI64D1bH7leCqi732TaIq4B3AVn+0gSH8eAAAIuxJREFUeF7tnQtYFWX+x9NH89qaJoaWEmoKAh7/cvECqCCY5gU0/wX/ahFD09W0wGRRMqmgFLzUQuEtYEUFBFQUvOElTHRXVtb7hou7aGoKCceeLtpj+/96pmaH950Dh8McPWfm93nm4Znzvu+8876/98PMO8Mw55H/EIR6eYRNIAgVQX4Taob8JtQM+U2oGfKbUDPkN6FmyG8Zamtrly9fnpCQEG9TfPDBB4cPH2Y7o23IbxkSExOvXLmit0FycnKysrLY/mgY8lsGHAtZcWwHNJ7tj4Yhv2Wwab+XLVvG9kfDkN8ykN+qgfyWoWG/a27VZO/MiZg/c9jI4U6uzvb29s6uA3z8fN6Imrd3/966ujp2gwcL+S2F/JbBmN+36mrTcjM8fbw8hntGRL++IufjDQcy8k4V4CfWkeLh7ek9wqewqJDd8gFCfkshv2WQ9fvazethc8Pd3Ae+82kcnDa2IFfnPijq7QW3bt1iq3ggkN9SyG8ZeL8h93PBY0dPDNh0LJt3mllQJnDSmBdDXnooipPfUshvGRi/MS3BkRtyby3fztssu6Dkc0FjFy5cKK3nwUB+SyG/ZWD8xpwb05LMUpkj99K174f84f9mLZmz+S9bmSyUd/d03717t7SqioqKcgPnzp375ptvpFlKQX5LIb9lkPpdc6vGy2eI7Jx78vSpj/yGQ79nNh/PYe3/7H0/fz/pHZVJkyZ16tTJ0dGxe/fubdq08ff3P336tJirCOS3FPJbBqnf2TtzPLw9ebmXb1nZokWLkDkvbzya5fv8SCj+f3Nf4Yv5jPApLi4Wa4Pfb775prBeWVkJv4cMGSLmKgL5LYX8lkHqd8T8mTOiX+fFHRcy/vEnHhdm5Gv2bIDfT/fuyRd7853ImJgYsTap32DdunWdO3cWP2LGsnfv3i+//JK5MD148ODWrVv/+c9/iik3btzYt29fYWHh9evXJQXvQ35LIb9lkPo9bOSwFdkf8+I+09/Ry3+o+NGuezconlmaxRRLyUsNCAgQa5P6ffnyZWRNnjxZ+Lhz585u3br5+fm5uLgMHjxYFHfChAk4xqNY165d169fj5TDhw87ODgEBgYiq0ePHgcOHBBKCpDfUshvGaR+O7k4bTj4Z97vdh3ajwsdz6czS/qhTTqdTqwNftvZ2bm6uvbp06ddu3YzZ87EkVjIwk43btyIFczXPT09V69ejXVchrZs2bK6uhrrJ0+exK9ETU1Nz549ExIShK1WrVrVt2/f2traX3dAfteH/JZB6vfTPZ/O+ds2XtwWLVsEh0/h09nlZEGvXr3E2uB3eHh4eXn5sWPHNmzY4Obm9vvf/17M/de//lVQULBmzRpfX9/IyEikwGzoGxwcjGO2UAbTEpwoYP+nBuA3PkJ9sRLyWwr5LYPUb2dXZ9njd6vWrSb9PphPZ5YtJVuZ47d0/n3p0iVcpGLOjXUIjcnGtGnTlixZ4uPjIxb797//vWDBAmS5u7ufOXMmJyenTZs2C+ojvQlDfkshv2WQ+u09ylt2/t2l2xN+QaPFjzNjZ0+e/sK64nSm2OcF6cbm33qDu/A7Ly/v1KlTOAxDXyE9JCREWgxgWjJ16tSgoCAc+6UlAXMxSn5LIb9lkPr9RtQ82fsnumH/86xrP/GjcH2ZdngjU2zRe4uZ+yfC/OTEiRP5+fk4Tvfu3RtT8AsXLmCeLUxCtm3b1qlTp4iICKyfPXsWc3TMW7COesaPH4+VcePGYcOLFy9i/ciRI05OTlVVVeIuyG8p5LcMUr/37t/r6e3F+z09egam4H/a8RnWE7PuT4IdnnVgyuw4UzRq1Cjp/W/I6mgA15ceHh7z58+vrKwUshITEx9//PEnnnhi7NixWVlZU6ZMQeK1a9cwY+nQoQOuSl1cXPBboTfceAkLC+vcuXO3bt0gNw7/Yv168rs+5LcMUr/r6up8Rvrwf7/cdCynW49uXbvbjX3p+c5dO8PvefFvMWU+zfjM39/f9CfCUVK4VcJQW1t78+ZNNlWvl00kv6WQ3zIwz58UFhXq3Afxz5+k7FrrNkTXus2jTzzZdfrCGUzujhOFQ4YMYZ4/eQCQ31LIbxn452Oj3l4QOGmM6c8PFpwumvq/U6Ojo5l6HgDktxTyWwbe71u3br0Y8tJzQWNNef67oOy+3KGhofT890OH/JaB91tvUHzhwoXunu5LP3ufd1pYcEGJOTemJThyPxS59eR3fchvGWT9FsB82s/Pz3uEz/zYt1LyU9MPZm4/Xbi5JDutIGNR3OJRo0Yh98HPuaWQ31LIbxka8FtvuMtRXFwcExMTGBio0+ns7e3xE+tIQbrpd0ssBPkthfyWoWG/rRzyWwr5LQP5rRrIbxnIb9VAfstAfqsG8lsG+J2WlhZvg6Snp5PfUshvGeLp+K0WyG8ZyG/VQH7LQH6rBvJbBvJbNZDfMpDfqoH8loH8Vg3ktwzkt2ogv2WIp/vfaoH8liGejt9qgfyWgfxWDeS3DOS3aiC/ZSC/VQP5LQP5rRrIbxng90P/NzPzqKioWLNmDdsfDUN+y1BSUpKbm8u6Y5xz586Jr/FWENSJmtlU41y8ePGPf/zjnTt32P5oGPJbnry8vCQTWL58eXBw8FNPPYUVNq/ZoE7UjPpNrBxH7rt377I90Tbkt/mUlZW5u7tDwV69erF5CoGaUT/2gn2xeYQJkN/mgMnAvHnzHBwc7A24ubmxJRQCNQu7wL6wR+yXLUE0CPndZHbs2NG/f38cWQXzgL+/P1tIIVCzuBfsEfvF3tlChHHI7yZQVVU1derU7t27Ozo6Ys4wcODAHj16wLywsDC2qEKgZtSPvWBf2KPwxbBoA1rCFiXkIL9N4ueff05OTu7bt6+Xl9err766bNmyzz//XGcA/sXHx7MbKARqtje8Hwtgj9gv9o42oCVoD1rFbkDUh/w2iYqKivPnz0vvToSEhKSkpISHh8O//Px8SVklQc2oH3vBvrBHMR0tQXvQKklZQgby2xzy8vJGjx6Nw2daWhr8O3HiBFtCIVAz6sdesC/sEftlSxANQn43mdraWswWysvLsY6f8O/q1atsIYVAzahf3Bf2i72zhQjjkN9NJjIyMjY2Vli/c+eOg4OD5ebBqBn1i3+SxH6x9/pFiIYgv5tGaWmpu7v7d999J6bggk+SrzzS+rFf7B1tkOQTDUF+NwEcR729vffs2SNN3LRpk/Sj4jD1Y+9oAz1kYiLkdxNITEycPn06k1hdXc2kKAtfP9qAljCJhCzkt6lUVFS4uLhcv36dzXjgoA1oCd0cNAXy2yR++eWXoKCgtLQ0NuMhgZagPWgVm0HUh/w2iczMzAkTJty7d4/NeEigJWgPWsVmEPUhvxvn5s2brq6u58+fZzMeKmgPWoW2sRmEBPK7cWbNmpWQkMCmWgFoFdrGphISyO9GOHDgwLBhw3766Sc2wwpAq9A2tJDNIH6D/G6I77//3svL64svvmAzrAa0DS1EO9kMwgD53RBxcXFz585lU60MtBDtZFMJA+S3Uc6ePevm5lZTU8NmWBloIdqJ1rIZBPltjHv37o0dOzYrK4vNsErQTrTWem5fWg/ktzzr1q174YUX2FQrBq1Fm9lUzUN+y3Dt2jUXF5fKyko2w4pBa9FmtJzN0DbktwzTpk1buXIlm2r1oM1oOZuqbchvlqKiIl9fX1t8ERTajJaj/WyGhiG/63H79u3BgwcfP36czbAR0HK0H71gM7QK+V2PRYsWRUVFsak2BdqPXrCpWoX8/i8nT57U6XR1dXVshk2B9qMX6AuboUnI718RXsBguTeZPEjQC+H1FWyG9iC/fyU5OTk0NJRNtVnQF/SITdUe5Pd9qqqqBgwYoKaX+qmvR+ZBft9HlUc7lZ2RzIP8Vu1sVU1XFGajdb/VfbdBHXeEmoPW/Y6Kilq8eDGbqiLQO1u/o98cNO23Fv7aZ+t/kW0m2vVbO09r2O4TNc1Hu35r6mk7G30isvlo1G+tPS1ti0+0K4JG/dbgf7vY3H8kKYIW/dbmfyva1n+UKoXm/Nbyf5vbyhsBFERzfmv8bSE28UYXBdGW3/S2J+t/I5eyaMjvH3/8kd7W95/f3qiIaLAZakRDftPbVkWs9o24iqMVv+lt2VKs843mlkATftO3HfBY2zdSWAhN+J2WlhYcHEzfViMF0UBMrOcbhSyE+v2mbxszhvV8I5zlUL/f9G2RDSD7jZ5qQuV+07f9NozsNzKrCTX7Td/WbgqID6KEWLEZqkDNfsfGxkZGRrKpBAeihFixqapAtX6Xl5frdLra2lo2g+BAlBArRIzNsH3U6bfwaoS8vDw2gzACYqXKl2So0++UlJSQkBA2lWgQRAxxY1NtHBX6/cMPP3h4eNCryZoKIoa4IXpshi0j7zcmZMuXL09ISIi3TeLi4tgkRUFkEJ8H+d6cBzMilo6b5TA2IvJ+JyYmXrlyRU8YB/FJSkpiA2cxaEQaRXZE5P3GLwS7NcHxIB8xpRExBX5EyG/z4aNpOWhETIEfEfLbfPhoWg4aEVPgR8Qcv2tu1WTvzImYP3PYyOFOrs729vbOrgN8/HzeiJq3d/9ezPHZDVQKH03LQSNiCvyINM3vW3W1abkZnj5eHsM9I6JfX5Hz8YYDGXmnCvAT60jx8Pb0HuFTWFTIbqlG+GhaDhoRU+BHpAl+X7t5PWxuuJv7wHc+jUMEjS3I1bkPinp7wa1bt9gq1AUfTctBI2IK/IiY6jdC+Vzw2NETAzYdy+YjyCwoEzhpzIshL6k7oHw0LQeNiCnwI2KS3zgJ4jiBUG4t387HTnZByeeCxi5cuFBaj8rgo2k5aERMgR8Rk/zGDA8nwcxS9jiR9dfciJjXA6aMCZnzctrhjUwuyrt7uu/evVtaVUVFRbmBM2fOXLt2TZr14ElNTT18+DCbyvGXv/xly5YtJ0+eZNL5aFoOGhEptbW1O3bsOHXqFJPOj0jjfuPa3MtnCD/Dw/HA1dPtkd/oat+VD+jSz9738/eTXr9PmjSpbdu2Xbp0eeyxx1q2bOns7PzJJ5+IuaYzaNCgGTNmsKlNZOjQoYmJiWyqhOrq6qCgoO7du48ZMwYNnjt3rjSXj6bloBERKCsre+ONN3r27IkO8u3kR6Rxv7N35uAanAkTlllL5mAfzoNd4jOWDQ0YjvVxoeP5Yj4jfIqLi8XaEM3Zs2cL619//fWaNWvs7OymTZsmFjCRzMzMPXv2sKlNpNFoRkVF9enTR/jDOI7fHTt2xH7FXD6aloNGRAAnnyVLlhw6dAjjoozfEfNnzoh+nQ9Tf50TIpiUsxrrOE7gV79Tl058sTffiYyJiRFrk0ZToKSkBNvu2rVLTLlx48a+ffsKCwuvX78uJlZWVn5joKCgAIefS5cuXb16FelfffWVtBhGCCWNVQJwCi4qKkKAUEnD0UQBHNWWL18upoSHh48ePVr8yEfTctCIMDz77LPK+D1s5LAV2R8zMcouy0cI2ndsL6YEhU0eMX7UxqNZTMmUvNSAgACxNj6awMfH57XXXhPWMf1ycHAIDAycMGFCjx49Dhw4IKSj58nJyS4uLo6OjvgIz2JjY7GCYmFhYb/VpPfz84uMjDRWCY5bTz75JKry9/f39fUdMGBAA9HEARu6HDt2TExJS0v73e9+J37ko2k5aEQYFPPbycVpw8E/MzFK3pmKsXd41oFJ55f0Q5t0Op1Ym2w0EQ4h4jU1NZhaoZVC+qpVq/r27YuLCb0hmkOGDMnOzhayxGhu374dE0ccRbB+4cKF1q1b//3vf5etBJXjpIYph5COA0mrVq0aiOb+/fvRRxyWxBRsghRhX3q5aFoOGhEGxfx+uufTOX/bxsRo+ZaViCZOiHz42OVkQa9evcTaZKMZEhKCX2us4PyFalevXv2pAQQCH4UbF4jm5MmTxU3EaOKkhmCtXbsW60uXLn3++eeNVVJaWoqVqqoqsZLBgwc3EM0vv/wS5f/xj3+IKRi5Fi1aYFSEj3w0LQeNCINifju7OvNHCyGa/Qb2Z2PHLVtKtjZ8tBDCER0djfWcnJw2bdosqM/p06f1hmhKWyVGE3z44Yc4tWGlX79++fn5xirJzc199NFHxRr0jV3N4MiNPh48eFBM+dOf/tStWzfxIx9Ny0EjwqCY396jvPnZXsqutYhmzz69xJQlqe/NT4jMOLKZKfl5QXrDs72kpKR27doJISsvL0e1Z86cEXPFv7eh54iamC6N5uXLlzt06LB58+bevXtjbIxVcvz4caSXlZUJid9++y1Omg1Hc9CgQeLZE0ycOPHll18WP/LRtBw0IgyK+f1G1Dz+ah3nx1atW7Vp1za3fIeQ8pTj02jruv1pTMlF7y1mrtanTJmCq4rdu3evX78exrRt2zYjI0MsMG7cOFzcXLx4EetHjhxxcnISzl8NRFNvmC/a2dmJMzxjlWC+iMsdXOZXV1dHRERgmthwNDds2NCxY8edO3diToKDNw42JSUlYi4fTctBI8KgmN979+/19PZiYoTFxcMV4YtbH4/1dcXpLVq26GLXhSmz40zRqFGjpHdbZ86c6WjA2dkZHcN56ty5c2Ku3vCrj9B07twZMwFEIS8vT0jHGGDqJhZ75ZVXVqxYIX48evQoRBRncsYqqaioQKDbt29vb2//7rvvojHCNLEBPvroo65du6KnzzzzDA5I0iw+mpaDRoTB399f+ksowI9I437j/OIz0of/a1lU4kJEs3uvHrPemeM0yBnrweFTmDKfZnyGdpj3/PHNmzfZpKYjWwnOg0yTLsshLXDjxg3pRwE+mpaDRuRy/RGRhR+Rxv0GhUWFOvdB/NMO/sEBj/yGo1PvzNJ6t1p3nCjE2Yd52sE6eVEOthAHH03LQSPyolkjYpLfIOrtBYGTxvBPq723ISH87YgFSdHZZfnS9ILTRVP/d6pwDa5W+GhaDhoRU+BHxFS/ccH7YshLzwWNNeVp44Ky+6EMDQ3V2tPGloNGxBT4ETHVb70hoAsXLnT3dF/62ft8BIUFly+Y4eEkiOOEukOpl4um5aARMQV+RJrgtwBmb7jK9h7hMz/2rZT81PSDmdtPF24uyU4ryFgUtxjX5si1iRle8+GjaTloREyBH5Em+603XL8XFxfHxMQEBgbqdDp7e3v8xDpSkG7etbktwkfTctCImAI/Iub4TQjw0bQcNCKmwI8I+W0+fDQtB42IKfAjQn6bDx9Ny0EjYgr8iJDf5sNH03LQiJgCPyJG/U5LS4snjJOens5H03LE04g0huyIGPWb/dUgOPhoWg4aEVPgR4T8Nh8+mpaDRsQU+BEhv82Hj6bloBExBX5EyG/z4aNpOWhETIEfEfLbfPhoWg4aEVPgR4T8Nh8+mpaDRsQU+BEhv82Hj6bloBExBX5EjPpNd1sbRvZuq+WIpxFpDNkRMeo3+6tBcPDRtBw0IqbAjwj5bT58NC0HjYgp8CNCfpsPH03LQSNiCvyIkN/mw0fTctCImAI/IuS3+fDRtBw0IqbAj4hRv7XzT03mgfjw0bQcNCKNIjsi8n6XlJTk5uayFdgIN27cYN4wpji3b9/Oy8tDlNjAWYwHMyKIm+ybuqwfYyMi7zdA6STbZPny5U899VRwcDBW2DyFwHEiOzubDZmFseiIIFaIGOJmuaBZFGMjYtRvm6ZXr14YKnd397KyMjaP4ECUECtEDHFj82wcdfrt5uZmb8DBwWHevHk4f7ElCAOIDOKDKAnhQtzYEjaOOv329/cXBgzgmNS/f/8dO3awhTQPYoLIID5irBA3tpCNo06/w8LCMFo9evQYOHAgzryOjo7du3efOnVqVVUVW1STIA6IBmKCyCA+iBJihYghbmxRG0edfsfHx9sb3uEEPv/882XLlr366qteXl59+/ZNTk7++eef2Q00A/qOCCAOiAZigsggPkKgEDHEjd3AxlGn3/n5+Rit8PDwlJSUkJAQMf3u3bvnz5+vqKiQlNUW6DsigDiIKYgPooRYIWKIm6SsGlCn3ydOnMBopaWl4XA1evTovLw8tgRhAJFBfBAlxAoRQ9zYEjaOOv2+evUqRqu8vBzr+ImTb21tLVtI8yAmiIwYJUQMcWML2Tjq9BsHJAcHhzt37ggfY2NjIyMj6xch/oOYIDLCOmKFiKnvykSdfgNcPInr3333nbu7e2lpqSRf6yAaiAkiI6ZII6YaVOv3pk2bpB/37Nnj7e0tHtE1DuKAaCAm0kQmYupAtX5XV1czKdOnT09MTGQStQnigGgwiXzEVIBq/ea5fv26i4uLlm8OCiACiAOiwWaoEQ35DdLS0oKCgn755Rc2QzOg74gA4sBmqBRt+X3v3r0JEyZkZmayGZoBfUcEEAc2Q6Voy29w/vx5V1fXmzdvshkaAL1G3xEBNkO9aM5vkJCQMGvWLDZVA6DX/H9wqRst+v3TTz8NGzbswIEDbIaqQX/Ra/SdzVA1WvQbfPHFF15eXt9//z2boVLQU/QXvWYz1I5G/QZz586Ni4tjU1UKeor+sqkaQLt+19TUuLm5nT17ls1QHegjeor+shkaQLt+g6ysrLFjx6r7Zhl6hz6ip2yGNtC03+CFF15Yt24dm6oi0Dv0kU3VDFr3u7Ky0sXF5dq1a2yGKkC/0Dv0kc3QDFr3G6xcuXLatGlsqipAv9A7NlVLkN/3/ynT19e3qKiIzbBx0CP0S/qvlhqE/L7P8ePHBw8efPv2bTbDZkFf0CP0i83QGOT3r0RFRS1atIhNtVnQF/SITdUe5Pev1NXV6XS6kydPshk2CHqBvqBHbIb2IL//S35+vvCyBDbDphBeiaG+N5mYB/ldj9DQ0OTkZDbVpkD70Qs2VauQ3/WoqqoaMGCA7b6m0NbbrzjkN4tNH/9UcP5RFvKbxXbnr+q4flAW8lsGW7z/oKb7PwpCfsuzePFi27p/jNaizWyq5iG/5bGtv/+p7++vSkF+G8VWnt9Q6/MzikB+N4RNPH+n4ucfmw/53RDW//y0up9fbz7kdyNY+f+/qP7/j5oJ+d0I1vz/i1r4/9FmQn43jnX+/7l2/v+/OZDfJmGF7w/R1PtbzIb8Nglre/+T1t6/ZTbkt6kI7+/78ccf2YwHDtqgwfcnmgf53QSs5P2rmn3/rRmQ303AGt6freX3l5sB+d00Hu73H9D3TzQV8rtp/PLLL8HBwQ/r+2uwX+xdy98f1FTI7ybzsL5/jL7/zQzIb3OQ/f5IS0Pf32kG5Lc5yH7/r0Wh7182D/LbTPjvb7cc2Av2hT2yGURjkN/mExkZGRsby6ZaAOwF+2JTCRMgv82ntrZWp9OVl5ezGYqC+rEX7IvNIEyA/G4WeXl5Fn0lg/CyCuyFzSBMg/xuLiEhISkpKWyqQqBm1M+mEiZDfjeXqqoqDw+PH374gc1oNqgTNdPL1pqDLfl96NChDz74IN76iIuLY5MUwnI1N4eEhISkpCS9Xs+OkPVhM35jDpqTk6MnrIMrV65Y/5sF/mNDfn/00UdsjImHCkaEHSTrg/wmzIT8VhLy29ogv5WkYb/r6up27C6Y/dYfho/ydnZ1tre3x0+sIwXpyGU3IJoN+a0kDfidV5A/1Heox3DPiOjXV+R8vOFARt6pAvzEOlKQjlyUYTcjmgf5rSSyft+6dWvOW3MHug9859M4OG1sQS7KoCTKs1UQ5kJ+KwnvN2QNmho8emLApmPZvNPMgjIoifKkuFKQ30rC+/1G1Dwou7V8O2+z7IKSKI+tmHoI8yC/lYTxe1dh4UB3XWapzJE766+5ETGvB0wZEzLn5bTDG6VZKI+tsK20KlBRUVFu4MyZM9euXWNyHzCpqamHDx8W1q22YXryW1mkftfV1fmM9JGdc+Mg7erp9shvdLXvyiiOrbAtc0dl0qRJbdu27dKly2OPPdayZUtnZ+dPPvlEWsAUBg0aNGPGDDa16QwdOjQxMVFYt9qG6clvZZH6XVxc7OntxcuNZdaSOdDaebBLfMayoQHDsT4udDxTBtuiBrE2vUGj2bNnC+tff/31mjVr7Ozspk2bJi3TKJmZmXv27GFTmw7jt3U2TE9+K4vU76joBTOiX+flxtJf5wSnk3JWYx1HbhzzOnXpxJTBtqhBrE1fXyOBkpISbLtr1y7h440bN/bt21dYWHj9+nWxTGVl5TcGCgru32K/dOnS1atXkf7VV19Ji8FLlBTWZesBmHsUFRUdOnQI9RjzW8BKGqYnv5VF6vdI/1Ersj/m5c4uy8fYt+/YXkwJCps8YvyojUezpMWwLWoQa9PLaQR8fHxee+01rGDS6eDgEBgYOGHChB49ehw4cEAogPFOTk52cXFxdHTEx9GjR8fGxmIFxcLCwsR6/Pz8IiMjG6gHJ5Mnn3wStfn7+/v6+g4YMKABv/XW0TA9+a0sUr9d3Fw3HPwz73fyzlQcvB2edeCzpAu2RQ1ibXojGkGFgICAmpqanj17JiQkCImrVq3q27dvbW2t3qDRkCFDsrOzhSxRo+3bt2O6jMMn1i9cuNC6deuzZ88aqwfpffr0iYqKEtJxBG3VqlXDfltDw/Tkt7JI/cZ45PxtGy/u8i0r4TemKHyWdMG2qEGsTW9Eo5CQEBzPcNZGnatXr/7UAIYfH0+ePKk3aDR58mSxvKgRTuVQZO3atVhfunTp888/jxVj9ZSWlmKlqqpKrGfw4MEN+20NDdOT38oi9dvVyPFb8LvfwP58lnTBtq6NHb8FFaKjo3Nyctq0abOgPqdPn9YbNIqPjxc3ETUCH374IU7oWOnXr19+/v1HA4zVk5ub++ijj4qV6I1fXwpYScP05LeySP32H+0vO/9O2bUWfvfs00tMWZL63vyEyIwjm6XFsC1qEGvTy2mUlJTUrl07DHN5eTnqPHPmjJgl/gUU4w1dxHSpRpcvX+7QocPmzZt79+4t3Is0Vs/x48eRXlZWJiR+++23OLc04LeVNExPfiuL1O+YmJjZMXN5vzHxaNW6VZt2bXPLdwgpTzk+jUFatz9NWgzbogaxNr1BoylTpuByavfu3evXr584cWLbtm0zMjKE3HHjxuGS7uLFi1g/cuSIk5OTcNZuQCO9YZZsZ2cnzmv1xuvBXBmXelevXq2uro6IiMAUWeq3dTZMT34rC3P/e7ivN+83FhcPVwgdtz4e6+uK01u0bNHFrgtTBtsy979nzpzpaMDZ2RkjihP0uXPnxFwc8+BE586du3XrhrHPy8sT0mEeJqxisVdeeWXFihXix6NHj3bs2FE6fzVWT0VFBQxr3769vb39u+++i8YIU2S9FTdMT34ri9RvnFj9/P3jUj/g/Y5KXAi/u/fqMeudOU6DnLEeHD5FWgBbYVvzngi/efMmm2QWsvVgAmBeq/RGKjQD2XqMNYz8VhKp3wDnaw8vD9nnT/yDAx75DUen3pml/735jfLYCttKqyLMg/xWEsZvEB0dPWHyRNnnB9/bkBD+dsSCpOjssnwxESVRHlsx9RDmQX4rCe83LvNDQ0MnTQnadCyHV5xZUAYlUZ6e/1YK8ltJeL/1BsVxPPb08ly2Lol3WlyQizIoSXIrCPmtJLJ+C2A+7efnN2LkiLeXLEzdtn7j4S1wGj+xjhSkI5fm3IpDfitJA37rDXdUiouLY2JiAgMDdTqdvb09fmIdKUiXvfwnmgn5rSQN+008eMhvJSG/rQ3yW0nIb2uD/FYS8tvaIL+VBNFMS0tj30RNPCTS09PJbyWh47e1QX4rCfltbZDfSkJ+Wxvkt5KQ39YG+a0k5Le1QX4rCfltbZDfSkJ+Wxvkt5LQ/W+rgu5/Kwwdv60N8ltJyG9rg/xWEvLb2iC/lYT8tjbIbyUhv60N8ltJUlNTKyoq2BgTD4m6ujryW0nu3LkTHR1NilsDt2/f3rZt25EjR9hBsj5sxm9w9+7dNWvWJBEPm4SEhOzsbHZ4rBJb8psgmgr5TagZ8ptQM+Q3oWbIb0LN/D/Ye7VfqVYJYwAAAABJRU5ErkJggg==" /></p>

ダイヤモンド継承は、
[仮想継承](term_explanation.md#SS_19_10_11)(virtual inheritance)を使ったものと、使わないものに分類できる。

[仮想継承](term_explanation.md#SS_19_10_11)を使わないダイヤモンド継承のコードを以下に示す。

```cpp
    //  example/term_explanation/diamond_inheritance_ut.cpp 6

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
    //  example/term_explanation/diamond_inheritance_ut.cpp 26

    auto dd = DerivedDerived{};

    Base& b0 = static_cast<Derived_0&>(dd);  // Derived_0::Baseのリファレンス
    Base& b1 = static_cast<Derived_1&>(dd);  // Derived_1::Baseのリファレンス

    ASSERT_NE(&b0, &b1);  // ddの中には、Baseインスタンスが2つできる
```

これからわかるように、DerivedDerivedインスタンスの中に2つのBaseインスタンスが存在する。
この状態をオブジェクト図で表すと下記のようになる。

<!-- pu:deep/plant_uml/diamond_inheritance_obj.pu--><p><img src="data:image/png;base64,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" /></p>

下記コードは、それが原因で名前解決が曖昧になりコンパイルできない。

```cpp
    //  example/term_explanation/diamond_inheritance_ut.cpp 36

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
    //  example/term_explanation/diamond_inheritance_ut.cpp 53

    ASSERT_EQ(0, dd.Derived_0::get());  // クラス名による名前修飾
    ASSERT_EQ(0, dd.Derived_1::get());

    dd.Derived_0::set(1);
    ASSERT_EQ(1, dd.Derived_0::get());  // Derived_0::Base::x_は1に変更
    ASSERT_EQ(0, dd.Derived_1::get());  // Derived_1::Base::x_は0のまま

    dd.Derived_1::set(2);
    ASSERT_EQ(1, dd.Derived_0::get());  // Derived_0::Base::x_は1のまま
    ASSERT_EQ(2, dd.Derived_1::get());  // Derived_1::Base::x_は2に変更
```

次に示すのは、[仮想継承](term_explanation.md#SS_19_10_11)を使用したダイヤモンド継承の例である。

```cpp
    //  example/term_explanation/diamond_inheritance_ut.cpp 70

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
    //  example/term_explanation/diamond_inheritance_ut.cpp 90

    auto dd = DerivedDerived{};

    Base& b0 = static_cast<Derived_0&>(dd);  // Derived_0::Baseのリファレンス
    Base& b1 = static_cast<Derived_1&>(dd);  // Derived_1::Baseのリファレンス

    ASSERT_EQ(&b0, &b1);  // ddの中には、Baseインスタンスが1つできる
```

仮想継承の効果で、DerivedDerivedインスタンスの中に存在するBaseインスタンスは1つになるため、
上で示した仮想継承を使わないダイヤモンド継承での問題は解消される
(が、[仮想継承](term_explanation.md#SS_19_10_11)による別の問題が発生する)。

```cpp
    //  example/term_explanation/diamond_inheritance_ut.cpp 99

    Base& b = dd;  // Baseインスタンスは1つであるため、コンパイルできる

    dd.get();  // Baseインスタンスは1つであるため、コンパイルできる

    dd.Derived_0::set(1);               // クラス名による修飾
    ASSERT_EQ(1, dd.Derived_1::get());  // Derived_1::BaseとDerived_1::Baseは同一であるため

    dd.set(2);
    ASSERT_EQ(2, dd.get());
```

この状態をオブジェクト図で表すと下記のようになる。

<!-- pu:deep/plant_uml/diamond_inheritance_virtual_obj.pu--><p><img src="data:image/png;base64,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" /></p>

### 仮想継承 <a id="SS_19_10_11"></a>
下記に示した継承方法を仮想継承、仮想継承の基底クラスを仮想基底クラスと呼ぶ。

```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 9

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

仮想継承は、[ダイヤモンド継承](term_explanation.md#SS_19_10_10)の基底クラスのインスタンスを、
その継承ヒエラルキーの中で1つのみにするための言語機能である。

仮想継承の独特の動作を示すため、
上記コードに加え、仮想継承クラス、通常の継承クラス、
それぞれを通常の継承したクラスを下記のように定義する。

```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 25

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
    //  example/term_explanation/virtual_inheritance_ut.cpp 46

    auto dv = DerivedVirtual{1};  // 仮想継承クラス
    auto dn = DerivedNormal{1};   // 通常の継承クラス

    ASSERT_EQ(1, dv.get());  // これは非仮想継承と同じ動作
    ASSERT_EQ(1, dn.get());

    auto ddv = DerivedDerivedVirtual{1};  // 仮想継承クラスを継承したクラス Base::Base()が呼ばれる
    auto ddn = DerivedDerivedNormal{1};  // 通常継承クラスを継承したクラス Base::Base(1)が呼ばれる

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
    //  example/term_explanation/virtual_inheritance_ut.cpp 62

    class DerivedDerivedVirtualFixed : public DerivedVirtual {  // DerivedDerivedNormalと同じように動作
    public:
        explicit DerivedDerivedVirtualFixed(int32_t x) noexcept : Base{x}, DerivedVirtual{x} {}
        //                     基底クラスのコンストラクタ呼び出し ^^^^^^^
    };
```
```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 73

    DerivedDerivedVirtual ddv{1};  // 仮想継承クラスを継承したクラス
    DerivedDerivedVirtualFixed ddvf{1};  // 上記クラスのコンストラクタを修正したクラス
    DerivedDerivedNormal ddn{1};         // 通常の継承クラスを継承したクラス

    ASSERT_EQ(0, ddv.get());  // 仮想継承独特の動作
    ASSERT_EQ(1, ddvf.get());
    ASSERT_EQ(1, ddn.get());
```
「仮想継承のコンストラクタ呼び出し」仕様は、
[ダイヤモンド継承](term_explanation.md#SS_19_10_10)での基底クラスのコンストラクタ呼び出しを一度にするために存在する。

もし、この機能がなければ、下記のコードでの基底クラスのコンストラクタ呼び出しは2度になるため、
デバッグ困難なバグが発生してしまうことは容易に想像できるだろう。

```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 88

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
    //  example/term_explanation/virtual_inheritance_ut.cpp 124

    ASSERT_EQ(0, base_called);

    auto dd = DerivedDerived{2, 3};  // Base::Baseが最初に呼ばれないとassertion failする

    ASSERT_EQ(1, base_called);  // 「仮想継承のコンストラクタ呼び出し」仕様のため
    ASSERT_EQ(0, dd.get());  // Baseのデフォルトコンストラクタは、x_を0にする
```

基底クラスのコンストラクタ呼び出しは、下記のコードのようにした場合でも、
単体テストが示すように、一番最初に行われる。

```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 139

    class DerivedDerived : public Derived_0, public Derived_1 {
    public:
        DerivedDerived(int32_t x0, int32_t x1) noexcept : Derived_0{x0}, Derived_1{x1}, Base{1} {}
    };
```
```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 151

    ASSERT_EQ(0, base_called);

    auto dd = DerivedDerived{2, 3};  // Base::Baseが最初に呼ばれないとassertion failする

    ASSERT_EQ(1, base_called);  // 「仮想継承のコンストラクタ呼び出し」仕様のため
    ASSERT_EQ(1, dd.get());  // Base{1}呼び出しの効果
```

このため、基底クラスのコンストラクタ呼び出しは下記のような順番で行うべきである。

```cpp
    //  example/term_explanation/virtual_inheritance_ut.cpp 164

    class DerivedDerived : public Derived_0, public Derived_1 {
    public:
        DerivedDerived(int32_t x0, int32_t x1) noexcept : Base{1}, Derived_0{x0}, Derived_1{x1} {}
    };
```

### 仮想基底 <a id="SS_19_10_12"></a>
仮想基底(クラス)とは、[仮想継承](term_explanation.md#SS_19_10_11)の基底クラス指す。

### ドミナンス <a id="SS_19_10_13"></a>
[ドミナンス(Dominance、支配性)](https://en.wikipedia.org/wiki/Dominance_(C%2B%2B))とは、
「探索対称の名前が継承の中にも存在するような場合の[name lookup](term_explanation.md#SS_19_10_2)の仕様の一部」
を指す慣用句である。

以下に

* [ダイヤモンド継承を含まない場合](term_explanation.md#SS_19_10_13_1)
* [ダイヤモンド継承かつそれが仮想継承でない場合](term_explanation.md#SS_19_10_13_2)
* [ダイヤモンド継承かつそれが仮想継承である場合](term_explanation.md#SS_19_10_13_3)

のドミナンスについてのコードを例示する。

この例で示したように、[ダイヤモンド継承](term_explanation.md#SS_19_10_10)を通常の継承で行うか、
[仮想継承](term_explanation.md#SS_19_10_11)で行うかでは結果が全く異なるため、注意が必要である。

#### ダイヤモンド継承を含まない場合 <a id="SS_19_10_13_1"></a>

```cpp
    //  example/term_explanation/dominance_ut.cpp 9

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
    //  example/term_explanation/dominance_ut.cpp 29

    Base b;

    ASSERT_EQ(2, b.f(2.14));  // オーバーロード解決により、B::f(double)が呼ばれる

    DerivedDerived dd;

    // Derivedのドミナンスにより、B::fは、DerivedDerived::gでのfのname lookupの対象にならず、
    // DerivedDerived::gはDerived::fを呼び出す。
    ASSERT_EQ(3, dd.g());
```

この[name lookup](term_explanation.md#SS_19_10_2)については、[name-hiding](term_explanation.md#SS_19_10_9)で説明した通りである。

#### ダイヤモンド継承かつそれが仮想継承でない場合 <a id="SS_19_10_13_2"></a>

```cpp
    //  example/term_explanation/dominance_ut.cpp 45

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

#### ダイヤモンド継承かつそれが仮想継承である場合 <a id="SS_19_10_13_3"></a>

```cpp
    //  example/term_explanation/dominance_ut.cpp 71

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
    //  example/term_explanation/dominance_ut.cpp 92

    DerivedDerived dd;

    // Derived_0のドミナンスと仮想継承の効果により、
    // B::fは、DerivedDerived::gでのfのname lookupの対象にならず、
    // DerivedDerived::gはDerived_0::fを呼び出す。
    ASSERT_EQ(3, dd.g());
```

これまでと同様にDerived_0のドミナンスによりBase::fは[name-hiding](term_explanation.md#SS_19_10_9)されることになる。
この時、Derived_0、Derived_1がBaseから[仮想継承](term_explanation.md#SS_19_10_11)した効果により、
この継承ヒエラルキーの中でBaseは１つのみ存在することになるため、
Derived_1により導入されたBase::fも併せて[name-hiding](term_explanation.md#SS_19_10_9)される。
結果として、曖昧性は排除され、コンパイルエラーにはならず、このような結果となる。

### using宣言 <a id="SS_19_10_14"></a>
using宣言とは、"using XXX::func"のような記述である。
この記述が行われたスコープでは、この記述後の行から名前空間XXXでの修飾をすることなく、
funcが使用できる。

```cpp
    //  example/term_explanation/namespace_ut.cpp 6
    namespace XXX {
    void func() noexcept {}
    void gunc() noexcept {}
    }  // namespace XXX
```
```cpp
    //  example/term_explanation/namespace_ut.cpp 12

    // global namespace
    void using_declaration() noexcept
    {
        using XXX::func;  // using宣言

        func();       // XXX::不要
        XXX::gunc();  // XXX::必要
    }

```

### usingディレクティブ <a id="SS_19_10_15"></a>
usingディレクティブとは、"using namespace XXX"のような記述である。
この記述が行われたスコープでは、下記例のように、この記述後から名前空間XXXでの修飾をすることなく、
XXXの識別子が使用できる。

```cpp
    //  example/term_explanation/namespace_ut.cpp 6
    namespace XXX {
    void func() noexcept {}
    void gunc() noexcept {}
    }  // namespace XXX
```
```cpp
    //  example/term_explanation/namespace_ut.cpp 24

    // global namespace
    void using_directive() noexcept
    {
        using namespace XXX;  // usingディレクティブ

        func();  // XXX::不要
        gunc();  // XXX::不要
    }
```

より多くの識別子が名前空間の修飾無しで使えるようになる点において、
[using宣言](term_explanation.md#SS_19_10_14)よりも危険であり、また、
下記のように[name-hiding](term_explanation.md#SS_19_10_9)された識別子の導入には効果がない。

```cpp
    //  example/term_explanation/namespace_ut.cpp 6
    namespace XXX {
    void func() noexcept {}
    void gunc() noexcept {}
    }  // namespace XXX
```
```cpp
    //  example/term_explanation/namespace_ut.cpp 35

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

## template強化機能 <a id="SS_19_11"></a>
### SFINAE <a id="SS_19_11_1"></a>
[SFINAE](https://cpprefjp.github.io/lang/cpp11/sfinae_expressions.html)
(Substitution Failure Is Not An Errorの略称、スフィネェと読む)とは、
「テンプレートのパラメータ置き換えに失敗した([ill-formed](term_explanation.md#SS_19_18_5)になった)際に、
即時にコンパイルエラーとはせず、置き換えに失敗したテンプレートを
[name lookup](term_explanation.md#SS_19_10_2)の候補から除外する」
という言語機能である。

### コンセプト <a id="SS_19_11_2"></a>
C++17までのテンプレートには以下のような問題があった。

* [SFINAE](term_explanation.md#SS_19_11_1)による制約が複雑  
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
    //  example/term_explanation/concept_ut.cpp 12

    // SFINAEを使用したc++17スタイル
    template <typename T, typename = typename std::enable_if<std::is_arithmetic<T>::value>::type>
    T add(T a, T b)
    {
        return a + b;
    }

    //  example/term_explanation/concept_ut.cpp 24

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
    //  example/term_explanation/concept_ut.cpp 49

    // コンセプトを使用したC++20スタイル
    template <typename T>
    concept Arithmetic = std::is_arithmetic_v<T>;

    template <Arithmetic T>
    T add(T a, T b)
    {
        return a + b;
    }

    //  example/term_explanation/concept_ut.cpp 64

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
    //  example/term_explanation/concept_ut.cpp 85

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
    //  example/term_explanation/concept_ut.cpp 113

    // 標準コンセプト std::floating_point と std::same_as を使用
    template <std::floating_point FLOAT_0, std::same_as<FLOAT_0> FLOAT_1>
    bool is_equal(FLOAT_0 lhs, FLOAT_1 rhs) noexcept
    {
        return std::abs(lhs - rhs) <= std::numeric_limits<FLOAT_0>::epsilon();
    }
```

フレキシブルに制約を記述するためにrequiresを使用したコード例を下記する。

```cpp
    //  example/term_explanation/concept_ut.cpp 138

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

### 畳み込み式 <a id="SS_19_11_3"></a>
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
    //  example/term_explanation/flold_expression_ut.cpp 9

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
    //  example/term_explanation/flold_expression_ut.cpp 36
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
    //  example/term_explanation/flold_expression_ut.cpp 61

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
    //  example/term_explanation/flold_expression_ut.cpp 89

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
    //  example/term_explanation/flold_expression_ut.cpp 117
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
    //  example/term_explanation/flold_expression_ut.cpp 128

    static_assert(is_same_some_of<int, int, double, char>::value);
    static_assert(!is_same_some_of<int, double, char>::value);
    static_assert(is_same_some_of<std::string, std::string, int>::value);
```

畳み込み式を使うことで、この問題をある程度緩和したコードを下記する。

```cpp
    //  example/term_explanation/flold_expression_ut.cpp 140
    template <typename T, typename U, typename... Us>
    struct is_same_some_of {
        static constexpr bool value = (std::is_same_v<T, U> || ... || std::is_same_v<T, Us>);
    };
```
```cpp
    //  example/term_explanation/flold_expression_ut.cpp 146

    static_assert(is_same_some_of<int, int, double, char>::value);
    static_assert(!is_same_some_of<int, double, char>::value);
    static_assert(is_same_some_of<std::string, std::string, int>::value);
```

### ジェネリックラムダ <a id="SS_19_11_4"></a>
ジェネリックラムダとは、C++11のラムダ式のパラメータの型にautoを指定できるようにした機能で、
C++14で導入された。

この機能により関数の中で関数テンプレートと同等のものが定義できるようになった。

ジェネリックラムダで定義されたクロージャは、通常のラムダと同様にオブジェクトであるため、
下記のように使用することもできる便利な記法である。

```cpp
    //  example/term_explanation/generic_lambda_ut.cpp 4

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
    //  example/term_explanation/generic_lambda_ut.cpp 23

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

### クラステンプレートのテンプレート引数の型推論 <a id="SS_19_11_5"></a>
C++17から、
「コンストラクタに渡される値によって、クラステンプレートのテンプレート引数を推論する」
機能が導入された。

この機能がないC++14までは以下のように記述する必要があった。

```cpp
    //  example/term_explanation/template_ut.cpp 13

    auto a = std::vector<int>{1, 2, 3};

    static_assert(std::is_same_v<decltype(a), std::vector<int>>);
```

これに対して、この機能により、以下のようにシンプルに記述できるようになった。

```cpp
    //  example/term_explanation/template_ut.cpp 24

    auto a = std::vector{1, 2, 3};

    static_assert(std::is_same_v<decltype(a), std::vector<int>>);  // テンプレート引数がintと推論
```

### テンプレートの型推論ガイド <a id="SS_19_11_6"></a>
テンプレートの型推論ガイドは、C++17で導入された機能である。この機能により、
クラステンプレートのインスタンス化時にテンプレート引数を明示的に指定せず、
引数から自動的に型を推論できるようになる。型推論ガイドを使用することで、
コードの可読性と簡潔性が向上する。

型推論ガイドがない場合、[クラステンプレートのテンプレート引数の型推論](term_explanation.md#SS_19_11_5)は限定的であり、
明示的にテンプレート引数を指定する必要がある場合が多い。
一方、型推論ガイドを使用することで、
コンストラクタの引数からテンプレート引数を自動的に決定することが可能になる。

```cpp
    //  example/term_explanation/deduction_guide_ut.cpp 8

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
上記のクラステンプレートは、ガイドがない場合、
以下に示すように型推論によりテンプレート引数を決定することができない。

```cpp
    //  example/term_explanation/deduction_guide_ut.cpp 31

    S<int>    s1{42};   // 明示的にテンプレート引数を指定
    S<double> s2{1.0};  // 明示的にテンプレート引数を指定

    // テンプレート引数の推論ができず、下記はコンパイルできない
    // S       s1{42};   // 明示的にテンプレート引数を指定
    // S       s2{1.0};  // 明示的にテンプレート引数を指定
```

以上に示したクラステンプレートに以下の型推論ガイドを追加することにより、
テンプレート引数を型推論できるようになる。

```cpp
    //  example/term_explanation/deduction_guide_ut.cpp 44

    template <typename T>
    S(T) -> S<T>;
```
```cpp
    //  example/term_explanation/deduction_guide_ut.cpp 52

    S s1{42};   // 推論ガイドの効果
    S s2{1.0};  // 推論ガイドの効果
    S s3 = 42;  // S<int>のコンストラクタがintであるため、暗黙の型変換が可能
    // S    s4 = 1.0;  // S<double>のコンストラクタがexplicitであるため
```

### 変数テンプレート <a id="SS_19_11_7"></a>
変数テンプレートとは、下記のコード示したような機能である。

```cpp
    //  example/term_explanation/template_ut.cpp 32

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


### エイリアステンプレート <a id="SS_19_11_8"></a>
エイリアステンプレート(alias templates)とはC++11から導入され、
下記のコード例で示したようにテンプレートによって型の別名を定義する機能である。

```cpp
    //  example/term_explanation/template_ut.cpp 56

    using IntVector = std::vector<int>;  // std::vector<int> のエイリアスを定義

    template <typename T>  //エイリアステンプレートを定義
    using Vec = std::vector<T>;

    static_assert(std::is_same_v<IntVector, Vec<int>>);  // Vec<int> == std::vector<int>
```

### constexpr if文 <a id="SS_19_11_9"></a>
C++17で導入された[constexpr if文](https://cpprefjp.github.io/lang/cpp17/if_constexpr.html)とは、
文を条件付きコンパイルすることができるようにするための制御構文である。

まずは、この構文を使用しない例を示す。

```cpp
    //  example/term_explanation/constexpr_if_ut.cpp 9

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
    //  example/term_explanation/constexpr_if_ut.cpp 31

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

このような場合、[SFINAE](term_explanation.md#SS_19_11_1)によるオーバーロードが必須であったが、
この文を使用することで、下記のようにオーバーロードを使用せずに記述できるため、
条件分岐の可読性の向上が見込める。

```cpp
    //  example/term_explanation/constexpr_if_ut.cpp 52

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

この構文は[パラメータパック](template_meta_programming.md#SS_13_1_3)の展開においても有用な場合がある。

```cpp
    //  example/term_explanation/constexpr_if_ut.cpp 93

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
    //  example/term_explanation/constexpr_if_ut.cpp 111

    static_assert(4 == (MaxSizeof<int8_t, int16_t, int32_t>()));
    static_assert(4 == (MaxSizeof<int32_t, int16_t, int8_t>()));
    static_assert(sizeof(std::string) == MaxSizeof<int32_t, int16_t, int8_t, std::string>());
```

C++14までの構文を使用する場合、
上記のようなオーバーロードとリカーシブコールの組み合わせが必要であったが、
constexpr ifを使用することで、やや単純に記述できる。

```cpp
    //  example/term_explanation/constexpr_if_ut.cpp 123

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

### autoパラメータによる関数テンプレートの簡易定義 <a id="SS_19_11_10"></a>
この機能は、C++20から導入された。
下記のコードで示すように簡易的に関数テンプレートを定義するための機能である。

```cpp
    //  example/term_explanation/decltype_ut.cpp 182

    #if __cplusplus >= 202002L  // c++20
    auto add(auto lhs, auto rhs) { 
        return lhs + rhs; 
    }

    #else  // c++17
    template <typename T, typename U>
    auto add(T lhs, U rhs)
    {
        return lhs + rhs;
    }
    #endif
```
```cpp
    //  example/term_explanation/decltype_ut.cpp 201

    ASSERT_EQ(add(1, 2), 3);

    ASSERT_DOUBLE_EQ(add(1.5, 2.5), 4.0);

    using namespace std::literals::string_literals;

    ASSERT_EQ(add("hello"s, "world"s), "helloworld"s);
```


## 型推論 <a id="SS_19_12"></a>
### AAAスタイル <a id="SS_19_12_1"></a>
このドキュメントでのAAAとは、単体テストのパターンarrange-act-assertではなく、
almost always autoを指し、
AAAスタイルとは、「可能な場合、型を左辺に明示して変数を宣言する代わりに、autoを使用する」
というコーディングスタイルである。
この用語は、Andrei Alexandrescuによって造られ、Herb Sutterによって広く推奨されている。

特定の型を明示して使用する必要がない場合、下記のように書く。

```cpp
    //  example/term_explanation/aaa.cpp 11

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
    //  example/term_explanation/aaa.cpp 51

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
    //  example/term_explanation/aaa.cpp 94

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
    //  example/term_explanation/aaa.cpp 121

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
    //  example/term_explanation/aaa.cpp 148

    template <typename F, typename T>
    auto apply_0(F&& f, T value)
    {
        return f(value);
    }
```

ただし、インライン関数や関数テンプレートが複雑な下記のような場合、
AAAスタイルは出来る限り避けるべきである。

```cpp
    //  example/term_explanation/aaa.cpp 156

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
    //  example/term_explanation/aaa.cpp 183

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
    //  example/term_explanation/aaa.cpp 197

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

### decltype <a id="SS_19_12_2"></a>
decltypeはオペランドに[expression](term_explanation.md#SS_19_14_1)を取り、その型を算出する機能である。
下記のコードにあるようなautoの機能との微妙な差に気を付ける必要がある。

```cpp
    //  example/term_explanation/decltype_ut.cpp 13

    int32_t  x{3};
    int32_t& r{x};

    auto        a = r;  // aの型はint32_t
    decltype(r) b = r;  // bの型はint32_t&

    // std::is_sameはオペランドの型が同じか否かを返すメタ関数
    static_assert(std::is_same_v<decltype(a), int>);
    static_assert(std::is_same_v<decltype(b), int&>);
```

decltypeは、テンプレートプログラミングに多用されるが、
クロージャ型(「[ラムダ式](term_explanation.md#SS_19_8_3)」参照)
のような記述不可能な型をオブジェクトから算出できるため、
下記例のような場合にも有用である。

```cpp
    //  example/term_explanation/decltype_ut.cpp 28

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

        ...
        // do something for a_ptr
        ...

        // a_ptrによるメモリの自動解放
    }
```

### decltype(auto) <a id="SS_19_12_3"></a>
decltype(auto)はC++14から導入されたdecltypeの類似機能である。

auto、decltype、decltype(auto)では、以下に示す通りリファレンスの扱いが異なることに注意する必要がある。

```cpp
    //  example/term_explanation/decltype_ut.cpp 63

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

### 戻り値型を後置する関数宣言 <a id="SS_19_12_4"></a>
関数の戻り値型後置構文は戻り値型をプレースホルダ(auto)にして、
実際の型を->で示して型推論させるシンタックスを指す。実際には関数テンプレートで使用されることが多い。
コード例を以下に示す。

```cpp
    //  example/term_explanation/decltype_ut.cpp 82

    template <typename T, typename U>
    auto add(T a, U b) -> decltype(a + b)
    {
        return a + b;
    }

    static_assert(std::is_same_v<decltype(add(1, 2)), int>);  // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(1u, 2u)), uint32_t>);  // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(std::string{"str"}, "2")),
                                 std::string>);  // addの戻り値型はstd::stringに型推論
```

この構文をC++11から導入された理由は以下のコードを見れば明らかだろう。

```cpp
    //  example/term_explanation/decltype_ut.cpp 97

    template <typename T, typename U>  // 戻り値型を後置する関数宣言
    decltype(std::declval<T>() + std::declval<T>()) add(T a, U b)
    {
        return a + b;
    }

    static_assert(std::is_same_v<decltype(add(1, 2)), int>);  // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(1u, 2u)), uint32_t>);  // addの戻り値型はintに型推論
    static_assert(std::is_same_v<decltype(add(std::string{"str"}, "2")),
                                 std::string>);  // addの戻り値型はstd::stringに型推論
```

### 関数の戻り値型auto <a id="SS_19_12_5"></a>
C++14から導入された機能で、関数の戻り値の型をautoキーワードで宣言することで、
コンパイラがreturn文から自動的に型を推論してくれる機能である。
これにより、複雑な型の戻り値を持つ関数でも、より簡潔に記述できるようになる
(「[autoパラメータによる関数テンプレートの簡易定義](term_explanation.md#SS_19_11_10)」を参照)。

```cpp
    //  example/term_explanation/decltype_ut.cpp 114

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
    //  example/term_explanation/decltype_ut.cpp 144

    auto result = split("hello,world", ',');

    ASSERT_EQ(result.size(), 2);
    ASSERT_EQ(result[0], "hello");
    ASSERT_EQ(result[1], "world");
```

### 後置戻り値型auto <a id="SS_19_12_6"></a>
C++14から導入された[関数の戻り値型auto](term_explanation.md#SS_19_12_5)と似た、
関数の戻り値の型を関数本体の後に-> autoと書くことでができる機能である。
autoプレースホルダーとし、そのプレースホルダーを修飾することで、戻り値型の推論を補助できる。

```cpp
    //  example/term_explanation/decltype_ut.cpp 154

    int16_t gvalue = 1;

    auto getValue(int16_t a) -> auto& { return gvalue += a; }
```
```cpp
    //  example/term_explanation/decltype_ut.cpp 163

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


## explicit <a id="SS_19_13"></a>
explicitは、コンストラクタに対して付与することで、
コンストラクタによる暗黙の型変換を禁止するためのキーワードである。
暗黙の型変換とは、ある型の値を別の型の値に自動的に変換する言語機能を指す。
explicitキーワードを付けることで、意図しない型変換を防ぎ、コードの堅牢性を高めることがでできる。

この節で説明するexplicitの機能は下記のような項目に渡って説明を行う。

- [暗黙の型変換](term_explanation.md#SS_19_13_1)
- [暗黙の型変換抑止](term_explanation.md#SS_19_13_2)
- [explicit type operator()](term_explanation.md#SS_19_13_3)
- [explicit(COND)](term_explanation.md#SS_19_13_4)

### 暗黙の型変換 <a id="SS_19_13_1"></a>
この節で扱う暗黙の型変換とは、
以下に示したような「非explicitなコンストラクタを持つクラス」による暗黙の型変換を指し、
[汎整数型昇格](term_explanation.md#SS_19_1_7)や[算術変換](term_explanation.md#SS_19_1_6)等を指さない。

```cpp
    //  example/term_explanation/implicit_conversion_ut.cpp 8

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
    //  example/term_explanation/implicit_conversion_ut.cpp 40

    void f(Person const& person) noexcept
    {
        ...
    }

    void using_implicit_coversion()
    {
        f("Ohtani");  // "Ohtani"はPerson型ではないが、コンパイル可能
    }
```

この記法は下記コードの短縮形であり、コードの見た目をシンプルに保つ効果がある。

```cpp
    //  example/term_explanation/implicit_conversion_ut.cpp 54

    void not_using_implicit_coversion()
    {
        f(Person{"Ohtani"});  // 本来は、fの引数はPerson型
    }
```

この記法は下記のようにstd::string等のSTLでも多用され、その効果は十分に発揮されているものの、

```cpp
    //  example/term_explanation/implicit_conversion_ut.cpp 66

    auto otani = std::string{"Ohtani"};

    ...

    if (otani == "Ohtani") {  // 暗黙の型変換によりコンパイルできる
        ...
    }
```

以下のようなコードがコンパイルできてしまうため、わかりづらいバグの元にもなる。

```cpp
    //  example/term_explanation/implicit_conversion_ut.cpp 80

    auto otani = Person{"Ohtani", 26};

    ...

    if (otani == "Otani") {  // このコードがコンパイルされる。
        ...
    }

    if (otani == Person{"Otani"}) {  // 暗黙の型変換を使わない記法
        ...
    }
```

下記のようにコンストラクタにexplicitを付けて宣言することにより、この問題を防ぐことができる。

```cpp
    //  example/term_explanation/implicit_conversion_ut.cpp 112

    class Person {
    public:
        explicit Person(char const* name, uint32_t age = 0) : name_{name}, age_{age} {}
        Person(Person const&)            = default;
        Person& operator=(Person const&) = default;

        ...
    };

    void prohibit_implicit_coversion()
    {
    #if 0  // explicit付きのコンストラクタを持つPersonと違い、コンパイルできない。
        f("Ohtani");
    #else
        f(Person{"Ohtani"});
    #endif

        auto otani = Person{"Ohtani", 26};

        ...

    #if 0
        if (otani == "Otani") {  // このコードもコンパイルできない。
            ...
        }
    #else
        if (otani == Person{"Otani", 26}) {  // この記述を強制できる。
            ...
        }
    #endif
    }
```

std::stringは暗黙の型変換を許して良く、(多くの場合)Personには暗黙の型変換をしない方が良い理由は、

* std::stringの役割は文字列の管理と演算のみであるため、
  std::stringを文字列リテラルと等価なもののように扱っても違和感がない
* Personは、明らかに文字列リテラルと等価なものではない

といったセマンティクス的観点(「[シンタックス、セマンティクス](term_explanation.md#SS_19_17)」参照)によるものである。

クラスPersonと同様に、
ほとんどのユーザ定義クラスには非explicitなコンストラクタによる暗黙の型変換は必要ない。

### 暗黙の型変換抑止 <a id="SS_19_13_2"></a>
explicit宣言されていないコンストラクタを持つクラスは、
下記のコードのように[暗黙の型変換](term_explanation.md#SS_19_13_1)が起こる。

```cpp
    //  example/term_explanation/explicit_ut.cpp 10

    struct A {
        A(int a) : x{a} {}
        int x;
    };

    A f(A a) { return a; };
```
```cpp
    //  example/term_explanation/explicit_ut.cpp 21

    A a = 1;  // A::Aがexplicitでないため、iはA{1}に変換される
    ASSERT_EQ(a.x, 1);

    auto b = f(2);  // A::Aがexplicitでないため、2はA{2}に変換される
    ASSERT_EQ(b.x, 2);
```

暗黙の型変換はわかりづらいバグを生み出してしまうことがあるため、
下記のように適切にexplicitを使うことで、このような変換を抑止することができる。

```cpp
    //  example/term_explanation/explicit_ut.cpp 34

    struct A {
        explicit A(int a) : x{a} {}  // 暗黙の型変換の抑止
        int x;
    };

    A f(A a) { return a; };
```
```cpp
    //  example/term_explanation/explicit_ut.cpp 45

    // A a = 1;    // A::Aがexplicitであるため、コンパイルエラー
    // auto b = f(2);  // A::Aがexplicitであるため、コンパイルエラー
```

C++03までは、[一様初期化](term_explanation.md#SS_19_5_2)がサポートされていなかったため、
explicitは単一引数のコンストラクタに使用されることが一般的であった。

C++11からサポートされた[一様初期化](term_explanation.md#SS_19_5_2)を下記のように使用することで、
暗黙の型変換を使用できる。

```cpp
    //  example/term_explanation/explicit_ut.cpp 56

    struct A {
        A(int a, int b) : x{a}, y{b} {}
        int x;
        int y;
    };

    A    f(A a) { return a; };
    bool operator==(A lhs, A rhs) { return std::tuple(lhs.x, lhs.x) == std::tuple(rhs.x, rhs.x); }
```
```cpp
    //  example/term_explanation/explicit_ut.cpp 70

    A a = {1, 2};  // A::Aがexplicitでないため、iはA{1, 2}に変換される
    ASSERT_EQ(a, (A{1, 2}));

    auto b = f({2, 1});  // A::Aがexplicitでないため、2はA{2,1}に変換される
    ASSERT_EQ(b, (A{2, 1}));
```

以下に示す通り、コンストラクタの引数の数によらず、
C++11からは暗黙の型変換を抑止したい型のコンストラクタにはexplicit宣言することが一般的となっている。

```cpp
    //  example/term_explanation/explicit_ut.cpp 82

    struct A {
        explicit A(int a, int b) : x{a}, y{b} {}
        int x;
        int y;
    };

    A    f(A a) { return a; };
    bool operator==(A lhs, A rhs) { return std::tuple(lhs.x, lhs.x) == std::tuple(rhs.x, rhs.x); }
```
```cpp
    //  example/term_explanation/explicit_ut.cpp 96

    // A a = {1, 2};  // A::Aがexplicitであるため、コンパイルエラー
    // auto b = f({2, 1});  // A::Aがexplicitであるため、コンパイルエラー
```

### explicit type operator() <a id="SS_19_13_3"></a>
型変換演算子のオーバーロードの戻り値をさらに別の型に変換すると、
きわめてわかりづらいバグを生み出してしまうことがあるため、
この機能を使用すると型変換演算子のオーバーロードの型変換の抑止することができる。

```cpp
    //  example/term_explanation/explicit_ut.cpp 110

    struct A {
        explicit A(int a) : x{a} {}  // 暗黙の型変換の抑止
        operator bool() const noexcept { return x; }
        int x;
    };
```
```cpp
    //  example/term_explanation/explicit_ut.cpp 123

    auto a = A{2};

    ASSERT_TRUE(a);
    ASSERT_EQ(1, a);  // aをboolに変換するとtrue、trueをintに変換すると1

    int b = a + 1;  // aをboolに変換するとtrue、trueをintに変換すると1であるため、bは2
    ASSERT_EQ(b, 2);

```

以下に示すようにexplicitを使うことで、このような暗黙の型変換を抑止できる。

```cpp
    //  example/term_explanation/explicit_ut.cpp 137

    struct A {
        explicit A(int a) : x{a} {}  // 暗黙の型変換の抑止
        explicit operator bool() const noexcept { return x; }// 暗黙の型変換の抑止
        int x;
    };
```
```cpp
    //  example/term_explanation/explicit_ut.cpp 150

    auto a = A{2};

    // ASSERT_EQ(1, a);  // operator boolがexplicitであるため、コンパイルエラー
    // int b = a + 1;  // operator boolがexplicitであるため、コンパイルエラー
```

### explicit(COND) <a id="SS_19_13_4"></a>
C++20から導入されたexplicit(COND)は、
コンストラクタや変換演算子に対して、
特定の条件下で暗黙の型変換を許可または禁止する機能である。
CONDには、型特性や定数式などの任意のconstexprな条件式を指定できる。
以下にこのシンタックスの単純な使用例を示す。

```cpp
    //  example/term_explanation/explicit_ut.cpp 162

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
    //  example/term_explanation/explicit_ut.cpp 190

    S s = 1;      // Tがintであるため、explicit宣言されていないため、暗黙の型変換は許可
    // S t = 1.0; // Tが整数型でないため暗黙の型変換は禁止であるため、コンパイルエラー
    S t{1.0};     // Tが整数型でないが、明示的な初期化は問題ない

    ASSERT_EQ(s.value, 1);
```

テンプレートのパラメータの型による暗黙の型変換の可否をコントロールする例を以下に示す。

```cpp
    //  example/term_explanation/explicit_ut.cpp 203

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
    //  example/term_explanation/explicit_ut.cpp 235

    Optional a = 2;   // T == intであるため、暗黙の型変換を許可
    ASSERT_TRUE(a);   // has_value_がtrueであるため
    ASSERT_EQ(a, 2);  // T型への暗黙的変換をチェック

    // Optional n = nullptr; // T == std::nullptr_tのため暗黙の型変換抑止により、コンパイルエラー
    Optional n{nullptr};  // 通常の初期化
    ASSERT_FALSE(n);
```

こういった工夫により、コードの過度な柔軟性を適度に保つことができ、
可読性の向上につながる。


## expressionと値カテゴリ <a id="SS_19_14"></a>
ここでは、expression(式)の値カテゴリや、それに付随した機能についての解説を行う。

### expression <a id="SS_19_14_1"></a>

C++においてexpression、lvalue、rvalue、xvalue、glvalue、prvalueは以下のように定められている。

* [expression](https://ja.cppreference.com/w/cpp/language/expressions)(式)
  とは「演算子とそのオペランドの並び」である(オペランドのみの記述も式である)。
  演算子とは以下のようなものである。
    * 四則演算、代入(a = b、a += b ...)、インクリメント、比較、論理式
    * 明示的キャストや型変換
    * メンバアクセス(a.b、a->b、a[x]、 \*a、&a ...)
    * 関数呼び出し演算子(f(...))、sizeof、decltype等

* expressionは、以下のいずれかに分類される。lvalueでないexpressionがrvalueである。
    * lvalue
    * rvalue

* lvalueとは、関数もしくはオブジェクトを指す。

* rvalueは、以下のいずれかに分類される。
    * xvalue
    * prvalue

* xvalueとは以下のようなものである。
    * 戻り値の型がT&&(Tは任意の型)である関数の呼び出し式(std::move(x))
    * オブジェクトへのT&&へのキャスト式(static_cast<char&&>(x))
    * aを配列のrvalueとした場合のa[N]や、
      cをクラス型のrvalueとした場合のc.m(mはaの非staticメンバ)等

* prvalueとは、オブジェクトやビットフィールドを初期化する、
  もしくはオペランドの値を計算する式であり、以下のようなものである。
    * 文字列リテラルを除くリテラル
    * 戻り値の型が非リファレンスである関数呼び出し式、
      または前置++と前置--を除くオーバーロードされた演算子式(path.string()、str1 + str2、it++ ...)
    * 組み込み型インスタンスaのa++、a\-\-(++a、\-\-aはlvalue)
    * 組み込み型インスタンスa、bに対する
      a + b、 a % b、 a & b、 a && b、 a || b、 !a、 a < b、 a == b等

* glvalueは、以下のいずれかに分類される。
    * lvalue
    * xvalue

<!-- pu:deep/plant_uml/rvalue.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAEmCAIAAACLfU5zAAAayElEQVR4Xu2de1QV173HD/jgKQ+PMSiYCyTxKhpwpVXWhdZ4lchakaRGl0ajbTFgdMUoxcu9WL2r7VJUNISkpoChy2c0YoO9agS9VYlYqpHUXkWTRkAbLAnxjdrwhtyf7DDd7nPwMGdmDuPM97O+f+zXzBn27M+ZPUGN5VsAgEGxiA0AAKMAvQEwLP/UuwMAYAigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigNwCGBXoDYFigN7BDbm7u+fPnxVbwsAG9gR0sFgsZLraChw3orRcaGxsPHjxYUFBQV1dH1d27d2/atKm9vZ3Kt2/fJtnKyso6Op+rFy5cOHr06I4dO6qrq6XDqf3ixYvl5eUbNmyQGoVzMkpKSrZs2fLpp58+oEWgqanp8OHDdJ7a2lq+nT60qqrq9OnT27dvLyoqam5u5ntBrwO9dcGVK1ciIyMtnfj5+Z04cYLspXJ+fj71Ll682MfHh0Tq6HyuBgcHs5H9+/ffuXMnOwNVU1NT3dzcEhISujsnOxVroZHr1q2z28LOJj29r1279v3vf5+NocvYs2cPa2fDIiIiWBcxduzYlpYWqRf0OtBbFyxcuDAqKooevxUVFSEhIbGxsdQ4derUgQMHfvjhh+7u7tIzmSwaNGjQsWPHbt26NX/+/ICAgOvXr7P2IUOGlJaW0pP2Aef09fV9/fXXb968mZeXd/XqVbst7GyS3q+99hp9O9DegTx//vnnrVYrfbQ0bMCAAXv37v3mm2/oAU7VQ4cOsS6gB6C3LggNDU1KSsrtZMqUKeQzWUo7anKJys888wzbpXd0GrV27VpWvnz5MlVp+83aFyxYIJ2wo5tzTpgwYdiwYfTMb21tZcNsWzru1/uxxx5LS0tj5crKSukT2bCVK1eyMj23qfruu++yKtAD0FsXeHt7s/2tBNuKP/vss1TOyMiQRlo48e7evUtVemyy9pycHGlYRzfnvHHjxpIlS7y8vKKjoxsaGmiYbQs7m/QptCHPyspiZf4ThWG2VdDrQG9dQLvorVu3snJbWxu9NlNhy5YtJAxtqsm9CxcusF5q+dnPfsbKRUVFVD158iRrF9Sye062dT979iyN3717t92WjvvPNmbMmBdffJGV+U8UhtlWQa8DvXXB5s2byeGUlBTaeMfExAQFBX322Wf+/v6zZ8+ur68fOnQoSU6KdnQq5Obm9uqrr65Zs4aGjRs3ju3bbdWyPSe9GD/yyCO006aXbUvne/Lx48eFFnYsf7ZNmzZRdd68ebSJGDx4MJ2Kf1OA3noGeusFEmP48OGenp60ST527FhcXFxAQAD7hdaePXvIHLZDpkJ8fHxYWJivr+9zzz1Hr9/scLtq8ecsLS29desWfS8EBgbSF0dqaioNsG1hCGd76623wsPD6XpmzJjBdgF2h9m9BtCLQO+HDCgEeg70fsiA3qDnQO+HjAULFtA2W2wFwB7QGwDDAr0BMCzQGwDDAr0BMCzQGwDDAr0BMCya6G21Wi0AAGWQR6JaMtFEb7oysQkAIBPlHkFvAHSKco+gNwA6RblH0BsAnaLcI+gNgE5R7hH0BkCnKPcIegOgU5R7BL0B0CnKPYLeAOgU5R5BbwB0inKPoDcAOkW5R9AbAJ2i3CPoDYBOUe4R9AZApyj3CHoDoFOUewS9AdApyj2C3gDoFOUeQW8AdIpyj6A3ADpFuUfQGwCdotwjdfSOjIy0dAN1iaMBAPZQ3SN19M7MzBQvpwvqEkcDAOyhukfq6F1TU+Pu7i5ekcVCjdQljgYA2EN1j9TRm5gwYYJ4URYLNYrjAADdo65Hqumdn58vXpTFQo3iOABA96jrkWp637x508PDg78mqlKjOA4A0D3qeqSa3sS0adP4y6KqOAIA4AgVPVJT78LCQv6yqCqOAAA4QkWP1NS7sbExMDCQXRMVqCqOAAA4QkWP1NSbSE5OZpdFBbEPANAz1PJIZb1LSkrYZVFB7AMA9Ay1PFJZ7/b29mGdUEHsAwD0DLU8UllvIr0TsRUAIAdVPFJf77OdiK0AADmo4pH6egMAdAL0dpKWlhbn3oucPhAAuUBvJ7FYLLm5uWJrD3D6QADkAr2dxGlLnT4QALlA7x5x6dKlHTt2FBQULFu2bNy4cU1NTbyl+fn5xcXF0uBt27YdOHCAClVVVVQuKipqbm6WevkDqXD+/Hmpi682NjYePHiQPrGurk4aAIAsoLdjCgsL+b/Ek5KSQu/PvKUvvPCC1WplDldWVlJXdnZ2VlaW9Ffzo6OjJcP5A/kyX71y5Yr07/L4+fmdOHFCGgNAz4HejgkPD4+Pj79169Z7771Hvu3du7fjfjP37dtHVfbEXrlyJX0XfPXVV3Pnzk1MTCRRP/jgA+rdv38/G9wTvRcuXBgVFXXx4sWKioqQkJDY2FhpDAA9B3o7hp6f69ato0J9fT0ZuH379o77zWxtbQ0ODp4zZw6VR40aNWvWrI7OP3hEO/b09HSq0uC8vDw2uCd6h4aGJiUl5XYyZcoU2gXQ64A0DIAeAr0dQ34GBQVlZmYmJCT07duX3qg7bMxcsWKFr6/vqVOnqP3w4cPUsmTJkj59+kyaNIn99QC7Snent7e3t+V+2IcCIAvo7Zjnn3+etsqDBw+mh+rOnTtZo2AmbaTd3NzGjh1LO3n2a21/f39yngrV1dX8YL5MGkv/AiY96qUu+ritW7ey9ra2NtrhszIAsoDejqFHd2BgYFxc3PTp01NTU//4xz922OhN0ABqzMjIYNWIiIjRo0evX7+eCmS+1M4fOHHiRLYvSEtL8/Hxkbo2b97s5eWVkpKydu3amJgYGnP79m12CAA9B3o7hvTj/3laKn/88ce2ehcUFNBuvLa2llVPnjw5cuRIej4nJibGx8fTxp618wdeunRp8uTJtKsPCwtbvXo1veRLXVQYPny4p6dndHR0aWkpawRAFtDbMQEBAePGjcvOzs7JyVm6dCn5uW/fPnEQAPoDejtm165dkZGRXp3QW/GGDRvEEQDoEugNgGGB3gAYFugNgGGB3gAYFugNgGGB3gAYFugNgGHRRG+r1Sr9GS8AeGhtiMsFaIYmetNdFJsA6ARrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZcCfQGLgVrw5VAb+BSsDZciTp6R0ZGWrqBusTRwExgbfQi6uidmZkp3rouqEscDcwE1kYvoo7eNTU1/P/gXoIaqUscDcwE1kYvoo7exIQJE8QbaLFQozgOmA+sjd5CNb3z8/PFG2ixUKM4DpgPrI3eQjW9b9686eHhwd8/qlKjOA6YD6yN3kI1vYlp06bxt5Cq4ghgVrA2egU19S4sLORvIVXFEcCsYG30Cmrq3djYGBgYyO4fFagqjgBmBWujV1BTbyI5OZndQiqIfcDcYG24HpX1LikpYbeQCmIfMDdYG65HZb3b29uHdUIFsQ+YG6wN16Oy3kR6J2IrAFgbLkd9vc92IrYCgLXhctTXGwCgE6A3AIYFegNgWKA3AIYFegNgWKA3AIYFegNgWDTRu39/P/bHD02O1WqV5sRq7St2mwx+NnwCfMRuYAM/Y86hid50ZTNmHEZoHurr6+/evdvQ0EDlb7/9npkjzMa7F99FHhx+xpqbm9va2kTTHAG9NQzNQ01NTV1d3Y0bN6C3MBu2qxkRws8YSU6Gi6Y5AnprGJqHc+fOVVVV1dbWQm9hNmxXMyKEnzEynJ7hommOgN4ahuahrKzszJkzdIegtzAbtqsZEcLPGD3D6QEumuYI6K1haB6Ki4vpDtF3MPQWZsN2NSNC+BmjXTq9h4umOQJ6axiah127dh06dKi8vBx6C7Nhu5oRIfyM0QOc9ueiaY6A3hoGevOB3nIDvXUd6M0HessN9NZ1oDcf6C030FvXgd58oLfcQG9dB3rzgd5yA711HejNB3rLDfTWdaA3H+gtN9Bb14HefKC33EBvXQd684HecgO9dR3ozQd6yw301nWgNx/oLTfQW9eB3nygt9xAb10HevOB3nIDvXUd6M0HessN9NZ1oDcf6C03ZtF71qwjM2eKjQ7j3FEqRm96t7Y+3dEhNrosD5feeZV5G6s32ra7MmbRm64qP/+vtu0PjnNHqRi96U3XkJf3mG27a/Jw6U1XOGfVHNt2VwZ6PyjOHaVioDcf6C03ptN748bPVq/+i9T+zjvn16z5P1Z+/fWyzupfaE8uHMVC5dTUE3arL798NCPjL9nZFcnJpdIA5VFd79/9Lnzz5lC2wb5zZwy5umxZ0MGDT0oDtm8PLSp6gpWrq0dTtbj4iZaWp1mLoDeVP/10lN1qU9PThw49uXt3+NdfR0oDFEY7vcnDVUdXLd25NOmtpNXHVvPtVF2+d/msX86i6o/X/HjJliVS77yseYs3LaZCxkcZ98qbF+deyJV6eb2p8Kv//RV/Wqma89ccOuf8DfPfOPWGNECtmE7vTz65eudOCxN48eI/UfvWrReovG3bhY6uH6aysp4NkI4STiJUk5JKv/jiLju2oaF1+fJy4dOdjup679wZRuf57W//hcqLFw/28XGfNGmA1dqXCVxVNZp633prGJXffDPE3d3CiI72YQMEvburXr0aFRnpxY718+tz8uQI4TKcizAbtqvZ6dDZAh4NYBfct1/f5LeTpfa4V+Lc3NwiJ0ZSNSouyifAhzm8qmQV9c7875kzls9wc3djx4aNCZMMt3B682W+mvVJVsiIEHasp69nemE6f1XKYzGb3pmZZ6jMntgFBdUtLe2vvHKMZD5+/KuPPvqSRM3KOksDMjPvDZCOEk4iVP/wh79/8cWdRYvKli49ef160+ef37K9AOfC3x6LGnpTpk4NGDiw74EDT5C977wzbP/+J+jM7Im9atVQDw+369ejSOa5cwcmJlpJ1MLCcBrw4Yf3Bli68VmoLlz4SFSU16VLo8+diwgJ6R8b62t7GU5EmA3b1ex06Gy+gb5pu9LePvP2D2f90NvPO/t0Nmv3H+yfVpCW83kOVRflL6IW9sT+0dIf9e3flx650VOjY6bHkKgLchZQ76LfLpLO6VDv8S+PDxkZQhuEXx78ZWBQ4OPfe1y4MIXhZ8wUer/00pEbN5qOH6+j8uXL/ygr+5oNmDnzMG3a9+79G7V0Dv6MP0o4iVC9erXh6NEvqUw5ffoaXf/s2Uf5T3c6woK2XfFOhHbL9Lgmt595ZgDt0tvang4O7jdnzkDqGjXKa9asewUKddGmPT09iFroozduvOdtdz4L1dDQ/klJg6hMmTLFnz6rufm77b2SCLNhu5qdDp1t2n9NY+XMP2VSlW3CqTB+9nhpWF5lHj3ko38UTeWhTw4dmzCWChurN9Lg+AXxVL3nbYYdpfkyX7WGWGNnxlKZ8tS/P0W7APY9olb4GTOF3pQ9ey41NrYtW3aKGleuPM0ai4svt7d3VFTcOHKkVhrMH/WAalNTm/SzM+g1nv90pyMsaNsV71yeffbe/6Fx9epgVl2xYoivr3t5+QhqPHJkOGtcsmRwnz5utHVPTh4keSsVWLqrent3beu7oNd4/gKci0VLvSX9NpzbQNVX3nyFtb+88mV+5HOLnvPw9vj5//yculLfS6WWiT+d6N7HfUTMiB+89AP+PN2V+Wp/r/5dM/Qd9BrPf5zCWEyoN+2i6bKrq29//XWD9Gvtb75pJe1ndP4HNmkwf9SMTo137KhkZXrUS720M//Nb86z9pkzj9AOXzpEYfjbY1FJ761bQ+lUtGH28nKvrLxnHe2i3dwsY8f6hId7SL/W9vfvQ9pT4eLFey/kdvUmjdet++47gh71Ui/tzLdtC2Xt7e33XsWlQ5REmA3b1ex06GyT5k1i5cWbF1N12Z5lrJ3XkkIbaXoVD40MHTRsEPu1ttcAL3KedfHj+TJpPC39u90BPeqlLtqZz8uax9o3Vm2kHT7/WcrDz5hZ9KbQU5pa3n+/Wmr5+9//cfny3e3bK6lAPxTrEo46d+7GrVvNZPj+/V+wJzbrzcn5tLm5vaioZseOqs8/r6cxP/lJiXABzkVY0LYrXm4uX36KvJ09e+Dt22OGDu1HkpN+1B4Xd9/znBIR4Tl6tNcbb4RQgeRnXYLeEycOCArqR4anpT3q43Pvic16t2wJpe+OlJTBmZnBMTG+NObOnTG2FyM3mupN0tJb94v/+aLfI36hUaFMXVu9KSNjR1L71P+YyqpDnhgydPjQ6cumU4FOIrXzx474txF0WjJ88vzJ9PCXun66/qf9PPtNSpxErwaPP/04jfl1xa+Fj1MSk+qdnV1BW/FXXz0utSxfXl5b+w+S9qOPvjxz5vqf/3zN9qjXXiujLtrYX7nS8P77VQ0NrVIvFb766puWlvbKyvpf/OIT/qOVRF296clMGgcE9GG/rPr97x+nc775ZgiVd+8Op634l1/+85dYH388YuRIT3o+JyZa4+P9EhL8v7XR+29/e2ryZD/a2IeFeaxZE+zn10fqpcLw4Z6enu7R0T7Hj/+rcCXORVO9R40fRQ9kcm/0hNH0+i212+o9f8N82o2vO7GOVek5T2LT8zlmegydhP03duHYNaVrIn4YQSenj5iaNtXT11PqosKjYY/28+gXNiYsrSBN+CyFMYveD2nU1fthj6Z622psgEBvXQd684HecgO9dR3ozUc7vcfPHq/6xlgPgd66DvTmo53eRg301nWgNx/oLTfQW9eB3nygt9xAb10HevOB3nIDvXUd6M0HessN9NZ1oDcf6C030FvXgd58oLfcQG9dB3rzgd5yA711HejNB3rLDfTWdaA3H+gtN9Bb14HefKC33EBvXQd684HecgO9dR3ozQd6yw301nWgNx/oLTfQW9eB3nygt9xAb10HevOB3nIDvXUd6M0HessN9NZ1oDcf6C030FvXgd58oLfcQG9dB3rzgd5yo1O9rVarBVgsPj4+0u0JCPjuf2FpWjAbcuFnTEd6E/X19TU1NefOnSsrKysuLt5lVuhnpxmgeajpwsxzgtmQCz9j5JSomSO00vvu3bt1dXX0lXPmzBm6vkNmhX52mgGah7ouzDwnmA258DNGTomaOUIrvRsaGmgvUVtbS1dG3z3lZoV+dpoBmocbXZh5TjAbcuFnjJwSNXOEVno3NzfTlw1dE33r0L6iyqzQz04zQPNwtwszzwlmQy78jJFTomaO0ErvtrY2uhr6vqHLoncG6dvabNDPTjNA89DchZnnBLMhF37GyClRM0dopTcAoNeB3tpythOxFQBHqLJyoLe2pHcitgLgCFVWDvTWkPb29mGdUEHsA6B71Fo50FtDSkpK2B8/ooLYB0D3qLVyoLeGJCcns5tEBbEPgO5Ra+VAb61obGwMDAxkN4kKVBVHAGAPFVcO9NaKwsJCdocYVBVHAGAPFVcO9NaKadOm8TeJquIIAOyh4sqB3ppw8+ZNDw8P/iZRlRrFcQDcj7orB3prQn5+Pn+HGNQojgPgftRdOdBbEyZMmCDeIouFGsVxANyPuisHeqtPTU2Nu7u7eIssFmqkLnE0AF2ovnKgt/pkZmaK96cL6hJHA9CF6isHeqtPZGSkeHO6oC5xNABdqL5yoLfm0L0RmwDoAcpXDvTWHOU3CZgT5SsHemuO8psEzInylQO9NUf5TQLmRPnKgd6ao/wmAXOifOVAb81RfpOAOVG+cqC35ii/ScCcKF850FtzlN8kYE6UrxzorTnKbxIwJ8pXDvTWHOU3CZgT5SsHemuO8psEzInylQO9NUf5TQLmRPnKgd6ao/wmAXOifOVAb81RfpOAOVG+cqC35ii/ScCcKF850FtzlN8kYE6UrxzorTnKbxIwJ8pXDvTWHOU3CZgT5SsHemuO8psEzInylQO9NUf5TQLmRPnKgd6ao/wmAXOifOVAb82xWq0WAORDK0dcTDKB3gAYFugNgGGB3gAYFugNgGGB3gAYFugNgGGB3gAYFugNepmWlpb29naxFagB9Aa9jMViyc3NFVuBGkBv0MtAb+2A3kAdSNGLFy+Wl5dv2LAhPz+/uLhY6tq2bduBAwdYuaqqiqpFRUXNzc2sRdCbyufPn7dbbWxsPHjwYEFBQV1dnTQAPADoDdSBLE1NTXVzc0tISHjhhResVisTuLKykrqys7OpnJWV5e7uzv5AdXR0NBsg6N1d9cqVK5GRkexYPz+/EydOSGNAd0BvoA5k3ZAhQ0pLS5uamvbt20dV9sReuXKlh4fHtWvXSOa5c+cmJiaSqB988AEN2L9/PzvQrs9CdeHChVFRUbRBqKioCAkJiY2NlcaA7oDeQB3IwwULFrBya2trcHDwnDlzqDxq1KhZs2ax9vb2dtq0p6enUwuNz8vLYwfa9VmohoaGJiUl5XYyZcoU2gXQ94g0DNgFegN1IA9zcnKk6ooVK3x9fU+dOkXthw8fZo1Llizp06fPpEmTkpOTJW+781moent7W+6HXuOlYcAu0Buog6Al7aLpPXzs2LHh4eHSr7X9/f1JeypUV1dL44UDSePMzExWpke91Es7861bt7L2trY22uFLh4DugN5AHQRLibi4OGrMyMiQWiIiIkaPHr1+/XoqkPysSzhw4sSJQUFBZHhaWpqPj4/Uu3nzZi8vr5SUlLVr18bExNCY27dvS0cBu0BvoA62ehcUFNBWvLa2Vmo5efLkyJEj6fmcmJgYHx+fkJDQYXPgpUuXJk+eTBv7sLCw1atX+/n5Sb1UGD58uKenZ3R0dGlpqXQI6A7oDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhgd4AGBboDYBhsaM3AMBgQG8ADAv0BsCw/D8r68UG6uhq2wAAAABJRU5ErkJggg==" /></p>

ざっくりと言えば、lvalueとは代入式の左辺になり得る式、rvalueとは代入式の左辺にはなり得ない式である。
T const&は左辺になり得ないが、lvalueである。rvalueリファレンス(T&&)もlvalueであるため、
rvalueであることとrvalueリファレンスであることとは全く異なる。

xvalueとは、多くの場合、「std::move()の呼び出し式のことである」と考えても差し支えない。

prvalueとは、いわゆるテンポラリオブジェクトのことであるため
(下記のstd::string()で作られるようなオブジェクト)、名前はない。
また、アドレス演算子(&)のオペランドになれない。

```cpp
    //  example/term_explanation/rvalue_lvalue_ut.cpp 8

    {
        // sを初期化するためにstd::string{}により生成されるオブジェクトはprvalue
        // sはlvalue

        auto s = std::string{};

    #if 0
        // 下記はコンパイルエラー

        auto* sp = &std::string{};
        // 下記はg++のエラーメッセージ
        // programming_convention_type.cpp|709 col 29| error: taking address of rvalue [-fpermissive]
        // ||   709 |     auto* sp = &std::string{};
    #else
        // 下記のようにすればアドレスを取得できるが、このようなことはすべきではない。
        auto&& rvalue_ref = std::string{};
        auto   sp         = &rvalue_ref;
    #endif
        static_assert(std::is_same_v<std::string*, decltype(sp)>);
    }
```

C++11でrvalueの概念の整理やstd::move()の導入が行われた目的はプログラム実行速度の向上である。

* lvalueからの代入
* rvalueからの代入
* std::move(lvalue)からの代入

の処理がどのように違うのかを見ることでrvalueの効果について説明する。

1. 下記コードにより「lvalueからの代入」を説明する。

    ```.cpp
    //  example/term_explanation/rvalue_lvalue_ut.cpp 35

    auto str0 = std::string{};        // str0はlvalue
    auto str1 = std::string{"hehe"};  // str1もlvalue
    str0      = str1;                 // lvalueからの代入
    ```

    * ステップ1。
      str0、str1がそれぞれ初期化される
      ("hehe"を保持するバッファが生成され、それをstr1オブジェクトが所有する)。

    * ステップ2。
      st1が所有している文字列バッファと等価のバッファが作られ
      (文字列バッファ用のメモリをnewし、文字列を代入)、
      str0がそれを所有する。従って、"hehe"を保持するバッファが2つできる。
      この代入をcopy代入と呼ぶ。

<!-- pu:deep/plant_uml/rvalue_from_lvalue.pu--><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAiYAAAGWCAIAAADDjt/5AAArhElEQVR4Xu3dD3BU5b3/8U0qBAiE0JRWAYsp42iditYrOmNHB+utWK7VqR31FnrxalUYL1DRjDrKgOWfQLlXBPnreC/WVByl6tUxRHqVqql/ImIkQC0RdDU/I2LCajAQSOLva44+Z3k2Ydmw55x9nuf9mh3mOWe/SXz2fL/57NEQY18CABCKmH4CAIBgEDkAgJD4kdMBAEAAiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASIgcAEBIiBwAQEiIHABASMyOnF27do0aNequu+7SnwAA5J4sR86BAweeSLJu3bpXX31VPVtfXz8zxY4dO5I+wZF8+umn27dv37p1a21t7ZYtW2pqauTDL7nkkqFDh3oF8tUrKys///zzwz8OAJATshw5kgoDBw4sLi4ePHjwsGHDBgwYMGTIkPb2du9ZSZd/SbFp06bDP8dXJDz0Ux0d8+bNi6UoKiqqqKiQZydOnFhSUiJnJJb0jwQA5IAsR06yQ4cOjRgxYs6cOerM9m589tlnqua1116rrq6WuJL0ksOrr7564cKF3lNNTU07d+6Mx+Nyt9TQ0LBnz57zzz9fksZ7dv369XL3Q+QAQM4KMHJWrVpVWFjoJYc4ePCgfofyjUceecSrqaur69Wr1xNPPHHSSSeVlZXJmeHDh8+fP199zmTNzc39+vUrLy9XZ1paWmJEDgDkqqAi56233pI88GJD+egbs2fPPv7449WhRIWqmTp16plnnvnggw9OmDBB7n7y8vKefvrppM/hu//++/v37598h0TkAEAuCyRyNm3aNGTIkNLSUrnLWb9+vf50R8fNN9989tln62c7vffee8uWLTt06JCs77nnnt69ezc2NupFHR1bt24tLi6eOXNm8kkiBwByWZYjp62tbfXq1XJ/c8kll3zxxRdyN9OrVy8tdTZv3lxSUiJPJZ/U7N+/X/ImPz//7rvv1p7at2/fvffeO3DgwLFjxx48eDD5KSIHAHJZNiOnqanprLPOOu6442bMmOHdpoiysjK516muru7oTIvLL79cguSyyy6TQDrsg5PceuutgwcP7tu379y5c5PPS8Bcc801EjYDBgyQxNLypoPIAYDcls3IEUuXLt22bVvymfb2dkmgjz76yDuUe6ANGzYkF6QqLy9fvHjx7t279Sc6OhYtWiSfIZFI6E8AAHJeliMHAIDuEDkAgJAQOQCAkBA5AICQEDkAgJAQOQCAkBA5AICQEDkAgJAQOQCAkFgVOd7/og22kuurX3Kr0c92c62fPVZFjlxFtQvYR65vIpFobm5uaWlpbW1ta2vTO8Au9LPdXOtnj799tdJLzMGI2k2ubzweb2hoaGxslEGVKdU7wC70s91c62ePv3210kvMwYjaTa5vbW1tXV1dfX29TGny/9nPSvSz3VzrZ4+/fbXSS8zBiNpNrm9VVVVNTY1Mqbw3lDeGegfYhX62m2v97PG3r1Z6iTkYUbvJ9a2oqJAplfeG8Xjc+v+HBf1sN9f62eNvX630EnMwonaT67t27drKysrq6mp5Y9jl/6HcJvSz3VzrZ4+/fbXSS8zBiNrNtRGln+3mWj97/O2rlV5iDkbUbq6NKP1sN9f62eNvX630EnMwonZzbUTpZ7u51s8ef/tqpZeYgxG1m2sjSj/bzbV+9vjbVyu9xByMqN1cG1H62W6u9bPH375a6SXmYETt5tqI0s92c62fPf721UovMQcjajfXRpR+tptr/ezxt69Weok5GFG7uTai9LPdXOtnj799tdJLzMGI2s21EaWf7eZaP3v87auVXmIORtRuro0o/Ww31/rZ429frfQSczCidnNtROlnu7nWzx5/+2qll5iDEbWbayNKP9vNtX72+NtXK73EHIyo3VwbUfrZbq71s8ffvlrpJeZgRO3m2ojSz3ZzrZ89/vbVSi8xByNqN9dGlH62m2v97PG3r1Z6iTkYUbu5NqL0s91c62ePv3210kvM4dqIfvzxx1u3btXPpti2bVt5efkzzzyzf/9+/TmjuDai9HOXmpqaHnroIelq/QnTuNbPHn/7aqWXmMO1ES0sLFyxYoV+Nom8JpMmTYp9o7S0VDpbLzKHayNKP2vkbdPYsWP79Okjr8yRK43gWj97/O2rlV5iDutHdOPGjWvWrNm+fbus5cZF9jtu3DiZvU8++cQrkPWuXbveeOONpUuXyuEDDzwgNQsWLJA3hq+88srw4cMvuOCC5E9oFtdGlH7W+llubsaPHz979mwix1z+9tVKLzGH3SM6ZcqUznuVWF5e3sKFCyU/vEMhM+nVyHratGlScOmll8rheeedN3r0aPUZHn/8cSl455131BmzuDai9LPWzx659DEix1j+9tVKLzGH3SPav3//yZMn7927d+XKlXv27Pmys2W1wZMzJ5xwwksvvdTa2iqHRUVFd999t3p29+7dUvDkk0/6H2AU10aUftb62UPkGM3fvlrpJeawe0TlfuXEE0985JFH2travDOpgydnJk6cqA4LCgoWL16sDg8cOCAFa9asUWfM4tqI0s9aP3uIHKP521crvcQcdo9oU1PT1KlT+/bte+6553o/e5Y6eHJm+fLl6rC0tPSWW25Rhzt27JCCDRs2qDNmcW1E6Wetnz1EjtH87auVXmIOu0fU+3cLW7ZskW0+9thjX3YzoslnrrvuuqFDh+7bt887nD59er9+/RKJhCowi2sjSj+nnvmSyDGcv3210kvMYfGIvvzyy4MHDy4rK5s8ebJs87nnnvuy84dKx4wZM2vWrEOHDnll2ijW1tb26dPnjDPOmD9//qRJk/Lz8+UzqGeN49qI0s9dRguRYzR/+2qll5jD4hGVW5Mbb7xx0KBBAwcOnDZtmndyxowZctdyyimnqL8WlzqKGzduHDVqVEFBwZAhQ+QuRw2ziVwbUfo5tZ+/JHIM529frfQSc1g8ovjSvRGln+3mWj97/O2rlV5iDkbUbq6NKP1sN9f62eNvX630EnMwonZzbUTpZ7u51s8ef/tqpZeYgxG1m2sjSj/bzbV+9vjbVyu9xByMqN1cG1H62W6u9bPH375a6SXmYETt5tqI0s92c62fPf721UovMQcjajfXRpR+tptr/ezxt69Weok5GFG7uTai9LPdXOtnj799tdJLzMGI2s21EaWf7eZaP3v87auVXmIORtRuro0o/Ww31/rZ429frfQSczCidnNtROlnu7nWzx5/+2qll5iDEbWbayNKP9vNtX72+NtXK73EHIyo3VwbUfrZbq71s8ffvlrpJeZgRO3m2ojSz3ZzrZ89/vbVSi8xByNqN9dGlH62m2v97PG3r1Z6iTkYUbu5NqL0s91c62ePv3210kvMwYjazbURpZ/t5lo/e/ztq5VeYg5G1G6ujSj9bDfX+tnjb1+t9BJzMKJ2c21E6We7udbPHn/7aqWXmIMRtZtrI0o/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" /></p>


2. 下記コードにより「rvalueからの代入」を説明する。

    ```.cpp
    //  example/term_explanation/rvalue_lvalue_ut.cpp 46

    auto str0 = std::string{};        // str0はlvalue
    str0      = std::string{"hehe"};  // rvalueからの代入
    ```

    * ステップ1。str0、「std::string()により作られたテンポラリオブジェクト」がそれぞれ初期化される
      ("hehe"を保持するバッファが生成され、それをテンポラリオブジェクトが所有する)。

    * ステップ2。
      "hehe"を保持する文字列バッファをもう1つ作る代わりに、
      テンポラリオブジェクトが所有している文字列バッファをstr0の所有にする。
      この代入をmove代入と呼ぶ。

    * ステップ3。
      テンポラリオブジェクトが解体されるが、
      文字列バッファはstr0の所有であるためdeleteする必要がなく、実際には何もしない。
      move代入によって、文字列バッファの生成と破棄の回数がそれぞれ1回少なくなったため、
      実行速度は向上する(通常、new/deleteの処理コストは高い)。

<!-- pu:deep/plant_uml/rvalue_from_rvalue.pu--><p><img src="data:image/png;base64,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" /></p>

3. 下記コードにより「std::move(lvalue)からの代入」を説明する。

    ```.cpp
    //  example/term_explanation/rvalue_lvalue_ut.cpp 56

    auto str0 = std::string{};        // str0はlvalue
    auto str1 = std::string{"hehe"};  // str1もlvalue
    str0      = std::move(str1);      // str1はこれ以降使われないとする
    ```

    * ステップ1。「lvalueからの代入」のステップ1と同じである。

    * ステップ2。
      std::move()の効果により(実際にはrvalueリファレンスへのキャストが行われるだけなので、
      実行時速度に影響はない)、"hehe"を保持する文字列バッファをもう1つ作る代わりに、
      str1が所有している文字列バッファをstr0の所有にする。
      この代入もmove代入と呼ぶ。
      この動作は「rvalueからの代入」と同じであり、同様に速度が向上するが、その副作用として、
      str1.size() == 0となる。

<!-- pu:deep/plant_uml/rvalue_from_move.pu--><p><img src="data:image/png;base64,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jx594MAB53x0lnQVM7FlgwYNcj5Ur169nnzySTk5ZMgQ9fElZpyykpKStLS08ePHq+cCgELk2Ene/fv27fviiy/u3btXbnTksLKy0jl/YpFz2mmnvfnmm7t3777pppvy8vK+/PLLTssGDBiwdu3a/fv3q5MAoBA5dpJ3/1mzZjlzub+Rw6VLlzrnTyxy5s2b58x37Nghh6tXr+60rLi4WB0Cmqy8rJBd8vPz9UXimIgcO4ViwsA57Or8MebaYXNzsxzKnVOnZYsWLVKHgEZ2yNJtS20asqJIJCJN0dLS0tra2tbWpq8ZRyNy7BQbBs5hZmZmWVmZc7KioqKrmIl9+rRp05z5qlWr5HD9+vWdlkUfAhorIyccDjc0NDQ2NkrwqO/TQVeIHDt1FQaXX355//79JXVKS0uzso78KUenMRP79LS0tEmTJt17773y9AsuuMD5h6LyEcaMGXPPPfd0+r0JgMbKyKmtra2rq6uvr5fUkXsdfc04GpFjp9jMcA63b99+xRVXZGdnFxUVzZ07Nycnp9OYiX26RIs8RZ44bty4HTt2OOenT58ut03Dhw93vtOayMGxWRk5VVVVNTU1kjpyryM3OvqacTQiB/GRJUgIKyOnoqJCUkfudcLhcCQS0deMoxE5iI/IQUJYGTkrVqyorKysrq6WG53GxkZ9zTgakYP4iouL165dq58FuonIAZEDwCPdipwHah+Y/frs+evmy68Pb314TPGYO5+7M7asq9Gteu1zxRZ0NYic7iJyAHikW5EzefFkqR/505Hy6183/lV+nTh7YmxZV6Nb9drnii3oahA53UXkAPBItyKn5IkSqf/xtT9OS09b8vGSbkXI0m5Gjva5Ygu6GkROdxE5wJGfgf3OO++Ul5c/9thjn3322ddff/300087P6FO1ezfv//VV1+V8/X19erksmXLKioq1KE8/Z///KdM9u3bt3r1ailuaGhQj6JbkfPHf/xR6n955y8zczOdN3eJkLtfvvuGP99wy99uWfzR4ujiRf+zaOrfp970wE1/+tefnDPdqtc+1/EPIqe7iBzgyFthjx49Qh369+8/YsQIZ65+AveuXbvOP/9852RWVtZzzz3nPPHKK6/Mz893/s351q1b5dG//OUvO3fuVB8hJydn3bp10Z8ryELdiZz56+affdHZJeUlF1x5gfPmXnBmgfOqiqEj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" /></p>


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
    //  example/term_explanation/rvalue_lvalue_ut.cpp 65

    #define IS_LVALUE(EXPR_) std::is_lvalue_reference_v<decltype((EXPR_))>
    #define IS_XVALUE(EXPR_) std::is_rvalue_reference_v<decltype((EXPR_))>
    #define IS_PRVALUE(EXPR_) !std::is_reference_v<decltype((EXPR_))>
    #define IS_RVALUE(EXPR_) (IS_PRVALUE(EXPR_) || IS_XVALUE(EXPR_))

    TEST(Expression, rvalue)
    {
        auto str = std::string{};

        static_assert(IS_LVALUE(str), "EXPR_ must be lvalue");
        static_assert(!IS_RVALUE(str), "EXPR_ must NOT be rvalue");

        static_assert(IS_XVALUE(std::move(str)), "EXPR_ must be xvalue");
        static_assert(!IS_PRVALUE(std::move(str)), "EXPR_ must NOT be prvalue");

        static_assert(IS_PRVALUE(std::string{}), "EXPR_ must be prvalue");
        static_assert(IS_RVALUE(std::string{}), "EXPR_ must be rvalue");
        static_assert(!IS_LVALUE(std::string{}), "EXPR_ must NOT be lvalue");
    }
```

### lvalue <a id="SS_19_14_2"></a>
「[expression](term_explanation.md#SS_19_14_1)」を参照せよ。

### rvalue <a id="SS_19_14_3"></a>
「[expression](term_explanation.md#SS_19_14_1)」を参照せよ。

#### xvalue <a id="SS_19_14_3_1"></a>
「[expression](term_explanation.md#SS_19_14_1)」を参照せよ。

#### prvalue <a id="SS_19_14_3_2"></a>
「[expression](term_explanation.md#SS_19_14_1)」を参照せよ。

### rvalue修飾 <a id="SS_19_14_4"></a>
下記GetString0()のような関数が返すオブジェクトの内部メンバに対するハンドルは、
オブジェクトのライフタイム終了後にもアクセスすることができるため、
そのハンドルを通じて、
ライフタイム終了後のオブジェクトのメンバオブジェクトにもアクセスできてしまう。

ライフタイム終了後のオブジェクトにアクセスすることは未定義動作であり、
特にそのオブジェクトがrvalueであった場合、さらにその危険性は高まる。

こういったコードに対処するためのシンタックスが、lvalue修飾、rvalue修飾である。

下記GetString1()、GetString3()、GetString4()のようにメンバ関数をlvalue修飾やrvalue修飾することで、
rvalueの内部ハンドルを返さないようにすることが可能となり、上記の危険性を緩和することができる。

```cpp
    //  example/term_explanation/rvalue_lvalue_ut.cpp 91

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
    //  example/term_explanation/rvalue_lvalue_ut.cpp 132

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

### lvalue修飾 <a id="SS_19_14_5"></a>
[rvalue修飾](term_explanation.md#SS_19_14_4)を参照せよ。


### リファレンス修飾 <a id="SS_19_14_6"></a>
[rvalue修飾](term_explanation.md#SS_19_14_4)と[lvalue修飾](term_explanation.md#SS_19_14_5)とを併せて、リファレンス修飾と呼ぶ。


## リファレンス <a id="SS_19_15"></a>
ここでは、C++11から導入された

* [ユニバーサルリファレンス](term_explanation.md#SS_19_15_1)
* [リファレンスcollapsing](term_explanation.md#SS_19_15_4)

について解説する。

### ユニバーサルリファレンス <a id="SS_19_15_1"></a>
関数テンプレートの型パラメータや型推論autoに&&をつけて宣言された変数を、
ユニバーサルリファレンスと呼ぶ(C++17から「forwardingリファレンス」という正式名称が与えられた)。
ユニバーサルリファレンスは一見rvalueリファレンスのように見えるが、
下記に示す通り、lvalueにもrvalueにもバインドできる。

```cpp
    //  example/term_explanation/universal_ref_ut.cpp 8

    template <typename T>
    void f(T&& t) noexcept  // tはユニバーサルリファレンス
    {
        ...
    }

    template <typename T>
    void g(std::vector<T>&& t) noexcept  // tはrvalueリファレンス
    {
        ...
    }
```
```cpp
    //  example/term_explanation/universal_ref_ut.cpp 29

    auto       vec  = std::vector<std::string>{"lvalue"};   // vecはlvalue
    auto const cvec = std::vector<std::string>{"clvalue"};  // cvecはconstなlvalue

    f(vec);                                 // 引数はlvalue
    f(cvec);                                // 引数はconstなlvalue
    f(std::vector<std::string>{"rvalue"});  // 引数はrvalue

    // g(vec);  // 引数がlvalueなのでコンパイルエラー
    // g(cvec); // 引数がconst lvalueなのでコンパイルエラー
    g(std::vector<std::string>{"rvalue"});  // 引数はrvalue
```

下記のコードは[ジェネリックラムダ](term_explanation.md#SS_19_11_4)の引数をユニバーサルリファレンスにした例である。

```cpp
    //  example/term_explanation/universal_ref_ut.cpp 47

    // sはユニバーサルリファレンス
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

通常、ユニバーサルリファレンスはstd::forwardと組み合わせて使用される。


### forwardingリファレンス <a id="SS_19_15_2"></a>
「[ユニバーサルリファレンス](term_explanation.md#SS_19_15_1)」を参照せよ。

### perfect forwarding <a id="SS_19_15_3"></a>
perfect forwarding とは、引数の[rvalue](term_explanation.md#SS_19_14_3)性や
[lvalue](term_explanation.md#SS_19_14_2)性を損失することなく、
その引数を別の関数に転送する技術のことを指す。
通常は、[ユニバーサルリファレンス](term_explanation.md#SS_19_15_1)である関数の仮引数をstd::forwardを用いて、
他の関数に渡すことで実現される。

### リファレンスcollapsing <a id="SS_19_15_4"></a>
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
    //  example/term_explanation/ref_collapsing_ut.cpp 7

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
    //  example/term_explanation/ref_collapsing_ut.cpp 26

    template <typename T>
    struct Ref {
        T&  t;
        T&& u;
    };
```

下記のコードにより、テンプレートパラメータに対するこの変換則を確かめることができる。

```cpp
    //  example/term_explanation/ref_collapsing_ut.cpp 38

    static_assert(std::is_same_v<int&, decltype(Ref<int>::t)>);    // lvalueリファレンス
    static_assert(std::is_same_v<int&&, decltype(Ref<int>::u)>);   // rvalueリファレンス

    static_assert(std::is_same_v<int&, decltype(Ref<int&>::t)>);   // lvalueリファレンス
    static_assert(std::is_same_v<int&, decltype(Ref<int&>::u)>);   // lvalueリファレンス

    static_assert(std::is_same_v<int&, decltype(Ref<int&&>::t)>);  // lvalueリファレンス
    static_assert(std::is_same_v<int&&, decltype(Ref<int&&>::u)>); // rvalueリファレンス
```

この機能がないC++03では、

```cpp
    //  example/term_explanation/ref_collapsing_ut.cpp 52

    template <typename T>
    struct AddRef {
        using type = T&;
    };
```

ようなクラステンプレートに下記コードのようにリファレンス型を渡すとコンパイルエラーとなる。

```cpp
    //  example/term_explanation/ref_collapsing_ut.cpp 69

    static_assert(std::is_same_v<int&, AddRef<int&>::type>);
```

この問題を回避するためには下記のようなテンプレートの特殊化が必要になる。

```cpp
    //  example/term_explanation/ref_collapsing_ut.cpp 59

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

### danglingリファレンス <a id="SS_19_15_5"></a>
Dangling リファレンスとは、破棄後のオブジェクトを指しているリファレンスを指す。
このようなリファレンスにアクセスすると、[未定義動作](term_explanation.md#SS_19_18_7)に繋がるに繋がる。

```cpp
    //  example/term_explanation/dangling_ut.cpp 9

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

    //  example/term_explanation/dangling_ut.cpp 34

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

### danglingポインタ <a id="SS_19_15_6"></a>
danglingポインタとは、[danglingリファレンス](term_explanation.md#SS_19_15_5)と同じような状態になったポインタを指す。

## エクセプション安全性の保証 <a id="SS_19_16"></a>
関数のエクセプション発生時の安全性の保証には以下の3つのレベルが規定されている。

* [no-fail保証](term_explanation.md#SS_19_16_1)
* [強い安全性の保証](term_explanation.md#SS_19_16_2)
* [基本的な安全性の保証](term_explanation.md#SS_19_16_3)

### no-fail保証 <a id="SS_19_16_1"></a>
「no-fail保証」を満たす関数はエクセプションをthrowしない。
no-failを保証する関数は、
[noexcept](term_explanation.md#SS_19_16_4)を使用してエクセプションを発生させないことを明示できる。

標準テンプレートクラスのパラメータとして使用するクラスのメンバ関数には、
正確にnoexceptの宣言をしないと、
テンプレートクラスのメンバ関数によってはパフォーマンスを起こしてしまう可能性がある。

### 強い安全性の保証 <a id="SS_19_16_2"></a>
「強い保証」を満たす関数は、この関数がエクセプションによりスコープから外れた場合でも、
この関数が呼ばれなかった状態と同じ(プログラムカウンタ以外の状態は同じ)であることを保証する。
従って、この関数呼び出しは成功したか、完全な無効だったかのどちらかになる。

### 基本的な安全性の保証 <a id="SS_19_16_3"></a>
「基本的な安全性の保証」を満たす関数は、この関数がエクセプションによりスコープから外れた場合でも、
メモリ等のリソースリークは起こさず、
オブジェクトは(変更されたかもしれないが)引き続き使えることを保証する。

### noexcept <a id="SS_19_16_4"></a>
C++11で導入されたnoexceptキーワードには、以下の2つの意味がある。

* C++03までのthrowキーワードによる例外仕様の代替。
  関数がどの例外を送出する可能性があるかを列挙するのではなく、
  例外を送出する可能性があるかないかのみを指定する。

* sizeofと同じような形式で使用されるのような演算子としてのnoexceptは、
  noexcept(expression)の形式使用され、
  expressionがエクセプションを送出しないと宣言されている場合(noexceptと宣言された関数の呼び出し)、
  noexcept(expression)は静的にtrueとなる。

以下に上記のコード例を示す。

```cpp
    //  example/term_explanation/noexcept_ut.cpp 11

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
    //  example/term_explanation/noexcept_ut.cpp 37

    static_assert(noexcept(f_noexcept()));  // エクセプションを発生させる可能性の確認
    static_assert(!noexcept(f_except()));   // エクセプションを発生させない可能性の確認
    static_assert(!noexcept(f_except2()));  // エクセプションを発生させない可能性の確認

    ASSERT_EQ(f_noexcept(), "No exceptions here!");  // 動作確認
    ASSERT_THROW(f_except(), std::runtime_error);    // エクセプションの発生確認
    ASSERT_THROW(f_except2(), std::runtime_error);   // エクセプションの発生確認
```

演算子としてのnoexceptはテンプレートで頻繁に使用されるため、以下にそのような例を示す。

```cpp
    //  example/term_explanation/noexcept_ut.cpp 50

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
    //  example/term_explanation/noexcept_ut.cpp 67

    auto i = int{};
    auto p = PossiblyThrow{};

    static_assert(!std::is_nothrow_constructible_v<PossiblyThrow>);
    static_assert(std::is_nothrow_constructible_v<decltype(i)>);
    static_assert(noexcept(t_f(i)));
    static_assert(!noexcept(t_f(p)));
```

### exception-unfriendly <a id="SS_19_16_5"></a>
以下のような関数  

* 初期化に関連する関数やコンストラクタ
    * 静的または thread_local な変数を初期化する関数やコンストラクタ
* 特殊メンバ関数
    * すべてのデストラクタ
    * すべての例外オブジェクトのコピーコンストラクタ
    * すべてのムーブコンストラクタ
    * すべてのムーブ代入演算子
* 特定の名前を持つ関数
    * "swap" という名前のすべての関数
* C言語との互換性を持つ関数
    * Cとのリンケージを持つすべての関数

の呼び出しでエクセプションがthrowされると、[未定義動作](term_explanation.md#SS_19_18_7)や[未規定動作](term_explanation.md#SS_19_18_8)が発生するため、
exception-unfriendly(エクセプションに不向き)であるとされる。
従って上記の関数は暗黙的または明示的に`noexcept`であることが求められる。

## シンタックス、セマンティクス <a id="SS_19_17"></a>
直訳すれば、シンタックスとは構文論のことであり、セマンティクスとは意味論のことである。
この二つの概念の違いをはっきりと際立たせる有名な文を例示する。

```
    Colorless green ideas sleep furiously(直訳:無色の緑の考えが猛烈に眠る)
```

この文は構文的には正しい(シンタックスは問題ない)が、
意味不明である(セマンティクスは誤り)。

C++プログラミングにおいては、コンパイルできることがシンタックス的な正しさであり、例えば

* クラスや関数がその名前から想起できる責務を持っている
    * 「[単一責任の原則(SRP)](solid.md#SS_8_1)」を満たしている
    * [Accessor](design_pattern.md#SS_9_4)を実装する関数の名前は、GetXxxやSetXxxになっている
    * コンテナクラスのメンバ関数beginやendは、
      そのクラスが保持する値集合の先頭や最後尾の次を指すイテレータを返す
    * 等

* 「[等価性のセマンティクス](term_explanation.md#SS_19_17_1)」を守ってる
* 「[copyセマンティクス](term_explanation.md#SS_19_17_2)」を守ってる
* 「[moveセマンティクス](term_explanation.md#SS_19_17_3)」を守っている

等がセマンティクス的な正しさである。

セマンティクス的に正しいソースコードは読みやすく、保守性、拡張性に優れている。

### 等価性のセマンティクス <a id="SS_19_17_1"></a>
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
    //  example/term_explanation/semantics_ut.cpp 13

    auto  a = 0;
    auto& b = a;

    ASSERT_TRUE(a == b);
    ASSERT_TRUE(&a == &b);  // aとbは同一
```

しかし、下記のコード内のa、bは同じ値を持つが、
アドレスが異なるため同一のオブジェクトではないにもかかわらず、組み込みの==の値はtrueとなる。

```cpp
    //  example/term_explanation/semantics_ut.cpp 23

    auto a = 0;
    auto b = 0;

    ASSERT_TRUE(a == b);
    ASSERT_FALSE(&a == &b);  // aとbは同一ではない
```

このような場合、aとbは等価であるという。同一ならば等価であるが、等価であっても同一とは限らない。

ポインタや配列をオペランドとする場合を除き、C++における組み込みの==は、
数学の等号とは違い、等価を表していると考えられるが、
上記した3つの律を守っている。従ってオーバーロードoperator==も同じ性質を守る必要がある。

組み込みの==やオーバーロード[==演算子](term_explanation.md#SS_19_6_7)のこのような性質をここでは「等価性のセマンティクス」と呼ぶ。

クラスAを下記のように定義し、

```cpp
    //  example/term_explanation/semantics_ut.cpp 34

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
    //  example/term_explanation/semantics_ut.cpp 51

    inline bool operator==(A const& lhs, A const& rhs) noexcept
    {
        return std::tuple(lhs.GetNum(), lhs.GetName()) == std::tuple(rhs.GetNum(), rhs.GetName());
    }
```

単体テストは下記のように書けるだろう。

```cpp
    //  example/term_explanation/semantics_ut.cpp 62

    auto a0 = A{0, "a"};
    auto a1 = A{0, "a"};

    ASSERT_TRUE(a0 == a1);
```

これは、一応パスするが(処理系定義の動作を前提とするため、必ず動作する保証はない)、
下記のようにすると、パスしなくなる。

```cpp
    //  example/term_explanation/semantics_ut.cpp 72

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
    //  example/term_explanation/semantics_ut.cpp 91

    inline bool operator==(A const& lhs, A const& rhs) noexcept
    {
        return std::tuple(lhs.GetNum(), std::string_view{lhs.GetName()})
               == std::tuple(rhs.GetNum(), std::string_view{rhs.GetName()});
    }
```

ポインタをメンバに持つクラスのoperator==については、上記したような処理が必要となる。

次に示す例は、基底クラスBaseとそのoperator==である。

```cpp
    //  example/term_explanation/semantics_ut.cpp 114

    class Base {
    public:
        explicit Base(int b) noexcept : b_{b} {}
        virtual ~Base() = default;
        int GetB() const noexcept { return b_; }

    private:
        int b_;
    };

    inline bool operator==(Base const& lhs, Base const& rhs) noexcept
    {
        return lhs.GetB() == rhs.GetB();
    }
```

次の単体テストが示す通り、これ自体には問題がないように見える。

```cpp
    //  example/term_explanation/semantics_ut.cpp 134

    auto b0 = Base{0};
    auto b1 = Base{0};
    auto b2 = Base{1};

    ASSERT_TRUE(b0 == b0);
    ASSERT_TRUE(b0 == b1);
    ASSERT_FALSE(b0 == b2);
```

しかし、Baseから派生したクラスDerivedを

```cpp
    //  example/term_explanation/semantics_ut.cpp 146

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
    //  example/term_explanation/semantics_ut.cpp 160

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
    //  example/term_explanation/semantics_ut.cpp 177

    bool operator==(Derived const& lhs, Derived const& rhs) noexcept
    {
        return std::tuple(lhs.GetB(), lhs.GetD()) == std::tuple(rhs.GetB(), rhs.GetD());
    }
```

と定義しても、下記に示す通り部分的な効果しかない。

```cpp
    //  example/term_explanation/semantics_ut.cpp 187

    auto d0 = Derived{0};
    auto d1 = Derived{1};

    ASSERT_FALSE(d0 == d1);  // OK operator==(Derived const&, Derived const&)の効果で正しい判定

    Base& d0_b_ref = d0;

    ASSERT_TRUE(d0_b_ref == d1);  // NG d0_b_refの実態はd0なのでd1と等価でない
```

この問題は、「[RTTI](term_explanation.md#SS_19_3_11)」使った下記のようなコードで対処できる。

```cpp
    //  example/term_explanation/semantics_ut.cpp 203

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
[オープン・クローズドの原則(OCP)](solid.md#SS_8_2)にも対応した柔軟な構造を実現している。

```cpp
    //  example/term_explanation/semantics_ut.cpp 270

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
    //  example/term_explanation/semantics_ut.cpp 320

    auto abc = std::string{"abc"};

    ASSERT_TRUE("abc" == abc);
    ASSERT_TRUE(abc == "abc");
```

これは、文字列リテラルを第1引数に取るstd::stringのコンストラクタが非explicitであることによって、
文字列リテラルからstd::stringへの[暗黙の型変換](term_explanation.md#SS_19_13_1)が起こるために成立する。

以上で見てきたように、等価性のセマンティクスを守ったoperator==の実装には多くの観点が必要になる。

### copyセマンティクス <a id="SS_19_17_2"></a>
copyセマンティクスとは以下を満たすようなセマンティクスである。

* a = bが行われた後に、aとbが等価である。
* a = bが行われた前後でbの値が変わっていない。

従って、これらのオブジェクトに対して[等価性のセマンティクス](term_explanation.md#SS_19_17_1)
を満たすoperator==が定義されている場合、
以下を満たすようなセマンティクスであると言い換えることができる。

* a = bが行われた後に、a == bがtrueになる。
* b == b_preがtrueの時に、a = bが行われた後でもb == b_preがtrueとなる。

下記に示す通り、std::stringはcopyセマンティクスを満たしている。

```cpp
    //  example/term_explanation/semantics_ut.cpp 334

    auto c_str = "string";
    auto str   = std::string{};

    str = c_str;
    ASSERT_TRUE(c_str == str);      // = 後には == が成立している
    ASSERT_STREQ("string", c_str);  // c_strの値は変わっていない
```

一方で、std::auto_ptrはcopyセマンティクスを満たしていない。

```cpp
    //  example/term_explanation/semantics_ut.cpp 347

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
「[等価性のセマンティクス](term_explanation.md#SS_19_17_1)」で示した最後の例も、copyセマンティクスを満たしていない。

```cpp
    //  example/term_explanation/semantics_ut.cpp 367

    auto b = Base{1};
    auto d = Derived{1};

    b = d;  // スライシングが起こる

    ASSERT_FALSE(b == d);  // copyセマンティクスを満たしていない
```

原因は、copy代入で[スライシング](term_explanation.md#SS_19_5_9_3)が起こるためである。


### moveセマンティクス <a id="SS_19_17_3"></a>
moveセマンティクスとは以下を満たすようなセマンティクスである(operator==が定義されていると前提)。

* copy代入の実行コスト >= move代入の実行コスト
* a == bがtrueの時に、c = std::move(a)が行われた場合、
    * b == cがtrueになる。
    * a == cはtrueにならなくても良い(aはmove代入により破壊されるかもしれない)。

  必須ではないが、「aがポインタ等のリソースを保有している場合、move代入後には、
  そのリソースはcに移動している」ことが一般的である(「[rvalue](term_explanation.md#SS_19_14_3)」参照)。

* [no-fail保証](term_explanation.md#SS_19_16_1)をする(noexceptと宣言し、エクセプションをthrowしない)。

moveセマンティクスはcopy代入後に使用されなくなるオブジェクト(主にrvalue)
からのcopy代入の実行コストを下げるために導入されたため、
下記のようなコードは推奨されない。

```cpp
    //  example/term_explanation/semantics_ut.cpp 382

    class NotRecommended {
    public:
        NotRecommended(char const* name) : name_{name} {}
        std::string const& Name() const noexcept { return name_; }

        NotRecommended& operator=(NotRecommended&& rhs)  // move代入、非no-fail保証
        {
            name_ = rhs.name_;  // rhs.name_からname_へのcopy代入。パフォーマンス問題になるかも。
            return *this;
        }

    private:
        std::string name_;
    };

    bool operator==(NotRecommended const& lhs, NotRecommended const& rhs) noexcept
    {
        return lhs.Name() == rhs.Name();
    }

    TEST(Semantics, move1)
    {
        auto a = NotRecommended{"a"};
        auto b = NotRecommended{"a"};

        ASSERT_EQ("a", a.Name());
        ASSERT_TRUE(a == b);

        auto c = NotRecommended{"c"};
        ASSERT_EQ("c", c.Name());

        c = std::move(a);
        ASSERT_TRUE(b == c);  // 一応、moveセマンティクスは守っているが・・・
    }

```

下記のコードのようにメンバの代入もできる限りmove代入を使うことで、
パフォーマンスの良い代入ができる。

```cpp
    //  example/term_explanation/semantics_ut.cpp 420

    class Recommended {
    public:
        Recommended(char const* name) : name_{name} {}
        std::string const& Name() const noexcept { return name_; }

        Recommended& operator=(Recommended&& rhs) noexcept  // move代入、no-fail保証
        {
            name_ = std::move(rhs.name_);  // rhs.name_からname_へのmove代入
            return *this;
        }

    private:
        std::string name_;
    };

    bool operator==(Recommended const& lhs, Recommended const& rhs) noexcept
    {
        return lhs.Name() == rhs.Name();
    }

    TEST(Semantics, move2)
    {
        auto a = Recommended{"a"};
        auto b = Recommended{"a"};

        ASSERT_EQ("a", a.Name());
        ASSERT_TRUE(a == b);

        auto c = Recommended{"c"};
        ASSERT_EQ("c", c.Name());

        c = std::move(a);     // これ以降aは使ってはならない
        ASSERT_TRUE(b == c);  // moveセマンティクスを正しく守っている
    }

```

### MoveAssignable要件 <a id="SS_19_17_4"></a>
MoveAssignable要件は、C++において型がムーブ代入をサポートするために満たすべき条件を指す。
ムーブ代入はリソースを効率的に転送する操作であり、以下の条件を満たす必要がある。

1. リソースの移動  
   ムーブ代入では、リソース(動的メモリ等)が代入元から代入先へ効率的に転送される。

2. 有効だが未定義の状態  
   ムーブ代入後、代入元のオブジェクトは有効ではあるが未定義の状態となる。
   未定義の状態とは、破棄や再代入が可能である状態を指し、それ以外の操作は保証されない。

3. 自己代入の安全性  
   同一のオブジェクトをムーブ代入する場合でも、未定義動作やリソースリークを引き起こしてはならない。

4. 効率性  
   ムーブ代入は通常、コピー代入よりも効率的であることが求められる。
   これは、リソースの複製を避けることで達成される(「[moveセマンティクス](term_explanation.md#SS_19_17_3)」参照)。

5. デフォルト実装  
   ムーブ代入演算子が明示的に定義されていない場合でも、
   クラスが一定の条件(例: ムーブ不可能なメンバが存在しないこと)を満たしていれば、
   コンパイラがデフォルトの実装(「[特殊メンバ関数](term_explanation.md#SS_19_3_1)」参照)を生成する。

### CopyAssignable要件 <a id="SS_19_17_5"></a>
CopyAssignable要件は、C++において型がコピー代入をサポートするために満たすべき条件を指す。

1. 動作が定義されていること  
   代入操作は未定義動作を引き起こしてはならない。自己代入（同じオブジェクトを代入する場合）においても正しく動作し、リソースリークを引き起こさないことが求められる。

2. 値の保持  
   代入後、代入先のオブジェクトの値は代入元のオブジェクトの値と一致していなければならない。

3. 正しいセマンティクス  
   コピー代入によって代入元のオブジェクトが変更されてはならない(「[copyセマンティクス](term_explanation.md#SS_19_17_2)」参照)。
   代入先のオブジェクトが保持していたリソース(例: メモリ)は適切に解放される必要がある。

4. デフォルト実装  
   コピー代入演算子が明示的に定義されていない場合でも、
   クラスが一定の条件(例: コピー不可能なメンバが存在しないこと)を満たしていれば、
   コンパイラがデフォルトの実装(「[特殊メンバ関数](term_explanation.md#SS_19_3_1)」参照)を生成する。

## C++その他 <a id="SS_19_18"></a>
### 型特性キーワード <a id="SS_19_18_1"></a>
アライメントとは、
データが効率的にアクセスされるために特定のメモリアドレス境界に配置される規則である。
C++03までの規約では、アライメントのコントロールは実装依存した#pragmaなどで行っていた。

[alignas](term_explanation.md#SS_19_18_1_2)、
[alignof](term_explanation.md#SS_19_18_1_1)によりコンパイラの標準的な方法でアライメントのコントロールできるようになった。

#### alignof <a id="SS_19_18_1_1"></a>
C++11で導入されたキーワードで、型のアライメント要求を取得するために使用する。

```cpp
    //  example/term_explanation/aliging_ut.cpp 12

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

#### alignas <a id="SS_19_18_1_2"></a>
C++11で導入されたキーワードで、メモリのアライメントを指定するために使用する。

```cpp
    //  example/term_explanation/aliging_ut.cpp 27

    ASSERT_EQ(alignof(long double), 16);  // アライメントが正しいか確認
    ASSERT_EQ(alignof(long long), 8);     // アライメントが正しいか確認
    ASSERT_EQ(alignof(void*), 8);         // アライメントが正しいか確認
    ASSERT_EQ(alignof(int), 4);           // アライメントが正しいか確認
```

#### addressof <a id="SS_19_18_1_3"></a>
addressofは、オブジェクトの「実際の」
アドレスを取得するために使用されるC++標準ライブラリのユーティリティ関数である。
通常、オブジェクトのアドレスを取得するには&演算子を使うが、
operator& がオーバーロードされている場合には、
&演算子ではオブジェクトのメモリ上の実際のアドレスを取得できない場合があり得る。
そのような場合にstd::addressofすることにより、
オーバーロードを無視して元のアドレスを確実に取得できる。

```cpp
    //  example/term_explanation/aliging_ut.cpp 38

    class X {
    public:
        explicit X(int v) : v_{v} {}

        X* operator&()
        {  // `operator&` をオーバーロードしてアドレス取得の挙動を変更
            return nullptr;  // 意図的に nullptr を返す
        }
        operator int() const noexcept { return v_; }

    private:
        int v_;
    };
```
```cpp
    //  example/term_explanation/aliging_ut.cpp 54

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

### 演算子のオペランドの評価順位 <a id="SS_19_18_2"></a>

C++17で、演算子のオペランドに対する評価順序が明確に規定された。
それに対し、C++14までは、演算子のオペランド部分式の評価順序は[未規定動作](term_explanation.md#SS_19_18_8)であった。
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
    //  example/term_explanation/etc_ut.cpp 22

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
    //  example/term_explanation/etc_ut.cpp 31

    int a      = 1;
    int b      = 2;
    int result = (a < b) ? func1() : func2();
```

なお、単項演算子のオペランドは1つであるため、優先順位の定義は不要である。

### 実引数/仮引数 <a id="SS_19_18_3"></a>
引数(もしくは実引数、argument)、仮引数(parameter)とは下記のように定義される。

```cpp
    //  example/term_explanation/argument.cpp 2

    int f0(int a, int& b) noexcept  // a, bは仮引数
    {
        ...
    }

    void f1() noexcept
    {
        ...

        f0(x, y);  // x, yは実引数
    }
```

### 単純代入 <a id="SS_19_18_4"></a>
代入は下記のように分類される。

* 単純代入(=)
* 複合代入(+=，++ 等)

### ill-formed <a id="SS_19_18_5"></a>
[標準規格と処理系](https://cpprefjp.github.io/implementation-compliance.html)に詳しい解説があるが、

* [well-formed](term_explanation.md#SS_19_18_6)(適格)とはプログラムが全ての構文規則・診断対象の意味規則・
  単一定義規則を満たすことである。
* ill-formed(不適格)とはプログラムが適格でないことである。

プログラムがwell-formedになった場合、そのプログラムはコンパイルできる。
プログラムがill-formedになった場合、通常はコンパイルエラーになるが、
対象がテンプレートの場合、事情は少々異なり、[SFINAE](term_explanation.md#SS_19_11_1)によりコンパイルできることもある。

### well-formed <a id="SS_19_18_6"></a>
「[ill-formed](term_explanation.md#SS_19_18_5)」を参照せよ。

### 未定義動作 <a id="SS_19_18_7"></a>
未定義動作(Undefined Behavior)とは、
C++標準が特定の操作や状況に対して一切の制約を設けないケースである。
未定義動作が発生すると、プログラムの実行結果が予測できなくなり、
何が起こるかはコンパイラや環境によって異なる。
未定義動作を含むコードは、クラッシュやセキュリティの問題を引き起こす可能性がある。

```cpp
    //  example/term_explanation/undefined_ut.cpp 14

    int a = 42;
    int b = 0;
    int c = a / b;  // 未定義動作 - ゼロ除算

    int arr[]{1, 2, 3};
    int x = arr[index];  // 未定義動作 - index>2の場合、配列範囲外アクセス

```

### 未規定動作 <a id="SS_19_18_8"></a>
未規定動作(Unspecified Behavior)とは、C++標準がある操作の動作を完全には決めておらず、
複数の許容可能な選択肢がある場合でのコードの動作を指す。
未規定動作は、実装ごとに異なる可能性があり、標準は少なくとも「何らかの合理的な結果」を保証する。
つまり、動作が特定の範囲で予測可能だが、正確な挙動が処理系の実装に依存することになる。

```cpp
    //  example/term_explanation/undefined_ut.cpp 35

    enum class MyEnum : int { Value1 = 1, Value2 = 256 };
    int value = static_cast<int8_t>(MyEnum::Value2);  // 未規定 - 256はint8_tとして表現できない

    auto a      = int{5};
    auto lambda = [](auto a0, auto a1) { return a0 / a1; };
    auto result = lambda(a++, a++);  // 未規定 - 引数評価の順序が決まっていない
```

### 未定義動作と未規定動作 <a id="SS_19_18_9"></a>
| 種類            |定義                                                               | 例                               | 結果                           |
|-----------------|-------------------------------------------------------------------|----------------------------------|--------------------------------|
|[未定義動作](term_explanation.md#SS_19_18_7)|C++標準が全く保証しない動作                                        | ゼロ除算、配列範囲外アクセス     | 予測不能(クラッシュなど)       |
|[未規定動作](term_explanation.md#SS_19_18_8)|C++標準が動作を定めていないが、いくつかの選択肢が許容されている動作| `int8_t` に収まらない値のキャスト| 実装依存(異なるが合理的な動作) |


### 被修飾型 <a id="SS_19_18_10"></a>
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

見た目が類似する[修飾付き関数呼び出し](term_explanation.md#SS_19_10_7)とは無関係である。

### one-definition rule <a id="SS_19_18_11"></a>
「[ODR](term_explanation.md#SS_19_18_12)」を参照せよ。

### ODR <a id="SS_19_18_12"></a>
ODRとは、One Definition Ruleの略語であり、下記のようなことを定めている。

* どの翻訳単位でも、テンプレート、型、関数、またはオブジェクトは、複数の定義を持つことができない。
* プログラム全体で、オブジェクトまたは非インライン関数は複数の定義を持つことはできない。
* 型、テンプレート、外部インライン関数等、いくつかのものは複数の翻訳単位で定義することができる。

より詳しい内容がが知りたい場合は、
[https://en.cppreference.com/w/cpp/language/definition](https://en.cppreference.com/w/cpp/language/definition)
が参考になる。

### RVO(Return Value Optimization) <a id="SS_19_18_13"></a>
関数の戻り値がオブジェクトである場合、
戻り値オブジェクトは、その関数の呼び出し元のオブジェクトにコピーされた後、すぐに破棄される。
この「オブジェクトをコピーして、その後すぐにそのオブジェクトを破棄する」動作は、
「関数の戻り値オブジェクトをそのままその関数の呼び出し元で使用する」ことで効率的になる。
RVOとはこのような最適化を指す。

なお、このような最適化は、
[C++17から規格化](https://cpprefjp.github.io/lang/cpp17/guaranteed_copy_elision.html)された。


### SSO(Small String Optimization) <a id="SS_19_18_14"></a>
一般にstd::stringで文字列を保持する場合、newしたメモリが使用される。
64ビット環境であれば、newしたメモリのアドレスを保持する領域は8バイトになる。
std::stringで保持する文字列が終端の'\0'も含め8バイト以下である場合、
アドレスを保持する領域をその文字列の格納に使用すれば、newする必要がない(当然deleteも不要)。
こうすることで、短い文字列を保持するstd::stringオブジェクトは効率的に動作できる。

SOOとはこのような最適化を指す。

### heap allocation elision <a id="SS_19_18_15"></a>
C++11までの仕様では、new式によるダイナミックメモリアロケーションはコードに書かれた通りに、
実行されなければならず、ひとまとめにしたり省略したりすることはできなかった。
つまり、ヒープ割り当てに対する最適化は認められなかった。
ダイナミックメモリアロケーションの最適化のため、この制限は緩和され、
new/deleteの呼び出しをまとめたり省略したりすることができるようになった。

```cpp
    //  example/term_explanation/heap_allocation_elision_ut.cpp 4

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


### Most Vexing Parse <a id="SS_19_18_16"></a>
Most Vexing Parse(最も困惑させる構文解析)とは、C++の文法に関連する問題で、
Scott Meyersが彼の著書"Effective STL"の中でこの現象に名前をつけたことに由来する。

この問題はC++の文法が関数の宣言と変数の定義とを曖昧に扱うことによって生じる。
特にオブジェクトの初期化の文脈で発生し、意図に反して、その行は関数宣言になってしまう。

```cpp
    //  example/term_explanation/most_vexing_parse_ut.cpp 6

    class Vexing {
    public:
        Vexing(int) {}
        Vexing() {}
    };

    //  example/term_explanation/most_vexing_parse_ut.cpp 21

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

[初期化子リストコンストラクタ](term_explanation.md#SS_19_5_3)の呼び出しでオブジェクトの初期化を行うことで、
このような問題を回避できる。


### トライグラフ <a id="SS_19_18_17"></a>
トライグラフとは、2つの疑問符とその後に続く1文字によって表される、下記の文字列である。

```
    ??=  ??/  ??'  ??(  ??)  ??!  ??<  ??>  ??-
```

## C++コンパイラ <a id="SS_19_19"></a>
本ドキュメントで使用するg++/clang++のバージョンは以下のとおりである。

### g++ <a id="SS_19_19_1"></a>
```
    g++ (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
    Copyright (C) 2021 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### clang++ <a id="SS_19_19_2"></a>
```
    Ubuntu clang version 14.0.0-1ubuntu1
    Target: x86_64-pc-linux-gnu
    Thread model: posix
    InstalledDir: /usr/bin
```

## ソフトウェア一般 <a id="SS_19_20"></a>
### フリースタンディング環境 <a id="SS_19_20_1"></a>
[フリースタンディング環境](https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AA%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E7%92%B0%E5%A2%83)
とは、組み込みソフトウェアやOSのように、その実行にOSの補助を受けられないソフトウエアを指す。

### サイクロマティック複雑度 <a id="SS_19_20_2"></a>
[サイクロマティック複雑度](https://ja.wikipedia.org/wiki/%E5%BE%AA%E7%92%B0%E7%9A%84%E8%A4%87%E9%9B%91%E5%BA%A6)
とは関数の複雑さを表すメトリクスである。
このメトリクスの解釈は諸説あるものの、概ね以下のテーブルのようなものである。

|サイクロマティック複雑度(CC)|複雑さの状態                              |
|:--------------------------:|:-----------------------------------------|
|           CC <= 10         |非常に良い構造                            |
|      11 < CC <  30         |やや複雑                                  |
|      31 < CC <  50         |構造的なリスクあり                        |
|      51 < CC               |テスト不可能、デグレードリスクが非常に高い|

### 凝集度 <a id="SS_19_20_3"></a>
[凝集度](https://ja.wikipedia.org/wiki/%E5%87%9D%E9%9B%86%E5%BA%A6)
とはクラス設計の妥当性を表す尺度の一種であり、
「[凝集度の欠如](term_explanation.md#SS_19_20_3_1)(LCOM)」というメトリクスで計測される。

* [凝集度の欠如](term_explanation.md#SS_19_20_3_1)メトリクスの値が1に近ければ凝集度は低く、この値が0に近ければ凝集度は高い。
* メンバ変数やメンバ関数が多くなれば、凝集度は低くなりやすい。
* 凝集度は、クラスのメンバがどれだけ一貫した責任を持つかを示す。
* 「[単一責任の原則(SRP)](solid.md#SS_8_1)」を守ると凝集度は高くなりやすい。
* 「[Accessor](design_pattern.md#SS_9_4)」を多用すれば、振る舞いが分散しがちになるため、通常、凝集度は低くなる。
   従って、下記のようなクラスは凝集度が低い。言い換えれば、凝集度を下げることなく、
   より小さいクラスに分割できる。

```cpp
    //  example/term_explanation/lack_of_cohesion_ut.cpp 7

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

良く設計されたクラスは、下記のようにメンバが結合しあっているため凝集度が高い
(ただし、「[Immutable](design_pattern.md#SS_9_6)」の観点からは、QuadraticEquation::Set()がない方が良い)。
言い換えれば、凝集度を落とさずにクラスを分割することは難しい。

```cpp
    //  example/term_explanation/lack_of_cohesion_ut.cpp 26

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

#### 凝集度の欠如 <a id="SS_19_20_3_1"></a>
[凝集度](term_explanation.md#SS_19_20_3)の欠如(Lack of Cohesion in Methods/LCOM)とは、
クラス設計の妥当性を表す尺度の一種であり、`0 ～ 1`の値で表すメトリクスである。

LCOMの値が大きい(1か1に近い値)場合、「クラス内のメソッドが互いに関連性を持たず、
それぞれが独立した責務やデータに依存するため、クラス全体の統一性が欠けている」ことを表す。

クラスデザイン見直しの基準値としてLCOMを活用する場合、
[LCOMの評価基準](term_explanation.md#SS_19_20_3_2)に具体的な推奨値を示す。

#### LCOMの評価基準 <a id="SS_19_20_3_2"></a>
クラスデザイン良し悪しの基準値としてLCOMを活用する場合の推奨値を以下に示す。

| 凝集度の欠如(LCOM)  | クラスの状態 |
|:-------------------:|:------------:|
|       `LCOM <= 0.4` | 理想的な状態 |
|`0.4 <  LCOM <  0.6` | 要注意状態   |
|`0.6 <= LCOM`        | 改善必須状態 |


* `LCOM <= 0.4`  
  クラスが非常に凝集しており、[単一責任の原則(SRP)](solid.md#SS_8_1)を強く遵守している状態であるため、
  通常、デザインの見直しは不要である。

* `0.4 < LCOM < 0.6`  
  クラスの凝集度がやや弱くなり始めている。
  デザイン見直しの必要な時期が迫りつつあると考えるべきだろう。
  このタイミングであればリファクタリングは低コストで完了できるだろう。

* `0.6 <= LCOM`  
  クラス内のメソッド間の関連性が低く、凝集度が不十分である。
  メソッドが異なる責務にまたがっている可能性が高いため、
  一刻も早くデザインの見直しを行うべきだろう。


### Spurious Wakeup <a id="SS_19_20_4"></a>
[Spurious Wakeup](https://en.wikipedia.org/wiki/Spurious_wakeup)とは、
条件変数に対する通知待ちの状態であるスレッドが、その通知がされていないにもかかわらず、
起き上がってしまう現象のことを指す。

下記のようなstd::condition_variableの使用で起こり得る。

```cpp
    //  example/term_explanation/spurious_wakeup_ut.cpp 8

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
    //  example/term_explanation/spurious_wakeup_ut.cpp 34

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

### 副作用 <a id="SS_19_20_5"></a>
プログラミングにおいて、式の評価による作用には、
主たる作用とそれ以外の
[副作用](https://ja.wikipedia.org/wiki/%E5%89%AF%E4%BD%9C%E7%94%A8_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0))
(side effect)とがある。
式は、評価値を得ること(関数では「引数を受け取り値を返す」と表現する)が主たる作用とされ、
それ以外のコンピュータの論理的状態(ローカル環境以外の状態変数の値)を変化させる作用を副作用という。
副作用の例としては、グローバル変数や静的ローカル変数の変更、
ファイルの読み書き等のI/O実行、等がある。


### is-a <a id="SS_19_20_6"></a>
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
    //  example/term_explanation/class_relation_ut.cpp 11

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

bird::flyのオーバーライド(penguin::fly)について、 リスコフの置換原則に反した例を下記する。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 50

    class penguin : public bird {
    public:
        void fly(int altitude) override
        {
            if (altitude != 0) {
                throw std::invalid_argument{"altitude error"};
            }
        }
    };

    // ...

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
    // birdからpenguinへの派生がリスコフ置換の原則を満たすのであれば、
    // 上記のテストのpをbで置き換えたテストがパスしなければならないが、
    // 実際には逆に下記テストがパスしてしまう
    ASSERT_NE(let_it_fly(b, 0), 1);
    // このことからpenguinへの派生はリスコフ置換の原則を満たさない

```

birdからpenguinへの派生がリスコフ置換の原則に反してしまった原因は以下のように考えることができる。

* bird::flyの事前条件penguin::flyが強めた
* bird::flyの事後条件をpenguin::flyが弱めた

penguinとbirdの関係はis-aの関係ではあるが、
上記コードの問題によって不適切なis-aの関係と言わざるを得ない。

上記の例では鳥全般と鳥の種類のis-a関係をpublic継承を使用して表した(一部不適切であるもの)。
さらにis-aの誤った適用例を示す。
自身が飼っている九官鳥に"キューちゃん"と名付けることははよくあることである。
キューちゃんという名前の九官鳥は一種の九官鳥であることは間違いのないことであるが、
このis-aの関係を表すためにpublic継承を使用するのは、is-aの関係の誤用になることが多い。
実際のコード例を以下に示す。この場合、型とインスタンスの概念の混乱が原因だと思われる。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 92

    class q_chan : public kyukancho {
    public:
        std::string get_name() const override { return "キューちゃん"; }
    };
```

この誤用を改めた例を以下に示す。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 114

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
kyukanchoとstd::stringの関係を[has-a](term_explanation.md#SS_19_20_7)の関係と呼ぶ。


### has-a <a id="SS_19_20_7"></a>
「has-a」の関係は、
あるクラスのインスタンスが別のクラスのインスタンスを構成要素として含む関係を指す。
つまり、あるクラスのオブジェクトが別のクラスのオブジェクトを保持している関係である。

例えば、CarクラスとEngineクラスがあるとする。CarクラスはEngineクラスのインスタンスを含むので、
CarはEngineを「has-a」の関係にあると言える。
通常、has-aの関係はクラス内でメンバ変数またはメンバオブジェクトとして実装される。
Carクラスの例ではCarクラスにはEngine型のメンバ変数が存在する。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 145

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

### is-implemented-in-terms-of <a id="SS_19_20_8"></a>
「is-implemented-in-terms-of」の関係は、
オブジェクト指向プログラミング（OOP）において、
あるクラスが別のクラスの機能を内部的に利用して実装されていることを示す概念である。
これは、あるクラスが他のクラスのインターフェースやメソッドを用いて、
自身の機能を提供する場合に使われる。
[has-a](term_explanation.md#SS_19_20_7)の関係は、is-implemented-in-terms-of の関係の一種である。

is-implemented-in-terms-ofは下記の手段1-3に示した方法がある。

*手段1.* [public継承によるis-implemented-in-terms-of](term_explanation.md#SS_19_20_8_1)  
*手段2.* [private継承によるis-implemented-in-terms-of](term_explanation.md#SS_19_20_8_2)  
*手段3.* [コンポジションによる(has-a)is-implemented-in-terms-of](term_explanation.md#SS_19_20_8_3)  

手段1-3にはそれぞれ、長所、短所があるため、必要に応じて手段を選択する必要がある。
以下の議論を単純にするため、下記のようにクラスS、C、CCを定める。

* S(サーバー): 実装を提供するクラス
* C(クライアント): Sの実装を利用するクラス
* CC(クライアントのクライアント): Cのメンバをを使用するクラス

コード量の観点から考えた場合、手段1が最も優れていることが多い。
依存関係の複雑さから考えた場合、CはSに強く依存する。
場合によっては、この依存はCCからSへの依存間にも影響をあたえる。
従って、手段3が依存関係を単純にしやすい。
手段1は[is-a](term_explanation.md#SS_19_20_6)に見え、以下に示すような問題も考慮する必要があるため、
可読性、保守性を劣化させる可能性がある。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 261

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


#### public継承によるis-implemented-in-terms-of <a id="SS_19_20_8_1"></a>
public継承によるis-implemented-in-terms-ofの実装例を以下に示す。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 283

    class MyString : public std::string {};

    // ...
    MyString str{"str"};

    ASSERT_EQ(str[0], 's');
    ASSERT_STREQ(str.c_str(), "str");

    str.clear();
    ASSERT_EQ(str.size(), 0);
```

すでに述べたようにこの方法は、
[private継承によるis-implemented-in-terms-of](term_explanation.md#SS_19_20_8_2)や、
[コンポジションによる(has-a)is-implemented-in-terms-of](term_explanation.md#SS_19_20_8_3)
と比べコードがシンプルになる。 

#### private継承によるis-implemented-in-terms-of <a id="SS_19_20_8_2"></a>
private継承によるis-implemented-in-terms-ofの実装例を以下に示す。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 180

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

この方法は、[public継承によるis-implemented-in-terms-of](term_explanation.md#SS_19_20_8_1)が持つデストラクタ問題は発生せす、
[is-a](term_explanation.md#SS_19_20_6)と誤解してしまう問題も発生しない。


#### コンポジションによる(has-a)is-implemented-in-terms-of <a id="SS_19_20_8_3"></a>
コンポジションによる(has-a)is-implemented-in-terms-ofの実装例を示す。

```cpp
    //  example/term_explanation/class_relation_ut.cpp 208

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


## 非ソフトウェア用語 <a id="SS_19_21"></a>
### 割れ窓理論 <a id="SS_19_21_1"></a>
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


### 車輪の再発明 <a id="SS_19_21_2"></a>
[車輪の再発明](https://ja.wikipedia.org/wiki/%E8%BB%8A%E8%BC%AA%E3%81%AE%E5%86%8D%E7%99%BA%E6%98%8E)
とは、広く受け入れられ確立されている技術や解決法を（知らずに、または意図的に無視して）
再び一から作ること」を指すための慣用句である。
ソフトウェア開発では、STLのような優れたライブラリを使わずに、
それと同様なライブラリを自分たちで実装するような非効率な様を指すことが多い。


