##!/usr/bin/python3
"""
Author:YiYang.Dong
Purpose:the third experiment
Created:2/7/2020
"""
import multiprocessing
import time
def process_1(interval):
    print("子进程1")
    time.sleep(interval)
    print("子进程1结束")


def process_2(interval):
    print("子进程2")
    time.sleep(interval)
    print("子进程2结束")


def process_3(interval):
    print("子进程3")
    time.sleep(interval)
    print("子进程3结束")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=process_1, args=(1,))  # 睡眠1秒
    p2 = multiprocessing.Process(target=process_2, args=(2,))  # 睡眠2秒
    p3 = multiprocessing.Process(target=process_3, args=(3,))  # 睡眠3秒
    #启动子进程
    p1.start()
    p2.start()
    p3.start()
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))