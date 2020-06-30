# coding=utf-8
"""
  Author:  Jiang Eryu
  Purpose: 采用Python内置工具包os.path获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕
  Created: 30/6/2020
"""

# --------实验说明---------
# 采用Python内置工具包os.path获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕

import os


def print_list_dir(root_path):
    # 得到该路径下所有的文件
    dir_files = os.listdir(root_path)
    # 遍历根目录下所有文件/目录
    for f in dir_files:
        # 获取文件绝对路径
        file_path = os.path.join(root_path, f)
        # 如果是文件，直接输出
        if os.path.isfile(file_path):
            print(file_path)
        # 如果是目录，则递归子目录
        if os.path.isdir(file_path):
            print_list_dir(file_path)


if __name__ == '__main__':
    dir_path = 'input your path here'  # 键入要输出的文件夹路径
    print_list_dir(dir_path)
