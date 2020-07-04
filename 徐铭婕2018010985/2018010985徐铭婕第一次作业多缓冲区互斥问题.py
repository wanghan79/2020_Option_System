# coding=utf-8
# 问题：使用PV信号量互斥同步解决CP,IOP多缓冲区互斥同步问题
'''
    设某计算进程 CP 和 打印进程 IOP 共用一个大小为 N 的缓冲区 T
    CP 进程负责不断地计算数据并送入缓冲区 T 中
    IOP 进程负责不断地从缓冲区 T 中取出数据去打印
'''
# 思考过程如下
'''
1.定性：互斥+同步问题
2.角色<->进程：CP和IOP
3.设置信号量并赋初值：
    假设初始状态：大小为N的缓冲区为空
    sempty=N，缓冲区空位数
    sfull=0，已用缓冲区数
    mutex=1，互斥信号量
4.编写主程序
'''
sempty = N
sfull = 0
mutex = 1
def CP():
    while(1):
        count()
        P(sempty)
        P(mutex)
        sendToBuffer()
        V(mutex)
        V(sfull)
def IOP():
    while(1):
        P(sfull)
        P(mutex)
        getFromBuffer()
        V(mutex)
        V(sempty)
        print("num")
def __main__():
    CP()
    IOP()
