'''
Author: YixuanLiu
purpose: python语言创建多进程
Data: 2020/6/28
'''

import os, time
from multiprocessing import Process

def func(ii):
    for i in range(10):
        print("{}:{}".format('this is ',i))
        time.sleep(0.1)

if __name__ == '__main__':
    start = time.time()
    exp = Process(target=func, args=('111',))
    exp.start()
    for i in range(10):
        print('subStread   ',end='')
        time.sleep(0.1)
    end = time.time()
    time.sleep(2)
    print("whole program costs ",end - start)