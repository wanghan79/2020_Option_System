# coding=utf-8
# 问题：使用管程解决哲学家进餐问题
'''
    有 N 个哲学家，他们的生活方式是交替地进行思考和进餐
    哲学家们共用一张圆桌，分别坐在周围的 N张椅子上，在圆桌上有 N个碗和 N支筷子
    平时哲学家进行思考，饥饿时便试图取其左、右最靠近他的筷子，只有在他拿到两支筷子时才能进餐
    该哲学家进餐完毕后，放下左右两只筷子又继续思考。
'''
# 思考过程如下
'''
1.定性：互斥+同步问题
2.角色<->进程：Philosopher
3.设置信号量并赋初值：
    __philosopherState[0:N]=['thinking' for i in range(N)],哲学家状态，有thinking，eating，hungry
    假设哲学家们初始状态为思考
    __philosopher[0:N]=[0 for i in range(N)],哲学家,初始值为0
    mutex=1，互斥信号量
4.编写主程序
'''
class Moniter:
    __philosopherState=['thinking' for i in range(N)]
    __philosopher=[0 for i in range(N)]
    mutex=1

    def __init__(self):
        self.__philosopherState = ['thinking' for i in range(N)]
        self.__philosopher = [0 for i in range(N)]
        mutex = 1

    #isEating判断哲学家x是否在吃饭
    def isEating(self,x):
        if self.__philosopherState[x] == 'eating':
            return 1
        else:
            return 0

    #canEat判断哲学家x是否可以吃饭：当且仅当哲学家x hungry且其左右的哲学家(x-1和x+1)不处于eating状态
    def canEat(self,x):
        if self.__philosopherState[x] == 'hungry':
            if (x == 0)&(self.isEating(self, 1) == 0)&(self.isEating(self, N) == 0):
                return 1
            elif (x == N)&(self.isEating(self, 0) == 0)&(self.isEating(self, N - 1) == 0):
                return 1
            elif (self.isEating(self, x - 1) == 0)&(self.isEating(self, x + 1) == 0):
                return 1
            else:
                return 0
        else:
            return 0

    #让哲学家x吃饭
    def eat(self,x):
        self.__philosopherState[x]='eating'
        V(self.__philosopher[x])

    #哲学家x试图吃饭
    def tryToEat(self,x):
        self.__philosopherState[x]='hungry'
        P(self.mutex)
        if self.canEat(x):
            self.eat(x)
        V(self.mutex)
        P(self.__philosopher[x])

    # 哲学家x开始思考
    def afterEat(self, x):
        self.__philosopherState[x] = 'thinking'
        P(self.mutex)
        if x!=0&self.canEat(x-1):
            self.eat(x-1)
        elif x!=N&self.canEat(x+1):
            self.eat(x+1)
        elif x==0&self.canEat(N):
            self.eat(N)
        elif x==N&self.canEat(0):
            self.eat(0)
        V(self.mutex)