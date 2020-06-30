# -*-coding:utf-8 -*-
"""
    Author:W
    Purpose:
    Created:2020-6-26
"""
from multiprocessing import Process
import time


def create1():
    start = int(time.time())
    print("子进程（一）开始时间为：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start)))
    for i in range(1, 11):
        print("运行子进程（一）" + str(i) + "次")
        time.sleep(1)
    end = time.time()
    print("子进程（一）结束时间为：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end)))
    print("子进程（一）用时" + str(end - start))


def create2():
    start = int(time.time())
    print("子进程（二）开始时间为：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start)))
    for i in range(1, 11):
        print("运行子进程（二）" + str(i) + "次")
        time.sleep(2.5)
    end = time.time()
    print("子进程（二）结束时间为：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end)))
    print("子进程（二）用时" + str(end - start))


if __name__ == '__main__':
    p1 = Process(target=create1)
    p2 = Process(target=create2)

    p1.start()
    p2.start()
