<!-- ./md/sample_code.md -->
# Sample Code <a id="SS_23"></a>
## vim <a id="SS_23_1"></a>
### vim_config/README.md <a id="SS_23_1_1"></a>
```vim
          1 # このリポジトリの目的
          2 wsl-ubuntu vim/nvim、cygwin vim、windows gvim/nvim/nvim-qtの設定方法や設定ファイルを保存する。
          3 
          4 
          5 # このリポジトリのファイル
          6 ## README.md
          7 このファイル。
          8 
          9 ## ./nvimディレクトリ
         10 
         11 |ファイル名        |内容                              |
         12 |:-----------------|:---------------------------------|
         13 |nvim/init.vim     |nvimから最初に読み込まれる        |
         14 |nvim/org.vim      |オリジナルの設定                  |
         15 |nvim/package.vim  |deinを使用した外部パッケージの設定|
         16 |nvim/plugin/      |自作プラグイン                    |
         17 |nvim/autoload/    |自作プラグインのオートロード      |
         18 |nvim/rplugin/     |自作プラグイン                    |
         19 |nvim/ftplugin/    |filetype別プラグイン              |
         20 |nvim/cheatsheet.md|自分用ヘルプ。:Cheatで表示        |
         21 
         22 ## ./vimディレクトリ
         23 |ファイル名|内容                                             |
         24 |:---------|:------------------------------------------------|
         25 |vim/vimrc |~/.vimrcにコピーかシンボリックリンクを張って使用 |
         26 |vim/gimrc |~/.gvimrcにコピーかシンボリックリンクを張って使用|
         27 
         28 ## その他
         29 |ファイル名|内容                                                                                 |
         30 |:---------|:------------------------------------------------------------------------------------|
         31 |vim.sh    |bashrc等からsource                                                                   |
         32 |inputrc   |readline(gdb)を使用するアプリケーションのrcファイル。~/.inputrcにコピーして使用する。|
         33 
         34 
         35 # 環境変数
         36 ここで説明する環境変数は下記のvim系プログラムを初期設定をするためのものである。
         37 * ubuntu上のvim、nvim
         38 * cygwin上のvim
         39 * windows上のgvim、nvim、nvim-qt
         40 * cygwinターミナルから起動されたwindows上のgvim、nvim、nvim-qt
         41 
         42 下記の環境変数XDG_CONFIG_HOMEはすべて同一の実態(ディレクトリ)を指している。
         43 
         44 環境変数VIMやVIMRUNTIMEは設定しない。設定しない場合、
         45 * windows版gvimでは、
         46     * VIMは、'$HOME/.vim'がセットされる。
         47     * VIMRUNTIMEは、'$HOME/.vim/vimNN'がセットされる。
         48 
         49 * windows版nvim-qでは、Neovimにバンドルされているパッケージが入っているディレクトリが
         50   VIMやVIMRUNTIMEにセットされる。
         51 
         52 ## wsl-ubuntu
         53 * .bashrcに下記を追加する。
         54 
         55         export XDG_CONFIG_HOME=~/.config
         56         source $XDG_CONFIG_HOME/vim.sh
         57 
         58 ## cygwin
         59 * .bashrcに下記を追加する。
         60 
         61         # LINUX_HOMEはubuntuのホームディレクトリを指定
         62         export LINUX_HOME=/cygdrive/c/XXX
         63         export XDG_CONFIG_HOME=$LINUX_HOME/.config
         64         source $XDG_CONFIG_HOME/vim.sh
         65 
         66 ## windows
         67 * 環境変数に以下を追加する
         68 
         69         # XXXは上記と同じものを指定
         70         # YYYはcygwinのホームディレクトリを指定
         71         XDG_CONFIG_HOME C:\XXX\.config
         72         HOME C:\cygwin64\home\YYY
         73 
         74 
         75 # インストール
         76 1. 上記「環境変数」に従って環境変数、bashrcを設定
         77 2. このリポジトリを'$LINUX_HOME/.confg'にgit clone
         78 3. https://github.com/Shougo/dein.vim
         79    に従ってdeinを'$LINUX_HOME/.config/nvim_pkg/dein'にインストール
         80 4. 外部パッケージのインストールのために、wsl-ubuntu nvim立ち上げて:call deine#install()を実行
         81 5. cygwin vimの設定として、'$LINUX_HOME/.confg/vim/vimrc'をcygwinのホームディレクトリの
         82    .vimrcにコピーするかシンボリックリンクを張る。
         83 6. windows gvimの設定として、'$LINUX_HOME/.confg/vim/gvimrc'をcygwinのホームディレクトリの
         84    .gvimrcにコピーするかシンボリックリンクを張る。
         85 
         86 
         87 # 現在の問題点
         88 * パス形式の違いでwindows nvim/nvim-qtから動作しないプラグインがある。
         89 * cygwin vimはpython3対応でコンパイルされていないため、pythonが必要なプラグインは動作しない。
         90 * deinから設定したvim-fugitiveはcygwin vimでは動作しないため、
         91   https://github.com/tpope/vim-fugitive
         92   に書いてある設定が必要である。
         93 
         94 
         95 # スクリプト読み込みのデバッグ
         96 |コマンド                      |意味                                      |
         97 |:-----------------------------|:-----------------------------------------|
         98 |:echo $MYVIMRC                |最初に読み込まれる設定ファイルの表示      |
         99 |:scriptnames                  |現在読み込まれているスクリプトファイル一覧|
        100 |:let @a=execute('scriptnames')|scriptnamesの出力をレジスタaに取り込む    |
        101 |:checkhealt                   |足りないパッケージや設定等のチェック      |
```

### vim_config/inputrc <a id="SS_23_1_2"></a>
```vim
          1 set editing-mode vi
          2 set completion-ignore-case on
          3 set show-all-if-unmodified on
```

### vim_config/nvim/autoload/buffers.vim <a id="SS_23_1_3"></a>
```vim
          1 let s:buffers_buffer = 'Buffers'
          2 
          3 function! s:line(num, buff_name)
          4     if a:buff_name == s:buffers_buffer
          5         return printf("%3d [%s]\n", a:num, a:buff_name)
          6     else
          7         return printf("%3d %s\n", a:num, a:buff_name)
          8     endif
          9 endfunction
         10 
         11 function! s:load_buffers_list()
         12     let l:line = line('.')
         13     let l:col = col('.')
         14 
         15     let buffs = split(execute('buffers'), "\n")
         16 
         17     setlocal modifiable
         18 
         19     silent execute ':%delete'
         20     for b in buffs
         21         let new_b = substitute(b, '^ *\(\d\+\).*\"\(.*\)\".*', { m -> s:line(m[1], m[2])}, 'g')
         22         silent execute ':normal i' . new_b 
         23     endfor
         24     silent execute ':$delete'
         25 
         26     setlocal modifiable
         27     call cursor(l:line, l:col)
         28 endfunction
         29 
         30 function! buffers#close_buff(force)
         31     let word = expand("<cword>")
         32 
         33     if word =~ '\d\+'
         34         let to_delete = bufname(str2nr(word))
         35     elseif word =~ '.\+'
         36         let to_delete = word
         37     else
         38         echo 'no file'
         39         return
         40     endif
         41 
         42     if to_delete == s:buffers_buffer
         43         execute 'bdelete!' . word
         44     else
         45         let bwipeout = 'bwipeout' . (a:force == 0 ? ' ' : '! ')
         46         execute bwipeout . word
         47         call s:load_buffers_list()
         48     endif
         49 endfunction
         50 
         51 function! buffers#open_buff()
         52     let word = expand("<cword>")
         53 
         54     if word =~ '\d\+'
         55         execute 'buffer ' . word
         56     elseif word =~ '.\+'
         57         execute 'buffer ' . word
         58     else
         59         echo 'no file'
         60     endif
         61 endfunction
         62 
         63 function! s:key_map() abort
         64     nnoremap <silent> <buffer> <Plug>(buffers-delete) :call buffers#close_buff(0)<CR>
         65     nmap <buffer> d <Plug>(buffers-delete)
         66 
         67     nnoremap <silent> <buffer> <Plug>(buffers-delete-force) :call buffers#close_buff(1)<CR>
         68     nmap <buffer> D <Plug>(buffers-delete-force)
         69 
         70     nnoremap <silent> <buffer> <Plug>(buffers-open) :call buffers#open_buff()<CR>
         71     nmap <buffer> o <Plug>(buffers-open)
         72 
         73     nnoremap <silent> <buffer> <Plug>(buffers-reload) :call buffers#begin()<CR>
         74     nmap <buffer> r <Plug>(buffers-reload)
         75 endfunction
         76 
         77 function! buffers#begin()
         78     let winid = bufwinid(s:buffers_buffer)
         79     if winid isnot# -1
         80         call win_gotoid(winid)
         81     else
         82         execute 'new' s:buffers_buffer
         83         set buftype=nofile
         84         set noswapfile
         85         call s:key_map()
         86     endif
         87     call s:load_buffers_list()
         88 endfunction
```

### vim_config/nvim/autoload/cd.vim <a id="SS_23_1_4"></a>
```vim
          1 function! s:is_term()
          2     let bn = bufname("%")
          3     if bn =~ 'term://'
          4         return 1
          5     else
          6         return 0
          7     endif
          8 endfunction
          9 
         10 function! cd#find_dir_candidate()
         11     for i in range(50)
         12         silent execute 'normal "uyy'
         13         let reg=@u
         14         if reg =~ 'ichiro@[^ ]\+ \~.*'
         15             return substitute(reg, 'ichiro@[^ ]\+', '', '') 
         16         endif
         17         silent execute 'normal k'
         18     endfor
         19 
         20     return ''
         21 endfunction
         22 
         23 
         24 function! cd#change_dir()
         25     if s:is_term() == 1
         26         let dir_candidate=cd#find_dir_candidate()
         27 
         28         if dir_candidate == ''
         29             echo "no dir candidate"
         30         else
         31             silent execute ':cd ' . dir_candidate
         32         endif
         33     else
         34         silent execute ':cd %:h'
         35     endif
         36 endfunction
```

### vim_config/nvim/autoload/git_diff.vim <a id="SS_23_1_5"></a>
```vim
          1 let s:git_diff_buffer = 'GIT DIFF'
          2 let s:git_diff_buffer_cur =''
          3 let s:git_diff_buffer_new =''   " .newと表示されるが実際には改定前ファイル
          4 
          5 set patchexpr=git_diff#patch()
          6 
          7 function! git_diff#patch() abort
          8     silent execute '!patch -R  -o ' . v:fname_out .  ' ' . v:fname_in . ' < ' . v:fname_diff
          9 endfunction
         10 
         11 function! s:echo_err(msg) abort
         12   echohl ErrorMsg
         13   echomsg 'git_diff.vim:' a:msg
         14   echohl None
         15 endfunction
         16 
         17 " pattern : 0       just changed
         18 "         : 1       change filename
         19 function! s:modified_pattern(pattern) abort
         20     if  a:pattern == 0
         21         return '^[ADMU? ][DMU? ] \+'
         22     elseif  a:pattern == 1
         23         return 'R[M ] \+.* -> '
         24     endif
         25     call s:echo_err('modified_pattern wrong')
         26 endfunction
         27 
         28 function! s:get_target_name() abort
         29     let l:line=getline(".")
         30 
         31     if match(l:line, s:modified_pattern(0)) isnot# -1
         32         return substitute(l:line, s:modified_pattern(0), "", "")
         33     elseif match(l:line, s:modified_pattern(1)) isnot# -1
         34         return substitute(l:line, s:modified_pattern(1), "", "")
         35     else
         36         call s:echo_err(l:line . ' :this file is not modefied')
         37         return ''
         38     endif
         39 endfunction
         40 
         41 function! s:git_diff(patch_target, patch_file_name, from_head) abort
         42     if a:from_head == 0
         43         silent execute '!git diff ' .  a:patch_target .  ' > ' .  a:patch_file_name
         44     else
         45         silent execute '!git diff HEAD ' .  a:patch_target .  ' > ' .  a:patch_file_name
         46     endif
         47 endfunction
         48 
         49 function! s:each(line1, line2, func_ref) abort
         50     let l:col = col('.')
         51 
         52     for i in range(a:line1, a:line2)
         53         call cursor(i, l:col)
         54         call a:func_ref()
         55     endfor
         56 endfunction
         57 
         58 function! s:launch_file() abort
         59     let l:target=s:get_target_name()
         60 
         61     if g:os == 'linux'
         62         silent execute '!wslstart ' .  l:target
         63     else 
         64         if g:os == 'cygwin'
         65             silent execute '!wslstart ' .  l:target
         66         else
         67             echo 'not support launch'
         68         endif
         69     endif
         70 endfunction
         71 
         72 function! git_diff#launch_file(line1, line2) abort
         73     call s:each(a:line1, a:line2, function('s:launch_file'))
         74 endfunction
         75 
         76 
         77 function! s:git_add() abort
         78     let l:target=s:get_target_name()
         79 
         80     silent execute '!git add ' .  l:target
         81     call git_diff#make_list_load()
         82 endfunction
         83 
         84 function! git_diff#git_add(line1, line2) abort
         85     call s:each(a:line1, a:line2, function('s:git_add'))
         86 endfunction
         87 
         88 function! s:git_reset() abort
         89     let l:target=s:get_target_name()
         90 
         91     if len(l:target) == 0
         92         return
         93     endif
         94 
         95     silent execute '!git reset ' .  l:target
         96     call git_diff#make_list_load()
         97 endfunction
         98 
         99 function! git_diff#git_reset(line1, line2) abort
        100     call s:each(a:line1, a:line2, function('s:git_reset'))
        101 endfunction
        102 
        103 function! git_diff#make_list_load() abort
        104     setlocal modifiable
        105 
        106     let l:line = line('.')
        107     let l:col = col('.')
        108     silent execute ':%delete'
        109     silent execute 'r! git status -s'
        110     silent execute ':1delete'
        111     call cursor(l:line, l:col)
        112 
        113     setlocal nomodifiable
        114 endfunction
        115 
        116 function! s:key_map_end() abort
        117     delcommand GitAdd
        118     delcommand GitReset
        119 endfunction
        120 
        121 function! s:key_map_begin() abort
        122     command! -range GitAdd :call git_diff#git_add(<line1>, <line2>)
        123     map <silent> <buffer> a :GitAdd<CR>
        124 
        125     command! -range LauchFile :call git_diff#launch_file(<line1>, <line2>)
        126     map <silent> <buffer> L :LauchFile<CR>
        127 
        128     command! -range GitReset :call git_diff#git_reset(<line1>, <line2>)
        129     map <silent> <buffer> r :GitReset<CR>
        130 
        131     nnoremap <silent> <buffer> <Plug>(diff-open) :<C-u>call git_diff#show_diff(0, 0)<CR>
        132     nmap <buffer> d <Plug>(diff-open)
        133 
        134     nnoremap <silent> <buffer> <Plug>(diff-open-V) :<C-u>call git_diff#show_diff(1, 0)<CR>
        135     nmap <buffer> vd <Plug>(diff-open-V)
        136 
        137     nnoremap <silent> <buffer> <Plug>(diff-open-h) :<C-u>call git_diff#show_diff(0, 1)<CR>
        138     nmap <buffer> h <Plug>(diff-open-h)
        139 
        140     nnoremap <silent> <buffer> <Plug>(diff-open-Vh) :<C-u>call git_diff#show_diff(1, 1)<CR>
        141     nmap <buffer> vh <Plug>(diff-open-Vh)
        142 
        143     nnoremap <silent> <buffer> <Plug>(diff-list-close) :<C-u>call git_diff#end()<CR>
        144     nmap <buffer> <C-Q> <Plug>(diff-list-close)
        145 
        146     nnoremap <silent> <buffer> <Plug>(diff-reload) :<C-u>call git_diff#make_list_load()<CR>
        147     nmap <buffer> s <Plug>(diff-reload)
        148 
        149     nnoremap <silent> <buffer> <Plug>(git-commit) :!git commit -m 
        150     nmap <buffer> c <Plug>(git-commit)
        151 endfunction
        152 
        153 "vertial    : 0 normal split to show diff buffers
        154 "           : 1 virtial split to show diff buffers
        155 "from_head  : 0 git diff 
        156 "           : 1 git diff HEAD
        157 function! git_diff#show_diff(vertical, from_head) abort
        158     call git_diff#show_diff_off()
        159 
        160     let l:target=s:get_target_name()
        161 
        162     if getftime(l:target) == -1
        163         s:echo_err('file not exits')
        164     endif
        165 
        166     let s:git_diff_buffer_cur = l:target
        167     let s:git_diff_buffer_new = l:target . '.new'
        168 
        169     let l:temp_file = tempname()
        170     call s:git_diff(l:target, l:temp_file, a:from_head)
        171 
        172     execute ':sp'
        173 	execute ':e ' . l:target
        174 
        175     if a:vertical == 0
        176 	    execute ':diffpatch ' . l:temp_file
        177 
        178         " 上バッファがオリジナル。下バッファが変更後ファイル
        179         execute "normal \<C-w>j"
        180     else
        181 	    execute ':vert diffpatch ' . l:temp_file
        182 
        183         " 左バッファがオリジナル。右バッファが変更後ファイル
        184         execute "normal \<C-w>l"
        185     endif
        186 
        187     call delete(l:temp_file)
        188 endfunction
        189 
        190 function! git_diff#show_diff_off()
        191     execute ':diffoff!'
        192 
        193     if s:git_diff_buffer_cur != ''
        194         let winid = bufwinid(s:git_diff_buffer_cur)
        195 
        196         if winid isnot# -1
        197             call win_gotoid(winid)
        198             :quit
        199         endif
        200 
        201         let s:git_diff_buffer_cur = ''
        202     endif
        203 
        204     if s:git_diff_buffer_new != ''
        205         let winid = bufwinid(s:git_diff_buffer_new)
        206 
        207         if winid isnot# -1
        208             call win_gotoid(winid)
        209             execute 'bwipeout! ' . s:git_diff_buffer_new
        210         endif
        211 
        212         let s:git_diff_buffer_new = ''
        213     endif
        214 endfunction
        215 
        216 function! git_diff#begin(resize) abort
        217     let winid = bufwinid(s:git_diff_buffer)
        218     if winid isnot# -1
        219         call win_gotoid(winid)
        220     else
        221         execute 'edit' s:git_diff_buffer
        222         set buftype=nofile
        223         set noswapfile
        224         setlocal nomodifiable
        225 
        226         call s:key_map_begin()
        227         call git_diff#make_list_load()
        228     endif
        229 
        230     if a:resize != 0
        231         execute ":only"
        232         let l:lines=&lines
        233         echo l:lines
        234         if l:lines < 50
        235             execute ":set lines=50"
        236         endif
        237         execute ":set columns=201"
        238     endif
        239 
        240 endfunction
        241 
        242 function! git_diff#end()
        243     call git_diff#show_diff_off()
        244     call s:key_map_end()
        245     bwipeout!
        246 endfunction
        247 
```

### vim_config/nvim/autoload/git_session.vim <a id="SS_23_1_6"></a>
```vim
          1 function! s:get_git_top()
          2     let top = system('git rev-parse --show-toplevel')
          3     return substitute(top, "\n", '/', 'g')
          4 endfunction
          5 
          6 let s:git_session_top = s:get_git_top()
          7 let s:git_session_file = s:git_session_top . 'Session.vim'
          8 
          9 function! s:get_dirs() abort
         10     " ディレクトリのみを抽出
         11     let dir_filter = '|sed -e /^[^/]\\+$/d  -e  s\@/[^/]\\+$\@\@g | sort | uniq'
         12     let dirs_str = system("git ls-files --full-name " . s:git_session_top . dir_filter)
         13 
         14     let dirs_list = split(dirs_str, "\n")
         15 
         16     let full_dirs = map(dirs_list, 's:git_session_top . v:val')
         17 
         18     call add(full_dirs, s:git_session_top)
         19 
         20     return full_dirs
         21 endfunction
         22 
         23 function! git_session#set_path()
         24     let dirs = s:get_dirs()
         25     let &path ='./,/usr/include/c++/9/,' . join(dirs, ',') 
         26 
         27     let tag_dirs = map(dirs, 'v:val . "tags"')
         28     let &tags ='tags,./tags,' .  join(tag_dirs, ',')
         29 endfunction
         30 
         31 function! git_session#begin() abort
         32     let top = s:get_git_top()
         33 
         34     if top != s:git_session_top
         35         echo 'must be on the dir under ' . s:git_session_top
         36         return
         37     endif
         38 
         39     try
         40         execute 'source ' . s:git_session_file
         41     catch
         42         echo 'no session file'
         43     endtry
         44     call git_session#set_path()
         45 endfunction
         46 
         47 function! git_session#dir() abort
         48     echo s:git_session_top
         49 endfunction
         50 
         51 function! git_session#make() abort
         52     let top = s:get_git_top()
         53 
         54     if top != s:git_session_top
         55         echo 'must be on the dir under ' . s:git_session_top
         56         return
         57     endif
         58 
         59     execute 'mksession! ' . s:git_session_file
         60 endfunction
         61 
         62 function! git_session#new_session() abort
         63     let s:git_session_top = s:get_git_top()
         64     let s:git_session_file = s:git_session_top . 'Session.vim'
         65     call git_session#begin()
         66 endfunction
```

### vim_config/nvim/autoload/grep.vim <a id="SS_23_1_7"></a>
```vim
          1 function s:grep(target, args_for_dir)
          2     let ignore_case=&ic
          3     if l:ignore_case == 0
          4         let ic_str = ''
          5     else
          6         let ic_str = '-i '
          7     end
          8     execute ':grep -R ' . l:ic_str . a:args_for_dir . ' "' . a:target . '"' 
          9 endfunction
         10 
         11 function grep#grep(...)
         12     let args_for_dir = s:make_args_for_dir(a:000)
         13     let l:target=@/
         14     call s:grep(l:target, args_for_dir)
         15 endfunction
         16 
         17 function grep#grepp(pattern, ...)
         18     let args_for_dir = s:make_args_for_dir(a:000)
         19     call s:grep(a:pattern, args_for_dir)
         20 endfunction
         21 
         22 function s:make_include(array)
         23     let beg='--include="*.'
         24     let end='"'
         25     let inc = map(a:array,  'l:beg . v:val . l:end')
         26     return join(inc)
         27 endfunction
         28 
         29 function! s:make_args_for_dir(args)
         30   let res = []
         31   call extend(res, a:args)
         32 
         33   if len(res) == 0
         34     return s:make_include(['[chCH]', 'cpp', 'sh', 'rb', 'py', 'vim', 'md', 'pu'])
         35   else
         36     if len(res) == 1 && res[0] == '-'
         37         return '--exclude-dir=".git"'
         38     else
         39         return s:make_include(res)
         40     endif
         41   end
         42 endfunction
         43 
```

### vim_config/nvim/autoload/multi_hl.vim <a id="SS_23_1_8"></a>
```vim
          1 function! multi_hl#add_word(word, row)
          2 
          3     let curr = @/
          4     if a:row
          5         let new_word = a:word
          6     else
          7         let new_word = '\<' . a:word . '\>'
          8     endif
          9 
         10     if len(curr) != 0
         11         let search = curr . '\|' . new_word
         12     else
         13         let search = new_word
         14     endif
         15 
         16     let @/ = search
         17 
         18 endfunction
         19 
         20 function! multi_hl#clear()
         21     let @/ = ''
         22 endfunction
```

### vim_config/nvim/autoload/next_file.vim <a id="SS_23_1_9"></a>
```vim
          1 " カレントファイルがxxx_yyy_zzz.cppだったとすると、
          2 "   del_num     :0      エクステンションを取ったxxx_yyy_zzzに*を付けてglob
          3 "               :5      xxx_yyy_z*をglob
          4 
          5 function! s:make_stem(curr_file, del_num) abort
          6     if a:del_num == 0
          7         let stem = expand('%:r')
          8     else
          9         let name_len = len(a:curr_file)
         10 
         11         if name_len > a:del_num
         12             let name_len -= a:del_num
         13         else
         14             let name_len = 1
         15         endif
         16 
         17         let stem = expand('%')[0 : name_len]
         18     endif
         19 
         20     " ファイル名がxxx_ut.(cpp|h)だった場合の調整
         21     return substitute(stem, "_ut$", "", "")
         22 endfunction
         23 
         24 function! s:get_next_file(curr_file, stem) abort
         25     let candidates = glob(a:stem . "*", 1, 1)
         26     let candi_num = len(candidates)
         27 
         28     if candi_num < 2
         29         return ''
         30     endif
         31 
         32 	for i in range(candi_num)
         33         if a:curr_file == candidates[i]
         34             let i = i + 1
         35             if i < candi_num
         36                 return candidates[i]
         37             else
         38                 return candidates[0]
         39             endif
         40         endif
         41 	endfor
         42 
         43     echomsg 'mybe bug found in next_file.vim:'
         44 endfunction
         45 
         46 let s:last_file = ''
         47 let s:last_del_num = 0
         48 
         49 function! next_file#change(del_num) abort
         50     let curr_file = expand('%')
         51 
         52     if s:last_file == curr_file && a:del_num == 0
         53         let del_num = s:last_del_num
         54     else
         55         let del_num = a:del_num
         56     endif
         57 
         58     let stem = s:make_stem(curr_file, del_num)
         59     echo stem . '*  :' . del_num
         60 
         61     let next_file = s:get_next_file(curr_file, stem)
         62     if next_file == ''
         63         let s:last_file = curr_file
         64         let s:last_del_num = del_num < 6 ? 6 : del_num + 1
         65     else
         66         let s:last_file = next_file
         67         let s:last_del_num = del_num
         68         execute 'edit' next_file
         69     endif
         70 endfunction
         71 
```

### vim_config/nvim/autoload/term.vim <a id="SS_23_1_10"></a>
```vim
          1 let s:term_num = -1
          2 
          3 function! s:start_term() abort
          4 "    silent execute 'new'
          5     silent execute 'terminal'
          6 
          7     let s:term_num = bufnr()
          8 endfunction
          9 
         10 function! term#start() abort
         11     if s:term_num == -1
         12         call s:start_term()
         13     else
         14         try
         15             execute "buffer " . s:term_num
         16         catch
         17             " bufferが閉じられていた
         18             call s:start_term()
         19         endtry
         20     endif
         21 endfunction
         22 
         23 
```

### vim_config/nvim/autoload/termdbg.vim <a id="SS_23_1_11"></a>
```vim
          1 ":Run [args]    [args] または以前の引数でプログラムを実行する
          2 ":Arguments     {args}  次の :Run のために引数を設定する
          3 ":Break         カーソル位置にブレークポイントを設定する。
          4 ":Break         {position}
          5 "               指定位置にブレークポイントを設定する。
          6 ":Clear         カーソル位置のブレークポイントを削除する
          7 ":Step          gdb の "step" コマンドを実行する
          8 ":Over          gdb の "next" コマンドを実行する
          9 "               (:Next だと Vim のコマンドとかぶるので)
         10 ":Finish        gdb の "finish" コマンドを実行する
         11 ":Continue      gdb の "continue" コマンドを実行する
         12 ":Stop          プログラムを中断する
         13 
         14 
         15 " todo
         16 "  b    をトグルにしたい
         17 "
         18 function! termdbg#key_map() abort
         19     nnoremap <silent> <buffer> <Plug>(gdb-run) :Run<CR>
         20     nmap <buffer> R <Plug>(gdb-run)
         21 
         22     nnoremap <silent> <buffer> <Plug>(gdb-break) :Break<CR>
         23     nmap <buffer> B <Plug>(gdb-break)
         24 
         25     nnoremap <silent> <buffer> <Plug>(gdb-continue) :Continue<CR>
         26     nmap <buffer> C <Plug>(gdb-continue)
         27 
         28     nnoremap <silent> <buffer> <Plug>(gdb-break-clear) :Clear<CR>
         29     nmap <buffer> D <Plug>(gdb-break-clear)
         30 
         31     nnoremap <silent> <buffer> <Plug>(gdb-finish) :Finish<CR>
         32     nmap <buffer> F <Plug>(gdb-finish)
         33 
         34     nnoremap <silent> <buffer> <Plug>(gdb-next) :Over<CR>
         35     nmap <buffer> N <Plug>(gdb-next)
         36 
         37     nnoremap <silent> <buffer> <Plug>(gdb-step) :Step<CR>
         38     nmap <buffer> S <Plug>(gdb-step)
         39 
         40 endfunction
         41 
         42 function! termdbg#start(program)
         43     silent execute ':packadd termdebug'
         44     silent execute ':Termdebug ' . a:program
         45 endfunction
         46 
```

### vim_config/nvim/cheatsheet.md <a id="SS_23_1_12"></a>
```vim
          1 # My CheatSheet
          2 
          3 ## dein
          4 * https://github.com/Shougo/dein.vimからdeinとダウンロードしてセットアップ
          5     * curl ... > installer.sh   # インストーラのダウンロード
          6     * sh ./installer.sh ~/$XDG_CONFIG_HOME/nvim_pkg/dein    # deinのダウンロード
          7 * :call dein#install()			# 他のパッケージインストール
          8 
          9 ## terminal(windows app)操作
         10 * Alt-space -> x    最大化
         11 * Alt-space -> r    元のサイズに戻す
         12 * Alt-space -> n    最小化
         13 * Alt-space -> m    ウィンドウの移動
         14 * Alt-space -> s    ウィンドウのサイズ変更
         15 * window-m          全アプリの最小化
         16 * window-d          デスクトップの表示/全アプリの表示
         17 
         18 
         19 ## 正規表現
         20 [正規表現アトム](https://vim-jp.org/vimdoc-ja/pattern.html#pattern-atoms)
         21 
         22 \_.         改行含むすべての文字にマッチ
         23 
         24 ## NextFile 
         25 <M-q>           現在のファイル名を@qに代入
         26 <Num><C-q>      現在のファイル名を<Num>文字消して、"その文字列.\*"とマッチしたファイルを開く
         27                 Numが省略された場合<Num>は0として処理する
         28                 Numが0であった場合、"サフィックスを削除した文字列.\*"とマッチしたファイルを開く
         29 
         30 ## MultiHl
         31 :MultiHlAdd     現在のカーソルの下のwordを'\<word\>にして、@/に追加。
         32 :MultiHlAddR    現在のカーソルの下のwordをそのまま@/に追加。
         33 :MultiHlAddI    <WORD> WORDをそのまま@/に追加。
         34 :MultiHlClear   @/に""を入力。
         35 
         36 ## git diff
         37 :GitDiff        : gitリポジトリのdiffリスト
         38 :GitDiffResize  : 画面をリサイズして、gitリポジトリのdiffリスト
         39 :GitDiffOff     : \*.newをbwipeoutしてdiffモード終了
         40 {Visual}a       : git add from '< to '>
         41 c"              : git commit -m "までコマンドラインに入力
         42 d               : 水平分割diff表示
         43 vd              : 垂直分割diff表示
         44 h               : HEADとの水平分割diff表示
         45 vh              : HEADとの垂直分割diff表示
         46 <C-Q>           : git diffモード終了
         47 {Visual}L       : cygstart/wslstart from '< to '>
         48 {Visual}r       : git reset from '< to '>
         49 s               : diffリストの再ロード
         50 
         51 ## grep
         52 :Grep [suffix ...]          : grep -R --include=\*.suffix ... @/
         53 :GrepP pattern [suffix ...] : grep -R --include=\*.suffix ... pattern
         54 
         55 suffixを省略した場合、cpp c h rb py vimがsuffixになる。
         56 全体をgrepしたい場合は - を指定する。
         57 :Grep、:Grepp実行後はquick fixウインドが開いて結果を見ることができる。
         58 <C-g><C-n>で次へ移動、<C-g><C-p>で前に移動できる。
         59 
         60 :set ignorecaseが行われていた場合には、grepのオプションに-iが追加される。
         61 :Grepが行われた場合に実際に起動されるgrepコマンドは、:grepである。
         62 :grepが行われた場合に実際に起動されるgrepコマンドは、:set grepprg=...で設定されている。
         63 
         64 
         65 ## :terminalの使い方
         66 * <C-q>                                     vimモード
         67 * a, i等の通常のinsertモード移行で          terminalモード
         68 
         69 でソースコード全体からの補完ができるらしいので調べる。
         70 
         71 ## termdebug
         72 * nvim-gdbはやめて、こちらにした。
         73 
         74 :DbgStart <prog>    termdebugをロードして、gdb <prog>
         75 :DbgKey             下記mapをバッファローカルでmap
         76 
         77 オリジナルコマンド  map
         78 :Run [args]         R   [args] または以前の引数でプログラムを実行する
         79 :Arguments              {args}  次の :Run のために引数を設定する
         80 :Break              B   カーソル位置にブレークポイントを設定する。
         81 :Clear              D   カーソル位置のブレークポイントを削除する
         82 :Step               S   gdb の "step" コマンドを実行する
         83 :Over               N   gdb の "next" コマンドを実行する
         84 :Finish             F   gdb の "finish" コマンドを実行する
         85 :Continue           C   gdb の "continue" コマンドを実行する
         86 :Stop                   プログラムを中断する
         87 
         88 ## Session
         89 * gitプロジェクトの全ディレクトリを使用してpathやtabsをセットする。
         90 * mksessionでgitリポジトリのトップにSession.vimを作る。
         91 
         92 :ProjectBegin       Session.vimをsourceして、path、tabsをセットする。
         93 :ProjectDir         現在のセッションが使用しているgitリポジトリの
         94                     トップディレクトリを表示。
         95 :ProjectMake        Session.vimを作る。
         96 :ProjectNew         現在のセッションをカレントディレクトリを含む
         97                     gitリポジトリにする。
         98   
         99 ## PathSet
        100 * pathにカレントディレクトリ以下のディレクトリをセットする。
        101 
        102 :PathAdd            pathにディレクトリを追加する
        103 :PathClear          pathを./のみにする
        104 :PathSet            PathClearしてからPathAddする
        105 
        106 ## Buff
        107 軽いのが取り柄のバッファエクスプローラ。
        108 
        109 :Buff               :buffersの情報からBuffers問う名前のバッファを開く。
        110 o                   プロンプトの下のバッファを開く。
        111 d                   プロンプトの下のバッファをスワイプアウトする。
        112 D                   プロンプトの下のバッファを強制スワイプアウトする。
        113 
        114 ## チップス
        115 * 現在のrcフィルの確認
        116         :echo $MYGVIMRC
        117 
        118 * マップの定義位置
        119         :verbose map <C-Q>
        120 
        121 * vimコマンドの出力の取り込み
        122         :let @a=execute('scriptnames')  "scriptnamesの出力をレジスタaに入れる。
        123 
        124 * globalで行に移動し、そこでコマンド実行
        125         :global/^</normal AHEHE     "先頭が"<"である行の末尾に"HEHE"を追加する。
        126 
        127 * コマンドの繰り返し数の注意
        128         :map <C-A>  3w
        129   とした場合、 
        130         2<C-A>
        131   は
        132         23w
        133   となるため、このコマンドは23ワードの移動になるが、それはおそらく意図したものではない。
        134   <Num><C-A>を<C-A>の<Num>回の繰り返しにしたい場合、式レジスタを使い以下のように書く。
        135         :map <C-A>  @='3w'<CR>
        136 
        137 ### todo
        138 * 言語サポート
        139     * gdbのpでSTLコンテナのきれいな表示がしたい。
        140     * rtag.vim
        141     * Tagbar: a class outline viewer for Vim
        142 
        143 * そのうち調べる
        144     * コメントフォーマット。'formatoptions' の設定
        145     * 'showcmd'、'backspace'
        146     * 関数escape(@", '\\/')
        147     * packadd! matchit  「と」のマッチング
        148     * colorscheme evening
        149     * :mksession、:wviminfo、:rviminfo
        150     * terminal 端末通信 call/drop
```

### vim_config/nvim/ftplugin/c.vim <a id="SS_23_1_13"></a>
```vim
          1 setlocal tabstop=4
          2 setlocal shiftwidth=4
          3 setlocal expandtab
          4 setlocal tags=tags,./tags
          5 
          6 " paren and etc matching
          7 set matchpairs+=<:>
          8 hi MatchParen ctermbg=0 cterm=bold,reverse
          9 
```

### vim_config/nvim/ftplugin/python.vim <a id="SS_23_1_14"></a>
```vim
          1 setlocal tabstop=4
          2 setlocal shiftwidth=4
          3 setlocal expandtab
          4 setlocal tags=tags,./tags
          5 
```

### vim_config/nvim/ftplugin/ruby.vim <a id="SS_23_1_15"></a>
```vim
          1 setlocal tabstop=2
          2 setlocal shiftwidth=2
          3 setlocal expandtab
          4 setlocal tags=tags,./tags
```

### vim_config/nvim/init.vim <a id="SS_23_1_16"></a>
```vim
          1 if exists('s:loaded')
          2     finish
          3 else
          4     let s:loaded = 1
          5 endif
          6 
          7 function! s:get_os()
          8     if isdirectory('c:/')
          9         if isdirectory('/usr')
         10             return 'cygwin'
         11         else
         12             return 'windows'
         13         endif
         14     endif
         15 
         16     let old=&ignorecase
         17     let uname=system('uname')
         18 
         19     let &ignorecase = 1
         20 
         21     if uname =~ ".*linux.*"
         22         let ret = 'linux'
         23     else
         24         let ret = 'unknown'
         25     endif
         26 
         27     let &ignorecase = old
         28     return ret
         29 endfunction
         30 
         31 let g:os=s:get_os()
         32 
         33 let s:dir=expand('<sfile>:p:h')
         34 
         35 execute 'source ' . s:dir . '/' . 'org.vim'
         36 execute 'source ' . s:dir . '/' . 'package.vim'
         37 
         38 if !has('nvim')
         39     execute 'set runtimepath+=' . s:dir
         40     if g:os == 'linux'
         41         set runtimepath+=/usr/share/vim/
         42     elseif g:os == 'cygwin'
         43         set runtimepath+=/usr/share/vim/vim82
         44     elseif g:os == 'windows'
         45 
         46     endif
         47 endif
```

### vim_config/nvim/org.vim <a id="SS_23_1_17"></a>
```vim
          1 " misc
          2 set hidden
          3 set ruler
          4 set hlsearch
          5 set nowrapscan
          6 set laststatus=2
          7 set noequalalways
          8 set backspace=indent,eol,start
          9 set incsearch
         10 set background=dark
         11 set statusline=%<%f[%n]%h%m%r%=%l,%c%V\ %P
         12 set fileformats=unix,dos,mac
         13 set printoptions=number:y
         14 
         15 set virtualedit=block
         16 
         17 " Makefileやbashスクリプトでgfを効かせるため
         18 set isfname-=:
         19 set isfname-=,
         20 set isfname-=\=
         21 
         22 " encoding
         23 "set encoding=utf-8
         24 set fileencoding=utf-8
         25 set fileencodings=iso-2022-jp,euc-jp,sjis,utf-8
         26 
         27 "
         28 syntax on
         29 
         30 " to use quick fix
         31 "make setting
         32 set makeprg=/usr/bin/make
         33 set errorformat+=In\ file\ included\ from\ %f:%l:%m     "gcc
         34 set errorformat+=%f:%l:%m                               "gcc
         35 set errorformat+=%f\|%l\|%m                             "grep from vim
         36 set errorformat+=%t\\,%f\\,%l\\,%c\\,%m
         37 
         38 "grep setting
         39 set grepprg=/usr/bin/grep\ -nH
         40 
         41 let &makeef = expand('<sfile>:p:h') . '/' . getpid()
         42 
         43 " default text
         44 set tabstop=4
         45 set shiftwidth=4
         46 set expandtab
         47 set nowrap
         48 set cindent
         49 "set iskeyword+=-
```

### vim_config/nvim/package.vim <a id="SS_23_1_18"></a>
```vim
          1 if &compatible
          2     set nocompatible " Be iMproved
          3 endif
          4 
          5 " このファイルのあるディレクトリ/../nvim_pkg/deinにパッケージを入れる。
          6 let g:pkg_dir=simplify(expand('<sfile>:p:h') . '/../nvim_pkg/dein')
          7 
          8 " Required:
          9 " Add the dein installation directory into runtimepath
         10 execute 'set runtimepath+=' . g:pkg_dir . '/repos/github.com/Shougo/dein.vim'
         11 execute 'set runtimepath+=' . g:pkg_dir . '/repos/github.com/'
         12 
         13 " Required:
         14 call dein#begin(g:pkg_dir)
         15 
         16 " Let dein manage dein
         17 " Required:
         18 call dein#add(g:pkg_dir . '/repos/github.com/Shougo/dein.vim')
         19 if !has('nvim')
         20     call dein#add('roxma/nvim-yarp')
         21     call dein#add('roxma/vim-hug-neovim-rpc')
         22 endif
         23 
         24 call dein#add('Shougo/deoplete.nvim')
         25 call dein#add('zchee/deoplete-clang')
         26 
         27 " Add or remove your plugins here like this:
         28 call dein#add('Shougo/neosnippet.vim')
         29 call dein#add('Shougo/neosnippet-snippets')
         30 call dein#add('Shougo/neoinclude.vim')
         31 
         32 call dein#add('tpope/vim-fugitive')
         33 call dein#add('reireias/vim-cheatsheet')
         34 call dein#add('mattn/vim-maketable')
         35 call dein#add('aklt/plantuml-syntax')
         36 
         37 " Required:
         38 call dein#end()
         39 
         40 " Required:
         41 filetype plugin indent on
         42 syntax enable
         43 
         44 let g:cheatsheet#cheat_file = expand('<sfile>:p:h') . '/cheatsheet.md'
         45 let g:table_mode_corner = '|'
         46 
         47 if g:os == 'windows'
         48     let g:python_host_prog  = 'C:\cygwin64\bin\python2.7.exe'
         49     let g:python3_host_prog  = 'C:\cygwin64\bin\python3.8.exe'
         50 elseif g:os == 'cygwin'
         51 
         52 elseif g:os == 'linux'
         53     let g:ruby_host_prog = '/usr/local/bin/neovim-ruby-host'
         54     let g:python_host_prog  = '/usr/bin/python2'
         55     let g:python3_host_prog  = '/usr/bin/python3'
         56 else
         57     echo 'unkown os'
         58 endif
         59 
         60 " deoplete
         61 if has('python3')
         62     let g:deoplete#enable_at_startup = 1
         63     let g:deoplete#sources#clang#libclang_path = '/usr/lib/llvm-10/lib/libclang.so'
         64     let g:deoplete#sources#clang#clang_header = '/usr/lib/llvm-10/lib/clang/'
         65     let g:deoplete#sources#clang#clang_complete_database = './'
         66     "g:deoplete#sources#clang#flags	See this section	No
         67     "g:deoplete#sources#clang#sort_algo	''	No
         68     "g:deoplete#sources#clang#include_default_arguments	False	No
         69     "g:deoplete#sources#clang#filter_availability_kinds
         70 endif
```

### vim_config/nvim/plugin/buffers.vim <a id="SS_23_1_19"></a>
```vim
          1 command! -nargs=0 Buff     call buffers#begin()
```

### vim_config/nvim/plugin/cd.vim <a id="SS_23_1_20"></a>
```vim
          1 command! -nargs=0 Cd    call cd#change_dir()
          2 nmap <C-c>       :Cd<CR>
          3 
          4 nmap <S-c>       :cd ..<CR>:pwd<CR>
          5 
```

### vim_config/nvim/plugin/clear_undo.vim <a id="SS_23_1_21"></a>
```vim
          1 function! ClearUndo()
          2     let old_undolevels = &undolevels
          3     set undolevels=-1
          4     exe "normal a \<BS>\<Esc>"
          5     let &undolevels = old_undolevels
          6     unlet old_undolevels
          7 endfunction
          8 
          9 command! -nargs=0 ClearUndo call ClearUndo()
         10 
         11 
```

### vim_config/nvim/plugin/ctags_ext.vim <a id="SS_23_1_22"></a>
```vim
          1 function! CTags(...)
          2     if a:0 == 0
          3         let l:dir="."
          4     else
          5         let l:dir=a:1
          6     end
          7     silent execute '!ctags -R --extras=+q ' . l:dir
          8 endfunction
          9 
         10 command!  -nargs=? -complete=dir Ctags call CTags(<f-args>)
         11 
```

### vim_config/nvim/plugin/dev_env.vim <a id="SS_23_1_23"></a>
```vim
          1 function! dev_env#setup()
          2     execute ":only"
          3     execute ":set lines=62"
          4     execute ":set columns=201"
          5     
          6     "少し待たないとカラムが増える前にvsplitしてしまう
          7     execute ":sleep 300m"   
          8     execute ":vsplit"
          9     execute ":split"
         10     execute "normal \<C-W>l"
         11     execute ":split"
         12     execute "normal \<C-W>j"
         13     execute ":Term"
         14     execute "normal \<C-W>h"
         15     execute "normal \<C-W>k"
         16     set textwidth=100
         17 endfunction
         18 
         19 command! -nargs=0 DevEnv     call dev_env#setup()
```

### vim_config/nvim/plugin/git_diff.vim <a id="SS_23_1_24"></a>
```vim
          1 command! -nargs=0 GitDiff       call git_diff#begin(0)
          2 command! -nargs=0 GitDiffResize call git_diff#begin(1)
          3 command! -nargs=0 GitDiffOff    call git_diff#show_diff_off()
```

### vim_config/nvim/plugin/git_session.vim <a id="SS_23_1_25"></a>
```vim
          1 command! -nargs=0 SessionBegin  call git_session#begin()
          2 command! -nargs=0 SessionDir    call git_session#dir()
          3 command! -nargs=0 SessionMake   call git_session#make()
          4 command! -nargs=0 SessionNew    call git_session#new_session()
          5 command! -nargs=0 SessionPath   call git_session#set_path()
```

### vim_config/nvim/plugin/grep.vim <a id="SS_23_1_26"></a>
```vim
          1 command!  -nargs=? Grep call grep#grep(<f-args>)
          2 command!  -nargs=+ Grepp call grep#grepp(<f-args>)
          3 
```

### vim_config/nvim/plugin/keybind.vim <a id="SS_23_1_27"></a>
```vim
          1 "Set up key binding
          2 
          3 " window control
          4 nmap ;   4<C-W>+
          5 nmap -   4<C-W>-
          6 noremap L   <C-L>
          7 nmap >   <C-W>>
          8 nmap <   <C-W><
          9 nmap <C-k>   <C-W>k
         10 nmap <C-j>   <C-W>j
         11 nmap <C-h>   <C-W>h
         12 nmap <C-l>   <C-W>l
         13 nmap <C-p>   <C-o>
         14 
         15 "next/prev file
         16 nmap <C-n>   :bn<CR>
         17 nmap <C-p>   :bp<CR>
         18 
         19 "next/prev quick fix
         20 nmap <C-g><C-n>  :cn<CR>
         21 nmap <C-g><C-p>  :cp<CR>
         22 
```

### vim_config/nvim/plugin/multi_hl.vim <a id="SS_23_1_28"></a>
```vim
          1 command! -nargs=0 MultiHlAdd    call multi_hl#add_word(expand('<cword>'), 0)
          2 command! -nargs=0 MultiHlAddR   call multi_hl#add_word(expand('<cword>'), 1)
          3 command! -nargs=1 MultiHlAddI      call multi_hl#add_word(<q-args>, 1)
          4 command! -nargs=0 MultiHlClear     call multi_hl#clear()
```

### vim_config/nvim/plugin/next_file.vim <a id="SS_23_1_29"></a>
```vim
          1 if g:os == 'linux'
          2     nmap <M-q>      :let @q=expand('%')<CR>
          3 else
          4     nmap <S-C-q>    :let @q=expand('%')<CR>
          5 endif
          6 
          7 command!  -count NF call next_file#change(<count>)
          8 nmap <C-q>      :NF<CR>
```

### vim_config/nvim/plugin/path_set.vim <a id="SS_23_1_30"></a>
```vim
          1 function! path_set#add()
          2     let temp = system('find $(pwd) -type d')
          3     let dirs = split(temp, "\n")
          4     let paths = &path . ',' . join(dirs, ',')
          5     let &path = paths
          6 endfunction
          7 
          8 function! path_set#clear()
          9     let &path = './'
         10 endfunction
         11 
         12 function! path_set#set()
         13     call path_set#clear()
         14     call path_set#add()
         15 endfunction
         16 
         17 command! -nargs=0 PathAdd  call path_set#add()
         18 command! -nargs=0 PathClear  call path_set#clear()
         19 command! -nargs=0 PathSet  call path_set#set()
```

### vim_config/nvim/plugin/scratch.vim <a id="SS_23_1_31"></a>
```vim
          1 let s:scratch_buffer = 'Scratch'
          2 
          3 function! scratch#begin()
          4     let winid = bufwinid(s:scratch_buffer)
          5     if winid isnot# -1
          6         call win_gotoid(winid)
          7     else
          8         execute 'new' s:scratch_buffer
          9         set buftype=nofile
         10         set noswapfile
         11     endif
         12 endfunction
         13 
         14 command! -nargs=0 Scratch     call scratch#begin()
         15 
```

### vim_config/nvim/plugin/term.vim <a id="SS_23_1_32"></a>
```vim
          1 if g:os == 'windows'
          2     set shell=C:/cygwin64/bin/bash.exe
          3 else
          4     set shell=/bin/bash
          5 endif
          6 
          7 set shellpipe=\|&\ tee
          8 set shellcmdflag=-c
          9 set shellslash
         10 
         11 tnoremap <silent> <C-q> <C-\><C-n>
         12 command! -nargs=0 Term     call term#start()
         13 
```

### vim_config/nvim/plugin/termdbg.vim <a id="SS_23_1_33"></a>
```vim
          1 command! -nargs=1 -complete=file DbgStart   call termdbg#start(<q-args>)
          2 command! -nargs=0 DbgKey     call termdbg#key_map()
          3 
          4 
```

### vim_config/nvim/rplugin/python3/next_file.py <a id="SS_23_1_34"></a>
```vim
          1 import pynvim
          2 import glob
          3 
          4 @pynvim.plugin
          5 class NextFile(object):
          6 
          7     def __init__(self, nvim):
          8         self.nvim = nvim
          9         self.delete_len = 0
         10         self.latest_file = None
         11         self.file_list = []
         12 
         13     @pynvim.command('NextFile', nargs='?', range='', sync = True)
         14     def next_file(self, args, range):
         15         if len(args) != 0 :
         16             try :
         17                 self.delete_len = int(args[0])
         18             except:
         19                 self.delete_len = 0
         20 
         21         curr_filename = self.nvim.eval("expand('%')")
         22         next_filename = self._next_filename(curr_filename)
         23         self.nvim.command(f"edit {next_filename}")
         24 
         25     def _next_filename(self, filename) :
         26 
         27         if self.delete_len == 0 :
         28             body, *_ = filename.split(".")
         29         else:
         30             body = filename[0 : len(filename) - self.delete_len]
         31             self.latest_file = None
         32 
         33         if self.latest_file != filename :
         34             self.file_list = glob.glob(body + "*")
         35 
         36         for i, f in enumerate(self.file_list) :
         37             if filename == f :
         38                 self.latest_file = self.file_list[(i + 1) % len(self.file_list)]
         39 
         40                 return self.latest_file
         41 
```

### vim_config/vim.sh <a id="SS_23_1_35"></a>
```vim
          1 function os_name()
          2 {
          3     local -r uname=$(uname)
          4 
          5     if [[ $uname =~ .*[lL]inux.* ]]; then
          6         echo linux
          7     elif [[ $uname =~ .*CYGWIN_NT.* ]]; then
          8         echo cygwin
          9     else
         10         echo unknown
         11     fi
         12 }
         13 
         14 readonly OS=$(os_name)
         15 
         16 if [[ $OS == 'cygwin' ]]; then
         17     function gvim()
         18     {
         19         (
         20             gvim_prog=$(which gvim)
         21             export XDG_CONFIG_HOME=$(cygpath -w $XDG_CONFIG_HOME)
         22             $gvim_prog "$@"
         23         )
         24     }
         25 
         26     function _nvim_qt()
         27     {
         28         (
         29             export XDG_CONFIG_HOME=$(cygpath -w $XDG_CONFIG_HOME)
         30             nvim-qt "$@"
         31         )
         32     }
         33 
         34     function _nvim()
         35     {
         36         (
         37             export XDG_CONFIG_HOME=$(cygpath -w $XDG_CONFIG_HOME)
         38             nvim "$@"
         39         )
         40     }
         41     alias nvim-qt=_nvim_qt
         42     alias nvim=_nvim
         43 
         44 elif [[ $OS == 'linux' ]]; then
         45     function tnvim()
         46     {
         47         /mnt/c/Users/ichiro.inoue/AppData/Local/wsltty/bin/mintty.exe \
         48             --WSL= \
         49             --configdir='C:\Users\ichiro.inoue\AppData\Roaming\wsltty' \
         50             nvim "$@"
         51     }
         52 
         53     alias tn=tnvim
         54 fi
```

### vim_config/vim/gvimrc <a id="SS_23_1_36"></a>
```vim
          1 "このファイルは$HOME/.gvimrcにコピーするかシンボリックリンクを張る。
          2 
          3 set guifont=ＭＳ_ゴシック:h10:cSHIFTJIS
          4 
          5 let g:bg_coler='black'
          6 highlight Normal guibg='black' guifg='white'
          7 
```

### vim_config/vim/vimrc <a id="SS_23_1_37"></a>
```vim
          1 "このファイルは$HOME/.vimrcにコピーするかシンボリックリンクを張る。
          2 
          3 source $XDG_CONFIG_HOME/nvim/init.vim
```

## C++ <a id="SS_23_2"></a>
### example/deps/app/src/deps_opts.cpp <a id="SS_23_2_1"></a>
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
         10 std::string DepsOpts::Help()
         11 {
         12     auto ss = std::ostringstream{};
         13 
         14     ss << "deps CMD [option] [DIRS] ..." << std::endl;
         15     ss << "   CMD:" << std::endl;
         16     ss << "         p    : generate package to OUT." << std::endl;
         17     ss << "         s    : generate srcs with incs to OUT." << std::endl;
         18     ss << "         p2s  : generate package and srcs pairs to OUT." << std::endl;
         19     ss << "         p2p  : generate packages' dependencies to OUT." << std::endl;
         20     ss << "         a    : generate structure to OUT from p2p output." << std::endl;
         21     ss << "         a2pu : generate plant uml package to OUT from p2p output." << std::endl;
         22     ss << "         cyc  : exit !0 if found cyclic dependencies." << std::endl;
         23     ss << "         help : show help message." << std::endl;
         24     ss << "         h    : same as help(-h, --help)." << std::endl;
         25     ss << std::endl;
         26     ss << "   opptions:" << std::endl;
         27     ss << "         --in IN     : use IN to execute CMD." << std::endl;
         28     ss << "         --out OUT   : CMD outputs to OUT." << std::endl;
         29     ss << "         --recursive : search dir as package from DIRS or IN contents." << std::endl;
         30     ss << "         -R          : same as --recursive." << std::endl;
         31     ss << "         --src_as_pkg: every src is as a package." << std::endl;
         32     ss << "         -s          : same as --src_as_pkg." << std::endl;
         33     ss << "         --log LOG   : loggin to LOG(if LOG is \"-\", using STDOUT)." << std::endl;
         34     ss << "         --exclude PTN : exclude dirs which matchs to PTN(JS regex)." << std::endl;
         35     ss << "         -e PTN      : same as --exclude." << std::endl;
         36     ss << std::endl;
         37     ss << "   DIRS: use DIRS to execute CMD." << std::endl;
         38     ss << "   IN  : 1st line in this file must be" << std::endl;
         39     ss << "             #dir2srcs for pkg-srcs file" << std::endl;
         40     ss << "         or" << std::endl;
         41     ss << "             #dir for pkg file." << std::endl << std::endl;
         42 
         43     return ss.str();
         44 }
         45 
         46 DepsOpts::Cmd DepsOpts::parse_command(int argc, char* const* argv)
         47 {
         48     if (argc < 2) {
         49         return Cmd::NotCmd;
         50     }
         51 
         52     auto command = std::string{argv[1]};
         53 
         54     if (command == "p") {
         55         return Cmd::GenPkg;
         56     }
         57     if (command == "s") {
         58         return Cmd::GenSrc;
         59     }
         60     else if (command == "p2s") {
         61         return Cmd::GenPkg2Srcs;
         62     }
         63     else if (command == "p2p") {
         64         return Cmd::GenPkg2Pkg;
         65     }
         66     else if (command == "a") {
         67         return Cmd::GenArch;
         68     }
         69     else if (command == "a2pu") {
         70         return Cmd::GenPlantUml;
         71     }
         72     else if (command == "cyc") {
         73         return Cmd::GenCyclic;
         74     }
         75     else if (command == "h" || command == "help" || command == "-h" || command == "--help") {
         76         return Cmd::Help;
         77     }
         78 
         79     return Cmd::NotCmd;
         80 }
         81 
         82 bool DepsOpts::parse_opt(int opt_char, DepsOpts::DepsOptsData& data) noexcept
         83 {
         84     switch (opt_char) {
         85     case 'i':
         86         data.in = optarg;
         87         return true;
         88     case 'e':
         89         data.exclude = optarg;
         90         return true;
         91     case 'o':
         92         data.out = optarg;
         93         return true;
         94     case 'l':
         95         data.log = optarg;
         96         return true;
         97     case 'R':
         98         data.recursive = true;
         99         return true;
        100     case 's':
        101         data.src_as_pkg = true;
        102         return true;
        103     case 'h':
        104         data.cmd = Cmd::Help;
        105         return false;
        106     default:
        107         return false;
        108     }
        109 }
        110 
        111 DepsOpts::DepsOptsData DepsOpts::parse(int argc, char* const* argv)
        112 {
        113     DepsOptsData data{parse_command(argc, argv)};
        114 
        115     if (data.cmd == Cmd::NotCmd || data.cmd == Cmd::Help) {
        116         return data;
        117     }
        118 
        119     optind = 2;
        120     static struct option const opts[]
        121         = {{"in", required_argument, 0, 'i'},      {"out", required_argument, 0, 'o'},
        122            {"exclude", required_argument, 0, 'e'}, {"recursive", no_argument, 0, 'R'},
        123            {"src_as_pkg", no_argument, 0, 's'},    {"log", required_argument, 0, 'l'},
        124            {"help", no_argument, 0, 'h'},          {0, 0, 0, 0}};
        125 
        126     for (;;) {
        127         auto opt_char = getopt_long(argc, argv, "i:o:e:l:Rsh", opts, nullptr);
        128 
        129         if (!parse_opt(opt_char, data)) {
        130             break;
        131         }
        132     }
        133 
        134     if (optind < argc) {
        135         while (optind < argc) {
        136             data.dirs.emplace_back(FileUtils::NormalizeLexically(argv[optind++]));
        137         }
        138     }
        139 
        140     return data;
        141 }
        142 
        143 namespace {
        144 std::string to_string_cmd(DepsOpts::Cmd cmd)
        145 {
        146     switch (cmd) {
        147     case DepsOpts::Cmd::GenPkg:
        148         return "GenPkg";
        149     case DepsOpts::Cmd::GenSrc:
        150         return "GenSrc";
        151     case DepsOpts::Cmd::GenPkg2Srcs:
        152         return "GenPkg2Srcs";
        153     case DepsOpts::Cmd::GenPkg2Pkg:
        154         return "GenPkg2Pkg";
        155     case DepsOpts::Cmd::GenPlantUml:
        156         return "GenPlantUml";
        157     case DepsOpts::Cmd::GenCyclic:
        158         return "GenCyclic";
        159     case DepsOpts::Cmd::Help:
        160         return "Help";
        161     case DepsOpts::Cmd::NotCmd:
        162     default:
        163         return "NotCmd";
        164     }
        165 }
        166 }  // namespace
        167 
        168 std::string ToStringDepsOpts(DepsOpts const& deps_opts, std::string_view indent)
        169 {
        170     auto       ss      = std::ostringstream{};
        171     char const cmd[]   = "cmd       : ";
        172     auto const indent2 = std::string(Nstd::ArrayLength(cmd) - 1, ' ') + std::string{indent};
        173 
        174     ss << std::boolalpha;
        175 
        176     ss << indent << cmd << to_string_cmd(deps_opts.GetCmd()) << std::endl;
        177     ss << indent << "in        : " << deps_opts.In() << std::endl;
        178     ss << indent << "out       : " << deps_opts.Out() << std::endl;
        179     ss << indent << "recursive : " << deps_opts.IsRecursive() << std::endl;
        180     ss << indent << "src_as_pkg: " << deps_opts.IsSrcPkg() << std::endl;
        181     ss << indent << "log       : " << deps_opts.Log() << std::endl;
        182     ss << indent << "dirs      : " << FileUtils::ToStringPaths(deps_opts.Dirs(), "\n" + indent2)
        183        << std::endl;
        184     ss << indent << "exclude   : " << deps_opts.Exclude() << std::endl;
        185     ss << indent << "parsed    : " << !!deps_opts;
        186 
        187     return ss.str();
        188 }
        189 }  // namespace App
```

### example/deps/app/src/deps_opts.h <a id="SS_23_2_2"></a>
```cpp
          1 #pragma once
          2 #include <ostream>
          3 
          4 #include "file_utils/path_utils.h"
          5 
          6 namespace App {
          7 class DepsOpts {
          8 public:
          9     enum class Cmd {
         10         GenPkg,
         11         GenSrc,
         12         GenPkg2Srcs,
         13         GenPkg2Pkg,
         14         GenArch,
         15         GenPlantUml,
         16         GenCyclic,
         17         Help,
         18         NotCmd,
         19     };
         20     explicit DepsOpts(int argc, char* const* argv) : data_{parse(argc, argv)} {}
         21     static std::string Help();
         22 
         23     Cmd                       GetCmd() const noexcept { return data_.cmd; }
         24     std::string const&        In() const noexcept { return data_.in; }
         25     std::string const&        Out() const noexcept { return data_.out; }
         26     std::string const&        Log() const noexcept { return data_.log; }
         27     bool                      IsRecursive() const noexcept { return data_.recursive; }
         28     bool                      IsSrcPkg() const noexcept { return data_.src_as_pkg; }
         29     FileUtils::Paths_t const& Dirs() const noexcept { return data_.dirs; }
         30     std::string const&        Exclude() const noexcept { return data_.exclude; }
         31 
         32     explicit operator bool() const { return data_.cmd != Cmd::NotCmd; }
         33 
         34 private:
         35     struct DepsOptsData {
         36         DepsOptsData(Cmd cmd_arg) noexcept : cmd{cmd_arg} {}
         37         Cmd                cmd;
         38         std::string        in{};
         39         std::string        out{};
         40         std::string        log{};
         41         FileUtils::Paths_t dirs{};
         42         std::string        exclude{};
         43         bool               recursive{false};
         44         bool               src_as_pkg{false};
         45     };
         46     DepsOptsData const data_;
         47 
         48     static DepsOptsData parse(int argc, char* const* argv);
         49     static Cmd          parse_command(int argc, char* const* argv);
         50     static bool         parse_opt(int opt_char, DepsOptsData& data) noexcept;
         51 };
         52 
         53 // @@@ sample begin 0:0
         54 
         55 std::string          ToStringDepsOpts(DepsOpts const& deps_opts, std::string_view indent = "");
         56 inline std::ostream& operator<<(std::ostream& os, DepsOpts const& opts)
         57 {
         58     return os << ToStringDepsOpts(opts);
         59 }
         60 // @@@ sample end
         61 }  // namespace App
```

### example/deps/app/src/main.cpp <a id="SS_23_2_3"></a>
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
         14     explicit OStreamSelector(std::string const& out) : os_{select(out, out_f_)} {}
         15     std::ostream& OStream() noexcept { return os_; }
         16 
         17 private:
         18     std::ofstream out_f_{};
         19     std::ostream& os_;
         20 
         21     static std::ostream& select(std::string const& out, std::ofstream& out_f)
         22     {
         23         if (out.size()) {
         24             out_f.open(out);
         25             assert(out_f);
         26             return out_f;
         27         }
         28         else {
         29             return std::cout;
         30         }
         31     }
         32 };
         33 
         34 class ScenarioGeneratorNop : public Dependency::ScenarioGenerator {
         35 public:
         36     explicit ScenarioGeneratorNop(bool no_error) : no_error_{no_error} {}
         37     virtual bool Output(std::ostream&) const noexcept override { return no_error_; }
         38 
         39 private:
         40     bool no_error_;
         41 };
         42 
         43 // @@@ sample begin 0:0
         44 std::unique_ptr<Dependency::ScenarioGenerator> gen_scenario(App::DepsOpts const& opt)
         45 try {
         46     using namespace Dependency;
         47 
         48     switch (opt.GetCmd()) {
         49     case App::DepsOpts::Cmd::GenPkg:
         50         LOGGER("start GenPkg");
         51         return std::make_unique<PkgGenerator>(opt.In(), opt.IsRecursive(), opt.Dirs(),
         52                                               opt.Exclude());
         53     case App::DepsOpts::Cmd::GenSrc:
         54         LOGGER("start GenPkg");
         55         return std::make_unique<SrcsGenerator>(opt.In(), opt.IsRecursive(), opt.Dirs(),
         56                                                opt.Exclude());
         57     // @@@ ignore begin
         58     case App::DepsOpts::Cmd::GenPkg2Srcs:
         59         LOGGER("start GenPkg2Srcs");
         60         return std::make_unique<Pkg2SrcsGenerator>(opt.In(), opt.IsRecursive(), opt.IsSrcPkg(),
         61                                                    opt.Dirs(), opt.Exclude());
         62     case App::DepsOpts::Cmd::GenPkg2Pkg:
         63         LOGGER("start GenPkg2Pkg");
         64         return std::make_unique<Pkg2PkgGenerator>(opt.In(), opt.IsRecursive(), opt.IsSrcPkg(),
         65                                                   opt.Dirs(), opt.Exclude());
         66     case App::DepsOpts::Cmd::GenArch:
         67         LOGGER("start GenArch");
         68         return std::make_unique<ArchGenerator>(opt.In());
         69     case App::DepsOpts::Cmd::GenPlantUml:
         70         LOGGER("start GenPlantUml");
         71         return std::make_unique<Arch2PUmlGenerator>(opt.In());
         72     case App::DepsOpts::Cmd::GenCyclic:
         73         LOGGER("start GenCyclic");
         74         return std::make_unique<CyclicGenerator>(opt.In());
         75     case App::DepsOpts::Cmd::Help:
         76         std::cout << App::DepsOpts::Help() << std::endl;
         77         return std::make_unique<ScenarioGeneratorNop>(true);
         78     case App::DepsOpts::Cmd::NotCmd:
         79     default:
         80         std::cout << App::DepsOpts::Help() << std::endl;
         81         return std::make_unique<ScenarioGeneratorNop>(false);
         82         // @@@ ignore end
         83     }
         84 }
         85 catch (std::runtime_error const& e) {
         86     LOGGER("error occured:", e.what());
         87 
         88     std::cerr << e.what() << std::endl;
         89 
         90     return std::make_unique<ScenarioGeneratorNop>(false);
         91 }
         92 
         93 // @@@ ignore begin
         94 catch (...) {
         95     LOGGER("unknown error occured:");
         96 
         97     return std::make_unique<ScenarioGeneratorNop>(false);
         98 }
         99 }  // namespace
        100 // @@@ ignore end
        101 
        102 int main(int argc, char* argv[])
        103 {
        104     App::DepsOpts d_opt{argc, argv};
        105 
        106     LOGGER_INIT(d_opt.Log() == "-" ? nullptr : d_opt.Log().c_str());
        107 
        108     LOGGER("Options", '\n', d_opt);
        109 
        110     auto out_sel   = OStreamSelector{d_opt.Out()};
        111     auto exit_code = gen_scenario(d_opt)->Output(out_sel.OStream()) ? 0 : -1;
        112 
        113     LOGGER("Exit", exit_code);
        114 
        115     return exit_code;
        116 }
        117 // @@@ sample end
```

### example/deps/app/ut/deps_opts_ut.cpp <a id="SS_23_2_4"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "deps_opts.h"
          4 #include "lib/nstd.h"
          5 
          6 namespace App {
          7 namespace {
          8 
          9 TEST(deps_args, DepsOpts)
         10 {
         11     using FileUtils::Paths_t;
         12 
         13     char prog[]          = "prog";
         14     char cmd_p[]         = "p";
         15     char cmd_s[]         = "s";
         16     char cmd_p2s[]       = "p2s";
         17     char cmd_p2p[]       = "p2p";
         18     char cmd_a[]         = "a";
         19     char cmd_a2pu[]      = "a2pu";
         20     char cmd_help[]      = "help";
         21     char cmd_dd_help[]   = "--help";
         22     char cmd_h[]         = "h";
         23     char cmd_d_h[]       = "-h";
         24     char cmd_unknown[]   = "unknown";
         25     char opt_in[]        = "--in";
         26     char opt_in_arg[]    = "in-file";
         27     char opt_out[]       = "--out";
         28     char opt_out_arg[]   = "out-file";
         29     char opt_e[]         = "-e";
         30     char opt_exclude[]   = "--exclude";
         31     char opt_e_arg[]     = "pattern.*";
         32     char opt_recursive[] = "--recursive";
         33     char opt_src_pkg[]   = "--src_as_pkg";
         34     char opt_log[]       = "--log";
         35     char opt_log_arg[]   = "log-file";
         36     char opt_log_dash[]  = "-";
         37     char opt_R[]         = "-R";
         38     char opt_s[]         = "-s";
         39     char opt_help[]      = "--help";
         40     char opt_h[]         = "-h";
         41     char dir0[]          = "dir0";
         42     char dir1[]          = "dir1";
         43     char dir2[]          = "dir2";
         44 
         45     {
         46         char* const argv[]{prog, cmd_p, opt_recursive, opt_out, opt_out_arg, dir0, dir1, dir2};
         47 
         48         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         49 
         50         ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
         51         ASSERT_EQ("", d_opt.In());
         52         ASSERT_EQ(opt_out_arg, d_opt.Out());
         53         ASSERT_TRUE(d_opt.IsRecursive());
         54         ASSERT_EQ((Paths_t{dir0, dir1, dir2}), d_opt.Dirs());
         55         ASSERT_TRUE(d_opt);
         56     }
         57     {
         58         char* const argv[] = {prog, cmd_p, opt_src_pkg, opt_out, opt_out_arg, dir0, dir1, dir2};
         59 
         60         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         61 
         62         ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
         63         ASSERT_EQ("", d_opt.In());
         64         ASSERT_EQ(opt_out_arg, d_opt.Out());
         65         ASSERT_FALSE(d_opt.IsRecursive());
         66         ASSERT_TRUE(d_opt.IsSrcPkg());
         67         ASSERT_EQ((Paths_t{dir0, dir1, dir2}), d_opt.Dirs());
         68         ASSERT_TRUE(d_opt);
         69     }
         70     {
         71         char* const argv[]{prog, cmd_s, opt_src_pkg, opt_out, opt_out_arg, dir0, dir1, dir2};
         72 
         73         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         74 
         75         ASSERT_EQ(DepsOpts::Cmd::GenSrc, d_opt.GetCmd());
         76         ASSERT_EQ("", d_opt.In());
         77         ASSERT_EQ(opt_out_arg, d_opt.Out());
         78         ASSERT_FALSE(d_opt.IsRecursive());
         79         ASSERT_TRUE(d_opt.IsSrcPkg());
         80         ASSERT_EQ((Paths_t{dir0, dir1, dir2}), d_opt.Dirs());
         81         ASSERT_TRUE(d_opt);
         82     }
         83     {
         84         char* const argv[]{prog, cmd_p2s, opt_R, opt_in, opt_in_arg, opt_exclude, opt_e_arg, dir0};
         85 
         86         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
         87 
         88         ASSERT_EQ(DepsOpts::Cmd::GenPkg2Srcs, d_opt.GetCmd());
         89         ASSERT_EQ(opt_in_arg, d_opt.In());
         90         ASSERT_EQ("", d_opt.Out());
         91         ASSERT_TRUE(d_opt.IsRecursive());
         92         ASSERT_EQ((Paths_t{dir0}), d_opt.Dirs());
         93         ASSERT_TRUE(d_opt);
         94         ASSERT_EQ(opt_e_arg, d_opt.Exclude());
         95     }
         96     {
         97         char* const argv[]{prog, cmd_p2s, opt_s, opt_in, opt_in_arg, opt_e, opt_e_arg, dir0};
         98 
         99         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        100 
        101         ASSERT_EQ(DepsOpts::Cmd::GenPkg2Srcs, d_opt.GetCmd());
        102         ASSERT_EQ(opt_in_arg, d_opt.In());
        103         ASSERT_EQ("", d_opt.Out());
        104         ASSERT_FALSE(d_opt.IsRecursive());
        105         ASSERT_TRUE(d_opt.IsSrcPkg());
        106         ASSERT_EQ((Paths_t{dir0}), d_opt.Dirs());
        107         ASSERT_TRUE(d_opt);
        108         ASSERT_EQ(opt_e_arg, d_opt.Exclude());
        109     }
        110     {
        111         char* const argv[]{prog, cmd_p2p, opt_in, opt_in_arg, opt_out, opt_out_arg};
        112 
        113         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        114 
        115         ASSERT_EQ(DepsOpts::Cmd::GenPkg2Pkg, d_opt.GetCmd());
        116         ASSERT_EQ(opt_in_arg, d_opt.In());
        117         ASSERT_EQ(opt_out_arg, d_opt.Out());
        118         ASSERT_FALSE(d_opt.IsRecursive());
        119         ASSERT_EQ(Paths_t{}, d_opt.Dirs());
        120         ASSERT_TRUE(d_opt);
        121     }
        122     {
        123         char* const argv[]{prog, cmd_a, opt_in, opt_in_arg, opt_out, opt_out_arg};
        124 
        125         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        126 
        127         ASSERT_EQ(DepsOpts::Cmd::GenArch, d_opt.GetCmd());
        128         ASSERT_EQ(opt_in_arg, d_opt.In());
        129         ASSERT_EQ(opt_out_arg, d_opt.Out());
        130         ASSERT_FALSE(d_opt.IsRecursive());
        131         ASSERT_EQ(Paths_t{}, d_opt.Dirs());
        132         ASSERT_TRUE(d_opt);
        133     }
        134     {
        135         char* const argv[]{prog, cmd_a2pu, opt_in, opt_in_arg, opt_out, opt_out_arg};
        136 
        137         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        138 
        139         ASSERT_EQ(DepsOpts::Cmd::GenPlantUml, d_opt.GetCmd());
        140         ASSERT_EQ(opt_in_arg, d_opt.In());
        141         ASSERT_EQ(opt_out_arg, d_opt.Out());
        142         ASSERT_FALSE(d_opt.IsRecursive());
        143         ASSERT_EQ(Paths_t{}, d_opt.Dirs());
        144         ASSERT_TRUE(d_opt);
        145     }
        146     {
        147         char* const argv[]{prog, cmd_help};
        148 
        149         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        150 
        151         ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        152         ASSERT_TRUE(d_opt);
        153     }
        154     {
        155         char* const argv[]{prog, cmd_dd_help};
        156 
        157         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        158 
        159         ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        160         ASSERT_TRUE(d_opt);
        161     }
        162     {
        163         char* const argv[]{prog, cmd_h};
        164 
        165         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        166 
        167         ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        168         ASSERT_TRUE(d_opt);
        169     }
        170     {
        171         char* const argv[]{prog, cmd_d_h};
        172 
        173         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        174 
        175         ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        176         ASSERT_TRUE(d_opt);
        177     }
        178     {
        179         char* const argv[]{prog, cmd_unknown};
        180 
        181         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        182 
        183         ASSERT_EQ(DepsOpts::Cmd::NotCmd, d_opt.GetCmd());
        184         ASSERT_FALSE(d_opt);
        185     }
        186     {
        187         char* const argv[]{prog, cmd_p, opt_recursive, opt_out, opt_out_arg, opt_help};
        188 
        189         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        190 
        191         ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        192         ASSERT_TRUE(d_opt);
        193     }
        194     {
        195         char* const argv[]{prog, cmd_p, opt_recursive, opt_out, opt_out_arg, opt_h};
        196 
        197         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        198 
        199         ASSERT_EQ(DepsOpts::Cmd::Help, d_opt.GetCmd());
        200         ASSERT_TRUE(d_opt);
        201     }
        202     {
        203         char* const argv[]{prog, cmd_p, opt_log, opt_log_arg, opt_out, opt_out_arg};
        204 
        205         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        206 
        207         ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
        208         ASSERT_EQ(opt_log_arg, d_opt.Log());
        209         ASSERT_EQ(opt_out_arg, d_opt.Out());
        210         ASSERT_TRUE(d_opt);
        211     }
        212     {
        213         char* const argv[]{prog, cmd_p, opt_log, opt_log_dash, opt_in, opt_in_arg};
        214 
        215         auto d_opt = DepsOpts{Nstd::ArrayLength(argv), argv};
        216 
        217         ASSERT_EQ(DepsOpts::Cmd::GenPkg, d_opt.GetCmd());
        218         ASSERT_EQ(opt_log_dash, d_opt.Log());
        219         ASSERT_EQ(opt_in_arg, d_opt.In());
        220         ASSERT_TRUE(d_opt);
        221     }
        222 }
        223 }  // namespace
        224 }  // namespace App
```

### example/deps/dependency/h/dependency/deps_scenario.h <a id="SS_23_2_5"></a>
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
         12     virtual bool Output(std::ostream& os) const = 0;
         13     virtual ~ScenarioGenerator() {}
         14 };
         15 
         16 class PkgGenerator : public ScenarioGenerator {
         17 public:
         18     explicit PkgGenerator(std::string const& in, bool recursive, FileUtils::Paths_t const& dirs_opt,
         19                           std::string const& pattern);
         20     virtual bool Output(std::ostream& os) const override;
         21 
         22 private:
         23     FileUtils::Paths_t const dirs_;
         24 };
         25 
         26 class SrcsGenerator : public ScenarioGenerator {
         27 public:
         28     explicit SrcsGenerator(std::string const& in, bool recursive,
         29                            FileUtils::Paths_t const& dirs_opt, std::string const& pattern);
         30     virtual bool Output(std::ostream& os) const override;
         31 
         32 private:
         33     FileUtils::Paths_t const dirs_;
         34 };
         35 
         36 class Pkg2SrcsGenerator : public ScenarioGenerator {
         37 public:
         38     explicit Pkg2SrcsGenerator(std::string const& in, bool recursive, bool src_as_pkg,
         39                                FileUtils::Paths_t const& dirs_opt, std::string const& pattern);
         40     virtual bool Output(std::ostream& os) const override;
         41 
         42 private:
         43     FileUtils::Dirs2Srcs_t const dirs2srcs_;
         44 };
         45 
         46 class Pkg2PkgGenerator : public ScenarioGenerator {
         47 public:
         48     explicit Pkg2PkgGenerator(std::string const& in, bool recursive, bool src_as_pkg,
         49                               FileUtils::Paths_t const& dirs_opt, std::string const& pattern);
         50     virtual bool Output(std::ostream& os) const override;
         51 
         52 private:
         53     FileUtils::Dirs2Srcs_t const dirs2srcs_;
         54 };
         55 
         56 class ArchGenerator : public ScenarioGenerator {
         57 public:
         58     explicit ArchGenerator(std::string const& in);
         59     virtual bool Output(std::ostream& os) const override;
         60     ~ArchGenerator();
         61 
         62 protected:
         63     struct Impl;
         64     std::unique_ptr<Impl> impl_;
         65 };
         66 
         67 class Arch2PUmlGenerator : public ArchGenerator {
         68 public:
         69     explicit Arch2PUmlGenerator(std::string const& in);
         70     virtual bool Output(std::ostream& os) const override;
         71 };
         72 
         73 class CyclicGenerator : public ArchGenerator {
         74 public:
         75     explicit CyclicGenerator(std::string const& in);
         76     virtual bool Output(std::ostream& os) const override;
         77 
         78 private:
         79     bool has_cyclic_dep_;
         80 };
         81 }  // namespace Dependency
```

### example/deps/dependency/src/arch_pkg.cpp <a id="SS_23_2_6"></a>
```cpp
          1 #include <cassert>
          2 #include <sstream>
          3 
          4 #include "arch_pkg.h"
          5 #include "lib/nstd.h"
          6 
          7 namespace Dependency {
          8 
          9 void ArchPkg::set_cyclic(ArchPkg const* pkg, bool is_cyclic) const
         10 {
         11     assert(std::count(depend_on_.cbegin(), depend_on_.cend(), pkg) != 0);
         12     assert(cyclic_.count(pkg) == 0 || cyclic_[pkg] == is_cyclic);
         13 
         14     cyclic_.insert(std::make_pair(pkg, is_cyclic));
         15 }
         16 
         17 bool ArchPkg::is_cyclic(ArchPkgs_t& history, size_t depth) const
         18 {
         19     if (++depth > max_depth_) {
         20         std::cerr << "too deep dependency:" << name_ << std::endl;
         21         return true;
         22     }
         23 
         24     auto const it = find(history.cbegin(), history.cend(), this);
         25 
         26     if (it != history.cend()) {  // 循環検出
         27         for (auto it2 = it; it2 != history.cend(); ++it2) {
         28             auto next = (std::next(it2) == history.cend()) ? it : std::next(it2);
         29             (*it2)->set_cyclic(*next, true);
         30         }
         31 
         32         // it == history.cbegin()ならば、一番上からの循環 A->B->C->...->A
         33         // it != history.cbegin()ならば、上記以外の循環 A->B->C->...->B
         34         return it == history.cbegin();
         35     }
         36 
         37     auto gs = Nstd::ScopedGuard{[&history] { history.pop_back(); }};
         38     history.push_back(this);
         39 
         40     for (ArchPkg const* pkg : depend_on_) {
         41         if (pkg->is_cyclic(history, depth)) {
         42             return true;
         43         }
         44     }
         45 
         46     return false;
         47 }
         48 
         49 bool ArchPkg::IsCyclic(ArchPkg const& pkg) const
         50 {
         51     if (std::count(depend_on_.cbegin(), depend_on_.cend(), &pkg) == 0) {
         52         return false;
         53     }
         54 
         55     if (cyclic_.count(&pkg) == 0) {
         56         ArchPkgs_t history{this};
         57         set_cyclic(&pkg, pkg.is_cyclic(history, 0));
         58     }
         59 
         60     assert(cyclic_.count(&pkg) != 0);
         61 
         62     return cyclic_[&pkg];
         63 }
         64 
         65 bool ArchPkg::IsCyclic() const noexcept
         66 {
         67     for (ArchPkg const* pkg : DependOn()) {
         68         if (IsCyclic(*pkg)) {
         69             return true;
         70         }
         71     }
         72 
         73     return false;
         74 }
         75 
         76 ArchPkg::Map_Path_ArchPkg_t ArchPkg::build_depend_on(DepRelation const&   dep_rel,
         77                                                      Map_Path_ArchPkg_t&& pkg_all)
         78 {
         79     auto const a_path = FileUtils::Path_t(dep_rel.PackageA);
         80     if (pkg_all.count(a_path) == 0) {
         81         pkg_all.insert(std::make_pair(a_path, std::make_unique<ArchPkg>(a_path)));
         82     }
         83 
         84     auto const b_path = FileUtils::Path_t(dep_rel.PackageB);
         85     if (pkg_all.count(b_path) == 0) {
         86         pkg_all.insert(std::make_pair(b_path, std::make_unique<ArchPkg>(b_path)));
         87     }
         88 
         89     ArchPkgPtr_t& a_ptr = pkg_all.at(a_path);
         90     ArchPkgPtr_t& b_ptr = pkg_all.at(b_path);
         91 
         92     if (dep_rel.CountAtoB != 0) {
         93         a_ptr->depend_on_.push_back(b_ptr.get());
         94     }
         95     if (dep_rel.CountBtoA != 0) {
         96         b_ptr->depend_on_.push_back(a_ptr.get());
         97     }
         98 
         99     return std::move(pkg_all);
        100 }
        101 
        102 Arch_t ArchPkg::build_children(Map_Path_ArchPkg_t&& pkg_all)
        103 {
        104     auto cache = std::map<FileUtils::Path_t, ArchPkg*>{};
        105     auto top   = Arch_t{};
        106 
        107     for (auto& [path, pkg] : pkg_all) {  // C++17 style
        108 
        109         auto const parent_name = path.parent_path();
        110         cache.insert(std::make_pair(path, pkg.get()));
        111 
        112         if (pkg_all.count(parent_name) == 0) {
        113             top.emplace_back(std::move(pkg));
        114         }
        115         else {
        116             ArchPkg* parent = cache.count(parent_name) != 0 ? cache.at(parent_name)
        117                                                             : pkg_all.at(parent_name).get();
        118 
        119             pkg->parent_ = parent;
        120             parent->children_.emplace_back(std::move(pkg));
        121         }
        122     }
        123 
        124     return top;
        125 }
        126 
        127 Arch_t ArchPkg::GenArch(DepRels_t const& dep_rels)
        128 {
        129     auto pkg_all = std::map<FileUtils::Path_t, ArchPkgPtr_t>{};
        130 
        131     for (auto const& d : dep_rels) {
        132         pkg_all = build_depend_on(d, std::move(pkg_all));
        133     }
        134 
        135     auto top = Arch_t{build_children(std::move(pkg_all))};
        136 
        137     return top;
        138 }
        139 
        140 std::string ArchPkg::make_full_name(ArchPkg const& pkg)
        141 {
        142     if (pkg.Parent()) {
        143         return make_full_name(*pkg.Parent()) + "/" + pkg.Name();
        144     }
        145     else {
        146         return pkg.Name();
        147     }
        148 }
        149 
        150 ArchPkg const* FindArchPkgByName(Arch_t const& arch, std::string_view pkg_name) noexcept
        151 {
        152     for (ArchPkgPtr_t const& pkg_ptr : arch) {
        153         if (pkg_ptr->Name() == pkg_name) {
        154             return pkg_ptr.get();
        155         }
        156         else {
        157             ArchPkg const* pkg_found = FindArchPkgByName(pkg_ptr->Children(), pkg_name);
        158             if (pkg_found) {
        159                 return pkg_found;
        160             }
        161         }
        162     }
        163     return nullptr;
        164 }
        165 
        166 ArchPkg const* FindArchPkgByFullName(Arch_t const& arch, std::string_view full_name) noexcept
        167 {
        168     for (ArchPkgPtr_t const& pkg_ptr : arch) {
        169         if (pkg_ptr->FullName() == full_name) {
        170             return pkg_ptr.get();
        171         }
        172         else {
        173             ArchPkg const* pkg_found = FindArchPkgByFullName(pkg_ptr->Children(), full_name);
        174             if (pkg_found) {
        175                 return pkg_found;
        176             }
        177         }
        178     }
        179     return nullptr;
        180 }
        181 
        182 namespace {
        183 
        184 std::string unique_str_name(std::string const& full_name)
        185 {
        186     auto ret = Nstd::Replace(full_name, "/", "___");
        187     return Nstd::Replace(ret, "-", "_");
        188 }
        189 
        190 std::string_view cyclic_str(ArchPkg const& pkg) noexcept
        191 {
        192     if (pkg.IsCyclic()) {
        193         return ":CYCLIC";
        194     }
        195 
        196     return "";
        197 }
        198 
        199 std::string to_string_depend_on(ArchPkg const& pkg_top, uint32_t indent)
        200 {
        201     auto ss         = std::ostringstream{};
        202     auto indent_str = std::string(indent, ' ');
        203 
        204     auto first = true;
        205 
        206     for (ArchPkg const* pkg : pkg_top.DependOn()) {
        207         if (!std::exchange(first, false)) {
        208             ss << std::endl;
        209         }
        210 
        211         ss << indent_str << pkg->Name();
        212 
        213         if (pkg_top.IsCyclic(*pkg)) {
        214             ss << " : CYCLIC";
        215         }
        216         else {
        217             ss << " : STRAIGHT";
        218         }
        219     }
        220 
        221     return ss.str();
        222 }
        223 
        224 std::string to_string_pkg(ArchPkg const& arch_pkg, uint32_t indent)
        225 {
        226     static auto const top        = std::string{"TOP"};
        227     auto              ss         = std::ostringstream{};
        228     auto              indent_str = std::string(indent, ' ');
        229 
        230     auto package   = "package  :";
        231     auto full      = "fullname :";
        232     auto parent    = "parent   :";
        233     auto children  = "children : {";
        234     auto depend_on = "depend_on: {";
        235 
        236     constexpr auto next_indent = 4U;
        237 
        238     ss << indent_str << package << arch_pkg.Name() << cyclic_str(arch_pkg) << std::endl;
        239     ss << indent_str << full << arch_pkg.FullName() << std::endl;
        240     ss << indent_str << parent << (arch_pkg.Parent() ? arch_pkg.Parent()->Name() : top)
        241        << std::endl;
        242 
        243     ss << indent_str << depend_on;
        244     if (arch_pkg.DependOn().size() != 0) {
        245         ss << std::endl;
        246         ss << to_string_depend_on(arch_pkg, indent + next_indent) << std::endl;
        247         ss << indent_str << "}" << std::endl;
        248     }
        249     else {
        250         ss << " }" << std::endl;
        251     }
        252 
        253     ss << indent_str << children;
        254     if (arch_pkg.Children().size() != 0) {
        255         ss << std::endl;
        256         ss << ToStringArch(arch_pkg.Children(), indent + next_indent) << std::endl;
        257         ss << indent_str << "}";
        258     }
        259     else {
        260         ss << " }";
        261     }
        262 
        263     return ss.str();
        264 }
        265 }  // namespace
        266 
        267 std::string ToStringArch(Arch_t const& arch, uint32_t indent)
        268 {
        269     auto ss    = std::ostringstream{};
        270     auto first = true;
        271 
        272     for (auto const& pkg : arch) {
        273         if (!std::exchange(first, false)) {
        274             ss << std::endl << std::endl;
        275         }
        276         ss << to_string_pkg(*pkg, indent);
        277     }
        278 
        279     return ss.str();
        280 }
        281 
        282 namespace {
        283 std::string to_pu_rectangle(ArchPkg const& pkg, uint32_t indent)
        284 {
        285     auto ss         = std::ostringstream{};
        286     auto indent_str = std::string(indent, ' ');
        287 
        288     ss << indent_str << "rectangle \"" << pkg.Name() << "\" as " << unique_str_name(pkg.FullName());
        289 
        290     if (pkg.Children().size() != 0) {
        291         ss << " {" << std::endl;
        292         ss << ToPlantUML_Rectangle(pkg.Children(), indent + 4);
        293         ss << std::endl << indent_str << "}";
        294     }
        295 
        296     return ss.str();
        297 }
        298 }  // namespace
        299 
        300 std::string ToPlantUML_Rectangle(Arch_t const& arch, uint32_t indent)
        301 {
        302     auto ss    = std::ostringstream{};
        303     auto first = true;
        304 
        305     for (auto const& pkg : arch) {
        306         if (!std::exchange(first, false)) {
        307             ss << std::endl;
        308         }
        309         ss << to_pu_rectangle(*pkg, indent);
        310     }
        311 
        312     return ss.str();
        313 }
        314 
        315 namespace {
        316 
        317 // 単方向依存のみ
        318 bool dep_is_cyclic(std::string const& from, std::string const& to, Arch_t const& arch) noexcept
        319 {
        320     ArchPkg const* pkg_from = FindArchPkgByFullName(arch, from);
        321     ArchPkg const* pkg_to   = FindArchPkgByFullName(arch, to);
        322 
        323     assert(pkg_from != nullptr);
        324     assert(pkg_to != nullptr);
        325 
        326     return pkg_from->IsCyclic(*pkg_to);
        327 }
        328 
        329 std::string_view pu_link_color(std::string const& from, std::string const& to,
        330                                Arch_t const& arch) noexcept
        331 {
        332     return dep_is_cyclic(from, to, arch) ? "orange" : "green";
        333 }
        334 
        335 std::string to_pu_rectangle(Arch_t const& arch, DepRelation const& dep_rel)
        336 {
        337     auto ss = std::ostringstream{};
        338     auto a  = unique_str_name(dep_rel.PackageA);
        339     auto b  = unique_str_name(dep_rel.PackageB);
        340 
        341     if (dep_rel.CountAtoB != 0) {
        342         ss << a << " \"" << dep_rel.CountAtoB << "\" ";
        343         if (dep_rel.CountBtoA != 0) {
        344             ss << "<-[#red]-> \"" << dep_rel.CountBtoA << "\" " << b;
        345         }
        346         else {
        347             ss << "-[#" << pu_link_color(dep_rel.PackageA, dep_rel.PackageB, arch) << "]-> " << b;
        348         }
        349     }
        350     else if (dep_rel.CountBtoA != 0) {
        351         ss << b << " \"" << dep_rel.CountBtoA << "\" -[#"
        352            << pu_link_color(dep_rel.PackageB, dep_rel.PackageA, arch) << "]-> " << a;
        353     }
        354 
        355     return ss.str();
        356 }
        357 }  // namespace
        358 
        359 bool HasCyclicDeps(Arch_t const& arch, DepRels_t const& dep_rels) noexcept
        360 {
        361     for (auto const& dep : dep_rels) {
        362         if (dep.CountAtoB != 0) {
        363             if (dep.CountBtoA != 0) {
        364                 return true;
        365             }
        366             else {
        367                 if (dep_is_cyclic(dep.PackageA, dep.PackageB, arch)) {
        368                     return true;
        369                 }
        370             }
        371         }
        372         else if (dep.CountBtoA != 0) {
        373             if (dep_is_cyclic(dep.PackageB, dep.PackageA, arch)) {
        374                 return true;
        375             }
        376         }
        377     }
        378 
        379     return false;
        380 }
        381 
        382 std::string ToPlantUML_Rectangle(Arch_t const& arch, DepRels_t const& dep_rels)
        383 {
        384     auto ss = std::ostringstream{};
        385 
        386     auto first = true;
        387     for (auto const& d : dep_rels) {
        388         auto rel_s = to_pu_rectangle(arch, d);
        389 
        390         if (rel_s.size() != 0) {
        391             if (!std::exchange(first, false)) {
        392                 ss << std::endl;
        393             }
        394             ss << rel_s;
        395         }
        396     }
        397     return ss.str();
        398 }
        399 }  // namespace Dependency
```

### example/deps/dependency/src/arch_pkg.h <a id="SS_23_2_7"></a>
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
         10 using Arch_t       = std::list<ArchPkgPtr_t>;
         11 
         12 using ArchPkgs_t = std::vector<ArchPkg const*>;
         13 
         14 class ArchPkg {
         15 public:
         16     explicit ArchPkg(FileUtils::Path_t const& full_name)
         17         : name_{full_name.filename()}, full_name_{full_name}
         18     {
         19     }
         20 
         21     std::string const& Name() const noexcept { return name_; }
         22     ArchPkg const*     Parent() const noexcept { return parent_; }
         23     Arch_t const&      Children() const noexcept { return children_; }
         24     ArchPkgs_t const&  DependOn() const noexcept { return depend_on_; }
         25     bool               IsCyclic() const noexcept;
         26     bool               IsCyclic(ArchPkg const& pkg) const;
         27     std::string const& FullName() const noexcept { return full_name_; }
         28 
         29     ArchPkg(ArchPkg const&)            = delete;
         30     ArchPkg& operator=(ArchPkg const&) = delete;
         31 
         32     static Arch_t GenArch(DepRels_t const& deps);
         33 
         34 private:
         35     std::string const                      name_;
         36     std::string const                      full_name_{};
         37     ArchPkg const*                         parent_{};
         38     Arch_t                                 children_{};
         39     ArchPkgs_t                             depend_on_{};
         40     mutable std::map<ArchPkg const*, bool> cyclic_{};
         41     static constexpr size_t                max_depth_{12};
         42 
         43     void set_cyclic(ArchPkg const* pkg, bool is_cyclic) const;
         44 
         45     using Map_Path_ArchPkg_t = std::map<FileUtils::Path_t, ArchPkgPtr_t>;
         46     static Map_Path_ArchPkg_t build_depend_on(DepRelation const&   dep_rel,
         47                                               Map_Path_ArchPkg_t&& pkg_all);
         48     static Arch_t             build_children(Map_Path_ArchPkg_t&& pkg_all);
         49     static std::string        make_full_name(ArchPkg const& pkg);
         50     bool                      is_cyclic(ArchPkgs_t& history, size_t depth) const;
         51 };
         52 
         53 std::string          ToStringArch(Arch_t const& arch, uint32_t indent = 0);
         54 inline std::ostream& operator<<(std::ostream& os, Arch_t const& arch)
         55 {
         56     return os << ToStringArch(arch);
         57 }
         58 
         59 std::string ToPlantUML_Rectangle(Arch_t const& arch, uint32_t indent = 0);
         60 std::string ToPlantUML_Rectangle(Arch_t const& arch, DepRels_t const& dep_rels);
         61 bool        HasCyclicDeps(Arch_t const& arch, DepRels_t const& dep_rels) noexcept;
         62 
         63 ArchPkg const* FindArchPkgByName(Arch_t const& arch, std::string_view pkg_name) noexcept;
         64 ArchPkg const* FindArchPkgByFullName(Arch_t const& arch, std::string_view full_name) noexcept;
         65 }  // namespace Dependency
```

### example/deps/dependency/src/cpp_deps.cpp <a id="SS_23_2_8"></a>
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
         13 bool operator==(DepRelation const& lhs, DepRelation const& rhs) noexcept
         14 {
         15     return std::tie(lhs.PackageA, lhs.CountAtoB, lhs.IncsAtoB, lhs.PackageB, lhs.CountBtoA,
         16                     lhs.IncsBtoA)
         17            == std::tie(rhs.PackageA, rhs.CountAtoB, rhs.IncsAtoB, rhs.PackageB, rhs.CountBtoA,
         18                        rhs.IncsBtoA);
         19 }
         20 
         21 std::string ToStringDepRel(DepRelation const& rep_rel)
         22 {
         23     auto ss = std::ostringstream{};
         24 
         25     ss << FileUtils::ToStringPath(rep_rel.PackageA) << " -> "
         26        << FileUtils::ToStringPath(rep_rel.PackageB) << " : " << rep_rel.CountAtoB << " "
         27        << FileUtils::ToStringPaths(rep_rel.IncsAtoB, " ") << std::endl;
         28 
         29     ss << FileUtils::ToStringPath(rep_rel.PackageB) << " -> "
         30        << FileUtils::ToStringPath(rep_rel.PackageA) << " : " << rep_rel.CountBtoA << " "
         31        << FileUtils::ToStringPaths(rep_rel.IncsBtoA, " ");
         32 
         33     return ss.str();
         34 }
         35 
         36 std::string ToStringDepRels(DepRels_t const& dep_rels)
         37 {
         38     auto ss = std::ostringstream{};
         39 
         40     auto first = true;
         41     for (auto const& dep : dep_rels) {
         42         if (!std::exchange(first, false)) {
         43             ss << std::endl;
         44         }
         45         ss << ToStringDepRel(dep) << std::endl;
         46     }
         47 
         48     return ss.str();
         49 }
         50 
         51 namespace {
         52 DepRelation gen_DepRelation(CppDir const& dirA, CppDir const& dirB)
         53 {
         54     auto a_dep        = std::pair<uint32_t, FileUtils::Paths_t>{dirA.DependsOn(dirB)};
         55     auto count_from_a = a_dep.first;
         56     auto incs_from_a  = std::move(a_dep.second);
         57 
         58     auto b_dep        = std::pair<uint32_t, FileUtils::Paths_t>{dirB.DependsOn(dirA)};
         59     auto count_from_b = b_dep.first;
         60     auto incs_from_b  = std::move(b_dep.second);
         61 
         62     if (dirA < dirB) {
         63         return DepRelation{dirA.Path(), count_from_a, std::move(incs_from_a),
         64                            dirB.Path(), count_from_b, std::move(incs_from_b)};
         65     }
         66     else {
         67         return DepRelation{dirB.Path(), count_from_b, std::move(incs_from_b),
         68                            dirA.Path(), count_from_a, std::move(incs_from_a)};
         69     }
         70 }
         71 }  // namespace
         72 
         73 Dir2Dir_t GenDir2Dir(std::string dirA, std::string dirB)
         74 {
         75     return dirA < dirB ? std::make_pair(std::move(dirA), std::move(dirB))
         76                        : std::make_pair(std::move(dirB), std::move(dirA));
         77 }
         78 
         79 DepRels_t GenDepRels(CppDirs_t const& cpp_dirs)
         80 {
         81     auto ret = DepRels_t{};
         82 
         83     for (auto const& dirA : cpp_dirs) {
         84         for (auto const& dirB : cpp_dirs) {
         85             if (dirA <= dirB) {
         86                 continue;
         87             }
         88             ret.emplace_back(gen_DepRelation(dirA, dirB));
         89         }
         90     }
         91 
         92     ret.sort();
         93 
         94     return ret;
         95 }
         96 
         97 DepRels_t::const_iterator FindDepRels(DepRels_t const& dep_rels, std::string const& dirA,
         98                                       std::string const& dirB) noexcept
         99 {
        100     assert(dirA != dirB);
        101 
        102     auto dirs = std::minmax(dirA, dirB);
        103 
        104     return std::find_if(dep_rels.cbegin(), dep_rels.cend(), [&dirs](auto const& d) noexcept {
        105         return d.PackageA == dirs.first && d.PackageB == dirs.second;
        106     });
        107 }
        108 }  // namespace Dependency
```

### example/deps/dependency/src/cpp_deps.h <a id="SS_23_2_9"></a>
```cpp
          1 #pragma once
          2 #include <vector>
          3 
          4 #include "cpp_deps.h"
          5 #include "cpp_dir.h"
          6 #include "file_utils/path_utils.h"
          7 
          8 namespace Dependency {
          9 
         10 struct DepRelation {
         11     explicit DepRelation(std::string package_a, uint32_t count_a2b, FileUtils::Paths_t&& incs_a2b,
         12                          std::string package_b, uint32_t count_b2a, FileUtils::Paths_t&& incs_b2a)
         13         : PackageA{std::move(package_a)},
         14           CountAtoB{count_a2b},
         15           IncsAtoB{std::move(incs_a2b)},
         16           PackageB{std::move(package_b)},
         17           CountBtoA{count_b2a},
         18           IncsBtoA{std::move(incs_b2a)}
         19     {
         20     }
         21 
         22     std::string const        PackageA;
         23     uint32_t const           CountAtoB;
         24     FileUtils::Paths_t const IncsAtoB;
         25 
         26     std::string const        PackageB;
         27     uint32_t const           CountBtoA;
         28     FileUtils::Paths_t const IncsBtoA;
         29 };
         30 
         31 using Dir2Dir_t = std::pair<std::string, std::string>;
         32 using DepRels_t = std::list<DepRelation>;
         33 
         34 std::string ToStringDepRel(DepRelation const& rep_rel);
         35 
         36 bool        operator==(DepRelation const& lhs, DepRelation const& rhs) noexcept;
         37 inline bool operator!=(DepRelation const& lhs, DepRelation const& rhs) noexcept
         38 {
         39     return !(lhs == rhs);
         40 }
         41 inline bool operator<(DepRelation const& lhs, DepRelation const& rhs) noexcept
         42 {
         43     return lhs.PackageA != rhs.PackageA ? lhs.PackageA < rhs.PackageA : lhs.PackageB < rhs.PackageB;
         44 }
         45 
         46 inline bool operator>(DepRelation const& lhs, DepRelation const& rhs) noexcept { return rhs < lhs; }
         47 
         48 inline std::ostream& operator<<(std::ostream& os, DepRelation const& dep_rel)
         49 {
         50     return os << ToStringDepRel(dep_rel);
         51 }
         52 
         53 Dir2Dir_t GenDir2Dir(std::string const& dirA, std::string const& dirB);
         54 
         55 std::string          ToStringDepRels(DepRels_t const& dep_rels);
         56 inline std::ostream& operator<<(std::ostream& os, DepRels_t const& dep_rels)
         57 {
         58     return os << ToStringDepRels(dep_rels);
         59 }
         60 
         61 DepRels_t                 GenDepRels(CppDirs_t const& dirs);
         62 DepRels_t::const_iterator FindDepRels(DepRels_t const& dep_rels, std::string const& dirA,
         63                                       std::string const& dirB) noexcept;
         64 }  // namespace Dependency
```

### example/deps/dependency/src/cpp_dir.cpp <a id="SS_23_2_10"></a>
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
         11 bool CppDir::Contains(FileUtils::Path_t const& inc_path) const noexcept
         12 {
         13     for (auto const& src : srcs_) {
         14         if (src.Path() == inc_path) {
         15             return true;
         16         }
         17     }
         18 
         19     return false;
         20 }
         21 
         22 std::pair<uint32_t, FileUtils::Paths_t> CppDir::DependsOn(CppDir const& cpp_pack) const
         23 {
         24     auto count = 0U;
         25     auto incs  = FileUtils::Paths_t{};
         26 
         27     for (auto const& src : srcs_) {
         28         for (auto const& inc : src.GetIncs()) {
         29             if (cpp_pack.Contains(inc)) {
         30                 incs.push_back(inc);
         31                 ++count;
         32             }
         33         }
         34     }
         35 
         36     Nstd::SortUnique(incs);
         37 
         38     return {count, std::move(incs)};
         39 }
         40 
         41 bool operator==(CppDir const& lhs, CppDir const& rhs) noexcept
         42 {
         43     return std::tie(lhs.path_, lhs.srcs_) == std::tie(rhs.path_, rhs.srcs_);
         44 }
         45 
         46 bool operator<(CppDir const& lhs, CppDir const& rhs) noexcept
         47 {
         48     return std::tie(lhs.path_, lhs.srcs_) < std::tie(rhs.path_, rhs.srcs_);
         49 }
         50 
         51 CppDirs_t GenCppDirs(FileUtils::Paths_t const& srcs, FileUtils::Filename2Path_t const& db)
         52 {
         53     auto ret = CppDirs_t{};
         54 
         55     for (auto const& src : srcs) {
         56         auto cpp_src = CppSrc{src, db};
         57         ret.emplace_back(CppDir{cpp_src.Filename(), {cpp_src}});
         58     }
         59 
         60     return ret;
         61 }
         62 
         63 std::string ToStringCppDir(CppDir const& cpp_pack)
         64 {
         65     auto ss = std::ostringstream{};
         66 
         67     ss << FileUtils::ToStringPath(cpp_pack.Path()) << std::endl;
         68 
         69     auto first = true;
         70     for (auto const& src : cpp_pack.GetSrcs()) {
         71         if (first) {
         72             first = false;
         73         }
         74         else {
         75             ss << std::endl;
         76         }
         77         ss << ToStringCppSrc(src);
         78     }
         79 
         80     return ss.str();
         81 }
         82 }  // namespace Dependency
```

### example/deps/dependency/src/cpp_dir.h <a id="SS_23_2_11"></a>
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
         13     explicit CppDir(FileUtils::Path_t const& path, CppSrcs_t&& srcs)
         14         : path_{path}, srcs_{std::move(srcs)}
         15     {
         16     }
         17 
         18     FileUtils::Path_t const& Path() const noexcept { return path_; }
         19     bool                     Contains(FileUtils::Path_t const& inc_path) const noexcept;
         20 
         21     // first  依存するヘッダファイルのインクルード数
         22     // second 依存するヘッダファイル
         23     std::pair<uint32_t, FileUtils::Paths_t> DependsOn(CppDir const& cpp_pack) const;
         24     CppSrcs_t const&                        GetSrcs() const noexcept { return srcs_; }
         25 
         26 private:
         27     FileUtils::Path_t const path_;
         28     CppSrcs_t const         srcs_;
         29 
         30     friend bool operator==(CppDir const& lhs, CppDir const& rhs) noexcept;
         31     friend bool operator<(CppDir const& lhs, CppDir const& rhs) noexcept;
         32 };
         33 
         34 inline bool operator<=(CppDir const& lhs, CppDir const& rhs) noexcept
         35 {
         36     if (lhs == rhs) {
         37         return true;
         38     }
         39 
         40     return lhs < rhs;
         41 }
         42 
         43 inline bool operator!=(CppDir const& lhs, CppDir const& rhs) noexcept { return !(lhs == rhs); }
         44 inline bool operator>(CppDir const& lhs, CppDir const& rhs) noexcept { return rhs < lhs; }
         45 inline bool operator>=(CppDir const& lhs, CppDir const& rhs) noexcept { return rhs <= lhs; }
         46 
         47 using CppDirs_t = std::vector<CppDir>;
         48 
         49 CppDirs_t GenCppDirs(FileUtils::Paths_t const& srcs, FileUtils::Filename2Path_t const& db);
         50 
         51 std::string          ToStringCppDir(CppDir const& cpp_pack);
         52 inline std::ostream& operator<<(std::ostream& os, CppDir const& dir)
         53 {
         54     return os << ToStringCppDir(dir);
         55 }
         56 }  // namespace Dependency
```

### example/deps/dependency/src/cpp_src.cpp <a id="SS_23_2_12"></a>
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
         12 FileUtils::Paths_t get_incs(FileUtils::Path_t const& src)
         13 {
         14     static auto const include_line = std::regex{R"(^\s*#include\s+["<]([\w/.]+)[">](.*))"};
         15 
         16     auto ret  = FileUtils::Paths_t{};
         17     auto f    = std::ifstream{src};
         18     auto line = std::string{};
         19 
         20     while (std::getline(f, line)) {
         21         if (line.size() > 0) {  // CRLF対策
         22             auto last = --line.end();
         23             if (*last == '\xa' || *last == '\xd') {
         24                 line.erase(last);
         25             }
         26         }
         27 
         28         if (auto results = std::smatch{}; std::regex_match(line, results, include_line)) {
         29             ret.emplace_back(FileUtils::Path_t(results[1].str()).filename());
         30         }
         31     }
         32 
         33     return ret;
         34 }
         35 
         36 void get_incs_full(FileUtils::Filename2Path_t const& db, FileUtils::Path_t const& src,
         37                    FileUtils::Paths_t& incs, FileUtils::Paths_t& not_found, bool sort_uniq)
         38 {
         39     auto const inc_files = get_incs(src);
         40 
         41     for (auto const& f : inc_files) {
         42         if (db.count(f) == 0) {
         43             not_found.push_back(f);
         44         }
         45         else {
         46             auto full_path = db.at(f);
         47             if (!any_of(
         48                     incs.cbegin(), incs.cend(),
         49                     [&full_path](FileUtils::Path_t const& p) noexcept { return p == full_path; })) {
         50                 incs.emplace_back(full_path);
         51                 get_incs_full(db, full_path, incs, not_found, false);
         52             }
         53         }
         54     }
         55 
         56     if (sort_uniq) {
         57         Nstd::SortUnique(incs);
         58         Nstd::SortUnique(not_found);
         59     }
         60 }
         61 }  // namespace
         62 
         63 namespace Dependency {
         64 
         65 CppSrc::CppSrc(FileUtils::Path_t const& pathname, FileUtils::Filename2Path_t const& db)
         66     : path_{FileUtils::NormalizeLexically(pathname)},
         67       filename_{path_.filename()},
         68       incs_{},
         69       not_found_{}
         70 {
         71     get_incs_full(db, pathname, incs_, not_found_, true);
         72 }
         73 
         74 bool operator==(CppSrc const& lhs, CppSrc const& rhs) noexcept
         75 {
         76     return std::tie(lhs.path_, lhs.filename_, lhs.incs_, lhs.not_found_)
         77            == std::tie(rhs.path_, rhs.filename_, rhs.incs_, rhs.not_found_);
         78 }
         79 
         80 bool operator<(CppSrc const& lhs, CppSrc const& rhs) noexcept
         81 {
         82     return std::tie(lhs.path_, lhs.filename_, lhs.incs_, lhs.not_found_)
         83            < std::tie(rhs.path_, rhs.filename_, rhs.incs_, rhs.not_found_);
         84 }
         85 
         86 CppSrcs_t GenCppSrc(FileUtils::Paths_t const& srcs, FileUtils::Filename2Path_t const& db)
         87 {
         88     auto ret = CppSrcs_t{};
         89 
         90     for (auto const& src : srcs) {
         91         ret.emplace_back(CppSrc{src, db});
         92     }
         93 
         94     return ret;
         95 }
         96 
         97 std::string ToStringCppSrc(CppSrc const& cpp_src)
         98 {
         99     auto ss = std::ostringstream{};
        100 
        101     ss << "file              : " << FileUtils::ToStringPath(cpp_src.Filename()) << std::endl;
        102     ss << "path              : " << FileUtils::ToStringPath(cpp_src.Path()) << std::endl;
        103     ss << "include           : " << FileUtils::ToStringPaths(cpp_src.GetIncs(), " ") << std::endl;
        104     ss << "include not found : " << FileUtils::ToStringPaths(cpp_src.GetIncsNotFound(), " ")
        105        << std::endl;
        106 
        107     return ss.str();
        108 }
        109 
        110 namespace {
        111 constexpr std::string_view target_ext[]{".c", ".h", ".cpp", ".cxx", ".cc", ".hpp", ".hxx", ".tcc"};
        112 
        113 bool is_c_or_cpp(std::string ext)
        114 {
        115     std::transform(ext.begin(), ext.end(), ext.begin(), ::tolower);
        116 
        117     if (std::any_of(std::begin(target_ext), std::end(target_ext),
        118                     [&ext](std::string_view s) noexcept { return s == ext; })) {
        119         return true;
        120     }
        121 
        122     return false;
        123 }
        124 
        125 FileUtils::Paths_t gen_dirs(FileUtils::Path_t const& top_dir, FileUtils::Paths_t const& srcs)
        126 {
        127     auto dirs           = FileUtils::Paths_t{top_dir};
        128     auto const top_dir2 = FileUtils::Path_t{""};  // top_dirが"."の場合、parent_path()は""になる}。
        129 
        130     for (auto const& src : srcs) {
        131         for (auto dir = src.parent_path(); dir != top_dir && dir != top_dir2;
        132              dir      = dir.parent_path()) {
        133             dirs.push_back(dir);
        134         }
        135     }
        136 
        137     return dirs;
        138 }
        139 
        140 FileUtils::Paths_t find_c_or_cpp_srcs(FileUtils::Path_t const& top_path)
        141 {
        142     auto srcs = FileUtils::Paths_t{};
        143 
        144     namespace fs = std::filesystem;
        145     for (fs::path const& p : fs::recursive_directory_iterator{top_path}) {
        146         if (fs::is_regular_file(p) && is_c_or_cpp(p.extension())) {
        147             srcs.emplace_back(FileUtils::NormalizeLexically(p));
        148         }
        149     }
        150 
        151     return srcs;
        152 }
        153 }  // namespace
        154 
        155 std::pair<FileUtils::Paths_t, FileUtils::Paths_t> GetCppDirsSrcs(FileUtils::Paths_t const& dirs)
        156 {
        157     auto dirs_srcs = FileUtils::Paths_t{};
        158     auto srcs      = FileUtils::Paths_t{};
        159 
        160     for (auto const& dir : dirs) {
        161         FileUtils::Path_t const top_path      = FileUtils::NormalizeLexically(dir);
        162         auto                    sub_srcs      = find_c_or_cpp_srcs(top_path);
        163         auto                    sub_dirs_srcs = gen_dirs(top_path, sub_srcs);
        164 
        165         Nstd::Concatenate(srcs, std::move(sub_srcs));
        166         Nstd::Concatenate(dirs_srcs, std::move(sub_dirs_srcs));
        167     }
        168 
        169     Nstd::SortUnique(srcs);
        170     Nstd::SortUnique(dirs_srcs);
        171 
        172     return {std::move(dirs_srcs), std::move(srcs)};
        173 }
        174 }  // namespace Dependency
```

### example/deps/dependency/src/cpp_src.h <a id="SS_23_2_13"></a>
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
         12     explicit CppSrc(FileUtils::Path_t const& pathname, FileUtils::Filename2Path_t const& db);
         13     FileUtils::Paths_t const& GetIncs() const noexcept { return incs_; }
         14     FileUtils::Paths_t const& GetIncsNotFound() const noexcept { return not_found_; }
         15     FileUtils::Path_t const&  Filename() const noexcept { return filename_; }
         16     FileUtils::Path_t const&  Path() const noexcept { return path_; }
         17 
         18 private:
         19     FileUtils::Path_t const path_;
         20     FileUtils::Path_t const filename_;
         21     FileUtils::Paths_t      incs_;
         22     FileUtils::Paths_t      not_found_;
         23 
         24     friend bool operator==(CppSrc const& lhs, CppSrc const& rhs) noexcept;
         25     friend bool operator<(CppSrc const& lhs, CppSrc const& rhs) noexcept;
         26 };
         27 
         28 inline bool operator!=(CppSrc const& lhs, CppSrc const& rhs) noexcept { return !(lhs == rhs); }
         29 inline bool operator>(CppSrc const& lhs, CppSrc const& rhs) noexcept
         30 {
         31     if (lhs < rhs) {
         32         return false;
         33     }
         34 
         35     return lhs != rhs;
         36 }
         37 
         38 using CppSrcs_t = std::vector<CppSrc>;
         39 CppSrcs_t   GenCppSrc(FileUtils::Paths_t const& srcs, FileUtils::Filename2Path_t const& db);
         40 std::string ToStringCppSrc(CppSrc const& cpp_src);
         41 inline std::ostream& operator<<(std::ostream& os, CppSrc const& cpp_src)
         42 {
         43     return os << ToStringCppSrc(cpp_src);
         44 }
         45 
         46 // first  dirs配下のソースファイルを含むディレクトリ
         47 // second dirs配下のソースファイル
         48 std::pair<FileUtils::Paths_t, FileUtils::Paths_t> GetCppDirsSrcs(FileUtils::Paths_t const& dirs);
         49 }  // namespace Dependency
```

### example/deps/dependency/src/deps_scenario.cpp <a id="SS_23_2_14"></a>
```cpp
          1 #include <cassert>
          2 #include <iostream>
          3 #include <regex>
          4 #include <stdexcept>
          5 
          6 #include "arch_pkg.h"  // 実装用ヘッダファイル
          7 // @@@ sample begin 0:0
          8 
          9 #include "cpp_deps.h"                  // 実装用ヘッダファイル
         10 #include "cpp_dir.h"                   // 実装用ヘッダファイル
         11 #include "cpp_src.h"                   // 実装用ヘッダファイル
         12 #include "dependency/deps_scenario.h"  // dependencyパッケージからのインポート
         13 #include "file_utils/load_store.h"     // file_utilsパッケージからのインポート
         14 #include "lib/nstd.h"                  // libパッケージからのインポート
         15 // @@@ sample end
         16 #include "load_store_format.h"
         17 
         18 namespace Dependency {
         19 namespace {
         20 
         21 bool has_error_for_dir(FileUtils::Paths_t const& dirs)
         22 {
         23     if (dirs.size() == 0) {
         24         throw std::runtime_error{"need directories to generate package"};
         25     }
         26 
         27     auto not_dirs = FileUtils::NotDirs(dirs);
         28 
         29     if (not_dirs.size() != 0) {
         30         throw std::runtime_error{FileUtils::ToStringPaths(not_dirs) + " not directory"};
         31     }
         32 
         33     return false;
         34 }
         35 
         36 FileUtils::Paths_t remove_dirs_match_pattern(FileUtils::Paths_t&& dirs, std::string const& pattern)
         37 {
         38     if (pattern.size() == 0) {
         39         return std::move(dirs);
         40     }
         41 
         42     auto const re_pattern = std::regex{pattern};
         43 
         44     dirs.remove_if([&re_pattern](auto const& d) {
         45         auto results = std::smatch{};
         46         auto d_str   = d.string();
         47         return std::regex_match(d_str, results, re_pattern);
         48     });
         49 
         50     return std::move(dirs);
         51 }
         52 
         53 // first  dirs配下のソースファイルを含むディレクトリ(パッケージ)
         54 // second 上記パッケージに含まれるソースファイル
         55 std::pair<FileUtils::Paths_t, FileUtils::Dirs2Srcs_t> gen_dirs_and_dirs2srcs(
         56     FileUtils::Paths_t const& dirs, bool recursive, std::string const& pattern)
         57 {
         58     auto ret      = std::pair<FileUtils::Paths_t, FileUtils::Paths_t>{GetCppDirsSrcs(dirs)};
         59     auto srcs     = FileUtils::Paths_t{std::move(ret.second)};
         60     auto dirs_pkg = FileUtils::Paths_t{recursive ? std::move(ret.first) : dirs};
         61 
         62     dirs_pkg = remove_dirs_match_pattern(std::move(dirs_pkg), pattern);
         63 
         64     auto dirs2srcs = FileUtils::Dirs2Srcs_t{FileUtils::AssginSrcsToDirs(dirs_pkg, srcs)};
         65 
         66     return {std::move(dirs_pkg), std::move(dirs2srcs)};
         67 }
         68 
         69 FileUtils::Paths_t gen_dirs(FileUtils::Paths_t const& dirs, bool recursive,
         70                             std::string const& pattern)
         71 {
         72     auto dirs2srcs = std::pair<FileUtils::Paths_t, FileUtils::Dirs2Srcs_t>{
         73         gen_dirs_and_dirs2srcs(dirs, recursive, pattern)};
         74 
         75     auto dirs_pkg = FileUtils::Paths_t{std::move(dirs2srcs.first)};
         76     auto assign   = FileUtils::Dirs2Srcs_t{std::move(dirs2srcs.second)};
         77 
         78     auto ret = FileUtils::Paths_t{};
         79     for (auto& dir : dirs_pkg) {
         80         if (assign.count(dir) == 0) {
         81             std::cout << dir << " not including C++ files" << std::endl;
         82         }
         83         else {
         84             ret.emplace_back(std::move(dir));
         85         }
         86     }
         87 
         88     return ret;
         89 }
         90 
         91 FileUtils::Paths_t gen_dirs(std::string const& in, bool recursive,
         92                             FileUtils::Paths_t const& dirs_opt, std::string const& pattern)
         93 {
         94     auto dirs = FileUtils::Paths_t{};
         95 
         96     if (in.size() != 0) {
         97         auto ret = std::optional<FileUtils::Paths_t>{FileUtils::LoadFromFile(in, Load_Paths)};
         98         if (!ret) {
         99             throw std::runtime_error{in + " is illegal"};
        100         }
        101         dirs = std::move(*ret);
        102     }
        103 
        104     Nstd::Concatenate(dirs, FileUtils::Paths_t(dirs_opt));
        105 
        106     if (has_error_for_dir(dirs)) {
        107         return dirs;
        108     }
        109 
        110     return gen_dirs(dirs, recursive, pattern);
        111 }
        112 
        113 bool includes(FileUtils::Paths_t const& dirs, FileUtils::Path_t const& dir) noexcept
        114 {
        115     auto const count
        116         = std::count_if(dirs.cbegin(), dirs.cend(),
        117                         [&dir](auto const& dir_in_dirs) noexcept { return dir_in_dirs == dir; });
        118 
        119     return count != 0;
        120 }
        121 
        122 FileUtils::Dirs2Srcs_t dirs2srcs_to_src2src(FileUtils::Paths_t const&    dirs_opt,
        123                                             FileUtils::Dirs2Srcs_t const dirs2srcs, bool recursive)
        124 {
        125     auto ret = FileUtils::Dirs2Srcs_t{};
        126 
        127     for (auto const& pair : dirs2srcs) {
        128         for (auto const& src : pair.second) {
        129             if (recursive) {
        130                 ret.insert(std::make_pair(src.filename(), FileUtils::Paths_t{src}));
        131             }
        132             else {
        133                 if (includes(dirs_opt, pair.first)) {
        134                     auto dir = FileUtils::NormalizeLexically(src.parent_path());
        135 
        136                     if (dir == pair.first) {
        137                         ret.insert(std::make_pair(src.filename(), FileUtils::Paths_t{src}));
        138                     }
        139                 }
        140             }
        141         }
        142     }
        143 
        144     return ret;
        145 }
        146 
        147 FileUtils::Dirs2Srcs_t gen_dirs2srcs(std::string const& in, bool recursive, bool src_as_pkg,
        148                                      FileUtils::Paths_t const& dirs_opt, std::string const& pattern)
        149 {
        150     auto dirs2srcs = FileUtils::Dirs2Srcs_t{};
        151     auto dirs      = FileUtils::Paths_t{};
        152 
        153     if (in.size() != 0) {
        154         using FileUtils::LoadFromFile;
        155         auto ret = std::optional<FileUtils::Dirs2Srcs_t>{LoadFromFile(in, Load_Dirs2Srcs)};
        156 
        157         if (ret) {
        158             if (dirs_opt.size() != 0) {
        159                 std::cout << "DIRS ignored." << std::endl;
        160             }
        161 
        162             if (recursive) {
        163                 std::cout << "option \"recursive\" ignored." << std::endl;
        164             }
        165             return std::move(*ret);
        166         }
        167         else {
        168             auto ret = std::optional<FileUtils::Paths_t>{LoadFromFile(in, Load_Paths)};
        169 
        170             if (!ret) {
        171                 throw std::runtime_error{in + " is illegal"};
        172             }
        173             dirs = std::move(*ret);
        174         }
        175     }
        176 
        177     Nstd::Concatenate(dirs, FileUtils::Paths_t(dirs_opt));
        178 
        179     if (has_error_for_dir(dirs)) {
        180         return dirs2srcs;
        181     }
        182 
        183     std::pair<FileUtils::Paths_t, FileUtils::Dirs2Srcs_t> ret
        184         = gen_dirs_and_dirs2srcs(dirs, recursive, pattern);
        185 
        186     auto dirs_pkg = FileUtils::Paths_t{std::move(ret.first)};
        187     auto assign   = FileUtils::Dirs2Srcs_t{std::move(ret.second)};
        188 
        189     return src_as_pkg ? dirs2srcs_to_src2src(dirs_opt, assign, recursive) : assign;
        190 }
        191 
        192 FileUtils::Filename2Path_t gen_src_db(FileUtils::Dirs2Srcs_t const& dir2srcs)
        193 {
        194     auto srcs = FileUtils::Paths_t{};
        195 
        196     for (auto const& pair : dir2srcs) {
        197         auto s = pair.second;
        198         Nstd::Concatenate(srcs, std::move(s));
        199     }
        200 
        201     return FileUtils::GenFilename2Path(srcs);
        202 }
        203 }  // namespace
        204 
        205 PkgGenerator::PkgGenerator(std::string const& in, bool recursive,
        206                            FileUtils::Paths_t const& dirs_opt, std::string const& pattern)
        207     : dirs_{gen_dirs(in, recursive, dirs_opt, pattern)}
        208 {
        209 }
        210 
        211 bool PkgGenerator::Output(std::ostream& os) const
        212 {
        213     StoreToStream(os, dirs_);
        214 
        215     return true;
        216 }
        217 
        218 SrcsGenerator::SrcsGenerator(std::string const& in, bool recursive,
        219                              FileUtils::Paths_t const& dirs_opt, std::string const& pattern)
        220     : dirs_{gen_dirs(in, recursive, dirs_opt, pattern)}
        221 {
        222 }
        223 
        224 bool SrcsGenerator::Output(std::ostream& os) const
        225 {
        226     auto       ret  = std::pair<FileUtils::Paths_t, FileUtils::Paths_t>{GetCppDirsSrcs(dirs_)};
        227     auto       dirs = FileUtils::Paths_t{std::move(ret.first)};
        228     auto       srcs = FileUtils::Paths_t{std::move(ret.second)};
        229     auto const db   = FileUtils::GenFilename2Path(srcs);
        230 
        231     auto cpp_dirs = CppDirs_t{GenCppDirs(srcs, db)};
        232 
        233     for (auto const& d : cpp_dirs) {
        234         os << "---" << std::endl;
        235         os << d << std::endl;
        236     }
        237 
        238     return true;
        239 }
        240 
        241 Pkg2SrcsGenerator::Pkg2SrcsGenerator(std::string const& in, bool recursive, bool src_as_pkg,
        242                                      FileUtils::Paths_t const& dirs_opt, std::string const& pattern)
        243     : dirs2srcs_{gen_dirs2srcs(in, recursive, src_as_pkg, dirs_opt, pattern)}
        244 {
        245 }
        246 
        247 bool Pkg2SrcsGenerator::Output(std::ostream& os) const
        248 {
        249     StoreToStream(os, dirs2srcs_);
        250 
        251     return true;
        252 }
        253 
        254 Pkg2PkgGenerator::Pkg2PkgGenerator(std::string const& in, bool recursive, bool src_as_pkg,
        255                                    FileUtils::Paths_t const& dirs_opt, std::string const& pattern)
        256     : dirs2srcs_{gen_dirs2srcs(in, recursive, src_as_pkg, dirs_opt, pattern)}
        257 {
        258 }
        259 
        260 bool Pkg2PkgGenerator::Output(std::ostream& os) const
        261 {
        262     auto cpp_dirs = CppDirs_t{};
        263 
        264     auto const db = gen_src_db(dirs2srcs_);
        265 
        266     for (auto const& pair : dirs2srcs_) {
        267         cpp_dirs.emplace_back(CppDir{pair.first, GenCppSrc(pair.second, db)});
        268     }
        269 
        270     DepRels_t const dep_rels = GenDepRels(cpp_dirs);
        271 
        272     StoreToStream(os, dep_rels);
        273 
        274     return true;
        275 }
        276 
        277 namespace {
        278 DepRels_t gen_dep_rel(std::string const& in)
        279 {
        280     if (in.size() == 0) {
        281         throw std::runtime_error{"IN-file needed"};
        282     }
        283 
        284     auto ret = std::optional<DepRels_t>{FileUtils::LoadFromFile(in, Load_DepRels)};
        285 
        286     if (!ret) {
        287         throw std::runtime_error{"IN-file load error"};
        288     }
        289 
        290     return *ret;
        291 }
        292 }  // namespace
        293 
        294 struct ArchGenerator::Impl {
        295     Impl(DepRels_t&& a_dep_rels) : dep_rels(std::move(a_dep_rels)), arch(ArchPkg::GenArch(dep_rels))
        296     {
        297     }
        298     DepRels_t const dep_rels;
        299     Arch_t const    arch;
        300 };
        301 
        302 ArchGenerator::ArchGenerator(std::string const& in)
        303     : impl_{std::make_unique<ArchGenerator::Impl>(gen_dep_rel(in))}
        304 {
        305 }
        306 
        307 bool ArchGenerator::Output(std::ostream& os) const
        308 {
        309     StoreToStream(os, impl_->arch);
        310 
        311     return true;
        312 }
        313 ArchGenerator::~ArchGenerator() {}
        314 
        315 Arch2PUmlGenerator::Arch2PUmlGenerator(std::string const& in) : ArchGenerator{in} {}
        316 
        317 bool Arch2PUmlGenerator::Output(std::ostream& os) const
        318 {
        319     os << "@startuml" << std::endl;
        320     os << "scale max 730 width" << std::endl;  // これ以上大きいとpdfにした時に右端が切れる
        321 
        322     os << ToPlantUML_Rectangle(impl_->arch) << std::endl;
        323     os << std::endl;
        324 
        325     os << ToPlantUML_Rectangle(impl_->arch, impl_->dep_rels) << std::endl;
        326     os << std::endl;
        327 
        328     os << "@enduml" << std::endl;
        329 
        330     return true;
        331 }
        332 
        333 CyclicGenerator::CyclicGenerator(std::string const& in)
        334     : ArchGenerator{in}, has_cyclic_dep_{HasCyclicDeps(impl_->arch, impl_->dep_rels)}
        335 {
        336 }
        337 
        338 bool CyclicGenerator::Output(std::ostream& os) const
        339 {
        340     os << "cyclic dependencies " << (has_cyclic_dep_ ? "" : "not ") << "found" << std::endl;
        341 
        342     return !has_cyclic_dep_;
        343 }
        344 }  // namespace Dependency
```

### example/deps/dependency/src/load_store_format.cpp <a id="SS_23_2_15"></a>
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
         11 auto const file_format_dir      = std::string_view{"#dir"};
         12 auto const file_format_deps     = std::string_view{"#deps"};
         13 auto const file_format_arch     = std::string_view{"#arch"};
         14 }  // namespace
         15 
         16 bool StoreToStream(std::ostream& os, FileUtils::Paths_t const& paths)
         17 {
         18     os << file_format_dir << std::endl;
         19 
         20     using FileUtils::operator<<;
         21     os << paths << std::endl;
         22 
         23     return true;
         24 }
         25 
         26 bool StoreToStream(std::ostream& os, FileUtils::Dirs2Srcs_t const& dirs2srcs)
         27 {
         28     os << file_format_dir2srcs << std::endl;
         29 
         30     using FileUtils::operator<<;
         31     os << dirs2srcs << std::endl;
         32 
         33     return true;
         34 }
         35 
         36 namespace {
         37 
         38 bool is_format_dirs2srcs(std::istream& is)
         39 {
         40     auto line = std::string{};
         41 
         42     if (std::getline(is, line)) {
         43         if (line == file_format_dir2srcs) {
         44             return true;
         45         }
         46     }
         47 
         48     return false;
         49 }
         50 
         51 FileUtils::Dirs2Srcs_t load_Dirs2Srcs_t(std::istream& is)
         52 {
         53     static auto const line_sep = std::regex{R"(^\s*$)"};
         54     static auto const line_dir = std::regex{R"(^([\w/.]+)$)"};
         55     static auto const line_src = std::regex{R"(^\s+([\w/.]+)$)"};
         56 
         57     auto line      = std::string{};
         58     auto dir       = FileUtils::Path_t{};
         59     auto srcs      = FileUtils::Paths_t{};
         60     auto dirs2srcs = FileUtils::Dirs2Srcs_t{};
         61 
         62     while (std::getline(is, line)) {
         63         if (auto results = std::smatch{}; std::regex_match(line, results, line_sep)) {
         64             dirs2srcs[dir].swap(srcs);
         65         }
         66         else if (std::regex_match(line, results, line_dir)) {
         67             dir = results[1].str();
         68         }
         69         else if (std::regex_match(line, results, line_src)) {
         70             srcs.push_back(results[1].str());
         71         }
         72         else {
         73             std::cout << line << std::endl;
         74             assert(false);
         75         }
         76     }
         77 
         78     return dirs2srcs;
         79 }
         80 }  // namespace
         81 
         82 std::optional<FileUtils::Dirs2Srcs_t> Load_Dirs2Srcs(std::istream& is)
         83 {
         84     auto dirs2srcs = FileUtils::Dirs2Srcs_t{};
         85 
         86     if (!is) {
         87         return std::nullopt;
         88     }
         89 
         90     if (!is_format_dirs2srcs(is)) {
         91         return std::nullopt;
         92     }
         93 
         94     return load_Dirs2Srcs_t(is);
         95 }
         96 
         97 namespace {
         98 
         99 bool is_format_dirs(std::istream& is)
        100 {
        101     auto line = std::string{};
        102 
        103     if (std::getline(is, line)) {
        104         if (line == file_format_dir) {
        105             return true;
        106         }
        107     }
        108 
        109     return false;
        110 }
        111 }  // namespace
        112 
        113 std::optional<FileUtils::Paths_t> Load_Paths(std::istream& is)
        114 {
        115     auto paths = FileUtils::Paths_t{};
        116 
        117     if (!is_format_dirs(is)) {
        118         return std::nullopt;
        119     }
        120 
        121     auto line = std::string{};
        122     while (std::getline(is, line)) {
        123         paths.emplace_back(FileUtils::Path_t(line));
        124     }
        125 
        126     return paths;
        127 }
        128 
        129 bool StoreToStream(std::ostream& os, DepRels_t const& dep_rels)
        130 {
        131     os << file_format_deps << std::endl;
        132     os << dep_rels << std::endl;
        133 
        134     return true;
        135 }
        136 
        137 namespace {
        138 
        139 bool is_format_deps(std::istream& is)
        140 {
        141     auto line = std::string{};
        142 
        143     if (std::getline(is, line)) {
        144         if (line == file_format_deps) {
        145             return true;
        146         }
        147     }
        148 
        149     return false;
        150 }
        151 
        152 struct dep_half_t {
        153     bool               valid{false};
        154     std::string        from{};
        155     std::string        to{};
        156     uint32_t           count{0};
        157     FileUtils::Paths_t headers{};
        158 };
        159 
        160 FileUtils::Paths_t gen_paths(std::string const& paths_str)
        161 {
        162     auto const sep = std::regex{R"( +)"};
        163     auto       ret = FileUtils::Paths_t{};
        164 
        165     if (paths_str.size() != 0) {
        166         auto end = std::sregex_token_iterator{};
        167         for (auto it = std::sregex_token_iterator{paths_str.begin(), paths_str.end(), sep, -1};
        168              it != end; ++it) {
        169             ret.emplace_back(it->str());
        170         }
        171     }
        172 
        173     return ret;
        174 }
        175 
        176 dep_half_t get_dep_half(std::smatch const& results)
        177 {
        178     auto dep_half = dep_half_t{};
        179 
        180     dep_half.valid   = true;
        181     dep_half.from    = results[1].str();
        182     dep_half.to      = results[2].str();
        183     dep_half.count   = std::stoi(results[3].str());
        184     dep_half.headers = gen_paths(results[4].str());
        185 
        186     return dep_half;
        187 }
        188 
        189 DepRelation gen_dep_rel(dep_half_t&& first, dep_half_t&& second)
        190 {
        191     assert(first.valid);
        192     assert(second.valid);
        193     assert(first.from < second.from);
        194 
        195     return DepRelation{first.from,  first.count,  std::move(first.headers),
        196                        second.from, second.count, std::move(second.headers)};
        197 }
        198 
        199 DepRels_t load_DepRelations_t(std::istream& is)
        200 {
        201     static auto const line_sep = std::regex{R"(^\s*$)"};
        202     static auto const line_dep = std::regex{R"(^([\w/.-]+) -> ([\w/.-]+) : ([\d]+) *(.*)$)"};
        203 
        204     auto line   = std::string{};
        205     auto first  = dep_half_t{};
        206     auto second = dep_half_t{};
        207 
        208     auto dep_rels = DepRels_t{};
        209 
        210     while (std::getline(is, line)) {
        211         if (auto results = std::smatch{}; std::regex_match(line, results, line_sep)) {
        212             dep_rels.emplace_back(gen_dep_rel(std::move(first), std::move(second)));
        213 
        214             first.valid  = false;
        215             second.valid = false;
        216         }
        217         else if (std::regex_match(line, results, line_dep)) {
        218             (!first.valid ? first : second) = get_dep_half(results);
        219         }
        220         else {
        221             assert(false);
        222         }
        223     }
        224 
        225     return dep_rels;
        226 }
        227 }  // namespace
        228 
        229 std::optional<DepRels_t> Load_DepRels(std::istream& is)
        230 {
        231     if (!is) {
        232         return std::nullopt;
        233     }
        234 
        235     if (!is_format_deps(is)) {
        236         return std::nullopt;
        237     }
        238 
        239     return load_DepRelations_t(is);
        240 }
        241 
        242 bool StoreToStream(std::ostream& os, Arch_t const& arch)
        243 {
        244     os << file_format_arch << std::endl;
        245     os << arch << std::endl;
        246 
        247     return true;
        248 }
        249 }  // namespace Dependency
```

### example/deps/dependency/src/load_store_format.h <a id="SS_23_2_16"></a>
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
         12 bool                              StoreToStream(std::ostream& os, FileUtils::Paths_t const& paths);
         13 std::optional<FileUtils::Paths_t> Load_Paths(std::istream& is);
         14 
         15 // Dirs2Srcs_t
         16 bool StoreToStream(std::ostream& os, FileUtils::Dirs2Srcs_t const& dirs2srcs);
         17 std::optional<FileUtils::Dirs2Srcs_t> Load_Dirs2Srcs(std::istream& is);
         18 
         19 // DepRels_t
         20 bool                     StoreToStream(std::ostream& os, DepRels_t const& dep_rels);
         21 std::optional<DepRels_t> Load_DepRels(std::istream& is);
         22 
         23 // Arch_t
         24 bool StoreToStream(std::ostream& os, Arch_t const& arch);
         25 }  // namespace Dependency
```

### example/deps/dependency/ut/arch_pkg_ut.cpp <a id="SS_23_2_17"></a>
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
         42     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
         43     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
         44     {DepRelation{"ut_data/app1/mod2/mod2_1", 1, Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         45                  "ut_data/app1/mod2/mod2_2", 2, Paths_t{"ut_data/app1/mod2/mod2_1/mod2_1_1.h"}}},
         46 };
         47 
         48 DepRels_t const dep_rels_complex{
         49     {DepRelation{"ut_data/app1", 2,
         50                  Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"},
         51                  "ut_data/app1/mod1", 0, Paths_t{}}},
         52     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2", 0, Paths_t{}}},
         53     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
         54     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 1,
         55                  Paths_t{"ut_data/app1/a_1_cpp.h"}}},
         56     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app2", 1,
         57                  Paths_t{"ut_data/app1/a_2_cpp.hpp"}}},
         58     {DepRelation{"ut_data/app1/mod1", 1, Paths_t{"ut_data/app1/mod2/mod2_1.hpp"},
         59                  "ut_data/app1/mod2", 0, Paths_t{}}},
         60     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
         61     {DepRelation{"ut_data/app1/mod1", 1, Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         62                  "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
         63     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app2", 2,
         64                  Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}}},
         65     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
         66     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
         67     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app2", 0, Paths_t{}}},
         68     {DepRelation{"ut_data/app1/mod2/mod2_1", 1, Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         69                  "ut_data/app1/mod2/mod2_2", 2, Paths_t{"ut_data/app1/mod2/mod2_1/mod2_1_1.h"}}},
         70     {DepRelation{"ut_data/app1/mod2/mod2_1", 0, Paths_t{}, "ut_data/app2", 0, Paths_t{}}},
         71     {DepRelation{"ut_data/app1/mod2/mod2_2", 0, Paths_t{}, "ut_data/app2", 0, Paths_t{}}},
         72 };
         73 
         74 TEST(arch_pkg, ArchPkgSimple)
         75 {
         76     auto const arch = ArchPkg::GenArch(dep_rels_simple);
         77 
         78     ASSERT_EQ(2, arch.size());
         79 
         80     auto const& a = *arch.cbegin();
         81     ASSERT_EQ("A", a->Name());
         82     ASSERT_EQ(nullptr, a->Parent());
         83     ASSERT_EQ("B", a->DependOn().front()->Name());
         84     ASSERT_FALSE(a->IsCyclic());
         85     ASSERT_FALSE(a->IsCyclic(*a->DependOn().front()));
         86 
         87     auto const& children = a->Children();
         88     ASSERT_EQ(0, children.size());
         89 
         90     auto const& b = *std::next(arch.cbegin());
         91     ASSERT_EQ("B", b->Name());
         92     ASSERT_EQ(nullptr, b->Parent());
         93 
         94     ASSERT_EQ(0, b->DependOn().size());
         95     ASSERT_FALSE(b->IsCyclic());
         96 }
         97 
         98 TEST(arch_pkg, ArchPkgSimple2)
         99 {
        100     auto const arch = ArchPkg::GenArch(dep_rels_simple2);
        101 
        102     auto exp = std::string{
        103         "package  :X\n"
        104         "fullname :X\n"
        105         "parent   :TOP\n"
        106         "depend_on: {\n"
        107         "    A : STRAIGHT\n"
        108         "    B : STRAIGHT\n"
        109         "    C : STRAIGHT\n"
        110         "}\n"
        111         "children : {\n"
        112         "    package  :A:CYCLIC\n"
        113         "    fullname :X/A\n"
        114         "    parent   :X\n"
        115         "    depend_on: {\n"
        116         "        B : CYCLIC\n"
        117         "        E : CYCLIC\n"
        118         "    }\n"
        119         "    children : { }\n"
        120         "\n"
        121         "    package  :B:CYCLIC\n"
        122         "    fullname :X/B\n"
        123         "    parent   :X\n"
        124         "    depend_on: {\n"
        125         "        C : CYCLIC\n"
        126         "    }\n"
        127         "    children : { }\n"
        128         "\n"
        129         "    package  :C:CYCLIC\n"
        130         "    fullname :X/C\n"
        131         "    parent   :X\n"
        132         "    depend_on: {\n"
        133         "        D : CYCLIC\n"
        134         "    }\n"
        135         "    children : { }\n"
        136         "\n"
        137         "    package  :D:CYCLIC\n"
        138         "    fullname :X/D\n"
        139         "    parent   :X\n"
        140         "    depend_on: {\n"
        141         "        A : CYCLIC\n"
        142         "    }\n"
        143         "    children : { }\n"
        144         "\n"
        145         "    package  :E:CYCLIC\n"
        146         "    fullname :X/E\n"
        147         "    parent   :X\n"
        148         "    depend_on: {\n"
        149         "        A : CYCLIC\n"
        150         "    }\n"
        151         "    children : { }\n"
        152         "}"};
        153 
        154     ASSERT_EQ(exp, ToStringArch(arch));
        155 }
        156 
        157 TEST(arch_pkg, ArchPkgSimple3)
        158 {
        159     auto const arch = ArchPkg::GenArch(dep_rels_simple3);
        160 
        161     auto exp = std::string{
        162         "package  :A:CYCLIC\n"
        163         "fullname :A\n"
        164         "parent   :TOP\n"
        165         "depend_on: {\n"
        166         "    B : STRAIGHT\n"
        167         "    C : CYCLIC\n"
        168         "}\n"
        169         "children : { }\n"
        170         "\n"
        171         "package  :B\n"
        172         "fullname :B\n"
        173         "parent   :TOP\n"
        174         "depend_on: { }\n"
        175         "children : { }\n"
        176         "\n"
        177         "package  :C:CYCLIC\n"
        178         "fullname :C\n"
        179         "parent   :TOP\n"
        180         "depend_on: {\n"
        181         "    B : STRAIGHT\n"
        182         "    D : CYCLIC\n"
        183         "}\n"
        184         "children : { }\n"
        185         "\n"
        186         "package  :D:CYCLIC\n"
        187         "fullname :D\n"
        188         "parent   :TOP\n"
        189         "depend_on: {\n"
        190         "    A : CYCLIC\n"
        191         "}\n"
        192         "children : { }"};
        193 
        194     ASSERT_EQ(exp, ToStringArch(arch));
        195 }
        196 
        197 TEST(arch_pkg, ArchPkg2)
        198 {
        199     auto const arch = ArchPkg::GenArch(dep_rels_middle);
        200 
        201     ASSERT_EQ(1, arch.size());
        202 
        203     Arch_t const* mod2_children(nullptr);
        204     {
        205         auto const& mod2 = *arch.cbegin();
        206 
        207         ASSERT_EQ("mod2", mod2->Name());
        208         ASSERT_EQ(nullptr, mod2->Parent());
        209         ASSERT_EQ(0, mod2->DependOn().size());
        210         ASSERT_FALSE(mod2->IsCyclic());
        211 
        212         mod2_children = &mod2->Children();
        213         ASSERT_EQ(2, mod2_children->size());
        214     }
        215     {
        216         auto const& mod2_1 = *mod2_children->cbegin();
        217         ASSERT_EQ("mod2_1", mod2_1->Name());
        218         ASSERT_EQ("mod2", mod2_1->Parent()->Name());
        219         ASSERT_EQ("mod2_2", mod2_1->DependOn().front()->Name());
        220         ASSERT_TRUE(mod2_1->IsCyclic());
        221         ASSERT_TRUE(mod2_1->IsCyclic(*mod2_1->DependOn().front()));
        222 
        223         auto const& children = mod2_1->Children();
        224         ASSERT_EQ(0, children.size());
        225     }
        226     {
        227         auto const& mod2_2 = *std::next(mod2_children->cbegin());
        228         ASSERT_EQ("mod2_2", mod2_2->Name());
        229         ASSERT_EQ("mod2", mod2_2->Parent()->Name());
        230         ASSERT_EQ("mod2_1", mod2_2->DependOn().front()->Name());
        231         ASSERT_TRUE(mod2_2->IsCyclic());
        232         ASSERT_TRUE(mod2_2->IsCyclic(*mod2_2->DependOn().front()));
        233 
        234         auto const& children = mod2_2->Children();
        235         ASSERT_EQ(0, children.size());
        236     }
        237 }
        238 
        239 TEST(arch_pkg, ArchPkg3)
        240 {
        241     auto const arch = ArchPkg::GenArch(dep_rels_complex);
        242 
        243     /* std::cout << ToStringArch(arch) << std::endl;
        244 
        245         package  :app1:CYCLIC
        246         parent   :TOP
        247         depend_on: {
        248             mod1
        249         }
        250         children : {
        251             package  :mod1:CYCLIC
        252             parent   :app1
        253             depend_on: {
        254                 mod2
        255                 mod2_2
        256             }
        257 
        258             package  :mod2
        259             parent   :app1
        260             children : {
        261                 package  :mod2_1:CYCLIC
        262                 parent   :mod2
        263                 depend_on: {
        264                     mod2_2
        265                 }
        266 
        267                 package  :mod2_2:CYCLIC
        268                 parent   :mod2
        269                 depend_on: {
        270                     app1
        271                     mod2_1
        272                 }
        273             }
        274         }
        275         package  :app2
        276         parent   :TOP
        277         depend_on: {
        278             app1
        279             mod1
        280         }
        281     */
        282 
        283     {
        284         Arch_t const* app1_children(nullptr);
        285         {
        286             auto const& app1 = *arch.cbegin();
        287 
        288             ASSERT_EQ("app1", app1->Name());
        289             ASSERT_EQ(nullptr, app1->Parent());
        290             ASSERT_EQ(1, app1->DependOn().size());
        291             {
        292                 auto const& depend = app1->DependOn();
        293 
        294                 ASSERT_EQ("mod1", (*depend.cbegin())->Name());
        295                 ASSERT_TRUE(app1->IsCyclic(*(*depend.cbegin())));
        296             }
        297 
        298             ASSERT_TRUE(app1->IsCyclic());
        299 
        300             app1_children = &app1->Children();
        301             ASSERT_EQ(2, app1_children->size());
        302         }
        303         {
        304             {
        305                 auto const& mod1 = *app1_children->cbegin();
        306                 ASSERT_EQ("mod1", mod1->Name());
        307                 ASSERT_EQ("app1", mod1->Parent()->Name());
        308                 ASSERT_EQ(2, mod1->DependOn().size());
        309                 {
        310                     auto const& depend = mod1->DependOn();
        311 
        312                     ASSERT_EQ("mod2", (*depend.cbegin())->Name());
        313                     ASSERT_FALSE(mod1->IsCyclic(*(*depend.cbegin())));
        314 
        315                     auto const next = *std::next(depend.cbegin());
        316                     ASSERT_EQ("mod2_2", next->Name());
        317                     ASSERT_TRUE(mod1->IsCyclic(*next));
        318                 }
        319                 ASSERT_TRUE(mod1->IsCyclic());
        320             }
        321             Arch_t const* mod2_children(nullptr);
        322             {
        323                 auto const& mod2 = *std::next(app1_children->cbegin());
        324                 ASSERT_EQ("mod2", mod2->Name());
        325                 ASSERT_EQ("app1", mod2->Parent()->Name());
        326                 ASSERT_EQ(0, mod2->DependOn().size());
        327 
        328                 mod2_children = &mod2->Children();
        329                 ASSERT_EQ(2, mod2_children->size());
        330 
        331                 ASSERT_FALSE(mod2->IsCyclic());
        332             }
        333             {
        334                 {
        335                     auto const& mod2_1 = *mod2_children->cbegin();
        336                     ASSERT_EQ("mod2_1", mod2_1->Name());
        337 
        338                     ASSERT_EQ("mod2", mod2_1->Parent()->Name());
        339                     ASSERT_EQ(1, mod2_1->DependOn().size());
        340                     {
        341                         auto const& depend = mod2_1->DependOn();
        342                         ASSERT_EQ("mod2_2", (*depend.cbegin())->Name());
        343                         ASSERT_TRUE(mod2_1->IsCyclic(*(*depend.cbegin())));
        344                     }
        345 
        346                     ASSERT_TRUE(mod2_1->IsCyclic());
        347                     ASSERT_EQ(0, mod2_1->Children().size());
        348                 }
        349                 {
        350                     auto const& mod2_2 = *std::next(mod2_children->cbegin());
        351                     ASSERT_EQ("mod2_2", mod2_2->Name());
        352 
        353                     ASSERT_EQ("mod2", mod2_2->Parent()->Name());
        354                     ASSERT_EQ(2, mod2_2->DependOn().size());
        355                     {
        356                         auto const& depend = mod2_2->DependOn();
        357                         ASSERT_EQ("app1", (*depend.cbegin())->Name());
        358                         ASSERT_TRUE(mod2_2->IsCyclic(*(*depend.cbegin())));
        359 
        360                         auto const next = *std::next(depend.cbegin());
        361                         ASSERT_EQ("mod2_1", (*std::next(depend.cbegin()))->Name());
        362                         ASSERT_TRUE(mod2_2->IsCyclic(*next));
        363                     }
        364 
        365                     ASSERT_TRUE(mod2_2->IsCyclic());
        366                     ASSERT_EQ(0, mod2_2->Children().size());
        367                 }
        368             }
        369         }
        370     }
        371     {
        372         auto const& app2 = *std::next(arch.cbegin());
        373 
        374         ASSERT_EQ("app2", app2->Name());
        375         ASSERT_EQ(nullptr, app2->Parent());
        376         ASSERT_EQ(2, app2->DependOn().size());
        377         {
        378             auto const& depend = app2->DependOn();
        379 
        380             ASSERT_EQ("app1", (*depend.cbegin())->Name());
        381             ASSERT_EQ("mod1", (*std::next(depend.cbegin()))->Name());
        382         }
        383 
        384         ASSERT_FALSE(app2->IsCyclic());
        385         ASSERT_EQ(0, app2->Children().size());
        386     }
        387 }
        388 
        389 TEST(arch_pkg, ToPlantUML_Rectangle)
        390 {
        391     {
        392         auto const arch = ArchPkg::GenArch(dep_rels_simple);
        393         auto const exp  = std::string{
        394             "rectangle \"A\" as A\n"
        395              "rectangle \"B\" as B"};
        396         ASSERT_EQ(exp, ToPlantUML_Rectangle(arch));
        397     }
        398     {
        399         auto const arch = ArchPkg::GenArch(dep_rels_middle);
        400         auto const exp  = std::string{
        401             "rectangle \"mod2\" as ut_data___app1___mod2 {\n"
        402              "    rectangle \"mod2_1\" as ut_data___app1___mod2___mod2_1\n"
        403              "    rectangle \"mod2_2\" as ut_data___app1___mod2___mod2_2\n"
        404              "}"};
        405         ASSERT_EQ(exp, ToPlantUML_Rectangle(arch));
        406     }
        407     {
        408         auto const arch = ArchPkg::GenArch(dep_rels_complex);
        409         auto const exp  = std::string{
        410             "rectangle \"app1\" as ut_data___app1 {\n"
        411              "    rectangle \"mod1\" as ut_data___app1___mod1\n"
        412              "    rectangle \"mod2\" as ut_data___app1___mod2 {\n"
        413              "        rectangle \"mod2_1\" as ut_data___app1___mod2___mod2_1\n"
        414              "        rectangle \"mod2_2\" as ut_data___app1___mod2___mod2_2\n"
        415              "    }\n"
        416              "}\n"
        417              "rectangle \"app2\" as ut_data___app2"};
        418         ASSERT_EQ(exp, ToPlantUML_Rectangle(arch));
        419     }
        420 }
        421 
        422 TEST(arch_pkg, ToPlantUML_Rectangle2)
        423 {
        424     auto const arch = ArchPkg::GenArch(dep_rels_complex);
        425     auto const exp  = std::string{
        426         "ut_data___app1 \"2\" -[#orange]-> ut_data___app1___mod1\n"
        427          "ut_data___app1___mod2___mod2_2 \"1\" -[#orange]-> ut_data___app1\n"
        428          "ut_data___app2 \"1\" -[#green]-> ut_data___app1\n"
        429          "ut_data___app1___mod1 \"1\" -[#green]-> ut_data___app1___mod2\n"
        430          "ut_data___app1___mod1 \"1\" -[#orange]-> ut_data___app1___mod2___mod2_2\n"
        431          "ut_data___app2 \"2\" -[#green]-> ut_data___app1___mod1\n"
        432          "ut_data___app1___mod2___mod2_1 \"1\" <-[#red]-> \"2\" ut_data___app1___mod2___mod2_2"};
        433 
        434     ASSERT_EQ(exp, ToPlantUML_Rectangle(arch, dep_rels_complex));
        435 }
        436 
        437 TEST(arch_pkg, HasCyclicDeps)
        438 {
        439     {
        440         auto const arch = ArchPkg::GenArch(dep_rels_simple);
        441         ASSERT_FALSE(HasCyclicDeps(arch, dep_rels_simple));
        442     }
        443     {
        444         auto const arch = ArchPkg::GenArch(dep_rels_middle);
        445         ASSERT_TRUE(HasCyclicDeps(arch, dep_rels_middle));
        446     }
        447     {
        448         auto const arch = ArchPkg::GenArch(dep_rels_complex);
        449         ASSERT_TRUE(HasCyclicDeps(arch, dep_rels_complex));
        450     }
        451 }
        452 
        453 TEST(arch_pkg, FindArchPkg)
        454 {
        455     auto const arch = ArchPkg::GenArch(dep_rels_simple);
        456 
        457     {
        458         ArchPkg const* pkg_a = FindArchPkgByName(arch, "A");
        459         ASSERT_NE(nullptr, pkg_a);
        460         ASSERT_EQ("A", pkg_a->Name());
        461     }
        462     {
        463         ArchPkg const* pkg_a_f = FindArchPkgByFullName(arch, "A");
        464         ASSERT_NE(nullptr, pkg_a_f);
        465         ASSERT_EQ("A", pkg_a_f->FullName());
        466     }
        467     {
        468         ArchPkg const* pkg_b = FindArchPkgByName(arch, "B");
        469         ASSERT_NE(nullptr, pkg_b);
        470         ASSERT_EQ("B", pkg_b->Name());
        471     }
        472     {
        473         ArchPkg const* pkg_b_f = FindArchPkgByName(arch, "B");
        474 
        475         ASSERT_NE(nullptr, pkg_b_f);
        476         ASSERT_EQ("B", pkg_b_f->FullName());
        477     }
        478 }
        479 
        480 TEST(arch_pkg, FindArchPkg2)
        481 {
        482     auto const arch = ArchPkg::GenArch(dep_rels_simple2);
        483 
        484     {
        485         ArchPkg const* pkg_x = FindArchPkgByName(arch, "X");
        486         ASSERT_NE(nullptr, pkg_x);
        487         ASSERT_EQ("X", pkg_x->Name());
        488     }
        489     {
        490         ArchPkg const* pkg_x_f = FindArchPkgByFullName(arch, "X");
        491         ASSERT_NE(nullptr, pkg_x_f);
        492         ASSERT_EQ("X", pkg_x_f->FullName());
        493     }
        494     {
        495         ArchPkg const* pkg_a = FindArchPkgByName(arch, "A");
        496         ASSERT_NE(nullptr, pkg_a);
        497         ASSERT_EQ("A", pkg_a->Name());
        498     }
        499     {
        500         ArchPkg const* pkg_a_f = FindArchPkgByFullName(arch, "X/A");
        501         ASSERT_NE(nullptr, pkg_a_f);
        502         ASSERT_EQ("X/A", pkg_a_f->FullName());
        503     }
        504     {
        505         ArchPkg const* pkg_y = FindArchPkgByName(arch, "Y");
        506         ASSERT_EQ(nullptr, pkg_y);
        507     }
        508     {
        509         ArchPkg const* pkg_y_f = FindArchPkgByFullName(arch, "Y");
        510         ASSERT_EQ(nullptr, pkg_y_f);
        511     }
        512 }
        513 
        514 TEST(arch_pkg, FindArchPkg3)
        515 {
        516     auto const arch = ArchPkg::GenArch(dep_rels_complex);
        517 
        518     {
        519         ArchPkg const* pkg_app1 = FindArchPkgByName(arch, "app1");
        520         ASSERT_NE(nullptr, pkg_app1);
        521         ASSERT_EQ("app1", pkg_app1->Name());
        522         ASSERT_EQ("ut_data/app1", pkg_app1->FullName());
        523     }
        524     {
        525         ArchPkg const* pkg_app1_f = FindArchPkgByFullName(arch, "ut_data/app1");
        526         ASSERT_NE(nullptr, pkg_app1_f);
        527         ASSERT_EQ("app1", pkg_app1_f->Name());
        528         ASSERT_EQ("ut_data/app1", pkg_app1_f->FullName());
        529     }
        530     {
        531         ArchPkg const* pkg_mod2_1 = FindArchPkgByName(arch, "mod2_1");
        532         ASSERT_NE(nullptr, pkg_mod2_1);
        533         ASSERT_EQ("mod2_1", pkg_mod2_1->Name());
        534         ASSERT_EQ("ut_data/app1/mod2/mod2_1", pkg_mod2_1->FullName());
        535     }
        536     {
        537         ArchPkg const* pkg_mod2_1_f = FindArchPkgByFullName(arch, "ut_data/app1/mod2/mod2_1");
        538         ASSERT_NE(nullptr, pkg_mod2_1_f);
        539         ASSERT_EQ("mod2_1", pkg_mod2_1_f->Name());
        540         ASSERT_EQ("ut_data/app1/mod2/mod2_1", pkg_mod2_1_f->FullName());
        541     }
        542 }
        543 }  // namespace
        544 }  // namespace Dependency
```

### example/deps/dependency/ut/cpp_deps_ut.cpp <a id="SS_23_2_18"></a>
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
         10 TEST(cpp_deps, GenDepRels)
         11 {
         12     using FileUtils::Paths_t;
         13 
         14     auto const [dirs, srcs] = GetCppDirsSrcs({"ut_data/"});
         15     auto const assign       = FileUtils::AssginSrcsToDirs(dirs, srcs);
         16     auto const srcs_db      = FileUtils::GenFilename2Path(srcs);
         17 
         18     auto cpp_dirs = CppDirs_t{};
         19 
         20     for (auto const& pair : assign) {
         21         cpp_dirs.emplace_back(CppDir{pair.first, GenCppSrc(pair.second, srcs_db)});
         22     }
         23 
         24     auto dep_all = GenDepRels(cpp_dirs);
         25 
         26     auto const app1   = std::string{"ut_data/app1"};
         27     auto const mod1   = std::string{"ut_data/app1/mod1"};
         28     auto const mod2_2 = std::string{"ut_data/app1/mod2/mod2_2"};
         29 
         30     {
         31         auto const app1_mod1 = FindDepRels(dep_all, app1, mod1);
         32         ASSERT_EQ("ut_data/app1", app1_mod1->PackageA);
         33         ASSERT_EQ("ut_data/app1/mod1", app1_mod1->PackageB);
         34 
         35         ASSERT_EQ(6, app1_mod1->CountAtoB);
         36         ASSERT_EQ(1, app1_mod1->CountBtoA);
         37 
         38         auto const app1_mod1_IncsAtoB
         39             = Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"};
         40 
         41         ASSERT_EQ(app1_mod1_IncsAtoB, app1_mod1->IncsAtoB);
         42         ASSERT_EQ(Paths_t{"ut_data/app1/a_1_cpp.h"}, app1_mod1->IncsBtoA);
         43     }
         44     {
         45         auto const app1_mod1 = FindDepRels(dep_all, mod1, app1);
         46         ASSERT_EQ("ut_data/app1", app1_mod1->PackageA);
         47         ASSERT_EQ("ut_data/app1/mod1", app1_mod1->PackageB);
         48 
         49         ASSERT_EQ(6, app1_mod1->CountAtoB);
         50         ASSERT_EQ(1, app1_mod1->CountBtoA);
         51 
         52         auto const app1_mod1_IncsAtoB
         53             = Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"};
         54 
         55         ASSERT_EQ(app1_mod1_IncsAtoB, app1_mod1->IncsAtoB);
         56         ASSERT_EQ(Paths_t{"ut_data/app1/a_1_cpp.h"}, app1_mod1->IncsBtoA);
         57     }
         58     {
         59         auto const mod1_mod2_2 = FindDepRels(dep_all, mod1, mod2_2);
         60         ASSERT_EQ("ut_data/app1/mod1", mod1_mod2_2->PackageA);
         61         ASSERT_EQ("ut_data/app1/mod2/mod2_2", mod1_mod2_2->PackageB);
         62 
         63         ASSERT_EQ(1, mod1_mod2_2->CountAtoB);
         64         ASSERT_EQ(4, mod1_mod2_2->CountBtoA);
         65 
         66         auto const mod1_mod2_2_IncsAtoB = Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"};
         67 
         68         ASSERT_EQ(mod1_mod2_2_IncsAtoB, mod1_mod2_2->IncsAtoB);
         69         ASSERT_EQ((Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}),
         70                   mod1_mod2_2->IncsBtoA);
         71     }
         72     {
         73         auto const app1_mod2_2 = FindDepRels(dep_all, app1, mod2_2);
         74         ASSERT_EQ("ut_data/app1", app1_mod2_2->PackageA);
         75         ASSERT_EQ("ut_data/app1/mod2/mod2_2", app1_mod2_2->PackageB);
         76 
         77         ASSERT_EQ(3, app1_mod2_2->CountAtoB);
         78         ASSERT_EQ(2, app1_mod2_2->CountBtoA);
         79 
         80         ASSERT_EQ(Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"}, app1_mod2_2->IncsAtoB);
         81 
         82         auto const app1_mod2_2_IncsAtoB = Paths_t{"ut_data/app1/a_1_cpp.h"};
         83         ASSERT_EQ(app1_mod2_2_IncsAtoB, app1_mod2_2->IncsBtoA);
         84     }
         85 }
         86 }  // namespace
         87 }  // namespace Dependency
```

### example/deps/dependency/ut/cpp_dir_ut.cpp <a id="SS_23_2_19"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "cpp_dir.h"
          4 #include "cpp_src.h"
          5 
          6 namespace Dependency {
          7 namespace {
          8 
          9 TEST(cpp_dir, GenCppDirs)
         10 {
         11     using FileUtils::Paths_t;
         12 
         13     auto const [dirs, srcs] = GetCppDirsSrcs({"ut_data/app1", "ut_data/app2///"});
         14     auto const db           = FileUtils::GenFilename2Path(srcs);
         15     auto const cpp_dirs     = CppDirs_t{GenCppDirs(srcs, db)};
         16 
         17     auto a_1_cpp = std::find_if(cpp_dirs.begin(), cpp_dirs.end(),
         18                                 [](CppDir const& pkg) { return pkg.Path() == "a_1_cpp.cpp"; });
         19     ASSERT_NE(a_1_cpp, cpp_dirs.end());
         20 
         21     auto a_1_cpp_h = std::find_if(cpp_dirs.begin(), cpp_dirs.end(),
         22                                   [](CppDir const& pkg) { return pkg.Path() == "a_1_cpp.h"; });
         23     ASSERT_NE(a_1_cpp_h, cpp_dirs.end());
         24 
         25     auto mod2_2_1_h = std::find_if(cpp_dirs.begin(), cpp_dirs.end(),
         26                                    [](CppDir const& pkg) { return pkg.Path() == "mod2_2_1.h"; });
         27     ASSERT_NE(mod2_2_1_h, cpp_dirs.end());
         28 
         29     auto ret_a_1_cpp = std::pair<uint32_t, Paths_t>{a_1_cpp->DependsOn(*a_1_cpp_h)};
         30     ASSERT_EQ(0, ret_a_1_cpp.first);
         31 
         32     auto ret_mod2_2_1_h = std::pair<uint32_t, Paths_t>{mod2_2_1_h->DependsOn(*a_1_cpp_h)};
         33     ASSERT_EQ(1, ret_mod2_2_1_h.first);
         34 }
         35 
         36 TEST(cpp_dir, CppDir)
         37 {
         38     using FileUtils::Paths_t;
         39 
         40     auto const [dirs, srcs]  = GetCppDirsSrcs({"ut_data/app1", "ut_data/app2///"});
         41     auto const packagae_srcs = FileUtils::AssginSrcsToDirs(dirs, srcs);
         42     auto const db            = FileUtils::GenFilename2Path(srcs);
         43 
         44     auto mod1 = CppDir{"ut_data/app1/mod1", GenCppSrc(packagae_srcs.at("ut_data/app1/mod1"), db)};
         45     auto app2 = CppDir{"ut_data/app2", GenCppSrc(packagae_srcs.at("ut_data/app2"), db)};
         46 
         47     ASSERT_TRUE(mod1.Contains("ut_data/app1/mod1/mod1_1.cpp"));
         48     ASSERT_TRUE(mod1.Contains("ut_data/app1/mod1/mod1_1.hpp"));
         49     ASSERT_TRUE(mod1.Contains("ut_data/app1/mod1/mod1_2.hpp"));
         50     ASSERT_FALSE(mod1.Contains("ut_data/app1/mod2/mod2_1.cpp"));
         51 
         52     auto ret_mod1 = std::pair<uint32_t, Paths_t>{mod1.DependsOn(app2)};
         53     ASSERT_EQ(0, ret_mod1.first);
         54     ASSERT_EQ(0, ret_mod1.second.size());
         55 
         56     auto ret_app2 = std::pair<uint32_t, Paths_t>{app2.DependsOn(mod1)};
         57     ASSERT_EQ(4, ret_app2.first);
         58     ASSERT_EQ((Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}),
         59               ret_app2.second);
         60 }
         61 
         62 TEST(cpp_dir, operator_eq_tl)
         63 {
         64     auto const [dirs, srcs]  = GetCppDirsSrcs({"ut_data/app1", "ut_data/app2///"});
         65     auto const packagae_srcs = FileUtils::AssginSrcsToDirs(dirs, srcs);
         66     auto const db            = FileUtils::GenFilename2Path(srcs);
         67 
         68     auto mod1_0 = CppDir{"ut_data/app1/mod1", GenCppSrc(packagae_srcs.at("ut_data/app1/mod1"), db)};
         69     auto mod1_1 = CppDir{"ut_data/app1/mod1", GenCppSrc(packagae_srcs.at("ut_data/app1/mod1"), db)};
         70     auto app2   = CppDir{"ut_data/app2", GenCppSrc(packagae_srcs.at("ut_data/app2"), db)};
         71 
         72     ASSERT_EQ(mod1_0, mod1_0);
         73     ASSERT_EQ(mod1_0, mod1_1);
         74     ASSERT_EQ(mod1_1, mod1_0);
         75 
         76     ASSERT_NE(mod1_0, app2);
         77     ASSERT_LT(mod1_0, app2);
         78     ASSERT_GT(app2, mod1_0);
         79 }
         80 }  // namespace
         81 }  // namespace Dependency
```

### example/deps/dependency/ut/cpp_src_ut.cpp <a id="SS_23_2_20"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "cpp_src.h"
          4 
          5 namespace Dependency {
          6 namespace {
          7 
          8 TEST(cpp_src, CppSrc)
          9 {
         10     using FileUtils::Paths_t;
         11 
         12     auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
         13     auto const db                   = FileUtils::GenFilename2Path(act_srcs);
         14     auto const cpp_src              = CppSrc{"ut_data/app1/a_1_c.c", db};
         15 
         16     auto const exp_incs = Paths_t{"ut_data/app1/a_1_c.h",
         17                                   "ut_data/app1/a_1_cpp.h",
         18                                   "ut_data/app1/mod1/mod1_1.hpp",
         19                                   "ut_data/app1/mod1/mod1_2.hpp",
         20                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
         21                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.h"};
         22     ASSERT_EQ(cpp_src.GetIncs(), exp_incs);
         23 
         24     auto const exp_not_found = Paths_t{"stdio.h", "string.h"};
         25     ASSERT_EQ(cpp_src.GetIncsNotFound(), exp_not_found);
         26 
         27     auto const cpp_src2 = CppSrc{"ut_data/app1/a_1_cpp.h", db};
         28 
         29     auto const exp_incs2 = Paths_t{
         30         "ut_data/app1/a_1_cpp.h", "ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp",
         31         "ut_data/app1/mod2/mod2_1/mod2_1_1.h", "ut_data/app1/mod2/mod2_2/mod2_2_1.h"};
         32     ASSERT_EQ(cpp_src2.GetIncs(), exp_incs2);
         33 
         34     ASSERT_EQ(cpp_src2.GetIncsNotFound(), Paths_t{});
         35 
         36     auto const cpp_src3 = CppSrc{"ut_data/app1/mod1/mod1_2.hpp", db};
         37 
         38     ASSERT_EQ(cpp_src3.GetIncs(), Paths_t{});
         39 
         40     ASSERT_EQ(cpp_src3.GetIncsNotFound(), Paths_t{});
         41 }
         42 
         43 TEST(cpp_src, GenCppSrc)
         44 {
         45     using FileUtils::Paths_t;
         46 
         47     auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
         48     auto const db                   = FileUtils::GenFilename2Path(act_srcs);
         49     auto const srcs
         50         = Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.cpp"};
         51     auto const cpp_srcs_act = GenCppSrc(srcs, db);
         52 
         53     ASSERT_EQ(cpp_srcs_act.size(), 3);
         54 
         55     Paths_t const exp_incs[]{
         56         {"ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.h", "ut_data/app1/mod1/mod1_1.hpp",
         57          "ut_data/app1/mod1/mod1_2.hpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
         58          "ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         59         {"ut_data/app1/a_1_cpp.h", "ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp",
         60          "ut_data/app1/mod2/mod2_1/mod2_1_1.h", "ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         61         {},
         62     };
         63     Paths_t const exp_not_found[]{
         64         {"stdio.h", "string.h"},
         65         {"stdio.h", "string.h"},
         66         {},
         67     };
         68 
         69     auto it_exp_srcs      = srcs.cbegin();
         70     auto it_exp_incs      = std::cbegin(exp_incs);
         71     auto it_exp_not_found = std::cbegin(exp_not_found);
         72 
         73     for (auto it_act = cpp_srcs_act.cbegin(); it_act != cpp_srcs_act.cend(); ++it_act) {
         74         ASSERT_EQ(*it_exp_srcs, it_act->Path());
         75         ASSERT_EQ(*it_exp_incs, it_act->GetIncs());
         76         ASSERT_EQ(*it_exp_not_found, it_act->GetIncsNotFound());
         77 
         78         ++it_exp_srcs;
         79         ++it_exp_incs;
         80         ++it_exp_not_found;
         81     }
         82 
         83     ASSERT_EQ(it_exp_srcs, srcs.cend());
         84     ASSERT_EQ(it_exp_incs, std::cend(exp_incs));
         85     ASSERT_EQ(it_exp_not_found, std::cend(exp_not_found));
         86 }
         87 
         88 TEST(cpp_src, operator_equal)
         89 {
         90     using FileUtils::Paths_t;
         91 
         92     auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
         93     auto const db                   = FileUtils::GenFilename2Path(act_srcs);
         94 
         95     auto const cpp_src_0 = CppSrc{"ut_data/app1/a_1_c.c", db};
         96     auto const cpp_src_1 = CppSrc{"ut_data/app1/a_1_c.c", db};
         97     auto const cpp_src_2 = CppSrc{"ut_data/app1/a_1_c.h", db};
         98 
         99     ASSERT_EQ(cpp_src_0, cpp_src_0);
        100     ASSERT_EQ(cpp_src_0, cpp_src_1);
        101     ASSERT_EQ(cpp_src_1, cpp_src_0);
        102     ASSERT_NE(cpp_src_0, cpp_src_2);
        103 }
        104 
        105 TEST(cpp_src, operator_lt)
        106 {
        107     using FileUtils::Paths_t;
        108 
        109     auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
        110     auto const db                   = FileUtils::GenFilename2Path(act_srcs);
        111 
        112     auto const cpp_src_0 = CppSrc{"ut_data/app1/a_1_c.c", db};
        113     auto const cpp_src_1 = CppSrc{"ut_data/app1/a_1_c.h", db};
        114 
        115     ASSERT_LT(cpp_src_0, cpp_src_1);
        116     ASSERT_GT(cpp_src_1, cpp_src_0);
        117 }
        118 
        119 TEST(cpp_src, ToString)
        120 {
        121     using FileUtils::Paths_t;
        122 
        123     auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"ut_data/app1"});
        124     auto const db                   = FileUtils::GenFilename2Path(act_srcs);
        125     auto const cpp_src              = CppSrc{"ut_data/app1/a_1_c.c", db};
        126 
        127     auto const exp = std::string_view{
        128         "file              : a_1_c.c\n"
        129         "path              : ut_data/app1/a_1_c.c\n"
        130         "include           : ut_data/app1/a_1_c.h ut_data/app1/a_1_cpp.h "
        131         "ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp "
        132         "ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        133         "include not found : stdio.h string.h\n"};
        134 
        135     ASSERT_EQ(ToStringCppSrc(cpp_src), exp);
        136 }
        137 
        138 TEST(cpp_src, GetCppDirsSrcs)
        139 {
        140     using FileUtils::Paths_t;
        141 
        142     {
        143         auto const exp_dirs = Paths_t{"ut_data/app1",
        144                                       "ut_data/app1/mod1",
        145                                       "ut_data/app1/mod2",
        146                                       "ut_data/app1/mod2/mod2_1",
        147                                       "ut_data/app1/mod2/mod2_2",
        148                                       "ut_data/app2"};
        149 
        150         auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        151                                       "ut_data/app1/a_1_c.h",
        152                                       "ut_data/app1/a_1_cpp.cpp",
        153                                       "ut_data/app1/a_1_cpp.h",
        154                                       "ut_data/app1/a_2_c.C",
        155                                       "ut_data/app1/a_2_c.H",
        156                                       "ut_data/app1/a_2_cpp.cxx",
        157                                       "ut_data/app1/a_2_cpp.hpp",
        158                                       "ut_data/app1/a_3_cpp.cc",
        159                                       "ut_data/app1/mod1/mod1_1.cpp",
        160                                       "ut_data/app1/mod1/mod1_1.hpp",
        161                                       "ut_data/app1/mod1/mod1_2.hpp",
        162                                       "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        163                                       "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        164                                       "ut_data/app1/mod2/mod2_1.cpp",
        165                                       "ut_data/app1/mod2/mod2_1.hpp",
        166                                       "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        167                                       "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        168                                       "ut_data/app2/b_1.cpp",
        169                                       "ut_data/app2/b_1.h"};
        170 
        171         auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"./ut_data/app1", "ut_data/app2///"});
        172 
        173         ASSERT_EQ(act_dirs, exp_dirs);
        174         ASSERT_EQ(act_srcs, exp_srcs);
        175     }
        176     {
        177         auto const exp_dirs = Paths_t{"ut_data",
        178                                       "ut_data/app1",
        179                                       "ut_data/app1/mod1",
        180                                       "ut_data/app1/mod2",
        181                                       "ut_data/app1/mod2/mod2_1",
        182                                       "ut_data/app1/mod2/mod2_2",
        183                                       "ut_data/app2"};
        184 
        185         auto const exp_srcs             = Paths_t{"ut_data/app1/a_1_c.c",
        186                                       "ut_data/app1/a_1_c.h",
        187                                       "ut_data/app1/a_1_cpp.cpp",
        188                                       "ut_data/app1/a_1_cpp.h",
        189                                       "ut_data/app1/a_2_c.C",
        190                                       "ut_data/app1/a_2_c.H",
        191                                       "ut_data/app1/a_2_cpp.cxx",
        192                                       "ut_data/app1/a_2_cpp.hpp",
        193                                       "ut_data/app1/a_3_cpp.cc",
        194                                       "ut_data/app1/mod1/mod1_1.cpp",
        195                                       "ut_data/app1/mod1/mod1_1.hpp",
        196                                       "ut_data/app1/mod1/mod1_2.hpp",
        197                                       "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        198                                       "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        199                                       "ut_data/app1/mod2/mod2_1.cpp",
        200                                       "ut_data/app1/mod2/mod2_1.hpp",
        201                                       "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        202                                       "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        203                                       "ut_data/app2/b_1.cpp",
        204                                       "ut_data/app2/b_1.h"};
        205         auto const [act_dirs, act_srcs] = GetCppDirsSrcs({"././ut_data"});
        206 
        207         ASSERT_EQ(act_dirs, exp_dirs);
        208         ASSERT_EQ(act_srcs, exp_srcs);
        209     }
        210 }
        211 }  // namespace
        212 }  // namespace Dependency
```

### example/deps/dependency/ut/deps_scenario_ut.cpp <a id="SS_23_2_21"></a>
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
         12 TEST(deps_scenario, PkgGenerator)
         13 {
         14     using FileUtils::Paths_t;
         15 
         16     {
         17         auto pg  = PkgGenerator{"ut_data/load_store/pkg_org", true, Paths_t{"ut_data/app3/"}, ""};
         18         auto exp = std::string{
         19             "#dir\n"
         20             "ut_data/app1\n"
         21             "ut_data/app1/mod1\n"
         22             "ut_data/app1/mod2\n"
         23             "ut_data/app1/mod2/mod2_1\n"
         24             "ut_data/app1/mod2/mod2_2\n"
         25             "ut_data/app2\n"};
         26 
         27         auto ss = std::ostringstream{};
         28 
         29         pg.Output(ss);
         30         ASSERT_EQ(exp, ss.str());
         31     }
         32     {
         33         auto pg  = PkgGenerator{"ut_data/load_store/pkg_org", false, Paths_t{}, ""};
         34         auto exp = std::string{
         35             "#dir\n"
         36             "ut_data/app1\n"
         37             "ut_data/app1/mod1\n"
         38             "ut_data/app1/mod2/mod2_1\n"
         39             "ut_data/app2\n"};
         40 
         41         auto ss = std::ostringstream{};
         42 
         43         pg.Output(ss);
         44         ASSERT_EQ(exp, ss.str());
         45     }
         46 }
         47 
         48 TEST(deps_scenario, PkgGenerator2)
         49 {
         50     using FileUtils::Paths_t;
         51 
         52     {
         53         auto pg  = PkgGenerator{"", false, Paths_t{"ut_data/app1", "ut_data/app2"}, ""};
         54         auto exp = std::string{
         55             "#dir\n"
         56             "ut_data/app1\n"
         57             "ut_data/app2\n"};
         58 
         59         auto ss = std::ostringstream{};
         60 
         61         pg.Output(ss);
         62         ASSERT_EQ(exp, ss.str());
         63     }
         64     {
         65         auto pg  = PkgGenerator{"", false, Paths_t{"ut_data/app1", "ut_data/app2"}, "hehe"};
         66         auto exp = std::string{
         67             "#dir\n"
         68             "ut_data/app1\n"
         69             "ut_data/app2\n"};
         70 
         71         auto ss = std::ostringstream{};
         72 
         73         pg.Output(ss);
         74         ASSERT_EQ(exp, ss.str());
         75     }
         76     {
         77         auto pg  = PkgGenerator{"", false, Paths_t{"ut_data/app1", "ut_data/app2"}, ".*/app2"};
         78         auto exp = std::string{
         79             "#dir\n"
         80             "ut_data/app1\n"};
         81 
         82         auto ss = std::ostringstream{};
         83 
         84         pg.Output(ss);
         85         ASSERT_EQ(exp, ss.str());
         86     }
         87     {
         88         auto pg  = PkgGenerator{"", true, Paths_t{"ut_data/app1", "ut_data/app2"}, ""};
         89         auto exp = std::string{
         90             "#dir\n"
         91             "ut_data/app1\n"
         92             "ut_data/app1/mod1\n"
         93             "ut_data/app1/mod2\n"
         94             "ut_data/app1/mod2/mod2_1\n"
         95             "ut_data/app1/mod2/mod2_2\n"
         96             "ut_data/app2\n"};
         97 
         98         auto ss = std::ostringstream{};
         99 
        100         pg.Output(ss);
        101         ASSERT_EQ(exp, ss.str());
        102     }
        103     {
        104         auto pg  = PkgGenerator{"", true, Paths_t{"ut_data/app1", "ut_data/app2"}, ".*/mod2/.*"};
        105         auto exp = std::string{
        106             "#dir\n"
        107             "ut_data/app1\n"
        108             "ut_data/app1/mod1\n"
        109             "ut_data/app1/mod2\n"
        110             "ut_data/app2\n"};
        111 
        112         auto ss = std::ostringstream{};
        113 
        114         pg.Output(ss);
        115         ASSERT_EQ(exp, ss.str());
        116     }
        117 
        118     auto exception_occured = false;
        119     try {
        120         auto pg = PkgGenerator{"", true, Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app2"}, ""};
        121     }
        122     catch (std::runtime_error const& e) {
        123         exception_occured = true;
        124         ASSERT_STREQ("ut_data/app1/a_1_c.c not directory", e.what());
        125     }
        126     ASSERT_TRUE(exception_occured);
        127 }
        128 
        129 TEST(deps_scenario, SrcsGenerator)
        130 {
        131     using FileUtils::Paths_t;
        132 
        133     {
        134         auto sg = SrcsGenerator{
        135             "", true, Paths_t{"ut_data/app1/mod2/mod2_1", "ut_data/app1/mod2/mod2_2"}, ""};
        136 
        137         // clang-format off
        138         auto exp = std::string {
        139             "---\n"
        140             "mod2_1_1.cpp\n"
        141             "file              : mod2_1_1.cpp\n"
        142             "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        143             "include           : \n"
        144             "include not found : \n"
        145             "\n"
        146             "---\n"
        147             "mod2_1_1.h\n"
        148             "file              : mod2_1_1.h\n"
        149             "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        150             "include           : ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        151             "include not found : a_1_cpp.h\n"
        152             "\n"
        153             "---\n"
        154             "mod2_2_1.cpp\n"
        155             "file              : mod2_2_1.cpp\n"
        156             "path              : ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        157             "include           : ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        158             "include not found : a_1_cpp.h\n"
        159             "\n"
        160             "---\n"
        161             "mod2_2_1.h\n"
        162             "file              : mod2_2_1.h\n"
        163             "path              : ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        164             "include           : ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        165             "include not found : a_1_cpp.h\n"
        166             "\n"};
        167         // clang-format on
        168 
        169         auto ss = std::ostringstream{};
        170 
        171         sg.Output(ss);
        172         ASSERT_EQ(exp, ss.str());
        173     }
        174     {
        175         auto sg = SrcsGenerator{
        176             "", true, Paths_t{"ut_data/app1/mod2/mod2_1", "ut_data/app1/mod2/mod2_2"}, ".*/mod2_2"};
        177 
        178         auto exp = std::string{
        179             "---\n"
        180             "mod2_1_1.cpp\n"
        181             "file              : mod2_1_1.cpp\n"
        182             "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        183             "include           : \n"
        184             "include not found : \n"
        185             "\n"
        186             "---\n"
        187             "mod2_1_1.h\n"
        188             "file              : mod2_1_1.h\n"
        189             "path              : ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        190             "include           : \n"
        191             "include not found : mod2_2_1.h\n"
        192             "\n"};
        193 
        194         auto ss = std::ostringstream{};
        195 
        196         sg.Output(ss);
        197         ASSERT_EQ(exp, ss.str());
        198     }
        199 }
        200 
        201 TEST(deps_scenario, Pkg2SrcsGenerator)
        202 {
        203     using FileUtils::Paths_t;
        204 
        205     auto exception_occured = false;
        206 
        207     try {
        208         auto p2sg
        209             = Pkg2SrcsGenerator{"ut_data/app1/a_1_c.c", false, false, Paths_t{"ut_data/app3/"}, ""};
        210     }
        211     catch (std::runtime_error const& e) {
        212         exception_occured = true;
        213         ASSERT_STREQ("ut_data/app1/a_1_c.c is illegal", e.what());
        214     }
        215     ASSERT_TRUE(exception_occured);
        216 
        217     {
        218         auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", true, false,
        219                                       Paths_t{"ut_data/app3/"}, ""};
        220 
        221         auto exp = std::string{
        222             "#dir2srcs\n"
        223             "ut_data/app1\n"
        224             "    ut_data/app1/a_1_c.c\n"
        225             "    ut_data/app1/a_1_c.h\n"
        226             "    ut_data/app1/a_1_cpp.cpp\n"
        227             "    ut_data/app1/a_1_cpp.h\n"
        228             "    ut_data/app1/a_2_c.C\n"
        229             "    ut_data/app1/a_2_c.H\n"
        230             "    ut_data/app1/a_2_cpp.cxx\n"
        231             "    ut_data/app1/a_2_cpp.hpp\n"
        232             "    ut_data/app1/a_3_cpp.cc\n"
        233             "\n"
        234             "ut_data/app1/mod1\n"
        235             "    ut_data/app1/mod1/mod1_1.cpp\n"
        236             "    ut_data/app1/mod1/mod1_1.hpp\n"
        237             "    ut_data/app1/mod1/mod1_2.hpp\n"
        238             "\n"
        239             "ut_data/app1/mod2\n"
        240             "    ut_data/app1/mod2/mod2_1.cpp\n"
        241             "    ut_data/app1/mod2/mod2_1.hpp\n"
        242             "\n"
        243             "ut_data/app1/mod2/mod2_1\n"
        244             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        245             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        246             "\n"
        247             "ut_data/app1/mod2/mod2_2\n"
        248             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        249             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        250             "\n"
        251             "ut_data/app2\n"
        252             "    ut_data/app2/b_1.cpp\n"
        253             "    ut_data/app2/b_1.h\n"
        254             "\n"};
        255 
        256         auto ss = std::ostringstream{};
        257 
        258         p2sg.Output(ss);
        259         ASSERT_EQ(exp, ss.str());
        260     }
        261     {
        262         auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", true, false,
        263                                       Paths_t{"ut_data/app3/"}, ".*/mod2\\b.*"};
        264 
        265         auto exp = std::string{
        266             "#dir2srcs\n"
        267             "ut_data/app1\n"
        268             "    ut_data/app1/a_1_c.c\n"
        269             "    ut_data/app1/a_1_c.h\n"
        270             "    ut_data/app1/a_1_cpp.cpp\n"
        271             "    ut_data/app1/a_1_cpp.h\n"
        272             "    ut_data/app1/a_2_c.C\n"
        273             "    ut_data/app1/a_2_c.H\n"
        274             "    ut_data/app1/a_2_cpp.cxx\n"
        275             "    ut_data/app1/a_2_cpp.hpp\n"
        276             "    ut_data/app1/a_3_cpp.cc\n"
        277             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        278             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        279             "    ut_data/app1/mod2/mod2_1.cpp\n"
        280             "    ut_data/app1/mod2/mod2_1.hpp\n"
        281             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        282             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        283             "\n"
        284             "ut_data/app1/mod1\n"
        285             "    ut_data/app1/mod1/mod1_1.cpp\n"
        286             "    ut_data/app1/mod1/mod1_1.hpp\n"
        287             "    ut_data/app1/mod1/mod1_2.hpp\n"
        288             "\n"
        289             "ut_data/app2\n"
        290             "    ut_data/app2/b_1.cpp\n"
        291             "    ut_data/app2/b_1.h\n"
        292             "\n"};
        293 
        294         auto ss = std::ostringstream{};
        295 
        296         p2sg.Output(ss);
        297         ASSERT_EQ(exp, ss.str());
        298     }
        299     {
        300         auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", false, false,
        301                                       Paths_t{"ut_data/app3/"}, ""};
        302 
        303         auto exp = std::string{
        304             "#dir2srcs\n"
        305             "ut_data/app1\n"
        306             "    ut_data/app1/a_1_c.c\n"
        307             "    ut_data/app1/a_1_c.h\n"
        308             "    ut_data/app1/a_1_cpp.cpp\n"
        309             "    ut_data/app1/a_1_cpp.h\n"
        310             "    ut_data/app1/a_2_c.C\n"
        311             "    ut_data/app1/a_2_c.H\n"
        312             "    ut_data/app1/a_2_cpp.cxx\n"
        313             "    ut_data/app1/a_2_cpp.hpp\n"
        314             "    ut_data/app1/a_3_cpp.cc\n"
        315             "    ut_data/app1/mod2/mod2_1.cpp\n"
        316             "    ut_data/app1/mod2/mod2_1.hpp\n"
        317             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        318             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        319             "\n"
        320             "ut_data/app1/mod1\n"
        321             "    ut_data/app1/mod1/mod1_1.cpp\n"
        322             "    ut_data/app1/mod1/mod1_1.hpp\n"
        323             "    ut_data/app1/mod1/mod1_2.hpp\n"
        324             "\n"
        325             "ut_data/app1/mod2\n"
        326             "\n"
        327             "\n"
        328             "ut_data/app1/mod2/mod2_1\n"
        329             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        330             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        331             "\n"
        332             "ut_data/app2\n"
        333             "    ut_data/app2/b_1.cpp\n"
        334             "    ut_data/app2/b_1.h\n"
        335             "\n"};
        336 
        337         auto ss = std::ostringstream{};
        338 
        339         p2sg.Output(ss);
        340         ASSERT_EQ(exp, ss.str());
        341     }
        342     {
        343         auto p2sg = Pkg2SrcsGenerator{"ut_data/load_store/pkg_org", false, false,
        344                                       Paths_t{"ut_data/app3/"}, "ut_data/app2"};
        345 
        346         auto exp = std::string{
        347             "#dir2srcs\n"
        348             "no_package\n"
        349             "    ut_data/app2/b_1.cpp\n"
        350             "    ut_data/app2/b_1.h\n"
        351             "\n"
        352             "ut_data/app1\n"
        353             "    ut_data/app1/a_1_c.c\n"
        354             "    ut_data/app1/a_1_c.h\n"
        355             "    ut_data/app1/a_1_cpp.cpp\n"
        356             "    ut_data/app1/a_1_cpp.h\n"
        357             "    ut_data/app1/a_2_c.C\n"
        358             "    ut_data/app1/a_2_c.H\n"
        359             "    ut_data/app1/a_2_cpp.cxx\n"
        360             "    ut_data/app1/a_2_cpp.hpp\n"
        361             "    ut_data/app1/a_3_cpp.cc\n"
        362             "    ut_data/app1/mod2/mod2_1.cpp\n"
        363             "    ut_data/app1/mod2/mod2_1.hpp\n"
        364             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        365             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        366             "\n"
        367             "ut_data/app1/mod1\n"
        368             "    ut_data/app1/mod1/mod1_1.cpp\n"
        369             "    ut_data/app1/mod1/mod1_1.hpp\n"
        370             "    ut_data/app1/mod1/mod1_2.hpp\n"
        371             "\n"
        372             "ut_data/app1/mod2\n"
        373             "\n"
        374             "\n"
        375             "ut_data/app1/mod2/mod2_1\n"
        376             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        377             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        378             "\n"};
        379 
        380         auto ss = std::ostringstream{};
        381 
        382         p2sg.Output(ss);
        383         ASSERT_EQ(exp, ss.str());
        384     }
        385 }
        386 
        387 TEST(deps_scenario, Pkg2SrcsGenerator2)
        388 {
        389     using FileUtils::Paths_t;
        390 
        391     {
        392         auto dirs2srcs_org_str = std::string{
        393             "#dir2srcs\n"
        394             "ut_data\n"
        395             "    ut_data/app1/a_1_c.c\n"
        396             "    ut_data/app1/a_1_c.h\n"
        397             "    ut_data/app1/a_1_cpp.cpp\n"
        398             "    ut_data/app1/a_1_cpp.h\n"
        399             "    ut_data/app1/a_2_c.C\n"
        400             "    ut_data/app1/a_2_c.H\n"
        401             "    ut_data/app1/a_2_cpp.cxx\n"
        402             "    ut_data/app1/a_2_cpp.hpp\n"
        403             "    ut_data/app1/a_3_cpp.cc\n"
        404             "    ut_data/app1/mod1/mod1_1.cpp\n"
        405             "    ut_data/app1/mod1/mod1_1.hpp\n"
        406             "    ut_data/app1/mod1/mod1_2.hpp\n"
        407             "\n"
        408             "ut_data/app1/mod2\n"
        409             "    ut_data/app1/mod2/mod2_1.cpp\n"
        410             "    ut_data/app1/mod2/mod2_1.hpp\n"
        411             "\n"
        412             "ut_data/app1/mod2/mod2_1\n"
        413             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        414             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        415             "\n"
        416             "ut_data/app1/mod2/mod2_2\n"
        417             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        418             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        419             "\n"
        420             "ut_data/app2\n"
        421             "    ut_data/app2/b_1.cpp\n"
        422             "    ut_data/app2/b_1.h\n"
        423             "\n"};
        424 
        425         auto p2sg
        426             = Pkg2SrcsGenerator{"ut_data/load_store/dirs2srcs_org", true, false, Paths_t{}, ""};
        427 
        428         auto ss = std::ostringstream{};
        429 
        430         p2sg.Output(ss);
        431         ASSERT_EQ(dirs2srcs_org_str, ss.str());
        432     }
        433     {
        434         auto dirs2srcs_org_str = std::string{
        435             "#dir2srcs\n"
        436             "ut_data\n"
        437             "    ut_data/app1/a_1_c.c\n"
        438             "    ut_data/app1/a_1_c.h\n"
        439             "    ut_data/app1/a_1_cpp.cpp\n"
        440             "    ut_data/app1/a_1_cpp.h\n"
        441             "    ut_data/app1/a_2_c.C\n"
        442             "    ut_data/app1/a_2_c.H\n"
        443             "    ut_data/app1/a_2_cpp.cxx\n"
        444             "    ut_data/app1/a_2_cpp.hpp\n"
        445             "    ut_data/app1/a_3_cpp.cc\n"
        446             "    ut_data/app1/mod1/mod1_1.cpp\n"
        447             "    ut_data/app1/mod1/mod1_1.hpp\n"
        448             "    ut_data/app1/mod1/mod1_2.hpp\n"
        449             "\n"
        450             "ut_data/app1\n"
        451             "\n"
        452             "\n"
        453             "ut_data/app1/mod2\n"
        454             "    ut_data/app1/mod2/mod2_1.cpp\n"
        455             "    ut_data/app1/mod2/mod2_1.hpp\n"
        456             "\n"
        457             "ut_data/app1/mod2/mod2_1\n"
        458             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        459             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        460             "\n"
        461             "ut_data/app1/mod2/mod2_2\n"
        462             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        463             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        464             "\n"
        465             "ut_data/app2\n"
        466             "    ut_data/app2/b_1.cpp\n"
        467             "    ut_data/app2/b_1.h\n"
        468             "\n"};
        469 
        470         auto const dirs = Paths_t{"ut_data", "ut_data/app1/mod2", "ut_data/app1/mod2/mod2_1",
        471                                   "ut_data/app1/mod2/mod2_2", "ut_data/app2"};
        472 
        473         auto p2sg = Pkg2SrcsGenerator{"", false, false, dirs, ""};
        474 
        475         auto ss = std::ostringstream{};
        476 
        477         p2sg.Output(ss);
        478         ASSERT_EQ(dirs2srcs_org_str, ss.str());
        479     }
        480     {
        481         auto p2sg = Pkg2SrcsGenerator{"", true, false, Paths_t{"ut_data"}, ""};
        482 
        483         auto const exp = std::string{
        484             "#dir2srcs\n"
        485             "ut_data/app1\n"
        486             "    ut_data/app1/a_1_c.c\n"
        487             "    ut_data/app1/a_1_c.h\n"
        488             "    ut_data/app1/a_1_cpp.cpp\n"
        489             "    ut_data/app1/a_1_cpp.h\n"
        490             "    ut_data/app1/a_2_c.C\n"
        491             "    ut_data/app1/a_2_c.H\n"
        492             "    ut_data/app1/a_2_cpp.cxx\n"
        493             "    ut_data/app1/a_2_cpp.hpp\n"
        494             "    ut_data/app1/a_3_cpp.cc\n"
        495             "\n"
        496             "ut_data/app1/mod1\n"
        497             "    ut_data/app1/mod1/mod1_1.cpp\n"
        498             "    ut_data/app1/mod1/mod1_1.hpp\n"
        499             "    ut_data/app1/mod1/mod1_2.hpp\n"
        500             "\n"
        501             "ut_data/app1/mod2\n"
        502             "    ut_data/app1/mod2/mod2_1.cpp\n"
        503             "    ut_data/app1/mod2/mod2_1.hpp\n"
        504             "\n"
        505             "ut_data/app1/mod2/mod2_1\n"
        506             "    ut_data/app1/mod2/mod2_1/mod2_1_1.cpp\n"
        507             "    ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        508             "\n"
        509             "ut_data/app1/mod2/mod2_2\n"
        510             "    ut_data/app1/mod2/mod2_2/mod2_2_1.cpp\n"
        511             "    ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        512             "\n"
        513             "ut_data/app2\n"
        514             "    ut_data/app2/b_1.cpp\n"
        515             "    ut_data/app2/b_1.h\n"
        516             "\n"};
        517 
        518         auto ss = std::ostringstream{};
        519 
        520         p2sg.Output(ss);
        521         ASSERT_EQ(exp, ss.str());
        522     }
        523 }
        524 
        525 TEST(deps_scenario, Pkg2PkgGenerator)
        526 {
        527     using FileUtils::Paths_t;
        528 
        529     auto exception_occured = false;
        530     try {
        531         auto p2pg
        532             = Pkg2PkgGenerator{"ut_data/app1/a_1_c.c", false, false, Paths_t{"ut_data/app3/"}, ""};
        533     }
        534     catch (std::runtime_error const& e) {
        535         exception_occured = true;
        536         ASSERT_STREQ("ut_data/app1/a_1_c.c is illegal", e.what());
        537     }
        538     ASSERT_TRUE(exception_occured);
        539 
        540     {
        541         auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", true, false,
        542                                      Paths_t{"ut_data/app3/"}, ""};
        543 
        544         // clang-format off
        545         auto exp = std::string {
        546             "#deps\n"
        547             "ut_data/app1 -> ut_data/app1/mod1 : 6 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        548             "ut_data/app1/mod1 -> ut_data/app1 : 1 ut_data/app1/a_1_cpp.h\n"
        549             "\n"
        550             "ut_data/app1 -> ut_data/app1/mod2 : 0 \n"
        551             "ut_data/app1/mod2 -> ut_data/app1 : 0 \n"
        552             "\n"
        553             "ut_data/app1 -> ut_data/app1/mod2/mod2_1 : 3 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        554             "ut_data/app1/mod2/mod2_1 -> ut_data/app1 : 1 ut_data/app1/a_1_cpp.h\n"
        555             "\n"
        556             "ut_data/app1 -> ut_data/app1/mod2/mod2_2 : 3 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        557             "ut_data/app1/mod2/mod2_2 -> ut_data/app1 : 2 ut_data/app1/a_1_cpp.h\n"
        558             "\n"
        559             "ut_data/app1 -> ut_data/app2 : 0 \n"
        560             "ut_data/app2 -> ut_data/app1 : 3 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp\n"
        561             "\n"
        562             "ut_data/app1/mod1 -> ut_data/app1/mod2 : 1 ut_data/app1/mod2/mod2_1.hpp\n"
        563             "ut_data/app1/mod2 -> ut_data/app1/mod1 : 0 \n"
        564             "\n"
        565             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_1 : 1 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        566             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        567             "\n"
        568             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_2 : 1 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        569             "ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        570             "\n"
        571             "ut_data/app1/mod1 -> ut_data/app2 : 0 \n"
        572             "ut_data/app2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        573             "\n"
        574             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_1 : 0 \n"
        575             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2 : 0 \n"
        576             "\n"
        577             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_2 : 0 \n"
        578             "ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod2 : 0 \n"
        579             "\n"
        580             "ut_data/app1/mod2 -> ut_data/app2 : 0 \n"
        581             "ut_data/app2 -> ut_data/app1/mod2 : 0 \n"
        582             "\n"
        583             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2/mod2_2 : 1 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        584             "ut_data/app1/mod2/mod2_2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        585             "\n"
        586             "ut_data/app1/mod2/mod2_1 -> ut_data/app2 : 0 \n"
        587             "ut_data/app2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        588             "\n"
        589             "ut_data/app1/mod2/mod2_2 -> ut_data/app2 : 0 \n"
        590             "ut_data/app2 -> ut_data/app1/mod2/mod2_2 : 2 ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        591             "\n"};
        592         // clang-format on
        593 
        594         auto ss = std::ostringstream{};
        595 
        596         p2pg.Output(ss);
        597         ASSERT_EQ(exp, ss.str());
        598     }
        599     {
        600         auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", true, false,
        601                                      Paths_t{"ut_data/app3/"}, ".*/mod2\\b.*"};
        602 
        603         // clang-format off
        604         auto exp = std::string {
        605             "#deps\n"
        606             "ut_data/app1 -> ut_data/app1/mod1 : 12 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        607             "ut_data/app1/mod1 -> ut_data/app1 : 4 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_1.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        608             "\n"
        609             "ut_data/app1 -> ut_data/app2 : 0 \n"
        610             "ut_data/app2 -> ut_data/app1 : 7 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp ut_data/app1/mod2/mod2_1/mod2_1_1.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        611             "\n"
        612             "ut_data/app1/mod1 -> ut_data/app2 : 0 \n"
        613             "ut_data/app2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        614             "\n"};
        615         // clang-format on
        616 
        617         auto ss = std::ostringstream{};
        618 
        619         p2pg.Output(ss);
        620         ASSERT_EQ(exp, ss.str());
        621     }
        622     {
        623         auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", false, false,
        624                                      Paths_t{"ut_data/app3/"}, ""};
        625 
        626         // clang-format off
        627         auto exp = std::string {
        628             "#deps\n"
        629             "ut_data/app1 -> ut_data/app1/mod1 : 10 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        630             "ut_data/app1/mod1 -> ut_data/app1 : 3 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_1.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        631             "\n"
        632             "ut_data/app1 -> ut_data/app1/mod2 : 0 \n"
        633             "ut_data/app1/mod2 -> ut_data/app1 : 0 \n"
        634             "\n"
        635             "ut_data/app1 -> ut_data/app1/mod2/mod2_1 : 5 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        636             "ut_data/app1/mod2/mod2_1 -> ut_data/app1 : 2 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        637             "\n"
        638             "ut_data/app1 -> ut_data/app2 : 0 \n"
        639             "ut_data/app2 -> ut_data/app1 : 5 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        640             "\n"
        641             "ut_data/app1/mod1 -> ut_data/app1/mod2 : 0 \n"
        642             "ut_data/app1/mod2 -> ut_data/app1/mod1 : 0 \n"
        643             "\n"
        644             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_1 : 1 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        645             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        646             "\n"
        647             "ut_data/app1/mod1 -> ut_data/app2 : 0 \n"
        648             "ut_data/app2 -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        649             "\n"
        650             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_1 : 0 \n"
        651             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2 : 0 \n"
        652             "\n"
        653             "ut_data/app1/mod2 -> ut_data/app2 : 0 \n"
        654             "ut_data/app2 -> ut_data/app1/mod2 : 0 \n"
        655             "\n"
        656             "ut_data/app1/mod2/mod2_1 -> ut_data/app2 : 0 \n"
        657             "ut_data/app2 -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        658             "\n"};
        659         // clang-format on
        660 
        661         auto ss = std::ostringstream{};
        662 
        663         p2pg.Output(ss);
        664         ASSERT_EQ(exp, ss.str());
        665     }
        666     {
        667         auto p2pg = Pkg2PkgGenerator{"ut_data/load_store/pkg_org", false, false,
        668                                      Paths_t{"ut_data/app3/"}, "ut_data/app2"};
        669 
        670         // clang-format off
        671         auto exp = std::string {
        672             "#deps\n"
        673             "no_package -> ut_data/app1 : 5 ut_data/app1/a_1_cpp.h ut_data/app1/a_2_cpp.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        674             "ut_data/app1 -> no_package : 0 \n"
        675             "\n"
        676             "no_package -> ut_data/app1/mod1 : 4 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        677             "ut_data/app1/mod1 -> no_package : 0 \n"
        678             "\n"
        679             "no_package -> ut_data/app1/mod2 : 0 \n"
        680             "ut_data/app1/mod2 -> no_package : 0 \n"
        681             "\n"
        682             "no_package -> ut_data/app1/mod2/mod2_1 : 2 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        683             "ut_data/app1/mod2/mod2_1 -> no_package : 0 \n"
        684             "\n"
        685             "ut_data/app1 -> ut_data/app1/mod1 : 10 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        686             "ut_data/app1/mod1 -> ut_data/app1 : 3 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_1.hpp ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        687             "\n"
        688             "ut_data/app1 -> ut_data/app1/mod2 : 0 \n"
        689             "ut_data/app1/mod2 -> ut_data/app1 : 0 \n"
        690             "\n"
        691             "ut_data/app1 -> ut_data/app1/mod2/mod2_1 : 5 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        692             "ut_data/app1/mod2/mod2_1 -> ut_data/app1 : 2 ut_data/app1/a_1_cpp.h ut_data/app1/mod2/mod2_2/mod2_2_1.h\n"
        693             "\n"
        694             "ut_data/app1/mod1 -> ut_data/app1/mod2 : 0 \n"
        695             "ut_data/app1/mod2 -> ut_data/app1/mod1 : 0 \n"
        696             "\n"
        697             "ut_data/app1/mod1 -> ut_data/app1/mod2/mod2_1 : 1 ut_data/app1/mod2/mod2_1/mod2_1_1.h\n"
        698             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod1 : 2 ut_data/app1/mod1/mod1_1.hpp ut_data/app1/mod1/mod1_2.hpp\n"
        699             "\n"
        700             "ut_data/app1/mod2 -> ut_data/app1/mod2/mod2_1 : 0 \n"
        701             "ut_data/app1/mod2/mod2_1 -> ut_data/app1/mod2 : 0 \n"
        702             "\n"};
        703         // clang-format on
        704 
        705         auto ss = std::ostringstream{};
        706 
        707         p2pg.Output(ss);
        708         ASSERT_EQ(exp, ss.str());
        709     }
        710 }
        711 
        712 TEST(deps_scenario, ArchGenerator)
        713 {
        714     using FileUtils::Paths_t;
        715 
        716     auto exception_occured = false;
        717     try {
        718         auto ag = ArchGenerator{"ut_data/load_store/arch_org"};
        719     }
        720     catch (std::runtime_error const& e) {
        721         exception_occured = true;
        722         ASSERT_STREQ("IN-file load error", e.what());
        723     }
        724     ASSERT_TRUE(exception_occured);
        725 
        726     {
        727         auto ag = ArchGenerator{"ut_data/load_store/deps_org"};
        728         auto ss = std::stringstream{};
        729 
        730         ag.Output(ss);
        731 
        732         auto act = std::optional<std::vector<std::string>>{FileUtils::Load_Strings(ss)};
        733 
        734         auto exp = std::optional<std::vector<std::string>>{
        735             FileUtils::LoadFromFile("ut_data/load_store/arch_org", FileUtils::Load_Strings)};
        736 
        737         ASSERT_TRUE(exp);
        738 
        739         ASSERT_EQ(*act, *exp);
        740     }
        741 }
        742 
        743 TEST(deps_scenario, Arch2PUmlGenerator)
        744 {
        745     auto exception_occured = false;
        746     try {
        747         auto ag = Arch2PUmlGenerator{"ut_data/load_store/arch_org"};
        748     }
        749     catch (std::runtime_error const& e) {
        750         exception_occured = true;
        751         ASSERT_STREQ("IN-file load error", e.what());
        752     }
        753     ASSERT_TRUE(exception_occured);
        754 
        755     {
        756         auto ag = Arch2PUmlGenerator{"ut_data/load_store/deps_org"};
        757         auto ss = std::stringstream{};
        758 
        759         ag.Output(ss);
        760 
        761         auto exp = std::string{
        762             "@startuml\n"
        763             "scale max 730 width\n"
        764             "rectangle \"app1\" as ut_data___app1 {\n"
        765             "    rectangle \"mod1\" as ut_data___app1___mod1\n"
        766             "    rectangle \"mod2\" as ut_data___app1___mod2 {\n"
        767             "        rectangle \"mod2_1\" as ut_data___app1___mod2___mod2_1\n"
        768             "        rectangle \"mod2_2\" as ut_data___app1___mod2___mod2_2\n"
        769             "    }\n"
        770             "}\n"
        771             "rectangle \"app2\" as ut_data___app2\n"
        772             "\n"
        773             "ut_data___app1 \"2\" -[#orange]-> ut_data___app1___mod1\n"
        774             "ut_data___app1___mod2___mod2_2 \"1\" -[#orange]-> ut_data___app1\n"
        775             "ut_data___app2 \"1\" -[#green]-> ut_data___app1\n"
        776             "ut_data___app1___mod1 \"1\" -[#green]-> ut_data___app1___mod2\n"
        777             "ut_data___app1___mod1 \"1\" -[#orange]-> ut_data___app1___mod2___mod2_2\n"
        778             "ut_data___app2 \"2\" -[#green]-> ut_data___app1___mod1\n"
        779             "ut_data___app1___mod2___mod2_1 \"1\" <-[#red]-> \"2\" ut_data___app1___mod2___mod2_2\n"
        780             "\n"
        781             "@enduml\n"};
        782 
        783         ASSERT_EQ(exp, ss.str());
        784     }
        785 }
        786 
        787 TEST(deps_scenario, CyclicGenerator)
        788 {
        789     auto exception_occured = false;
        790     try {
        791         auto cg = CyclicGenerator{"ut_data/load_store/arch_org"};
        792     }
        793     catch (std::runtime_error const& e) {
        794         exception_occured = true;
        795         ASSERT_STREQ("IN-file load error", e.what());
        796     }
        797     ASSERT_TRUE(exception_occured);
        798 
        799     {
        800         auto cg = CyclicGenerator{"ut_data/load_store/deps_org"};
        801         auto ss = std::stringstream{};
        802 
        803         ASSERT_FALSE(cg.Output(ss));
        804 
        805         ASSERT_EQ("cyclic dependencies found\n", ss.str());
        806     }
        807     {
        808         auto cg = CyclicGenerator{"ut_data/load_store/deps_org2"};
        809         auto ss = std::stringstream{};
        810 
        811         ASSERT_TRUE(cg.Output(ss));
        812 
        813         ASSERT_EQ("cyclic dependencies not found\n", ss.str());
        814     }
        815 }
        816 }  // namespace
        817 }  // namespace Dependency
```

### example/deps/dependency/ut/load_store_format_ut.cpp <a id="SS_23_2_22"></a>
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
         10 TEST(load_store_format, Paths_t)
         11 {
         12     using FileUtils::Paths_t;
         13 
         14     auto const pkg_org = std::string{"ut_data/load_store/pkg_org"};
         15     auto const pkg_act = std::string{"ut_data/load_store/pkg_act"};
         16 
         17     FileUtils::RemoveFile(pkg_act);
         18 
         19     auto const dir_in
         20         = Paths_t{"ut_data/app1", "ut_data/app1/mod1", "ut_data/app1/mod2/mod2_1", "ut_data/app2"};
         21 
         22     // ディレクトリなのでエラーなはず
         23     ASSERT_FALSE(FileUtils::StoreToFile("ut_data/app1", dir_in, StoreToStream));
         24 
         25     ASSERT_TRUE(FileUtils::StoreToFile(pkg_act, dir_in, StoreToStream));
         26 
         27     auto dir_out0 = std::optional<Paths_t>{FileUtils::LoadFromFile(pkg_org, Load_Paths)};
         28     ASSERT_TRUE(dir_out0);
         29 
         30     auto dir_out1 = std::optional<Paths_t>{FileUtils::LoadFromFile(pkg_act, Load_Paths)};
         31     ASSERT_TRUE(dir_out1);
         32 
         33     ASSERT_EQ(dir_in, *dir_out0);
         34     ASSERT_EQ(dir_in, *dir_out1);
         35 
         36     FileUtils::RemoveFile(pkg_act);
         37 }
         38 
         39 TEST(load_store_format, Dirs2Srcs_t)
         40 {
         41     auto const dirs2srcs_org = std::string{"ut_data/load_store/dirs2srcs_org"};
         42     auto const dirs2srcs_act = std::string{"ut_data/load_store/dirs2srcs_act"};
         43 
         44     FileUtils::RemoveFile(dirs2srcs_act);
         45 
         46     const auto dir2srcs_in = FileUtils::Dirs2Srcs_t{
         47         {"ut_data",
         48          {"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.cpp",
         49           "ut_data/app1/a_1_cpp.h", "ut_data/app1/a_2_c.C", "ut_data/app1/a_2_c.H",
         50           "ut_data/app1/a_2_cpp.cxx", "ut_data/app1/a_2_cpp.hpp", "ut_data/app1/a_3_cpp.cc",
         51           "ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp",
         52           "ut_data/app1/mod1/mod1_2.hpp"}},
         53         {"ut_data/app1/mod2", {"ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
         54         {"ut_data/app1/mod2/mod2_1",
         55          {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
         56         {"ut_data/app1/mod2/mod2_2",
         57          {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp", "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
         58         {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
         59     };
         60 
         61     // ディレクトリなのでエラーなはず
         62     ASSERT_FALSE(FileUtils::StoreToFile("ut_data/app1", dir2srcs_in, StoreToStream));
         63 
         64     ASSERT_TRUE(FileUtils::StoreToFile(dirs2srcs_act, dir2srcs_in, StoreToStream));
         65 
         66     auto dir2srcs_out0 = std::optional<FileUtils::Dirs2Srcs_t>{
         67         FileUtils::LoadFromFile(dirs2srcs_org, Load_Dirs2Srcs)};
         68     ASSERT_TRUE(dir2srcs_out0);
         69 
         70     auto dir2srcs_out1 = std::optional<FileUtils::Dirs2Srcs_t>{
         71         FileUtils::LoadFromFile(dirs2srcs_act, Load_Dirs2Srcs)};
         72     ASSERT_TRUE(dir2srcs_out1);
         73 
         74     ASSERT_EQ(dir2srcs_in, *dir2srcs_out0);
         75     ASSERT_EQ(dir2srcs_in, *dir2srcs_out1);
         76 
         77     FileUtils::RemoveFile(dirs2srcs_act);
         78 }
         79 
         80 namespace {
         81 using FileUtils::Paths_t;
         82 
         83 DepRels_t const dep_rels{
         84     {DepRelation{"ut_data/app1", 2,
         85                  Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"},
         86                  "ut_data/app1/mod1", 0, Paths_t{}}},
         87     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2", 0, Paths_t{}}},
         88     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
         89     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 1,
         90                  Paths_t{"ut_data/app1/a_1_cpp.h"}}},
         91     {DepRelation{"ut_data/app1", 0, Paths_t{}, "ut_data/app2", 1,
         92                  Paths_t{"ut_data/app1/a_2_cpp.hpp"}}},
         93     {DepRelation{"ut_data/app1/mod1", 1, Paths_t{"ut_data/app1/mod2/mod2_1.hpp"},
         94                  "ut_data/app1/mod2", 0, Paths_t{}}},
         95     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
         96     {DepRelation{"ut_data/app1/mod1", 1, Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
         97                  "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
         98     {DepRelation{"ut_data/app1/mod1", 0, Paths_t{}, "ut_data/app2", 2,
         99                  Paths_t{"ut_data/app1/mod1/mod1_1.hpp", "ut_data/app1/mod1/mod1_2.hpp"}}},
        100     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_1", 0, Paths_t{}}},
        101     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app1/mod2/mod2_2", 0, Paths_t{}}},
        102     {DepRelation{"ut_data/app1/mod2", 0, Paths_t{}, "ut_data/app2", 0, Paths_t{}}},
        103     {DepRelation{"ut_data/app1/mod2/mod2_1", 1, Paths_t{"ut_data/app1/mod2/mod2_2/mod2_2_1.h"},
        104                  "ut_data/app1/mod2/mod2_2", 2, Paths_t{"ut_data/app1/mod2/mod2_1/mod2_1_1.h"}}},
        105     {DepRelation{"ut_data/app1/mod2/mod2_1", 0, Paths_t{}, "ut_data/app2", 0, Paths_t{}}},
        106     {DepRelation{"ut_data/app1/mod2/mod2_2", 0, Paths_t{}, "ut_data/app2", 0, Paths_t{}}},
        107 };
        108 }  // namespace
        109 
        110 TEST(load_store_format, DepRels_t)
        111 {
        112     auto const deps_org = std::string{"ut_data/load_store/deps_org"};
        113     auto const deps_act = std::string{"ut_data/load_store/deps_act"};
        114 
        115     FileUtils::RemoveFile(deps_act);
        116 
        117     // ディレクトリなのでエラーなはず
        118     ASSERT_FALSE(FileUtils::StoreToFile("ut_data/app1", dep_rels, StoreToStream));
        119 
        120     ASSERT_TRUE(FileUtils::StoreToFile(deps_act, dep_rels, StoreToStream));
        121 
        122     auto deps_out0 = std::optional<DepRels_t>{FileUtils::LoadFromFile(deps_org, Load_DepRels)};
        123     ASSERT_TRUE(deps_out0);
        124 
        125     auto exp_it     = dep_rels.cbegin();
        126     auto exp_it_end = dep_rels.cend();
        127     auto act_it     = deps_out0->cbegin();
        128 
        129     while (exp_it != exp_it_end) {
        130         auto exp_str = ToStringDepRel(*exp_it);
        131         auto act_str = ToStringDepRel(*act_it);
        132         ASSERT_EQ(exp_str, act_str);
        133         ASSERT_EQ(exp_it->PackageA, act_it->PackageA);
        134         ASSERT_EQ(exp_it->CountAtoB, act_it->CountAtoB);
        135         ASSERT_EQ(exp_it->IncsAtoB, act_it->IncsAtoB);
        136         ASSERT_EQ(exp_it->PackageB, act_it->PackageB);
        137         ASSERT_EQ(exp_it->CountBtoA, act_it->CountBtoA);
        138         ASSERT_EQ(exp_it->IncsBtoA, act_it->IncsBtoA);
        139         ASSERT_EQ(*exp_it, *act_it);
        140 
        141         ++exp_it;
        142         ++act_it;
        143     }
        144     ASSERT_EQ(dep_rels, *deps_out0);
        145 
        146     auto deps_out1 = std::optional<DepRels_t>{FileUtils::LoadFromFile(deps_act, Load_DepRels)};
        147     ASSERT_TRUE(deps_out1);
        148 
        149     ASSERT_EQ(dep_rels, *deps_out1);
        150 
        151     FileUtils::RemoveFile(deps_act);
        152 }
        153 
        154 TEST(load_store_format, Arch_t)
        155 {
        156     auto const arch_exp = std::string{"ut_data/load_store/arch_org"};
        157     auto const arch_act = std::string{"ut_data/load_store/arch_act"};
        158 
        159     FileUtils::RemoveFile(arch_act);
        160 
        161     auto row_exp = std::optional<std::vector<std::string>>{
        162         FileUtils::LoadFromFile(arch_exp, FileUtils::Load_Strings)};
        163     ASSERT_TRUE(row_exp);
        164 
        165     auto const arch = ArchPkg::GenArch(dep_rels);
        166     ASSERT_TRUE(FileUtils::StoreToFile(arch_act, arch, StoreToStream));
        167 
        168     auto row_act = std::optional<std::vector<std::string>>{
        169         FileUtils::LoadFromFile(arch_act, FileUtils::Load_Strings)};
        170     ASSERT_TRUE(row_act);
        171 
        172     ASSERT_EQ(row_exp, *row_act);
        173 
        174     FileUtils::RemoveFile(arch_act);
        175 }
        176 }  // namespace
        177 }  // namespace Dependency
```

### example/deps/file_utils/h/file_utils/load_store.h <a id="SS_23_2_23"></a>
```cpp
          1 #pragma once
          2 #include <fstream>
          3 #include <optional>
          4 #include <string>
          5 
          6 namespace FileUtils {
          7 
          8 template <typename T>
          9 bool StoreToFile(std::string_view filename, T const& t, bool (*ss)(std::ostream& os, T const&))
         10 {
         11     auto fout = std::ofstream{filename.data()};
         12 
         13     if (!fout) {
         14         return false;
         15     }
         16 
         17     return (*ss)(fout, t);
         18 }
         19 
         20 template <typename T>
         21 std::optional<T> LoadFromFile(std::string_view filename, std::optional<T> (*ls)(std::istream& os))
         22 {
         23     auto fin = std::ifstream{filename.data()};
         24 
         25     if (!fin) {
         26         return std::nullopt;
         27     }
         28 
         29     return (*ls)(fin);
         30 }
         31 }  // namespace FileUtils
```

### example/deps/file_utils/h/file_utils/load_store_row.h <a id="SS_23_2_24"></a>
```cpp
          1 #pragma once
          2 #include <fstream>
          3 #include <optional>
          4 #include <utility>
          5 #include <vector>
          6 
          7 namespace FileUtils {
          8 
          9 bool StoreToStream(std::ostream& os, std::vector<std::string> const& lines);
         10 std::optional<std::vector<std::string>> Load_Strings(std::istream& is);
         11 }  // namespace FileUtils
```

### example/deps/file_utils/h/file_utils/path_utils.h <a id="SS_23_2_25"></a>
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
         11 std::string ToStringPath(Path_t const& paths);
         12 
         13 using Paths_t = std::list<std::filesystem::path>;
         14 
         15 Paths_t              NotDirs(Paths_t const& dirs);
         16 std::string          ToStringPaths(Paths_t const& paths, std::string_view sep = "\n",
         17                                    std::string_view indent = "");
         18 inline std::ostream& operator<<(std::ostream& os, Paths_t const& paths)
         19 {
         20     return os << ToStringPaths(paths);
         21 }
         22 
         23 // first path:  filename
         24 // second path: pathname
         25 using Filename2Path_t = std::map<Path_t, Path_t>;
         26 Filename2Path_t GenFilename2Path(Paths_t const& paths);
         27 
         28 // first  : package name(directory name)
         29 // second : srcs assigned to package
         30 using Dirs2Srcs_t = std::map<Path_t, Paths_t>;
         31 
         32 Dirs2Srcs_t          AssginSrcsToDirs(Paths_t const& dirs, Paths_t const& srcs);
         33 std::string          ToStringDirs2Srcs(Dirs2Srcs_t const& dirs2srcs);
         34 inline std::ostream& operator<<(std::ostream& os, Dirs2Srcs_t const& dirs2srcs)
         35 {
         36     return os << ToStringDirs2Srcs(dirs2srcs);
         37 }
         38 
         39 Path_t NormalizeLexically(Path_t const& path);
         40 
         41 void RemoveFile(Path_t const& filename);
         42 }  // namespace FileUtils
```

### example/deps/file_utils/src/load_store_row.cpp <a id="SS_23_2_26"></a>
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
         11 bool StoreToStream(std::ostream& os, std::vector<std::string> const& lines)
         12 {
         13     for (auto const& line : lines) {
         14         os << line;
         15     }
         16 
         17     return true;
         18 }
         19 
         20 std::optional<std::vector<std::string>> Load_Strings(std::istream& is)
         21 {
         22     auto content = std::vector<std::string>{};
         23     auto line    = std::string{};
         24 
         25     while (std::getline(is, line)) {
         26         auto ss = std::ostringstream{};
         27 
         28         ss << line << std::endl;
         29         content.emplace_back(ss.str());
         30     }
         31 
         32     return content;
         33 }
         34 }  // namespace FileUtils
```

### example/deps/file_utils/src/path_utils.cpp <a id="SS_23_2_27"></a>
```cpp
          1 #include <algorithm>
          2 #include <sstream>
          3 
          4 #include "file_utils/path_utils.h"
          5 
          6 namespace FileUtils {
          7 
          8 std::string ToStringPath(Path_t const& path)
          9 {
         10     auto pn = path.string();
         11 
         12     if (pn.size() == 0) {
         13         pn = "\"\"";
         14     }
         15 
         16     return pn;
         17 }
         18 
         19 std::string ToStringPaths(Paths_t const& paths, std::string_view sep, std::string_view indent)
         20 {
         21     auto ss    = std::ostringstream{};
         22     auto first = true;
         23 
         24     for (auto const& p : paths) {
         25         if (!std::exchange(first, false)) {
         26             ss << sep;
         27         }
         28 
         29         ss << indent << ToStringPath(p);
         30     }
         31 
         32     return ss.str();
         33 }
         34 
         35 std::string ToStringDirs2Srcs(Dirs2Srcs_t const& dirs2srcs)
         36 {
         37     auto ss    = std::ostringstream{};
         38     auto first = bool{true};
         39 
         40     for (auto const& pair : dirs2srcs) {
         41         if (first) {
         42             first = false;
         43         }
         44         else {
         45             ss << std::endl;
         46         }
         47 
         48         ss << ToStringPath(pair.first) << std::endl;
         49         ss << ToStringPaths(pair.second, "\n", "    ") << std::endl;
         50     }
         51 
         52     return ss.str();
         53 }
         54 
         55 Paths_t NotDirs(Paths_t const& dirs)
         56 {
         57     auto ret = Paths_t{};
         58 
         59     std::copy_if(dirs.cbegin(), dirs.cend(), std::back_inserter(ret),
         60                  [](auto const& dir) noexcept { return !std::filesystem::is_directory(dir); });
         61 
         62     return ret;
         63 }
         64 
         65 Filename2Path_t GenFilename2Path(Paths_t const& paths)
         66 {
         67     auto ret = Filename2Path_t{};
         68 
         69     for (auto const& p : paths) {
         70         ret[p.filename()] = p;
         71     }
         72 
         73     return ret;
         74 }
         75 
         76 namespace {
         77 Path_t const current_dir{"."};
         78 
         79 size_t match_count(Path_t const& dir, Path_t const& src)
         80 {
         81     auto const dir_str = dir.string();
         82     auto const src_str = dir == current_dir ? "./" + src.string() : src.string();
         83 
         84     if (dir_str.size() >= src_str.size()) {
         85         return 0;
         86     }
         87 
         88     auto count     = 0U;
         89     auto count_max = dir_str.size();
         90 
         91     for (; count < count_max; ++count) {
         92         if (dir_str[count] != src_str[count]) {
         93             break;
         94         }
         95     }
         96 
         97     if (count == count_max && src_str[count] == '/') {
         98         return count;
         99     }
        100 
        101     return 0;
        102 }
        103 
        104 Path_t select_package(Path_t const& src, Paths_t const& dirs)
        105 {
        106     Path_t const* best_match{nullptr};
        107     auto          count_max = 0U;
        108 
        109     for (auto const& dir : dirs) {
        110         auto count = match_count(dir, src);
        111         if (count_max < count) {
        112             best_match = &dir;
        113             count_max  = count;
        114         }
        115     }
        116 
        117     if (best_match == nullptr) {
        118         return Path_t("no_package");
        119     }
        120     else {
        121         return *best_match;
        122     }
        123 }
        124 
        125 Paths_t gen_parent_dirs(Path_t const dir)
        126 {
        127     auto ret = Paths_t{};
        128 
        129     for (auto p = dir.parent_path(), pp = p.parent_path(); !p.empty() && p != pp;
        130          p = pp, pp = p.parent_path()) {
        131         ret.push_front(p);
        132     }
        133 
        134     return ret;
        135 }
        136 
        137 // a/
        138 //   a0.c
        139 //   b/
        140 //     c/
        141 //       d/
        142 //         d.c
        143 // のようなファイ構造があった場合、
        144 // d2sには a、a/b/c/d が登録され、a/b、a/b/cは登録されていない。
        145 // a/b、a/b/cを埋めるのがpad_parent_dirsである。
        146 void pad_parent_dirs(Paths_t const& dirs, Dirs2Srcs_t& d2s)
        147 {
        148     for (auto const& dir : dirs) {
        149         auto parent_found = false;
        150 
        151         for (auto const& p : gen_parent_dirs(dir)) {
        152             if (!parent_found && d2s.count(p) != 0) {
        153                 parent_found = true;
        154             }
        155             else if (parent_found && d2s.count(p) == 0) {
        156                 d2s[p] = Paths_t();
        157             }
        158         }
        159     }
        160 }
        161 }  // namespace
        162 
        163 Dirs2Srcs_t AssginSrcsToDirs(Paths_t const& dirs, Paths_t const& srcs)
        164 {
        165     auto ret      = Dirs2Srcs_t{};
        166     auto add_dirs = Paths_t{};
        167 
        168     for (auto const& src : srcs) {
        169         auto dir = select_package(src, dirs);
        170 
        171         if (ret.count(dir) == 0) {
        172             ret[dir] = Paths_t();
        173             add_dirs.push_back(dir);
        174         }
        175         ret[dir].push_back(src);
        176     }
        177 
        178     pad_parent_dirs(add_dirs, ret);
        179 
        180     return ret;
        181 }
        182 
        183 Path_t NormalizeLexically(Path_t const& path)
        184 {
        185     // lexically_normalは"a/../b"を"b"にする
        186     // 最後の'/'を削除
        187     auto path_lex = Path_t(path.string() + '/').lexically_normal().string();
        188     path_lex.pop_back();
        189 
        190     if (path_lex.size() == 0) {
        191         return Path_t(".");
        192     }
        193     return path_lex;
        194 }
        195 
        196 void RemoveFile(Path_t const& filename)
        197 {
        198     if (std::filesystem::exists(filename)) {
        199         std::filesystem::remove(filename);
        200     }
        201 }
        202 }  // namespace FileUtils
```

### example/deps/file_utils/ut/load_store_row_ut.cpp <a id="SS_23_2_28"></a>
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
         10 TEST(load_store, Row)
         11 {
         12     auto const row_exp = std::string{"ut_data/load_store/pkg_org"};
         13     auto const row_act = std::string{"ut_data/load_store/pkg_act"};
         14 
         15     RemoveFile(row_act);
         16 
         17     auto row_data0 = std::optional<std::vector<std::string>>{LoadFromFile(row_act, Load_Strings)};
         18 
         19     // row_actはないのでエラーなはず
         20     ASSERT_FALSE(row_data0);
         21 
         22     // ディレクトリなのでエラーなはず
         23     ASSERT_FALSE(StoreToFile("ut_data/app1", *row_data0, StoreToStream));
         24 
         25     row_data0 = LoadFromFile(row_exp, Load_Strings);
         26     ASSERT_TRUE(row_data0);
         27     ASSERT_TRUE(StoreToFile(row_act, *row_data0, StoreToStream));
         28 
         29     auto row_data1 = std::optional<std::vector<std::string>>{LoadFromFile(row_act, Load_Strings)};
         30     ASSERT_TRUE(row_data1);
         31 
         32     ASSERT_EQ(*row_data0, *row_data1);
         33 
         34     RemoveFile(row_act);
         35 }
         36 }  // namespace
         37 }  // namespace FileUtils
```

### example/deps/file_utils/ut/path_utils_ut.cpp <a id="SS_23_2_29"></a>
```cpp
          1 #include "gtest_wrapper.h"
          2 
          3 #include "file_utils/load_store.h"
          4 #include "file_utils/load_store_row.h"
          5 #include "file_utils/path_utils.h"
          6 #include "logging/logger.h"
          7 
          8 namespace FileUtils {
          9 namespace {
         10 
         11 TEST(path_utils, Logger)
         12 {
         13     auto log_file_org = "ut_data/load_store/logger_org";
         14     auto log_file_act = "ut_data/load_store/logger_act";
         15 
         16     RemoveFile(log_file_act);
         17 
         18     LOGGER_INIT(log_file_act);
         19     LOGGER(1);
         20     LOGGER("xyz", 3, 5);
         21 
         22     auto const dirs = Paths_t{"ut_data/app1",
         23                               "ut_data/app1/mod1",
         24                               "ut_data/app1/mod2",
         25                               "ut_data/app1/mod2/mod2_1",
         26                               "ut_data/app1/mod2/mod2_2",
         27                               "ut_data/app2"};
         28 
         29     LOGGER(ToStringPaths(dirs));
         30     LOGGER(dirs);
         31 
         32     Logging::Logger::Inst().Close();
         33 
         34     auto exp = std::optional<std::vector<std::string>>{LoadFromFile(log_file_org, Load_Strings)};
         35     ASSERT_TRUE(exp);
         36 
         37     auto act = std::optional<std::vector<std::string>>{LoadFromFile(log_file_act, Load_Strings)};
         38     ASSERT_TRUE(act);
         39 
         40     ASSERT_EQ(*exp, *act);
         41 
         42     RemoveFile(log_file_act);
         43 }
         44 
         45 TEST(path_utils, NotDirs)
         46 {
         47     {
         48         auto const dir_in  = Paths_t{"ut_data/app1",
         49                                     "ut_data/app1/mod1",
         50                                     "ut_data/app1/mod2",
         51                                     "ut_data/app1/mod2/mod2_1",
         52                                     "ut_data/app1/mod2/mod2_2",
         53                                     "ut_data/app2"};
         54         auto const dir_act = Paths_t{NotDirs(dir_in)};
         55 
         56         ASSERT_EQ(Paths_t{}, dir_act);
         57     }
         58     {
         59         auto const dir_in  = Paths_t{"ut_data/app1",
         60                                     "ut_data/app1/notdir",
         61                                     "ut_data/notdir2",
         62                                     "ut_data/app1/mod2/mod2_1",
         63                                     "ut_data/app1/mod2/mod2_2",
         64                                     "ut_data/app2"};
         65         auto const dir_act = Paths_t{NotDirs(dir_in)};
         66         auto const dir_exp = Paths_t{
         67             "ut_data/app1/notdir",
         68             "ut_data/notdir2",
         69         };
         70 
         71         ASSERT_EQ(dir_exp, dir_act);
         72     }
         73 }
         74 
         75 TEST(path_utils, NormalizeLexically)
         76 {
         77     // こうなるのでNormalizeLexicallyが必要
         78     ASSERT_EQ(Path_t("a"), Path_t("a"));
         79     ASSERT_NE(Path_t("a/"), Path_t("a"));
         80     ASSERT_EQ("a/", Path_t("x/../a/").lexically_normal().string());
         81     ASSERT_EQ("a", Path_t("x/../a").lexically_normal().string());
         82 
         83     // テストはここから
         84     ASSERT_EQ("a", NormalizeLexically("x/../a/").string());
         85     ASSERT_EQ("a", NormalizeLexically("./x/../a/").string());
         86     ASSERT_EQ("../a", NormalizeLexically(".././x/../a/").string());
         87     ASSERT_EQ("../a", NormalizeLexically(".././x/../a////").string());
         88     ASSERT_EQ("../a", NormalizeLexically(".././x/../a/./././").string());
         89 
         90     ASSERT_EQ("a", NormalizeLexically(Path_t("x/../a/")).string());
         91 
         92     ASSERT_EQ(".", NormalizeLexically(Path_t("./")).string());
         93     ASSERT_EQ(".", NormalizeLexically(Path_t(".")).string());
         94 }
         95 
         96 TEST(path_utils, GenFilename2Path)
         97 {
         98     auto const act_srcs
         99         = Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.cpp",
        100                   "ut_data/app1/a_1_cpp.h", "ut_data/app1/a_2_c.C"};
        101 
        102     auto const act = GenFilename2Path(act_srcs);
        103 
        104     auto const exp = Filename2Path_t{
        105         {"a_1_c.c", "ut_data/app1/a_1_c.c"},         {"a_1_c.h", "ut_data/app1/a_1_c.h"},
        106         {"a_1_cpp.cpp", "ut_data/app1/a_1_cpp.cpp"}, {"a_1_cpp.h", "ut_data/app1/a_1_cpp.h"},
        107         {"a_2_c.C", "ut_data/app1/a_2_c.C"},
        108     };
        109 
        110     ASSERT_EQ(act, exp);
        111 }
        112 
        113 TEST(path_utils, AssginSrcsToDirs)
        114 {
        115     {
        116         auto const exp_dirs = Paths_t{"ut_data/app1",
        117                                       "ut_data/app1/mod1",
        118                                       "ut_data/app1/mod2",
        119                                       "ut_data/app1/mod2/mod2_1",
        120                                       "ut_data/app1/mod2/mod2_2",
        121                                       "ut_data/app2"};
        122 
        123         auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        124                                       "ut_data/app1/a_1_c.h",
        125                                       "ut_data/app1/a_1_cpp.cpp",
        126                                       "ut_data/app1/a_1_cpp.h",
        127                                       "ut_data/app1/a_2_c.C",
        128                                       "ut_data/app1/a_2_c.H",
        129                                       "ut_data/app1/a_2_cpp.cxx",
        130                                       "ut_data/app1/a_2_cpp.hpp",
        131                                       "ut_data/app1/a_3_cpp.cc",
        132                                       "ut_data/app1/mod1/mod1_1.cpp",
        133                                       "ut_data/app1/mod1/mod1_1.hpp",
        134                                       "ut_data/app1/mod1/mod1_2.hpp",
        135                                       "ut_data/app1/mod2/mod2_1.cpp",
        136                                       "ut_data/app1/mod2/mod2_1.hpp",
        137                                       "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        138                                       "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        139                                       "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        140                                       "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        141                                       "ut_data/app2/b_1.cpp",
        142                                       "ut_data/app2/b_1.h"};
        143 
        144         auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        145 
        146         auto const exp = Dirs2Srcs_t{
        147             {"ut_data/app1",
        148              {"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.cpp",
        149               "ut_data/app1/a_1_cpp.h", "ut_data/app1/a_2_c.C", "ut_data/app1/a_2_c.H",
        150               "ut_data/app1/a_2_cpp.cxx", "ut_data/app1/a_2_cpp.hpp", "ut_data/app1/a_3_cpp.cc"}},
        151             {"ut_data/app1/mod1",
        152              {"ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp",
        153               "ut_data/app1/mod1/mod1_2.hpp"}},
        154             {"ut_data/app1/mod2", {"ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
        155             {"ut_data/app1/mod2/mod2_1",
        156              {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
        157             {"ut_data/app1/mod2/mod2_2",
        158              {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp", "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
        159             {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
        160         };
        161 
        162         ASSERT_EQ(act, exp);
        163     }
        164     {
        165         auto const exp_dirs = Paths_t{".", "ut_data/app1/mod1"};
        166         auto const exp_srcs = Paths_t{"path_utils.cpp", "ut_data/app1/mod1/mod1_1.cpp",
        167                                       "ut_data/app1/mod1/mod1_1.hpp"};
        168 
        169         auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        170 
        171         auto const exp = Dirs2Srcs_t{
        172             {".", {"path_utils.cpp"}},
        173             {"ut_data/app1/mod1", {"ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp"}},
        174         };
        175 
        176         ASSERT_EQ(act, exp);
        177     }
        178 }
        179 
        180 TEST(path_utils, PackageSrcMatcher2)
        181 {
        182     auto const exp_dirs = Paths_t{"ut_data", "ut_data/app1/mod2", "ut_data/app1/mod2/mod2_1",
        183                                   "ut_data/app1/mod2/mod2_2", "ut_data/app2"};
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
        197                                   "ut_data/app1/mod2/mod2_1.cpp",
        198                                   "ut_data/app1/mod2/mod2_1.hpp",
        199                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        200                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        201                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        202                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        203                                   "ut_data/app2/b_1.cpp",
        204                                   "ut_data/app2/b_1.h"};
        205 
        206     auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        207 
        208     auto const exp = Dirs2Srcs_t{
        209         {"ut_data",
        210          {"ut_data/app1/a_1_c.c", "ut_data/app1/a_1_c.h", "ut_data/app1/a_1_cpp.cpp",
        211           "ut_data/app1/a_1_cpp.h", "ut_data/app1/a_2_c.C", "ut_data/app1/a_2_c.H",
        212           "ut_data/app1/a_2_cpp.cxx", "ut_data/app1/a_2_cpp.hpp", "ut_data/app1/a_3_cpp.cc",
        213           "ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp",
        214           "ut_data/app1/mod1/mod1_2.hpp"}},
        215         {"ut_data/app1", {}},
        216         {"ut_data/app1/mod2", {"ut_data/app1/mod2/mod2_1.cpp", "ut_data/app1/mod2/mod2_1.hpp"}},
        217         {"ut_data/app1/mod2/mod2_1",
        218          {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
        219         {"ut_data/app1/mod2/mod2_2",
        220          {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp", "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
        221         {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
        222     };
        223 
        224     ASSERT_EQ(act, exp);
        225 }
        226 
        227 TEST(path_utils, PackageSrcMatcher3)
        228 {
        229     auto const exp_dirs
        230         = Paths_t{"ut_data/app1/mod2/mod2_1", "ut_data/app1/mod2/mod2_2", "ut_data/app2"};
        231 
        232     auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c",
        233                                   "ut_data/app1/mod1/mod1_1.cpp",
        234                                   "ut_data/app1/mod1/mod1_1.hpp",
        235                                   "ut_data/app1/mod1/mod1_2.hpp",
        236                                   "ut_data/app1/mod2/mod2_1.cpp",
        237                                   "ut_data/app1/mod2/mod2_1.hpp",
        238                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        239                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h",
        240                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.cpp",
        241                                   "ut_data/app1/mod2/mod2_2/mod2_2_1.h",
        242                                   "ut_data/app2/b_1.cpp",
        243                                   "ut_data/app2/b_1.h"};
        244 
        245     auto const act = AssginSrcsToDirs(exp_dirs, exp_srcs);
        246 
        247     auto const exp = Dirs2Srcs_t{
        248         {"ut_data/app1/mod2/mod2_1",
        249          {"ut_data/app1/mod2/mod2_1/mod2_1_1.cpp", "ut_data/app1/mod2/mod2_1/mod2_1_1.h"}},
        250         {"ut_data/app1/mod2/mod2_2",
        251          {"ut_data/app1/mod2/mod2_2/mod2_2_1.cpp", "ut_data/app1/mod2/mod2_2/mod2_2_1.h"}},
        252         {"ut_data/app2", {"ut_data/app2/b_1.cpp", "ut_data/app2/b_1.h"}},
        253         {"no_package",
        254          {"ut_data/app1/a_1_c.c", "ut_data/app1/mod1/mod1_1.cpp", "ut_data/app1/mod1/mod1_1.hpp",
        255           "ut_data/app1/mod1/mod1_2.hpp", "ut_data/app1/mod2/mod2_1.cpp",
        256           "ut_data/app1/mod2/mod2_1.hpp"}},
        257     };
        258 
        259     ASSERT_EQ(act, exp);
        260 }
        261 
        262 TEST(path_utils, ToString_Path)
        263 {
        264     {
        265         auto const exp_path = Path_t{"ut_data/app1/a_1_c.c"};
        266         auto const exp      = std::string{"ut_data/app1/a_1_c.c"};
        267         auto const act      = ToStringPath(exp_path);
        268 
        269         ASSERT_EQ(act, exp);
        270     }
        271     {
        272         auto const exp_path = Path_t{""};
        273         auto const exp      = std::string{"\"\""};
        274         auto const act      = ToStringPath(exp_path);
        275 
        276         ASSERT_EQ(act, exp);
        277     }
        278 }
        279 
        280 TEST(path_utils, ToString_Paths)
        281 {
        282     auto const exp_srcs = Paths_t{"ut_data/app1/a_1_c.c", "ut_data/app1/mod1/mod1_1.cpp",
        283                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp",
        284                                   "ut_data/app1/mod2/mod2_1/mod2_1_1.h", "ut_data/app2/b_1.h"};
        285 
        286     auto const exp = std::string{
        287         "ut_data/app1/a_1_c.c "
        288         "ut_data/app1/mod1/mod1_1.cpp "
        289         "ut_data/app1/mod2/mod2_1/mod2_1_1.cpp "
        290         "ut_data/app1/mod2/mod2_1/mod2_1_1.h "
        291         "ut_data/app2/b_1.h"};
        292     auto const act = ToStringPaths(exp_srcs, " ");
        293 
        294     ASSERT_EQ(act, exp);
        295 }
        296 }  // namespace
        297 }  // namespace FileUtils
```

### example/deps/lib/h/lib/nstd.h <a id="SS_23_2_30"></a>
```cpp
          1 #pragma once
          2 #include <algorithm>
          3 #include <fstream>
          4 #include <list>
          5 #include <string>
          6 #include <vector>
          7 
          8 namespace Nstd {
          9 template <typename T, size_t N>
         10 constexpr size_t ArrayLength(T const (&)[N]) noexcept
         11 {
         12     return N;
         13 }
         14 
         15 template <typename T>
         16 void SortUnique(std::vector<T>& v)
         17 {
         18     std::sort(v.begin(), v.end());
         19     auto result = std::unique(v.begin(), v.end());
         20     v.erase(result, v.end());
         21 }
         22 
         23 template <typename T>
         24 void SortUnique(std::list<T>& v)
         25 {
         26     v.sort();
         27     v.unique();
         28 }
         29 
         30 template <typename T>
         31 void Concatenate(std::vector<T>& v0, std::vector<T>&& v1)
         32 {
         33     for (auto& v1_elem : v1) {
         34         v0.insert(v0.end(), std::move(v1_elem));
         35     }
         36 }
         37 
         38 template <typename T>
         39 void Concatenate(std::list<T>& v0, std::list<T>&& v1)
         40 {
         41     v0.splice(v0.end(), std::move(v1));
         42 }
         43 
         44 template <typename F>
         45 class ScopedGuard {
         46 public:
         47     explicit ScopedGuard(F&& f) noexcept : f_{f} {}
         48     ~ScopedGuard() { f_(); }
         49     ScopedGuard(ScopedGuard const&)            = delete;
         50     ScopedGuard& operator=(ScopedGuard const&) = delete;
         51 
         52 private:
         53     F f_;
         54 };
         55 
         56 inline std::string Replace(std::string in, std::string_view from, std::string_view to)
         57 {
         58     auto pos = in.find(from);
         59 
         60     while (pos != std::string::npos) {
         61         in.replace(pos, from.length(), to);
         62         pos = in.find(from, pos + to.length());
         63     }
         64 
         65     return in;
         66 }
         67 
         68 //
         69 // operator<< for range
         70 //
         71 namespace Inner_ {
         72 //
         73 // exists_put_to_as_member
         74 //
         75 template <typename, typename = std::ostream&>
         76 struct exists_put_to_as_member : std::false_type {
         77 };
         78 
         79 template <typename T>
         80 struct exists_put_to_as_member<T, decltype(std::declval<std::ostream&>().operator<<(
         81                                       std::declval<T>()))> : std::true_type {
         82 };
         83 
         84 template <typename T>
         85 constexpr bool exists_put_to_as_member_v{exists_put_to_as_member<T>::value};
         86 
         87 //
         88 // exists_put_to_as_non_member
         89 //
         90 template <typename, typename = std::ostream&>
         91 struct exists_put_to_as_non_member : std::false_type {
         92 };
         93 
         94 template <typename T>
         95 struct exists_put_to_as_non_member<T, decltype(operator<<(std::declval<std::ostream&>(),
         96                                                           std::declval<T>()))> : std::true_type {
         97 };
         98 
         99 template <typename T>
        100 constexpr bool exists_put_to_as_non_member_v{exists_put_to_as_non_member<T>::value};
        101 
        102 //
        103 // exists_put_to_v
        104 //
        105 template <typename T>
        106 constexpr bool exists_put_to_v{
        107     Nstd::Inner_::exists_put_to_as_member_v<T> || Nstd::Inner_::exists_put_to_as_non_member_v<T>};
        108 
        109 //
        110 // is_range
        111 //
        112 template <typename, typename = bool>
        113 struct is_range : std::false_type {
        114 };
        115 
        116 template <typename T>
        117 struct is_range<T, typename std::enable_if_t<!std::is_array_v<T>,
        118                                              decltype(std::begin(std::declval<T>()), bool{})>>
        119     : std::true_type {
        120 };
        121 
        122 template <typename T>
        123 struct is_range<T, typename std::enable_if_t<std::is_array_v<T>, bool>> : std::true_type {
        124 };
        125 
        126 //
        127 // is_range_v
        128 //
        129 template <typename T>
        130 constexpr bool is_range_v{is_range<T>::value};
        131 
        132 }  // namespace Inner_
        133 
        134 //
        135 // operator<< for range
        136 //
        137 template <typename T>
        138 auto operator<<(std::ostream& os, T const& t) ->
        139     typename std::enable_if_t<Inner_::is_range_v<T> && !Inner_::exists_put_to_v<T>, std::ostream&>
        140 {
        141     auto first = true;
        142 
        143     for (auto const& i : t) {
        144         if (!std::exchange(first, false)) {
        145             os << ", ";
        146         }
        147         os << i;
        148     }
        149 
        150     return os;
        151 }
        152 }  // namespace Nstd
```

### example/deps/lib/ut/nstd_ut.cpp <a id="SS_23_2_31"></a>
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
         14 TEST(Nstd, ArrayLength)
         15 {
         16     {
         17         char const* act[] = {"d", "a", "ab", "bcd"};
         18 
         19         ASSERT_EQ(4, ArrayLength(act));
         20     }
         21     {
         22         std::string const act[] = {"d", "a", "Ab"};
         23 
         24         ASSERT_EQ(3, ArrayLength(act));
         25     }
         26 }
         27 
         28 TEST(Nstd, SortUnique)
         29 {
         30     {
         31         auto act = std::vector<std::string>{"d", "a", "ab", "bcd"};
         32 
         33         SortUnique(act);
         34 
         35         ASSERT_EQ((std::vector<std::string>{"a", "ab", "bcd", "d"}), act);
         36     }
         37     {
         38         auto act = std::list<std::filesystem::path>{"d", "a", "Ab", "bcd"};
         39 
         40         SortUnique(act);
         41 
         42         ASSERT_EQ((std::list<std::filesystem::path>{"Ab", "a", "bcd", "d"}), act);
         43     }
         44 }
         45 
         46 TEST(Nstd, Concatenate)
         47 {
         48     {
         49         auto act0 = std::vector<std::string>{"d", "a", "ab"};
         50         auto act1 = std::vector<std::string>{"bcd", "ef"};
         51 
         52         Concatenate(act0, std::move(act1));
         53         ASSERT_EQ((std::vector<std::string>{"d", "a", "ab", "bcd", "ef"}), act0);
         54     }
         55     {
         56         auto act0 = std::list<std::filesystem::path>{"d", "a", "ab"};
         57         auto act1 = std::list<std::filesystem::path>{"bcd", "ef"};
         58 
         59         Concatenate(act0, std::move(act1));
         60         ASSERT_EQ((std::list<std::filesystem::path>{"d", "a", "ab", "bcd", "ef"}), act0);
         61     }
         62 }
         63 
         64 TEST(Nstd, ScopedGuard)
         65 {
         66     auto s = std::string{"not called"};
         67 
         68     {
         69         auto sg = ScopedGuard{[&s]() noexcept { s = "called"; }};
         70         ASSERT_EQ(s, "not called");
         71     }
         72 
         73     ASSERT_EQ(s, "called");
         74 }
         75 
         76 TEST(Nstd, Replace)
         77 {
         78     {
         79         auto in  = std::string{"a-b-c-d"};
         80         auto act = Replace(in, "-", "/");
         81         ASSERT_EQ(act, "a/b/c/d");
         82     }
         83     {
         84         auto in  = std::string{"a-b-c-d"};
         85         auto act = Replace(in, "-", "///////");
         86         ASSERT_EQ(act, "a///////b///////c///////d");
         87     }
         88     {
         89         auto in  = std::string{"a-b-c-d"};
         90         auto act = Replace(in, "-", "");
         91         ASSERT_EQ(act, "abcd");
         92     }
         93 }
         94 
         95 TEST(stl_try, exclude)
         96 {
         97     auto       dirs    = std::list<std::string>{"A", "B", "A/e", "A/e/f", "B/xxx/ef"};
         98     auto       exclude = std::string{R"(.*/e\b.*)"};
         99     auto const pattern = std::regex{exclude};
        100 
        101     dirs.remove_if([&pattern](auto const& d) {
        102         auto results = std::smatch{};
        103         return std::regex_match(d, results, pattern);
        104     });
        105 
        106     ASSERT_EQ(dirs, (std::list<std::string>{"A", "B", "B/xxx/ef"}));
        107 }
        108 }  // namespace
        109 
        110 namespace Inner_ {
        111 namespace {
        112 class test_class_exits_put_to {};
        113 
        114 std::ostream& operator<<(std::ostream& os, test_class_exits_put_to) { return os; }
        115 
        116 class test_class_not_exits_put_to {};
        117 
        118 TEST(Nstd, exists_put_to_as_member)
        119 {
        120     static_assert(exists_put_to_as_member_v<bool>);
        121     static_assert(exists_put_to_as_member_v<char[3]>);
        122     static_assert(!exists_put_to_as_member_v<std::string>);
        123     static_assert(!exists_put_to_as_member_v<std::vector<int>>);
        124     static_assert(exists_put_to_as_member_v<std::vector<int>*>);
        125     static_assert(!exists_put_to_as_member_v<test_class_exits_put_to>);
        126     static_assert(!exists_put_to_as_member_v<test_class_not_exits_put_to>);
        127     static_assert(exists_put_to_as_member_v<test_class_not_exits_put_to[3]>);
        128     auto oss = std::ostringstream{};
        129     oss << test_class_exits_put_to{};
        130 }
        131 
        132 TEST(Template, exists_put_to_as_non_member)
        133 {
        134     static_assert(!exists_put_to_as_non_member_v<bool>);
        135     static_assert(exists_put_to_as_non_member_v<std::string>);
        136     static_assert(!exists_put_to_as_non_member_v<std::vector<int>>);
        137     static_assert(!exists_put_to_as_non_member_v<std::vector<int>*>);
        138     static_assert(exists_put_to_as_non_member_v<test_class_exits_put_to>);
        139     static_assert(!exists_put_to_as_non_member_v<test_class_not_exits_put_to>);
        140     static_assert(!exists_put_to_as_non_member_v<test_class_not_exits_put_to[3]>);
        141 }
        142 
        143 TEST(Template, exists_put_to_v)
        144 {
        145     static_assert(exists_put_to_v<bool>);
        146     static_assert(exists_put_to_v<std::string>);
        147     static_assert(!exists_put_to_v<std::vector<int>>);
        148     static_assert(exists_put_to_v<std::vector<int>*>);
        149     static_assert(exists_put_to_v<test_class_exits_put_to>);
        150     static_assert(!exists_put_to_v<test_class_not_exits_put_to>);
        151     static_assert(exists_put_to_v<test_class_not_exits_put_to[3]>);
        152 }
        153 
        154 TEST(Template, is_range)
        155 {
        156     static_assert(is_range_v<std::string>);
        157     static_assert(!is_range_v<int>);
        158     static_assert(is_range_v<int const[3]>);
        159     static_assert(is_range_v<int[3]>);
        160 }
        161 }  // namespace
        162 }  // namespace Inner_
        163 
        164 namespace {
        165 TEST(Template, PutTo)
        166 {
        167     {
        168         auto oss = std::ostringstream{};
        169         char c[] = "c3";
        170 
        171         oss << c;
        172         ASSERT_EQ("c3", oss.str());
        173     }
        174     {
        175         auto oss = std::ostringstream{};
        176         auto str = std::vector<std::string>{"1", "2", "3"};
        177 
        178         oss << str;
        179         ASSERT_EQ("1, 2, 3", oss.str());
        180     }
        181     {
        182         auto oss = std::ostringstream{};
        183         auto p   = std::list<std::filesystem::path>{"1", "2", "3"};
        184 
        185         oss << p;
        186         ASSERT_EQ("\"1\", \"2\", \"3\"", oss.str());
        187     }
        188 }
        189 }  // namespace
        190 }  // namespace Nstd
```

### example/deps/logging/h/logging/logger.h <a id="SS_23_2_32"></a>
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
         16     static Logger& Inst(char const* filename = nullptr);
         17 
         18     template <typename HEAD, typename... TAIL>
         19     void Set(char const* filename, uint32_t line_no, HEAD const& head, TAIL... tails)
         20     {
         21         auto   path     = std::string_view{filename};
         22         size_t npos     = path.find_last_of('/');
         23         auto   basename = (npos != std::string_view::npos) ? path.substr(npos + 1) : path;
         24 
         25         os_.width(12);
         26         os_ << basename << ":";
         27 
         28         os_.width(3);
         29         os_ << line_no;
         30 
         31         set_inner(head, tails...);
         32     }
         33 
         34     // @@@ ignore begin
         35     void Close();
         36     Logger(Logger const&)            = delete;
         37     Logger& operator=(Logger const&) = delete;
         38     // @@@ ignore end
         39 
         40 private:
         41     void set_inner() { os_ << std::endl; }
         42 
         43     template <typename HEAD, typename... TAIL>
         44     void set_inner(HEAD const& head, TAIL... tails)
         45     {
         46         using Nstd::operator<<;
         47         os_ << ":" << head;
         48         set_inner(tails...);
         49     }
         50 
         51     template <typename HEAD, typename... TAIL>
         52     void set_inner(char sep, HEAD const& head, TAIL... tails)
         53     {
         54         using Nstd::operator<<;
         55         os_ << sep << head;
         56         set_inner(tails...);
         57     }
         58 
         59     // @@@ ignore begin
         60     explicit Logger(char const* filename);
         61 
         62     std::ofstream ofs_{};
         63     std::ostream& os_;
         64 
         65     // @@@ ignore end
         66 };
         67 }  // namespace Logging
         68 
         69 #define LOGGER_INIT(filename) Logging::Logger::Inst(filename)
         70 #define LOGGER(...) Logging::Logger::Inst().Set(__FILE__, __LINE__, __VA_ARGS__)
         71 // @@@ sample end
```

### example/deps/logging/src/logger.cpp <a id="SS_23_2_33"></a>
```cpp
          1 #include "logging/logger.h"
          2 
          3 namespace {
          4 class null_ostream : private std::streambuf, public std::ostream {
          5 public:
          6     static null_ostream& Inst()
          7     {
          8         static null_ostream inst;
          9         return inst;
         10     }
         11 
         12 protected:
         13     virtual int overflow(int c)
         14     {
         15         setp(buf_, buf_ + sizeof(buf_));
         16         return (c == eof() ? '\0' : c);
         17     }
         18 
         19 private:
         20     null_ostream() : std::ostream{this} {}
         21     char buf_[128];
         22 };
         23 
         24 std::ostream& init_os(char const* filename, std::ofstream& ofs)
         25 {
         26     if (filename == nullptr) {
         27         return std::cout;
         28     }
         29     else {
         30         if (std::string{filename}.size() == 0) {
         31             return null_ostream::Inst();
         32         }
         33         else {
         34             ofs.open(filename);
         35             return ofs;
         36         }
         37     }
         38 }
         39 }  // namespace
         40 
         41 namespace Logging {
         42 Logger::Logger(char const* filename) : os_{init_os(filename, ofs_)} {}
         43 
         44 Logger& Logger::Inst(char const* filename)
         45 {
         46     static auto inst = Logger{filename};
         47 
         48     return inst;
         49 }
         50 
         51 void Logger::Close()
         52 {
         53     if (&std::cout != &os_) {
         54         ofs_.close();
         55     }
         56 }
         57 }  // namespace Logging
```

### example/deps/logging/ut/logger_ut.cpp <a id="SS_23_2_34"></a>
```cpp
          1 #include <filesystem>
          2 
          3 #include "gtest_wrapper.h"
          4 
          5 #include "logging/logger.h"
          6 
          7 namespace {
          8 
          9 TEST(log, Logger)
         10 {
         11     // loggingのテストは他のライブラリで行う。
         12     // ここではコンパイルできることの確認のみ。
         13 
         14     LOGGER_INIT(nullptr);
         15     LOGGER(1);
         16     LOGGER("xyz", 3, 5);
         17 
         18     auto file = std::filesystem::path{"hehe"};
         19     LOGGER(file);
         20 }
         21 }  // namespace
```

### example/dynamic_memory_allocation/malloc_ut.cpp <a id="SS_23_2_35"></a>
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
         25     size_t    n_nuits;  // header_tが何個あるか
         26 };
         27 
         28 header_t*        header{nullptr};
         29 SpinLock         spin_lock{};
         30 constexpr size_t unit_size{sizeof(header_t)};
         31 
         32 inline bool sprit(header_t* header, size_t n_nuits, header_t*& next) noexcept
         33 {
         34     // @@@ ignore begin
         35     assert(n_nuits > 1);  // ヘッダとバッファなので最低でも2
         36 
         37     next = nullptr;
         38 
         39     if (header->n_nuits == n_nuits || header->n_nuits == n_nuits + 1) {
         40         next = header->next;
         41         return true;
         42     }
         43     else if (header->n_nuits > n_nuits) {
         44         next            = header + n_nuits;
         45         next->n_nuits   = header->n_nuits - n_nuits;
         46         next->next      = header->next;
         47         header->n_nuits = n_nuits;
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
         58     if (front + front->n_nuits == rear) {  // 1枚のメモリになる
         59         front->n_nuits += rear->n_nuits;
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
         76     auto n_nuits = (Roundup(unit_size, size) / unit_size) + 1;
         77     auto lock    = std::lock_guard{spin_lock};
         78 
         79     auto curr = header;
         80     for (header_t* prev = nullptr; curr != nullptr; prev = curr, curr = curr->next) {
         81         header_t* next;
         82 
         83         if (!sprit(curr, n_nuits, next)) {
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
        154         add->n_nuits  = add_size / unit_size;
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
        176         constexpr auto n_nuits = Roundup(unit_size, unit_size + sizeof(int)) / unit_size;
        177 
        178         for (auto& i : ints) {
        179             i = malloc(sizeof(int));
        180 
        181             header_t* h = set_back(i);
        182             ASSERT_EQ(h->n_nuits, n_nuits);
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

### example/dynamic_memory_allocation/mpool_variable.h <a id="SS_23_2_36"></a>
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
         15     size_t    n_nuits;  // header_tが何個あるか
         16 };
         17 
         18 constexpr auto unit_size = sizeof(header_t);
         19 
         20 inline std::optional<header_t*> sprit(header_t* header, size_t n_nuits) noexcept
         21 {
         22     assert(n_nuits > 1);  // ヘッダとバッファなので最低でも2
         23 
         24     if (header->n_nuits == n_nuits || header->n_nuits == n_nuits + 1) {
         25         return header->next;
         26     }
         27     else if (header->n_nuits > n_nuits) {
         28         auto next       = header + n_nuits;
         29         next->n_nuits   = header->n_nuits - n_nuits;
         30         next->next      = header->next;
         31         header->n_nuits = n_nuits;
         32         return next;
         33     }
         34 
         35     return std::nullopt;
         36 }
         37 
         38 inline void concat(header_t* front, header_t* rear) noexcept
         39 {
         40     if (front + front->n_nuits == rear) {  // 1枚のメモリになる
         41         front->n_nuits += rear->n_nuits;
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
         55     alignas(alignof(std::max_align_t)) uint8_t buffer[Roundup(sizeof(header_t), MEM_SIZE)];
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
         69         header_->n_nuits = sizeof(buff_) / Inner_::unit_size;
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
         89         bool operator==(const_iterator const& rhs) noexcept { return header_ == rhs.header_; }
         90         bool operator!=(const_iterator const& rhs) noexcept { return !(*this == rhs); }
         91 
         92     private:
         93         Inner_::header_t const* header_;
         94     };
         95 
         96     const_iterator begin() const noexcept { return const_iterator{header_}; }
         97     const_iterator end() const noexcept { return const_iterator{nullptr}; }
         98     const_iterator cbegin() const noexcept { return const_iterator{header_}; }
         99     const_iterator cend() const noexcept { return const_iterator{nullptr}; }
        100     // @@@ sample end
        101     // @@@ sample begin 0:3
        102 
        103 private:
        104     using header_t = Inner_::header_t;
        105 
        106     Inner_::buffer_t<MEM_SIZE> buff_{};
        107     header_t*                  header_{reinterpret_cast<header_t*>(buff_.buffer)};
        108     mutable SpinLock           spin_lock_{};
        109     size_t                     unit_count_{sizeof(buff_) / Inner_::unit_size};
        110     size_t                     unit_count_min_{sizeof(buff_) / Inner_::unit_size};
        111 
        112     virtual void* alloc(size_t size) noexcept override
        113     {
        114         // @@@ ignore begin
        115         // size分のメモリとヘッダ
        116         auto n_nuits = (Roundup(Inner_::unit_size, size) / Inner_::unit_size) + 1;
        117 
        118         auto lock = std::lock_guard{spin_lock_};
        119 
        120         auto curr = header_;
        121 
        122         for (header_t* prev{nullptr}; curr != nullptr; prev = curr, curr = curr->next) {
        123             auto opt_next = std::optional<header_t*>{sprit(curr, n_nuits)};
        124 
        125             if (!opt_next) {
        126                 continue;
        127             }
        128 
        129             auto next = *opt_next;
        130             if (prev == nullptr) {
        131                 header_ = next;
        132             }
        133             else {
        134                 prev->next = next;
        135             }
        136             break;
        137         }
        138 
        139         if (curr != nullptr) {
        140             unit_count_ -= curr->n_nuits;
        141             unit_count_min_ = std::min(unit_count_, unit_count_min_);
        142             ++curr;
        143         }
        144 
        145         return curr;
        146         // @@@ ignore end
        147     }
        148 
        149     virtual void free(void* mem) noexcept override
        150     {
        151         // @@@ ignore begin
        152         header_t* to_free = Inner_::set_back(mem);
        153 
        154         to_free->next = nullptr;
        155 
        156         auto lock = std::lock_guard{spin_lock_};
        157 
        158         unit_count_ += to_free->n_nuits;
        159         unit_count_min_ = std::min(unit_count_, unit_count_min_);
        160 
        161         if (header_ == nullptr) {
        162             header_ = to_free;
        163             return;
        164         }
        165 
        166         if (to_free < header_) {
        167             concat(to_free, header_);
        168             header_ = to_free;
        169             return;
        170         }
        171 
        172         header_t* curr = header_;
        173 
        174         for (; curr->next != nullptr; curr = curr->next) {
        175             if (to_free < curr->next) {  // 常に curr < to_free
        176                 concat(to_free, curr->next);
        177                 concat(curr, to_free);
        178                 return;
        179             }
        180         }
        181 
        182         concat(curr, to_free);
        183         // @@@ ignore end
        184     }
        185 
        186     virtual size_t get_size() const noexcept override { return 1; }
        187     virtual size_t get_count() const noexcept override { return unit_count_ * Inner_::unit_size; }
        188     virtual size_t get_count_min() const noexcept override
        189     {
        190         return unit_count_min_ * Inner_::unit_size;
        191     }
        192 
        193     virtual bool is_valid(void const* mem) const noexcept override
        194     {
        195         return (&buff_ < mem) && (mem < &buff_.buffer[ArrayLength(buff_.buffer)]);
        196     }
        197     // @@@ sample end
        198     // @@@ sample begin 0:4
        199 };
        200 // @@@ sample end
```

### example/programming_convention/fixed_point.h <a id="SS_23_2_37"></a>
```cpp
          1 #pragma once
          2 
          3 #include <cstdint>
          4 #include <type_traits>
          5 
          6 // @@@ sample begin 0:0
          7 
          8 /// @class FixedPoint
          9 /// @brief BASIC_TYPEで指定する基本型のビット長を持つ固定小数点を扱うためのクラス
         10 /// @tparam BASIC_TYPE       全体のビット長や、符号を指定するための整数型
         11 /// @tparam FRACTION_BIT_NUM 小数点保持のためのビット長
         12 template <typename BASIC_TYPE, uint32_t FRACTION_BIT_NUM>
         13 class FixedPoint {
         14 public:
         15     FixedPoint(BASIC_TYPE                                integer  = 0,
         16                typename std::make_unsigned_t<BASIC_TYPE> fraction = 0) noexcept
         17         : value_{get_init_value(integer, fraction)}
         18     {
         19         // @@@ ignore begin
         20         // signedに対する右ビットシフトの仕様が、算術右ビットシフトでないと
         21         // このクラスは成立しない。下記のstatic_assertはその確認。
         22         static_assert(IsSigned() ? (-1 >> 1 == -1) : true, "need logical right bit sift");
         23 
         24         // BASIC_TYPEをcharにすることは認めない。
         25         static_assert(!std::is_same_v<BASIC_TYPE, char>, "BASIC_TYPE should not be char");
         26         // @@@ ignore end
         27     }
         28     // @@@ sample end
         29     // @@@ sample begin 0:1
         30 
         31     // @@@ ignore begin
         32     ~FixedPoint()                                = default;
         33     FixedPoint(FixedPoint const&)                = default;
         34     FixedPoint& operator=(FixedPoint const&)     = default;
         35     FixedPoint(FixedPoint&&) noexcept            = default;
         36     FixedPoint& operator=(FixedPoint&&) noexcept = default;
         37 
         38     BASIC_TYPE GetValue() const noexcept { return value_; }
         39 
         40     BASIC_TYPE GetInteger() const noexcept { return value_ >> fraction_bit_num_; }
         41 
         42     BASIC_TYPE GetFraction() const noexcept { return value_ & fraction_bit_mask_; }
         43 
         44     double ToFloatPoint() const noexcept
         45     {
         46         return GetInteger() + (static_cast<double>(GetFraction()) / (fraction_bit_mask_ + 1));
         47     }
         48 
         49     constexpr typename std::make_unsigned_t<BASIC_TYPE> GetFractionMask() const noexcept
         50     {
         51         return fraction_bit_mask_;
         52     }
         53 
         54     constexpr typename std::make_unsigned_t<BASIC_TYPE> GetIntegerMask() const noexcept
         55     {
         56         return integer_bit_mask_;
         57     }
         58 
         59     static constexpr bool IsSigned() noexcept { return std::is_signed_v<BASIC_TYPE>; }
         60 
         61     static constexpr bool IsUnsigned() noexcept { return std::is_unsigned_v<BASIC_TYPE>; }
         62 
         63     // @@@ ignore end
         64     FixedPoint& operator+=(FixedPoint rhs) noexcept
         65     // @@@ ignore begin
         66     {
         67         value_ += rhs.value_;
         68         return *this;
         69     }
         70 
         71     // @@@ ignore end
         72     FixedPoint& operator-=(FixedPoint rhs) noexcept
         73     // @@@ ignore begin
         74     {
         75         value_ -= rhs.value_;
         76         return *this;
         77     }
         78 
         79     // @@@ ignore end
         80     FixedPoint& operator*=(FixedPoint rhs) noexcept
         81     // @@@ ignore begin
         82     {
         83         value_ *= rhs.value_ >> fraction_bit_num_;
         84         return *this;
         85     }
         86 
         87     // @@@ ignore end
         88     FixedPoint& operator/=(FixedPoint rhs) noexcept
         89     // @@@ ignore begin
         90     {
         91         using T = std::conditional_t<IsSigned(), int64_t, uint64_t>;
         92 
         93         value_ = (static_cast<T>(value_) << fraction_bit_num_) / rhs.value_;
         94 
         95         return *this;
         96     }
         97 
         98     // @@@ ignore end
         99 private:
        100     BASIC_TYPE value_;
        101     // @@@ ignore begin
        102 
        103     static constexpr uint32_t bit_mask(uint32_t bit_len) noexcept
        104     {
        105         if (bit_len == 0) {
        106             return 0x0;
        107         }
        108 
        109         return bit_mask(bit_len - 1) | (0x01 << (bit_len - 1));
        110     }
        111 
        112     static constexpr uint32_t fraction_bit_num_{FRACTION_BIT_NUM};
        113     static constexpr uint32_t fraction_bit_mask_{bit_mask(fraction_bit_num_)};
        114     static constexpr uint32_t integer_bit_num_{sizeof(BASIC_TYPE) * 8 - FRACTION_BIT_NUM};
        115     static constexpr uint32_t integer_bit_mask_{bit_mask(integer_bit_num_) << fraction_bit_num_};
        116 
        117     static constexpr BASIC_TYPE get_init_value(BASIC_TYPE integer, BASIC_TYPE fraction) noexcept
        118     {
        119 #if 0  // 本来は左シフト<<を使いたいが、signedに対しての<<は良くないので
        120         return (integer << fraction_bit_num_) | fraction;
        121 #else
        122         return (integer * (fraction_bit_mask_ + 1)) | fraction;
        123 #endif
        124     }
        125     // @@@ ignore end
        126 
        127     friend bool operator==(FixedPoint lhs, FixedPoint rhs) noexcept
        128     // @@@ ignore begin
        129     {
        130         return lhs.value_ == rhs.value_;
        131     }
        132 
        133     friend bool operator!=(FixedPoint lhs, FixedPoint rhs) noexcept { return !(lhs == rhs); }
        134 
        135     friend bool operator>(FixedPoint lhs, FixedPoint rhs) noexcept
        136     {
        137         return lhs.value_ > rhs.value_;
        138     }
        139 
        140     friend bool operator>=(FixedPoint lhs, FixedPoint rhs) noexcept
        141     {
        142         return (lhs > rhs) || (lhs == rhs);
        143     }
        144 
        145     friend bool operator<(FixedPoint lhs, FixedPoint rhs) noexcept { return (rhs > lhs); }
        146 
        147     friend bool operator<=(FixedPoint lhs, FixedPoint rhs) noexcept
        148     {
        149         return (lhs < rhs) || (lhs == rhs);
        150     }
        151     // @@@ ignore end
        152 
        153     // FixedPoint() + intのようなオーバーロードを作るためにあえてfriend
        154     friend FixedPoint operator+(FixedPoint lhs, FixedPoint rhs) noexcept
        155     // @@@ ignore begin
        156     {
        157         lhs += rhs;
        158         return lhs;
        159     }
        160 
        161     friend FixedPoint operator-(FixedPoint lhs, FixedPoint rhs) noexcept
        162     {
        163         lhs -= rhs;
        164         return lhs;
        165     }
        166 
        167     friend FixedPoint operator*(FixedPoint lhs, FixedPoint rhs) noexcept
        168     {
        169         lhs *= rhs;
        170         return lhs;
        171     }
        172 
        173     friend FixedPoint operator/(FixedPoint lhs, FixedPoint rhs) noexcept
        174     {
        175         lhs /= rhs;
        176         return lhs;
        177     }
        178     // @@@ ignore end
        179 };
        180 // @@@ sample end
```

## etc <a id="SS_23_3"></a>
### example/deps/CMakeLists.txt <a id="SS_23_3_1"></a>
```
          1 cmake_minimum_required(VERSION 3.10)
          2 
          3 project(main_project)
          4 
          5 set(CMAKE_CXX_STANDARD 17)
          6 set(CMAKE_CXX_STANDARD_REQUIRED True)
          7 
          8 set(GTEST_DIR "../../googletest")
          9 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
         10 
         11 include_directories("${GTEST_DIR}/googletest/include")
         12 
         13 # googletestサブディレクトリを追加
         14 add_subdirectory(${GTEST_DIR} ${CMAKE_BINARY_DIR}/googletest EXCLUDE_FROM_ALL)
         15 
         16 add_subdirectory(lib)
         17 add_subdirectory(logging)
         18 add_subdirectory(file_utils)
         19 add_subdirectory(dependency)
         20 add_subdirectory(app)
         21 
         22 # すべてのテストを実行するカスタムターゲットを追加
         23 add_custom_target(tests
         24     DEPENDS app_ut dependency_ut file_utils_ut lib_ut logging_ut deps_it
         25     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
         26 )
         27 
```

### example/deps/dependency/CMakeLists.txt <a id="SS_23_3_2"></a>
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

### example/deps/file_utils/CMakeLists.txt <a id="SS_23_3_3"></a>
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

### example/deps/lib/CMakeLists.txt <a id="SS_23_3_4"></a>
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

### example/deps/logging/CMakeLists.txt <a id="SS_23_3_5"></a>
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



