__author__ = '2018013343'
"""
Author: sun hejian
Purpose: get documents
Created: 30/6/2020
"""
import os
import os.path

# 当前文件所在文件夹的绝对路径
my_path = os.path.dirname(__file__)
print(my_path)

# 当前文件所在文件夹的上一级的绝对路径
path = os.path.dirname(os.path.dirname(__file__))
print(path)


for root, dirs, files in os.walk(path):
   for file in files:
      print (os.path.join(root, file))