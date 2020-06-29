"""
    Author:
        BowenCao
        2018013070

    Purpose:
        采用Python语言创建多进程

    Created: 25/6/2020
"""

from multiprocessing import Process,Pool
import os, time, random


def pr1(process_name):
    '''
    :param process_name: 传进来的进程名称
    '''
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)


def pr2(process_name):
    '''
    :param process_name: 传进来的进程名称
    '''
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)

#-----------------------------------------------------------------------------------------------------------------------


def long_time_task(name):
    '''
    long_time_task()定义了子进程。
    :param name: 为传进来的进程名称
    '''
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random())
    end = time.time() # 加上时间延迟可以明显的看到在task0、1、2、3执行完之后，才开始执行task4的效果
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == "__main__":
    '''
    使用multiprocessing模块中的Process类，一个进程对象对于类的一个实例。所以创建一个Process类实例，就相当于创建了一个进程
    本程序中创建了p1 p2两个进程
    '''
    print("main process run...")
    # target:指定进程执行的函数
    # args:传入target参数对应函数的参数，需要使用tuple
    p1 = Process(target=pr1, args=('process_name1',))
    p2 = Process(target=pr2, args=('process_name2',))

    p1.start()  # 运行子进程p1
    p2.start()  # 运行子进程p2
    p1.join()   # 调用了px.join()方法，该方法会阻塞父进程，直到子进程全部运行完成后才会继续运行父进程。
    p2.join()
    print("main process ran all lines...\n")
#-----------------------------------------------------------------------------------------------------------------------

    '''
    如果要启动大量的子进程，可以用进程池Pool的方式批量创建子进程
    '''
    print('Parent process %s.' % os.getpid())
    p = Pool(4) #创建大小为4的进程池
    for i in range(5):
        p.apply_async(long_time_task, args=(i,)) # apply_async 是异步非阻塞的。即不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    # 往往将apply_async和join结合使用,因为如果主进程对应的主程序很简洁很快就运行完毕了，
    # 那么很可能还没来得及将主程序中调用的放在子进程中运行的部分执行完，主程序就先结束了，这样可能会带来错误


