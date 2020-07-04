"""
    Author:
        BowenCao
        2018013070

    Purpose:
        采用python语言实现windows命令行调用

    Created: 25/6/2020
"""
import os

'''
system 函数可以将字符串转化成命令在服务器上运行；其原理是每一条 system 函数执行时，
其会创建一个子进程在系统上执行命令行，子进程的执行结果无法影响主进程。
此程序简单的举例几个采用python语言实现windows命令行调用的例子
'''

def test():
    os.system('dir d:')  # 显示d盘目录列表
    os.system('notepad')  # 打开记事本
    os.system(r'"D:\Dev-Cpp\devcpp.exe"')  # 打开dev-cpp
    os.system('start ping www.baidu.com -t')  # 使用ping命令对一个百度网址发送测试数据包

test()