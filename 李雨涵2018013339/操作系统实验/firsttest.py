#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 14:02
# @Author  : liyuhan
# @File    : new firsthw.py
"""
Author:liyuhan
Purpose:采用python语言获取操作系统信息；提示：使用Python内置platform工具包
Created:2020
"""
import platform

def OsInfo():
    print('获取操作系统名称及版本号',platform.platform())
    print('获取操作系统版本号',platform.version())
    print('获取操作系统位数',platform.architecture())
    print('计算机类型',platform.machine())
    print('计算机网络名称',platform.node())
    print('计算机处理器信息',platform.processor())
    print('计算机操作系统类型',platform.system())
    print('汇总信息',platform.uname())

def PyInfo():
    print('获取python构建号和日期',platform.python_build())
    print('获取用于编译python的编译器',platform.python_compiler())
    print('获取python实现SCM分支',platform.python_branch())
    print('获取python实现的字符串',platform.python_implementation())
    print('获取python版本',platform.python_version())
    print('获取python实现SCM修订',platform.python_revision())
    print('获取python实现的数组',platform.python_version_tuple())


if __name__ == '__main__':
    OsInfo()
    PyInfo()