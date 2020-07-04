from multiprocessing import Process
import time

def coding(language):
     # 子进程要执行的代码
     for i in range(5):
         print("{} coding".format(language), end=' | ')
         time.sleep(1)

if __name__== '__main__':
     # 多进程
     multi_start = time.time()
     p = Process(target=coding, args=('python', ))
     p.start()
     for i in range(5):
         print("main program", end=' | ')
         time.sleep(1)
     multi_end = time.time()
     print("\nMulti process cost time:", multi_end - multi_start)
