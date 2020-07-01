import os

def get_all_files(dir):
    files_ = []
    list_ = os.listdir(dir)
    for i in range(0, len(list_)):
        path = os.path.join(dir, list_[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_


if __name__ == '__main__':
    filelist = []      #定义存储文件
    filelist = get_all_files("D:\python")
    for i in filelist:
        print(i)
