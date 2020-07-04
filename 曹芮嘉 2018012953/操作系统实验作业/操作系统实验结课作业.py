##!/usr/bin/python3
"""
  Author:  RuiJia.Cao
  Purpose: Get all files and folders in a given file directory under the operating system.
  Created: 29/6/2020
"""
import os

def list(i):
    dir_files = os.listdir(i)

    for file in dir_files:
        file_path = os.path.join(i, file)
        if os.path.isfile(file_path):
            print(file_path)

        if os.path.isdir(file_path):
            list(file_path)
if __name__ == '__main__':
    dir_path =input('Enter your file path here:')
    list(dir_path)