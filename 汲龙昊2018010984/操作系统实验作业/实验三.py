"""
Author:JLH2018010984
Created:2020/6/30
"""
###################################################
from multiprocessing import Process
import time


def print_line():
        print("*" * 60)
    print_line()

def JLH(name):
        while True:
            print('Startt', name, time.ctime())
            time.sleep(1)
            return

if __name__ == '__main__':
        print('启动')
        p_list = []
        for i in range(3):
            P1 = Process(target=JLH, args=('First进程',))
            P2 = Process(target=JLH, args=('Second进程',))
            P1.start()
            P2.start()
            P1.join()
            P2.join()
            print('结束')
    print_line()