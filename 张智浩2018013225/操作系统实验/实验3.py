import time
from multiprocessing import Process
def func(n):
    print("执行子进程:", n)
    time.sleep(2)
if __name__ == '__main__':
    for i in range(4):
        p = Process(target=func, args=(i,))
        p.start()
        p.join()
        print("执行父进程")