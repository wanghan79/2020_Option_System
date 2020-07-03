##!/usr/bin/python3
"""
Author:YiYang.Dong
Purpose:the forth experiment
Created:2/7/2020
"""
import os
def findlistdir(dirpath):
    dir_files = os.listdir(dirpath)
    for file in dir_files:
        file_path = os.path.join(dirpath, file)
        if os.path.isfile(file_path):
            print(file_path)
        if os.path.isdir(file_path):# 如果是文件夹，递归子目录
            findlistdir(file_path)
if __name__ == '__main__':
    dir_path =input('在这里输入您的文件路径:')
    findlistdir(dir_path)