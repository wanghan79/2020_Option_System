'''
Author: WeiFan 2018011641
Aim: 采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕。
Data: 2020/6/28
'''
import os

path = "D:\四六级文件"  # 文件夹路径

def get_dir(path):  # 获取目录路径
    for root, dirs, files in os.walk(path):
        # 遍历path,进入每个目录都调用visit函数，，有3个参数，root表示目录路径，dirs表示当前目录的目录名，files代表当前目录的文件名
        for dir in dirs:
            # print(dir)             #文件夹名
            print(os.path.join(root, dir))  # 把目录和文件名合成一个路径

def get_file(path):  # 获取文件路径
    for root, dirs, files in os.walk(path):
        for file in files:
            # print(file)     #文件名
            print(os.path.join(root, file))

get_dir(path)
get_file(path)
