from multiprocessing import Process
import time

def mywork3(type:int):
    while True:
        print("%d" % type)
        time.sleep(1)
        return

if __name__ == '__main__':
    for i in range(2):
        p1 = Process(target=mywork3,args=(10,))
        p2 = Process(target=mywork3,args=(20,))
        p1.start()
        p2.start()