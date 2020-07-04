import os
import threading
import multiprocessing

# worker function
def worker(sign, lock):
    lock.acquire()#加锁
    print(sign, os.getpid())#打印句柄
    lock.release()#释放锁

lock = multiprocessing.Lock()#多进程锁

if __name__ == '__main__':
    for i in range(5):#创建5个进程
        process = multiprocessing.Process(target=worker, args=('process', lock))
        process.start()

