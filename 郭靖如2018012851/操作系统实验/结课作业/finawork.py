import os

path = "E:\操作系统"
filelst = os.listdir(path)

for i in range(len(filelst)):
    show= os.path.join(path, filelst[i])
    if os.path.isfile(show):
        print(filelst[i])

'''
输出结果：
1-2  操作系统定义.pdf
1-3.1 操作系统发展过程.pdf
1-3.2 操作系统发展过程.pdf
1-4 OS第1讲 操作系统特征与功能.pdf
1-5 操作系统结构.pdf
2-1 进程的引入.pdf
2-10 进程通信.pdf
2-11 线程.pdf
2-2 进程控制.pdf
2-3 进程互斥.pdf
2-4 读者写者问题.pdf
2-5 哲学家就餐问题.pdf
2-6 AND型信号量.pdf
2-7 进程同步.pdf
2-8 生产者消费者问题（上）.pdf
2-8 生产者消费者问题（下）.pdf
2-9 管程.pdf
2018操作系统综合模拟测试.doc
2原子性应用.pdf
3-1 处理机调度的基本概念 .pdf
3-2 作业调度算法.pdf
3-3 进程调度算法.pdf
3-4 实时调度算法.pdf
3-5 死锁概述.pdf
3-6上 安全性算法.pdf
3-6下 避免死锁—银行家算法.pdf
3-7 检测解除死锁.pdf
4-1 存储器管理的基础知识.pdf
4-2 连续分配方式（上）.pdf
4-2 连续分配方式（下）.pdf
4-3 基本分页存储管理方式.pdf
4-4 基本分段存储管理方式.pdf
4-5 虚拟存储器的基本概念.pdf
4-6 请求分页存储管理方式.pdf
4-7 页面置换算法.pdf
4-8 请求分段存储管理方式.pdf
4页面置换算法.pdf
5-1 IO系统.pdf
5-2 IO控制方式.pdf
5-3 缓冲管理.pdf
5-4 IO软件.pdf
5-5 设备分配.pdf
5-6 磁盘存储器管理.pdf
5缓冲应用.pdf
6-1 文件和文件系统.pdf
6-2 文件的逻辑结构.pdf
6-3 外存分配方式.pdf
6-4 目录管理.pdf
6-5 文件存储空间的管理.pdf
6-6 文件的共享与保护.pdf
6文件结构.pdf
OS1.pptx
OS2.ppt
OS3.ppt
OS习题3.pdf
OS习题4.pdf
OS习题5.pdf
OS习题6.pdf
OS第2讲 题目.pdf
OS第3讲 题目.pdf
OS第4讲 题目.pdf
OS第5讲 题目.pdf
OS第6讲 题目.pdf
~$1-Introduction.pptx
操作系统第一章.mp4
操作系统结构的应用.pdf
第二章 互斥同步问题案例解答.mp4
'''
