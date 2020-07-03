"""
Author:JLH2018010984
Created:2020/6/30
"""
#######################################
import os

def print_line():
    print("*" * 60)
print_line()

def get_path(root_path):
    for root, files,dir_files in os.walk(root_path):
        for dir_file in dir_files:
            dir_path = os.path.join(root, dir_file)
            get_path(dir_path)
        for file in files:
            file_path = os.path.join(root, file)
            file_lists.append(file_path)

if __name__ == "__main__":
    root_path = r"D:\work"
    file_lists = []
    get_path(root_path)
    for file_list in file_lists:
        print(file_list)
print_line()