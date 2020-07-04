"""
    Author:
        BowenCao
        2018013070

    Purpose:
        采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕

    Created: 25/6/2020
"""
import os

allFileNum = 0

def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 用于存储所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 用于存储所有文件
    fileList = []
    # 返回一个列表，其中包含在path目录里的文件和文件夹的名字
    files = os.listdir(path)
    # 给目录添加级别
    dirList.append(str(level))
    for f in files:
        # 判断path + '/' + f是否为目录
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        # 判断path + '/' + f是否为文件
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    # print(dirList)
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print("   "*(int(dirList[0])-1),"第",(int(dirList[0])),"级", dl)
            # 递归调用printPath 打印目录下的所有文件夹和文件，每次调用目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print("   "*(int(dirList[0])-1),"第",(int(dirList[0])),"级", fl)
        # 计算一下有多少个文件
        allFileNum = allFileNum + 1


if __name__ == '__main__':
    #此处可更改路径
    printPath(1, 'E:\python')
    print('总文件数 =', allFileNum)
