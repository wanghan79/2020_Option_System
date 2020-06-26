"""
Author: ShuMing.Bai
Purpose: Final Work: Gets all files and folders under a given file directory under the operating system
Created: 6/26/2020
"""
import os


def list_all_files(rootdir):
    files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            files.extend(list_all_files(path))
        if os.path.isfile(path):
            files.append(path)
    return files


file_list = []
file_list = list_all_files("F:/PythonProgram/homework")
for i in file_list:
    print(i)
