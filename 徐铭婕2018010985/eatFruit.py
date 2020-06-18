# coding=utf-8
# 问题：使用PV信号量互斥同步解决吃水果问题
'''
    桌上有一个空盘，最多允许存放 N 只水果。
    爸爸可向盘中放一个苹果或者放一个橘子。
    儿子专等吃盘中的橘子，女儿专等吃盘子中的苹果。
    试用 PV 操作实现爸爸、儿子、女儿三个并发进程的同步
'''
# 思考过程如下
'''
1.定性：互斥+同步问题
2.角色<->进程：Father，Son，Daughter
3.设置信号量并赋初值：
    假设初始状态：容量为N的盘为空
    sempty=N，盘中空位数
    sorange=0，盘中橘子数
    sapple=0，盘中苹果数
    mutex=1，互斥信号量
4.编写主程序
'''
sempty=N
sorange=0
sapple=0
mutex=1
def Father():
    while(1):
        P(sempty)
        P(mutex)
        fruit=putItOnThePlate()
        V(mutex)
        if(fruit=='orange'):
            V(sorange)
        else:
            V(sapple)
def Son():
    while(1):
        P(sorange)
        P(mutex)
        eatOrange()
        V(mutex)
        V(sempty)
def Daughter():
    while(1):
        P(sapple)
        P(mutex)
        eatApple()
        V(mutex)
        V(sempty)
