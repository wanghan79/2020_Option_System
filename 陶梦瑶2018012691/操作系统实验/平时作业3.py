from multiprocessing import Process
import os
import time


# 线程启动后实际执行的代码块
def pro1(process_name):
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)


def pro2(process_name):
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)


if __name__ == "__main__":
    print("main process run...")
    # target:指定进程执行的函数
    # args:传入target参数对应函数的参数，需要使用tuple
    p1 = Process(target=pro1, args=('process_name1',))
    p2 = Process(target=pro2, args=('process_name2',))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("main process ran all lines...")

