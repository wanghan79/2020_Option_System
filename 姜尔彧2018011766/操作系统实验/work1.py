# coding=utf-8
"""
  Author:  Jiang Eryu
  Purpose: 使用Python内置platform工具包获取操作系统信息
  Created: 28/6/2020
"""

# --------------实验说明----------------
# 使用Python内置platform工具包获取操作系统信息

import platform


def TestPlatform():
    print ("----------Operation System----------")
    #  获取Python版本
    print platform.python_version()

    #   获取操作系统可执行程序的结构
    print platform.architecture()

    #   计算机的网络名称
    print platform.node()

    # 获取操作系统名称及版本号
    print platform.platform()

    # 计算机处理器信息
    print platform.processor()

    # 获取操作系统中Python的构建日期
    print platform.python_build()

    #  获取系统中python解释器的信息
    print platform.python_compiler()

    if platform.python_branch() == "":
        print platform.python_implementation()
        print platform.python_revision()
    print platform.release()
    print platform.system()

    # print platform.system_alias()
    #  获取操作系统的版本
    print platform.version()

    #  包含上面所有的信息汇总
    print platform.uname()


def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print ("Call Windows tasks")
    elif (sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Other System tasks")


if __name__ == "__main__":
    TestPlatform()

    UsePlatform()
