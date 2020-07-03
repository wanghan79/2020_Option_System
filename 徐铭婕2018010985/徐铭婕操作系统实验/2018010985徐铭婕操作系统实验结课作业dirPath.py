# encoding: utf-8
"""
Author :    xumingjie
Purpose:
Created:    2020/7/3 10:32
"""

from pathlib import Path

srcPath = Path('D:\homeworktest')
allFn = []
allPath = [srcPath, ]
i = 1
while len(allPath) > 0:
    nowPath = allPath.pop()
    pathInfo = [(x, x.is_dir()) for x in nowPath.iterdir() if nowPath.is_dir()]
    for fn, isPath in pathInfo:
        print("正在寻找:", "<", str(i), ">", fn)
        if not isPath:
            print("找到新文件:", fn)
            allFn.append(fn)
        else:
            print("找到新目录:", fn)
            allPath.append(fn)
        i += 1
    print(nowPath, end="===>")
    print("寻找完毕")
print("寻找完毕,共{}个目录及文件".format(i))
