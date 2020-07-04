#邹佳鑫第三次实验

import time
import random
from multiprocessing import Process

def run(name):
    print(f'{name} is running')
    time.sleep(random.randint(1,3))
    print(f'{name} is end')
if __name__ == '__main__':
    for i in range(10):
        p = Process(target=run, args=(i,))
        p.start()
