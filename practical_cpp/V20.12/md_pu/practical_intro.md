<!-- ./md/practical_intro.md -->
# イントロダクション <a id="SS_1"></a>
このドキュメントはC++のプロジェクトにおいて必要になる様々なルール等を提供する。

## 改訂履歴 <a id="SS_1_1"></a>
* V20.12
    * CRTPの説明強化
    * 「標準ライブラリとプログラミングの概念」に「std::enable_shared_from_this」の説明追加
    * このドキュメントのSOLIDとデザインパターンの章をdeep_cppへ移動
    * C++慣用語句に「Modern CMake project layout」を追加

## 例示したコードの説明 <a id="SS_1_2"></a>
次章以降では、ソースコードを使って説明を行う場合がある。このような場合の注意点を述べる。

* 「...」のみで構成された行は、ソースコードの省略を表す。
* 特定の規則、法則、慣習等を説明するためのソースコードは、シンプルさを優先するため、
  その他の規則、法則、慣習に従っていない場合がある。特に識別子に関しては、
  「[命名規則](naming_practice.md#SS_4)」に従っていない場合が多い。
  また、一般にSTLのコンテナクラスやstd::stringをnewする必要はないが、
  コードの動作を示すためにあえてそのようにする場合がある。
* ソースコード内に動作説明のような本来不要なコメントがあるのは、
  読者にその意味を知らせるためであるため、製品コードのコメントをこのようにするべきではない。
* 例示したコードの動作の確認、明示のために
  [google test(gtest)](http://opencv.jp/googletestdocs/primer.html)のアサーション(下表)を使用する。

|アサーションマクロ  | 意味                                     |
|:-------------------|:-----------------------------------------|
| ASSERT_TRUE(x)     | xがtrue                                  |
| ASSERT_FALSE(x)    | xがfalse                                 |
| ASSERT_EQ(x, y)    | (x == y)がtrue                           |
| ASSERT_NE(x, y)    | (x != y)がtrue                           |
| ASSERT_GE(x, y)    | (x >= y)がtrue                           |
| ASSERT_GT(x, y)    | (x >  y)がtrue                           |
| ASSERT_LE(x, y)    | (x <= y)がtrue                           |
| ASSERT_LT(x, y)    | (x <  y)がtrue                           |
| ASSERT_STREQ(x, y) | (std::string(x) == std::string(y))がtrue |
| ASSERT_DEATH(x, y) | xを実行するとアボートすればtrue          |
| ASSERT_THROW(x, y) | xを実行するとy例外が発生すればtrue       |

* 問題を示すために掲載したコードは、実行すると不具合を発生させることがある。
  そういった場合、下記のように単体テストのラベルにDISABLED\_を付けることで、
  その実行を抑止することがある。

```cpp
    TEST(DISABLED_Xxx, yyy)
    {
        // 単体テスト
    }
```

## 本ドキュメントでの言葉の使い方の注意 <a id="SS_1_3"></a>
* 参照
    * 「～を参照する」というような文脈で使われる**「参照」**はそのまま使用する。
    * C++での参照型を表す**参照**は使わず、代わりに**「リファレンス」**を使用する。
* 例外
    * 「～の場合は例外である」というような文脈で使われる**「例外」**はそのまま使用する。
    * C++でthrowすると発生する事象を表す**例外**は使わず、代わりに**「エクセプション」**を使用する。
* classとクラス
    * **class**はC++のキーワードとして使用する。
    * **クラス**は上記以外で使用する。
* プログラミングとコーディング、ソースコードとコード、インスタンスとオブジェクト、に関しては同義語として使用する。


## インデックス <a id="SS_1_4"></a>
___

- [プログラミング規約](programming_convention.md#SS_2)
- [コーディングスタイル](coding_style.md#SS_3)
- [命名規則](naming_practice.md#SS_4)
- [コメント](comment.md#SS_5)
- [SOLID](solid.md#SS_6)
- [デザインパターン](design_pattern.md#SS_7)
- [テンプレートメタプログラミング](template_meta_programming.md#SS_8)
- [C++コア言語仕様](core_lang_spec.md#SS_9)
- [標準ライブラリとプログラミングの概念](stdlib_and_concepts.md#SS_10)
- [C++慣用語句](cpp_idioms.md#SS_11)
- [参考文献](bibliography.md#SS_12)
- [Sample Code](sample_code.md#SS_13)


