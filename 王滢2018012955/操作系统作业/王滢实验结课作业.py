import os
def print_list_dir(dir_path):
    dir_files = os.listdir(dir_path)  # 得到该文件夹下所有的文件
    for file in dir_files:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            print(file_path)
        if os.path.isdir(file_path):  # 如果目录，就递归子目录
            print_list_dir(file_path)
if __name__ == '__main__':
    dir_path ='D:\PyCharm\code'
    print_list_dir(dir_path)