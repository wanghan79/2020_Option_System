import os
import threading
import multiprocessing
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

lock = multiprocessing.Lock()

if __name__ == '__main__':
    for i in range(5):
        process = multiprocessing.Process(target=worker, args=('process', lock))
        process.start()

