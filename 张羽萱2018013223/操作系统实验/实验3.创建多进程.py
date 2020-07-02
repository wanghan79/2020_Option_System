'''
Author: Zhang yuxuan
purpose:  Create Multiprocess
Date: 2020/6/30
'''


from multiprocessing import Process


def func():
    print('running')


if __name__ == '__main__':
    p1 = Process(target=func)
    p1.start()
    print('created')
