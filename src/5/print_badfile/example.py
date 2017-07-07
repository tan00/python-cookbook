#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 打印不合法文件名
Desc : 
"""
import os
import sys
import io

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

os.chdir( cur_file_dir() )

def bad_filename(filename):
        return repr(filename)[1:-1]


def bad_filename2(filename,encoding = 'utf-8'):
    """完美方案"""
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode(encoding)


def print_badfile(filename,encoding = 'utf-8'):
    try:
        print(filename)
    except UnicodeEncodeError:
        print('UnicodeEncodeError')
        print(bad_filename2(filename,encoding))

    files = os.listdir('.')
    print(files)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
print( sys.stdout.encoding )

print_badfile('bäd.txt','utf-8')