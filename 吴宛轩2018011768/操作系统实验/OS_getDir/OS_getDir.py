# -*-coding:utf-8 -*-
"""
    Author:W
    Purpose:
    Created:2020-6-26
"""
import os


class getAllFile:

    def getDir(self, path):
        dirs = []
        '''获取文件目录（列表）'''
        pathDirs = os.listdir(path)
        for i in range(0, len(pathDirs)):
            p = os.path.join(path, pathDirs[i])
            '''判断是目录还是文件，若是目录则继续向下寻找，若是文件则添加到路径中'''
            if os.path.isdir(p):
                dirs.extend(self.getDir(p))
            if os.path.isfile(p):
                dirs.append(p)
        return dirs


if __name__ == '__main__':
    dirlist = getAllFile().getDir("D:\hengzhi")
    sum = 0
    for i in dirlist:
        print(i)
        sum += 1
    print("共有" + str(sum) + "个文件")
