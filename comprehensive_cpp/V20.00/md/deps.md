<!-- ./md/deps.md -->
# deps <a id="SS_17"></a>
本ドキュメントでは、いくつかの場所でパッケージ間の依存関係の重要性について説明したため、
これに従って開発を行うのであれば、依存関係の維持、監視が必要になる。

そのための市販のツールを購入することもできるが、
やりたいことと完全にマッチしたものがあるわけではないため、
このドキュメント専用のツールdepsを開発した。

このようなツールの開発にはpythonやrubyが適しているが、
このドキュメントの目的に合わせて、depsは下記のようにC++で書かれている。

---
__この章の構成__

&emsp;&emsp; [ディレクトリ、ファイル構成](deps.md#SS_17_1)  
&emsp;&emsp; [depsの使い方](deps.md#SS_17_2)  
&emsp;&emsp;&emsp; [ユースケース-循環依存を発見した場合、非0でexitする](deps.md#SS_17_2_1)  
&emsp;&emsp;&emsp; [ユースケース-C++のソースコードを含むディレクトリを探す](deps.md#SS_17_2_2)  
&emsp;&emsp;&emsp; [ユースケース-ディレクトリをパッケージとみなして、パッケージとソースコードの関係を示す](deps.md#SS_17_2_3)  
&emsp;&emsp;&emsp; [ユースケース-パッケージ間の依存関係を示す](deps.md#SS_17_2_4)  
&emsp;&emsp;&emsp; [ユースケース-パッケージ間の依存関係を構造的に表す](deps.md#SS_17_2_5)  
&emsp;&emsp;&emsp; [ユースケース-パッケージ間の依存関係をplant umlで表す](deps.md#SS_17_2_6)  
&emsp;&emsp;&emsp; [ユースケース-ソースコード間の依存関係をplant umlで表す](deps.md#SS_17_2_7)  
&emsp;&emsp;&emsp; [ユースケース-パッケージでないディレクトリをそれとみなさない](deps.md#SS_17_2_8)  

&emsp;&emsp; [makeによる依存関係の維持](deps.md#SS_17_3)  
  
  


## ディレクトリ、ファイル構成 <a id="SS_17_1"></a>

* app:main.cppを含むパッケージ
    * [example/deps/CMakeLists.txt](sample_code.md#SS_24_3_1) **---** メインのCMakeLists.txt
    * [example/deps/app/src/main.cpp](sample_code.md#SS_24_2_3) **---** depsのmain関数を含むファイル
    * [example/deps/app/src/deps_opts.cpp](sample_code.md#SS_24_2_1) **---** depsのオプション処理
    * [example/deps/app/src/deps_opts.h](sample_code.md#SS_24_2_2)
    * [example/deps/app/ut/deps_opts_ut.cpp](sample_code.md#SS_24_2_4) **---** appパッケージの単体テスト

* dependency:依存関係を導き出すアルゴリズムライブラリdependency.a用のパッケージ
    * [example/deps/dependency/CMakeLists.txt](sample_code.md#SS_24_3_2) **---** dependencyのCMakeLists.txt
    * [example/deps/dependency/src/arch_pkg.cpp](sample_code.md#SS_24_2_6) **---** パッケージの依存関係の導出
    * [example/deps/dependency/src/arch_pkg.h](sample_code.md#SS_24_2_7) **---** arch_pkg.cppの非公開ヘッダ
    * [example/deps/dependency/src/cpp_deps.cpp](sample_code.md#SS_24_2_8) **---** ファイル間依存関係の依存関係の導出
    * [example/deps/dependency/src/cpp_deps.h](sample_code.md#SS_24_2_9) **---** cpp_deps.cppの非公開ヘッダ
    * [example/deps/dependency/src/cpp_dir.cpp](sample_code.md#SS_24_2_10) **---** C++ファイルを含むディレクトリ抽出
    * [example/deps/dependency/src/cpp_dir.h](sample_code.md#SS_24_2_11) **---** cpp_dir.cppの非公開ヘッダ
    * [example/deps/dependency/src/cpp_src.cpp](sample_code.md#SS_24_2_12) **---** C++ファイルの抽出
    * [example/deps/dependency/src/cpp_src.h](sample_code.md#SS_24_2_13) **---** cpp_src.cppの非公開ヘッダ
    * [example/deps/dependency/h/dependency/deps_scenario.h](sample_code.md#SS_24_2_5) **---** 依存関係表示のシナリオの公開ヘッダ
    * [example/deps/dependency/src/deps_scenario.cpp](sample_code.md#SS_24_2_14) **---** 依存関係表示のユースケースシナリオ
    * [example/deps/dependency/src/load_store_format.cpp](sample_code.md#SS_24_2_15) **---** deps生成ファイルのロード/ストア
    * [example/deps/dependency/src/load_store_format.h](sample_code.md#SS_24_2_16) **---** load_store_format.cppの非公開ヘッダ
    * [example/deps/dependency/ut/arch_pkg_ut.cpp](sample_code.md#SS_24_2_17) **---** arch_pkg.cppの単体テスト
    * [example/deps/dependency/ut/cpp_deps_ut.cpp](sample_code.md#SS_24_2_18) **---** cpp_deps.cppの単体テスト
    * [example/deps/dependency/ut/cpp_dir_ut.cpp](sample_code.md#SS_24_2_19) **---** cpp_dir.cppの単体テスト
    * [example/deps/dependency/ut/cpp_src_ut.cpp](sample_code.md#SS_24_2_20) **---** cpp_src.cppの単体テスト
    * [example/deps/dependency/ut/deps_scenario_ut.cpp](sample_code.md#SS_24_2_21) **---** deps_scenario.cppの単体テスト
    * [example/deps/dependency/ut/load_store_format_ut.cpp](sample_code.md#SS_24_2_22) **---** load_store_format.cppの単体テスト

*  file_utils:file_utils.a用のディレクトリ
    * [example/deps/file_utils/CMakeLists.txt](sample_code.md#SS_24_3_3) **---** file_utilsのCMakeLists.txt
    * [example/deps/file_utils/h/file_utils/load_store.h](sample_code.md#SS_24_2_23) **---** ファイルのロード/ストア
    * [example/deps/file_utils/h/file_utils/load_store_row.h](sample_code.md#SS_24_2_24) **---** load_store_row.cppのヘッダ
    * [example/deps/file_utils/h/file_utils/path_utils.h](sample_code.md#SS_24_2_25) **---** path_utils.cppのヘッダ
    * [example/deps/file_utils/src/load_store_row.cpp](sample_code.md#SS_24_2_26) **---** ファイルののロード/ストア
    * [example/deps/file_utils/src/path_utils.cpp](sample_code.md#SS_24_2_27) **---** ファイル操作
    * [example/deps/file_utils/ut/load_store_row_ut.cpp](sample_code.md#SS_24_2_28) **---** load_store_row.cppの単体テスト
    * [example/deps/file_utils/ut/path_utils_ut.cpp](sample_code.md#SS_24_2_29) **---** path_utils.cppの単体テスト 

*  lib:全域からアクセス可能なテンプレートライブラリ
    * [example/deps/lib/CMakeLists.txt](sample_code.md#SS_24_3_4) **---** libのCMakeLists.txt
    * [example/deps/lib/h/lib/nstd.h](sample_code.md#SS_24_2_30) **---** テンプレートライブラリ
    * [example/deps/lib/ut/nstd_ut.cpp](sample_code.md#SS_24_2_31) **---** nstd.hの単体テスト

*  logging:logging.a用のディレクトリ
    * [example/deps/logging/CMakeLists.txt](sample_code.md#SS_24_3_5) **---** loggingのCMakeLists.txt
    * [example/deps/logging/h/logging/logger.h](sample_code.md#SS_24_2_32) **---** logger.cppのヘッダ
    * [example/deps/logging/src/logger.cpp](sample_code.md#SS_24_2_33) **---** ログの取得
    * [example/deps/logging/ut/logger_ut.cpp](sample_code.md#SS_24_2_34) **---** logger.cppの単体テスト
                                                             
                                                             
下記のをファイルツリーは上記を表す。

```
    deps
    ├── makefile                    # makeでもビルドできる
    ├── CMakeLists.txt              # cmakeのルートCMakeLists.txt
    ├── app                         # パケージappはエクスポートするヘッダはないためhもない
    │   ├── CMakeLists.txt
    │   ├── src
    │   │   ├── deps_opts.cpp
    │   │   ├── deps_opts.h
    │   │   └── main.cpp
    │   └── ut
    │       └── deps_opts_ut.cpp    # utはsrcにアクセスできる
    ├── dependency
    │   ├── CMakeLists.txt
    │   ├── h
    │   │   └── dependency          # このディレクトリにエクスポートするヘッダを配置
    │   │       └── deps_scenario.h
    │   ├── src
    │   │   ├── arch_pkg.cpp
    │   │   ├── arch_pkg.h
    │   │   ├── cpp_deps.cpp
    │   │   ├── cpp_deps.h
    │   │   ├── cpp_dir.cpp
    │   │   ├── cpp_dir.h
    │   │   ├── cpp_src.cpp
    │   │   ├── cpp_src.h
    │   │   ├── deps_scenario.cpp
    │   │   ├── load_store_format.cpp
    │   │   └── load_store_format.h
    │   └── ut                      # utはh、srcにアクセスできる
    │       ├── arch_pkg_ut.cpp
    │       ├── cpp_deps_ut.cpp
    │       ├── cpp_dir_ut.cpp
    │       ├── cpp_src_ut.cpp
    │       ├── deps_scenario_ut.cpp
    │       └── load_store_format_ut.cpp
    ├── file_utils
    │   ├── CMakeLists.txt
    │   ├── h
    │   │   └── file_utils      # このディレクトリにエクスポートするヘッダを配置
    │   │       ├── load_store.h
    │   │       ├── load_store_row.h
    │   │       └── path_utils.h
    │   ├── src
    │   │   ├── load_store_row.cpp
    │   │   └── path_utils.cpp
    │   └── ut
    │       ├── load_store_row_ut.cpp
    │       └── path_utils_ut.cpp
    ├── lib
    │   ├── CMakeLists.txt
    │   ├── h
    │   │   └── lib             # このディレクトリにエクスポートするヘッダを配置
    │   │       └── nstd.h
    │   └── ut
    │       └── nstd_ut.cpp     # utはh、srcにアクセスできる
    └── logging
        ├── CMakeLists.txt
        ├── h
        │   └── logging         # このディレクトリにエクスポートするヘッダを配置
        │       └── logger.h
        ├── src
        │   └── logger.cpp
        └── ut                  # utはh、srcにアクセスできる
            └── logger_ut.cpp

```

例えば、dependencyの外部公開ヘッダを配置するためのディレクトリ

    dependency/h/dependency

は助長に見える。コンパイラオプションのインクルードパスにdependency/h指定することにより、
dependencyをインポートするソースコードのインクルードディレクティブは下記のように記述することになる。


```cpp
    // @@@ example/deps/dependency/src/deps_scenario.cpp 7

    #include "cpp_deps.h"                  // 実装用ヘッダファイル
    #include "cpp_dir.h"                   // 実装用ヘッダファイル
    #include "cpp_src.h"                   // 実装用ヘッダファイル
    #include "dependency/deps_scenario.h"  // dependencyパッケージからのインポート
    #include "file_utils/load_store.h"     // file_utilsパッケージからのインポート
    #include "lib/nstd.h"                  // libパッケージからのインポート
```

上記から明らかな通り、このソースコードの外部パッケージとの依存関係が明確になる。
このようなインクルードディレクトリを下記のように指定することでこのような記述が可能になる。

```cpp
    // @@@ example/deps/dependency/CMakeLists.txt 19

    # dependency.aをリンクするファイルに
    # ../dependency/h ../file_utils/h ../lib/h
    # のヘッダファイルを公開する

    target_include_directories(dependency PUBLIC ../dependency/h ../file_utils/h ../lib/h)
```

CMakeの公式ガイドラインや一般的な慣習に沿ったこの構造とインクルードディレクティブの記述様式は、
プロジェクトの可読性と保守性を向上させるために推奨される方法である。
冗長に見えるディレクトリ名も、プロジェクト全体の理解を容易にするために有効である。

depsの各パッケージの依存関係は、

<!-- pu:plant_uml/deps.pu--><p><img src="data:image/png;base64,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" /></p>

のようになっている。

当然ながら、「[パッケージとその構成ファイル](programming_convention.md#SS_3_7)」で述べた構造と相似である。

なお、utディレクトリを各パッケージ内のサブパッケージとした場合の依存関係は、

<!-- pu:plant_uml/deps_2.pu--><p><img src="data:image/png;base64,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mADJ6Y3pVjoDqnR7KVq86kh+5513ghhki4iYNWuW9yGaTmhIPn369Ne//vXly5d7XQGvvymPEUeInFCXsPgji83YWiQ/Zch0SHbsd2iU0tm8OTUna+zKWJojzXXYZXkki/gVJlQLJE/3G0yPZNhTU4yiKPemRfIHtZCclZUllhIo/w2zZ8/GWy5duiQevvHGG74fGBkZGewmqAsXLvzrv/4rnp8/f75sRhwhcp4rz7w7aKPXREubUsZ0tQrStJ1o0+KT87fktxxpGbeKuge7YXglzwYR/sA17kweuPYOOE85cD3dq8qRHPhzTIBky6ybGJ9YmYmGrrA9KUTy7t27gdibbroJ1xiU7e/vb2xsTE8PtCVDTD9XV1fDU/vd73532223+X7gddddh/tHjhyZ8avvuOOOX/ziFwMDA4izt2/fjuezs7OlMuIiRO719JoXyUn1SWg2RHL4aj/ZrmLGLj9JvoM8BBVvK5Z5tf94GMu7AOZTp06dPn0adyYv77r77rvx0nTLu6Z7VTmSA3+O7Ei22LGMrsMueNPqIhnq6enJy8tbvHgx2JycnPzII4/s27cvwCefPHny/vvvj4uLu+aaa+68885f/vKXvh/40ksvLVu2TElr6+7ufuihh2688cY5c+YsX7787//+7//4xz9KZcSdh5wih4N5kZy5IbPrVBeRHL7yXHnaLRS13sYQz4gH7qzM+wbD2QQ1d0Kwfm1tHxg1EduT8NKtt96K2MZv2U2AV5UjecZvkRrJkh8ZG6xKt5d609MzQasOSnOkibWB5q1tgETaEVET1SrQEl8br90UgCVPq6vqrPKGEDZsfn19fYDlhz/84RBeVetbpEMyjJHMbSIEQnhzuxPJOvhz3h2o5q3tEneJtJsATVSr4GVFe4V2n2+9jEbjE/M+SfVJthqk+fznP//666+/++67R48eFct0fHM8BH5VrW+RGskN+xrMeGrYlBq5PBJbHev103UwZxFTyT5GHM6cN+mBeZEs84ioWWpVh0Oy20+2Z2/Ktp4P7TzklDZXqBbN79e//vWdd945b968BQsW3H333S+//LLyV9X6FqmRbKUZmo6BDt9BeEbJmkokEvcezG7e2pY5/DJLrdbvrddo75NX3YPdVppi8xXKBTCz+clZar2RXL6jXItUO4aoZneN7wpGtietW441att9zC3tKUNmqdXk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" /></p>

のようになっており、整理された依存関係であるといえる。

パッケージとその単体テスト用ソースコードへのヘッダファイル公開は、
必要以上に公開範囲を広げないようにするために下記のように行われる。

```cpp
    // @@@ example/deps/dependency/CMakeLists.txt 38

    # dependency_ut_exeはdependency.aの単体テスト
    # dependency_ut_exeが使用するライブラリのヘッダは下記の記述で公開される
    target_link_libraries(dependency_ut_exe dependency file_utils logging gtest gtest_main)

    # dependency_ut_exeに上記では公開範囲が不十分である場合、
    # dependency_ut_exeが使用するライブラリのヘッダは下記の記述で限定的に公開される
    # dependency_ut_exeにはdependency/src/*.hへのアクセスが必要
    target_include_directories(dependency_ut_exe PRIVATE ../../../deep/h src)
```

ソースコードの構成をdepsのようにすることを推奨する。


## depsの使い方 <a id="SS_17_2"></a>

depsのコマンドオプションを以下に示す。

```
    deps CMD [option] [DIRS] ...
       CMD:
             p    : generate package to OUT.
             s    : generate srcs with incs to OUT.
             p2s  : generate package and srcs pairs to OUT.
             p2p  : generate packages' dependencies to OUT.
             a    : generate structure to OUT from p2p output.
             a2pu : generate plant uml package to OUT from p2p output.
             cyc  : exit !0 if found cyclic dependencies.
             help : show help message.
             h    : same as help(-h, --help).

       opptions:
             --in IN     : use IN to execute CMD.
             --out OUT   : CMD outputs to OUT.
             --recursive : search dir as package from DIRS or IN contents.
             -R          : same as --recursive.
             --src_as_pkg: every src is as a package.
             -s          : same as --src_as_pkg.
             --log LOG   : loggin to LOG(if LOG is "-", using STDOUT).
             --exclude PTN : exclude dirs which matchs to PTN(JS regex).
             -e PTN      : same as --exclude.

       DIRS: use DIRS to execute CMD.
       IN  : 1st line in this file must be
                 #dir2srcs for pkg-srcs file
             or
                 #dir for pkg file.
```

各ユースケース

* [ユースケース-循環依存を発見した場合、非0でexitする](deps.md#SS_17_2_1)
* [ユースケース-C++のソースコードを含むディレクトリを探す](deps.md#SS_17_2_2)
* [ユースケース-ディレクトリをパッケージとみなして、パッケージとソースコードの関係を示す](deps.md#SS_17_2_3)
* [ユースケース-パッケージ間の依存関係を示す](deps.md#SS_17_2_4)
* [ユースケース-パッケージ間の依存関係を構造的に表す](deps.md#SS_17_2_5)
* [ユースケース-パッケージ間の依存関係をplant umlで表す](deps.md#SS_17_2_6)
* [ユースケース-ソースコード間の依存関係をplant umlで表す](deps.md#SS_17_2_7)
* [ユースケース-パッケージでないディレクトリをそれとみなさない](deps.md#SS_17_2_8)

におけるdepsの使い方や出力等を示す。

### ユースケース-循環依存を発見した場合、非0でexitする <a id="SS_17_2_1"></a>

このツールの主な目的は、パッケージ間の循環依存を検出することである。
このユースケースは、これを実現する方法を提示する。

ソースコードを含むディレクトリut_data/で下記のようにすれば、
ディレクトリをパッケージとみなした依存関係が循環した場合、depsは非0でexitする。

```
    > ./g++/deps p2p -R -s --out p2p.txt ut_data/
    > ./g++/deps cyc --in p2p.txt
```

CIのチェック項目(「[CI(継続的インテグレーション)](process_and_infra.md#SS_11_2_5)」参照)に上記を導入することで、
循環の無い依存関係を維持することができる。

下記に、「ディレクトリが必ずしもパッケージに対応するわけではない」場合の対処法を掲載する。

### ユースケース-C++のソースコードを含むディレクトリを探す <a id="SS_17_2_2"></a>

以下のコマンドは、CMD pによりut_data/配下のソースコードを含むディレクトリを探す。

```
    > ./g++/deps p -R ut_data/
```

アウトプットは以下のようになる。

```
    #dir
    ut_data/app1
    ut_data/app1/mod1
    ut_data/app1/mod2
    ut_data/app1/mod2/mod2_1
    ut_data/app1/mod2/mod2_2
    ut_data/app2
```

--out OUT-FILEを指定すれば、上記出力はOUT-FILEに書き出される。
OUT-FILEを適切に編集し、他のCMDの入力(--in IN-FILE)に使用することもできる。

### ユースケース-ディレクトリをパッケージとみなして、パッケージとソースコードの関係を示す <a id="SS_17_2_3"></a>

以下のコマンドは、CMD p2sによりut_data配下のディレクトリをパッケージとみなして、
パッケージとソースコードの関係を出力する。

```
    > ./g++/deps p2s -R ut_data/
```

アウトプットは以下のようになる。

```
    #dir2srcs
    ut_data/app1
        ut_data/app1/a_1_c.c
        ut_data/app1/a_1_c.h
        ut_data/app1/a_1_cpp.cpp
        ut_data/app1/a_1_cpp.h
    
    ... 中略 ...
    
    ut_data/app1/mod2/mod2_2
        ut_data/app1/mod2/mod2_2/mod2_2_1.cpp
        ut_data/app1/mod2/mod2_2/mod2_2_1.h

    ut_data/app2
        ut_data/app2/b_1.cpp
        ut_data/app2/b_1.h
```


### ユースケース-パッケージ間の依存関係を示す <a id="SS_17_2_4"></a>

以下のコマンドは、CMD p2pによりdeps/ut_data配下のパッケージとの依存関係をp2p.txtに出力する。

```
    > cd ./deps
    > ./g++/deps p2p -R --out p2p.txt ut_data/
```

アウトプットは以下のようになる。

```
    #deps
    ut_data/app1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp
    ut_data/app1/mod1 -> ut_data/app1 : 0
    
    ut_data/app1 -> ut_data/app1/mod2 : 0
    ut_data/app1/mod2 -> ut_data/app1 : 0
    
    ... 中略 ...
    
    ut_data/app1/mod2 -> ut_data/app2 : 0
    ut_data/app2 -> ut_data/app1/mod2 : 0
    
    ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2/mod2_2 : 1 ut_data/app1/mod2/mod2_2/mod2_2_1.h
    ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h
    
    ut_data/app1/mod2/mod2_1 -> ut_data/app2 : 0
    ut_data/app2 -> ut_data/app1/mod2/mod2_1 : 0
    
    ut_data/app1/mod2/mod2_2 -> ut_data/app2 : 0
    ut_data/app2 -> ut_data/app1/mod2/mod2_2 : 0
```

例を上げて、上記の意味を説明する。  

[例]
```
    ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2/mod2_2 : 1 ut_data/app1/mod2/mod2_2/mod2_2_1.h
    ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h
```

[例の意味]  

* ut_data/app1/mod2/mod2_1からut_data/app1/mod2/mod2_2への依存ファイルは
  ut_data/app1/mod2/mod2_2/mod2_2_1.hで、1箇所includeされている。

* ut_data/app1/mod2/mod2_2からut_data/app1/mod2/mod2_1の依存ファイルは
  ut_data/app1/mod2/mod2_1/mod2_1_1.hで、2箇所includeされている。


### ユースケース-パッケージ間の依存関係を構造的に表す <a id="SS_17_2_5"></a>

以下のコマンドは、CMD aにより上記p2p.txtを構造的に出力する。

```
    > ./g++/deps a  --in p2p.txt
```

アウトプットは以下のようになる。

```
    #arch
    package  :app1:CYCLIC
    parent   :TOP
    depend_on: {
        mod1 : CYCLIC
    }
    children : {
        package  :mod1:CYCLIC
        parent   :app1
        depend_on: {
            mod2 : STRAIGHT
            mod2_2 : CYCLIC
        }
        children : { }

        package  :mod2
        parent   :app1
        depend_on: { }
        children : {
            package  :mod2_1:CYCLIC
            parent   :mod2
            depend_on: {
                mod2_2 : CYCLIC
            }
            children : { }

            package  :mod2_2:CYCLIC
            parent   :mod2
            depend_on: {
                app1 : CYCLIC
                mod2_1 : CYCLIC
            }
            children : { }
        }
    }

    package  :app2
    parent   :TOP
    depend_on: {
        app1 : STRAIGHT
        mod1 : STRAIGHT
    }
    children : { }
```

ディレクトリ名の後ろの

* STRAIGHTは依存関係が循環していない
* CYCLICは依存関係が循環している

ことを示している。

### ユースケース-パッケージ間の依存関係をplant umlで表す <a id="SS_17_2_6"></a>

以下のコマンドは、CMD a2puにより上記p2p.txtをplant uml形式で出力する。

```
    > ./g++/deps a2pu  --in p2p.txt
```

アウトプットは以下のようになる。

```
    @startuml
    scale max 730 width
    rectangle "app1" as ut_data___app1 {
        rectangle "mod1" as ut_data___app1___mod1
        rectangle "mod2" as ut_data___app1___mod2 {
            rectangle "mod2_1" as ut_data___app1___mod2___mod2_1
            rectangle "mod2_2" as ut_data___app1___mod2___mod2_2
        }
    }
    rectangle "app2" as ut_data___app2

    ut_data___app1 "6" <-[#red]-> "1" ut_data___app1___mod1
    ut_data___app1 "3" <-[#red]-> "1" ut_data___app1___mod2___mod2_1
    ut_data___app1 "3" <-[#red]-> "2" ut_data___app1___mod2___mod2_2
    ut_data___app2 "3" -[#green]-> ut_data___app1
    ut_data___app1___mod1 "1" -[#green]-> ut_data___app1___mod2
    ut_data___app1___mod1 "1" <-[#red]-> "2" ut_data___app1___mod2___mod2_1
    ut_data___app1___mod1 "1" <-[#red]-> "4" ut_data___app1___mod2___mod2_2
    ut_data___app2 "4" -[#green]-> ut_data___app1___mod1
    ut_data___app1___mod2___mod2_1 "1" <-[#red]-> "2" ut_data___app1___mod2___mod2_2
    ut_data___app2 "2" -[#green]-> ut_data___app1___mod2___mod2_1
    ut_data___app2 "2" -[#green]-> ut_data___app1___mod2___mod2_2

    @enduml
```

このアウトプットを[plant umlオンラインジェネレータ](http://www.plantuml.com/plantuml/)
のテキストボックスに貼り付ければpngファイルが得られ、視覚的に依存関係を把握できる。

### ユースケース-ソースコード間の依存関係をplant umlで表す <a id="SS_17_2_7"></a>

ソースコードをパッケージとみなすオプション(-sもしくは--src_as_pkg)を付加して、
これまでの説明と同様のことを行うと、

```
    > ./g++/deps p2p -R -s --out p2p.txt ut_data/
    > ./g++/deps a2pu  --in p2p.txt --out p2p.pu
```

ソースコードの依存関係がplant uml形式で得られる。


### ユースケース-パッケージでないディレクトリをそれとみなさない <a id="SS_17_2_8"></a>

depsのソースコードを含むdependency/hは、
dependencyパッケージのインターフェースを外部公開するためのものであり、
dependencyのサブパッケージではない。
このような場合、dependency/h/deps_scenario.hのようなファイルは、
dependencyに直接属するように扱うべきであるが、
このツールがファイル構造からそれを読み解くことは不可能である。

このような場合に対処する方法は下記の3通りある。

* -Rを指定せず、パッケージとなる全ディレクトリをINに記述する。
* pコマンドで候補ディレクトリを全てファイルに出力し、
  パッケージでないディレクトリをそのファイルから削除した後、
  そのファイルをINファイルとしてp2pコマンド等を使う。
* --exclude PTNでパッケージ対象でないディレクトリを指定しp2pコマンド等を使う。
  なお、例えばhディレクトリを排除する場合のPTNの指定は下記のようになる(PTNはC++の正規表現)。

```
    --exclude ".*/h/?.*"
```


## makeによる依存関係の維持 <a id="SS_17_3"></a>
ビルドツールにmake、コンパイラにg++やclang++を使うのであれば、

* 下記のMakefileのように、コンパイラに指定するインクルードパスを制限し、
  パッケージごとにライブラリを作る

```Makefile
    // @@@ example/deps/Makefile 85
    ### logging
    INC_LOGGER=-Ilib/h -Ilogging/h  # インクルードパスの指定

    # 指定されたインクルードパスを使用したコンパイル
    $(O)logging/src/%.o : logging/src/%.cpp
    	$(CXX) $(INC_LOGGER) $(SANITIZER_OPT) $(CCFLAGS) -c -o $@ $<

    # 指定されたインクルードパスを使用したUTのコンパイル
    $(O)logging/ut/%.o : logging/ut/%.cpp
    	$(CXX) $(INC_UT) $(INC_LOGGER) $(SANITIZER_OPT) $(CCFLAGS) -c -o $@ $<

    # ライブラリの生成
    $(LOGGER_A) : $(LOGGER_OBJS)
    	ar cr $@ $^

    # UT実行バイナリの生成
    $(O)logging_ut : $(LOGGER_UT_OBJS) $(FILE_UTILS_A) $(LOGGER_A) $(DEPENDENCY_A) $(GTEST_LIB)
    	$(CXX) -o $@ $^ -lpthread  -lstdc++fs $(SANITIZER_OPT) 

    ### file_utils
    INC_FILE_UTILS:=-Ilib/h -Ilogging/h -Ifile_utils/h  # インクルードパスの指定

    # 指定されたインクルードパスを使用したコンパイル
    $(O)file_utils/src/%.o : file_utils/src/%.cpp
    	$(CXX) $(INC_FILE_UTILS) $(SANITIZER_OPT) $(CCFLAGS) -c -o $@ $<

    # 指定されたインクルードパスを使用したUTのコンパイル
    $(O)file_utils/ut/%.o : file_utils/ut/%.cpp
    	$(CXX) $(INC_UT) $(INC_FILE_UTILS) $(SANITIZER_OPT) $(CCFLAGS) -c -o $@ $<

    # ライブラリの生成
    $(FILE_UTILS_A) : $(FILE_UTILS_OBJS)
    	ar cr $@ $^

    # UT実行バイナリの生成
    $(O)file_utils_ut : $(FILE_UTILS_UT_OBJS) $(FILE_UTILS_A) $(LOGGER_A) $(GTEST_LIB)
    	$(CXX) -o $@ $^ -lpthread -lstdc++fs $(SANITIZER_OPT) 
```

* #includeディレクティブでのパスにに上方向のディレクトリ指定("../")を使わない
  (「[#includeで指定するパス名](programming_convention.md#SS_3_7_7)」参照)

とすることで、ビルド時に循環依存を作らないことを担保することができる
(「[アーキテクチャの設計](architecture.md#SS_10_2)」参照)。

CMakeやVisual Studioを含むほとんどのビルドツールでも同様のことは可能である
(逆に言えば、このようなことができないビルドツールを使うべきではない)。


