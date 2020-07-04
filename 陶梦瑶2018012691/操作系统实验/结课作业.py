import os

def printPath(path):
    for root, dirs, files in os.walk(path):
        print('文件夹的路径:', root)
        print('文件价的名字：', dirs)
        print('子文件的名字：', files)

if __name__ == '__main__':
    path = 'C:\Drivers'
    files = []
    dirs = []
    printPath(path)





