##!/usr/bin/python3
"""
  Author:  ZhengPeng.Han
  Purpose: Implement command line calls by a built-in function of python,which named os.system.
  Created: 26/6/2020
"""
import os
cmd1='ping github.com'
cmd2='winver'
cmd3='ipconfig /flushdns'
cmd4='taskmgr'
cmd5='cmd.exe'
print('/--ping Github官网的结果为：--/')
os.system(cmd1)
print('/--Windows操作系统版本为：--/')
os.system(cmd2)
print('/--即将清理DNS缓存：--/')
os.system(cmd3)
print('/--即将在pycharm控制台打开命令行窗口：--/')
os.system(cmd4)
print('/--即将打开任务管理器：--/')
os.system(cmd5)
