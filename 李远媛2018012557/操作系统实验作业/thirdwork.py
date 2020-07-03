#coding:utf-8
'''
    Author: Yy.Li
    Purpose:采用Python语言创建多进程；提示：采用Python内置工具包multiprocessing
    Created:30/6/2020
'''

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg

    def run(self):
        print('say hi', self.arg)
        time.sleep(1)


if __name__ == '__main__':

    for i in range(10):
        p = MyProcess(i)
        p.start()