from multiprocessing import Process, Pool
import os
import time


def run_proc(wTime):
    n = 0
    while n < 3:
        print("subProcess %s run," % os.getpid(), "{0}".format(time.ctime()))
        time.sleep(wTime)
        n += 1

if __name__ == "__main__":
    p = Process(target=run_proc, args=(2,))
    p.start()
    print("Parent process run. subProcess is ", p.pid)
    print("Parent process end,{0}".format(time.ctime()))
