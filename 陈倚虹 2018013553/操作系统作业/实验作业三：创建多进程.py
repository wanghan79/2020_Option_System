# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Use multiprocessing package to create multiprocessing.
    Created: 24/6/2020
"""

import multiprocessing as mul
from multiprocessing import Process
import os


# 进程信息输出函数
def info(title):
    print(title)
    # 输出进程名称
    print('module name:', __name__)
    # 输出进程号
    print('process id:', os.getpid())


# 进程对应打印输出函数
def process(name):
    # 调用info()函数输出进程信息
    info('function process')
    print('hello', name)
    print('=' * 50)


if __name__ == '__main__':
    info('main line')
    print('=' * 50)

    # 利用缓冲池创建多进程
    pool = mul.Pool(5)
    rel = pool.map(process, ['Wayne', 'Grayson', 'Jason', 'Drake', 'Damian'])

    p = Process(target=process, args=(rel,))
    p.start()
    p.join()
