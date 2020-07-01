"""
Author: YY.Dong
Purpose: Obtain all the files and folders (including sub folders) under the given file directory under the operating system
        and output them to the screen;
Created: 25/6/2020

"""
# -*- coding: utf-8 -*-
import os

#os.listdir(path)是得到在path路径下所以文件的名称列表
#open(path)
#是打开某个文件。

#iter是python的迭代器。

#所以读取某文件夹下的所有文件如下：
def get_file():
    path = "D:\董玉叶\\2020春天\算法"
    # 文件夹目录
    if os.path.exists(path):
        #files = os.listdir(path)  # 得到文件夹下的所有文件名称

        filenum=0
        for root, dirs, files in os.walk(path,topdown=True):#从top开始
                print('路径:',os.path.dirname(root),'\\',os.path.basename(root))  # 当前目录路径
                print('名称:',os.path.basename(root))

                for file in files:
                    print(os.path.basename(file))  # 当前路径下所有文件
                    filenum+=1
        print("共有子文件数目:",filenum)
    else:
        print("不含此文件夹,重新修改~")
if __name__ == '__main__':

    print("此文件下的文件：")
    get_file()

