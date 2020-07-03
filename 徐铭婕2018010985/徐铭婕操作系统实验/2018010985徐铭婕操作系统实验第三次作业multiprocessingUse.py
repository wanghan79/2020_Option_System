# encoding: utf-8
'''
Author :    xumingjie 
Purpose:   
Created:    2020/7/3 9:19
'''

from multiprocessing import Pool
import time
import os
import random


# 创建子进程函数
def run(name):
    print('子进程%s启动,进程号:%s' % (name, os.getpid()))
    # 为了验证进程执行数量可以采取随机停止时间
    # 记录开始时间
    start = time.time()
    time.sleep(random.choice(range(1, 4)))  # 随机停止1-3秒
    # 结束时间
    end = time.time()
    # 子进程结束标志
    print('子进程%s结束,子进程号:%s, 停留时间：%d' % (name, os.getpid(), end - start))


if __name__ == "__main__":
    # 主进程开始
    print('主进程启动')

    # 创建一个进程池,并设置最大同时执行数量
    p = Pool(5)

    # 开始创建子进程并启动
    for i in range(10):
        p.apply_async(run, args=(i,))

    p.close()  # 关闭进程池
    p.join()  # 合并父子进程让父进程在子进程运行完后结束

    # 主进程结束标志
    print('父进程结束')
