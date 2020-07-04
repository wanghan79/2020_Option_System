from multiprocessing import Process
import os
def test(name):
    '''
    	函数输出当前进程ID，以及其父进程ID。
    	此代码应在Linux下运行，因为windows下os模块不支持getppid()  ，在windows中可以使用return 把想要的值返回。
    	'''
    print("Process ID： %s" % (os.getpid()))
    print("Parent Process ID： %s" % (os.getppid()))


if __name__ == "__main__":
    '''
    windows下，创建进程的代码一下要放在main函数里面
    '''
    proc = Process(target=test, args=('nmask',))
    proc.start()
    proc.join()


    class MyProcess(Process):
        '''
        继承Process类，类似threading.Thread
        '''


    def __init__(self, arg):
        super(MyProcess, self).__init__()
        # multiprocessing.Process.__init__(self)
        self.arg = arg


    def run(self):
        '''
        重构run函数
        '''


    print
    'nMask',self.arg
    time.sleep(1)
if __name__ == '__main__':
    for i in range(10):
        p = MyProcess(i)
        p.start()
    for i in range(10):
        p.join()


from multiprocessing import Pool
def test(i):
    print(i)     # 使用Spyder 能够实现，可以采用return的方式  pycharm没问题
if __name__=="__main__":
	lists=[1,2,3]
	pool=Pool(processes=2) #定义最大的进程数
	pool.map(test,lists)        #p必须是一个可迭代变量。
	pool.close()
	pool.join()

from multiprocessing import Pool


def test(i):
    print(i)


if __name__ == "__main__":
    pool = Pool(processes=10)
    for i in range(500):
        '''
        For循环中执行步骤：
        （1）循环遍历，将500个子进程添加到进程池（相对父进程会阻塞）
        （2）每次执行10个子进程，等一个子进程执行完后，立马启动新的子进程。（相对父进程不阻塞）

        apply_async为异步进程池写法。
        异步指的是启动子进程的过程，与父进程本身的执行（print）是异步的，而For循环中往进程池添加子进程的过程，与父进程本身的执行却是同步的。
        '''
    pool.apply_async(test, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.

    pool.close()
from multiprocessing import Process, Lock   # 在pycharm、idle下根本测试不出来
def l(lock, num):
    lock.acquire()
    print
    "Hello Num: %s" % (num)
    lock.release()
if __name__ == '__main__':
    lock = Lock()  #这个一定要定义为全局
    for num in range(20):
        Process(target=l, args=(lock, num)).start()