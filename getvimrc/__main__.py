"""vimrcとdein.tomlの設定をするスクリプトです。

~/.vimrcに変数vimrcの内容が入り
~/.vim/dein.tomlに変数deinの内容が入ります。
~/.vim/dein_lazy.tomlは作成しませんが、読み込むように設定しています。
"""
import os


vimrc = """\
" deinの設定
if &compatible
    set nocompatible
endif
let g:rc_dir = expand('~/.vim')  " vim設定ディレクトリ
let s:dein_repo_dir = g:rc_dir . '/repos/github.com/Shougo/dein.vim' " deinリポジトリ
" dein.vim がないときgit clone
if &runtimepath !~# '/dein.vim'
    if !isdirectory(s:dein_repo_dir)
        execute '!git clone https://github.com/Shougo/dein.vim' s:dein_repo_dir
    endif
    execute 'set runtimepath^=' . fnamemodify(s:dein_repo_dir, ':p')
endif
" プラグイン設定
if dein#load_state(g:rc_dir)
    call dein#begin(g:rc_dir)
    let s:toml      = g:rc_dir . '/dein.toml' "通常ロード
    let s:lazy_toml = g:rc_dir . '/dein_lazy.toml' "遅延ロード
    call dein#load_toml(s:toml,      {'lazy': 0})
    call dein#load_toml(s:lazy_toml, {'lazy': 1})
    call dein#end()
    call dein#save_state()
endif
" 未インストールプラグインインストール
if dein#check_install()
    call dein#install()
endif

filetype plugin on


" jedi.vim docstring非表示
autocmd Filetype python setlocal completeopt-=preview

" NERDTree vimをファイル指定せずに開くとツリー表示
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" flake8を、保存するたびに実行
autocmd BufWritePost *.py call Flake8()

" 基本設定
syntax enable "構文ハイライト有効化
set number    "行番号表示
set showmatch " 対応括弧強調表示
set backspace=indent,eol,start " backspaceを有効化
set clipboard=unnamed,autoselect " ヤンクでクリップボードへ

" タブ設定
set expandtab     " ソフトタブ有効化
set tabstop=8     " タブ文字幅はスペース8つ相当
set softtabstop=4 " ソフトタブ幅はスペース4つ

" インデン
set autoindent   " 改行時自動インデント
set shiftwidth=4 " autoindent時の幅を4に

" Pythonの設定
autocmd FileType python setl smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class
" 改行時自動インデントする宣言
let python_highlight_all =1 " Python用のシンタックスハイライトを全てONに shutil
"""

dein = """\
[[plugins]]
repo = 'Shougo/dein.vim'

[[plugins]]
repo = 'Shougo/vimproc.vim'
build = 'make'

[[plugins]]
repo = 'scrooloose/nerdtree'

[[plugins]]
repo = 'davidhalter/jedi-vim'
on_ft = 'python'

[[plugins]]
repo = 'nvie/vim-flake8'
"""


if __name__ == '__main__':
    home = os.path.expanduser('~')
    vimrc_path = os.path.join(home, '.vimrc')
    with open(vimrc_path, 'w', encoding='utf-8') as file:
        file.write(vimrc)

    vim_path = os.path.join(home, '.vim')
    if not os.path.exists(vim_path):
        os.mkdir(vim_path)

    dein_path = os.path.join(vim_path, 'dein.toml')
    with open(dein_path, 'w', encoding='utf-8') as file:
        file.write(dein)
