"""
Author:Chenjiaying
Purpose:采用python语言实现windows命令行调用
Created:1/7/2020
"""
import os


def test():
    os.system("calc")  # 启动计算机
    os.system("appwiz.cpl")  # 程序和功能
    os.system("certmgr.msc")  # 证书管理实用程序
    os.system("charmap")  # 启动字符映射表
    os.system("chkdsk.exe")  # Chkdsk磁盘检查(管理员身份运行命令提示符)
    os.system("cleanmgr")  # 打开磁盘清理工具


test()
