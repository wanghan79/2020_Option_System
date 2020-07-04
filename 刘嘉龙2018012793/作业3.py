import multiprocessing
import time

# 定义一个空列表
m_list = []


# 定义一个向列表添加元素的函数
def add_list():
    # 查看进程id编号
    print("add:", id(m_list))
    # 循环0,1,2,3,4
    for i in range(5):
        # 把循环的元素添加到列表
        m_list.append(i)
        # 打印列表
        print(m_list)
        # 休息1秒
        time.sleep(1)


# 定义一个函数对比全局不共享
def get_list():
    # 查看进程id编号
    print("get:", id(m_list))
    # 获取列表
    print("current", m_list)


# main函数
def main():
    # 线程一
    add = multiprocessing.Process(target=add_list)
    add.start()
    add.join()
    # 线程二
    multiprocessing.Process(target=get_list).start()
    # 查看进程id编号
    print("before", id(m_list))
    # 获取现在列表
    print("now", m_list)


# 主函数
if __name__ == "__main__":
    main()
