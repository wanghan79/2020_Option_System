##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
  Author:  ZhengPeng.Han
  Purpose: Gets the names of all files and folders in the given file directory by a built-in function of python,which named os.path.
  Created: 26/6/2020
"""
import os
path = 'D:\VIPworks'
# 回调函数
def find_file(arg, dirname, files):
    for file in files:
        file_path = os.path.join(dirname, file)
    if os.path.isfile(file_path):
        print("找到文件:%s" % file_path)

# 调用
print('%s下的所有文件和文件夹为：' %path)
os.path.walk("D:\VIPworks", find_file, ())




'''
#有另外的一个不使用os.path.walk的办法是使用os.walk遍历目录
import os
def file_name_walk(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("root", root)  # 当前目录路径
        print("dirs", dirs)  # 当前路径下所有子目录
        print("files", files)  # 当前路径下所有非目录子文件

file_name_walk("D:\VIPworks")

#os.listdir()方法可以返回指定路径下所有的文件和文件夹列表,但是子目录下文件不遍历。
def file_name_listdir(file_dir):
    for files in os.listdir(file_dir):
        print("files", files)
file_name_listdir("D:\VIPworks")
'''
