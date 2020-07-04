"""
Author: YY.Dong
Purpose: Creating multiple processes
Created: 25/6/2020
Description:用了两种方法创建多进程 另外 通过子类创建进程在注释中
"""
# -*- coding: utf-8 -*-
from multiprocessing import Process
from multiprocessing import Pool
import time, os, random


def run1(i):  # 重写run方法
    '''
        Description:子进程1
        parameter name: progress name
    '''
    print("A类进程", i, '当前进程id：', os.getpid(), '父进程id', os.getppid())
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print('A',i,'进程结束' ,'用时：',(end - start))


def run2(i):
    '''
            Description:子进程2
            param name: progress name
    '''
    print('B类进程 ', i, '正在执行', '当前进程id：', os.getpid(), '父进程id', os.getppid())
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print('B',i, '进程结束', '用时：', (end - start))

################进程池###############################
def poolprocess(task_name):
    '''
            Description:进程池
            param name: progress name
    '''
    print('我有很多作业!', task_name)
    start = time.time()  # 计算代码运行时间
    # 使用sleep
    time.sleep(random.random())
    end = time.time()
    print('做完作业:', task_name, ' 用时:', end - start)

#######################################################################
if __name__ == '__main__':  # 在windows平台上用Process写多进程时，需要在main函数中执行
    '''用Process写的多进程程序，主进程会等待子进程结束后再结束。
    如果开启子进程后主进程还想执行，是可以的。因为主进程和子进程一起抢占CPU，主进程并不会等子进程结束之后再执行自己的代码。
    如果我们现在有一个需求：主进程需要等待子进程执行完毕后再执行一些语句，那怎么办呢？ 用join()。 join()起的作用是阻塞主进程。
    '''
    print('--' * 4, '创建方法1-直接创建')
    for item in range(2):
        p1 = Process(target=run1, args=(item + 1,))
        p2 = Process(target=run2, args=(item + 1,))  # args:对应函数的参数
        p1.start()
        p2.start()  # 开启进程
        p1.join()  # 也可以给join设置一个timeout
        p2.join()
    print('done!')  # 阻塞主进程 让 done！最后输出

    time.sleep(1)  # 进程挂起的时间
############################################进程池##########################
    # 非阻塞式
    print('--' * 4, '创建方法2-进程池')
    pool = Pool(5)  # 进程池大小

    tasks = ['操作系统作业', '项目实践作业', '大数据作业', '信息检索作业', '安卓作业', '体育作业', '不能休息']

    for t in tasks:
        pool.apply_async(poolprocess, args=(t,))

    pool.close()  # 关闭进程池，不允许继续添加进程
    pool.join()  # 等待进程池中的所有进程结束

    print('要是真能这么快就好了!!!!!!!!!!')


'''

#子类创建
class MyNewProcess(Process):
    def run(self):  # 重写run方法
        print("---1----")
        time.sleep(1)

p = MyNewProcess()
if __name__ == '__main__':
    p.start()  



'''

