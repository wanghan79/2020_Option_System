##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
  Author:  ZhengPeng.Han
  Purpose: Creating multiple processes by a built-in function of python,which named multiprocessing.
  Created: 26/6/2020
"""
from multiprocessing import Process
from multiprocessing import Pool
import os, time,random
# 线程启动后实际执行的代码块
def pr1(process_name):#声明用于执行的函数
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)


def pr2(process_name):#声明用于执行的函数
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)


if __name__ == "__main__":
    print('\n')
    print('----使用multiprocessing中的process方法创建进程----')
    print("/--父进程开始运行--/")
    p1 = Process(target=pr1, args=('process_name1',))#target:指定进程执行的函数
    p2 = Process(target=pr2, args=('process_name2',))#args:传入target所对应函数的参数

    p1.start()#使用start()方法开始执行p1进程,由于p1中有sleep方法暂停1个时间单位故会和p2进程交替输出
    p2.start()#使用start()方法开始执行p2进程,由于p2中有sleep方法暂停1个时间单位故会和p1进程交替输出
    p1.join()#使用join()方法在此时将父进程阻塞，并运行p1直至p1完成
    p2.join()#使用join()方法在此时将父进程阻塞，并运行p2直至p2完成
    #如果没有join方法，则父进程之中的两个print将会最先执行，之后才是p1和p2
    print("/--父进程运行完毕--/")

def long_time_task(name):#定义子进程
    print('执行进程 %s ，其id为(%s)...' % (name, os.getpid()))
    start = time.time()#获取此时时间
    time.sleep(random.random())#暂停随机时间
    end = time.time()#获取此时时间
    print('进程 %s 运行了 %0.2f 秒.' % (name, (end - start)))#end-start可得该进程运行时间


if __name__ == '__main__':
    print('\n')
    print('----使用pool方法批量创建进程----')
    print('父进程id为 %s.' % os.getpid())
    p = Pool(4)#创建一个Pool对象，其中传入的参数是这个Pool的大小，当没有参数传递时，这个大小值默认为CPU核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))#apply_async()方法表示使用该大小为4的Pool去完成long_time_task对应的程序，其中args为待传入target对应的程序的参数的元组
    print('/--等待所有的子进程执行完毕--/')
    p.close()#.close()表示关闭Pool，这样就不允许有新的Process加入Pool中
    p.join()#.join()表示主进程阻塞，要等待子进程执行完毕后才能继续执行。join()方法需要在close()或者terminate()使用完之后再使用
    print('/--所有的子进程执行完毕--/')
