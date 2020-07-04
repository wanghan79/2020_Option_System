##!/usr/bin/python3
"""
Author:YiYang.Dong
Purpose:the first experiment
Created:1/7/2020
"""
import platform

def TestPlatform():
    print('获取操作系统位数',platform.architecture())
    print('计算机类型',platform.machine())
    print('计算机的网络名称',platform.node())
    print('获取操作系统版本号', platform.version())
    print('获取操作系统名称及版本号', platform.platform())
    print('计算机处理器信息',platform.processor())
    print('计算机操作系统类型',platform.system())
    print('获取系统中python解释器的信息', platform.python_compiler())
    if platform.python_branch() == "":
        print('获取python实现的字符串',platform.python_implementation())
        print('获取python实现SCM修订',platform.python_revision())
    print(platform.release())
    print(platform.system())
    print('汇总信息',platform.uname())
    print('获取python构建号和日期',platform.python_build())
    print('获取python版本',platform.python_version())
    print('获取python实现的数组',platform.python_version_tuple())

def UsePlatform():
    sys = platform.system()
    if (sys == "Windows"):
        print ("调用Windows任务")
    elif (sys == "Linux"):
        print ("调用Linux任务")
    else:
        print ("其他的系统任务")

if __name__ == '__main__':
    TestPlatform()

    UsePlatform()