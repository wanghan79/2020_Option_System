#coding:utf-8
'''
    Author: Yy.Li
    Purpose:采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕；提示：采用Python内置工具包os.path
    Created:30/6/2020
'''

import os

# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# 输入文件夹路径、空文件列表[]
# 返回文件列表Filelist,包含文件名（完整路径）

def get_filelist(dir, Filelist):
    if os.path.isfile(dir):
        Filelist.append(dir)
        # 若只是要返回文件文，使用这个
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
                # continue
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist

if __name__ == '__main__':
    list = get_filelist('F:\\课程\\大二下\\操作系统', [])
    print("共有文件：")
    print(len(list))
    for i in list:
        print(i)