'''
Author: Zhang yuxuan
purpose:  Get Documents
Date: 2020/6/30
'''


import os


def list_files(root):
    subdir = []
    lists = os.listdir(root)
    for i in range(0, len(lists)):
           paths = os.path.join(root, lists[i])
           if os.path.isdir(paths):
              subdir.extend(list_files(paths))
           if os.path.isfile(paths):
               subdir.append(paths)
    return subdir


lists = list_files('/1.py')
print(lists)