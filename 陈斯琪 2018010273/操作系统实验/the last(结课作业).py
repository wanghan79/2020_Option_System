##!/usr/bin/python3
# """
#   Author:  Sq.Chen
#   Purpose: Get all files and folders (including subfolders) under the given file directory
#   Created: 27/6/2020
# """

import os

def get_all_path(file_path):
    rootdir = file_path
    path_list = []
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        com_path = os.path.join(rootdir, list[i])
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    for i in path_list:
        print(i)
    return path_list

get_all_path("./")
