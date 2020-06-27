from multiprocessing import Process
import os
import time
def prg1(name):
    print(name, os.getpid())
def prg2(name):
    print(name, os.getpid())
if __name__ == '__main__':
    s1 = Process(target=prg1, args=('proc1',))
    s2 = Process(target=prg2, args=('proc2',))
    s1.start()
    s2.start()
    s1.join()
    s2.join()

