#结课作业：采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕；
# 提示：采用Python内置工具包os.path


#os.walk()
import os
filePath = 'D:\作业库'
for i,j,k in os.walk(filePath):
    print(i,j,k)

#os.listdir()

import os
filePath = 'D:\作业库'
print(os.listdir(filePath))
#-----------------------------------------
import os
path = 'D:\作业库' #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          f = open(path+"/"+file); #打开文件
          iter_f = iter(f); #创建迭代器
          str = ""
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              str = str + line
          s.append(str) #每个文件的文本存到list中
print(s) #打印结果
