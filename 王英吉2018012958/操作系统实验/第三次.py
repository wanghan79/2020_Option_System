import time
from multiprocessing import Process
def process(i):
    time.sleep(2)
    print(i)


if __name__ == '__main__':
    process_list = []
    # 创建3个子进程
    for i in range(3):
        p = Process(target=process, args=(i+1,))
        process_list.append(p)

    # 依次启动进程
    process_list[0].start()
    process_list[1].start()
    process_list[2].start()