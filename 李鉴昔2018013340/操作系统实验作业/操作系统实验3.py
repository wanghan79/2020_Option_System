"""
  Author:  jianxi.li
  Purpose: homework3:采用Python语言创建多进程；提示：采用Python内置工具包multiprocessing
  Created: 27/6/2020
"""
from multiprocessing import Process
import os, time
def pr1(process_name):
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)
def pr2(process_name):
    for i in range(5):
        print(process_name, os.getpid())  # 打印出当前进程的id
        time.sleep(1)
if __name__ == "__main__":
    print("主程序运行")
    # target:指定进程执行的函数
    part1 = Process(target=pr1, args=('进程名称1',))
    part2 = Process(target=pr2, args=('进程名称2',))
    part1.start()
    part2.start()
    part1.join()
    part2.join()
    print("main process ran all lines...")
