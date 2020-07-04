##!/usr/bin/python3
"""
Author:YiYang.Dong
Purpose:the second experiment
Created:1/7/2020
"""
import os
#获取java信息
os.system('java -version')
#获取目录信息
os.system('dir')
#获取IP信息
os.system('ipconfig')
#启动计算器
os.system("calc")
#CMD命令提示符
os.system("cmd.exe")
#调用控制面板
os.system('control')
#程序和功能
os.system("appwiz.cpl")
#证书管理实用程序
os.system("certmgr.msc")
# 打开磁盘清理工具
os.system("cleanmgr")
#木马捆绑工具，系统自带
os.system("iexpress")
#连接管理器配置文件安装程序
os.system("cmstp")
# 键入命令
order = input('输入你的命令：')
os.system(order)