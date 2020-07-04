import time
import random
from multiprocessing import Process

def run(name):
    print(f'{name} is running')
    time.sleep(random.randint(1,3))
    print(f'{name} is end')

if __name__ =='__main__':
    p_list = []
    for i in range(3):
        # 传参的两种方式
        # p = Process(target=run,kwargs={'name':f'线程{i}'})
        p = Process(target=run,args=(f"线程{i}",))

        p_list.append(p)
        p.start()
    # for i in p_list:
        # p.join()  # join后主进程会等待子进程都结束再结束
    print('主进程结束')
    # strat():方法的功能 1.开启进程 2.执行功能

