##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:Get operating system information
      Created:30/6/2020
"""
import platform

os = platform.system()
print
os
print
platform.platform()
print
platform.version()
print
platform.architecture()

# global var
# 是否显示日志信息
SHOW_LOG = True

def get_platform():
    #获取操作系统名称及版本号
    return platform.platform()

def get_version():
    #获取操作系统版本号
    return platform.version()

def get_architecture():
    #获取操作系统的位数
    return platform.architecture()

def get_machine():
    #计算机类型
    return platform.machine()

def get_node():
    #计算机的网络名称
    return platform.node()

def get_processor():
    #计算机处理器信息
    return platform.processor()

def get_system():
    #获取操作系统类型
    return platform.system()

def get_uname():
    #汇总信息
    return platform.uname()

def show_os_all_info():
    #打印os的全部信息
    print('获取操作系统名称及版本号 : [{}]'.format(get_platform()))
    print('获取操作系统版本号 : [{}]'.format(get_version()))
    print('获取操作系统的位数 : [{}]'.format(get_architecture()))
    print('计算机类型 : [{}]'.format(get_machine()))
    print('计算机的网络名称 : [{}]'.format(get_node()))
    print('计算机处理器信息 : [{}]'.format(get_processor()))
    print('获取操作系统类型 : [{}]'.format(get_system()))
    print('汇总信息 : [{}]'.format(get_uname()))

def show_os_info():
    #只打印os的信息，没有解释部分
    print(get_platform())
    print(get_version())
    print(get_architecture())
    print(get_machine())
    print(get_node())
    print(get_processor())
    print(get_system())
    print(get_uname())

def test():
    print('操作系统信息:')
    if SHOW_LOG:
        show_os_all_info()
    else:
        show_os_info()
    print('*' * 50)

def init():
    global SHOW_LOG
    SHOW_LOG = True

def main():
    init()
    test()

if __name__ == '__main__':
    main()