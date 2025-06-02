#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
import shutil
import sys
import glob
from itertools import zip_longest
from collections import namedtuple

def get_args(args=None):
    parser = argparse.ArgumentParser(description="repos-dir")
    parser.add_argument("--repos", type=str, default=None) # VPATH
    parser.add_argument("-f", "--force", action="store_true", help="force operation")
    parser.add_argument("-N", "--not_add", action="store_true", help="not add/commit")

    args = parser.parse_args(args)
    args.repos = os.path.abspath(args.repos)
    return args;


def move_to_base_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)


def _subprocess_run(cmd):
    print("executing ", cmd)

    # subprocess.run()を使ってコマンドを実行し、標準出力をキャプチャ
    result = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # 標準出力を改行で分割してリストに変換
    output_lines = result.stdout.splitlines()
    
    return output_lines



Docs = namedtuple('Docs', ['key', 'ext', 'src_dir'])  # keyは保存dir名にも使用する

_DOCS_EXT = [Docs("md", "md", "o"), Docs("html", "html", "o"), Docs("md_pu", "md", "o/pu")]


def get_sh1(repos_dir):
    cmd = f"git -C {repos_dir} log -1 --pretty=format:%h"
    return _subprocess_run(cmd)[0]

def get_version_on_msg(repos_dir):
    cmd = f"git -C {repos_dir} log -1 --pretty=format:%s"
    ci_msg = _subprocess_run(cmd)
    return ci_msg[0].split()[1]


def get_version_from_file(dir):
    contents = ""

    with open(f"{dir}/version.txt", 'r', encoding='utf-8') as file:
        contents = file.read()

    return contents.rstrip()

def get_repos_name(dir):
    # remote 
    cmd = f"git -C {dir} config --get remote.origin.url"

    repos_url = _subprocess_run(cmd)

    repos_name = os.path.basename(repos_url[0])
    
    if repos_name.endswith('.git'):
        return repos_name[:-4]
    else:
        return None


class ReleasedRepos:
    def __init__(self, repos_dir):
        self._dir = repos_dir
        self._sh1 = get_sh1(repos_dir)
        self._version_on_msg = get_version_on_msg(repos_dir)
        self._repos_name =  get_repos_name(repos_dir)
        self._version_on_file = get_version_from_file(repos_dir)

    @property
    def dir(self):
        return self._dir

    @property
    def sh1(self):
        return self._sh1

    @property
    def version_on_msg(self):
        return self._version_on_msg

    @property
    def version_on_file(self):
        return self._version_on_file

    @property
    def repos_name(self):
        return self._repos_name

    def __str__(self):
        return f"{self.sh1} {self.version_on_msg} {self.repos_name} {self._version_on_file}"

def copy_files_to_docs(src_docs, to_dirs):
    for docs in _DOCS_EXT:
        for file in src_docs[docs.key]:
            print(docs.key, "-", file, to_dirs[docs.key])
            shutil.copy(file, to_dirs[docs.key])


def make_log(released_repos: ReleasedRepos):
    log_dir = os.path.join(released_repos.repos_name, released_repos.version_on_file) 
    log_file = os.path.join(log_dir, "sh1.txt")

    with open(log_file, 'w') as file:
        file.write(released_repos.sh1)

def git_add_ci(released_repos: ReleasedRepos):
    cmd = f"git add ."
    _subprocess_run(cmd)

    cmd = f"git commit -m '{released_repos.repos_name}({released_repos.version_on_file})'"
    _subprocess_run(cmd)



def _main():
    opt = get_args()

    released_repos = ReleasedRepos(opt.repos)

    move_to_base_dir()

    print(released_repos)

    if not opt.force:
        if not released_repos.version_on_msg == released_repos.version_on_file:
            raise Exception(f"{released_repos.dir} released imcompltely !!!")

    to_dirs = generate_dir(released_repos.repos_name, released_repos.version_on_file)

    all_docs = get_all_docs(released_repos.dir)

    copy_files_to_docs(all_docs, to_dirs)

    make_log(released_repos)

    if not opt.not_add:
        git_add_ci(released_repos)

def get_all_docs(dir):

    all_docs = {docs.key: [] for docs in _DOCS_EXT}

    for docs in _DOCS_EXT:
        src_dir = os.path.join(dir, docs.src_dir) 
        files_to_copy = glob.glob(os.path.join(src_dir, f'*.{docs.ext}'))
        if len(files_to_copy) == 0 :
            raise Exception(f"There is no *.{docs.ext} in {src_dir} !!!:")

        all_docs[docs.key] = files_to_copy

    return all_docs


def generate_dir(repos_name, version):
    if not os.path.isdir(repos_name):
        os.makedirs(repos_name)

    version_dir = os.path.join(repos_name, version)
    os.makedirs(version_dir, exist_ok=True)

    gen_dirs = [os.path.join(version_dir, docs.key) for docs in _DOCS_EXT]

    keys = [docs.key for docs in _DOCS_EXT]

    for dir in gen_dirs:
        os.makedirs(dir)

    contents_dirs = {}

    for item1, item2 in zip_longest(keys, gen_dirs):
        contents_dirs[item1] = item2
        
    return contents_dirs


if __name__ == "__main__":
    _main()
