# coding=utf-8
"""
  Author:  XHH
  Purpose: 采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹）
  Created: 1/7/2020
"""

import os

def getPath(filePath):
    rootdir = filePath
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            print(path)
        if os.path.isdir(path):
            getPath(path)

if __name__ == '__main__':
    file_path = input('please input the correct path:\n')
    getPath(file_path)