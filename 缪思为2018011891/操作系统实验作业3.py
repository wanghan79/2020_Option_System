from multiprocessing import Process
import time

def test():
    for i in range(5):
        print("---test---")
        time.sleep(1)

if __name__=="__main__":
    print("父进程正在运行")
    time.sleep(1)
    p=Process(target=test)
    print("子进程test将要执行：")
    time.sleep(1)
    p.start()
    p.join()
    print("子进程结束")

