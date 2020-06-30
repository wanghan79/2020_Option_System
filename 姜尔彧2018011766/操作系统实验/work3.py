# coding=utf-8
"""
  Author:  Jiang Eryu
  Purpose: 采用Python内置工具包multiprocessing创建多进程
  Created: 30/6/2020
"""

# --------实验说明---------
# 采用Python内置工具包multiprocessing创建多进程
# 创建函数并将其作为多个进程

import multiprocessing
import time


def worker_1(interval):
    print "worker_1"
    time.sleep(interval)  # 睡眠2秒，阻塞状态
    print "end worker_1"


def worker_2(interval):
    print "worker_2"
    time.sleep(interval)  # 睡眠3秒，阻塞状态
    print "end worker_2"


def worker_3(interval):
    print "worker_3"
    time.sleep(interval)  # 睡眠5秒，阻塞状态
    print "end worker_3"


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker_1, args=(2,))  # 睡眠2秒
    p2 = multiprocessing.Process(target=worker_2, args=(3,))  # 睡眠3秒
    p3 = multiprocessing.Process(target=worker_3, args=(5,))  # 睡眠5秒

    #启动子进程
    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"


