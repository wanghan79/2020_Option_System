'''
Author: WeiFan 2018011641
Aim:  python语言创建多进程
Data: 2020/6/28
'''
#from multiprocessing import Process
#import time
#import os

#def fun1(x,y):
    #StartTime=time.time()
    #print(os.getpid())
    #print(x+y)
    #time.sleep(3)
    #print((os.getpid(),(time.time()-StartTime)))

#if __name__ == '__main__':
    #s=Process(target=fun1,args=(1,2))
    #d=Process(target=fun1,args=(3,4))
    #s.start()
    #d.start()
    #print('main')

import os, time
from multiprocessing import Process

def worker():
    print("子进程执行中>>> pid={0},ppid={1}".format(os.getpid(), os.getppid()))
    time.sleep(2)
    print("子进程终止>>> pid={0}".format(os.getpid()))

def main():
    print("主进程执行中>>> pid={0}".format(os.getpid()))
    ps = []
    # 创建子进程实例
    for i in range(2):
        p = Process(target=worker, name="worker" + str(i), args=())
        ps.append(p)

    # 开启进程
    for i in range(2):
        ps[i].start()

    # 阻塞进程
    for i in range(2):
        ps[i].join()

    print("主进程终止")

if __name__ == '__main__':
    main()
