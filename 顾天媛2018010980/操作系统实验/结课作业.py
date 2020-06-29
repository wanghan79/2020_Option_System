# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: os.path
  Created: 29/6/2020
"""
# 结课作业：采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕；提示：采用Python内置工具包os.path
import os

def all_files_path(root_path):
    for root, dirs, files in os.walk(root_path):  # 分别代表根目录、文件夹、文件
        for file in files:  # 遍历文件
            file_path = os.path.join(root, file)  # 获取文件绝对路径
            filepaths.append(file_path)  # 将文件路径添加进列表
        for dir in dirs:  # 遍历目录下的子目录
            dir_path = os.path.join(root, dir)  # 获取子目录路径
            all_files_path(dir_path)  # 递归调用


if __name__ == "__main__":
    filepaths = []  # 初始化列表用来
    root_path = '../'
    all_files_path(root_path)
    for filepath in filepaths:
        print(filepath)
