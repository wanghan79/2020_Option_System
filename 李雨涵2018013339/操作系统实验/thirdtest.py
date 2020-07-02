#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 17:24
# @Author  : liyuhan
# @File    : thirdhw.py
"""
Author:liyuhan
Purpose: 采用Python语言创建多进程；提示：采用Python内置工具包multiprocessing
Created:2020
"""
import time
from multiprocessing import Process

def process(i):
    #沉睡两秒
    time.sleep(2)
    print('进程',i)


if __name__ == '__main__':
    process_list = []
    # 循环创建3个子进程
    for i in range(3):
        p = Process(target=process, args=(i+1,))
        process_list.append(p)

    # 依次启动进程
    process_list[0].start()
    process_list[1].start()
    process_list[2].start()