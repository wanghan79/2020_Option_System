"""
  Author:  jianxi.li
  Purpose: homework2:采用python语言实现windows命令行调用；提示：采用Python内置工具包os.system
  Created: 26/6/2020
"""
import os
#os.system("calc")#启动计算器
#os.system("appwiz.cpl")#程序和功能
#os.system("certmgr.msc")#证书管理实用程序
#os.system("charmap")#启动字符映射表
#os.system("chkdsk.exe")#Chkdsk磁盘检查(管理员身份运行命令提示符)
order = input('imput your order')
os.system(order)