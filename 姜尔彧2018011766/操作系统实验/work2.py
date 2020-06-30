# coding=utf-8
"""
  Author:  Jiang Eryu
  Purpose: 采用Python内置工具包os.system实现windows命令行调用
  Created: 30/6/2020
"""

# --------实验说明---------
# 采用Python内置工具包os.system实现windows命令行调用
# os.system(‘command’) 会执行括号中的命令，如果命令成功执行，这条语句返回0，否则返回1

import os

#启动计算器
os.system("calc")
#CMD命令提示符
os.system("cmd.exe")
#控制面板
os.system("control")
#程序和功能
os.system("appwiz.cpl")
#证书管理实用程序
os.system("certmgr.msc")
# 打开磁盘清理工具
os.system("cleanmgr")
#连接管理器配置文件安装程序
os.system("cmstp")
#input your order
order = input('input your order here')  # 键入命令
os.system(order)
