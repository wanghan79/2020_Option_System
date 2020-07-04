"""
    Author: Dd.Li
    Purpose: 采用python语言实现windows命令行调用
    Created: 3/7/2020
"""

import os

def call():
    # 调用命令行
    os.system('cmd')
    # Window IP配置
    os.system('ipconfig')
    # 打开QQ
    os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQScLauncher.exe')


def install_package():

    lib = {"matplotlib", "numpy", "openpyxl", "pandas", "pymongo", "xlrd"}
    for item in lib:
        os.system("pip install " + item)
    print("Successful")


if __name__ == '__main__':
    call()
    install_package()   # 批量安装python标准库