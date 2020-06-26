"""
Author: ShuMing.Bai
Purpose: First: Get operating system information using package platform
Created: 6/24/2020
"""
from multiprocessing import Process
from multiprocessing import Pool
from random import random
import threading
import time,os


# 方法一：直接传入要运行的方法
def foo(i):
    print('say hi', i)

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.start()


# 方法二：从Process继承并覆盖run()
# class MyProcess(Process):
#     def __init__(self, arg):
#         super(MyProcess, self).__init__()
#         self.arg = arg
#
#     def run(self):
#         print('say hi', self.arg)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = MyProcess(i)
#         p.start()


# 方法三：用Pool类实现非阻塞式进程

# def task(task_name):
#     print('开始做任务啦!',task_name)
#     start = time.time()
#     # 使用sleep
#     time.sleep(random() * 2)
#     end = time.time()
#     print('完成任务:{}! 耗时:{} ,进程ID:{}'.format(task_name,(end-start),os.getpid()))
#
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     tasks = ['1','2','3','4','5','6','7']
#     for t in tasks:
#         pool.apply_async(task, args=(t,))
#     pool.close() # 关闭进程池，不允许继续添加进程
#     pool.join() # 等待进程池中的所有进程结束
#     print('------'*10)
#     print('over!!!!!!!!!!')
