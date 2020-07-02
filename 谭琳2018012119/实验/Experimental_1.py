# python3
# coding=utf-8
"""
  Author:  Tanlin
  Purpose: 操作系统实验作业1. 采用python语言获取操作系统信息；提示：使用Python内置platform工具包
  Created: 2020.6.28
"""
import platform
def TestPlatform():
    print("------Operation System------")

    print(platform.python_version())    #  获取Python版本   3.7.6

    print(platform.architecture())  #   获取操作系统可执行程序的结构  ('64bit', 'WindowsPE')

    print(platform.node())  #   计算机的网络名称    LAPTOP-O6R63GS8

    print(platform.platform())  # 获取操作系统名称及版本号  Windows-10-10.0.18362-SP0

    print(platform.processor())  # 计算机处理器信息 Intel64 Family 6 Model 92 Stepping 9, GenuineIntel

    print(platform.python_build())  # 获取操作系统中Python的构建日期

    print(platform.python_compiler())   #  获取系统中python解释器的信息
    if platform.python_branch() == "":
        print(platform.python_implementation())
        print(platform.python_revision())
    print(platform.release())
    print(platform.system())
    print(platform.version())   #  获取操作系统的版本
    print(platform.uname()) #  包含上面所有的信息汇总  uname_result(system='Windows', node='LAPTOP-O6R63GS8', release='10', version='10.0.18362', machine='AMD64', processor='Intel64 Family 6 Model 92 Stepping 9, GenuineIntel')

def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print("Call Windows tasks")
    elif (sysstr == "Linux"):
        print("Call Linux tasks")
    else:
        print("Other System tasks")

if __name__ == "__main__":
    TestPlatform()
    UsePlatform()
