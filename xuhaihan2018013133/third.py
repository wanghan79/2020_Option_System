# coding=utf-8
"""
  Author:  XHH
  Purpose: 采用Python语言创建多进程
  Created: 1/7/2020
"""

from multiprocessing import Process
import os
import time

def pr1(process_name):
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(2)

def pr2(process_name):
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(2)

if __name__ == "__main__":
    # target:指定进程执行的函数
    # args:传入target参数对应函数的参数，需要使用tuple
    print("main process run...")    # 主进程运行
    # 创建子进程
    p1 = Process(target=pr1, args=('process_name1',))
    p2 = Process(target=pr2, args=('process_name2',))
    # 子进程运行
    p1.start()
    p2.start()
    # 子进程阻塞
    p1.join()
    p2.join()
    print("main process ran all lines...")  # 主进程结束
