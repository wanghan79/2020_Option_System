"""
设计有n个进程共享m个系统资源的系统，进程可动态的申请和释放资源，系统按各进程的申请动态的分配资源。
系统能显示各个进程申请和释放资源，以及系统动态分配资源的过程，便于用户观察和分析；
要输入3种资源，5个进程
"""
import copy
import numpy as np

class pcb:
    def __init__(self,m):
        self.id = 0
        self.finish = False       #是否符合安全性，true表示符合安全性，false表示否
        self.Need = np.zeros([m],dtype=np.int)     #最大需求
        self.Allocation = np.zeros([m],dtype=np.int)   #已分配资源
        #self.Need = self.Max-self.Allocation          #还需要的资源

    def out_init(self):  #显示最初的顺序 max、allocation、need、available
        Max = self.Need+self.Allocation
        if self.id == 0:
            print(("进程%d" + '\t' + str(Max) + '\t' + "   " + str(self.Allocation) + '\t' + "  " + str(
                self.Need)+'\t') % self.id,end='')
        else:
            print(("进程%d"+'\t'+str(Max)+'\t'+"   "+str(self.Allocation)+'\t'+"  "+str(self.Need))%self.id)

def init(pcblist,n,m):
    #直接采用书本上的P113的银行家算法的例子数据来
    for i in range(n):
        pcblist.append(pcb(m))
    pcblist[0].id = 0
    pcblist[0].Need = np.array([7, 4, 3], dtype=int)
    pcblist[0].Allocation = np.array([0, 1, 0], dtype=int)
    pcblist[1].id = 1
    pcblist[1].Need = np.array([1, 2, 2], dtype=int)
    pcblist[1].Allocation = np.array([2, 0, 0], dtype=int)
    pcblist[2].id = 2
    pcblist[2].Need = np.array([6, 0, 0], dtype=int)
    pcblist[2].Allocation = np.array([3, 0, 2], dtype=int)
    pcblist[3].id = 3
    pcblist[3].Need = np.array([0, 1, 1], dtype=int)
    pcblist[3].Allocation = np.array([2, 1, 1], dtype=int)
    pcblist[4].id = 4
    pcblist[4].Need = np.array([4, 3, 1], dtype=int)
    pcblist[4].Allocation = np.array([0, 0, 2], dtype=int)
    Available = np.array([3,3,2],dtype=np.int)
    #显示初始化时的数据情况，按照课本那样显示
    print("             T0时刻进程和资源分配情况")
    print("      "+ '\t' +"  Max"+'\t'+"  Allocation"+'\t'+"Need"+'\t'+ "Available")
    for i in range(n):
        pcblist[i].out_init()
        if i == 0:
            print(str(Available))

def compare(a,b):  #1表示a小于等于b，0是a大于b
    flag_all = 1
    flag_temp = 0
    for i in range(len(a)) :
        if a[i] != 0:
            flag_temp = 1
    # if flag_temp == 0:
    #     print("request全0")

    for i in range(len(a)):
        if a[i]>b[i]:
            flag_all = 0
    return flag_all

def judge_full_true(pcblist): #判断序列是不是状态都是True，都是1，不都是就是0
    flag = 1
    for i in pcblist:
        if i.finish == False:
            flag = 0
    return flag

def aqx(pcblist,work,id): #安全性判断
    work_1 = copy.deepcopy(work)
    safe_list = []
    
    while True:
        flag = 0
        for i in range(len(pcblist)):
            if pcblist[i].finish == False and compare(pcblist[i].Need,work)==1:
                work += pcblist[i].Allocation
                pcblist[i].finish = True
                safe_list.append(pcblist[i])
                flag = 1
                continue
        if judge_full_true(pcblist) == 1 :
            if id == 0:
                print("T0时刻系统安全,安全序列为：",end="")
            else:
                print(("P%d申请资源时系统安全序列为：")%id,end='')
            for i in safe_list:
                print("P"+str(i.id),end='  ')
            print('')
            if id == 0:
                print("             T0时刻进程安全序列")
            else:
                print("             P%d申请资源时的安全检查"%id)
            print("      " + '\t' + "  Max" + '\t' + "    Need" + '\t' + "Allocation" + '\t' + " Work+Allocation"+'\t'+"Finish")
            for i in safe_list:
                print("进程"+str(i.id)+'\t'+str(work_1)+'\t'+"  "+str(i.Need)+'\t'+" "+str(i.Allocation)+'\t'+"  "+str(work_1+i.Allocation)+'\t'+"        "+str(i.finish))
                work_1 += i.Allocation
            return id

        if flag == 0 :
            print("此系统不安全！")
            return -1

def yhj(pcbList): #银行家算法
    Available1 = np.array([3, 3, 2], dtype=np.int)

    m = len(pcbList[0].Need)
    now_list = []  #安全序列
    count = 0  #时间T
    while  True:

        id = 0
        Available = copy.deepcopy(Available1)
        pcblist = copy.deepcopy(pcbList)
        request1 = np.array([0,0,0], dtype=np.int)
        if count > 0 :
            flag_r = int(input("是否更改某一个进程的请求向量(0：不改变 1：改变)"))
            if flag_r == 1 :
                id = int(input("请输入你要改变的进程序号(0开始)"))
                print("请输入他的请求向量")
                while True :
                    request1 = np.array(input().split(), dtype=np.int)
                    if compare(request1, pcbList[id].Need) == 0 :
                        print("输入的请求向量超过了宣布的最大值，无效！请重新输入")
                    elif compare(request1, Available) == 0 :
                        print("输入的请求资源大于可用资源，请进程%d等待并重新输入"%id)
                    else :
                        break
                # pcblist[id].Allocation += request
                # pcblist[id].Need -= request

        for i in range(len(pcblist)):
            if id == i and count>0:
                request = copy.deepcopy(request1)
            else:
                request = pcblist[i].Need

            if compare(request,Available) == 1 :
                #print("当前是进程%d"%pcblist[i].id)
                Available -= request
                pcblist[i].Allocation += request
                pcblist[i].Need -= request
                work =Available
                return_aqx = aqx(pcblist,work,id )
                if return_aqx != -1 :
                    count +=1
                if count >1 :
                    pcbList[i].finish = True
                    pcbList[i].Allocation += request
                    pcbList[i].Need -= request
                    Available1 -= request
                break

        # flag_r = int(input("是否更改某一个进程的请求向量(0：不改变 1：改变)"))
        # if flag_r == 1 :
        #     id = int(input("请输入你要改变的进程序号(0开始)"))
        #     print("请输入他的请求向量")
        #     while True:
        #         request = np.array(input().split(), dtype=np.int)
        #         if compare(request,pcblist[id].Need) == 0:
        #             print("输入的请求向量超过了宣布的最大值，无效！请重新输入")
        #         else:
        #             break
        #     pcblist[id].Allocation += request
        #     pcblist[id].Need -= request
        # else :
        #     request = pcblist[0].Need

def main():
    n = int(input("请输入进程数："))
    m = int(input("请输入资源种类的数量："))
    pcblist = []
    Available = np.zeros([m], dtype=np.int)  # 可利用资源向量，索引代表种类，值代表可用数量
    # Max = np.zeros([n, m], dtype=np.int)  # 最大需求矩阵，M[i,j]=k代表进程i需要最大k个j类资源
    # Allocation = np.zeros([n, m], dtype=np.int)  # 分配矩阵，A[i,j]=k表示进程i已分配到k个j类资源
    # #Need = np.zeros([n, m], dtype=np.int)  # 需求矩阵，N[i,j]=k表示进程i还需要k个j类资源
    # # Need[i,j] = Max[i,j]-Allocation[i,j]
    # print("请输入可使用资源向量Available:")
    # Available[:] = np.array(input().split(),dtype=np.int)
    # print("请输入进程的最大需求矩阵：")
    # for i in range(n):
    #     Max[i][:] = np.array(input().split(),dtype=np.int)
    # Need = Max.copy()
    # Allocation = Max-Need
    init(pcblist,n,m)
    yhj(pcblist)

if __name__ == "__main__":
    main()