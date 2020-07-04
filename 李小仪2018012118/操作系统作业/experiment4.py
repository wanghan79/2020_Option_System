##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:Get all files and folders under the file directory
      Created:3/7/2020
"""
import os
from pip._vendor.distlib.compat import raw_input

allFileNum = 0
def printPath(level,path):
    global allFileNum
    fileList = []
    files = os.listdir(path)
    for f in files:
        if(os.path.isdir(path + '/'+ f)):
            if(f[0]!='.'):
              print('-'*level,f)
              print((level + 1),path + '/' + f)
            if(os.path.isfile(path + '/'+f)):
                 fileList.append(f)
            for fl in fileList:
               print('-'*level,fl)
    allFileNum  = allFileNum +1
    print('Please enter the directory path you want to list all file info:')
    yourPath = raw_input()

if __name__=='__main__':
    printPath(level = 1,path = 'C:/Users/lxy/PycharmProjects')
    print('总文件数=',allFileNum)
