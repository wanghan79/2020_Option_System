"""
Author   :  Yihang.Gao  高艺航
StuNumber: 2018012950
Purpose  : Set up multiprocess by python.
Created  : 1/7/2020
"""
from multiprocessing import Process

def setup_pro(i):
    print('process',i)

if __name__ == '__main__':
    list_pro = []
    for i in range(3):
        k = Process(target=setup_pro, args=(i+1,))
        list_pro.append(k)

    list_pro[0].start()
    list_pro[1].start()
    list_pro[2].start()