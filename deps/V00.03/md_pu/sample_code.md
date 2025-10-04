<!-- ./md/sample_code.md -->
# Sample Code <a id="SS_3"></a>
## C++ <a id="SS_3_1"></a>
### example/deps/app/src/deps_opts.cpp <a id="SS_3_1_1"></a>
```cpp
          1 #include <getopt.h>
          2 
          3 #include <cassert>
          4 #include <sstream>
          5 
          6 #include "deps_opts.h"
          7 #include "lib/nstd.h"
          8 
          9 namespace App {
         10 std::string DepsOpts::Help() {
         11   auto ss = std::ostringstream{};
         12 
         13   ss << "deps CMD [option] [DIRS] ..." << std::endl;
         14   ss << "   CMD:" << std::endl;
         15   ss << "         p    : generate package to OUT." << std::endl;
         16   ss << "         s    : generate srcs with incs to OUT." << std::endl;
         17   ss << "         p2s  : generate package and srcs pairs to OUT." << std::endl;
         18   ss << "         p2p  : generate packages' dependencies to OUT." << std::endl;
         19   ss << "         a    : generate structure to OUT from p2p output."
         20      << std::endl;
         21   ss << "         a2pu : generate plant uml package to OUT from p2p output."
         22      << std::endl;
         23   ss << "         cyc  : exit !0 if found cyclic dependencies." << std::endl;
         24   ss << "         help : show help message." << std::endl;
         25   ss << "         h    : same as help(-h, --help)." << std::endl;
         26   ss << std::endl;
         27   ss << "   options:" << std::endl;
         28   ss << "         --in IN     : use IN to execute CMD." << std::endl;
         29   ss << "         --out OUT   : CMD outputs to OUT." << std::endl;
         30   ss << "         --recursive : search dir as package from DIRS or IN contents."
         31      << std::endl;
         32   ss << "         -R          : same as --recursive." << std::endl;
         33   ss << "         --src_as_pkg: every src is as a package." << std::endl;
         34   ss << "         -s          : same as --src_as_pkg." << std::endl;
         35   ss << "         --log LOG   : logging to LOG(if LOG is \"-\", using STDOUT)."
         36      << std::endl;
         37   ss << "         --exclude PTN : exclude dirs which matchs to PTN(JS regex)."
         38      << std::endl;
         39   ss << "         -e PTN      : same as --exclude." << std::endl;
         40   ss << std::endl;
         41   ss << "   DIRS: use DIRS to execute CMD." << std::endl;
         42   ss << "   IN  : 1st line in this file must be" << std::endl;
         43   ss << "             #dir2srcs for pkg-srcs file" << std::endl;
         44   ss << "         or" << std::endl;
         45   ss << "             #dir for pkg file." << std::endl << std::endl;
         46 
         47   return ss.str();
         48 }
         49 
         50 DepsOpts::Cmd DepsOpts::parse_command(int argc, char *const *argv) {
         51   if (argc < 2) {
         52     return Cmd::NotCmd;
         53   }
         54 
         55   auto command = std::string{argv[1]};
         56 
         57   if (command == "p") {
         58     return Cmd::GenPkg;
         59   }
         60   if (command == "s") {
         61     return Cmd::GenSrc;
         62   } else if (command == "p2s") {
         63     return Cmd::GenPkg2Srcs;
         64   } else if (command == "p2p") {
         65     return Cmd::GenPkg2Pkg;
         66   } else if (command == "a") {
         67     return Cmd::GenArch;
         68   } else if (command == "a2pu") {
         69     return Cmd::GenPlantUml;
         70   } else if (command == "cyc") {
         71     return Cmd::GenCyclic;
         72   } else if (command == "h" || command == "help" || command == "-h" ||
         73              command == "--help") {
         74     return Cmd::Help;
         75   }
         76 
         77   return Cmd::NotCmd;
         78 }
         79 
         80 bool DepsOpts::parse_opt(int opt_char, DepsOpts::DepsOptsData &data) noexcept {
         81   switch (opt_char) {
         82   case 'i':
         83     data.in = optarg;
         84     return true;
         85   case 'e':
         86     data.exclude = optarg;
         87     return true;
         88   case 'o':
         89     data.out = optarg;
         90     return true;
         91   case 'l':
         92     data.log = optarg;
         93     return true;
         94   case 'R':
         95     data.recursive = true;
         96     return true;
         97   case 's':
         98     data.src_as_pkg = true;
         99     return true;
        100   case 'h':
        101     data.cmd = Cmd::Help;
        102     return false;
        103   default:
        104     return false;
        105   }
        106 }
        107 
        108 DepsOpts::DepsOptsData DepsOpts::parse(int argc, char *const *argv) {
        109   DepsOptsData data{parse_command(argc, argv)};
        110 
        111   if (data.cmd == Cmd::NotCmd || data.cmd == Cmd::Help) {
        112     return data;
        113   }
        114 
        115   optind = 2;
        116   static struct option const opts[] = {{"in", required_argument, 0, 'i'},
        117                                        {"out", required_argument, 0, 'o'},
        118                                        {"exclude", required_argument, 0, 'e'},
        119                                        {"recursive", no_argument, 0, 'R'},
        120                                        {"src_as_pkg", no_argument, 0, 's'},
        121                                        {"log", required_argument, 0, 'l'},
        122                                        {"help", no_argument, 0, 'h'},
        123                                        {0, 0, 0, 0}};
        124 
        125   for (;;) {
        126     auto opt_char = getopt_long(argc, argv, "i:o:e:l:Rsh", opts, nullptr);
        127 
        128     if (!parse_opt(opt_char, data)) {
        129       break;
        130     }
        131   }
        132 
        133   if (optind < argc) {
        134     while (optind < argc) {
        135       data.dirs.emplace_back(FileUtils::NormalizeLexically(argv[optind++]));
        136     }
        137   }
        138 
        139   return data;
        140 }
        141 
        142 namespace {
        143 std::string to_string_cmd(DepsOpts::Cmd cmd) {
        144   switch (cmd) {
        145   case DepsOpts::Cmd::GenPkg:
        146     return "GenPkg";
        147   case DepsOpts::Cmd::GenSrc:
        148     return "GenSrc";
        149   case DepsOpts::Cmd::GenPkg2Srcs:
        150     return "GenPkg2Srcs";
        151   case DepsOpts::Cmd::GenPkg2Pkg:
        152     return "GenPkg2Pkg";
        153   case DepsOpts::Cmd::GenPlantUml:
        154     return "GenPlantUml";
        155   case DepsOpts::Cmd::GenCyclic:
        156     return "GenCyclic";
        157   case DepsOpts::Cmd::Help:
        158     return "Help";
        159   case DepsOpts::Cmd::NotCmd:
        160   default:
        161     return "NotCmd";
        162   }
        163 }
        164 } // namespace
        165 
        166 std::string ToStringDepsOpts(DepsOpts const &deps_opts,
        167                              std::string_view indent) {
        168   auto ss = std::ostringstream{};
        169   char const cmd[] = "cmd       : ";
        170   auto const indent2 =
        171       std::string(Nstd::ArrayLength(cmd) - 1, ' ') + std::string{indent};
        172 
        173   ss << std::boolalpha;
        174 
        175   ss << indent << cmd << to_string_cmd(deps_opts.GetCmd()) << std::endl;
        176   ss << indent << "in        : " << deps_opts.In() << std::endl;
        177   ss << indent << "out       : " << deps_opts.Out() << std::endl;
        178   ss << indent << "recursive : " << deps_opts.IsRecursive() << std::endl;
        179   ss << indent << "src_as_pkg: " << deps_opts.IsSrcPkg() << std::endl;
        180   ss << indent << "log       : " << deps_opts.Log() << std::endl;
        181   ss << indent << "dirs      : "
        182      << FileUtils::ToStringPaths(deps_opts.Dirs(), "\n" + indent2) << std::endl;
        183   ss << indent << "exclude   : " << deps_opts.Exclude() << std::endl;
        184   ss << indent << "parsed    : " << !!deps_opts;
        185 
        186   return ss.str();
        187 }
        188 } // namespace App
```

### example/deps/app/src/deps_opts.h <a id="SS_3_1_2"></a>
```cpp
          1 #pragma once
          2 #include <ostream>
          3 
          4 #include "file_utils/path_utils.h"
          5 
          6 namespace App {
          7 class DepsOpts {
          8 public:
          9   enum class Cmd {
         10     GenPkg,
         11     GenSrc,
         12     GenPkg2Srcs,
         13     GenPkg2Pkg,
         14     GenArch,
         15     GenPlantUml,
         16     GenCyclic,
         17     Help,
         18     NotCmd,
         19   };
         20   explicit DepsOpts(int argc, char *const *argv) : data_{parse(argc, argv)} {}
         21   static std::string Help();
         22 
         23   Cmd GetCmd() const noexcept { return data_.cmd; }
         24   std::string const &In() const noexcept { return data_.in; }
         25   std::string const &Out() const noexcept { return data_.out; }
         26   std::string const &Log() const noexcept { return data_.log; }
         27   bool IsRecursive() const noexcept { return data_.recursive; }
         28   bool IsSrcPkg() const noexcept { return data_.src_as_pkg; }
         29   FileUtils::Paths_t const &Dirs() const noexcept { return data_.dirs; }
         30   std::string const &Exclude() const noexcept { return data_.exclude; }
         31 
         32   explicit operator bool() const { return data_.cmd != Cmd::NotCmd; }
         33 
         34 private:
         35   struct DepsOptsData {
         36     DepsOptsData(Cmd cmd_arg) noexcept : cmd{cmd_arg} {}
         37     Cmd cmd;
         38     std::string in{};
         39     std::string out{};
         40     std::string log{};
         41     FileUtils::Paths_t dirs{};
         42     std::string exclude{};
         43     bool recursive{false};
         44     bool src_as_pkg{false};
         45   };
         46   DepsOptsData const data_;
         47 
         48   static DepsOptsData parse(int argc, char *const *argv);
         49   static Cmd parse_command(int argc, char *const *argv);
         50   static bool parse_opt(int opt_char, DepsOptsData &data) noexcept;
         51 };
         52 
         53 // @@@ sample begin 0:0
         54 
         55 std::string ToStringDepsOpts(DepsOpts const &deps_opts,
         56                              std::string_view indent = "");
         57 inline std::ostream &operator<<(std::ostream &os, DepsOpts const &opts) {
         58   return os << ToStringDepsOpts(opts);
         59 }
         60 // @@@ sample end
         61 } // namespace App
```

### example/deps/app/src/main.cpp <a id="SS_3_1_3"></a>
```cpp
          1 #include <cassert>
          2 #include <fstream>
          3 #include <iostream>
          4 #include <stdexcept>
          5 
          6 #include "dependency/deps_scenario.h"
          7 #include "deps_opts.h"
          8 #include "logging/logger.h"
          9 
         10 namespace {
         11 
         12 class OStreamSelector {
         13 public:
         14   explicit OStreamSelector(std::string const &out) : os_{select(out, out_f_)} {}
         15   std::ostream &OStream() noexcept { return os_; }
         16 
         17 private:
         18   std::ofstream out_f_{};
         19   std::ostream &os_;
         20 
         21   static std::ostream &select(std::string const &out, std::ofstream &out_f) {
         22     if (out.size()) {
         23       out_f.open(out);
         24       assert(out_f);
         25       return out_f;
         26     } else {
         27       return std::cout;
         28     }
         29   }
         30 };
         31 
         32 class ScenarioGeneratorNop : public Dependency::ScenarioGenerator {
         33 public:
         34   explicit ScenarioGeneratorNop(bool no_error) : no_error_{no_error} {}
         35   virtual bool Output(std::ostream &) const noexcept override {
         36     return no_error_;
         37   }
         38 
         39 private:
         40   bool no_error_;
         41 };
         42 
         43 // @@@ sample begin 0:0
         44 std::unique_ptr<Dependency::ScenarioGenerator>
         45 gen_scenario(App::DepsOpts const &opt) try {
         46   using namespace Dependency;
         47 
         48   switch (opt.GetCmd()) {
         49   case App::DepsOpts::Cmd::GenPkg:
         50     LOGGER("start GenPkg");
         51     return std::make_unique<PkgGenerator>(opt.In(), opt.IsRecursive(),
         52                                           opt.Dirs(), opt.Exclude());
         53   case App::DepsOpts::Cmd::GenSrc:
         54     LOGGER("start GenPkg");
         55     return std::make_unique<SrcsGenerator>(opt.In(), opt.IsRecursive(),
         56                                            opt.Dirs(), opt.Exclude());
         57   // @@@ ignore begin
         58   case App::DepsOpts::Cmd::GenPkg2Srcs:
         59     LOGGER("start GenPkg2Srcs");
         60     return std::make_unique<Pkg2SrcsGenerator>(
         61         opt.In(), opt.IsRecursive(), opt.IsSrcPkg(), opt.Dirs(), opt.Exclude());
         62   case App::DepsOpts::Cmd::GenPkg2Pkg:
         63     LOGGER("start GenPkg2Pkg");
         64     return std::make_unique<Pkg2PkgGenerator>(
         65         opt.In(), opt.IsRecursive(), opt.IsSrcPkg(), opt.Dirs(), opt.Exclude());
         66   case App::DepsOpts::Cmd::GenArch:
         67     LOGGER("start GenArch");
         68     return std::make_unique<ArchGenerator>(opt.In());
         69   case App::DepsOpts::Cmd::GenPlantUml:
         70     LOGGER("start GenPlantUml");
         71     return std::make_unique<Arch2PUmlGenerator>(opt.In());
         72   case App::DepsOpts::Cmd::GenCyclic:
         73     LOGGER("start GenCyclic");
         74     return std::make_unique<CyclicGenerator>(opt.In());
         75   case App::DepsOpts::Cmd::Help:
         76     std::cout << App::DepsOpts::Help() << std::endl;
         77     return std::make_unique<ScenarioGeneratorNop>(true);
         78   case App::DepsOpts::Cmd::NotCmd:
         79   default:
         80     std::cout << App::DepsOpts::Help() << std::endl;
         81     return std::make_unique<ScenarioGeneratorNop>(false);
         82     // @@@ ignore end
         83   }
         84 } catch (std::runtime_error const &e) {
         85   LOGGER("error occured:", e.what());
         86 
         87   std::cerr << e.what() << std::endl;
         88 
         89   return std::make_unique<ScenarioGeneratorNop>(false);
         90 }
         91 
         92 // @@@ ignore begin
         93 catch (...) {
         94   LOGGER("unknown error occured:");
         95 
         96   return std::make_unique<ScenarioGeneratorNop>(false);
         97 }
         98 } // namespace
         99 // @@@ ignore end
        100 
        101 int main(int argc, char *argv[]) {
        102   App::DepsOpts d_opt{argc, argv};
        103 
        104   LOGGER_INIT(d_opt.Log() == "-" ? nullptr : d_opt.Log().c_str());
        105 
        106   LOGGER("Options", '\n', d_opt);
        107 
        108   auto out_sel = OStreamSelector{d_opt.Out()};
        109   auto exit_code = gen_scenario(d_opt)->Output(out_sel.OStream()) ? 0 : -1;
        110 
        111   LOGGER("Exit", exit_code);
        112 
        113   return exit_code;
        114 }
        115 // @@@ sample end
```

### example/deps/app/ut/deps_opts_ut.cpp <a id="SS_3_1_4"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "deps_opts.h"
          4 #include "lib/nstd.h"
          5 
          6 namespace App {
          7 namespace {
          8 
          9 TEST(deps_args, DepsOpts) {
         10   using FileUtils::Paths_t;
         11 
         12   char prog[] = "prog";
         13   char cmd_p[] = "p";
         14   char cmd_s[] = "s";
         15   char cmd_p2s[] = "p2s";
         16   char cmd_p2p[] = "p2p";
         17   char cmd_a[] = "a";
         18   char cmd_a2pu[] = "a2pu";
         19   char cmd_help[] = "help";
         20   char cmd_dd_help[] = "--help";
         21   char cmd_h[] = "h";
         22   char cmd_d_h[] = "-h";
         23   char cmd_unknown[] = "unknown";
         24   char opt_in[] = "--in";
         25   char opt_in_arg[] = "in-file";
         26   char opt_out[] = "--out";
         27   char opt_out_arg[] = "out-file";
         28   char opt_e[] = "-e";
         29   char opt_exclude[] = "--exclude";
         30   char opt_e_arg[] = "pattern.*";
         31   char opt_recursive[] = "--recursive";
         32   char opt_src_pkg[] = "--src_as_pkg";
         33   char opt_log[] = "--log";
         34   char opt_log_arg[] = "log-file";
         35   char opt_log_dash[] = "-";
         36   char opt_R[] = "-R";
         37   char opt_s[] = "-s";
         38   char opt_help[] = "--help";
         39   char opt_h[] = "-h";
         40   char dir0[] = "dir0";
         41   char dir1[] = "dir1";
         42   char dir2[] = "dir2";
         43 
         44   {
         45     char *const argv[]{prog,        cmd_p, opt_recursive, opt_out,
         46                        opt_out_arg, dir0,  dir1,          dir2};
         47 
         48     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         49 
         50     ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
         51     ASSERT_EQ("", d_opt.In());
         52     ASSERT_EQ(opt_out_arg, d_opt.Out());
         53     ASSERT_TRUE(d_opt.IsRecursive());
         54     ASSERT_EQ((Paths_t{dir0, dir1, dir2}), d_opt.Dirs());
         55     ASSERT_TRUE(d_opt);
         56   }
         57   {
         58     char *const argv[] = {prog,        cmd_p, opt_src_pkg, opt_out,
         59                           opt_out_arg, dir0,  dir1,        dir2};
         60 
         61     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         62 
         63     ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
         64     ASSERT_EQ("", d_opt.In());
         65     ASSERT_EQ(opt_out_arg, d_opt.Out());
         66     ASSERT_FALSE(d_opt.IsRecursive());
         67     ASSERT_TRUE(d_opt.IsSrcPkg());
         68     ASSERT_EQ((Paths_t{dir0, dir1, dir2}), d_opt.Dirs());
         69     ASSERT_TRUE(d_opt);
         70   }
         71   {
         72     char *const argv[]{prog,        cmd_s, opt_src_pkg, opt_out,
         73                        opt_out_arg, dir0,  dir1,        dir2};
         74 
         75     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         76 
         77     ASSERT_EQ(DepsOpts::Cmd::GenSrc, d_opt.GetCmd());
         78     ASSERT_EQ("", d_opt.In());
         79     ASSERT_EQ(opt_out_arg, d_opt.Out());
         80     ASSERT_FALSE(d_opt.IsRecursive());
         81     ASSERT_TRUE(d_opt.IsSrcPkg());
         82     ASSERT_EQ((Paths_t{dir0, dir1, dir2}), d_opt.Dirs());
         83     ASSERT_TRUE(d_opt);
         84   }
         85   {
         86     char *const argv[]{prog,       cmd_p2s,     opt_R,     opt_in,
         87                        opt_in_arg, opt_exclude, opt_e_arg, dir0};
         88 
         89     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         90 
         91     ASSERT_EQ(DepsOpts::Cmd::GenPkg2Srcs, d_opt.GetCmd());
         92     ASSERT_EQ(opt_in_arg, d_opt.In());
         93     ASSERT_EQ("", d_opt.Out());
         94     ASSERT_TRUE(d_opt.IsRecursive());
         95     ASSERT_EQ((Paths_t{dir0}), d_opt.Dirs());
         96     ASSERT_TRUE(d_opt);
         97     ASSERT_EQ(opt_e_arg, d_opt.Exclude());
         98   }
         99   {
        100     char *const argv[]{prog,       cmd_p2s, opt_s,     opt_in,
        101                        opt_in_arg, opt_e,   opt_e_arg, dir0};
        102 
        103     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        104 
        105     ASSERT_EQ(DepsOpts::Cmd::GenPkg2Srcs, d_opt.GetCmd());
        106     ASSERT_EQ(opt_in_arg, d_opt.In());
        107     ASSERT_EQ("", d_opt.Out());
        108     ASSERT_FALSE(d_opt.IsRecursive());
        109     ASSERT_TRUE(d_opt.IsSrcPkg());
        110     ASSERT_EQ((Paths_t{dir0}), d_opt.Dirs());
        111     ASSERT_TRUE(d_opt);
        112     ASSERT_EQ(opt_e_arg, d_opt.Exclude());
        113   }
        114   {
        115     char *const argv[]{prog, cmd_p2p, opt_in, opt_in_arg, opt_out, opt_out_arg};
        116 
        117     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        118 
        119     ASSERT_EQ(DepsOpts::Cmd::GenPkg2Pkg, d_opt.GetCmd());
        120     ASSERT_EQ(opt_in_arg, d_opt.In());
        121     ASSERT_EQ(opt_out_arg, d_opt.Out());
        122     ASSERT_FALSE(d_opt.IsRecursive());
        123     ASSERT_EQ(Paths_t{}, d_opt.Dirs());
        124     ASSERT_TRUE(d_opt);
        125   }
        126   {
        127     char *const argv[]{prog, cmd_a, opt_in, opt_in_arg, opt_out, opt_out_arg};
        128 
        129     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        130 
        131     ASSERT_EQ(DepsOpts::Cmd::GenArch, d_opt.GetCmd());
        132     ASSERT_EQ(opt_in_arg, d_opt.In());
        133     ASSERT_EQ(opt_out_arg, d_opt.Out());
        134     ASSERT_FALSE(d_opt.IsRecursive());
        135     ASSERT_EQ(Paths_t{}, d_opt.Dirs());
        136     ASSERT_TRUE(d_opt);
        137   }
        138   {
        139     char *const argv[]{prog,       cmd_a2pu, opt_in,
        140                        opt_in_arg, opt_out,  opt_out_arg};
        141 
        142     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        143 
        144     ASSERT_EQ(DepsOpts::Cmd::GenPlantUml, d_opt.GetCmd());
        145     ASSERT_EQ(opt_in_arg, d_opt.In());
        146     ASSERT_EQ(opt_out_arg, d_opt.Out());
        147     ASSERT_FALSE(d_opt.IsRecursive());
        148     ASSERT_EQ(Paths_t{}, d_opt.Dirs());
        149     ASSERT_TRUE(d_opt);
        150   }
        151   {
        152     char *const argv[]{prog, cmd_help};
        153 
        154     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        155 
        156     ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        157     ASSERT_TRUE(d_opt);
        158   }
        159   {
        160     char *const argv[]{prog, cmd_dd_help};
        161 
        162     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        163 
        164     ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        165     ASSERT_TRUE(d_opt);
        166   }
        167   {
        168     char *const argv[]{prog, cmd_h};
        169 
        170     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        171 
        172     ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        173     ASSERT_TRUE(d_opt);
        174   }
        175   {
        176     char *const argv[]{prog, cmd_d_h};
        177 
        178     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        179 
        180     ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        181     ASSERT_TRUE(d_opt);
        182   }
        183   {
        184     char *const argv[]{prog, cmd_unknown};
        185 
        186     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        187 
        188     ASSERT_EQ(DepsOpts::Cmd::NotCmd, d_opt.GetCmd());
        189     ASSERT_FALSE(d_opt);
        190   }
        191   {
        192     char *const argv[]{prog,    cmd_p,       opt_recursive,
        193                        opt_out, opt_out_arg, opt_help};
        194 
        195     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        196 
        197     ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        198     ASSERT_TRUE(d_opt);
        199   }
        200   {
        201     char *const argv[]{prog, cmd_p, opt_recursive, opt_out, opt_out_arg, opt_h};
        202 
        203     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        204 
        205     ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        206     ASSERT_TRUE(d_opt);
        207   }
        208   {
        209     char *const argv[]{prog, cmd_p, opt_log, opt_log_arg, opt_out, opt_out_arg};
        210 
        211     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        212 
        213     ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
        214     ASSERT_EQ(opt_log_arg, d_opt.Log());
        215     ASSERT_EQ(opt_out_arg, d_opt.Out());
        216     ASSERT_TRUE(d_opt);
        217   }
        218   {
        219     char *const argv[]{prog, cmd_p, opt_log, opt_log_dash, opt_in, opt_in_arg};
        220 
        221     auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        222 
        223     ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
        224     ASSERT_EQ(opt_log_dash, d_opt.Log());
        225     ASSERT_EQ(opt_in_arg, d_opt.In());
        226     ASSERT_TRUE(d_opt);
        227   }
        228 }
        229 } // namespace
        230 } // namespace App
```

### example/deps/dependency/h/dependency/deps_scenario.h <a id="SS_3_1_5"></a>
```cpp
          1 #pragma once
          2 #include <memory>
          3 #include <string>
          4 #include <vector>
          5 
          6 #include "file_utils/path_utils.h"
          7 
          8 namespace Dependency {
          9 
         10 class ScenarioGenerator {
         11 public:
         12   virtual bool Output(std::ostream &os) const = 0;
         13   virtual ~ScenarioGenerator() {}
         14 };
         15 
         16 class PkgGenerator : public ScenarioGenerator {
         17 public:
         18   explicit PkgGenerator(std::string const &in, bool recursive,
         19                         FileUtils::Paths_t const &dirs_opt,
         20                         std::string const &pattern);
         21   virtual bool Output(std::ostream &os) const override;
         22 
         23 private:
         24   FileUtils::Paths_t const dirs_;
         25 };
         26 
         27 class SrcsGenerator : public ScenarioGenerator {
         28 public:
         29   explicit SrcsGenerator(std::string const &in, bool recursive,
         30                          FileUtils::Paths_t const &dirs_opt,
         31                          std::string const &pattern);
         32   virtual bool Output(std::ostream &os) const override;
         33 
         34 private:
         35   FileUtils::Paths_t const dirs_;
         36 };
         37 
         38 class Pkg2SrcsGenerator : public ScenarioGenerator {
         39 public:
         40   explicit Pkg2SrcsGenerator(std::string const &in, bool recursive,
         41                              bool src_as_pkg,
         42                              FileUtils::Paths_t const &dirs_opt,
         43                              std::string const &pattern);
         44   virtual bool Output(std::ostream &os) const override;
         45 
         46 private:
         47   FileUtils::Dirs2Srcs_t const dirs2srcs_;
         48 };
         49 
         50 class Pkg2PkgGenerator : public ScenarioGenerator {
         51 public:
         52   explicit Pkg2PkgGenerator(std::string const &in, bool recursive,
         53                             bool src_as_pkg, FileUtils::Paths_t const &dirs_opt,
         54                             std::string const &pattern);
         55   virtual bool Output(std::ostream &os) const override;
         56 
         57 private:
         58   FileUtils::Dirs2Srcs_t const dirs2srcs_;
         59 };
         60 
         61 class ArchGenerator : public ScenarioGenerator {
         62 public:
         63   explicit ArchGenerator(std::string const &in);
         64   virtual bool Output(std::ostream &os) const override;
         65   ~ArchGenerator();
         66 
         67 protected:
         68   struct Impl;
         69   std::unique_ptr<Impl> impl_;
         70 };
         71 
         72 class Arch2PUmlGenerator : public ArchGenerator {
         73 public:
         74   explicit Arch2PUmlGenerator(std::string const &in);
         75   virtual bool Output(std::ostream &os) const override;
         76 };
         77 
         78 class CyclicGenerator : public ArchGenerator {
         79 public:
         80   explicit CyclicGenerator(std::string const &in);
         81   virtual bool Output(std::ostream &os) const override;
         82 
         83 private:
         84   bool has_cyclic_dep_;
         85 };
         86 } // namespace Dependency
```

### example/deps/dependency/src/arch_pkg.cpp <a id="SS_3_1_6"></a>
```cpp
          1 #include <cassert>
          2 #include <sstream>
          3 
          4 #include "arch_pkg.h"
          5 #include "lib/nstd.h"
          6 
          7 namespace Dependency {
          8 
          9 void ArchPkg::set_cyclic(ArchPkg const *pkg, bool is_cyclic) const {
         10   assert(std::count(depend_on_.cbegin(), depend_on_.cend(), pkg) != 0);
         11   assert(cyclic_.count(pkg) == 0 || cyclic_[pkg] == is_cyclic);
         12 
         13   cyclic_.insert(std::make_pair(pkg, is_cyclic));
         14 }
         15 
         16 bool ArchPkg::is_cyclic(ArchPkgs_t &history, size_t depth) const {
         17   if (++depth > max_depth_) {
         18     std::cerr << "too deep dependency:" << name_ << std::endl;
         19     return true;
         20   }
         21 
         22   auto const it = find(history.cbegin(), history.cend(), this);
         23 
         24   if (it != history.cend()) { // 循環検出
         25     for (auto it2 = it; it2 != history.cend(); ++it2) {
         26       auto next = (std::next(it2) == history.cend()) ? it : std::next(it2);
         27       (*it2)->set_cyclic(*next, true);
         28     }
         29 
         30     // it == history.cbegin()ならば、一番上からの循環 A->B->C->...->A
         31     // it != history.cbegin()ならば、上記以外の循環 A->B->C->...->B
         32     return it == history.cbegin();
         33   }
         34 
         35   auto gs = Nstd::ScopedGuard{[&history] { history.pop_back(); }};
         36   history.push_back(this);
         37 
         38   for (ArchPkg const *pkg : depend_on_) {
         39     if (pkg->is_cyclic(history, depth)) {
         40       return true;
         41     }
         42   }
         43 
         44   return false;
         45 }
         46 
         47 bool ArchPkg::IsCyclic(ArchPkg const &pkg) const {
         48   if (std::count(depend_on_.cbegin(), depend_on_.cend(), &pkg) == 0) {
         49     return false;
         50   }
         51 
         52   if (cyclic_.count(&pkg) == 0) {
         53     ArchPkgs_t history{this};
         54     set_cyclic(&pkg, pkg.is_cyclic(history, 0));
         55   }
         56 
         57   assert(cyclic_.count(&pkg) != 0);
         58 
         59   return cyclic_[&pkg];
         60 }
         61 
         62 bool ArchPkg::IsCyclic() const noexcept {
         63   for (ArchPkg const *pkg : DependOn()) {
         64     if (IsCyclic(*pkg)) {
         65       return true;
         66     }
         67   }
         68 
         69   return false;
         70 }
         71 
         72 ArchPkg::Map_Path_ArchPkg_t
         73 ArchPkg::build_depend_on(DepRelation const &dep_rel,
         74                          Map_Path_ArchPkg_t &&pkg_all) {
         75   auto const a_path = FileUtils::Path_t(dep_rel.PackageA);
         76   if (pkg_all.count(a_path) == 0) {
         77     pkg_all.insert(std::make_pair(a_path, std::make_unique<ArchPkg>(a_path)));
         78   }
         79 
         80   auto const b_path = FileUtils::Path_t(dep_rel.PackageB);
         81   if (pkg_all.count(b_path) == 0) {
         82     pkg_all.insert(std::make_pair(b_path, std::make_unique<ArchPkg>(b_path)));
         83   }
         84 
         85   ArchPkgPtr_t &a_ptr = pkg_all.at(a_path);
         86   ArchPkgPtr_t &b_ptr = pkg_all.at(b_path);
         87 
         88   if (dep_rel.CountAtoB != 0) {
         89     a_ptr->depend_on_.push_back(b_ptr.get());
         90   }
         91   if (dep_rel.CountBtoA != 0) {
         92     b_ptr->depend_on_.push_back(a_ptr.get());
         93   }
         94 
         95   return std::move(pkg_all);
         96 }
         97 
         98 Arch_t ArchPkg::build_children(Map_Path_ArchPkg_t &&pkg_all) {
         99   auto cache = std::map<FileUtils::Path_t, ArchPkg *>{};
        100   auto top = Arch_t{};
        101 
        102   for (auto &[path, pkg] : pkg_all) { // C++17 style
        103 
        104     auto const parent_name = path.parent_path();
        105     cache.insert(std::make_pair(path, pkg.get()));
        106 
        107     if (pkg_all.count(parent_name) == 0) {
        108       top.emplace_back(std::move(pkg));
        109     } else {
        110       ArchPkg *parent = cache.count(parent_name) != 0
        111                             ? cache.at(parent_name)
        112                             : pkg_all.at(parent_name).get();
        113 
        114       pkg->parent_ = parent;
        115       parent->children_.emplace_back(std::move(pkg));
        116     }
        117   }
        118 
        119   return top;
        120 }
        121 
        122 Arch_t ArchPkg::GenArch(DepRels_t const &dep_rels) {
        123   auto pkg_all = std::map<FileUtils::Path_t, ArchPkgPtr_t>{};
        124 
        125   for (auto const &d : dep_rels) {
        126     pkg_all = build_depend_on(d, std::move(pkg_all));
        127   }
        128 
        129   auto top = Arch_t{build_children(std::move(pkg_all))};
        130 
        131   return top;
        132 }
        133 
        134 std::string ArchPkg::make_full_name(ArchPkg const &pkg) {
        135   if (pkg.Parent()) {
        136     return make_full_name(*pkg.Parent()) + "/" + pkg.Name();
        137   } else {
        138     return pkg.Name();
        139   }
        140 }
        141 
        142 ArchPkg const *FindArchPkgByName(Arch_t const &arch,
        143                                  std::string_view pkg_name) noexcept {
        144   for (ArchPkgPtr_t const &pkg_ptr : arch) {
        145     if (pkg_ptr->Name() == pkg_name) {
        146       return pkg_ptr.get();
        147     } else {
        148       ArchPkg const *pkg_found =
        149           FindArchPkgByName(pkg_ptr->Children(), pkg_name);
        150       if (pkg_found) {
        151         return pkg_found;
        152       }
        153     }
        154   }
        155   return nullptr;
        156 }
        157 
        158 ArchPkg const *FindArchPkgByFullName(Arch_t const &arch,
        159                                      std::string_view full_name) noexcept {
        160   for (ArchPkgPtr_t const &pkg_ptr : arch) {
        161     if (pkg_ptr->FullName() == full_name) {
        162       return pkg_ptr.get();
        163     } else {
        164       ArchPkg const *pkg_found =
        165           FindArchPkgByFullName(pkg_ptr->Children(), full_name);
        166       if (pkg_found) {
        167         return pkg_found;
        168       }
        169     }
        170   }
        171   return nullptr;
        172 }
        173 
        174 namespace {
        175 
        176 std::string unique_str_name(std::string const &full_name) {
        177   auto ret = Nstd::Replace(full_name, "/", "___");
        178   return Nstd::Replace(ret, "-", "_");
        179 }
        180 
        181 std::string_view cyclic_str(ArchPkg const &pkg) noexcept {
        182   if (pkg.IsCyclic()) {
        183     return ":CYCLIC";
        184   }
        185 
        186   return "";
        187 }
        188 
        189 std::string to_string_depend_on(ArchPkg const &pkg_top, uint32_t indent) {
        190   auto ss = std::ostringstream{};
        191   auto indent_str = std::string(indent, ' ');
        192 
        193   auto first = true;
        194 
        195   for (ArchPkg const *pkg : pkg_top.DependOn()) {
        196     if (!std::exchange(first, false)) {
        197       ss << std::endl;
        198     }
        199 
        200     ss << indent_str << pkg->Name();
        201 
        202     if (pkg_top.IsCyclic(*pkg)) {
        203       ss << " : CYCLIC";
        204     } else {
        205       ss << " : STRAIGHT";
        206     }
        207   }
        208 
        209   return ss.str();
        210 }
        211 
        212 std::string to_string_pkg(ArchPkg const &arch_pkg, uint32_t indent) {
        213   static auto const top = std::string{"TOP"};
        214   auto ss = std::ostringstream{};
        215   auto indent_str = std::string(indent, ' ');
        216 
        217   auto package = "package  :";
        218   auto full = "fullname :";
        219   auto parent = "parent   :";
        220   auto children = "children : {";
        221   auto depend_on = "depend_on: {";
        222 
        223   constexpr auto next_indent = 4U;
        224 
        225   ss << indent_str << package << arch_pkg.Name() << cyclic_str(arch_pkg)
        226      << std::endl;
        227   ss << indent_str << full << arch_pkg.FullName() << std::endl;
        228   ss << indent_str << parent
        229      << (arch_pkg.Parent() ? arch_pkg.Parent()->Name() : top) << std::endl;
        230 
        231   ss << indent_str << depend_on;
        232   if (arch_pkg.DependOn().size() != 0) {
        233     ss << std::endl;
        234     ss << to_string_depend_on(arch_pkg, indent + next_indent) << std::endl;
        235     ss << indent_str << "}" << std::endl;
        236   } else {
        237     ss << " }" << std::endl;
        238   }
        239 
        240   ss << indent_str << children;
        241   if (arch_pkg.Children().size() != 0) {
        242     ss << std::endl;
        243     ss << ToStringArch(arch_pkg.Children(), indent + next_indent) << std::endl;
        244     ss << indent_str << "}";
        245   } else {
        246     ss << " }";
        247   }
        248 
        249   return ss.str();
        250 }
        251 } // namespace
        252 
        253 std::string ToStringArch(Arch_t const &arch, uint32_t indent) {
        254   auto ss = std::ostringstream{};
        255   auto first = true;
        256 
        257   for (auto const &pkg : arch) {
        258     if (!std::exchange(first, false)) {
        259       ss << std::endl << std::endl;
        260     }
        261     ss << to_string_pkg(*pkg, indent);
        262   }
        263 
        264   return ss.str();
        265 }
        266 
        267 namespace {
        268 std::string to_pu_rectangle(ArchPkg const &pkg, uint32_t indent) {
        269   auto ss = std::ostringstream{};
        270   auto indent_str = std::string(indent, ' ');
        271 
        272   ss << indent_str << "rectangle \"" << pkg.Name() << "\" as "
        273      << unique_str_name(pkg.FullName());
        274 
        275   if (pkg.Children().size() != 0) {
        276     ss << " {" << std::endl;
        277     ss << ToPlantUML_Rectangle(pkg.Children(), indent + 4);
        278     ss << std::endl << indent_str << "}";
        279   }
        280 
        281   return ss.str();
        282 }
        283 } // namespace
        284 
        285 std::string ToPlantUML_Rectangle(Arch_t const &arch, uint32_t indent) {
        286   auto ss = std::ostringstream{};
        287   auto first = true;
        288 
        289   for (auto const &pkg : arch) {
        290     if (!std::exchange(first, false)) {
        291       ss << std::endl;
        292     }
        293     ss << to_pu_rectangle(*pkg, indent);
        294   }
        295 
        296   return ss.str();
        297 }
        298 
        299 namespace {
        300 
        301 // 単方向依存のみ
        302 bool dep_is_cyclic(std::string const &from, std::string const &to,
        303                    Arch_t const &arch) noexcept {
        304   ArchPkg const *pkg_from = FindArchPkgByFullName(arch, from);
        305   ArchPkg const *pkg_to = FindArchPkgByFullName(arch, to);
        306 
        307   assert(pkg_from != nullptr);
        308   assert(pkg_to != nullptr);
        309 
        310   return pkg_from->IsCyclic(*pkg_to);
        311 }
        312 
        313 std::string_view pu_link_color(std::string const &from, std::string const &to,
        314                                Arch_t const &arch) noexcept {
        315   return dep_is_cyclic(from, to, arch) ? "orange" : "green";
        316 }
        317 
        318 std::string to_pu_rectangle(Arch_t const &arch, DepRelation const &dep_rel) {
        319   auto ss = std::ostringstream{};
        320   auto a = unique_str_name(dep_rel.PackageA);
        321   auto b = unique_str_name(dep_rel.PackageB);
        322 
        323   if (dep_rel.CountAtoB != 0) {
        324     ss << a << " \"" << dep_rel.CountAtoB << "\" ";
        325     if (dep_rel.CountBtoA != 0) {
        326       ss << "<-[#red]-> \"" << dep_rel.CountBtoA << "\" " << b;
        327     } else {
        328       ss << "-[#" << pu_link_color(dep_rel.PackageA, dep_rel.PackageB, arch)
        329          << "]-> " << b;
        330     }
        331   } else if (dep_rel.CountBtoA != 0) {
        332     ss << b << " \"" << dep_rel.CountBtoA << "\" -[#"
        333        << pu_link_color(dep_rel.PackageB, dep_rel.PackageA, arch) << "]-> "
        334        << a;
        335   }
        336 
        337   return ss.str();
        338 }
        339 } // namespace
        340 
        341 bool HasCyclicDeps(Arch_t const &arch, DepRels_t const &dep_rels) noexcept {
        342   for (auto const &dep : dep_rels) {
        343     if (dep.CountAtoB != 0) {
        344       if (dep.CountBtoA != 0) {
        345         return true;
        346       } else {
        347         if (dep_is_cyclic(dep.PackageA, dep.PackageB, arch)) {
        348           return true;
        349         }
        350       }
        351     } else if (dep.CountBtoA != 0) {
        352       if (dep_is_cyclic(dep.PackageB, dep.PackageA, arch)) {
        353         return true;
        354       }
        355     }
        356   }
        357 
        358   return false;
        359 }
        360 
        361 std::string ToPlantUML_Rectangle(Arch_t const &arch,
        362                                  DepRels_t const &dep_rels) {
        363   auto ss = std::ostringstream{};
        364 
        365   auto first = true;
        366   for (auto const &d : dep_rels) {
        367     auto rel_s = to_pu_rectangle(arch, d);
        368 
        369     if (rel_s.size() != 0) {
        370       if (!std::exchange(first, false)) {
        371         ss << std::endl;
        372       }
        373       ss << rel_s;
        374     }
        375   }
        376   return ss.str();
        377 }
        378 } // namespace Dependency
```

### example/deps/dependency/src/arch_pkg.h <a id="SS_3_1_7"></a>
```cpp
          1 #pragma once
          2 
          3 #include "cpp_deps.h"
          4 #include "file_utils/path_utils.h"
          5 
          6 namespace Dependency {
          7 
          8 class ArchPkg;
          9 using ArchPkgPtr_t = std::unique_ptr<ArchPkg>;
         10 using Arch_t = std::list<ArchPkgPtr_t>;
         11 
         12 using ArchPkgs_t = std::vector<ArchPkg const *>;
         13 
         14 class ArchPkg {
         15 public:
         16   explicit ArchPkg(FileUtils::Path_t const &full_name)
         17       : name_{full_name.filename()}, full_name_{full_name} {}
         18 
         19   std::string const &Name() const noexcept { return name_; }
         20   ArchPkg const *Parent() const noexcept { return parent_; }
         21   Arch_t const &Children() const noexcept { return children_; }
         22   ArchPkgs_t const &DependOn() const noexcept { return depend_on_; }
         23   bool IsCyclic() const noexcept;
         24   bool IsCyclic(ArchPkg const &pkg) const;
         25   std::string const &FullName() const noexcept { return full_name_; }
         26 
         27   ArchPkg(ArchPkg const &) = delete;
         28   ArchPkg &operator=(ArchPkg const &) = delete;
         29 
         30   static Arch_t GenArch(DepRels_t const &deps);
         31 
         32 private:
         33   std::string const name_;
         34   std::string const full_name_{};
         35   ArchPkg const *parent_{};
         36   Arch_t children_{};
         37   ArchPkgs_t depend_on_{};
         38   mutable std::map<ArchPkg const *, bool> cyclic_{};
         39   static constexpr size_t max_depth_{12};
         40 
         41   void set_cyclic(ArchPkg const *pkg, bool is_cyclic) const;
         42 
         43   using Map_Path_ArchPkg_t = std::map<FileUtils::Path_t, ArchPkgPtr_t>;
         44   static Map_Path_ArchPkg_t build_depend_on(DepRelation const &dep_rel,
         45                                             Map_Path_ArchPkg_t &&pkg_all);
         46   static Arch_t build_children(Map_Path_ArchPkg_t &&pkg_all);
         47   static std::string make_full_name(ArchPkg const &pkg);
         48   bool is_cyclic(ArchPkgs_t &history, size_t depth) const;
         49 };
         50 
         51 std::string ToStringArch(Arch_t const &arch, uint32_t indent = 0);
         52 inline std::ostream &operator<<(std::ostream &os, Arch_t const &arch) {
         53   return os << ToStringArch(arch);
         54 }
         55 
         56 std::string ToPlantUML_Rectangle(Arch_t const &arch, uint32_t indent = 0);
         57 std::string ToPlantUML_Rectangle(Arch_t const &arch, DepRels_t const &dep_rels);
         58 bool HasCyclicDeps(Arch_t const &arch, DepRels_t const &dep_rels) noexcept;
         59 
         60 ArchPkg const *FindArchPkgByName(Arch_t const &arch,
         61                                  std::string_view pkg_name) noexcept;
         62 ArchPkg const *FindArchPkgByFullName(Arch_t const &arch,
         63                                      std::string_view full_name) noexcept;
         64 } // namespace Dependency
```

### example/deps/dependency/src/cpp_deps.cpp <a id="SS_3_1_8"></a>
```cpp
          1 #include <algorithm>
          2 #include <cassert>
          3 #include <memory>
          4 #include <sstream>
          5 #include <tuple>
          6 
          7 #include "cpp_deps.h"
          8 #include "cpp_dir.h"
          9 #include "cpp_src.h"
         10 
         11 namespace Dependency {
         12 
         13 std::string ToStringDepRel(DepRelation const &rep_rel) {
         14   auto ss = std::ostringstream{};
         15 
         16   ss << FileUtils::ToStringPath(rep_rel.PackageA) << " -> "
         17      << FileUtils::ToStringPath(rep_rel.PackageB) << " : " << rep_rel.CountAtoB
         18      << " " << FileUtils::ToStringPaths(rep_rel.IncsAtoB, " ") << std::endl;
         19 
         20   ss << FileUtils::ToStringPath(rep_rel.PackageB) << " -> "
         21      << FileUtils::ToStringPath(rep_rel.PackageA) << " : " << rep_rel.CountBtoA
         22      << " " << FileUtils::ToStringPaths(rep_rel.IncsBtoA, " ");
         23 
         24   return ss.str();
         25 }
         26 
         27 std::string ToStringDepRels(DepRels_t const &dep_rels) {
         28   auto ss = std::ostringstream{};
         29 
         30   auto first = true;
         31   for (auto const &dep : dep_rels) {
         32     if (!std::exchange(first, false)) {
         33       ss << std::endl;
         34     }
         35     ss << ToStringDepRel(dep) << std::endl;
         36   }
         37 
         38   return ss.str();
         39 }
         40 
         41 namespace {
         42 DepRelation gen_DepRelation(CppDir const &dirA, CppDir const &dirB) {
         43   auto a_dep = std::pair<uint32_t, FileUtils::Paths_t>{dirA.DependsOn(dirB)};
         44   auto count_from_a = a_dep.first;
         45   auto incs_from_a = std::move(a_dep.second);
         46 
         47   auto b_dep = std::pair<uint32_t, FileUtils::Paths_t>{dirB.DependsOn(dirA)};
         48   auto count_from_b = b_dep.first;
         49   auto incs_from_b = std::move(b_dep.second);
         50 
         51   if (dirA < dirB) {
         52     return DepRelation{dirA.Path(), count_from_a, std::move(incs_from_a),
         53                        dirB.Path(), count_from_b, std::move(incs_from_b)};
         54   } else {
         55     return DepRelation{dirB.Path(), count_from_b, std::move(incs_from_b),
         56                        dirA.Path(), count_from_a, std::move(incs_from_a)};
         57   }
         58 }
         59 } // namespace
         60 
         61 Dir2Dir_t GenDir2Dir(std::string dirA, std::string dirB) {
         62   return dirA < dirB ? std::make_pair(std::move(dirA), std::move(dirB))
         63                      : std::make_pair(std::move(dirB), std::move(dirA));
         64 }
         65 
         66 DepRels_t GenDepRels(CppDirs_t const &cpp_dirs) {
         67   auto ret = DepRels_t{};
         68 
         69   for (auto const &dirA : cpp_dirs) {
         70     for (auto const &dirB : cpp_dirs) {
         71       if (dirA <= dirB) {
         72         continue;
         73       }
         74       ret.emplace_back(gen_DepRelation(dirA, dirB));
         75     }
         76   }
         77 
         78   ret.sort();
         79 
         80   return ret;
         81 }
         82 
         83 DepRels_t::const_iterator FindDepRels(DepRels_t const &dep_rels,
         84                                       std::string const &dirA,
         85                                       std::string const &dirB) noexcept {
         86   assert(dirA != dirB);
         87 
         88   auto dirs = std::minmax(dirA, dirB);
         89 
         90   return std::find_if(
         91       dep_rels.cbegin(), dep_rels.cend(), [&dirs](auto const &d) noexcept {
         92         return d.PackageA == dirs.first && d.PackageB == dirs.second;
         93       });
         94 }
         95 } // namespace Dependency
```

### example/deps/dependency/src/cpp_deps.h <a id="SS_3_1_9"></a>
```cpp
          1 #pragma once
          2 #include <compare>
          3 #include <vector>
          4 
          5 #include "cpp_deps.h"
          6 #include "cpp_dir.h"
          7 #include "file_utils/path_utils.h"
          8 
          9 namespace Dependency {
         10 
         11 struct DepRelation {
         12   explicit DepRelation(std::string package_a, uint32_t count_a2b,
         13                        FileUtils::Paths_t &&incs_a2b, std::string package_b,
         14                        uint32_t count_b2a, FileUtils::Paths_t &&incs_b2a)
         15       : PackageA{std::move(package_a)}, CountAtoB{count_a2b},
         16         IncsAtoB{std::move(incs_a2b)}, PackageB{std::move(package_b)},
         17         CountBtoA{count_b2a}, IncsBtoA{std::move(incs_b2a)} {}
         18 
         19   std::string const PackageA;
         20   uint32_t const CountAtoB;
         21   FileUtils::Paths_t const IncsAtoB;
         22 
         23   std::string const PackageB;
         24   uint32_t const CountBtoA;
         25   FileUtils::Paths_t const IncsBtoA;
         26 
         27   friend bool operator==(DepRelation const &lhs,
         28                          DepRelation const &rhs) noexcept = default;
         29 };
         30 
         31 inline auto operator<=>(DepRelation const &lhs,
         32                         DepRelation const &rhs) noexcept {
         33   // PackageA を比較し、等しくなければその比較結果を返す
         34   if (auto cmp = lhs.PackageA <=> rhs.PackageA; cmp != 0) {
         35     return cmp;
         36   }
         37 
         38   return lhs.PackageB <=> rhs.PackageB; // PackageAが等しければ PackageBを比較
         39 }
         40 
         41 using Dir2Dir_t = std::pair<std::string, std::string>;
         42 using DepRels_t = std::list<DepRelation>;
         43 
         44 std::string ToStringDepRel(DepRelation const &rep_rel);
         45 
         46 inline std::ostream &operator<<(std::ostream &os, DepRelation const &dep_rel) {
         47   return os << ToStringDepRel(dep_rel);
         48 }
         49 
         50 Dir2Dir_t GenDir2Dir(std::string const &dirA, std::string const &dirB);
         51 
         52 std::string ToStringDepRels(DepRels_t const &dep_rels);
         53 inline std::ostream &operator<<(std::ostream &os, DepRels_t const &dep_rels) {
         54   return os << ToStringDepRels(dep_rels);
         55 }
         56 
         57 DepRels_t GenDepRels(CppDirs_t const &dirs);
         58 DepRels_t::const_iterator FindDepRels(DepRels_t const &dep_rels,
         59                                       std::string const &dirA,
         60                                       std::string const &dirB) noexcept;
         61 } // namespace Dependency
```

### example/deps/dependency/src/cpp_dir.cpp <a id="SS_3_1_10"></a>
```cpp
          1 #include <cassert>
          2 #include <sstream>
          3 #include <tuple>
          4 
          5 #include "cpp_dir.h"
          6 #include "cpp_src.h"
          7 #include "lib/nstd.h"
          8 
          9 namespace Dependency {
         10 
         11 bool CppDir::Contains(FileUtils::Path_t const &inc_path) const noexcept {
         12   for (auto const &src : srcs_) {
         13     if (src.Path() == inc_path) {
         14       return true;
         15     }
         16   }
         17 
         18   return false;
         19 }
         20 
         21 std::pair<uint32_t, FileUtils::Paths_t>
         22 CppDir::DependsOn(CppDir const &cpp_pack) const {
         23   auto count = 0U;
         24   auto incs = FileUtils::Paths_t{};
         25 
         26   for (auto const &src : srcs_) {
         27     for (auto const &inc : src.GetIncs()) {
         28       if (cpp_pack.Contains(inc)) {
         29         incs.push_back(inc);
         30         ++count;
         31       }
         32     }
         33   }
         34 
         35   Nstd::SortUnique(incs);
         36 
         37   return {count, std::move(incs)};
         38 }
         39 
         40 CppDirs_t GenCppDirs(FileUtils::Paths_t const &srcs,
         41                      FileUtils::Filename2Path_t const &db) {
         42   auto ret = CppDirs_t{};
         43 
         44   for (auto const &src : srcs) {
         45     auto cpp_src = CppSrc{src, db};
         46     ret.emplace_back(CppDir{cpp_src.Filename(), {cpp_src}});
         47   }
         48 
         49   return ret;
         50 }
         51 
         52 std::string ToStringCppDir(CppDir const &cpp_pack) {
         53   auto ss = std::ostringstream{};
         54 
         55   ss << FileUtils::ToStringPath(cpp_pack.Path()) << std::endl;
         56 
         57   auto first = true;
         58   for (auto const &src : cpp_pack.GetSrcs()) {
         59     if (first) {
         60       first = false;
         61     } else {
         62       ss << std::endl;
         63     }
         64     ss << ToStringCppSrc(src);
         65   }
         66 
         67   return ss.str();
         68 }
         69 } // namespace Dependency
```

### example/deps/dependency/src/cpp_dir.h <a id="SS_3_1_11"></a>
```cpp
          1 #pragma once
          2 #include <iostream>
          3 #include <string>
          4 #include <utility>
          5 
          6 #include "cpp_src.h"
          7 #include "file_utils/path_utils.h"
          8 
          9 namespace Dependency {
         10 
         11 class CppDir {
         12 public:
         13   explicit CppDir(FileUtils::Path_t const &path, CppSrcs_t &&srcs)
         14       : path_{path}, srcs_{std::move(srcs)} {}
         15 
         16   FileUtils::Path_t const &Path() const noexcept { return path_; }
         17   bool Contains(FileUtils::Path_t const &inc_path) const noexcept;
         18 
         19   // first  依存するヘッダファイルのインクルード数
         20   // second 依存するヘッダファイル
         21   std::pair<uint32_t, FileUtils::Paths_t>
         22   DependsOn(CppDir const &cpp_pack) const;
         23   CppSrcs_t const &GetSrcs() const noexcept { return srcs_; }
         24 
         25 private:
         26   FileUtils::Path_t const path_;
         27   CppSrcs_t const srcs_;
         28 
         29   friend bool operator==(CppDir const &lhs,
         30                          CppDir const &rhs) noexcept = default;
         31   friend auto operator<=>(CppDir const &lhs,
         32                           CppDir const &rhs) noexcept = default;
         33 };
         34 
         35 using CppDirs_t = std::vector<CppDir>;
         36 
         37 CppDirs_t GenCppDirs(FileUtils::Paths_t const &srcs,
         38                      FileUtils::Filename2Path_t const &db);
         39 
         40 std::string ToStringCppDir(CppDir const &cpp_pack);
         41 inline std::ostream &operator<<(std::ostream &os, CppDir const &dir) {
         42   return os << ToStringCppDir(dir);
         43 }
         44 } // namespace Dependency
```

### example/deps/dependency/src/cpp_src.cpp <a id="SS_3_1_12"></a>
```cpp
          1 #include <cassert>
          2 #include <fstream>
          3 #include <regex>
          4 #include <sstream>
          5 #include <tuple>
          6 
          7 #include "cpp_src.h"
          8 #include "lib/nstd.h"
          9 
         10 namespace {
         11 
         12 FileUtils::Paths_t get_incs(FileUtils::Path_t const &src) {
         13   static auto const include_line =
         14       std::regex{R"(^\s*#include\s+["<]([\w/.]+)[">](.*))"};
         15 
         16   auto ret = FileUtils::Paths_t{};
         17   auto f = std::ifstream{src};
         18   auto line = std::string{};
         19 
         20   while (std::getline(f, line)) {
         21     if (line.size() > 0) { // CRLF対策
         22       auto last = --line.end();
         23       if (*last == '\xa' || *last == '\xd') {
         24         line.erase(last);
         25       }
         26     }
         27 
         28     if (auto results = std::smatch{};
         29         std::regex_match(line, results, include_line)) {
         30       ret.emplace_back(FileUtils::Path_t(results[1].str()).filename());
         31     }
         32   }
         33 
         34   return ret;
         35 }
         36 
         37 void get_incs_full(FileUtils::Filename2Path_t const &db,
         38                    FileUtils::Path_t const &src, FileUtils::Paths_t &incs,
         39                    FileUtils::Paths_t &not_found, bool sort_uniq) {
         40   auto const inc_files = get_incs(src);
         41 
         42   for (auto const &f : inc_files) {
         43     if (db.count(f) == 0) {
         44       not_found.push_back(f);
         45     } else {
         46       auto full_path = db.at(f);
         47       if (!any_of(incs.cbegin(), incs.cend(),
         48                   [&full_path](FileUtils::Path_t const &p) noexcept {
         49                     return p == full_path;
         50                   })) {
         51         incs.emplace_back(full_path);
         52         get_incs_full(db, full_path, incs, not_found, false);
         53       }
         54     }
         55   }
         56 
         57   if (sort_uniq) {
         58     Nstd::SortUnique(incs);
         59     Nstd::SortUnique(not_found);
         60   }
         61 }
         62 } // namespace
         63 
         64 namespace Dependency {
         65 
         66 CppSrc::CppSrc(FileUtils::Path_t const &pathname,
         67                FileUtils::Filename2Path_t const &db)
         68     : path_{FileUtils::NormalizeLexically(pathname)},
         69       filename_{path_.filename()}, incs_{}, not_found_{} {
         70   get_incs_full(db, pathname, incs_, not_found_, true);
         71 }
         72 
         73 CppSrcs_t GenCppSrc(FileUtils::Paths_t const &srcs,
         74                     FileUtils::Filename2Path_t const &db) {
         75   auto ret = CppSrcs_t{};
         76 
         77   for (auto const &src : srcs) {
         78     ret.emplace_back(CppSrc{src, db});
         79   }
         80 
         81   return ret;
         82 }
         83 
         84 std::string ToStringCppSrc(CppSrc const &cpp_src) {
         85   auto ss = std::ostringstream{};
         86 
         87   ss << "file              : " << FileUtils::ToStringPath(cpp_src.Filename())
         88      << std::endl;
         89   ss << "path              : " << FileUtils::ToStringPath(cpp_src.Path())
         90      << std::endl;
         91   ss << "include           : "
         92      << FileUtils::ToStringPaths(cpp_src.GetIncs(), " ") << std::endl;
         93   ss << "include not found : "
         94      << FileUtils::ToStringPaths(cpp_src.GetIncsNotFound(), " ") << std::endl;
         95 
         96   return ss.str();
         97 }
         98 
         99 namespace {
        100 constexpr std::string_view target_ext[]{".c",  ".h",   ".cpp", ".cxx",
        101                                         ".cc", ".hpp", ".hxx", ".tcc"};
        102 
        103 bool is_c_or_cpp(std::string ext) {
        104   std::transform(ext.begin(), ext.end(), ext.begin(), ::tolower);
        105 
        106   if (std::any_of(std::begin(target_ext), std::end(target_ext),
        107                   [&ext](std::string_view s) noexcept { return s == ext; })) {
        108     return true;
        109   }
        110 
        111   return false;
        112 }
        113 
        114 FileUtils::Paths_t gen_dirs(FileUtils::Path_t const &top_dir,
        115                             FileUtils::Paths_t const &srcs) {
        116   auto dirs = FileUtils::Paths_t{top_dir};
        117   auto const top_dir2 =
        118       FileUtils::Path_t{""}; // top_dirが"."の場合、parent_path()は""になる}。
        119 
        120   for (auto const &src : srcs) {
        121     for (auto dir = src.parent_path(); dir != top_dir && dir != top_dir2;
        122          dir = dir.parent_path()) {
        123       dirs.push_back(dir);
        124     }
        125   }
        126 
        127   return dirs;
        128 }
        129 
        130 FileUtils::Paths_t find_c_or_cpp_srcs(FileUtils::Path_t const &top_path) {
        131   auto srcs = FileUtils::Paths_t{};
        132 
        133   namespace fs = std::filesystem;
        134   for (fs::path const &p : fs::recursive_directory_iterator{top_path}) {
        135     if (fs::is_regular_file(p) && is_c_or_cpp(p.extension())) {
        136       srcs.emplace_back(FileUtils::NormalizeLexically(p));
        137     }
        138   }
        139 
        140   return srcs;
        141 }
        142 } // namespace
        143 
        144 std::pair<FileUtils::Paths_t, FileUtils::Paths_t>
        145 GetCppDirsSrcs(FileUtils::Paths_t const &dirs) {
        146   auto dirs_srcs = FileUtils::Paths_t{};
        147   auto srcs = FileUtils::Paths_t{};
        148 
        149   for (auto const &dir : dirs) {
        150     FileUtils::Path_t const top_path = FileUtils::NormalizeLexically(dir);
        151     auto sub_srcs = find_c_or_cpp_srcs(top_path);
        152     auto sub_dirs_srcs = gen_dirs(top_path, sub_srcs);
        153 
        154     Nstd::Concatenate(srcs, std::move(sub_srcs));
        155     Nstd::Concatenate(dirs_srcs, std::move(sub_dirs_srcs));
        156   }
        157 
        158   Nstd::SortUnique(srcs);
        159   Nstd::SortUnique(dirs_srcs);
        160 
        161   return {std::move(dirs_srcs), std::move(srcs)};
        162 }
        163 } // namespace Dependency
```

### example/deps/dependency/src/cpp_src.h <a id="SS_3_1_13"></a>
```cpp
          1 #pragma once
          2 #include <string>
          3 #include <utility>
          4 #include <vector>
          5 
          6 #include "file_utils/path_utils.h"
          7 
          8 namespace Dependency {
          9 
         10 class CppSrc {
         11 public:
         12   explicit CppSrc(FileUtils::Path_t const &pathname,
         13                   FileUtils::Filename2Path_t const &db);
         14   FileUtils::Paths_t const &GetIncs() const noexcept { return incs_; }
         15   FileUtils::Paths_t const &GetIncsNotFound() const noexcept {
         16     return not_found_;
         17   }
         18   FileUtils::Path_t const &Filename() const noexcept { return filename_; }
         19   FileUtils::Path_t const &Path() const noexcept { return path_; }
         20 
         21 private:
         22   FileUtils::Path_t const path_;
         23   FileUtils::Path_t const filename_;
         24   FileUtils::Paths_t incs_;
         25   FileUtils::Paths_t not_found_;
         26 
         27   friend bool operator==(CppSrc const &lhs,
         28                          CppSrc const &rhs) noexcept = default;
         29   friend auto operator<=>(CppSrc const &lhs,
         30                           CppSrc const &rhs) noexcept = default;
         31 };
         32 
         33 using CppSrcs_t = std::vector<CppSrc>;
         34 CppSrcs_t GenCppSrc(FileUtils::Paths_t const &srcs,
         35                     FileUtils::Filename2Path_t const &db);
         36 std::string ToStringCppSrc(CppSrc const &cpp_src);
         37 inline std::ostream &operator<<(std::ostream &os, CppSrc const &cpp_src) {
         38   return os << ToStringCppSrc(cpp_src);
         39 }
         40 
         41 // first  dirs配下のソースファイルを含むディレクトリ
         42 // second dirs配下のソースファイル
         43 std::pair<FileUtils::Paths_t, FileUtils::Paths_t>
         44 GetCppDirsSrcs(FileUtils::Paths_t const &dirs);
         45 } // namespace Dependency
```

### example/deps/dependency/src/deps_scenario.cpp <a id="SS_3_1_14"></a>
```cpp
          1 #include <cassert>
          2 #include <iostream>
          3 #include <regex>
          4 #include <stdexcept>
          5 
          6 #include "arch_pkg.h" // 実装用ヘッダファイル
          7 // @@@ sample begin 0:0
          8 
          9 #include "cpp_deps.h"                 // 実装用ヘッダファイル
         10 #include "cpp_dir.h"                  // 実装用ヘッダファイル
         11 #include "cpp_src.h"                  // 実装用ヘッダファイル
         12 #include "dependency/deps_scenario.h" // dependencyパッケージからのインポート
         13 #include "file_utils/load_store.h" // file_utilsパッケージからのインポート
         14 #include "lib/nstd.h"              // libパッケージからのインポート
         15 // @@@ sample end
         16 #include "load_store_format.h"
         17 
         18 namespace Dependency {
         19 namespace {
         20 
         21 bool has_error_for_dir(FileUtils::Paths_t const &dirs) {
         22   if (dirs.size() == 0) {
         23     throw std::runtime_error{"need directories to generate package"};
         24   }
         25 
         26   auto not_dirs = FileUtils::NotDirs(dirs);
         27 
         28   if (not_dirs.size() != 0) {
         29     throw std::runtime_error{FileUtils::ToStringPaths(not_dirs) +
         30                              " not directory"};
         31   }
         32 
         33   return false;
         34 }
         35 
         36 FileUtils::Paths_t remove_dirs_match_pattern(FileUtils::Paths_t &&dirs,
         37                                              std::string const &pattern) {
         38   if (pattern.size() == 0) {
         39     return std::move(dirs);
         40   }
         41 
         42   auto const re_pattern = std::regex{pattern};
         43 
         44   dirs.remove_if([&re_pattern](auto const &d) {
         45     auto results = std::smatch{};
         46     auto d_str = d.string();
         47     return std::regex_match(d_str, results, re_pattern);
         48   });
         49 
         50   return std::move(dirs);
         51 }
         52 
         53 // first  dirs配下のソースファイルを含むディレクトリ(パッケージ)
         54 // second 上記パッケージに含まれるソースファイル
         55 std::pair<FileUtils::Paths_t, FileUtils::Dirs2Srcs_t>
         56 gen_dirs_and_dirs2srcs(FileUtils::Paths_t const &dirs, bool recursive,
         57                        std::string const &pattern) {
         58   auto ret =
         59       std::pair<FileUtils::Paths_t, FileUtils::Paths_t>{GetCppDirsSrcs(dirs)};
         60   auto srcs = FileUtils::Paths_t{std::move(ret.second)};
         61   auto dirs_pkg = FileUtils::Paths_t{recursive ? std::move(ret.first) : dirs};
         62 
         63   dirs_pkg = remove_dirs_match_pattern(std::move(dirs_pkg), pattern);
         64 
         65   auto dirs2srcs =
         66       FileUtils::Dirs2Srcs_t{FileUtils::AssginSrcsToDirs(dirs_pkg, srcs)};
         67 
         68   return {std::move(dirs_pkg), std::move(dirs2srcs)};
         69 }
         70 
         71 FileUtils::Paths_t gen_dirs(FileUtils::Paths_t const &dirs, bool recursive,
         72                             std::string const &pattern) {
         73   auto dirs2srcs = std::pair<FileUtils::Paths_t, FileUtils::Dirs2Srcs_t>{
         74       gen_dirs_and_dirs2srcs(dirs, recursive, pattern)};
         75 
         76   auto dirs_pkg = FileUtils::Paths_t{std::move(dirs2srcs.first)};
         77   auto assign = FileUtils::Dirs2Srcs_t{std::move(dirs2srcs.second)};
         78 
         79   auto ret = FileUtils::Paths_t{};
         80   for (auto &dir : dirs_pkg) {
         81     if (assign.count(dir) == 0) {
         82       std::cout << dir << " not including C++ files" << std::endl;
         83     } else {
         84       ret.emplace_back(std::move(dir));
         85     }
         86   }
         87 
         88   return ret;
         89 }
         90 
         91 FileUtils::Paths_t gen_dirs(std::string const &in, bool recursive,
         92                             FileUtils::Paths_t const &dirs_opt,
         93                             std::string const &pattern) {
         94   auto dirs = FileUtils::Paths_t{};
         95 
         96   if (in.size() != 0) {
         97     auto ret = std::optional<FileUtils::Paths_t>{
         98         FileUtils::LoadFromFile(in, Load_Paths)};
         99     if (!ret) {
        100       throw std::runtime_error{in + " is illegal"};
        101     }
        102     dirs = std::move(*ret);
        103   }
        104 
        105   Nstd::Concatenate(dirs, FileUtils::Paths_t(dirs_opt));
        106 
        107   if (has_error_for_dir(dirs)) {
        108     return dirs;
        109   }
        110 
        111   return gen_dirs(dirs, recursive, pattern);
        112 }
        113 
        114 bool includes(FileUtils::Paths_t const &dirs,
        115               FileUtils::Path_t const &dir) noexcept {
        116   auto const count = std::count_if(
        117       dirs.cbegin(), dirs.cend(),
        118       [&dir](auto const &dir_in_dirs) noexcept { return dir_in_dirs == dir; });
        119 
        120   return count != 0;
        121 }
        122 
        123 FileUtils::Dirs2Srcs_t
        124 dirs2srcs_to_src2src(FileUtils::Paths_t const &dirs_opt,
        125                      FileUtils::Dirs2Srcs_t const dirs2srcs, bool recursive) {
        126   auto ret = FileUtils::Dirs2Srcs_t{};
        127 
        128   for (auto const &pair : dirs2srcs) {
        129     for (auto const &src : pair.second) {
        130       if (recursive) {
        131         ret.insert(std::make_pair(src.filename(), FileUtils::Paths_t{src}));
        132       } else {
        133         if (includes(dirs_opt, pair.first)) {
        134           auto dir = FileUtils::NormalizeLexically(src.parent_path());
        135 
        136           if (dir == pair.first) {
        137             ret.insert(std::make_pair(src.filename(), FileUtils::Paths_t{src}));
        138           }
        139         }
        140       }
        141     }
        142   }
        143 
        144   return ret;
        145 }
        146 
        147 FileUtils::Dirs2Srcs_t gen_dirs2srcs(std::string const &in, bool recursive,
        148                                      bool src_as_pkg,
        149                                      FileUtils::Paths_t const &dirs_opt,
        150                                      std::string const &pattern) {
        151   auto dirs2srcs = FileUtils::Dirs2Srcs_t{};
        152   auto dirs = FileUtils::Paths_t{};
        153 
        154   if (in.size() != 0) {
        155     using FileUtils::LoadFromFile;
        156     auto ret =
        157         std::optional<FileUtils::Dirs2Srcs_t>{LoadFromFile(in, Load_Dirs2Srcs)};
        158 
        159     if (ret) {
        160       if (dirs_opt.size() != 0) {
        161         std::cout << "DIRS ignored." << std::endl;
        162       }
        163 
        164       if (recursive) {
        165         std::cout << "option \"recursive\" ignored." << std::endl;
        166       }
        167       return std::move(*ret);
        168     } else {
        169       auto ret =
        170           std::optional<FileUtils::Paths_t>{LoadFromFile(in, Load_Paths)};
        171 
        172       if (!ret) {
        173         throw std::runtime_error{in + " is illegal"};
        174       }
        175       dirs = std::move(*ret);
        176     }
        177   }
        178 
        179   Nstd::Concatenate(dirs, FileUtils::Paths_t(dirs_opt));
        180 
        181   if (has_error_for_dir(dirs)) {
        182     return dirs2srcs;
        183   }
        184 
        185   std::pair<FileUtils::Paths_t, FileUtils::Dirs2Srcs_t> ret =
        186       gen_dirs_and_dirs2srcs(dirs, recursive, pattern);
        187 
        188   auto dirs_pkg = FileUtils::Paths_t{std::move(ret.first)};
        189   auto assign = FileUtils::Dirs2Srcs_t{std::move(ret.second)};
        190 
        191   return src_as_pkg ? dirs2srcs_to_src2src(dirs_opt, assign, recursive)
        192                     : assign;
        193 }
        194 
        195 FileUtils::Filename2Path_t gen_src_db(FileUtils::Dirs2Srcs_t const &dir2srcs) {
        196   auto srcs = FileUtils::Paths_t{};
        197 
        198   for (auto const &pair : dir2srcs) {
        199     auto s = pair.second;
        200     Nstd::Concatenate(srcs, std::move(s));
        201   }
        202 
        203   return FileUtils::GenFilename2Path(srcs);
        204 }
        205 } // namespace
        206 
        207 PkgGenerator::PkgGenerator(std::string const &in, bool recursive,
        208                            FileUtils::Paths_t const &dirs_opt,
        209                            std::string const &pattern)
        210     : dirs_{gen_dirs(in, recursive, dirs_opt, pattern)} {}
        211 
        212 bool PkgGenerator::Output(std::ostream &os) const {
        213   StoreToStream(os, dirs_);
        214 
        215   return true;
        216 }
        217 
        218 SrcsGenerator::SrcsGenerator(std::string const &in, bool recursive,
        219                              FileUtils::Paths_t const &dirs_opt,
        220                              std::string const &pattern)
        221     : dirs_{gen_dirs(in, recursive, dirs_opt, pattern)} {}
        222 
        223 bool SrcsGenerator::Output(std::ostream &os) const {
        224   auto ret =
        225       std::pair<FileUtils::Paths_t, FileUtils::Paths_t>{GetCppDirsSrcs(dirs_)};
        226   auto dirs = FileUtils::Paths_t{std::move(ret.first)};
        227   auto srcs = FileUtils::Paths_t{std::move(ret.second)};
        228   auto const db = FileUtils::GenFilename2Path(srcs);
        229 
        230   auto cpp_dirs = CppDirs_t{GenCppDirs(srcs, db)};
        231 
        232   for (auto const &d : cpp_dirs) {
        233     os << "---" << std::endl;
        234     os << d << std::endl;
        235   }
        236 
        237   return true;
        238 }
        239 
        240 Pkg2SrcsGenerator::Pkg2SrcsGenerator(std::string const &in, bool recursive,
        241                                      bool src_as_pkg,
        242                                      FileUtils::Paths_t const &dirs_opt,
        243                                      std::string const &pattern)
        244     : dirs2srcs_{gen_dirs2srcs(in, recursive, src_as_pkg, dirs_opt, pattern)} {}
        245 
        246 bool Pkg2SrcsGenerator::Output(std::ostream &os) const {
        247   StoreToStream(os, dirs2srcs_);
        248 
        249   return true;
        250 }
        251 
        252 Pkg2PkgGenerator::Pkg2PkgGenerator(std::string const &in, bool recursive,
        253                                    bool src_as_pkg,
        254                                    FileUtils::Paths_t const &dirs_opt,
        255                                    std::string const &pattern)
        256     : dirs2srcs_{gen_dirs2srcs(in, recursive, src_as_pkg, dirs_opt, pattern)} {}
        257 
        258 bool Pkg2PkgGenerator::Output(std::ostream &os) const {
        259   auto cpp_dirs = CppDirs_t{};
        260 
        261   auto const db = gen_src_db(dirs2srcs_);
        262 
        263   for (auto const &pair : dirs2srcs_) {
        264     cpp_dirs.emplace_back(CppDir{pair.first, GenCppSrc(pair.second, db)});
        265   }
        266 
        267   DepRels_t const dep_rels = GenDepRels(cpp_dirs);
        268 
        269   StoreToStream(os, dep_rels);
        270 
        271   return true;
        272 }
        273 
        274 namespace {
        275 DepRels_t gen_dep_rel(std::string const &in) {
        276   if (in.size() == 0) {
        277     throw std::runtime_error{"IN-file needed"};
        278   }
        279 
        280   auto ret =
        281       std::optional<DepRels_t>{FileUtils::LoadFromFile(in, Load_DepRels)};
        282 
        283   if (!ret) {
        284     throw std::runtime_error{"IN-file load error"};
        285   }
        286 
        287   return *ret;
        288 }
        289 } // namespace
        290 
        291 struct ArchGenerator::Impl {
        292   Impl(DepRels_t &&a_dep_rels)
        293       : dep_rels(std::move(a_dep_rels)), arch(ArchPkg::GenArch(dep_rels)) {}
        294   DepRels_t const dep_rels;
        295   Arch_t const arch;
        296 };
        297 
        298 ArchGenerator::ArchGenerator(std::string const &in)
        299     : impl_{std::make_unique<ArchGenerator::Impl>(gen_dep_rel(in))} {}
        300 
        301 bool ArchGenerator::Output(std::ostream &os) const {
        302   StoreToStream(os, impl_->arch);
        303 
        304   return true;
        305 }
        306 ArchGenerator::~ArchGenerator() {}
        307 
        308 Arch2PUmlGenerator::Arch2PUmlGenerator(std::string const &in)
        309     : ArchGenerator{in} {}
        310 
        311 bool Arch2PUmlGenerator::Output(std::ostream &os) const {
        312   os << "@startuml" << std::endl;
        313   os << "scale max 730 width"
        314      << std::endl; // これ以上大きいとpdfにした時に右端が切れる
        315 
        316   os << ToPlantUML_Rectangle(impl_->arch) << std::endl;
        317   os << std::endl;
        318 
        319   os << ToPlantUML_Rectangle(impl_->arch, impl_->dep_rels) << std::endl;
        320   os << std::endl;
        321 
        322   os << "@enduml" << std::endl;
        323 
        324   return true;
        325 }
        326 
        327 CyclicGenerator::CyclicGenerator(std::string const &in)
        328     : ArchGenerator{in}, has_cyclic_dep_{
        329                              HasCyclicDeps(impl_->arch, impl_->dep_rels)} {}
        330 
        331 bool CyclicGenerator::Output(std::ostream &os) const {
        332   os << "cyclic dependencies " << (has_cyclic_dep_ ? "" : "not ") << "found"
        333      << std::endl;
        334 
        335   return !has_cyclic_dep_;
        336 }
        337 } // namespace Dependency
```

### example/deps/dependency/src/load_store_format.cpp <a id="SS_3_1_15"></a>
```cpp
          1 #include <cassert>
          2 #include <iostream>
          3 #include <regex>
          4 
          5 #include "file_utils/load_store.h"
          6 #include "load_store_format.h"
          7 
          8 namespace Dependency {
          9 namespace {
         10 auto const file_format_dir2srcs = std::string_view{"#dir2srcs"};
         11 auto const file_format_dir = std::string_view{"#dir"};
         12 auto const file_format_deps = std::string_view{"#deps"};
         13 auto const file_format_arch = std::string_view{"#arch"};
         14 } // namespace
         15 
         16 bool StoreToStream(std::ostream &os, FileUtils::Paths_t const &paths) {
         17   os << file_format_dir << std::endl;
         18 
         19   using FileUtils::operator<<;
         20   os << paths << std::endl;
         21 
         22   return true;
         23 }
         24 
         25 bool StoreToStream(std::ostream &os, FileUtils::Dirs2Srcs_t const &dirs2srcs) {
         26   os << file_format_dir2srcs << std::endl;
         27 
         28   using FileUtils::operator<<;
         29   os << dirs2srcs << std::endl;
         30 
         31   return true;
         32 }
         33 
         34 namespace {
         35 
         36 bool is_format_dirs2srcs(std::istream &is) {
         37   auto line = std::string{};
         38 
         39   if (std::getline(is, line)) {
         40     if (line == file_format_dir2srcs) {
         41       return true;
         42     }
         43   }
         44 
         45   return false;
         46 }
         47 
         48 FileUtils::Dirs2Srcs_t load_Dirs2Srcs_t(std::istream &is) {
         49   static auto const line_sep = std::regex{R"(^\s*$)"};
         50   static auto const line_dir = std::regex{R"(^([\w/.]+)$)"};
         51   static auto const line_src = std::regex{R"(^\s+([\w/.]+)$)"};
         52 
         53   auto line = std::string{};
         54   auto dir = FileUtils::Path_t{};
         55   auto srcs = FileUtils::Paths_t{};
         56   auto dirs2srcs = FileUtils::Dirs2Srcs_t{};
         57 
         58   while (std::getline(is, line)) {
         59     if (auto results = std::smatch{};
         60         std::regex_match(line, results, line_sep)) {
         61       dirs2srcs[dir].swap(srcs);
         62     } else if (std::regex_match(line, results, line_dir)) {
         63       dir = results[1].str();
         64     } else if (std::regex_match(line, results, line_src)) {
         65       srcs.push_back(results[1].str());
         66     } else {
         67       std::cout << line << std::endl;
         68       assert(false);
         69     }
         70   }
         71 
         72   return dirs2srcs;
         73 }
         74 } // namespace
         75 
         76 std::optional<FileUtils::Dirs2Srcs_t> Load_Dirs2Srcs(std::istream &is) {
         77   auto dirs2srcs = FileUtils::Dirs2Srcs_t{};
         78 
         79   if (!is) {
         80     return std::nullopt;
         81   }
         82 
         83   if (!is_format_dirs2srcs(is)) {
         84     return std::nullopt;
         85   }
         86 
         87   return load_Dirs2Srcs_t(is);
         88 }
         89 
         90 namespace {
         91 
         92 bool is_format_dirs(std::istream &is) {
         93   auto line = std::string{};
         94 
         95   if (std::getline(is, line)) {
         96     if (line == file_format_dir) {
         97       return true;
         98     }
         99   }
        100 
        101   return false;
        102 }
        103 } // namespace
        104 
        105 std::optional<FileUtils::Paths_t> Load_Paths(std::istream &is) {
        106   auto paths = FileUtils::Paths_t{};
        107 
        108   if (!is_format_dirs(is)) {
        109     return std::nullopt;
        110   }
        111 
        112   auto line = std::string{};
        113   while (std::getline(is, line)) {
        114     paths.emplace_back(FileUtils::Path_t(line));
        115   }
        116 
        117   return paths;
        118 }
        119 
        120 bool StoreToStream(std::ostream &os, DepRels_t const &dep_rels) {
        121   os << file_format_deps << std::endl;
        122   os << dep_rels << std::endl;
        123 
        124   return true;
        125 }
        126 
        127 namespace {
        128 
        129 bool is_format_deps(std::istream &is) {
        130   auto line = std::string{};
        131 
        132   if (std::getline(is, line)) {
        133     if (line == file_format_deps) {
        134       return true;
        135     }
        136   }
        137 
        138   return false;
        139 }
        140 
        141 struct dep_half_t {
        142   bool valid{false};
        143   std::string from{};
        144   std::string to{};
        145   uint32_t count{0};
        146   FileUtils::Paths_t headers{};
        147 };
        148 
        149 FileUtils::Paths_t gen_paths(std::string const &paths_str) {
        150   auto const sep = std::regex{R"( +)"};
        151   auto ret = FileUtils::Paths_t{};
        152 
        153   if (paths_str.size() != 0) {
        154     auto end = std::sregex_token_iterator{};
        155     for (auto it = std::sregex_token_iterator{paths_str.begin(),
        156                                               paths_str.end(), sep, -1};
        157          it != end; ++it) {
        158       ret.emplace_back(it->str());
        159     }
        160   }
        161 
        162   return ret;
        163 }
        164 
        165 dep_half_t get_dep_half(std::smatch const &results) {
        166   auto dep_half = dep_half_t{};
        167 
        168   dep_half.valid = true;
        169   dep_half.from = results[1].str();
        170   dep_half.to = results[2].str();
        171   dep_half.count = std::stoi(results[3].str());
        172   dep_half.headers = gen_paths(results[4].str());
        173 
        174   return dep_half;
        175 }
        176 
        177 DepRelation gen_dep_rel(dep_half_t &&first, dep_half_t &&second) {
        178   assert(first.valid);
        179   assert(second.valid);
        180   assert(first.from < second.from);
        181 
        182   return DepRelation{first.from,  first.count,  std::move(first.headers),
        183                      second.from, second.count, std::move(second.headers)};
        184 }
        185 
        186 DepRels_t load_DepRelations_t(std::istream &is) {
        187   static auto const line_sep = std::regex{R"(^\s*$)"};
        188   static auto const line_dep =
        189       std::regex{R"(^([\w/.-]+) -> ([\w/.-]+) : ([\d]+) *(.*)$)"};
        190 
        191   auto line = std::string{};
        192   auto first = dep_half_t{};
        193   auto second = dep_half_t{};
        194 
        195   auto dep_rels = DepRels_t{};
        196 
        197   while (std::getline(is, line)) {
        198     if (auto results = std::smatch{};
        199         std::regex_match(line, results, line_sep)) {
        200       dep_rels.emplace_back(gen_dep_rel(std::move(first), std::move(second)));
        201 
        202       first.valid = false;
        203       second.valid = false;
        204     } else if (std::regex_match(line, results, line_dep)) {
        205       (!first.valid ? first : second) = get_dep_half(results);
        206     } else {
        207       assert(false);
        208     }
        209   }
        210 
        211   return dep_rels;
        212 }
        213 } // namespace
        214 
        215 std::optional<DepRels_t> Load_DepRels(std::istream &is) {
        216   if (!is) {
        217     return std::nullopt;
        218   }
        219 
        220   if (!is_format_deps(is)) {
        221     return std::nullopt;
        222   }
        223 
        224   return load_DepRelations_t(is);
        225 }
        226 
        227 bool StoreToStream(std::ostream &os, Arch_t const &arch) {
        228   os << file_format_arch << std::endl;
        229   os << arch << std::endl;
        230 
        231   return true;
        232 }
        233 } // namespace Dependency
```

### example/deps/dependency/src/load_store_format.h <a id="SS_3_1_16"></a>
```cpp
          1 #pragma once
          2 #include <optional>
          3 #include <utility>
          4 
          5 #include "arch_pkg.h"
          6 #include "cpp_deps.h"
          7 #include "file_utils/path_utils.h"
          8 
          9 namespace Dependency {
         10 
         11 // LoadStore
         12 bool StoreToStream(std::ostream &os, FileUtils::Paths_t const &paths);
         13 std::optional<FileUtils::Paths_t> Load_Paths(std::istream &is);
         14 
         15 // Dirs2Srcs_t
         16 bool StoreToStream(std::ostream &os, FileUtils::Dirs2Srcs_t const &dirs2srcs);
         17 std::optional<FileUtils::Dirs2Srcs_t> Load_Dirs2Srcs(std::istream &is);
         18 
         19 // DepRels_t
         20 bool StoreToStream(std::ostream &os, DepRels_t const &dep_rels);
         21 std::optional<DepRels_t> Load_DepRels(std::istream &is);
         22 
         23 // Arch_t
         24 bool StoreToStream(std::ostream &os, Arch_t const &arch);
         25 } // namespace Dependency
```

### example/deps/dependency/ut/arch_pkg_ut.cpp <a id="SS_3_1_17"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "arch_pkg.h"
          4 
          5 namespace Dependency {
          6 namespace {
          7 
          8 using FileUtils::Paths_t;
          9 
         10 DepRels_t const dep_rels_simple{
         11     {DepRelation{"A", 1, Paths_t{"b.h"}, "B", 0, Paths_t{}}},
         12 };
         13 
         14 DepRels_t const dep_rels_simple2{
         15     {DepRelation{"X", 1, Paths_t{"b"}, "X/A", 0, Paths_t{}}},
         16     {DepRelation{"X", 1, Paths_t{"c"}, "X/B", 0, Paths_t{}}},
         17     {DepRelation{"X", 1, Paths_t{"d"}, "X/C", 0, Paths_t{}}},
         18     {DepRelation{"X", 0, Paths_t{}, "X/D", 0, Paths_t{}}},
         19     {DepRelation{"X", 0, Paths_t{}, "X/E", 0, Paths_t{}}},
         20 
         21     {DepRelation{"X/A", 1, Paths_t{"b"}, "X/B", 0, Paths_t{}}},
         22     {DepRelation{"X/B", 1, Paths_t{"c"}, "X/C", 0, Paths_t{}}},
         23     {DepRelation{"X/C", 1, Paths_t{"d"}, "X/D", 0, Paths_t{}}},
         24     {DepRelation{"X/A", 0, Paths_t{"a"}, "X/D", 1, Paths_t{}}},
         25     {DepRelation{"X/A", 1, Paths_t{"a"}, "X/E", 1, Paths_t{"d"}}},
         26 };
         27 
         28 DepRels_t const dep_rels_simple3{
         29     // A -> B
         30     // A -> C -> D -> A
         31     //      C -> B
         32     {DepRelation{"A", 1, Paths_t{}, "B", 0, Paths_t{}}},
         33     {DepRelation{"A", 1, Paths_t{}, "C", 0, Paths_t{"a"}}},
         34     {DepRelation{"A", 0, Paths_t{}, "D", 1, Paths_t{"a"}}},
         35 
         36     {DepRelation{"B", 0, Paths_t{}, "C", 1, Paths_t{"b"}}},
         37     {DepRelation{"B", 0, Paths_t{}, "D", 0, Paths_t{}}},
         38     {DepRelation{"C", 1, Paths_t{"d"}, "D", 0, Paths_t{}}},
         39 };
         40 
         41 DepRels_t const dep_rels_middle{
         42     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1",
         43                  0, Paths_t{}}},
         44     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2",
         45                  0, Paths_t{}}},
         46     {DepRelation{"ut_data/app1/mod2/mod2_1", 1,
         47                  Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         48                  "ut_data/app1/mod2/mod2_2", 2,
         49                  Paths_t{"ut_data/app1/mod2/mod2_1/mod2_1_1.h"}}},
         50 };
         51 
         52 DepRels_t const dep_rels_complex{
         53     {DepRelation{
         54         "ut_data/app1", 2,
         55         Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"},
         56         "ut_data/app1/mod1", 0, Paths_t{}}},
         57     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2", 0,
         58                  Paths_t{}}},
         59     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0,
         60                  Paths_t{}}},
         61     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 1,
         62                  Paths_t{"ut_data/app1/a_1_cpp.h"}}},
         63     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app2", 1,
         64                  Paths_t{"ut_data/app1/a_2_cpp.hpp"}}},
         65     {DepRelation{"ut_data/app1/mod1", 1,
         66                  Paths_t{"ut_data/app1/mod2/mod2_1.hpp"}, "ut_data/app1/mod2",
         67                  0, Paths_t{}}},
         68     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1",
         69                  0, Paths_t{}}},
         70     {DepRelation{"ut_data/app1/mod1", 1,
         71                  Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         72                  "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
         73     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app2", 2,
         74                  Paths_t{"ut_data/app1/mod1/mod1_1.hpp",
         75                          "ut_data/app1/mod1/mod1_2.hpp"}}},
         76     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1",
         77                  0, Paths_t{}}},
         78     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2",
         79                  0, Paths_t{}}},
         80     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app2", 0,
         81                  Paths_t{}}},
         82     {DepRelation{"ut_data/app1/mod2/mod2_1", 1,
         83                  Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         84                  "ut_data/app1/mod2/mod2_2", 2,
         85                  Paths_t{"ut_data/app1/mod2/mod2_1/mod2_1_1.h"}}},
         86     {DepRelation{"ut_data/app1/mod2/mod2_1", 0, Paths_t{}, "ut_data/app2", 0,
         87                  Paths_t{}}},
         88     {DepRelation{"ut_data/app1/mod2/mod2_2", 0, Paths_t{}, "ut_data/app2", 0,
         89                  Paths_t{}}},
         90 };
         91 
         92 TEST(arch_pkg, ArchPkgSimple) {
         93   auto const arch = ArchPkg::GenArch(dep_rels_simple);
         94 
         95   ASSERT_EQ(2, arch.size());
         96 
         97   auto const &a = *arch.cbegin();
         98   ASSERT_EQ("A", a->Name());
         99   ASSERT_EQ(nullptr, a->Parent());
        100   ASSERT_EQ("B", a->DependOn().front()->Name());
        101   ASSERT_FALSE(a->IsCyclic());
        102   ASSERT_FALSE(a->IsCyclic(*a->DependOn().front()));
        103 
        104   auto const &children = a->Children();
        105   ASSERT_EQ(0, children.size());
        106 
        107   auto const &b = *std::next(arch.cbegin());
        108   ASSERT_EQ("B", b->Name());
        109   ASSERT_EQ(nullptr, b->Parent());
        110 
        111   ASSERT_EQ(0, b->DependOn().size());
        112   ASSERT_FALSE(b->IsCyclic());
        113 }
        114 
        115 TEST(arch_pkg, ArchPkgSimple2) {
        116   auto const arch = ArchPkg::GenArch(dep_rels_simple2);
        117 
        118   auto exp = std::string{"package  :X\n"
        119                          "fullname :X\n"
        120                          "parent   :TOP\n"
        121                          "depend_on: {\n"
        122                          "    A : STRAIGHT\n"
        123                          "    B : STRAIGHT\n"
        124                          "    C : STRAIGHT\n"
        125                          "}\n"
        126                          "children : {\n"
        127                          "    package  :A:CYCLIC\n"
        128                          "    fullname :X/A\n"
        129                          "    parent   :X\n"
        130                          "    depend_on: {\n"
        131                          "        B : CYCLIC\n"
        132                          "        E : CYCLIC\n"
        133                          "    }\n"
        134                          "    children : { }\n"
        135                          "\n"
        136                          "    package  :B:CYCLIC\n"
        137                          "    fullname :X/B\n"
        138                          "    parent   :X\n"
        139                          "    depend_on: {\n"
        140                          "        C : CYCLIC\n"
        141                          "    }\n"
        142                          "    children : { }\n"
        143                          "\n"
        144                          "    package  :C:CYCLIC\n"
        145                          "    fullname :X/C\n"
        146                          "    parent   :X\n"
        147                          "    depend_on: {\n"
        148                          "        D : CYCLIC\n"
        149                          "    }\n"
        150                          "    children : { }\n"
        151                          "\n"
        152                          "    package  :D:CYCLIC\n"
        153                          "    fullname :X/D\n"
        154                          "    parent   :X\n"
        155                          "    depend_on: {\n"
        156                          "        A : CYCLIC\n"
        157                          "    }\n"
        158                          "    children : { }\n"
        159                          "\n"
        160                          "    package  :E:CYCLIC\n"
        161                          "    fullname :X/E\n"
        162                          "    parent   :X\n"
        163                          "    depend_on: {\n"
        164                          "        A : CYCLIC\n"
        165                          "    }\n"
        166                          "    children : { }\n"
        167                          "}"};
        168 
        169   ASSERT_EQ(exp, ToStringArch(arch));
        170 }
        171 
        172 TEST(arch_pkg, ArchPkgSimple3) {
        173   auto const arch = ArchPkg::GenArch(dep_rels_simple3);
        174 
        175   auto exp = std::string{"package  :A:CYCLIC\n"
        176                          "fullname :A\n"
        177                          "parent   :TOP\n"
        178                          "depend_on: {\n"
        179                          "    B : STRAIGHT\n"
        180                          "    C : CYCLIC\n"
        181                          "}\n"
        182                          "children : { }\n"
        183                          "\n"
        184                          "package  :B\n"
        185                          "fullname :B\n"
        186                          "parent   :TOP\n"
        187                          "depend_on: { }\n"
        188                          "children : { }\n"
        189                          "\n"
        190                          "package  :C:CYCLIC\n"
        191                          "fullname :C\n"
        192                          "parent   :TOP\n"
        193                          "depend_on: {\n"
        194                          "    B : STRAIGHT\n"
        195                          "    D : CYCLIC\n"
        196                          "}\n"
        197                          "children : { }\n"
        198                          "\n"
        199                          "package  :D:CYCLIC\n"
        200                          "fullname :D\n"
        201                          "parent   :TOP\n"
        202                          "depend_on: {\n"
        203                          "    A : CYCLIC\n"
        204                          "}\n"
        205                          "children : { }"};
        206 
        207   ASSERT_EQ(exp, ToStringArch(arch));
        208 }
        209 
        210 TEST(arch_pkg, ArchPkg2) {
        211   auto const arch = ArchPkg::GenArch(dep_rels_middle);
        212 
        213   ASSERT_EQ(1, arch.size());
        214 
        215   Arch_t const *mod2_children(nullptr);
        216   {
        217     auto const &mod2 = *arch.cbegin();
        218 
        219     ASSERT_EQ("mod2", mod2->Name());
        220     ASSERT_EQ(nullptr, mod2->Parent());
        221     ASSERT_EQ(0, mod2->DependOn().size());
        222     ASSERT_FALSE(mod2->IsCyclic());
        223 
        224     mod2_children = &mod2->Children();
        225     ASSERT_EQ(2, mod2_children->size());
        226   }
        227   {
        228     auto const &mod2_1 = *mod2_children->cbegin();
        229     ASSERT_EQ("mod2_1", mod2_1->Name());
        230     ASSERT_EQ("mod2", mod2_1->Parent()->Name());
        231     ASSERT_EQ("mod2_2", mod2_1->DependOn().front()->Name());
        232     ASSERT_TRUE(mod2_1->IsCyclic());
        233     ASSERT_TRUE(mod2_1->IsCyclic(*mod2_1->DependOn().front()));
        234 
        235     auto const &children = mod2_1->Children();
        236     ASSERT_EQ(0, children.size());
        237   }
        238   {
        239     auto const &mod2_2 = *std::next(mod2_children->cbegin());
        240     ASSERT_EQ("mod2_2", mod2_2->Name());
        241     ASSERT_EQ("mod2", mod2_2->Parent()->Name());
        242     ASSERT_EQ("mod2_1", mod2_2->DependOn().front()->Name());
        243     ASSERT_TRUE(mod2_2->IsCyclic());
        244     ASSERT_TRUE(mod2_2->IsCyclic(*mod2_2->DependOn().front()));
        245 
        246     auto const &children = mod2_2->Children();
        247     ASSERT_EQ(0, children.size());
        248   }
        249 }
        250 
        251 TEST(arch_pkg, ArchPkg3) {
        252   auto const arch = ArchPkg::GenArch(dep_rels_complex);
        253 
        254   /* std::cout << ToStringArch(arch) << std::endl;
        255 
        256       package  :app1:CYCLIC
        257       parent   :TOP
        258       depend_on: {
        259           mod1
        260       }
        261       children : {
        262           package  :mod1:CYCLIC
        263           parent   :app1
        264           depend_on: {
        265               mod2
        266               mod2_2
        267           }
        268 
        269           package  :mod2
        270           parent   :app1
        271           children : {
        272               package  :mod2_1:CYCLIC
        273               parent   :mod2
        274               depend_on: {
        275                   mod2_2
        276               }
        277 
        278               package  :mod2_2:CYCLIC
        279               parent   :mod2
        280               depend_on: {
        281                   app1
        282                   mod2_1
        283               }
        284           }
        285       }
        286       package  :app2
        287       parent   :TOP
        288       depend_on: {
        289           app1
        290           mod1
        291       }
        292   */
        293 
        294   {
        295     Arch_t const *app1_children(nullptr);
        296     {
        297       auto const &app1 = *arch.cbegin();
        298 
        299       ASSERT_EQ("app1", app1->Name());
        300       ASSERT_EQ(nullptr, app1->Parent());
        301       ASSERT_EQ(1, app1->DependOn().size());
        302       {
        303         auto const &depend = app1->DependOn();
        304 
        305         ASSERT_EQ("mod1", (*depend.cbegin())->Name());
        306         ASSERT_TRUE(app1->IsCyclic(*(*depend.cbegin())));
        307       }
        308 
        309       ASSERT_TRUE(app1->IsCyclic());
        310 
        311       app1_children = &app1->Children();
        312       ASSERT_EQ(2, app1_children->size());
        313     }
        314     {
        315       {
        316         auto const &mod1 = *app1_children->cbegin();
        317         ASSERT_EQ("mod1", mod1->Name());
        318         ASSERT_EQ("app1", mod1->Parent()->Name());
        319         ASSERT_EQ(2, mod1->DependOn().size());
        320         {
        321           auto const &depend = mod1->DependOn();
        322 
        323           ASSERT_EQ("mod2", (*depend.cbegin())->Name());
        324           ASSERT_FALSE(mod1->IsCyclic(*(*depend.cbegin())));
        325 
        326           auto const next = *std::next(depend.cbegin());
        327           ASSERT_EQ("mod2_2", next->Name());
        328           ASSERT_TRUE(mod1->IsCyclic(*next));
        329         }
        330         ASSERT_TRUE(mod1->IsCyclic());
        331       }
        332       Arch_t const *mod2_children(nullptr);
        333       {
        334         auto const &mod2 = *std::next(app1_children->cbegin());
        335         ASSERT_EQ("mod2", mod2->Name());
        336         ASSERT_EQ("app1", mod2->Parent()->Name());
        337         ASSERT_EQ(0, mod2->DependOn().size());
        338 
        339         mod2_children = &mod2->Children();
        340         ASSERT_EQ(2, mod2_children->size());
        341 
        342         ASSERT_FALSE(mod2->IsCyclic());
        343       }
        344       {
        345         {
        346           auto const &mod2_1 = *mod2_children->cbegin();
        347           ASSERT_EQ("mod2_1", mod2_1->Name());
        348 
        349           ASSERT_EQ("mod2", mod2_1->Parent()->Name());
        350           ASSERT_EQ(1, mod2_1->DependOn().size());
        351           {
        352             auto const &depend = mod2_1->DependOn();
        353             ASSERT_EQ("mod2_2", (*depend.cbegin())->Name());
        354             ASSERT_TRUE(mod2_1->IsCyclic(*(*depend.cbegin())));
        355           }
        356 
        357           ASSERT_TRUE(mod2_1->IsCyclic());
        358           ASSERT_EQ(0, mod2_1->Children().size());
        359         }
        360         {
        361           auto const &mod2_2 = *std::next(mod2_children->cbegin());
        362           ASSERT_EQ("mod2_2", mod2_2->Name());
        363 
        364           ASSERT_EQ("mod2", mod2_2->Parent()->Name());
        365           ASSERT_EQ(2, mod2_2->DependOn().size());
        366           {
        367             auto const &depend = mod2_2->DependOn();
        368             ASSERT_EQ("app1", (*depend.cbegin())->Name());
        369             ASSERT_TRUE(mod2_2->IsCyclic(*(*depend.cbegin())));
        370 
        371             auto const next = *std::next(depend.cbegin());
        372             ASSERT_EQ("mod2_1", (*std::next(depend.cbegin()))->Name());
        373             ASSERT_TRUE(mod2_2->IsCyclic(*next));
        374           }
        375 
        376           ASSERT_TRUE(mod2_2->IsCyclic());
        377           ASSERT_EQ(0, mod2_2->Children().size());
        378         }
        379       }
        380     }
        381   }
        382   {
        383     auto const &app2 = *std::next(arch.cbegin());
        384 
        385     ASSERT_EQ("app2", app2->Name());
        386     ASSERT_EQ(nullptr, app2->Parent());
        387     ASSERT_EQ(2, app2->DependOn().size());
        388     {
        389       auto const &depend = app2->DependOn();
        390 
        391       ASSERT_EQ("app1", (*depend.cbegin())->Name());
        392       ASSERT_EQ("mod1", (*std::next(depend.cbegin()))->Name());
        393     }
        394 
        395     ASSERT_FALSE(app2->IsCyclic());
        396     ASSERT_EQ(0, app2->Children().size());
        397   }
        398 }
        399 
        400 TEST(arch_pkg, ToPlantUML_Rectangle) {
        401   {
        402     auto const arch = ArchPkg::GenArch(dep_rels_simple);
        403     auto const exp = std::string{"rectangle \"A\" as A\n"
        404                                  "rectangle \"B\" as B"};
        405     ASSERT_EQ(exp, ToPlantUML_Rectangle(arch));
        406   }
        407   {
        408     auto const arch = ArchPkg::GenArch(dep_rels_middle);
        409     auto const exp = std::string{
        410         "rectangle \"mod2\" as ut_data___app1___mod2 {\n"
        411         "    rectangle \"mod2_1\" as ut_data___app1___mod2___mod2_1\n"
        412         "    rectangle \"mod2_2\" as ut_data___app1___mod2___mod2_2\n"
        413         "}"};
        414     ASSERT_EQ(exp, ToPlantUML_Rectangle(arch));
        415   }
        416   {
        417     auto const arch = ArchPkg::GenArch(dep_rels_complex);
        418     auto const exp = std::string{
        419         "rectangle \"app1\" as ut_data___app1 {\n"
        420         "    rectangle \"mod1\" as ut_data___app1___mod1\n"
        421         "    rectangle \"mod2\" as ut_data___app1___mod2 {\n"
        422         "        rectangle \"mod2_1\" as ut_data___app1___mod2___mod2_1\n"
        423         "        rectangle \"mod2_2\" as ut_data___app1___mod2___mod2_2\n"
        424         "    }\n"
        425         "}\n"
        426         "rectangle \"app2\" as ut_data___app2"};
        427     ASSERT_EQ(exp, ToPlantUML_Rectangle(arch));
        428   }
        429 }
        430 
        431 TEST(arch_pkg, ToPlantUML_Rectangle2) {
        432   auto const arch = ArchPkg::GenArch(dep_rels_complex);
        433   auto const exp = std::string{
        434       "ut_data___app1 \"2\" -[#orange]-> ut_data___app1___mod1\n"
        435       "ut_data___app1___mod2___mod2_2 \"1\" -[#orange]-> ut_data___app1\n"
        436       "ut_data___app2 \"1\" -[#green]-> ut_data___app1\n"
        437       "ut_data___app1___mod1 \"1\" -[#green]-> ut_data___app1___mod2\n"
        438       "ut_data___app1___mod1 \"1\" -[#orange]-> "
        439       "ut_data___app1___mod2___mod2_2\n"
        440       "ut_data___app2 \"2\" -[#green]-> ut_data___app1___mod1\n"
        441       "ut_data___app1___mod2___mod2_1 \"1\" <-[#red]-> \"2\" "
        442       "ut_data___app1___mod2___mod2_2"};
        443 
        444   ASSERT_EQ(exp, ToPlantUML_Rectangle(arch, dep_rels_complex));
        445 }
        446 
        447 TEST(arch_pkg, HasCyclicDeps) {
        448   {
        449     auto const arch = ArchPkg::GenArch(dep_rels_simple);
        450     ASSERT_FALSE(HasCyclicDeps(arch, dep_rels_simple));
        451   }
        452   {
        453     auto const arch = ArchPkg::GenArch(dep_rels_middle);
        454     ASSERT_TRUE(HasCyclicDeps(arch, dep_rels_middle));
        455   }
        456   {
        457     auto const arch = ArchPkg::GenArch(dep_rels_complex);
        458     ASSERT_TRUE(HasCyclicDeps(arch, dep_rels_complex));
        459   }
        460 }
        461 
        462 TEST(arch_pkg, FindArchPkg) {
        463   auto const arch = ArchPkg::GenArch(dep_rels_simple);
        464 
        465   {
        466     ArchPkg const *pkg_a = FindArchPkgByName(arch, "A");
        467     ASSERT_NE(nullptr, pkg_a);
        468     ASSERT_EQ("A", pkg_a->Name());
        469   }
        470   {
        471     ArchPkg const *pkg_a_f = FindArchPkgByFullName(arch, "A");
        472     ASSERT_NE(nullptr, pkg_a_f);
        473     ASSERT_EQ("A", pkg_a_f->FullName());
        474   }
        475   {
        476     ArchPkg const *pkg_b = FindArchPkgByName(arch, "B");
        477     ASSERT_NE(nullptr, pkg_b);
        478     ASSERT_EQ("B", pkg_b->Name());
        479   }
        480   {
        481     ArchPkg const *pkg_b_f = FindArchPkgByName(arch, "B");
        482 
        483     ASSERT_NE(nullptr, pkg_b_f);
        484     ASSERT_EQ("B", pkg_b_f->FullName());
        485   }
        486 }
        487 
        488 TEST(arch_pkg, FindArchPkg2) {
        489   auto const arch = ArchPkg::GenArch(dep_rels_simple2);
        490 
        491   {
        492     ArchPkg const *pkg_x = FindArchPkgByName(arch, "X");
        493     ASSERT_NE(nullptr, pkg_x);
        494     ASSERT_EQ("X", pkg_x->Name());
        495   }
        496   {
        497     ArchPkg const *pkg_x_f = FindArchPkgByFullName(arch, "X");
        498     ASSERT_NE(nullptr, pkg_x_f);
        499     ASSERT_EQ("X", pkg_x_f->FullName());
        500   }
        501   {
        502     ArchPkg const *pkg_a = FindArchPkgByName(arch, "A");
        503     ASSERT_NE(nullptr, pkg_a);
        504     ASSERT_EQ("A", pkg_a->Name());
        505   }
        506   {
        507     ArchPkg const *pkg_a_f = FindArchPkgByFullName(arch, "X/A");
        508     ASSERT_NE(nullptr, pkg_a_f);
        509     ASSERT_EQ("X/A", pkg_a_f->FullName());
        510   }
        511   {
        512     ArchPkg const *pkg_y = FindArchPkgByName(arch, "Y");
        513     ASSERT_EQ(nullptr, pkg_y);
        514   }
        515   {
        516     ArchPkg const *pkg_y_f = FindArchPkgByFullName(arch, "Y");
        517     ASSERT_EQ(nullptr, pkg_y_f);
        518   }
        519 }
        520 
        521 TEST(arch_pkg, FindArchPkg3) {
        522   auto const arch = ArchPkg::GenArch(dep_rels_complex);
        523 
        524   {
        525     ArchPkg const *pkg_app1 = FindArchPkgByName(arch, "app1");
        526     ASSERT_NE(nullptr, pkg_app1);
        527     ASSERT_EQ("app1", pkg_app1->Name());
        528     ASSERT_EQ("ut_data/app1", pkg_app1->FullName());
        529   }
        530   {
        531     ArchPkg const *pkg_app1_f = FindArchPkgByFullName(arch, "ut_data/app1");
        532     ASSERT_NE(nullptr, pkg_app1_f);
        533     ASSERT_EQ("app1", pkg_app1_f->Name());
        534     ASSERT_EQ("ut_data/app1", pkg_app1_f->FullName());
        535   }
        536   {
        537     ArchPkg const *pkg_mod2_1 = FindArchPkgByName(arch, "mod2_1");
        538     ASSERT_NE(nullptr, pkg_mod2_1);
        539     ASSERT_EQ("mod2_1", pkg_mod2_1->Name());
        540     ASSERT_EQ("ut_data/app1/mod2/mod2_1", pkg_mod2_1->FullName());
        541   }
        542   {
        543     ArchPkg const *pkg_mod2_1_f =
        544         FindArchPkgByFullName(arch, "ut_data/app1/mod2/mod2_1");
        545     ASSERT_NE(nullptr, pkg_mod2_1_f);
        546     ASSERT_EQ("mod2_1", pkg_mod2_1_f->Name());
        547     ASSERT_EQ("ut_data/app1/mod2/mod2_1", pkg_mod2_1_f->FullName());
        548   }
        549 }
        550 } // namespace
        551 } // namespace Dependency
```

### example/deps/dependency/ut/cpp_deps_ut.cpp <a id="SS_3_1_18"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "cpp_deps.h"
          4 #include "cpp_dir.h"
          5 #include "cpp_src.h"
          6 
          7 namespace Dependency {
          8 namespace {
          9 
         10 TEST(cpp_deps, GenDepRels) {
         11   using FileUtils::Paths_t;
         12 
         13   auto const [dirs, srcs] = GetCppDirsSrcs({"ut_data/"});
         14   auto const assign = FileUtils::AssginSrcsToDirs(dirs, srcs);
         15   auto const srcs_db = FileUtils::GenFilename2Path(srcs);
         16 
         17   auto cpp_dirs = CppDirs_t{};
         18 
         19   for (auto const &pair : assign) {
         20     cpp_dirs.emplace_back(CppDir{pair.first, GenCppSrc(pair.second, srcs_db)});
         21   }
         22 
         23   auto dep_all = GenDepRels(cpp_dirs);
         24 
         25   auto const app1 = std::string{"ut_data/app1"};
         26   auto const mod1 = std::string{"ut_data/app1/mod1"};
         27   auto const mod2_2 = std::string{"ut_data/app1/mod2/mod2_2"};
         28 
         29   {
         30     auto const app1_mod1 = FindDepRels(dep_all, app1, mod1);
         31     ASSERT_EQ("ut_data/app1", app1_mod1->PackageA);
         32     ASSERT_EQ("ut_data/app1/mod1", app1_mod1->PackageB);
         33 
         34     ASSERT_EQ(6, app1_mod1->CountAtoB);
         35     ASSERT_EQ(1, app1_mod1->CountBtoA);
         36 
         37     auto const app1_mod1_IncsAtoB =
         38         Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"};
         39 
         40     ASSERT_EQ(app1_mod1_IncsAtoB, app1_mod1->IncsAtoB);
         41     ASSERT_EQ(Paths_t{"ut_data/app1/a_1_cpp.h"}, app1_mod1->IncsBtoA);
         42   }
         43   {
         44     auto const app1_mod1 = FindDepRels(dep_all, mod1, app1);
         45     ASSERT_EQ("ut_data/app1", app1_mod1->PackageA);
         46     ASSERT_EQ("ut_data/app1/mod1", app1_mod1->PackageB);
         47 
         48     ASSERT_EQ(6, app1_mod1->CountAtoB);
         49     ASSERT_EQ(1, app1_mod1->CountBtoA);
         50 
         51     auto const app1_mod1_IncsAtoB =
         52         Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"};
         53 
         54     ASSERT_EQ(app1_mod1_IncsAtoB, app1_mod1->IncsAtoB);
         55     ASSERT_EQ(Paths_t{"ut_data/app1/a_1_cpp.h"}, app1_mod1->IncsBtoA);
         56   }
         57   {
         58     auto const mod1_mod2_2 = FindDepRels(dep_all, mod1, mod2_2);
         59     ASSERT_EQ("ut_data/app1/mod1", mod1_mod2_2->PackageA);
         60     ASSERT_EQ("ut_data/app1/mod2/mod2_2", mod1_mod2_2->PackageB);
         61 
         62     ASSERT_EQ(1, mod1_mod2_2->CountAtoB);
         63     ASSERT_EQ(4, mod1_mod2_2->CountBtoA);
         64 
         65     auto const mod1_mod2_2_IncsAtoB =
         66         Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"};
         67 
         68     ASSERT_EQ(mod1_mod2_2_IncsAtoB, mod1_mod2_2->IncsAtoB);
         69     ASSERT_EQ((Paths_t{"ut_data/app1/mod1/mod1_1.hpp",
         70                        "ut_data/app1/mod1/mod1_2.hpp"}),
         71               mod1_mod2_2->IncsBtoA);
         72   }
         73   {
         74     auto const app1_mod2_2 = FindDepRels(dep_all, app1, mod2_2);
         75     ASSERT_EQ("ut_data/app1", app1_mod2_2->PackageA);
         76     ASSERT_EQ("ut_data/app1/mod2/mod2_2", app1_mod2_2->PackageB);
         77 
         78     ASSERT_EQ(3, app1_mod2_2->CountAtoB);
         79     ASSERT_EQ(2, app1_mod2_2->CountBtoA);
         80 
         81     ASSERT_EQ(Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         82               app1_mod2_2->IncsAtoB);
         83 
         84     auto const app1_mod2_2_IncsAtoB = Paths_t{"ut_data/app1/a_1_cpp.h"};
         85     ASSERT_EQ(app1_mod2_2_IncsAtoB, app1_mod2_2->IncsBtoA);
         86   }
         87 }
         88 } // namespace
         89 } // namespace Dependency
```

### example/deps/dependency/ut/cpp_dir_ut.cpp <a id="SS_3_1_19"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "cpp_dir.h"
          4 #include "cpp_src.h"
          5 
          6 namespace Dependency {
          7 namespace {
          8 
          9 TEST(cpp_dir, GenCppDirs) {
         10   using FileUtils::Paths_t;
         11 
         12   auto const [dirs, srcs] = GetCppDirsSrcs({"ut_data/app1", "ut_data/app2///"});
         13   auto const db = FileUtils::GenFilename2Path(srcs);
         14   auto const cpp_dirs = CppDirs_t{GenCppDirs(srcs, db)};
         15 
         16   auto a_1_cpp =
         17       std::find_if(cpp_dirs.begin(), cpp_dirs.end(), [](CppDir const &pkg) {
         18         return pkg.Path() == "a_1_cpp.cpp";
         19       });
         20   ASSERT_NE(a_1_cpp, cpp_dirs.end());
         21 
         22   auto a_1_cpp_h =
         23       std::find_if(cpp_dirs.begin(), cpp_dirs.end(),
         24                    [](CppDir const &pkg) { return pkg.Path() == "a_1_cpp.h"; });
         25   ASSERT_NE(a_1_cpp_h, cpp_dirs.end());
         26 
         27   auto mod2_2_1_h =
         28       std::find_if(cpp_dirs.begin(), cpp_dirs.end(), [](CppDir const &pkg) {
         29         return pkg.Path() == "mod2_2_1.h";
         30       });
         31   ASSERT_NE(mod2_2_1_h, cpp_dirs.end());
         32 
         33   auto ret_a_1_cpp =
         34       std::pair<uint32_t, Paths_t>{a_1_cpp->DependsOn(*a_1_cpp_h)};
         35   ASSERT_EQ(0, ret_a_1_cpp.first);
         36 
         37   auto ret_mod2_2_1_h =
         38       std::pair<uint32_t, Paths_t>{mod2_2_1_h->DependsOn(*a_1_cpp_h)};
         39   ASSERT_EQ(1, ret_mod2_2_1_h.first);
         40 }
         41 
         42 TEST(cpp_dir, CppDir) {
         43   using FileUtils::Paths_t;
         44 
         45   auto const [dirs, srcs] = GetCppDirsSrcs({"ut_data/app1", "ut_data/app2///"});
         46   auto const packagae_srcs = FileUtils::AssginSrcsToDirs(dirs, srcs);
         47   auto const db = FileUtils::GenFilename2Path(srcs);
         48 
         49   auto mod1 = CppDir{"ut_data/app1/mod1",
         50                      GenCppSrc(packagae_srcs.at("ut_data/app1/mod1"), db)};
         51   auto app2 =
         52       CppDir{"ut_data/app2", GenCppSrc(packagae_srcs.at("ut_data/app2"), db)};
         53 
         54   ASSERT_TRUE(mod1.Contains("ut_data/app1/mod1/mod1_1.cpp"));
         55   ASSERT_TRUE(mod1.Contains("ut_data/app1/mod1/mod1_1.hpp"));
         56   ASSERT_TRUE(mod1.Contains("ut_data/app1/mod1/mod1_2.hpp"));
         57   ASSERT_FALSE(mod1.Contains("ut_data/app1/mod2/mod2_1.cpp"));
         58 
         59   auto ret_mod1 = std::pair<uint32_t, Paths_t>{mod1.DependsOn(app2)};
         60   ASSERT_EQ(0, ret_mod1.first);
         61   ASSERT_EQ(0, ret_mod1.second.size());
         62 
         63   auto ret_app2 = std::pair<uint32_t, Paths_t>{app2.DependsOn(mod1)};
         64   ASSERT_EQ(4, ret_app2.first);
         65   ASSERT_EQ(
         66       (Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}),
         67       ret_app2.second);
         68 }
         69 
         70 TEST(cpp_dir, operator_eq_tl) {
         71   auto const [dirs, srcs] = GetCppDirsSrcs({"ut_data/app1", "ut_data/app2///"});
         72   auto const packagae_srcs = FileUtils::AssginSrcsToDirs(dirs, srcs);
         73   auto const db = FileUtils::GenFilename2Path(srcs);
         74 
         75   auto mod1_0 = CppDir{"ut_data/app1/mod1",
         76                        GenCppSrc(packagae_srcs.at("ut_data/app1/mod1"), db)};
         77   auto mod1_1 = CppDir{"ut_data/app1/mod1",
         78                        GenCppSrc(packagae_srcs.at("ut_data/app1/mod1"), db)};
         79   auto app2 =
         80       CppDir{"ut_data/app2", GenCppSrc(packagae_srcs.at("ut_data/app2"), db)};
         81 
         82   ASSERT_EQ(mod1_0, mod1_0);
         83   ASSERT_EQ(mod1_0, mod1_1);
         84   ASSERT_EQ(mod1_1, mod1_0);
         85 
         86   ASSERT_NE(mod1_0, app2);
         87   ASSERT_LT(mod1_0, app2);
         88   ASSERT_GT(app2, mod1_0);
         89 }
         90 } // namespace
         91 } // namespace Dependency
```

### example/deps/dependency/ut/cpp_src_ut.cpp <a id="SS_3_1_20"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "cpp_src.h"
          4 
          5 namespace Dependency {
          6 namespace {
          7 
          8 TEST(cpp_src, CppSrc) {
          9   using FileUtils::Paths_t;
         10 
         11   auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
         12   auto const db = FileUtils::GenFilename2Path(act_srcs);
         13   auto const cpp_src = CppSrc{"ut_data/app1/a_1_c.c", db};
         14 
         15   auto const exp_incs = Paths_t{"ut_data/app1/a_1_c.h",
         16                                 "ut_data/app1/a_1_cpp.h",
         17                                 "ut_data/app1/mod1/mod1_1.hpp",
         18                                 "ut_data/app1/mod1/mod1_2.hpp",
         19                                 "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
         20                                 "ut_data/app1/mod2/mod2_2/mod2_2_1.h"};
         21   ASSERT_EQ(cpp_src.GetIncs(), exp_incs);
         22 
         23   auto const exp_not_found = Paths_t{"stdio.h", "string.h"};
         24   ASSERT_EQ(cpp_src.GetIncsNotFound(), exp_not_found);
         25 
         26   auto const cpp_src2 = CppSrc{"ut_data/app1/a_1_cpp.h", db};
         27 
         28   auto const exp_incs2 = Paths_t{
         29       "ut_data/app1/a_1_cpp.h", "ut_data/app1/mod1/mod1_1.hpp",
         30       "ut_data/app1/mod1/mod1_2.hpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
         31       "ut_data/app1/mod2/mod2_2/mod2_2_1.h"};
         32   ASSERT_EQ(cpp_src2.GetIncs(), exp_incs2);
         33 
         34   ASSERT_EQ(cpp_src2.GetIncsNotFound(), Paths_t{});
         35 
         36   auto const cpp_src3 = CppSrc{"ut_data/app1/mod1/mod1_2.hpp", db};
         37 
         38   ASSERT_EQ(cpp_src3.GetIncs(), Paths_t{});
         39 
         40   ASSERT_EQ(cpp_src3.GetIncsNotFound(), Paths_t{});
         41 }
         42 
         43 TEST(cpp_src, GenCppSrc) {
         44   using FileUtils::Paths_t;
         45 
         46   auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
         47   auto const db = FileUtils::GenFilename2Path(act_srcs);
         48   auto const srcs = Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h",
         49                             "ut_data/app1/a_1_cpp.cpp"};
         50   auto const cpp_srcs_act = GenCppSrc(srcs, db);
         51 
         52   ASSERT_EQ(cpp_srcs_act.size(), 3);
         53 
         54   Paths_t const exp_incs[]{
         55       {"ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.h",
         56        "ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp",
         57        "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
         58        "ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         59       {"ut_data/app1/a_1_cpp.h", "ut_data/app1/mod1/mod1_1.hpp",
         60        "ut_data/app1/mod1/mod1_2.hpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
         61        "ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         62       {},
         63   };
         64   Paths_t const exp_not_found[]{
         65       {"stdio.h", "string.h"},
         66       {"stdio.h", "string.h"},
         67       {},
         68   };
         69 
         70   auto it_exp_srcs = srcs.cbegin();
         71   auto it_exp_incs = std::cbegin(exp_incs);
         72   auto it_exp_not_found = std::cbegin(exp_not_found);
         73 
         74   for (auto it_act = cpp_srcs_act.cbegin(); it_act != cpp_srcs_act.cend();
         75        ++it_act) {
         76     ASSERT_EQ(*it_exp_srcs, it_act->Path());
         77     ASSERT_EQ(*it_exp_incs, it_act->GetIncs());
         78     ASSERT_EQ(*it_exp_not_found, it_act->GetIncsNotFound());
         79 
         80     ++it_exp_srcs;
         81     ++it_exp_incs;
         82     ++it_exp_not_found;
         83   }
         84 
         85   ASSERT_EQ(it_exp_srcs, srcs.cend());
         86   ASSERT_EQ(it_exp_incs, std::cend(exp_incs));
         87   ASSERT_EQ(it_exp_not_found, std::cend(exp_not_found));
         88 }
         89 
         90 TEST(cpp_src, operator_equal) {
         91   using FileUtils::Paths_t;
         92 
         93   auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
         94   auto const db = FileUtils::GenFilename2Path(act_srcs);
         95 
         96   auto const cpp_src_0 = CppSrc{"ut_data/app1/a_1_c.c", db};
         97   auto const cpp_src_1 = CppSrc{"ut_data/app1/a_1_c.c", db};
         98   auto const cpp_src_2 = CppSrc{"ut_data/app1/a_1_c.h", db};
         99 
        100   ASSERT_EQ(cpp_src_0, cpp_src_0);
        101   ASSERT_EQ(cpp_src_0, cpp_src_1);
        102   ASSERT_EQ(cpp_src_1, cpp_src_0);
        103   ASSERT_NE(cpp_src_0, cpp_src_2);
        104 }
        105 
        106 TEST(cpp_src, operator_lt) {
        107   using FileUtils::Paths_t;
        108 
        109   auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
        110   auto const db = FileUtils::GenFilename2Path(act_srcs);
        111 
        112   auto const cpp_src_0 = CppSrc{"ut_data/app1/a_1_c.c", db};
        113   auto const cpp_src_1 = CppSrc{"ut_data/app1/a_1_c.h", db};
        114 
        115   ASSERT_LT(cpp_src_0, cpp_src_1);
        116   ASSERT_GT(cpp_src_1, cpp_src_0);
        117 }
        118 
        119 TEST(cpp_src, ToString) {
        120   using FileUtils::Paths_t;
        121 
        122   auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
        123   auto const db = FileUtils::GenFilename2Path(act_srcs);
        124   auto const cpp_src = CppSrc{"ut_data/app1/a_1_c.c", db};
        125 
        126   auto const exp = std::string_view{
        127       "file              : a_1_c.c\n"
        128       "path              : ut_data/app1/a_1_c.c\n"
        129       "include           : ut_data/app1/a_1_c.h ut_data/app1/a_1_cpp.h "
        130       "ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp "
        131       "ut_data/app1/mod2/mod2_1/mod2_1_1.h "
        132       "ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        133       "include not found : stdio.h string.h\n"};
        134 
        135   ASSERT_EQ(ToStringCppSrc(cpp_src), exp);
        136 }
        137 
        138 TEST(cpp_src, GetCppDirsSrcs) {
        139   using FileUtils::Paths_t;
        140 
        141   {
        142     auto const exp_dirs = Paths_t{"ut_data/app1",
        143                                   "ut_data/app1/mod1",
        144                                   "ut_data/app1/mod2",
        145                                   "ut_data/app1/mod2/mod2_1",
        146                                   "ut_data/app1/mod2/mod2_2",
        147                                   "ut_data/app2"};
        148 
        149     auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        150                                   "ut_data/app1/a_1_c.h",
        151                                   "ut_data/app1/a_1_cpp.cpp",
        152                                   "ut_data/app1/a_1_cpp.h",
        153                                   "ut_data/app1/a_2_c.C",
        154                                   "ut_data/app1/a_2_c.H",
        155                                   "ut_data/app1/a_2_cpp.cxx",
        156                                   "ut_data/app1/a_2_cpp.hpp",
        157                                   "ut_data/app1/a_3_cpp.cc",
        158                                   "ut_data/app1/mod1/mod1_1.cpp",
        159                                   "ut_data/app1/mod1/mod1_1.hpp",
        160                                   "ut_data/app1/mod1/mod1_2.hpp",
        161                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        162                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        163                                   "ut_data/app1/mod2/mod2_1.cpp",
        164                                   "ut_data/app1/mod2/mod2_1.hpp",
        165                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        166                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        167                                   "ut_data/app2/b_1.cpp",
        168                                   "ut_data/app2/b_1.h"};
        169 
        170     auto const [act_dirs, act_srcs] =
        171         GetCppDirsSrcs({"./ut_data/app1", "ut_data/app2///"});
        172 
        173     ASSERT_EQ(act_dirs, exp_dirs);
        174     ASSERT_EQ(act_srcs, exp_srcs);
        175   }
        176   {
        177     auto const exp_dirs = Paths_t{"ut_data",
        178                                   "ut_data/app1",
        179                                   "ut_data/app1/mod1",
        180                                   "ut_data/app1/mod2",
        181                                   "ut_data/app1/mod2/mod2_1",
        182                                   "ut_data/app1/mod2/mod2_2",
        183                                   "ut_data/app2"};
        184 
        185     auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        186                                   "ut_data/app1/a_1_c.h",
        187                                   "ut_data/app1/a_1_cpp.cpp",
        188                                   "ut_data/app1/a_1_cpp.h",
        189                                   "ut_data/app1/a_2_c.C",
        190                                   "ut_data/app1/a_2_c.H",
        191                                   "ut_data/app1/a_2_cpp.cxx",
        192                                   "ut_data/app1/a_2_cpp.hpp",
        193                                   "ut_data/app1/a_3_cpp.cc",
        194                                   "ut_data/app1/mod1/mod1_1.cpp",
        195                                   "ut_data/app1/mod1/mod1_1.hpp",
        196                                   "ut_data/app1/mod1/mod1_2.hpp",
        197                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        198                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        199                                   "ut_data/app1/mod2/mod2_1.cpp",
        200                                   "ut_data/app1/mod2/mod2_1.hpp",
        201                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        202                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        203                                   "ut_data/app2/b_1.cpp",
        204                                   "ut_data/app2/b_1.h"};
        205     auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"././ut_data"});
        206 
        207     ASSERT_EQ(act_dirs, exp_dirs);
        208     ASSERT_EQ(act_srcs, exp_srcs);
        209   }
        210 }
        211 } // namespace
        212 } // namespace Dependency
```

### example/deps/dependency/ut/deps_scenario_ut.cpp <a id="SS_3_1_21"></a>
```cpp
          1 #include <sstream>
          2 
          3 #include "gtest_wrapper.h"
          4 
          5 #include "dependency/deps_scenario.h"
          6 #include "file_utils/load_store.h"
          7 #include "file_utils/load_store_row.h"
          8 
          9 namespace Dependency {
         10 namespace {
         11 
         12 TEST(deps_scenario, PkgGenerator) {
         13   using FileUtils::Paths_t;
         14 
         15   {
         16     auto pg = PkgGenerator{"ut_data/load_store/pkg_org", true,
         17                            Paths_t{"ut_data/app3/"}, ""};
         18     auto exp = std::string{"#dir\n"
         19                            "ut_data/app1\n"
         20                            "ut_data/app1/mod1\n"
         21                            "ut_data/app1/mod2\n"
         22                            "ut_data/app1/mod2/mod2_1\n"
         23                            "ut_data/app1/mod2/mod2_2\n"
         24                            "ut_data/app2\n"};
         25 
         26     auto ss = std::ostringstream{};
         27 
         28     pg.Output(ss);
         29     ASSERT_EQ(exp, ss.str());
         30   }
         31   {
         32     auto pg = PkgGenerator{"ut_data/load_store/pkg_org", false, Paths_t{}, ""};
         33     auto exp = std::string{"#dir\n"
         34                            "ut_data/app1\n"
         35                            "ut_data/app1/mod1\n"
         36                            "ut_data/app1/mod2/mod2_1\n"
         37                            "ut_data/app2\n"};
         38 
         39     auto ss = std::ostringstream{};
         40 
         41     pg.Output(ss);
         42     ASSERT_EQ(exp, ss.str());
         43   }
         44 }
         45 
         46 TEST(deps_scenario, PkgGenerator2) {
         47   using FileUtils::Paths_t;
         48 
         49   {
         50     auto pg =
         51         PkgGenerator{"", false, Paths_t{"ut_data/app1", "ut_data/app2"}, ""};
         52     auto exp = std::string{"#dir\n"
         53                            "ut_data/app1\n"
         54                            "ut_data/app2\n"};
         55 
         56     auto ss = std::ostringstream{};
         57 
         58     pg.Output(ss);
         59     ASSERT_EQ(exp, ss.str());
         60   }
         61   {
         62     auto pg = PkgGenerator{"", false, Paths_t{"ut_data/app1", "ut_data/app2"},
         63                            "hehe"};
         64     auto exp = std::string{"#dir\n"
         65                            "ut_data/app1\n"
         66                            "ut_data/app2\n"};
         67 
         68     auto ss = std::ostringstream{};
         69 
         70     pg.Output(ss);
         71     ASSERT_EQ(exp, ss.str());
         72   }
         73   {
         74     auto pg = PkgGenerator{"", false, Paths_t{"ut_data/app1", "ut_data/app2"},
         75                            ".*/app2"};
         76     auto exp = std::string{"#dir\n"
         77                            "ut_data/app1\n"};
         78 
         79     auto ss = std::ostringstream{};
         80 
         81     pg.Output(ss);
         82     ASSERT_EQ(exp, ss.str());
         83   }
         84   {
         85     auto pg =
         86         PkgGenerator{"", true, Paths_t{"ut_data/app1", "ut_data/app2"}, ""};
         87     auto exp = std::string{"#dir\n"
         88                            "ut_data/app1\n"
         89                            "ut_data/app1/mod1\n"
         90                            "ut_data/app1/mod2\n"
         91                            "ut_data/app1/mod2/mod2_1\n"
         92                            "ut_data/app1/mod2/mod2_2\n"
         93                            "ut_data/app2\n"};
         94 
         95     auto ss = std::ostringstream{};
         96 
         97     pg.Output(ss);
         98     ASSERT_EQ(exp, ss.str());
         99   }
        100   {
        101     auto pg = PkgGenerator{"", true, Paths_t{"ut_data/app1", "ut_data/app2"},
        102                            ".*/mod2/.*"};
        103     auto exp = std::string{"#dir\n"
        104                            "ut_data/app1\n"
        105                            "ut_data/app1/mod1\n"
        106                            "ut_data/app1/mod2\n"
        107                            "ut_data/app2\n"};
        108 
        109     auto ss = std::ostringstream{};
        110 
        111     pg.Output(ss);
        112     ASSERT_EQ(exp, ss.str());
        113   }
        114 
        115   auto exception_occured = false;
        116   try {
        117     auto pg = PkgGenerator{"", true,
        118                            Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app2"}, ""};
        119   } catch (std::runtime_error const &e) {
        120     exception_occured = true;
        121     ASSERT_STREQ("ut_data/app1/a_1_c.c not directory", e.what());
        122   }
        123   ASSERT_TRUE(exception_occured);
        124 }
        125 
        126 TEST(deps_scenario, SrcsGenerator) {
        127   using FileUtils::Paths_t;
        128 
        129   {
        130     auto sg = SrcsGenerator{
        131         "", true,
        132         Paths_t{"ut_data/app1/mod2/mod2_1", "ut_data/app1/mod2/mod2_2"}, ""};
        133 
        134     // clang-format off
        135         auto exp = std::string {
        136             "---\n"
        137             "mod2_1_1.cpp\n"
        138             "file              : mod2_1_1.cpp\n"
        139             "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        140             "include           : \n"
        141             "include not found : \n"
        142             "\n"
        143             "---\n"
        144             "mod2_1_1.h\n"
        145             "file              : mod2_1_1.h\n"
        146             "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        147             "include           : ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        148             "include not found : a_1_cpp.h\n"
        149             "\n"
        150             "---\n"
        151             "mod2_2_1.cpp\n"
        152             "file              : mod2_2_1.cpp\n"
        153             "path              : ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        154             "include           : ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        155             "include not found : a_1_cpp.h\n"
        156             "\n"
        157             "---\n"
        158             "mod2_2_1.h\n"
        159             "file              : mod2_2_1.h\n"
        160             "path              : ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        161             "include           : ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        162             "include not found : a_1_cpp.h\n"
        163             "\n"};
        164     // clang-format on
        165 
        166     auto ss = std::ostringstream{};
        167 
        168     sg.Output(ss);
        169     ASSERT_EQ(exp, ss.str());
        170   }
        171   {
        172     auto sg = SrcsGenerator{
        173         "", true,
        174         Paths_t{"ut_data/app1/mod2/mod2_1", "ut_data/app1/mod2/mod2_2"},
        175         ".*/mod2_2"};
        176 
        177     auto exp = std::string{
        178         "---\n"
        179         "mod2_1_1.cpp\n"
        180         "file              : mod2_1_1.cpp\n"
        181         "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        182         "include           : \n"
        183         "include not found : \n"
        184         "\n"
        185         "---\n"
        186         "mod2_1_1.h\n"
        187         "file              : mod2_1_1.h\n"
        188         "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        189         "include           : \n"
        190         "include not found : mod2_2_1.h\n"
        191         "\n"};
        192 
        193     auto ss = std::ostringstream{};
        194 
        195     sg.Output(ss);
        196     ASSERT_EQ(exp, ss.str());
        197   }
        198 }
        199 
        200 TEST(deps_scenario, Pkg2SrcsGenerator) {
        201   using FileUtils::Paths_t;
        202 
        203   auto exception_occured = false;
        204 
        205   try {
        206     auto p2sg = Pkg2SrcsGenerator{"ut_data/app1/a_1_c.c", false, false,
        207                                   Paths_t{"ut_data/app3/"}, ""};
        208   } catch (std::runtime_error const &e) {
        209     exception_occured = true;
        210     ASSERT_STREQ("ut_data/app1/a_1_c.c is illegal", e.what());
        211   }
        212   ASSERT_TRUE(exception_occured);
        213 
        214   {
        215     auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", true, false,
        216                                   Paths_t{"ut_data/app3/"}, ""};
        217 
        218     auto exp = std::string{"#dir2srcs\n"
        219                            "ut_data/app1\n"
        220                            "    ut_data/app1/a_1_c.c\n"
        221                            "    ut_data/app1/a_1_c.h\n"
        222                            "    ut_data/app1/a_1_cpp.cpp\n"
        223                            "    ut_data/app1/a_1_cpp.h\n"
        224                            "    ut_data/app1/a_2_c.C\n"
        225                            "    ut_data/app1/a_2_c.H\n"
        226                            "    ut_data/app1/a_2_cpp.cxx\n"
        227                            "    ut_data/app1/a_2_cpp.hpp\n"
        228                            "    ut_data/app1/a_3_cpp.cc\n"
        229                            "\n"
        230                            "ut_data/app1/mod1\n"
        231                            "    ut_data/app1/mod1/mod1_1.cpp\n"
        232                            "    ut_data/app1/mod1/mod1_1.hpp\n"
        233                            "    ut_data/app1/mod1/mod1_2.hpp\n"
        234                            "\n"
        235                            "ut_data/app1/mod2\n"
        236                            "    ut_data/app1/mod2/mod2_1.cpp\n"
        237                            "    ut_data/app1/mod2/mod2_1.hpp\n"
        238                            "\n"
        239                            "ut_data/app1/mod2/mod2_1\n"
        240                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        241                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        242                            "\n"
        243                            "ut_data/app1/mod2/mod2_2\n"
        244                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        245                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        246                            "\n"
        247                            "ut_data/app2\n"
        248                            "    ut_data/app2/b_1.cpp\n"
        249                            "    ut_data/app2/b_1.h\n"
        250                            "\n"};
        251 
        252     auto ss = std::ostringstream{};
        253 
        254     p2sg.Output(ss);
        255     ASSERT_EQ(exp, ss.str());
        256   }
        257   {
        258     auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", true, false,
        259                                   Paths_t{"ut_data/app3/"}, ".*/mod2\\b.*"};
        260 
        261     auto exp = std::string{"#dir2srcs\n"
        262                            "ut_data/app1\n"
        263                            "    ut_data/app1/a_1_c.c\n"
        264                            "    ut_data/app1/a_1_c.h\n"
        265                            "    ut_data/app1/a_1_cpp.cpp\n"
        266                            "    ut_data/app1/a_1_cpp.h\n"
        267                            "    ut_data/app1/a_2_c.C\n"
        268                            "    ut_data/app1/a_2_c.H\n"
        269                            "    ut_data/app1/a_2_cpp.cxx\n"
        270                            "    ut_data/app1/a_2_cpp.hpp\n"
        271                            "    ut_data/app1/a_3_cpp.cc\n"
        272                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        273                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        274                            "    ut_data/app1/mod2/mod2_1.cpp\n"
        275                            "    ut_data/app1/mod2/mod2_1.hpp\n"
        276                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        277                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        278                            "\n"
        279                            "ut_data/app1/mod1\n"
        280                            "    ut_data/app1/mod1/mod1_1.cpp\n"
        281                            "    ut_data/app1/mod1/mod1_1.hpp\n"
        282                            "    ut_data/app1/mod1/mod1_2.hpp\n"
        283                            "\n"
        284                            "ut_data/app2\n"
        285                            "    ut_data/app2/b_1.cpp\n"
        286                            "    ut_data/app2/b_1.h\n"
        287                            "\n"};
        288 
        289     auto ss = std::ostringstream{};
        290 
        291     p2sg.Output(ss);
        292     ASSERT_EQ(exp, ss.str());
        293   }
        294   {
        295     auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", false, false,
        296                                   Paths_t{"ut_data/app3/"}, ""};
        297 
        298     auto exp = std::string{"#dir2srcs\n"
        299                            "ut_data/app1\n"
        300                            "    ut_data/app1/a_1_c.c\n"
        301                            "    ut_data/app1/a_1_c.h\n"
        302                            "    ut_data/app1/a_1_cpp.cpp\n"
        303                            "    ut_data/app1/a_1_cpp.h\n"
        304                            "    ut_data/app1/a_2_c.C\n"
        305                            "    ut_data/app1/a_2_c.H\n"
        306                            "    ut_data/app1/a_2_cpp.cxx\n"
        307                            "    ut_data/app1/a_2_cpp.hpp\n"
        308                            "    ut_data/app1/a_3_cpp.cc\n"
        309                            "    ut_data/app1/mod2/mod2_1.cpp\n"
        310                            "    ut_data/app1/mod2/mod2_1.hpp\n"
        311                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        312                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        313                            "\n"
        314                            "ut_data/app1/mod1\n"
        315                            "    ut_data/app1/mod1/mod1_1.cpp\n"
        316                            "    ut_data/app1/mod1/mod1_1.hpp\n"
        317                            "    ut_data/app1/mod1/mod1_2.hpp\n"
        318                            "\n"
        319                            "ut_data/app1/mod2\n"
        320                            "\n"
        321                            "\n"
        322                            "ut_data/app1/mod2/mod2_1\n"
        323                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        324                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        325                            "\n"
        326                            "ut_data/app2\n"
        327                            "    ut_data/app2/b_1.cpp\n"
        328                            "    ut_data/app2/b_1.h\n"
        329                            "\n"};
        330 
        331     auto ss = std::ostringstream{};
        332 
        333     p2sg.Output(ss);
        334     ASSERT_EQ(exp, ss.str());
        335   }
        336   {
        337     auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", false, false,
        338                                   Paths_t{"ut_data/app3/"}, "ut_data/app2"};
        339 
        340     auto exp = std::string{"#dir2srcs\n"
        341                            "no_package\n"
        342                            "    ut_data/app2/b_1.cpp\n"
        343                            "    ut_data/app2/b_1.h\n"
        344                            "\n"
        345                            "ut_data/app1\n"
        346                            "    ut_data/app1/a_1_c.c\n"
        347                            "    ut_data/app1/a_1_c.h\n"
        348                            "    ut_data/app1/a_1_cpp.cpp\n"
        349                            "    ut_data/app1/a_1_cpp.h\n"
        350                            "    ut_data/app1/a_2_c.C\n"
        351                            "    ut_data/app1/a_2_c.H\n"
        352                            "    ut_data/app1/a_2_cpp.cxx\n"
        353                            "    ut_data/app1/a_2_cpp.hpp\n"
        354                            "    ut_data/app1/a_3_cpp.cc\n"
        355                            "    ut_data/app1/mod2/mod2_1.cpp\n"
        356                            "    ut_data/app1/mod2/mod2_1.hpp\n"
        357                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        358                            "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        359                            "\n"
        360                            "ut_data/app1/mod1\n"
        361                            "    ut_data/app1/mod1/mod1_1.cpp\n"
        362                            "    ut_data/app1/mod1/mod1_1.hpp\n"
        363                            "    ut_data/app1/mod1/mod1_2.hpp\n"
        364                            "\n"
        365                            "ut_data/app1/mod2\n"
        366                            "\n"
        367                            "\n"
        368                            "ut_data/app1/mod2/mod2_1\n"
        369                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        370                            "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        371                            "\n"};
        372 
        373     auto ss = std::ostringstream{};
        374 
        375     p2sg.Output(ss);
        376     ASSERT_EQ(exp, ss.str());
        377   }
        378 }
        379 
        380 TEST(deps_scenario, Pkg2SrcsGenerator2) {
        381   using FileUtils::Paths_t;
        382 
        383   {
        384     auto dirs2srcs_org_str =
        385         std::string{"#dir2srcs\n"
        386                     "ut_data\n"
        387                     "    ut_data/app1/a_1_c.c\n"
        388                     "    ut_data/app1/a_1_c.h\n"
        389                     "    ut_data/app1/a_1_cpp.cpp\n"
        390                     "    ut_data/app1/a_1_cpp.h\n"
        391                     "    ut_data/app1/a_2_c.C\n"
        392                     "    ut_data/app1/a_2_c.H\n"
        393                     "    ut_data/app1/a_2_cpp.cxx\n"
        394                     "    ut_data/app1/a_2_cpp.hpp\n"
        395                     "    ut_data/app1/a_3_cpp.cc\n"
        396                     "    ut_data/app1/mod1/mod1_1.cpp\n"
        397                     "    ut_data/app1/mod1/mod1_1.hpp\n"
        398                     "    ut_data/app1/mod1/mod1_2.hpp\n"
        399                     "\n"
        400                     "ut_data/app1/mod2\n"
        401                     "    ut_data/app1/mod2/mod2_1.cpp\n"
        402                     "    ut_data/app1/mod2/mod2_1.hpp\n"
        403                     "\n"
        404                     "ut_data/app1/mod2/mod2_1\n"
        405                     "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        406                     "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        407                     "\n"
        408                     "ut_data/app1/mod2/mod2_2\n"
        409                     "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        410                     "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        411                     "\n"
        412                     "ut_data/app2\n"
        413                     "    ut_data/app2/b_1.cpp\n"
        414                     "    ut_data/app2/b_1.h\n"
        415                     "\n"};
        416 
        417     auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/dirs2srcs_org", true,
        418                                   false, Paths_t{}, ""};
        419 
        420     auto ss = std::ostringstream{};
        421 
        422     p2sg.Output(ss);
        423     ASSERT_EQ(dirs2srcs_org_str, ss.str());
        424   }
        425   {
        426     auto dirs2srcs_org_str =
        427         std::string{"#dir2srcs\n"
        428                     "ut_data\n"
        429                     "    ut_data/app1/a_1_c.c\n"
        430                     "    ut_data/app1/a_1_c.h\n"
        431                     "    ut_data/app1/a_1_cpp.cpp\n"
        432                     "    ut_data/app1/a_1_cpp.h\n"
        433                     "    ut_data/app1/a_2_c.C\n"
        434                     "    ut_data/app1/a_2_c.H\n"
        435                     "    ut_data/app1/a_2_cpp.cxx\n"
        436                     "    ut_data/app1/a_2_cpp.hpp\n"
        437                     "    ut_data/app1/a_3_cpp.cc\n"
        438                     "    ut_data/app1/mod1/mod1_1.cpp\n"
        439                     "    ut_data/app1/mod1/mod1_1.hpp\n"
        440                     "    ut_data/app1/mod1/mod1_2.hpp\n"
        441                     "\n"
        442                     "ut_data/app1\n"
        443                     "\n"
        444                     "\n"
        445                     "ut_data/app1/mod2\n"
        446                     "    ut_data/app1/mod2/mod2_1.cpp\n"
        447                     "    ut_data/app1/mod2/mod2_1.hpp\n"
        448                     "\n"
        449                     "ut_data/app1/mod2/mod2_1\n"
        450                     "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        451                     "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        452                     "\n"
        453                     "ut_data/app1/mod2/mod2_2\n"
        454                     "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        455                     "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        456                     "\n"
        457                     "ut_data/app2\n"
        458                     "    ut_data/app2/b_1.cpp\n"
        459                     "    ut_data/app2/b_1.h\n"
        460                     "\n"};
        461 
        462     auto const dirs =
        463         Paths_t{"ut_data", "ut_data/app1/mod2", "ut_data/app1/mod2/mod2_1",
        464                 "ut_data/app1/mod2/mod2_2", "ut_data/app2"};
        465 
        466     auto p2sg = Pkg2SrcsGenerator{"", false, false, dirs, ""};
        467 
        468     auto ss = std::ostringstream{};
        469 
        470     p2sg.Output(ss);
        471     ASSERT_EQ(dirs2srcs_org_str, ss.str());
        472   }
        473   {
        474     auto p2sg = Pkg2SrcsGenerator{"", true, false, Paths_t{"ut_data"}, ""};
        475 
        476     auto const exp = std::string{"#dir2srcs\n"
        477                                  "ut_data/app1\n"
        478                                  "    ut_data/app1/a_1_c.c\n"
        479                                  "    ut_data/app1/a_1_c.h\n"
        480                                  "    ut_data/app1/a_1_cpp.cpp\n"
        481                                  "    ut_data/app1/a_1_cpp.h\n"
        482                                  "    ut_data/app1/a_2_c.C\n"
        483                                  "    ut_data/app1/a_2_c.H\n"
        484                                  "    ut_data/app1/a_2_cpp.cxx\n"
        485                                  "    ut_data/app1/a_2_cpp.hpp\n"
        486                                  "    ut_data/app1/a_3_cpp.cc\n"
        487                                  "\n"
        488                                  "ut_data/app1/mod1\n"
        489                                  "    ut_data/app1/mod1/mod1_1.cpp\n"
        490                                  "    ut_data/app1/mod1/mod1_1.hpp\n"
        491                                  "    ut_data/app1/mod1/mod1_2.hpp\n"
        492                                  "\n"
        493                                  "ut_data/app1/mod2\n"
        494                                  "    ut_data/app1/mod2/mod2_1.cpp\n"
        495                                  "    ut_data/app1/mod2/mod2_1.hpp\n"
        496                                  "\n"
        497                                  "ut_data/app1/mod2/mod2_1\n"
        498                                  "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        499                                  "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        500                                  "\n"
        501                                  "ut_data/app1/mod2/mod2_2\n"
        502                                  "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        503                                  "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        504                                  "\n"
        505                                  "ut_data/app2\n"
        506                                  "    ut_data/app2/b_1.cpp\n"
        507                                  "    ut_data/app2/b_1.h\n"
        508                                  "\n"};
        509 
        510     auto ss = std::ostringstream{};
        511 
        512     p2sg.Output(ss);
        513     ASSERT_EQ(exp, ss.str());
        514   }
        515 }
        516 
        517 TEST(deps_scenario, Pkg2PkgGenerator) {
        518   using FileUtils::Paths_t;
        519 
        520   auto exception_occured = false;
        521   try {
        522     auto p2pg = Pkg2PkgGenerator{"ut_data/app1/a_1_c.c", false, false,
        523                                  Paths_t{"ut_data/app3/"}, ""};
        524   } catch (std::runtime_error const &e) {
        525     exception_occured = true;
        526     ASSERT_STREQ("ut_data/app1/a_1_c.c is illegal", e.what());
        527   }
        528   ASSERT_TRUE(exception_occured);
        529 
        530   {
        531     auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", true, false,
        532                                  Paths_t{"ut_data/app3/"}, ""};
        533 
        534     // clang-format off
        535         auto exp = std::string {
        536             "#deps\n"
        537             "ut_data/app1 -> ut_data/app1/mod1 : 6 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        538             "ut_data/app1/mod1 -> ut_data/app1 : 1 ut_data/app1/a_1_cpp.h\n"
        539             "\n"
        540             "ut_data/app1 -> ut_data/app1/mod2 : 0 \n"
        541             "ut_data/app1/mod2 -> ut_data/app1 : 0 \n"
        542             "\n"
        543             "ut_data/app1 -> ut_data/app1/mod2/mod2_1 : 3 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        544             "ut_data/app1/mod2/mod2_1 -> ut_data/app1 : 1 ut_data/app1/a_1_cpp.h\n"
        545             "\n"
        546             "ut_data/app1 -> ut_data/app1/mod2/mod2_2 : 3 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        547             "ut_data/app1/mod2/mod2_2 -> ut_data/app1 : 2 ut_data/app1/a_1_cpp.h\n"
        548             "\n"
        549             "ut_data/app1 -> ut_data/app2 : 0 \n"
        550             "ut_data/app2 -> ut_data/app1 : 3 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp\n"
        551             "\n"
        552             "ut_data/app1/mod1 -> ut_data/app1/mod2 : 1 ut_data/app1/mod2/mod2_1.hpp\n"
        553             "ut_data/app1/mod2 -> ut_data/app1/mod1 : 0 \n"
        554             "\n"
        555             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_1 : 1 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        556             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        557             "\n"
        558             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_2 : 1 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        559             "ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        560             "\n"
        561             "ut_data/app1/mod1 -> ut_data/app2 : 0 \n"
        562             "ut_data/app2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        563             "\n"
        564             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_1 : 0 \n"
        565             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2 : 0 \n"
        566             "\n"
        567             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_2 : 0 \n"
        568             "ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod2 : 0 \n"
        569             "\n"
        570             "ut_data/app1/mod2 -> ut_data/app2 : 0 \n"
        571             "ut_data/app2 -> ut_data/app1/mod2 : 0 \n"
        572             "\n"
        573             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2/mod2_2 : 1 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        574             "ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        575             "\n"
        576             "ut_data/app1/mod2/mod2_1 -> ut_data/app2 : 0 \n"
        577             "ut_data/app2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        578             "\n"
        579             "ut_data/app1/mod2/mod2_2 -> ut_data/app2 : 0 \n"
        580             "ut_data/app2 -> ut_data/app1/mod2/mod2_2 : 2 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        581             "\n"};
        582     // clang-format on
        583 
        584     auto ss = std::ostringstream{};
        585 
        586     p2pg.Output(ss);
        587     ASSERT_EQ(exp, ss.str());
        588   }
        589   {
        590     auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", true, false,
        591                                  Paths_t{"ut_data/app3/"}, ".*/mod2\\b.*"};
        592 
        593     // clang-format off
        594         auto exp = std::string {
        595             "#deps\n"
        596             "ut_data/app1 -> ut_data/app1/mod1 : 12 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        597             "ut_data/app1/mod1 -> ut_data/app1 : 4 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_1.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        598             "\n"
        599             "ut_data/app1 -> ut_data/app2 : 0 \n"
        600             "ut_data/app2 -> ut_data/app1 : 7 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        601             "\n"
        602             "ut_data/app1/mod1 -> ut_data/app2 : 0 \n"
        603             "ut_data/app2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        604             "\n"};
        605     // clang-format on
        606 
        607     auto ss = std::ostringstream{};
        608 
        609     p2pg.Output(ss);
        610     ASSERT_EQ(exp, ss.str());
        611   }
        612   {
        613     auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", false, false,
        614                                  Paths_t{"ut_data/app3/"}, ""};
        615 
        616     // clang-format off
        617         auto exp = std::string {
        618             "#deps\n"
        619             "ut_data/app1 -> ut_data/app1/mod1 : 10 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        620             "ut_data/app1/mod1 -> ut_data/app1 : 3 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_1.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        621             "\n"
        622             "ut_data/app1 -> ut_data/app1/mod2 : 0 \n"
        623             "ut_data/app1/mod2 -> ut_data/app1 : 0 \n"
        624             "\n"
        625             "ut_data/app1 -> ut_data/app1/mod2/mod2_1 : 5 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        626             "ut_data/app1/mod2/mod2_1 -> ut_data/app1 : 2 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        627             "\n"
        628             "ut_data/app1 -> ut_data/app2 : 0 \n"
        629             "ut_data/app2 -> ut_data/app1 : 5 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        630             "\n"
        631             "ut_data/app1/mod1 -> ut_data/app1/mod2 : 0 \n"
        632             "ut_data/app1/mod2 -> ut_data/app1/mod1 : 0 \n"
        633             "\n"
        634             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_1 : 1 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        635             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        636             "\n"
        637             "ut_data/app1/mod1 -> ut_data/app2 : 0 \n"
        638             "ut_data/app2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        639             "\n"
        640             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_1 : 0 \n"
        641             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2 : 0 \n"
        642             "\n"
        643             "ut_data/app1/mod2 -> ut_data/app2 : 0 \n"
        644             "ut_data/app2 -> ut_data/app1/mod2 : 0 \n"
        645             "\n"
        646             "ut_data/app1/mod2/mod2_1 -> ut_data/app2 : 0 \n"
        647             "ut_data/app2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        648             "\n"};
        649     // clang-format on
        650 
        651     auto ss = std::ostringstream{};
        652 
        653     p2pg.Output(ss);
        654     ASSERT_EQ(exp, ss.str());
        655   }
        656   {
        657     auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", false, false,
        658                                  Paths_t{"ut_data/app3/"}, "ut_data/app2"};
        659 
        660     // clang-format off
        661         auto exp = std::string {
        662             "#deps\n"
        663             "no_package -> ut_data/app1 : 5 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        664             "ut_data/app1 -> no_package : 0 \n"
        665             "\n"
        666             "no_package -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        667             "ut_data/app1/mod1 -> no_package : 0 \n"
        668             "\n"
        669             "no_package -> ut_data/app1/mod2 : 0 \n"
        670             "ut_data/app1/mod2 -> no_package : 0 \n"
        671             "\n"
        672             "no_package -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        673             "ut_data/app1/mod2/mod2_1 -> no_package : 0 \n"
        674             "\n"
        675             "ut_data/app1 -> ut_data/app1/mod1 : 10 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        676             "ut_data/app1/mod1 -> ut_data/app1 : 3 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_1.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        677             "\n"
        678             "ut_data/app1 -> ut_data/app1/mod2 : 0 \n"
        679             "ut_data/app1/mod2 -> ut_data/app1 : 0 \n"
        680             "\n"
        681             "ut_data/app1 -> ut_data/app1/mod2/mod2_1 : 5 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        682             "ut_data/app1/mod2/mod2_1 -> ut_data/app1 : 2 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        683             "\n"
        684             "ut_data/app1/mod1 -> ut_data/app1/mod2 : 0 \n"
        685             "ut_data/app1/mod2 -> ut_data/app1/mod1 : 0 \n"
        686             "\n"
        687             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_1 : 1 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        688             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        689             "\n"
        690             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_1 : 0 \n"
        691             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2 : 0 \n"
        692             "\n"};
        693     // clang-format on
        694 
        695     auto ss = std::ostringstream{};
        696 
        697     p2pg.Output(ss);
        698     ASSERT_EQ(exp, ss.str());
        699   }
        700 }
        701 
        702 TEST(deps_scenario, ArchGenerator) {
        703   using FileUtils::Paths_t;
        704 
        705   auto exception_occured = false;
        706   try {
        707     auto ag = ArchGenerator{"ut_data/load_store/arch_org"};
        708   } catch (std::runtime_error const &e) {
        709     exception_occured = true;
        710     ASSERT_STREQ("IN-file load error", e.what());
        711   }
        712   ASSERT_TRUE(exception_occured);
        713 
        714   {
        715     auto ag = ArchGenerator{"ut_data/load_store/deps_org"};
        716     auto ss = std::stringstream{};
        717 
        718     ag.Output(ss);
        719 
        720     auto act =
        721         std::optional<std::vector<std::string>>{FileUtils::Load_Strings(ss)};
        722 
        723     auto exp = std::optional<std::vector<std::string>>{FileUtils::LoadFromFile(
        724         "ut_data/load_store/arch_org", FileUtils::Load_Strings)};
        725 
        726     ASSERT_TRUE(exp);
        727 
        728     ASSERT_EQ(*act, *exp);
        729   }
        730 }
        731 
        732 TEST(deps_scenario, Arch2PUmlGenerator) {
        733   auto exception_occured = false;
        734   try {
        735     auto ag = Arch2PUmlGenerator{"ut_data/load_store/arch_org"};
        736   } catch (std::runtime_error const &e) {
        737     exception_occured = true;
        738     ASSERT_STREQ("IN-file load error", e.what());
        739   }
        740   ASSERT_TRUE(exception_occured);
        741 
        742   {
        743     auto ag = Arch2PUmlGenerator{"ut_data/load_store/deps_org"};
        744     auto ss = std::stringstream{};
        745 
        746     ag.Output(ss);
        747 
        748     auto exp = std::string{
        749         "@startuml\n"
        750         "scale max 730 width\n"
        751         "rectangle \"app1\" as ut_data___app1 {\n"
        752         "    rectangle \"mod1\" as ut_data___app1___mod1\n"
        753         "    rectangle \"mod2\" as ut_data___app1___mod2 {\n"
        754         "        rectangle \"mod2_1\" as ut_data___app1___mod2___mod2_1\n"
        755         "        rectangle \"mod2_2\" as ut_data___app1___mod2___mod2_2\n"
        756         "    }\n"
        757         "}\n"
        758         "rectangle \"app2\" as ut_data___app2\n"
        759         "\n"
        760         "ut_data___app1 \"2\" -[#orange]-> ut_data___app1___mod1\n"
        761         "ut_data___app1___mod2___mod2_2 \"1\" -[#orange]-> ut_data___app1\n"
        762         "ut_data___app2 \"1\" -[#green]-> ut_data___app1\n"
        763         "ut_data___app1___mod1 \"1\" -[#green]-> ut_data___app1___mod2\n"
        764         "ut_data___app1___mod1 \"1\" -[#orange]-> "
        765         "ut_data___app1___mod2___mod2_2\n"
        766         "ut_data___app2 \"2\" -[#green]-> ut_data___app1___mod1\n"
        767         "ut_data___app1___mod2___mod2_1 \"1\" <-[#red]-> \"2\" "
        768         "ut_data___app1___mod2___mod2_2\n"
        769         "\n"
        770         "@enduml\n"};
        771 
        772     ASSERT_EQ(exp, ss.str());
        773   }
        774 }
        775 
        776 TEST(deps_scenario, CyclicGenerator) {
        777   auto exception_occured = false;
        778   try {
        779     auto cg = CyclicGenerator{"ut_data/load_store/arch_org"};
        780   } catch (std::runtime_error const &e) {
        781     exception_occured = true;
        782     ASSERT_STREQ("IN-file load error", e.what());
        783   }
        784   ASSERT_TRUE(exception_occured);
        785 
        786   {
        787     auto cg = CyclicGenerator{"ut_data/load_store/deps_org"};
        788     auto ss = std::stringstream{};
        789 
        790     ASSERT_FALSE(cg.Output(ss));
        791 
        792     ASSERT_EQ("cyclic dependencies found\n", ss.str());
        793   }
        794   {
        795     auto cg = CyclicGenerator{"ut_data/load_store/deps_org2"};
        796     auto ss = std::stringstream{};
        797 
        798     ASSERT_TRUE(cg.Output(ss));
        799 
        800     ASSERT_EQ("cyclic dependencies not found\n", ss.str());
        801   }
        802 }
        803 } // namespace
        804 } // namespace Dependency
```

### example/deps/dependency/ut/load_store_format_ut.cpp <a id="SS_3_1_22"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "file_utils/load_store.h"
          4 #include "file_utils/load_store_row.h"
          5 #include "load_store_format.h"
          6 
          7 namespace Dependency {
          8 namespace {
          9 
         10 TEST(load_store_format, Paths_t) {
         11   using FileUtils::Paths_t;
         12 
         13   auto const pkg_org = std::string{"ut_data/load_store/pkg_org"};
         14   auto const pkg_act = std::string{"ut_data/load_store/pkg_act"};
         15 
         16   FileUtils::RemoveFile(pkg_act);
         17 
         18   auto const dir_in = Paths_t{"ut_data/app1", "ut_data/app1/mod1",
         19                               "ut_data/app1/mod2/mod2_1", "ut_data/app2"};
         20 
         21   // ディレクトリなのでエラーなはず
         22   ASSERT_FALSE(FileUtils::StoreToFile("ut_data/app1", dir_in, StoreToStream));
         23 
         24   ASSERT_TRUE(FileUtils::StoreToFile(pkg_act, dir_in, StoreToStream));
         25 
         26   auto dir_out0 =
         27       std::optional<Paths_t>{FileUtils::LoadFromFile(pkg_org, Load_Paths)};
         28   ASSERT_TRUE(dir_out0);
         29 
         30   auto dir_out1 =
         31       std::optional<Paths_t>{FileUtils::LoadFromFile(pkg_act, Load_Paths)};
         32   ASSERT_TRUE(dir_out1);
         33 
         34   ASSERT_EQ(dir_in, *dir_out0);
         35   ASSERT_EQ(dir_in, *dir_out1);
         36 
         37   FileUtils::RemoveFile(pkg_act);
         38 }
         39 
         40 TEST(load_store_format, Dirs2Srcs_t) {
         41   auto const dirs2srcs_org = std::string{"ut_data/load_store/dirs2srcs_org"};
         42   auto const dirs2srcs_act = std::string{"ut_data/load_store/dirs2srcs_act"};
         43 
         44   FileUtils::RemoveFile(dirs2srcs_act);
         45 
         46   const auto dir2srcs_in = FileUtils::Dirs2Srcs_t{
         47       {"ut_data",
         48        {"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h",
         49         "ut_data/app1/a_1_cpp.cpp", "ut_data/app1/a_1_cpp.h",
         50         "ut_data/app1/a_2_c.C", "ut_data/app1/a_2_c.H",
         51         "ut_data/app1/a_2_cpp.cxx", "ut_data/app1/a_2_cpp.hpp",
         52         "ut_data/app1/a_3_cpp.cc", "ut_data/app1/mod1/mod1_1.cpp",
         53         "ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}},
         54       {"ut_data/app1/mod2",
         55        {"ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
         56       {"ut_data/app1/mod2/mod2_1",
         57        {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
         58         "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
         59       {"ut_data/app1/mod2/mod2_2",
         60        {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
         61         "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
         62       {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
         63   };
         64 
         65   // ディレクトリなのでエラーなはず
         66   ASSERT_FALSE(
         67       FileUtils::StoreToFile("ut_data/app1", dir2srcs_in, StoreToStream));
         68 
         69   ASSERT_TRUE(
         70       FileUtils::StoreToFile(dirs2srcs_act, dir2srcs_in, StoreToStream));
         71 
         72   auto dir2srcs_out0 = std::optional<FileUtils::Dirs2Srcs_t>{
         73       FileUtils::LoadFromFile(dirs2srcs_org, Load_Dirs2Srcs)};
         74   ASSERT_TRUE(dir2srcs_out0);
         75 
         76   auto dir2srcs_out1 = std::optional<FileUtils::Dirs2Srcs_t>{
         77       FileUtils::LoadFromFile(dirs2srcs_act, Load_Dirs2Srcs)};
         78   ASSERT_TRUE(dir2srcs_out1);
         79 
         80   ASSERT_EQ(dir2srcs_in, *dir2srcs_out0);
         81   ASSERT_EQ(dir2srcs_in, *dir2srcs_out1);
         82 
         83   FileUtils::RemoveFile(dirs2srcs_act);
         84 }
         85 
         86 namespace {
         87 using FileUtils::Paths_t;
         88 
         89 DepRels_t const dep_rels{
         90     {DepRelation{
         91         "ut_data/app1", 2,
         92         Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"},
         93         "ut_data/app1/mod1", 0, Paths_t{}}},
         94     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2", 0,
         95                  Paths_t{}}},
         96     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0,
         97                  Paths_t{}}},
         98     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 1,
         99                  Paths_t{"ut_data/app1/a_1_cpp.h"}}},
        100     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app2", 1,
        101                  Paths_t{"ut_data/app1/a_2_cpp.hpp"}}},
        102     {DepRelation{"ut_data/app1/mod1", 1,
        103                  Paths_t{"ut_data/app1/mod2/mod2_1.hpp"}, "ut_data/app1/mod2",
        104                  0, Paths_t{}}},
        105     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1",
        106                  0, Paths_t{}}},
        107     {DepRelation{"ut_data/app1/mod1", 1,
        108                  Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
        109                  "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
        110     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app2", 2,
        111                  Paths_t{"ut_data/app1/mod1/mod1_1.hpp",
        112                          "ut_data/app1/mod1/mod1_2.hpp"}}},
        113     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1",
        114                  0, Paths_t{}}},
        115     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2",
        116                  0, Paths_t{}}},
        117     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app2", 0,
        118                  Paths_t{}}},
        119     {DepRelation{"ut_data/app1/mod2/mod2_1", 1,
        120                  Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
        121                  "ut_data/app1/mod2/mod2_2", 2,
        122                  Paths_t{"ut_data/app1/mod2/mod2_1/mod2_1_1.h"}}},
        123     {DepRelation{"ut_data/app1/mod2/mod2_1", 0, Paths_t{}, "ut_data/app2", 0,
        124                  Paths_t{}}},
        125     {DepRelation{"ut_data/app1/mod2/mod2_2", 0, Paths_t{}, "ut_data/app2", 0,
        126                  Paths_t{}}},
        127 };
        128 } // namespace
        129 
        130 TEST(load_store_format, DepRels_t) {
        131   auto const deps_org = std::string{"ut_data/load_store/deps_org"};
        132   auto const deps_act = std::string{"ut_data/load_store/deps_act"};
        133 
        134   FileUtils::RemoveFile(deps_act);
        135 
        136   // ディレクトリなのでエラーなはず
        137   ASSERT_FALSE(FileUtils::StoreToFile("ut_data/app1", dep_rels, StoreToStream));
        138 
        139   ASSERT_TRUE(FileUtils::StoreToFile(deps_act, dep_rels, StoreToStream));
        140 
        141   auto deps_out0 =
        142       std::optional<DepRels_t>{FileUtils::LoadFromFile(deps_org, Load_DepRels)};
        143   ASSERT_TRUE(deps_out0);
        144 
        145   auto exp_it = dep_rels.cbegin();
        146   auto exp_it_end = dep_rels.cend();
        147   auto act_it = deps_out0->cbegin();
        148 
        149   while (exp_it != exp_it_end) {
        150     auto exp_str = ToStringDepRel(*exp_it);
        151     auto act_str = ToStringDepRel(*act_it);
        152     ASSERT_EQ(exp_str, act_str);
        153     ASSERT_EQ(exp_it->PackageA, act_it->PackageA);
        154     ASSERT_EQ(exp_it->CountAtoB, act_it->CountAtoB);
        155     ASSERT_EQ(exp_it->IncsAtoB, act_it->IncsAtoB);
        156     ASSERT_EQ(exp_it->PackageB, act_it->PackageB);
        157     ASSERT_EQ(exp_it->CountBtoA, act_it->CountBtoA);
        158     ASSERT_EQ(exp_it->IncsBtoA, act_it->IncsBtoA);
        159     ASSERT_EQ(*exp_it, *act_it);
        160 
        161     ++exp_it;
        162     ++act_it;
        163   }
        164   ASSERT_EQ(dep_rels, *deps_out0);
        165 
        166   auto deps_out1 =
        167       std::optional<DepRels_t>{FileUtils::LoadFromFile(deps_act, Load_DepRels)};
        168   ASSERT_TRUE(deps_out1);
        169 
        170   ASSERT_EQ(dep_rels, *deps_out1);
        171 
        172   FileUtils::RemoveFile(deps_act);
        173 }
        174 
        175 TEST(load_store_format, Arch_t) {
        176   auto const arch_exp = std::string{"ut_data/load_store/arch_org"};
        177   auto const arch_act = std::string{"ut_data/load_store/arch_act"};
        178 
        179   FileUtils::RemoveFile(arch_act);
        180 
        181   auto row_exp = std::optional<std::vector<std::string>>{
        182       FileUtils::LoadFromFile(arch_exp, FileUtils::Load_Strings)};
        183   ASSERT_TRUE(row_exp);
        184 
        185   auto const arch = ArchPkg::GenArch(dep_rels);
        186   ASSERT_TRUE(FileUtils::StoreToFile(arch_act, arch, StoreToStream));
        187 
        188   auto row_act = std::optional<std::vector<std::string>>{
        189       FileUtils::LoadFromFile(arch_act, FileUtils::Load_Strings)};
        190   ASSERT_TRUE(row_act);
        191 
        192   ASSERT_EQ(row_exp, *row_act);
        193 
        194   FileUtils::RemoveFile(arch_act);
        195 }
        196 } // namespace
        197 } // namespace Dependency
```

### example/deps/file_utils/h/file_utils/load_store.h <a id="SS_3_1_23"></a>
```cpp
          1 #pragma once
          2 #include <fstream>
          3 #include <optional>
          4 #include <string>
          5 
          6 namespace FileUtils {
          7 
          8 template <typename T>
          9 bool StoreToFile(std::string_view filename, T const &t,
         10                  bool (*ss)(std::ostream &os, T const &)) {
         11   auto fout = std::ofstream{filename.data()};
         12 
         13   if (!fout) {
         14     return false;
         15   }
         16 
         17   return (*ss)(fout, t);
         18 }
         19 
         20 template <typename T>
         21 std::optional<T> LoadFromFile(std::string_view filename,
         22                               std::optional<T> (*ls)(std::istream &os)) {
         23   auto fin = std::ifstream{filename.data()};
         24 
         25   if (!fin) {
         26     return std::nullopt;
         27   }
         28 
         29   return (*ls)(fin);
         30 }
         31 } // namespace FileUtils
```

### example/deps/file_utils/h/file_utils/load_store_row.h <a id="SS_3_1_24"></a>
```cpp
          1 #pragma once
          2 #include <fstream>
          3 #include <optional>
          4 #include <utility>
          5 #include <vector>
          6 
          7 namespace FileUtils {
          8 
          9 bool StoreToStream(std::ostream &os, std::vector<std::string> const &lines);
         10 std::optional<std::vector<std::string>> Load_Strings(std::istream &is);
         11 } // namespace FileUtils
```

### example/deps/file_utils/h/file_utils/path_utils.h <a id="SS_3_1_25"></a>
```cpp
          1 #pragma once
          2 #include <filesystem>
          3 #include <fstream>
          4 #include <list>
          5 #include <map>
          6 #include <string>
          7 
          8 namespace FileUtils {
          9 
         10 using Path_t = std::filesystem::path;
         11 std::string ToStringPath(Path_t const &paths);
         12 
         13 using Paths_t = std::list<std::filesystem::path>;
         14 
         15 Paths_t NotDirs(Paths_t const &dirs);
         16 std::string ToStringPaths(Paths_t const &paths, std::string_view sep = "\n",
         17                           std::string_view indent = "");
         18 inline std::ostream &operator<<(std::ostream &os, Paths_t const &paths) {
         19   return os << ToStringPaths(paths);
         20 }
         21 
         22 // first path:  filename
         23 // second path: pathname
         24 using Filename2Path_t = std::map<Path_t, Path_t>;
         25 Filename2Path_t GenFilename2Path(Paths_t const &paths);
         26 
         27 // first  : package name(directory name)
         28 // second : srcs assigned to package
         29 using Dirs2Srcs_t = std::map<Path_t, Paths_t>;
         30 
         31 Dirs2Srcs_t AssginSrcsToDirs(Paths_t const &dirs, Paths_t const &srcs);
         32 std::string ToStringDirs2Srcs(Dirs2Srcs_t const &dirs2srcs);
         33 inline std::ostream &operator<<(std::ostream &os,
         34                                 Dirs2Srcs_t const &dirs2srcs) {
         35   return os << ToStringDirs2Srcs(dirs2srcs);
         36 }
         37 
         38 Path_t NormalizeLexically(Path_t const &path);
         39 
         40 void RemoveFile(Path_t const &filename);
         41 } // namespace FileUtils
```

### example/deps/file_utils/src/load_store_row.cpp <a id="SS_3_1_26"></a>
```cpp
          1 #include <cassert>
          2 #include <iostream>
          3 #include <optional>
          4 #include <regex>
          5 
          6 #include "file_utils/load_store.h"
          7 #include "file_utils/load_store_row.h"
          8 
          9 namespace FileUtils {
         10 
         11 bool StoreToStream(std::ostream &os, std::vector<std::string> const &lines) {
         12   for (auto const &line : lines) {
         13     os << line;
         14   }
         15 
         16   return true;
         17 }
         18 
         19 std::optional<std::vector<std::string>> Load_Strings(std::istream &is) {
         20   auto content = std::vector<std::string>{};
         21   auto line = std::string{};
         22 
         23   while (std::getline(is, line)) {
         24     auto ss = std::ostringstream{};
         25 
         26     ss << line << std::endl;
         27     content.emplace_back(ss.str());
         28   }
         29 
         30   return content;
         31 }
         32 } // namespace FileUtils
```

### example/deps/file_utils/src/path_utils.cpp <a id="SS_3_1_27"></a>
```cpp
          1 #include <algorithm>
          2 #include <sstream>
          3 #include <utility>
          4 
          5 #include "file_utils/path_utils.h"
          6 
          7 namespace FileUtils {
          8 
          9 std::string ToStringPath(Path_t const &path) {
         10   auto pn = path.string();
         11 
         12   if (pn.size() == 0) {
         13     pn = "\"\"";
         14   }
         15 
         16   return pn;
         17 }
         18 
         19 std::string ToStringPaths(Paths_t const &paths, std::string_view sep,
         20                           std::string_view indent) {
         21   auto ss = std::ostringstream{};
         22   auto first = true;
         23 
         24   for (auto const &p : paths) {
         25     if (!std::exchange(first, false)) {
         26       ss << sep;
         27     }
         28 
         29     ss << indent << ToStringPath(p);
         30   }
         31 
         32   return ss.str();
         33 }
         34 
         35 std::string ToStringDirs2Srcs(Dirs2Srcs_t const &dirs2srcs) {
         36   auto ss = std::ostringstream{};
         37   auto first = bool{true};
         38 
         39   for (auto const &pair : dirs2srcs) {
         40     if (first) {
         41       first = false;
         42     } else {
         43       ss << std::endl;
         44     }
         45 
         46     ss << ToStringPath(pair.first) << std::endl;
         47     ss << ToStringPaths(pair.second, "\n", "    ") << std::endl;
         48   }
         49 
         50   return ss.str();
         51 }
         52 
         53 Paths_t NotDirs(Paths_t const &dirs) {
         54   auto ret = Paths_t{};
         55 
         56   std::copy_if(dirs.cbegin(), dirs.cend(), std::back_inserter(ret),
         57                [](auto const &dir) noexcept {
         58                  return !std::filesystem::is_directory(dir);
         59                });
         60 
         61   return ret;
         62 }
         63 
         64 Filename2Path_t GenFilename2Path(Paths_t const &paths) {
         65   auto ret = Filename2Path_t{};
         66 
         67   for (auto const &p : paths) {
         68     ret[p.filename()] = p;
         69   }
         70 
         71   return ret;
         72 }
         73 
         74 namespace {
         75 Path_t const current_dir{"."};
         76 
         77 size_t match_count(Path_t const &dir, Path_t const &src) {
         78   auto const dir_str = dir.string();
         79   auto const src_str = dir == current_dir ? "./" + src.string() : src.string();
         80 
         81   if (dir_str.size() >= src_str.size()) {
         82     return 0;
         83   }
         84 
         85   auto count = 0U;
         86   auto count_max = dir_str.size();
         87 
         88   for (; count < count_max; ++count) {
         89     if (dir_str[count] != src_str[count]) {
         90       break;
         91     }
         92   }
         93 
         94   if (count == count_max && src_str[count] == '/') {
         95     return count;
         96   }
         97 
         98   return 0;
         99 }
        100 
        101 Path_t select_package(Path_t const &src, Paths_t const &dirs) {
        102   Path_t const *best_match{nullptr};
        103   auto count_max = 0U;
        104 
        105   for (auto const &dir : dirs) {
        106     auto count = match_count(dir, src);
        107     if (count_max < count) {
        108       best_match = &dir;
        109       count_max = count;
        110     }
        111   }
        112 
        113   if (best_match == nullptr) {
        114     return Path_t("no_package");
        115   } else {
        116     return *best_match;
        117   }
        118 }
        119 
        120 Paths_t gen_parent_dirs(Path_t const dir) {
        121   auto ret = Paths_t{};
        122 
        123   for (auto p = dir.parent_path(), pp = p.parent_path(); !p.empty() && p != pp;
        124        p = pp, pp = p.parent_path()) {
        125     ret.push_front(p);
        126   }
        127 
        128   return ret;
        129 }
        130 
        131 // a/
        132 //   a0.c
        133 //   b/
        134 //     c/
        135 //       d/
        136 //         d.c
        137 // のようなファイ構造があった場合、
        138 // d2sには a、a/b/c/d が登録され、a/b、a/b/cは登録されていない。
        139 // a/b、a/b/cを埋めるのがpad_parent_dirsである。
        140 void pad_parent_dirs(Paths_t const &dirs, Dirs2Srcs_t &d2s) {
        141   for (auto const &dir : dirs) {
        142     auto parent_found = false;
        143 
        144     for (auto const &p : gen_parent_dirs(dir)) {
        145       if (!parent_found && d2s.count(p) != 0) {
        146         parent_found = true;
        147       } else if (parent_found && d2s.count(p) == 0) {
        148         d2s[p] = Paths_t();
        149       }
        150     }
        151   }
        152 }
        153 } // namespace
        154 
        155 Dirs2Srcs_t AssginSrcsToDirs(Paths_t const &dirs, Paths_t const &srcs) {
        156   auto ret = Dirs2Srcs_t{};
        157   auto add_dirs = Paths_t{};
        158 
        159   for (auto const &src : srcs) {
        160     auto dir = select_package(src, dirs);
        161 
        162     if (ret.count(dir) == 0) {
        163       ret[dir] = Paths_t();
        164       add_dirs.push_back(dir);
        165     }
        166     ret[dir].push_back(src);
        167   }
        168 
        169   pad_parent_dirs(add_dirs, ret);
        170 
        171   return ret;
        172 }
        173 
        174 Path_t NormalizeLexically(Path_t const &path) {
        175   // lexically_normalは"a/../b"を"b"にする
        176   // 最後の'/'を削除
        177   auto path_lex = Path_t(path.string() + '/').lexically_normal().string();
        178   path_lex.pop_back();
        179 
        180   if (path_lex.size() == 0) {
        181     return Path_t(".");
        182   }
        183   return path_lex;
        184 }
        185 
        186 void RemoveFile(Path_t const &filename) {
        187   if (std::filesystem::exists(filename)) {
        188     std::filesystem::remove(filename);
        189   }
        190 }
        191 } // namespace FileUtils
```

### example/deps/file_utils/ut/load_store_row_ut.cpp <a id="SS_3_1_28"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "file_utils/load_store.h"
          4 #include "file_utils/load_store_row.h"
          5 #include "file_utils/path_utils.h"
          6 
          7 namespace FileUtils {
          8 namespace {
          9 
         10 TEST(load_store, Row) {
         11   auto const row_exp = std::string{"ut_data/load_store/pkg_org"};
         12   auto const row_act = std::string{"ut_data/load_store/pkg_act"};
         13 
         14   RemoveFile(row_act);
         15 
         16   auto row_data0 = std::optional<std::vector<std::string>>{
         17       LoadFromFile(row_act, Load_Strings)};
         18 
         19   // row_actはないのでエラーなはず
         20   ASSERT_FALSE(row_data0);
         21 
         22   // ディレクトリなのでエラーなはず
         23   ASSERT_FALSE(StoreToFile("ut_data/app1", *row_data0, StoreToStream));
         24 
         25   row_data0 = LoadFromFile(row_exp, Load_Strings);
         26   ASSERT_TRUE(row_data0);
         27   ASSERT_TRUE(StoreToFile(row_act, *row_data0, StoreToStream));
         28 
         29   auto row_data1 = std::optional<std::vector<std::string>>{
         30       LoadFromFile(row_act, Load_Strings)};
         31   ASSERT_TRUE(row_data1);
         32 
         33   ASSERT_EQ(*row_data0, *row_data1);
         34 
         35   RemoveFile(row_act);
         36 }
         37 } // namespace
         38 } // namespace FileUtils
```

### example/deps/file_utils/ut/path_utils_ut.cpp <a id="SS_3_1_29"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "file_utils/load_store.h"
          4 #include "file_utils/load_store_row.h"
          5 #include "file_utils/path_utils.h"
          6 #include "logging/logger.h"
          7 
          8 #define SCAN_BUILD_ERROR 0
          9 
         10 #if SCAN_BUILD_ERROR == 1
         11 struct X {};
         12 void potential_leak(int a) {
         13   X *x{new X};
         14 
         15   if (a == 2) { // aが2ならメモリリーク
         16     return;
         17   }
         18 
         19   delete x;
         20 }
         21 #endif
         22 
         23 namespace FileUtils {
         24 namespace {
         25 
         26 TEST(path_utils, Logger) {
         27   auto log_file_org = "ut_data/load_store/logger_org";
         28   auto log_file_act = "ut_data/load_store/logger_act";
         29 
         30   RemoveFile(log_file_act);
         31 
         32   LOGGER_INIT(log_file_act);
         33   LOGGER(1);
         34   LOGGER("xyz", 3, 5);
         35 
         36   auto const dirs = Paths_t{"ut_data/app1",
         37                             "ut_data/app1/mod1",
         38                             "ut_data/app1/mod2",
         39                             "ut_data/app1/mod2/mod2_1",
         40                             "ut_data/app1/mod2/mod2_2",
         41                             "ut_data/app2"};
         42 
         43   LOGGER(ToStringPaths(dirs));
         44   LOGGER(dirs);
         45 
         46   Logging::Logger::Inst().Close();
         47 
         48   auto exp = std::optional<std::vector<std::string>>{
         49       LoadFromFile(log_file_org, Load_Strings)};
         50   ASSERT_TRUE(exp);
         51 
         52   auto act = std::optional<std::vector<std::string>>{
         53       LoadFromFile(log_file_act, Load_Strings)};
         54   ASSERT_TRUE(act);
         55 
         56   ASSERT_EQ(*exp, *act);
         57 
         58   RemoveFile(log_file_act);
         59 }
         60 
         61 TEST(path_utils, NotDirs) {
         62   {
         63     auto const dir_in = Paths_t{"ut_data/app1",
         64                                 "ut_data/app1/mod1",
         65                                 "ut_data/app1/mod2",
         66                                 "ut_data/app1/mod2/mod2_1",
         67                                 "ut_data/app1/mod2/mod2_2",
         68                                 "ut_data/app2"};
         69     auto const dir_act = Paths_t{NotDirs(dir_in)};
         70 
         71     ASSERT_EQ(Paths_t{}, dir_act);
         72   }
         73   {
         74     auto const dir_in = Paths_t{"ut_data/app1",
         75                                 "ut_data/app1/notdir",
         76                                 "ut_data/notdir2",
         77                                 "ut_data/app1/mod2/mod2_1",
         78                                 "ut_data/app1/mod2/mod2_2",
         79                                 "ut_data/app2"};
         80     auto const dir_act = Paths_t{NotDirs(dir_in)};
         81     auto const dir_exp = Paths_t{
         82         "ut_data/app1/notdir",
         83         "ut_data/notdir2",
         84     };
         85 
         86     ASSERT_EQ(dir_exp, dir_act);
         87   }
         88 }
         89 
         90 TEST(path_utils, NormalizeLexically) {
         91   // こうなるのでNormalizeLexicallyが必要
         92   ASSERT_EQ(Path_t("a"), Path_t("a"));
         93   ASSERT_NE(Path_t("a/"), Path_t("a"));
         94   ASSERT_EQ("a/", Path_t("x/../a/").lexically_normal().string());
         95   ASSERT_EQ("a", Path_t("x/../a").lexically_normal().string());
         96 
         97   // テストはここから
         98   ASSERT_EQ("a", NormalizeLexically("x/../a/").string());
         99   ASSERT_EQ("a", NormalizeLexically("./x/../a/").string());
        100   ASSERT_EQ("../a", NormalizeLexically(".././x/../a/").string());
        101   ASSERT_EQ("../a", NormalizeLexically(".././x/../a////").string());
        102   ASSERT_EQ("../a", NormalizeLexically(".././x/../a/./././").string());
        103 
        104   ASSERT_EQ("a", NormalizeLexically(Path_t("x/../a/")).string());
        105 
        106   ASSERT_EQ(".", NormalizeLexically(Path_t("./")).string());
        107   ASSERT_EQ(".", NormalizeLexically(Path_t(".")).string());
        108 }
        109 
        110 TEST(path_utils, GenFilename2Path) {
        111   auto const act_srcs =
        112       Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h",
        113               "ut_data/app1/a_1_cpp.cpp", "ut_data/app1/a_1_cpp.h",
        114               "ut_data/app1/a_2_c.C"};
        115 
        116   auto const act = GenFilename2Path(act_srcs);
        117 
        118   auto const exp = Filename2Path_t{
        119       {"a_1_c.c", "ut_data/app1/a_1_c.c"},
        120       {"a_1_c.h", "ut_data/app1/a_1_c.h"},
        121       {"a_1_cpp.cpp", "ut_data/app1/a_1_cpp.cpp"},
        122       {"a_1_cpp.h", "ut_data/app1/a_1_cpp.h"},
        123       {"a_2_c.C", "ut_data/app1/a_2_c.C"},
        124   };
        125 
        126   ASSERT_EQ(act, exp);
        127 }
        128 
        129 TEST(path_utils, AssginSrcsToDirs) {
        130   {
        131     auto const exp_dirs = Paths_t{"ut_data/app1",
        132                                   "ut_data/app1/mod1",
        133                                   "ut_data/app1/mod2",
        134                                   "ut_data/app1/mod2/mod2_1",
        135                                   "ut_data/app1/mod2/mod2_2",
        136                                   "ut_data/app2"};
        137 
        138     auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        139                                   "ut_data/app1/a_1_c.h",
        140                                   "ut_data/app1/a_1_cpp.cpp",
        141                                   "ut_data/app1/a_1_cpp.h",
        142                                   "ut_data/app1/a_2_c.C",
        143                                   "ut_data/app1/a_2_c.H",
        144                                   "ut_data/app1/a_2_cpp.cxx",
        145                                   "ut_data/app1/a_2_cpp.hpp",
        146                                   "ut_data/app1/a_3_cpp.cc",
        147                                   "ut_data/app1/mod1/mod1_1.cpp",
        148                                   "ut_data/app1/mod1/mod1_1.hpp",
        149                                   "ut_data/app1/mod1/mod1_2.hpp",
        150                                   "ut_data/app1/mod2/mod2_1.cpp",
        151                                   "ut_data/app1/mod2/mod2_1.hpp",
        152                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        153                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        154                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        155                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        156                                   "ut_data/app2/b_1.cpp",
        157                                   "ut_data/app2/b_1.h"};
        158 
        159     auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        160 
        161     auto const exp = Dirs2Srcs_t{
        162         {"ut_data/app1",
        163          {"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h",
        164           "ut_data/app1/a_1_cpp.cpp", "ut_data/app1/a_1_cpp.h",
        165           "ut_data/app1/a_2_c.C", "ut_data/app1/a_2_c.H",
        166           "ut_data/app1/a_2_cpp.cxx", "ut_data/app1/a_2_cpp.hpp",
        167           "ut_data/app1/a_3_cpp.cc"}},
        168         {"ut_data/app1/mod1",
        169          {"ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp",
        170           "ut_data/app1/mod1/mod1_2.hpp"}},
        171         {"ut_data/app1/mod2",
        172          {"ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
        173         {"ut_data/app1/mod2/mod2_1",
        174          {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        175           "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
        176         {"ut_data/app1/mod2/mod2_2",
        177          {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        178           "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
        179         {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
        180     };
        181 
        182     ASSERT_EQ(act, exp);
        183   }
        184   {
        185     auto const exp_dirs = Paths_t{".", "ut_data/app1/mod1"};
        186     auto const exp_srcs =
        187         Paths_t{"path_utils.cpp", "ut_data/app1/mod1/mod1_1.cpp",
        188                 "ut_data/app1/mod1/mod1_1.hpp"};
        189 
        190     auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        191 
        192     auto const exp = Dirs2Srcs_t{
        193         {".", {"path_utils.cpp"}},
        194         {"ut_data/app1/mod1",
        195          {"ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp"}},
        196     };
        197 
        198     ASSERT_EQ(act, exp);
        199   }
        200 }
        201 
        202 TEST(path_utils, PackageSrcMatcher2) {
        203   auto const exp_dirs =
        204       Paths_t{"ut_data", "ut_data/app1/mod2", "ut_data/app1/mod2/mod2_1",
        205               "ut_data/app1/mod2/mod2_2", "ut_data/app2"};
        206 
        207   auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        208                                 "ut_data/app1/a_1_c.h",
        209                                 "ut_data/app1/a_1_cpp.cpp",
        210                                 "ut_data/app1/a_1_cpp.h",
        211                                 "ut_data/app1/a_2_c.C",
        212                                 "ut_data/app1/a_2_c.H",
        213                                 "ut_data/app1/a_2_cpp.cxx",
        214                                 "ut_data/app1/a_2_cpp.hpp",
        215                                 "ut_data/app1/a_3_cpp.cc",
        216                                 "ut_data/app1/mod1/mod1_1.cpp",
        217                                 "ut_data/app1/mod1/mod1_1.hpp",
        218                                 "ut_data/app1/mod1/mod1_2.hpp",
        219                                 "ut_data/app1/mod2/mod2_1.cpp",
        220                                 "ut_data/app1/mod2/mod2_1.hpp",
        221                                 "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        222                                 "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        223                                 "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        224                                 "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        225                                 "ut_data/app2/b_1.cpp",
        226                                 "ut_data/app2/b_1.h"};
        227 
        228   auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        229 
        230   auto const exp = Dirs2Srcs_t{
        231       {"ut_data",
        232        {"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h",
        233         "ut_data/app1/a_1_cpp.cpp", "ut_data/app1/a_1_cpp.h",
        234         "ut_data/app1/a_2_c.C", "ut_data/app1/a_2_c.H",
        235         "ut_data/app1/a_2_cpp.cxx", "ut_data/app1/a_2_cpp.hpp",
        236         "ut_data/app1/a_3_cpp.cc", "ut_data/app1/mod1/mod1_1.cpp",
        237         "ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}},
        238       {"ut_data/app1", {}},
        239       {"ut_data/app1/mod2",
        240        {"ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
        241       {"ut_data/app1/mod2/mod2_1",
        242        {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        243         "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
        244       {"ut_data/app1/mod2/mod2_2",
        245        {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        246         "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
        247       {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
        248   };
        249 
        250   ASSERT_EQ(act, exp);
        251 }
        252 
        253 TEST(path_utils, PackageSrcMatcher3) {
        254   auto const exp_dirs = Paths_t{"ut_data/app1/mod2/mod2_1",
        255                                 "ut_data/app1/mod2/mod2_2", "ut_data/app2"};
        256 
        257   auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        258                                 "ut_data/app1/mod1/mod1_1.cpp",
        259                                 "ut_data/app1/mod1/mod1_1.hpp",
        260                                 "ut_data/app1/mod1/mod1_2.hpp",
        261                                 "ut_data/app1/mod2/mod2_1.cpp",
        262                                 "ut_data/app1/mod2/mod2_1.hpp",
        263                                 "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        264                                 "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        265                                 "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        266                                 "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        267                                 "ut_data/app2/b_1.cpp",
        268                                 "ut_data/app2/b_1.h"};
        269 
        270   auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        271 
        272   auto const exp = Dirs2Srcs_t{
        273       {"ut_data/app1/mod2/mod2_1",
        274        {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        275         "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
        276       {"ut_data/app1/mod2/mod2_2",
        277        {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        278         "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
        279       {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
        280       {"no_package",
        281        {"ut_data/app1/a_1_c.c", "ut_data/app1/mod1/mod1_1.cpp",
        282         "ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp",
        283         "ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
        284   };
        285 
        286   ASSERT_EQ(act, exp);
        287 }
        288 
        289 TEST(path_utils, ToString_Path) {
        290   {
        291     auto const exp_path = Path_t{"ut_data/app1/a_1_c.c"};
        292     auto const exp = std::string{"ut_data/app1/a_1_c.c"};
        293     auto const act = ToStringPath(exp_path);
        294 
        295     ASSERT_EQ(act, exp);
        296   }
        297   {
        298     auto const exp_path = Path_t{""};
        299     auto const exp = std::string{"\"\""};
        300     auto const act = ToStringPath(exp_path);
        301 
        302     ASSERT_EQ(act, exp);
        303   }
        304 }
        305 
        306 TEST(path_utils, ToString_Paths) {
        307   auto const exp_srcs =
        308       Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app1/mod1/mod1_1.cpp",
        309               "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        310               "ut_data/app1/mod2/mod2_1/mod2_1_1.h", "ut_data/app2/b_1.h"};
        311 
        312   auto const exp = std::string{"ut_data/app1/a_1_c.c "
        313                                "ut_data/app1/mod1/mod1_1.cpp "
        314                                "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp "
        315                                "ut_data/app1/mod2/mod2_1/mod2_1_1.h "
        316                                "ut_data/app2/b_1.h"};
        317   auto const act = ToStringPaths(exp_srcs, " ");
        318 
        319   ASSERT_EQ(act, exp);
        320 }
        321 } // namespace
        322 } // namespace FileUtils
```

### example/deps/lib/h/lib/nstd.h <a id="SS_3_1_30"></a>
```cpp
          1 #pragma once
          2 #include <algorithm>
          3 #include <fstream>
          4 #include <list>
          5 #include <string>
          6 #include <utility>
          7 #include <vector>
          8 
          9 namespace Nstd {
         10 template <typename T, size_t N>
         11 constexpr size_t ArrayLength(T const (&)[N]) noexcept {
         12   return N;
         13 }
         14 
         15 template <typename T> void SortUnique(std::vector<T> &v) {
         16   std::sort(v.begin(), v.end());
         17   auto result = std::unique(v.begin(), v.end());
         18   v.erase(result, v.end());
         19 }
         20 
         21 template <typename T> void SortUnique(std::list<T> &v) {
         22   v.sort();
         23   v.unique();
         24 }
         25 
         26 template <typename T>
         27 void Concatenate(std::vector<T> &v0, std::vector<T> &&v1) {
         28   for (auto &v1_elem : v1) {
         29     v0.insert(v0.end(), std::move(v1_elem));
         30   }
         31 }
         32 
         33 template <typename T> void Concatenate(std::list<T> &v0, std::list<T> &&v1) {
         34   v0.splice(v0.end(), std::move(v1));
         35 }
         36 
         37 template <typename F> class ScopedGuard {
         38 public:
         39   explicit ScopedGuard(F &&f) noexcept : f_{f} {}
         40   ~ScopedGuard() { f_(); }
         41   ScopedGuard(ScopedGuard const &) = delete;
         42   ScopedGuard &operator=(ScopedGuard const &) = delete;
         43 
         44 private:
         45   F f_;
         46 };
         47 
         48 inline std::string Replace(std::string in, std::string_view from,
         49                            std::string_view to) {
         50   auto pos = in.find(from);
         51 
         52   while (pos != std::string::npos) {
         53     in.replace(pos, from.length(), to);
         54     pos = in.find(from, pos + to.length());
         55   }
         56 
         57   return in;
         58 }
         59 
         60 //
         61 // operator<< for range
         62 //
         63 namespace Inner_ {
         64 //
         65 // exists_put_to_as_member
         66 //
         67 template <typename, typename = std::ostream &>
         68 struct exists_put_to_as_member : std::false_type {};
         69 
         70 template <typename T>
         71 struct exists_put_to_as_member<
         72     T, decltype(std::declval<std::ostream &>().operator<<(std::declval<T>()))>
         73     : std::true_type {};
         74 
         75 template <typename T>
         76 constexpr bool exists_put_to_as_member_v{exists_put_to_as_member<T>::value};
         77 
         78 //
         79 // exists_put_to_as_non_member
         80 //
         81 template <typename, typename = std::ostream &>
         82 struct exists_put_to_as_non_member : std::false_type {};
         83 
         84 template <typename T>
         85 struct exists_put_to_as_non_member<
         86     T, decltype(operator<<(std::declval<std::ostream &>(), std::declval<T>()))>
         87     : std::true_type {};
         88 
         89 template <typename T>
         90 constexpr bool exists_put_to_as_non_member_v{
         91     exists_put_to_as_non_member<T>::value};
         92 
         93 //
         94 // exists_put_to_v
         95 //
         96 template <typename T>
         97 constexpr bool exists_put_to_v{Nstd::Inner_::exists_put_to_as_member_v<T> ||
         98                                Nstd::Inner_::exists_put_to_as_non_member_v<T>};
         99 
        100 //
        101 // is_range
        102 //
        103 template <typename, typename = bool> struct is_range : std::false_type {};
        104 
        105 template <typename T>
        106 struct is_range<T, typename std::enable_if_t<
        107                        !std::is_array_v<T>,
        108                        decltype(std::begin(std::declval<T>()), bool{})>>
        109     : std::true_type {};
        110 
        111 template <typename T>
        112 struct is_range<T, typename std::enable_if_t<std::is_array_v<T>, bool>>
        113     : std::true_type {};
        114 
        115 //
        116 // is_range_v
        117 //
        118 template <typename T> constexpr bool is_range_v{is_range<T>::value};
        119 
        120 } // namespace Inner_
        121 
        122 //
        123 // operator<< for range
        124 //
        125 template <typename T>
        126 auto operator<<(std::ostream &os, T const &t) -> typename std::enable_if_t<
        127     Inner_::is_range_v<T> && !Inner_::exists_put_to_v<T>, std::ostream &> {
        128   auto first = true;
        129 
        130   for (auto const &i : t) {
        131     if (!std::exchange(first, false)) {
        132       os << ", ";
        133     }
        134     os << i;
        135   }
        136 
        137   return os;
        138 }
        139 } // namespace Nstd
```

### example/deps/lib/ut/nstd_ut.cpp <a id="SS_3_1_31"></a>
```cpp
          1 #include <filesystem>
          2 #include <list>
          3 #include <ostream>
          4 #include <regex>
          5 #include <string>
          6 
          7 #include "gtest_wrapper.h"
          8 
          9 #include "lib/nstd.h"
         10 
         11 namespace Nstd {
         12 namespace {
         13 
         14 TEST(Nstd, ArrayLength) {
         15   {
         16     char const *act[] = {"d", "a", "ab", "bcd"};
         17 
         18     ASSERT_EQ(4, ArrayLength(act));
         19   }
         20   {
         21     std::string const act[] = {"d", "a", "Ab"};
         22 
         23     ASSERT_EQ(3, ArrayLength(act));
         24   }
         25 }
         26 
         27 TEST(Nstd, SortUnique) {
         28   {
         29     auto act = std::vector<std::string>{"d", "a", "ab", "bcd"};
         30 
         31     SortUnique(act);
         32 
         33     ASSERT_EQ((std::vector<std::string>{"a", "ab", "bcd", "d"}), act);
         34   }
         35   {
         36     auto act = std::list<std::filesystem::path>{"d", "a", "Ab", "bcd"};
         37 
         38     SortUnique(act);
         39 
         40     ASSERT_EQ((std::list<std::filesystem::path>{"Ab", "a", "bcd", "d"}), act);
         41   }
         42 }
         43 
         44 TEST(Nstd, Concatenate) {
         45   {
         46     auto act0 = std::vector<std::string>{"d", "a", "ab"};
         47     auto act1 = std::vector<std::string>{"bcd", "ef"};
         48 
         49     Concatenate(act0, std::move(act1));
         50     ASSERT_EQ((std::vector<std::string>{"d", "a", "ab", "bcd", "ef"}), act0);
         51   }
         52   {
         53     auto act0 = std::list<std::filesystem::path>{"d", "a", "ab"};
         54     auto act1 = std::list<std::filesystem::path>{"bcd", "ef"};
         55 
         56     Concatenate(act0, std::move(act1));
         57     ASSERT_EQ((std::list<std::filesystem::path>{"d", "a", "ab", "bcd", "ef"}),
         58               act0);
         59   }
         60 }
         61 
         62 TEST(Nstd, ScopedGuard) {
         63   auto s = std::string{"not called"};
         64 
         65   {
         66     auto sg = ScopedGuard{[&s]() noexcept { s = "called"; }};
         67     ASSERT_EQ(s, "not called");
         68   }
         69 
         70   ASSERT_EQ(s, "called");
         71 }
         72 
         73 TEST(Nstd, Replace) {
         74   {
         75     auto in = std::string{"a-b-c-d"};
         76     auto act = Replace(in, "-", "/");
         77     ASSERT_EQ(act, "a/b/c/d");
         78   }
         79   {
         80     auto in = std::string{"a-b-c-d"};
         81     auto act = Replace(in, "-", "///////");
         82     ASSERT_EQ(act, "a///////b///////c///////d");
         83   }
         84   {
         85     auto in = std::string{"a-b-c-d"};
         86     auto act = Replace(in, "-", "");
         87     ASSERT_EQ(act, "abcd");
         88   }
         89 }
         90 
         91 TEST(stl_try, exclude) {
         92   auto dirs = std::list<std::string>{"A", "B", "A/e", "A/e/f", "B/xxx/ef"};
         93   auto exclude = std::string{R"(.*/e\b.*)"};
         94   auto const pattern = std::regex{exclude};
         95 
         96   dirs.remove_if([&pattern](auto const &d) {
         97     auto results = std::smatch{};
         98     return std::regex_match(d, results, pattern);
         99   });
        100 
        101   ASSERT_EQ(dirs, (std::list<std::string>{"A", "B", "B/xxx/ef"}));
        102 }
        103 } // namespace
        104 
        105 namespace Inner_ {
        106 namespace {
        107 class test_class_exits_put_to {};
        108 
        109 std::ostream &operator<<(std::ostream &os, test_class_exits_put_to) {
        110   return os;
        111 }
        112 
        113 class test_class_not_exits_put_to {};
        114 
        115 TEST(Nstd, exists_put_to_as_member) {
        116   static_assert(exists_put_to_as_member_v<bool>);
        117   static_assert(exists_put_to_as_member_v<char[3]>);
        118   static_assert(!exists_put_to_as_member_v<std::string>);
        119   static_assert(!exists_put_to_as_member_v<std::vector<int>>);
        120   static_assert(exists_put_to_as_member_v<std::vector<int> *>);
        121   static_assert(!exists_put_to_as_member_v<test_class_exits_put_to>);
        122   static_assert(!exists_put_to_as_member_v<test_class_not_exits_put_to>);
        123   static_assert(exists_put_to_as_member_v<test_class_not_exits_put_to[3]>);
        124   auto oss = std::ostringstream{};
        125   oss << test_class_exits_put_to{};
        126 }
        127 
        128 TEST(Template, exists_put_to_as_non_member) {
        129   static_assert(!exists_put_to_as_non_member_v<bool>);
        130   static_assert(exists_put_to_as_non_member_v<std::string>);
        131   static_assert(!exists_put_to_as_non_member_v<std::vector<int>>);
        132   static_assert(!exists_put_to_as_non_member_v<std::vector<int> *>);
        133   static_assert(exists_put_to_as_non_member_v<test_class_exits_put_to>);
        134   static_assert(!exists_put_to_as_non_member_v<test_class_not_exits_put_to>);
        135   static_assert(!exists_put_to_as_non_member_v<test_class_not_exits_put_to[3]>);
        136 }
        137 
        138 TEST(Template, exists_put_to_v) {
        139   static_assert(exists_put_to_v<bool>);
        140   static_assert(exists_put_to_v<std::string>);
        141   static_assert(!exists_put_to_v<std::vector<int>>);
        142   static_assert(exists_put_to_v<std::vector<int> *>);
        143   static_assert(exists_put_to_v<test_class_exits_put_to>);
        144   static_assert(!exists_put_to_v<test_class_not_exits_put_to>);
        145   static_assert(exists_put_to_v<test_class_not_exits_put_to[3]>);
        146 }
        147 
        148 TEST(Template, is_range) {
        149   static_assert(is_range_v<std::string>);
        150   static_assert(!is_range_v<int>);
        151   static_assert(is_range_v<int const[3]>);
        152   static_assert(is_range_v<int[3]>);
        153 }
        154 } // namespace
        155 } // namespace Inner_
        156 
        157 namespace {
        158 TEST(Template, PutTo) {
        159   {
        160     auto oss = std::ostringstream{};
        161     char c[] = "c3";
        162 
        163     oss << c;
        164     ASSERT_EQ("c3", oss.str());
        165   }
        166   {
        167     auto oss = std::ostringstream{};
        168     auto str = std::vector<std::string>{"1", "2", "3"};
        169 
        170     oss << str;
        171     ASSERT_EQ("1, 2, 3", oss.str());
        172   }
        173   {
        174     auto oss = std::ostringstream{};
        175     auto p = std::list<std::filesystem::path>{"1", "2", "3"};
        176 
        177     oss << p;
        178     ASSERT_EQ("\"1\", \"2\", \"3\"", oss.str());
        179   }
        180 }
        181 } // namespace
        182 } // namespace Nstd
```

### example/deps/logging/h/logging/logger.h <a id="SS_3_1_32"></a>
```cpp
          1 #pragma once
          2 
          3 #include <fstream>
          4 #include <iostream>
          5 #include <sstream>
          6 #include <string>
          7 #include <string_view>
          8 
          9 #include "lib/nstd.h"
         10 
         11 // @@@ sample begin 0:0
         12 
         13 namespace Logging {
         14 class Logger {
         15 public:
         16   static Logger &Inst(char const *filename = nullptr);
         17 
         18   template <typename HEAD, typename... TAIL>
         19   void Set(char const *filename, uint32_t line_no, HEAD const &head,
         20            TAIL... tails) {
         21     auto path = std::string_view{filename};
         22     size_t npos = path.find_last_of('/');
         23     auto basename =
         24         (npos != std::string_view::npos) ? path.substr(npos + 1) : path;
         25 
         26     os_.width(12);
         27     os_ << basename << ":";
         28 
         29     os_.width(3);
         30     os_ << line_no;
         31 
         32     set_inner(head, tails...);
         33   }
         34 
         35   // @@@ ignore begin
         36   void Close();
         37   Logger(Logger const &) = delete;
         38   Logger &operator=(Logger const &) = delete;
         39   // @@@ ignore end
         40 
         41 private:
         42   void set_inner() { os_ << std::endl; }
         43 
         44   template <typename HEAD, typename... TAIL>
         45   void set_inner(HEAD const &head, TAIL... tails) {
         46     using Nstd::operator<<;
         47     os_ << ":" << head;
         48     set_inner(tails...);
         49   }
         50 
         51   template <typename HEAD, typename... TAIL>
         52   void set_inner(char sep, HEAD const &head, TAIL... tails) {
         53     using Nstd::operator<<;
         54     os_ << sep << head;
         55     set_inner(tails...);
         56   }
         57 
         58   // @@@ ignore begin
         59   explicit Logger(char const *filename);
         60 
         61   std::ofstream ofs_{};
         62   std::ostream &os_;
         63 
         64   // @@@ ignore end
         65 };
         66 } // namespace Logging
         67 
         68 #define LOGGER_INIT(filename) Logging::Logger::Inst(filename)
         69 #define LOGGER(...) Logging::Logger::Inst().Set(__FILE__, __LINE__, __VA_ARGS__)
         70 // @@@ sample end
```

### example/deps/logging/src/logger.cpp <a id="SS_3_1_33"></a>
```cpp
          1 #include "logging/logger.h"
          2 
          3 namespace {
          4 class null_ostream : private std::streambuf, public std::ostream {
          5 public:
          6   static null_ostream &Inst() {
          7     static null_ostream inst;
          8     return inst;
          9   }
         10 
         11 protected:
         12   virtual int overflow(int c) {
         13     setp(buf_, buf_ + sizeof(buf_));
         14     return (c == eof() ? '\0' : c);
         15   }
         16 
         17 private:
         18   null_ostream() : std::ostream{this} {}
         19   char buf_[128];
         20 };
         21 
         22 std::ostream &init_os(char const *filename, std::ofstream &ofs) {
         23   if (filename == nullptr) {
         24     return std::cout;
         25   } else {
         26     if (std::string{filename}.size() == 0) {
         27       return null_ostream::Inst();
         28     } else {
         29       ofs.open(filename);
         30       return ofs;
         31     }
         32   }
         33 }
         34 } // namespace
         35 
         36 namespace Logging {
         37 Logger::Logger(char const *filename) : os_{init_os(filename, ofs_)} {}
         38 
         39 Logger &Logger::Inst(char const *filename) {
         40   static auto inst = Logger{filename};
         41 
         42   return inst;
         43 }
         44 
         45 void Logger::Close() {
         46   if (&std::cout != &os_) {
         47     ofs_.close();
         48   }
         49 }
         50 } // namespace Logging
```

### example/deps/logging/ut/logger_ut.cpp <a id="SS_3_1_34"></a>
```cpp
          1 #include <filesystem>
          2 
          3 #include "gtest_wrapper.h"
          4 
          5 #include "logging/logger.h"
          6 
          7 namespace {
          8 
          9 TEST(log, Logger) {
         10   // loggingのテストは他のライブラリで行う。
         11   // ここではコンパイルできることの確認のみ。
         12 
         13   LOGGER_INIT(nullptr);
         14   LOGGER(1);
         15   LOGGER("xyz", 3, 5);
         16 
         17   auto file = std::filesystem::path{"hehe"};
         18   LOGGER(file);
         19 }
         20 } // namespace
```

## etc <a id="SS_3_2"></a>
### example/deps/CMakeLists.txt <a id="SS_3_2_1"></a>
```
          1 cmake_minimum_required(VERSION 3.10)
          2 
          3 project(main_project)
          4 
          5 set(CMAKE_CXX_STANDARD 17)
          6 set(CMAKE_CXX_STANDARD_REQUIRED True)
          7 
          8 # CMakeオプションを定義
          9 option(USE_SANITIZERS "Enable sanitizers" OFF)
         10 
         11 # USE_SANITIZERS オプションをチェック
         12 if(USE_SANITIZERS)
         13     message(STATUS "Sanitizers are enabled")
         14     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address,leak,undefined,float-divide-by-zero,float-cast-overflow")
         15     set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fsanitize=address,leak,undefined,float-divide-by-zero,float-cast-overflow")
         16 else()
         17     message(STATUS "Sanitizers are disabled")
         18 endif()
         19 
         20 
         21 set(GTEST_DIR "../../googletest")
         22 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
         23 
         24 include_directories("${GTEST_DIR}/googletest/include")
         25 
         26 # googletestサブディレクトリを追加
         27 add_subdirectory(${GTEST_DIR} ${CMAKE_BINARY_DIR}/googletest EXCLUDE_FROM_ALL)
         28 
         29 add_subdirectory(lib)
         30 add_subdirectory(logging)
         31 add_subdirectory(file_utils)
         32 add_subdirectory(dependency)
         33 add_subdirectory(app)
         34 
         35 # すべてのテストを実行するカスタムターゲットを追加
         36 add_custom_target(tests
         37     DEPENDS app_ut dependency_ut file_utils_ut lib_ut logging_ut deps_it
         38     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
         39 )
         40 
```

### example/deps/dependency/CMakeLists.txt <a id="SS_3_2_2"></a>
```
          1 cmake_minimum_required(VERSION 3.10)
          2 
          3 project(dependency VERSION 1.0)
          4 
          5 # C++の標準を設定
          6 set(CMAKE_CXX_STANDARD 17)
          7 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
          8 
          9 # ライブラリのソースファイルを追加
         10 add_library(dependency STATIC
         11     src/arch_pkg.cpp
         12     src/cpp_deps.cpp
         13     src/cpp_dir.cpp
         14     src/cpp_src.cpp
         15     src/deps_scenario.cpp
         16     src/load_store_format.cpp
         17 )
         18 
         19 # @@@ sample begin 0:0
         20 
         21 # dependency.aをリンクするファイルに
         22 # ../dependency/h ../file_utils/h ../lib/h
         23 # のヘッダファイルを公開する
         24 
         25 target_include_directories(dependency PUBLIC ../dependency/h ../file_utils/h ../lib/h)
         26 # @@@ sample end
         27 
         28 # テスト用のソースファイルを追加して単一の実行ファイルを生成
         29 add_executable(dependency_ut_exe
         30     ut/arch_pkg_ut.cpp
         31     ut/cpp_deps_ut.cpp
         32     ut/cpp_dir_ut.cpp
         33     ut/cpp_src_ut.cpp
         34     ut/deps_scenario_ut.cpp
         35     ut/load_store_format_ut.cpp
         36 )
         37 
         38 # @@@ sample begin 1:0
         39 
         40 # dependency_ut_exeはdependency.aの単体テスト
         41 # dependency_ut_exeが使用するライブラリのヘッダは下記の記述で公開される
         42 target_link_libraries(dependency_ut_exe dependency file_utils logging gtest gtest_main)
         43 
         44 # dependency_ut_exeに上記では公開範囲が不十分である場合、
         45 # dependency_ut_exeが使用するライブラリのヘッダは下記の記述で限定的に公開される
         46 # dependency_ut_exeにはdependency/src/*.hへのアクセスが必要
         47 target_include_directories(dependency_ut_exe PRIVATE ../../../deep/h src)
         48 # @@@ sample end
         49 
         50 # テストを追加
         51 enable_testing()
         52 add_test(NAME dependency_ut COMMAND dependency_ut_exe)
         53 
         54 add_custom_target(dependency_ut_copy_test_data
         55     COMMAND ${CMAKE_COMMAND} -E copy_directory 
         56     ${CMAKE_SOURCE_DIR}/ut_data $<TARGET_FILE_DIR:dependency_ut_exe>/ut_data
         57 )
         58 
         59 # カスタムターゲットを追加して、ビルド後にテストを実行
         60 add_custom_target(dependency_ut
         61     COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
         62     DEPENDS dependency_ut_exe dependency_ut_copy_test_data
         63 )
         64 
```

### example/deps/file_utils/CMakeLists.txt <a id="SS_3_2_3"></a>
```
          1 cmake_minimum_required(VERSION 3.10)
          2 
          3 project(file_utils VERSION 1.0)
          4 
          5 # C++の標準を設定
          6 set(CMAKE_CXX_STANDARD 17)
          7 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
          8 
          9 add_library(file_utils STATIC
         10     src/load_store_row.cpp
         11     src/path_utils.cpp
         12 )
         13 
         14 target_include_directories(file_utils PUBLIC ../file_utils/h)
         15 
         16 add_executable(file_utils_ut_exe ut/load_store_row_ut.cpp ut/path_utils_ut.cpp)
         17 
         18 target_link_libraries(file_utils_ut_exe file_utils logging gtest gtest_main)
         19 
         20 target_include_directories(file_utils_ut_exe PRIVATE h ../../../deep/h ../logging/h ../lib/h)
         21 
         22 add_custom_command(TARGET file_utils_ut_exe POST_BUILD
         23     COMMAND ${CMAKE_COMMAND} -E copy_directory
         24     ${CMAKE_SOURCE_DIR}/ut_data $<TARGET_FILE_DIR:file_utils_ut_exe>/ut_data
         25 )
         26 
         27 enable_testing()
         28 add_test(NAME file_utils_ut COMMAND file_utils_ut_exe)
         29 
         30 add_custom_target(file_utils_ut_copy_test_data
         31     COMMAND ${CMAKE_COMMAND} -E copy_directory 
         32     ${CMAKE_SOURCE_DIR}/ut_data $<TARGET_FILE_DIR:file_utils_ut_exe>/ut_data
         33 )
         34 
         35 # カスタムターゲットを追加して、ビルド後にテストを実行
         36 add_custom_target(file_utils_ut
         37     COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
         38     DEPENDS file_utils_ut_exe file_utils_ut_copy_test_data
         39 )
         40 
```

### example/deps/lib/CMakeLists.txt <a id="SS_3_2_4"></a>
```
          1 cmake_minimum_required(VERSION 3.10)
          2 
          3 project(lib VERSION 1.0)
          4 
          5 # C++の標準を設定
          6 set(CMAKE_CXX_STANDARD 17)
          7 set(CMAKE_CXX_STANDARD_REQUIRED True)
          8 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
          9 
         10 add_executable(lib_ut_exe ut/nstd_ut.cpp)
         11 
         12 if(NOT TARGET gtest)
         13     message(FATAL_ERROR "gtest target not found. Make sure googletest is added at the top level CMakeLists.txt")
         14 endif()
         15 
         16 target_include_directories(lib_ut_exe PRIVATE h ../../h/ ../../../deep/h)
         17 target_link_libraries(lib_ut_exe gtest gtest_main)
         18 
         19 enable_testing()
         20 add_test(NAME lib_ut COMMAND lib_ut_exe)
         21 
         22 add_custom_target(lib_ut
         23     COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
         24     DEPENDS lib_ut_exe
         25 )
         26 
```

### example/deps/logging/CMakeLists.txt <a id="SS_3_2_5"></a>
```
          1 #logging/CMakeLists.txt
          2 
          3 cmake_minimum_required(VERSION 3.10)
          4 
          5 project(logging VERSION 1.0)
          6 
          7 # C++の標準を設定
          8 set(CMAKE_CXX_STANDARD 17)
          9 set(CMAKE_CXX_STANDARD_REQUIRED True)
         10 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
         11 
         12 add_library(logging STATIC src/logger.cpp)
         13 
         14 target_include_directories(logging PUBLIC h ../lib/h)
         15 
         16 add_executable(logging_ut_exe ut/logger_ut.cpp)
         17 
         18 target_include_directories(logging_ut_exe PRIVATE ../../../deep/h ../lib/h)
         19 target_link_libraries(logging_ut_exe logging gtest gtest_main)
         20 
         21 enable_testing()
         22 add_test(NAME logging_ut COMMAND logging_ut_exe)
         23 
         24 add_custom_target(logging_ut
         25     COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
         26     DEPENDS logging_ut_exe
         27 )
         28 
```



