import os


def apply():
    os.system('cmd')        # 执行命令行
    print('显示目录信息:',os.system('dir'))
    print('显示c盘目录信息:',os.system('dir c:'))    # 显示c盘目录信息
    os.system("ipconfig")
    os.system('ping www.baidu.com >result.text')  # 调用ping命令，但只能以上述方式把结果管道输出本地文件里
    os.system("start C:\操作系统.py")             # 打开文件：可执行文件的绝对路径


apply()
#总结：
# 1.从主进程中fork一个子进程
# 2.在子进程中调用python的exec函数去执行命令
# 3.在主进程中调用wait（阻塞）等待子进程结束。
# 如果对于fork结束，system()函数返回-1