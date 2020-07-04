#coding:utf-8
'''
Description:Gets all the files and folders (including subfolders)
            in the given file directory and outputs them to the screen
Author:li tong

'''
import os

def get_file(path):
   file=[]
   file_list=os.listdir(path)#得到该文件夹下所有文件
   for index in file_list:
       file_path=os.path.join(path,index)#路径拼接成绝对路径
       if os.path.isfile(file_path):#如果是文件，就添加到列表file中
           file.append(file_path)
       elif os.path.isdir(file_path):#如果是子目录，就递归子目录
           file.extend(get_file(file_path))
   return file

if __name__ == '__main__':
    path=input()
    files=get_file(path)
    for index in files:
        print(index)