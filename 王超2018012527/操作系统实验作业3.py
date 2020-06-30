from multiprocessing import Pool
from time import sleep
import os


def text(id):
    print('Process %s is running as id(%d).' % (os.getpid(), id))
    sleep(5)


if __name__ == '__main__':
    pool = Pool(4)
    pool.apply_async(text, args=(111,))
    pool.apply_async(text, args=(222,))
    pool.apply_async(text, args=(333,))
    pool.close()
    pool.join()
