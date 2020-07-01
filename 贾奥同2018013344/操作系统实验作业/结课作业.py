import os

def show_files(path,n):#path是文件夹的绝对路径，n是前面需要缩进的行数
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            for i in range(n):
                print(end='\t')
            print(cur_path)
            show_files(cur_path,n+1)
        else:
            for i in range(n):
                print(end='\t')
            print(file)

# 传入空的list接收文件名
contents = show_files("D:\极速下载",0)
