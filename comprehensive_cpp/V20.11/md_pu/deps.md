<!-- deps/md/deps.md -->
# deps <a id="SS_17"></a>

一般的に、ある程度の規模のソフトウェアのソースコードは下記のようにファイルツリーとして管理され、
ディレクトリによりソースコードは機能毎に分割される。

```
    deps
    ├── app
    │   ├── *.cpp or *.h
    │   └── ...
    ├── dependency
    │   ├── *.cpp or *.h
    │   └── ...
    ├── file_utils
    │   ├── *.cpp or *.h
    │   └── ...
    ├── lib
    │   ├── *.cpp or *.h
    │   └── ...
    └── logging
        ├── *.cpp or *.h
        └── ...
```

このような場合、各ディレクトリはヘッダファイルを持つため、ディレクトリ間に依存関係が発生する。
このディレクトリをパッケージとみなすことにより、以下のように図示することができる。

```deps/plant_uml/deps.pu
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


常識的にはこのような依存関係には双方向や循環がない方が好ましい。

```deps/plant_uml/deps_ng.pu
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
dependency "24" <-[#red]-> file_utils
dependency "4" -[#green]-> lib
file_utils "1" -[#green]-> lib
file_utils "1" -[#green]-> logging
logging "3" <-[#red]-> lib

@enduml

```

良好な、または意図した依存関係をキープするためには、
以上で示した依存関係を簡単に図示する方法が必要になる。

そのための市販のツールを購入することもできるが、
やりたいことに完全にマッチしたものがあるわけではないため、
この章では、専用のツールdepsを開発する。

通常、このようなツールの開発にはpythonやrubyが適しているが、
このドキュメントの目的に合わせて、depsはC++で開発し、
コードツリーは、 [ディレクトリ、ファイル構成](deps.md#SS_17_2)に掲載する。

---
__この章の構成__

&emsp;&emsp; [depsの使い方](deps.md#SS_17_1)  
&emsp;&emsp;&emsp; [ユースケース-循環依存を発見した場合、非0でexitする](deps.md#SS_17_1_1)  
&emsp;&emsp;&emsp; [ユースケース-C++のソースコードを含むディレクトリを探す](deps.md#SS_17_1_2)  
&emsp;&emsp;&emsp; [ユースケース-ディレクトリをパッケージとみなして、パッケージとソースコードの関係を示す](deps.md#SS_17_1_3)  
&emsp;&emsp;&emsp; [ユースケース-パッケージ間の依存関係を示す](deps.md#SS_17_1_4)  
&emsp;&emsp;&emsp; [ユースケース-パッケージ間の依存関係を構造的に表す](deps.md#SS_17_1_5)  
&emsp;&emsp;&emsp; [ユースケース-パッケージ間の依存関係をplant umlで表す](deps.md#SS_17_1_6)  
&emsp;&emsp;&emsp; [ユースケース-ソースコード間の依存関係をplant umlで表す](deps.md#SS_17_1_7)  
&emsp;&emsp;&emsp; [ユースケース-パッケージでないディレクトリをそれとみなさない](deps.md#SS_17_1_8)  
&emsp;&emsp;&emsp; [ユースケース-depsを用いてdepsの依存関係を調べる](deps.md#SS_17_1_9)  

&emsp;&emsp; [ディレクトリ、ファイル構成](deps.md#SS_17_2)  
&emsp;&emsp; [makeによる依存関係の維持](deps.md#SS_17_3)  
  
  


## depsの使い方 <a id="SS_17_1"></a>

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

       options:
             --in IN     : use IN to execute CMD.
             --out OUT   : CMD outputs to OUT.
             --recursive : search dir as package from DIRS or IN contents.
             -R          : same as --recursive.
             --src_as_pkg: every src is as a package.
             -s          : same as --src_as_pkg.
             --log LOG   : logging to LOG(if LOG is "-", using STDOUT).
             --exclude PTN : exclude dirs which matchs to PTN(JS regex).
             -e PTN      : same as --exclude.

       DIRS: use DIRS to execute CMD.
       IN  : 1st line in this file must be
                 #dir2srcs for pkg-srcs file
             or
                 #dir for pkg file.
```

depsの仕様は入り組んでいるため、細かく機能を説明するより、
以下の各ユースケースで使い方を示した方がdepsの理解が容易であると判断した。


* [ユースケース-循環依存を発見した場合、非0でexitする](deps.md#SS_17_1_1)
* [ユースケース-C++のソースコードを含むディレクトリを探す](deps.md#SS_17_1_2)
* [ユースケース-ディレクトリをパッケージとみなして、パッケージとソースコードの関係を示す](deps.md#SS_17_1_3)
* [ユースケース-パッケージ間の依存関係を示す](deps.md#SS_17_1_4)
* [ユースケース-パッケージ間の依存関係を構造的に表す](deps.md#SS_17_1_5)
* [ユースケース-パッケージ間の依存関係をplant umlで表す](deps.md#SS_17_1_6)
* [ユースケース-ソースコード間の依存関係をplant umlで表す](deps.md#SS_17_1_7)
* [ユースケース-パッケージでないディレクトリをそれとみなさない](deps.md#SS_17_1_8)
* [ユースケース-depsを用いてdepsの依存関係を調べる](deps.md#SS_17_1_9)

におけるdepsの使い方や出力等を示す。

### ユースケース-循環依存を発見した場合、非0でexitする <a id="SS_17_1_1"></a>

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

### ユースケース-C++のソースコードを含むディレクトリを探す <a id="SS_17_1_2"></a>

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

### ユースケース-ディレクトリをパッケージとみなして、パッケージとソースコードの関係を示す <a id="SS_17_1_3"></a>

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


### ユースケース-パッケージ間の依存関係を示す <a id="SS_17_1_4"></a>

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


### ユースケース-パッケージ間の依存関係を構造的に表す <a id="SS_17_1_5"></a>

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

### ユースケース-パッケージ間の依存関係をplant umlで表す <a id="SS_17_1_6"></a>

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

実際に上記plantumlのファイルをレンダリングしたpngファイルの描画を以下に示す。

```deps/plant_uml/deps_ut_data.pu
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

### ユースケース-ソースコード間の依存関係をplant umlで表す <a id="SS_17_1_7"></a>

ソースコードをパッケージとみなすオプション(-sもしくは--src_as_pkg)を付加して、
これまでの説明と同様のことを行うと、

```
    > ./g++/deps p2p -R -s --out p2p.txt ut_data/
    > ./g++/deps a2pu  --in p2p.txt --out p2p.pu
```

ソースコードの依存関係がplant uml形式で得られる。


### ユースケース-パッケージでないディレクトリをそれとみなさない <a id="SS_17_1_8"></a>

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

### ユースケース-depsを用いてdepsの依存関係を調べる <a id="SS_17_1_9"></a>

depsを用いてdepsの依存関係を調べてみよう。

まずは下記のコマンドで依存関係を調べる。

```
    > cd comprehensive_cpp/example/deps     # comprehensive_cppはTOP_DIR
    > ./g++/deps p2p -R --out p2p.txt .
    > ./g++/deps a2pu  --in p2p.txt --out deps.pu
```

上記のほとんどデフォルトのパラメータでは以下のようなパケージ図となるため、役に立たない。
原因はテスト用のコードと、各ディレクトリの配下の「h、src、ut」がパケージとみなされるためである。

```deps/plant_uml/deps_default.pu
@startuml
scale max 730 width
rectangle "src" as app___src
rectangle "ut" as app___ut
rectangle "dependency" as dependency___h___dependency
rectangle "src" as dependency___src
rectangle "ut" as dependency___ut
rectangle "file_utils" as file_utils___h___file_utils
rectangle "src" as file_utils___src
rectangle "ut" as file_utils___ut
rectangle "a" as it_data___fake___a {
    rectangle "e" as it_data___fake___a___e
}
rectangle "b" as it_data___fake___b {
    rectangle "e" as it_data___fake___b___e
}
rectangle "c" as it_data___fake___c {
    rectangle "e" as it_data___fake___c___e
}
rectangle "d" as it_data___fake___d {
    rectangle "e" as it_data___fake___d___e
}
rectangle "e" as it_data___fake___e {
    rectangle "e" as it_data___fake___e___e
}
rectangle "lib" as lib___h___lib
rectangle "ut" as lib___ut
rectangle "logging" as logging___h___logging
rectangle "src" as logging___src
rectangle "ut" as logging___ut
rectangle "app1" as ut_data___app1 {
    rectangle "mod1" as ut_data___app1___mod1
    rectangle "mod2" as ut_data___app1___mod2 {
        rectangle "mod2_1" as ut_data___app1___mod2___mod2_1
        rectangle "mod2_2" as ut_data___app1___mod2___mod2_2
    }
}
rectangle "app2" as ut_data___app2

app___ut "1" -[#green]-> app___src
app___src "1" -[#green]-> dependency___h___dependency
app___src "3" -[#green]-> file_utils___h___file_utils
app___src "2" -[#green]-> lib___h___lib
app___src "1" -[#green]-> logging___h___logging
app___ut "1" -[#green]-> file_utils___h___file_utils
app___ut "1" -[#green]-> lib___h___lib
dependency___src "1" -[#green]-> dependency___h___dependency
dependency___ut "1" -[#green]-> dependency___h___dependency
dependency___h___dependency "1" -[#green]-> file_utils___h___file_utils
dependency___ut "15" -[#green]-> dependency___src
dependency___src "13" -[#green]-> file_utils___h___file_utils
dependency___src "4" -[#green]-> lib___h___lib
dependency___ut "10" -[#green]-> file_utils___h___file_utils
file_utils___src "3" -[#green]-> file_utils___h___file_utils
file_utils___ut "6" -[#green]-> file_utils___h___file_utils
file_utils___ut "1" -[#green]-> lib___h___lib
file_utils___ut "1" -[#green]-> logging___h___logging
it_data___fake___a "1" -[#green]-> it_data___fake___b___e
it_data___fake___a "1" -[#green]-> it_data___fake___d___e
it_data___fake___c "1" -[#green]-> it_data___fake___a___e
it_data___fake___b "1" -[#green]-> it_data___fake___c___e
it_data___fake___c "1" -[#green]-> it_data___fake___c___e
it_data___fake___d "1" -[#green]-> it_data___fake___e___e
it_data___fake___e "1" -[#green]-> it_data___fake___d___e
lib___ut "1" -[#green]-> lib___h___lib
logging___h___logging "1" -[#green]-> lib___h___lib
logging___src "1" -[#green]-> lib___h___lib
logging___ut "1" -[#green]-> lib___h___lib
logging___src "1" -[#green]-> logging___h___logging
logging___ut "1" -[#green]-> logging___h___logging
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

この問題を回避するため、パッケージを定義する必要がある。
パッケージの定義のためにはまず以下のようなコマンドを実行し、p.txtを生成し、
それを修正するのが良い。

```
    > ./g++/deps p -R --out p.txt .
```

```
    > cat p.txt
    #dir
    app/src
    app/ut

    ... 省略

    ut_data/app1/mod1
    ut_data/app1/mod2
    ut_data/app1/mod2/mod2_1
    ut_data/app1/mod2/mod2_2
    ut_data/app2
```

上記のようなp.txtを下記のように修正する。

```
    > cat p.txt
    #dir
    app
    dependency
    file_utils
    lib
    logging
```

このパッケージの定義ファイルを使用し以下のコマンドを実行することで、
deps.puを生成する。

```
    > ./g++/deps p2p  --in p.txt --out p2p.txt .    # 最後の引数はディレクトリ(忘れがち)
    > ./g++/deps a2pu  --in p2p.txt --out deps.pu
```
deps.puをレンダリングすることで以下のイメージを得ることができる。

```deps/plant_uml/deps_usecase.pu
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

なお、plant_umlのレンダリングには適切な環境設定が必要であるが下記の実行が便利である。

```
    > <TOP_DIR>/md_gen/export/sh/pu2png.sh deps.pu
```



## ディレクトリ、ファイル構成 <a id="SS_17_2"></a>

* app:main.cppを含むパッケージ
    * [example/deps/CMakeLists.txt](sample_code.md#SS_26_3_1) **---** メインのCMakeLists.txt
    * [example/deps/app/src/main.cpp](sample_code.md#SS_26_2_3) **---** depsのmain関数を含むファイル
    * [example/deps/app/src/deps_opts.cpp](sample_code.md#SS_26_2_1) **---** depsのオプション処理
    * [example/deps/app/src/deps_opts.h](sample_code.md#SS_26_2_2)
    * [example/deps/app/ut/deps_opts_ut.cpp](sample_code.md#SS_26_2_4) **---** appパッケージの単体テスト

* dependency:依存関係を導き出すアルゴリズムライブラリdependency.a用のパッケージ
    * [example/deps/dependency/CMakeLists.txt](sample_code.md#SS_26_3_2) **---** dependencyのCMakeLists.txt
    * [example/deps/dependency/src/arch_pkg.cpp](sample_code.md#SS_26_2_6) **---** パッケージの依存関係の導出
    * [example/deps/dependency/src/arch_pkg.h](sample_code.md#SS_26_2_7) **---** arch_pkg.cppの非公開ヘッダ
    * [example/deps/dependency/src/cpp_deps.cpp](sample_code.md#SS_26_2_8) **---** ファイル間依存関係の依存関係の導出
    * [example/deps/dependency/src/cpp_deps.h](sample_code.md#SS_26_2_9) **---** cpp_deps.cppの非公開ヘッダ
    * [example/deps/dependency/src/cpp_dir.cpp](sample_code.md#SS_26_2_10) **---** C++ファイルを含むディレクトリ抽出
    * [example/deps/dependency/src/cpp_dir.h](sample_code.md#SS_26_2_11) **---** cpp_dir.cppの非公開ヘッダ
    * [example/deps/dependency/src/cpp_src.cpp](sample_code.md#SS_26_2_12) **---** C++ファイルの抽出
    * [example/deps/dependency/src/cpp_src.h](sample_code.md#SS_26_2_13) **---** cpp_src.cppの非公開ヘッダ
    * [example/deps/dependency/h/dependency/deps_scenario.h](sample_code.md#SS_26_2_5) **---** 依存関係表示のシナリオの公開ヘッダ
    * [example/deps/dependency/src/deps_scenario.cpp](sample_code.md#SS_26_2_14) **---** 依存関係表示のユースケースシナリオ
    * [example/deps/dependency/src/load_store_format.cpp](sample_code.md#SS_26_2_15) **---** deps生成ファイルのロード/ストア
    * [example/deps/dependency/src/load_store_format.h](sample_code.md#SS_26_2_16) **---** load_store_format.cppの非公開ヘッダ
    * [example/deps/dependency/ut/arch_pkg_ut.cpp](sample_code.md#SS_26_2_17) **---** arch_pkg.cppの単体テスト
    * [example/deps/dependency/ut/cpp_deps_ut.cpp](sample_code.md#SS_26_2_18) **---** cpp_deps.cppの単体テスト
    * [example/deps/dependency/ut/cpp_dir_ut.cpp](sample_code.md#SS_26_2_19) **---** cpp_dir.cppの単体テスト
    * [example/deps/dependency/ut/cpp_src_ut.cpp](sample_code.md#SS_26_2_20) **---** cpp_src.cppの単体テスト
    * [example/deps/dependency/ut/deps_scenario_ut.cpp](sample_code.md#SS_26_2_21) **---** deps_scenario.cppの単体テスト
    * [example/deps/dependency/ut/load_store_format_ut.cpp](sample_code.md#SS_26_2_22) **---** load_store_format.cppの単体テスト

*  file_utils:file_utils.a用のディレクトリ
    * [example/deps/file_utils/CMakeLists.txt](sample_code.md#SS_26_3_3) **---** file_utilsのCMakeLists.txt
    * [example/deps/file_utils/h/file_utils/load_store.h](sample_code.md#SS_26_2_23) **---** ファイルのロード/ストア
    * [example/deps/file_utils/h/file_utils/load_store_row.h](sample_code.md#SS_26_2_24) **---** load_store_row.cppのヘッダ
    * [example/deps/file_utils/h/file_utils/path_utils.h](sample_code.md#SS_26_2_25) **---** path_utils.cppのヘッダ
    * [example/deps/file_utils/src/load_store_row.cpp](sample_code.md#SS_26_2_26) **---** ファイルのロード/ストア
    * [example/deps/file_utils/src/path_utils.cpp](sample_code.md#SS_26_2_27) **---** ファイル操作
    * [example/deps/file_utils/ut/load_store_row_ut.cpp](sample_code.md#SS_26_2_28) **---** load_store_row.cppの単体テスト
    * [example/deps/file_utils/ut/path_utils_ut.cpp](sample_code.md#SS_26_2_29) **---** path_utils.cppの単体テスト 

*  lib:全域からアクセス可能なテンプレートライブラリ
    * [example/deps/lib/CMakeLists.txt](sample_code.md#SS_26_3_4) **---** libのCMakeLists.txt
    * [example/deps/lib/h/lib/nstd.h](sample_code.md#SS_26_2_30) **---** テンプレートライブラリ
    * [example/deps/lib/ut/nstd_ut.cpp](sample_code.md#SS_26_2_31) **---** nstd.hの単体テスト

*  logging:logging.a用のディレクトリ
    * [example/deps/logging/CMakeLists.txt](sample_code.md#SS_26_3_5) **---** loggingのCMakeLists.txt
    * [example/deps/logging/h/logging/logger.h](sample_code.md#SS_26_2_32) **---** logger.cppのヘッダ
    * [example/deps/logging/src/logger.cpp](sample_code.md#SS_26_2_33) **---** ログの取得
    * [example/deps/logging/ut/logger_ut.cpp](sample_code.md#SS_26_2_34) **---** logger.cppの単体テスト
                                                             
                                                             
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

は冗長に見える。コンパイラオプションのインクルードパスにdependency/h指定することにより、
dependencyをインポートするソースコードのインクルードディレクティブは下記のように記述することになる。


```cpp
    //  example/deps/dependency/src/deps_scenario.cpp 7

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
    //  example/deps/dependency/CMakeLists.txt 19

    # dependency.aをリンクするファイルに
    # ../dependency/h ../file_utils/h ../lib/h
    # のヘッダファイルを公開する

    target_include_directories(dependency PUBLIC ../dependency/h ../file_utils/h ../lib/h)
```

CMakeの公式ガイドラインや一般的な慣習に沿ったこの構造とインクルードディレクティブの記述様式は、
プロジェクトの可読性と保守性を向上させるために推奨される方法である。
冗長に見えるディレクトリ名も、プロジェクト全体の理解を容易にするために有効である。

depsの各パッケージの依存関係は、

```deps/plant_uml/deps.pu
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

のようになっている。

当然ながら、「[パッケージとその構成ファイル](programming_convention.md#SS_3_7)」で述べた構造と相似である。

なお、utディレクトリを各パッケージ内のサブパッケージとした場合の依存関係は、

```deps/plant_uml/deps_2.pu
@startuml
scale max 730 width
rectangle "app" as app {
    rectangle "ut" as app___ut
}
rectangle "dependency" as dependency {
    rectangle "ut" as dependency___ut
}
rectangle "file_utils" as file_utils {
    rectangle "ut" as file_utils___ut
}
rectangle "lib" as lib {
    rectangle "ut" as lib___ut
}
rectangle "logging" as logging {
    rectangle "ut" as logging___ut
}

app___ut "1" -[#green]-> app
app "1" -[#green]-> dependency
app "3" -[#green]-> file_utils
app "2" -[#green]-> lib
app "1" -[#green]-> logging
app___ut "1" -[#green]-> file_utils
app___ut "1" -[#green]-> lib
dependency___ut "16" -[#green]-> dependency
dependency "14" -[#green]-> file_utils
dependency "4" -[#green]-> lib
dependency___ut "10" -[#green]-> file_utils
file_utils___ut "6" -[#green]-> file_utils
file_utils___ut "1" -[#green]-> lib
file_utils___ut "1" -[#green]-> logging
lib___ut "1" -[#green]-> lib
logging "2" -[#green]-> lib
logging___ut "1" -[#green]-> lib
logging___ut "1" -[#green]-> logging

@enduml
```

のようになっており、整理された依存関係であるといえる。

パッケージとその単体テスト用ソースコードへのヘッダファイル公開は、
必要以上に公開範囲を広げないようにするために下記のように行われる。

```cpp
    //  example/deps/dependency/CMakeLists.txt 38

    # dependency_ut_exeはdependency.aの単体テスト
    # dependency_ut_exeが使用するライブラリのヘッダは下記の記述で公開される
    target_link_libraries(dependency_ut_exe dependency file_utils logging gtest gtest_main)

    # dependency_ut_exeに上記では公開範囲が不十分である場合、
    # dependency_ut_exeが使用するライブラリのヘッダは下記の記述で限定的に公開される
    # dependency_ut_exeにはdependency/src/*.hへのアクセスが必要
    target_include_directories(dependency_ut_exe PRIVATE ../../../deep/h src)
```

ソースコードの構成をdepsのようにすることを推奨する。


## makeによる依存関係の維持 <a id="SS_17_3"></a>
ビルドツールにmake、コンパイラにg++やclang++を使うのであれば、

* 下記のMakefileのように、コンパイラに指定するインクルードパスを制限し、
  パッケージごとにライブラリを作る

```Makefile
    //  example/deps/Makefile 86
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

* #includeディレクティブでのパスに上方向のディレクトリ指定("../")を使わない
  (「[#includeで指定するパス名](programming_convention.md#SS_3_7_7)」参照)

とすることで、ビルド時に循環依存を作らないことを担保することができる
(「[アーキテクチャの設計](architecture.md#SS_10_2)」参照)。

CMakeやVisual Studioを含むほとんどのビルドツールでも同様のことは可能である
(逆に言えば、このようなことができないビルドツールを使うべきではない)。


