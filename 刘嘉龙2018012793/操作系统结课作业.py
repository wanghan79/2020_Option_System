# -*- coding:utf8 -*-
import os
class ScanFile(object):
    def __init__(self, directory, prefix=None, postfix=None):
        self.directory = directory
        self.prefix = prefix
        self.postfix = postfix

    def scan_files(self):
        files_list = []
        for dirpath, dirnames, filenames in os.walk(self.directory):
            '''''
            dirpath is a string, the path to the directory.
            dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..').
            filenames is a list of the names of the non-directory files in dirpath.
            '''
            for special_file in filenames:
                if self.postfix:
                    if special_file.endswith(self.postfix): # 判断一个字符的结尾是否是某字符   Python 内置函数 endswith（）
                        files_list.append(os.path.join(dirpath, special_file))
                elif self.prefix:
                    if special_file.startswith(self.prefix): # 判断一个字符的开始是否是某字符   Python 内置函数 endswith（）
                        files_list.append(os.path.join(dirpath, special_file))
                else:
                    files_list.append(os.path.join(dirpath, special_file))

        return files_list

    def scan_subdir(self):
        subdir_list = []
        for dirpath, dirnames, files in os.walk(self.directory):
            subdir_list.append(dirpath)
        return subdir_list


if __name__ == "__main__":
    dir = r"/home/djl/project/s" #需要扫描的文件路径
    scan = ScanFile(dir, postfix=".py")
    subdirs = scan.scan_subdir()
    files = scan.scan_files()

    print ("扫描的子目录是:")
    for subdir in subdirs:
        print (subdir)

    print ("扫描的文件是:")
    for file in files:
        print (file)

    print ('--------------------------')
    print (files)
    print ('--------------------------')
