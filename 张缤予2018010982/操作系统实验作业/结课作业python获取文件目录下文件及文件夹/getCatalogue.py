# coding=utf-8
##!/usr/bin/python3
'''

Author: By.Zhang
Purpose: give a file directory and gets all files and folders by python.
Created: 28/6/2020

'''

import os


def get_Path(yourpath):
    # 所有文件
    file_list = []
    # 返回一个列表
    list = os.listdir(yourpath)
    for i in range(0, len(list)):
        newpath = os.path.join(yourpath, list[i])
        if os.path.isfile(newpath):
            file_list.append(newpath)
        if os.path.isdir(newpath):
            file_list.extend(get_Path(newpath))
    return file_list


file_list = []
file_list = get_Path("D:/OSexperience")
for i in file_list:
    print(i)
