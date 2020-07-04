##!/usr/bin/python3
'''

Author: By.Zhang
Purpose: get information by python.platform.
Created: 26/6/2020

'''

import platform


def get_OS():
    '''
    :Description:get information about operation system
    '''
    print("获取操作系统名称及版本号：", platform.platform())
    print("获取操作系统名称：", platform.system())
    print("获取操作系统的发行号：", platform.release())
    print("获取操作系统版本号：", platform.version())
    print("获取操作系统的位数：", platform.architecture())
    print("获取计算机架构类型：", platform.machine())
    print("获取计算机的网络名称：", platform.node())
    print("获取计算机处理器信息：", platform.processor())
    print("计算机信息汇总：", platform.uname())


def get_Python():
    '''
    :Description:get information about Python Interpreter
    '''
    print("获取Python解释器版本：", platform.python_branch())
    print("获取构建信息：", platform.python_build())
    print("获取编译器信息：", platform.python_compiler())
    print("获取解释器的发行版本：", platform.python_implementation())
    print("获取修订信息：", platform.python_revision())
    print("获取版本信息：", platform.python_version())
    print("以元组的形式返回版本信息：", platform.python_version_tuple())


def get_info():
    print("获取操作系统相关信息：")
    get_OS()
    print('\n')
    print("获取Python解释器相关信息：")
    get_Python()


get_info()
