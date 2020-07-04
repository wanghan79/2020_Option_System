import multiprocessing
import time
import threading
def f(flag):
    time.sleep(2)
    print("work",flag)
    t=threading.Thread(target=run,)
    t.start()

def run():
    print(threading.get_ident())

if __name__ == '__main__':
    for i in range(4):
        p=multiprocessing.Process(target=f,args=('ok %s'%i,))
        p.start()
