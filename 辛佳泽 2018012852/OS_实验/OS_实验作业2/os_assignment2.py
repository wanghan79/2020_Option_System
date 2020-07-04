#作业2. 采用python语言实现windows命令行调用；提示：采用Python内置工具包os.system

"""
  Author:  Jiaza.Xin
  Purpose: Windows command line using Python language calls.
  Created: 29/6/2020
"""

#system 函数可以将字符串转化成命令在服务器上运行；
# 其原理是每一条 system 函数执行时，其会创建一个子进程在系统上执行命令行，子进程的执行结果无法影响主进程。

import os

#os.system 默认阻塞当前程序执行
os.system('cd /usr/local ; mkdir aaa.txt')

#在 cmd 命令前加入 start 可不阻塞当前程序执行
os.system('start ping www.baidu.com -t')




