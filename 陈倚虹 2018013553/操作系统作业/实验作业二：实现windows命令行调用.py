# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Use os.system to call the command of Windows.
    Created: 24/6/2020
"""

import os


def read_file():
    # 执行Windows命令之读文件
    a = os.system(r"d:\test.py")

    # 执行结果
    print(a)


def create_file():
    """
    在/usr/local目录下创建文件‘aaa.txt’,
    在使用os.system()执行多条指令时，必须将指令放在同一个子进程中
    """
    os.system('mkdir bbb')  # 在当前目录下创建文件
    os.system('cd /usr/local ; mkdir aaa.txt')


def install_package():
    # 批量安装python第三方库，可大大提升安装效率，实现自动化安装
    libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "jieba", "beautifulsoup4", "wheel", "networkx", "sympy", "pyinstaller", "django", "flask", "werbot", "pyQt5", "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}
    try:
        for lib in libs:
            os.system("pip install "+lib)
        print("Successful")
    except:
        print("Failed Somehow")


if __name__ == '__main__':
    read_file()
    create_file()
