#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 16:58
# @Author  : liyuhan
# @File    : finaltest.py
"""
Author:liyuhan
Purpose:采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕；提示：采用Python内置工具包os.path
Created:2020
"""
import os

def get_file(path):
    path_list = []
    list = os.listdir(path)
    for i in range(0, len(list)):
        re_path = os.path.join(path, list[i])
        #获取当前文件夹下的文件
        if os.path.isfile(re_path):
            path_list.append(re_path)
        #调用get_file迭代获取文件夹中子文件夹中的文件
        if os.path.isdir(re_path):
            path_list.extend(get_file(re_path))
    return path_list

if __name__ == '__main__':
    #给定文件目录
    scanf_path=('E:\wyf')
    print(get_file(scanf_path))