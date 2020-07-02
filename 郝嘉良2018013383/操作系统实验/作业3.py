import multiprocessing
import threading
import logging
import time


# 1.多进程实例演示

def hello(i):
    print('hello, im', i)

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=hello, args=(i,))
        p.start()

# 2.多进程自定义进程名称

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)

def worker():
    name = multiprocessing.current_process().name
    logging.debug('%s 开始' % name)
    time.sleep(3)
    logging.debug('%s 结束' % name)

def my_service():
    name = multiprocessing.current_process().name
    logging.debug('%s 开始' % name)
    time.sleep(3)
    logging.debug('%s 结束' % name)


if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )

    worker_1 = multiprocessing.Process(
        name='worker_1',
        target=worker,
    )

    worker_2 = multiprocessing.Process(
        target=worker,
    )
    service.start()
    worker_1.start()
    worker_2.start()

# 3.守护进程无等待的方式

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def daemon():
    p = multiprocessing.current_process()
    logging.debug('%s %s 开始' % (p.name, p.pid))
    time.sleep(2)
    logging.debug('%s %s 结束' % (p.name, p.pid))


def no_daemon():
    p = multiprocessing.current_process()
    logging.debug('%s %s 开始' % (p.name, p.pid))
    logging.debug('%s %s 结束' % (p.name, p.pid))

if __name__ == '__main__':
    daemon_obj = multiprocessing.Process(
        target=daemon,
        name='daemon'
    )

    daemon_obj.daemon = True

    no_daemon_obj = multiprocessing.Process(
        target=no_daemon,
        name='no_daemon'
    )

    no_daemon_obj.daemon = False

    daemon_obj.start()
    time.sleep(1)
    no_daemon_obj.start()

# 4.守护进程设置等待超时时间

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def daemon():
    p = multiprocessing.current_process()
    logging.debug('%s %s 开始' % (p.name, p.pid))
    time.sleep(2)
    logging.debug('%s %s 结束' % (p.name, p.pid))

def no_daemon():
    p = multiprocessing.current_process()
    logging.debug('%s %s 开始' % (p.name, p.pid))
    logging.debug('%s %s 结束' % (p.name, p.pid))


if __name__ == '__main__':
    daemon_obj = multiprocessing.Process(
        target=daemon,
        name='daemon'
    )

    daemon_obj.daemon = True

    no_daemon_obj = multiprocessing.Process(
        target=no_daemon,
        name='no_daemon'
    )

    no_daemon_obj.daemon = False

    daemon_obj.start()
    time.sleep(1)
    no_daemon_obj.start()

    daemon_obj.join(1)
    logging.debug('daemon_obj.is_alive():%s' % daemon_obj.is_alive())
    no_daemon_obj.join()

# 5.进程的终止，注意：terminate的时候，需要使用join()进程，保证进程成功终止

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def slow_worker():
    print('开始工作')
    time.sleep(0.1)
    print('结束工作')

if __name__ == '__main__':
    p = multiprocessing.Process(
        target=slow_worker
    )
    logging.debug('开始之前的状态%s' % p.is_alive())

    p.start()
    logging.debug('正在运行的状态%s' % p.is_alive())

    p.terminate()
    logging.debug('调用终止进程的状态%s' % p.is_alive())

    p.join()
    logging.debug('等待所有进程运行完成，状态%s' % p.is_alive())

# 6.进程退出状态码
def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('运行时的错误')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    funcs = [
        exit_error,
        exit_ok,
        return_value,
        raises,
        terminated,
    ]
    for func in funcs:
        print('运行进程的函数名 %s' % func.__name__)
        j = multiprocessing.Process(
            target=func,
            name=func.__name__
        )
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print('{:>15}.exitcode={}'.format(j.name, j.exitcode))