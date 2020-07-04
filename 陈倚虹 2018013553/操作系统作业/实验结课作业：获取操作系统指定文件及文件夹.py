# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Use os.path to get the special files on OperaSystem.
    Created: 27/6/2020
    Finished: 29/6/2020
"""

import os


# 定义文件输出函数
def print_files(path):
    # 定义counter计数器变量，用于计算‘path’路径下的所有子文件的数量
    i = 0

    # 利用os.walk()方法遍历‘path’路径下的所有文件及文件夹（包括子文件夹）
    # topdown为True表示优先从top文件开始便利，再便利子文件夹和子文件
    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        # 定义counter计数器变量，用于计算子文件夹下的所有文件的数量
        j = 0
        # 输出当前文件路径
        print('文件路径：' + os.path.dirname(dirpath) + '\\' + os.path.basename(dirpath))
        # 输出当前文件夹名称
        print('文件夹名：' + os.path.basename(dirpath))

        # 便利文件夹中的所有子文件
        for filename in filenames:
            # 打印第j个子文件的名称
            print('子文件', j, '：' + os.path.basename(filename))
            j = j + 1
            i = i + 1
        # 当该目录下存在子文件（不含子文件夹）时，输出子文件的个数
        if j != 0:
            print('该目录下共有', j, '个子文件')
        print('-' * 50)
    # 输出‘path’路径下的所有子文件的数量
    print('该目录', path, '下共有', i, '个子文件')


# 主函数，调用print_files函数
if __name__ == '__main__':
    # 定义要查询的文件路径（可为绝对/相对路径）
    files_path = '..\main'

    # 若存在‘files_path’路径，调用函数print_files
    if os.path.exists(files_path):
        # 打印给定文件目录下的所有文件及文件夹（包括子文件夹）
        print_files(files_path)
    # 否则输出错误提示信息
    else:
        print('没有找到该文件路径，请确认输入路径是否有误！')
