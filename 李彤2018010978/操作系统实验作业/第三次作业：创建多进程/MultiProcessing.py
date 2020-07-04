#coding:utf-8
'''
Description:Create multiple processes
Author:li tong

'''

from multiprocessing import Process,Pool
from time import sleep,ctime
import os

##实例化类Process创建一个进程
# def text(id):
#     print('Child Process',id,'is running.')
#
# if __name__ == '__main__':
#     print('Main process ',os.getpid(),'start.')
#     for i in range(3):
#         p=Process(target=text,args=(i,))
#         p.start()
#         p.join()
#     print('Main Process end.')

##继承Process类创建子进程
# class ChildProcess(Process):
#     def __init__(self):
#         super().__init__()
#     def run(self) :
#         print('I am child process:',os.getpid())
#
# if __name__ == '__main__':
#     print('Main process ',os.getpid(),'start.')
#     for i in range(3):
#         print('Child Process ',i,'start.')
#         p=ChildProcess()
#         p.start()
#         p.join()
#         print('Child Process ',i,'end.')
#     print('Main Process end.')

##进程池函数Pool()用来批量创建子进程
def text2(id):
    print('Process',os.getpid(),'is running as',id,'at',ctime())
    sleep(5) #停顿五秒
if __name__ == '__main__':
    print('Main process ',os.getpid(),'start.')
    pool=Pool(2)
    for i in range(4):
        pool.apply_async(text2,args=(i,))
    pool.close()
    pool.join()
    print('Main Process end.')

