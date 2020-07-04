#作业3. 采用Python语言创建多进程；提示：采用Python内置工具包multiprocessing
#Process模块用来创建子进程，是Multiprocessing核心模块，可以实现多进程的创建，启动，关闭等操作。
#class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

"""
  Author:  Jiaza.Xin
  Purpose: Using the Python language to create a multiple - Process
  Created: 29/6/2020
"""

#方法一,直接传入
from multiprocessing import Process

def foo(i):
    print ('hello', i)

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.start()


#方法二，Process继承并覆盖run()

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()#-------继承
        self.arg = arg

    def run(self):  #--------------覆盖run()
        print('say hi', self.arg)
        time.sleep(1)  #------------ time sleep() 函数推迟调用线程的运行，推迟一秒

if __name__ == '__main__':

    for i in range(10):
        p = MyProcess(i)
        p.start()
