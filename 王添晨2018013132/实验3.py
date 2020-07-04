from multiprocessing import Process

def testrun_proc():
    print('子进程正在运行')


if __name__ == '__main__':
    print('父进程开始运行')
    p = Process(target=testrun_proc)
    print('子进程准备执行')
    p.start()
