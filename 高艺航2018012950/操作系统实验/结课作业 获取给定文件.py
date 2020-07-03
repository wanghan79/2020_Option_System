"""
Author   :  Yihang.Gao  高艺航
StuNumber: 2018012950
Purpose  : Get files in directory.
Created  : 1/7/2020
"""

import os

def list_path(path):
    get_list = []
    list_part = os.listdir(path)
    for i in range(0, len(list_part)):
        upd_path = os.path.join(path, list_part[i])
        if os.path.isfile(upd_path):
            get_list.append(upd_path)
        if os.path.isdir(upd_path):
            get_list.extend(list_path(upd_path))
    return get_list
path = input('Please input path.')
get_list = []
get_list = list_path(path)
print(get_list)