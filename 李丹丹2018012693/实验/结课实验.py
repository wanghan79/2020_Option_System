"""
    Author: Dd.Li
    Purpose: 采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹）
    Created: 4/7/2020
"""
import os

def printPath(path):
    fileNum = 0
    for root, dirs, files in os.walk(path):
        print('当前文件夹路径:', root)
        print('该路径下的文件夹：', dirs)
        print('子文件：', files)
        print("该文件夹下有", len(files), "个文件")
        fileNum = fileNum + len(files)
        print('-'*80)
    return fileNum


if __name__ == '__main__':
    Path = 'C:\操作系统'
    num = printPath(Path)
    print("共有文件：", num)