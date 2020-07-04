"""
    Author: Dd.Li
    Purpose: 采用Python语言创建多进程
    Created: 3/7/2020
"""

import os
import time
from multiprocessing import Pool


def run(arg):
    print("子进程开始执行>>> pid={}, ppid={}, 编号{}".format(os.getpid(), os.getppid(), arg))
    time.sleep(0.5)
    print("子进程终止>>> pid={}, ppid={}, 编号{}".format(os.getpid(), os.getppid(), arg))


def main():
    print("主进程开始执行>>> pid={}".format(os.getpid()))
    p = Pool(5)                             # 利用进程池Pool创建多进程
    for i in range(10):
        p.apply(run, args=(i, ))            # 同步执行
        # p.apply_async(run, args=(i, ))    # 异步执行

    p.close()                               # 关闭进程池，停止接受其它进程
    p.join()                                # 阻塞进程
    print("主进程终止")

if __name__ == '__main__':
    main()