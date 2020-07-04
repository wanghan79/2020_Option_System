##!/usr/bin/python3
"""
  Author:  ZhengPeng.Han
  Purpose: Get infomation of the operating system by a built-in function of python,which named platform.
  Created: 26/6/2020
"""
import platform
def TestPlatform():
    print("----------Operation System Info--------------------------")
    print('The version of Python is:',platform.python_version())#  获取Python版本
    print('The structure of OS executable is:',platform.architecture())#   获取操作系统可执行程序的结构
    print('The network name of the computer is:',platform.node())#   计算机的网络名称
    print('The name of OS and version number is:',platform.platform())# 获取操作系统名称及版本号
    print('The computer processor information is:',platform.processor())# 计算机处理器信息
    print('The build date for Python on the OS is:',platform.python_build())# 获取操作系统中Python的构建日期
    print('The information about the Python interpreter in the OS is:',platform.python_compiler()) #  获取系统中python解释器的信息
    if platform.python_branch() == "":
        print('The Python implementation is:',platform.python_implementation())
        print('The Python implementation SCM revision is:',platform.python_revision())
    print('The release information is:',platform.release())
    print('The operating system is:',platform.system())#获取此电脑使用什么操作系统
    print('The OS version is:',platform.version())#  获取操作系统的版本
    print('All the information is:',platform.uname())#  包含上面所有的信息汇总



if __name__ == "__main__":
    TestPlatform()
