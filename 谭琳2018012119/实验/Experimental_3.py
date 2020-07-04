# python3
# coding=utf-8
"""
  Author:  Tanlin
  Purpose: 操作系统实验作业3. 采用Python语言创建多进程；提示：采用Python内置工具包multiprocessing
  Created: 2020.6.28
"""
import os
from multiprocessing import Process

def func():
    print("子进程pid：%s,父进程pid：%s"%(os.getpid(),os.getppid()))     # os模块的getpid方法可以获取当前进程的pid，getppid方法可以获取当前进程的父进程的pid

if __name__ == '__main__':
    p_l = []
    # 创建多个进程
    for i in range(10):
        p = Process(target=func)
        p.start()
        p_l.append(p)

    # 异步执行子进程，最后执行主进程中的代码
    for p in p_l:
        p.join()   # 阻塞，使主进程等待子进程结束
    print("------主进程------")