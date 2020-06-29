# !/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
  Author:  Ty.Gu
  Purpose: random data set & MongoDB
  Created: 26/6/2020
"""
# 作业3. 采用Python语言创建多进程；提示：采用Python内置工具包multiprocessing

from multiprocessing import Pool
import time, os
from random import random


def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务:{}! 耗时:{} ,进程ID:{}'.format(task_name, (end - start), os.getpid()))


# 容器
container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '看电影', '读书', '看报', '玩游戏', '打篮球', '弹钢琴']
    for t in tasks:
        pool.apply_async(task, args=(t,))

    pool.close()  # 关闭进程池，不允许继续添加进程
    pool.join()  # 等待进程池中的所有进程结束

    print('------' * 10)
    for c in container:
        print(c)

    print('over!!!!!!!!!!')
