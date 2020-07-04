# python3
# coding=utf-8
"""
  Author:  Tanlin
  Purpose: 操作系统实验结课作业：采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕；提示：采用Python内置工具包os.path
  Created: 2020.6.28
"""
import os

def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            print('文件: %s' % tmp_path)
        else:
            print('文件夹：%s' % tmp_path)
            traverse(tmp_path)

path = 'D:\B207\python3\work1\work2'
traverse(path)