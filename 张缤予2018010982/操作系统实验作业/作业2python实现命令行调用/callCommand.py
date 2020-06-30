# coding=utf-8
##!/usr/bin/python3
'''

Author: By.Zhang
Purpose: call windows command line by python.os.
Created: 27/6/2020

'''


import os

# 调用命令行
# os.system('cmd')

# 获取系统信息，相当于在cmd下输入systeminfo
os.system('systeminfo')

# 能查看当前电脑网卡的ip信息、DNS信息、DHCP服务器信息等
os.system('ipconfig')

# 在同一目录下创建aaa文件夹
# 执行多条命令
os.system('cd  && mkdir aaa')

# 获取目录信息
os.system('dir')

# 创建ccc文件夹
os.system('md ccc')

# 删除ccc文件夹
os.system('rd ccc')

# 输出test中的运行结果
os.system('python test.py')

# 返回值为0
print(os.system('test.py'))

# 相当于在命令行中输入ping www.baidu.com
os.system('ping www.baidu.com')

