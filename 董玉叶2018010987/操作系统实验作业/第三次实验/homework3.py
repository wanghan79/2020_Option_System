"""
Author: YY.Dong
Purpose: Creating multiple processes
Created: 25/6/2020
"""
# -*- coding: utf-8 -*-
import os
from multiprocessing import Process
import time
#继承process类




def fun(name):
    print("2 子进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    print("hello " + name)


def test():
    print('ssss')


if __name__ == "__main__":
    print("1 主进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    ps = Process(target=fun, args=('dyy', ))
    print("111 ##### ps pid: " + str(ps.pid) + ", ident:" + str(ps.ident))
    print("3 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    print(ps.is_alive())
    ps.start()
    print(ps.is_alive())
    print("222 #### ps pid: " + str(ps.pid) + ", ident:" + str(ps.ident))
    print("4 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    ps.join()
    print(ps.is_alive())
    print("5 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    ps.terminate()
    print("6 进程信息： pid=%s, ppid=%s" % (os.getpid(), os.getppid()))

