import os


def seek(dir):
    dirs = os.listdir(dir)
    for i in dirs:
        if os.path.isdir(i):
            print(os.path.abspath(dir) + '\\' + os.path.relpath(i) + '\\')
            seek(i)
        else:
            print(os.path.abspath(dir)+'\\'+os.path.relpath(i))


seek(os.curdir) # 查找当前目录
