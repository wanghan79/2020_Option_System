"""
Author:Chenjiaying
Purpose:采用Python语言创建多进程
Created:1/7/2020
"""
from multiprocessing import Process
import time


def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = Process(target=f, args=('reid',))  # 创建一个进程对象,再传入一个函数f为参数
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    print('end')