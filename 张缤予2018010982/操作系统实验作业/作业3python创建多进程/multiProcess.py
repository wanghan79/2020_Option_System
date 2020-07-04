# coding=utf-8
'''

Author: By.Zhang
Purpose: create multiprocess by python.
Created: 28/6/2020

'''
from multiprocessing import Process
from multiprocessing import Pool
import time
import os
import random


# --------创建函数并将其作为单个进程。--------
# 通过Multiprocessing模块中的Process类，创建Process对象
# 通过对象参数target="需要执行的子进程"
# def pro1(interval):
#     for i in range(3):
#         print("子进程", i)
#         print("The time is {0}".format(time.ctime()))
#         time.sleep(interval)
#
#
# if __name__ == "__main__":
#     p = Process(target=pro1, args=(2,))
#     p.start()
#     p.join()  # 加入该语句是等子进程结束后再执行下面代码
#     print("执行主进程内容")
#     print("p.pid:", p.pid)
#     print("p.name:", p.name)
#     print("p.is_alive:", p.is_alive())


# -------子类创建进程-------
# 通过继承Process类创建子进程，并进行重写
# class newProcess(Process):
#     # 继承Process类，必须要调用Process中的init初始化参数，
#     def __init__(self, interval):
#         Process.__init__(self)
#         self.interval = interval
#
#     # 重写run方法
#     def run(self):
#         for i in range(3):
#             print("子进程", i)
#             print("The time is {0}".format(time.ctime()))
#             time.sleep(self.interval)
#
#
# if __name__ == "__main__":
#     p = newProcess(1)
#     p.start()
#     print("执行主进程")


# -------使用进程池（非阻塞）-------
# Pool可以提供指定数量的进程，供用户调用
# def pro2(msg):
#     print("msg start:", msg)
#     start_time = time.time()
#     time.sleep(random.random())
#     end_time = time.time()
#     print('msg end:{} cost time:{} pid:{}'.format(msg, (end_time - start_time), os.getpid()))
#     print('\n')
#
#
# if __name__ == "__main__":
#     pool = Pool(processes=3)
#     for i in range(4):
#         msg = "子进程 %d" % i
#         # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#         pool.apply_async(pro2, (msg, ))
#
#     print("~~~~~~~~~~~~~~~~~~")
#     pool.close()  # 关闭进程池，不允许继续添加进程
#     pool.join()
#     print("All processes done.")


# -------使用进程池（阻塞）--------
def pro3(msg):
    print("%s start:" % msg)
    start_time = time.time()
    time.sleep(random.random()*3)
    end_time = time.time()
    print('msg end:{} cost time:{} pid:{}'.format(msg, (end_time - start_time), os.getpid()))
    print("msg end:", msg)
    print('\n')


if __name__ == "__main__":
    pool = Pool(processes=4)
    for i in range(4):
        msg = "子进程 %d" % i
        # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply(pro3, (msg, ))

    print("~~~~~~~~~~~~~~~~~~")
    pool.close()  # 执行完close后不会有新的进程加入到pool
    pool.join()   # join函数等待所有子进程结束
    print("All processes done.")
