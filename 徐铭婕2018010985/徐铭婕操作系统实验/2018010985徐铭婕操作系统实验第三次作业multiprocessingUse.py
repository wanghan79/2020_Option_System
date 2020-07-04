# encoding: utf-8
'''
Author :    xumingjie 
Purpose:    Use multiprocessing to create multiple processes.
Created:    2020/7/3 9:19
'''

from multiprocessing import Pool
import time
import os
import random

def mult(multname):
    print('子进程%s启动' %multname)
    start = time.time()
    time.sleep(random.randint(1, 5))
    end = time.time()
    print('子进程%s结束 耗时：%d，进程号为%s' % (multname, end - start, os.getpid()))


if __name__ == "__main__":
    p = Pool(5)
    for i in range(10):
        p.apply_async(mult, args=(i,))
    p.close()
    p.join()  
    
