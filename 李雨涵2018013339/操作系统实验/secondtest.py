#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 14:51
# @Author  : liyuhan
# @File    : secondtest.py
"""
Author:liyuhan
Purpose:采用python语言实现windows命令行调用；提示：采用Python内置工具包os.system
Created:2020
"""

import os

#显示IP信息
if os.system('ipconfig')==0:
    print("执行完毕")

#显示目录信息
if os.system('dir')==0:
    print("执行完毕")

#调用控制面板
os.system('control')

#调用命令行
cmd='echo "helloworld"'
os.system(cmd)

#调用本地程序
os.system('Overcooked.exe')




