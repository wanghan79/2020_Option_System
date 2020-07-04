'''
Author: YixuanLiu
purpose: python实现windows命令调用
Data: 2020/6/28
'''

import os
from os import path

def pathScreening(path):
    for path, sublist, file in os.walk(path):
        for i in file:
            print(os.path.abspath(i))

pathScreening(r"C:\Users\think\Desktop\学习文件\浏览器及不常用软件")