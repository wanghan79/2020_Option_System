
# -*- coding:utf-8 -*-

"""
Author: YY.Dong
Purpose: Using Python language to realize windows command line call
Created: 6/25/2020
"""
import os
def apply():
    #Windows IP 配置
    print('测试开始')

    # 显示目录信息
    print('显示目录信息:')
    os.system('dir')

    #显示c盘目录信息
    print('显示c盘目录信息:')
    os.system('dir c:')

    ## 调用ping命令实现ping IP地址功能
    os.system('ping -c 1 -w 1 192.168.1.1')#发送报文一次，等待一秒

    # 执行操作系统命令，但是只能执行，获取不到结果；
    os.system("ipconfig")

    #打开文件夹
    os.system("start D:\ARMMMM")

    #执行多条命令
    os.system('cd d && mkdir aaa.txt')

    res = os.system('date')
    print(res)

    #命令行
    os.system('cmd')
    
    print(u'测试结束')


apply()
