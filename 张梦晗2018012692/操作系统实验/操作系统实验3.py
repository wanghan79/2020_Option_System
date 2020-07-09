import time
import random
from multiprocessing import Process

def run(name):
    print(f'{name} 正在运行')
    time.sleep(random.randint(1, 3))
    print(f'{name} 结束啦')

if __name__ =='__main__':
    process_list = []
    for i in range(3):
        p = Process(target=run, args=(f"线程{i}",))

        process_list.append(p)
        p.start()

    print('主进程结束')
    # strat():方法的功能 1.开启进程 2.执行功能