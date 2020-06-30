#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 17:01
# @Author  : liyuhan
# @File    : firsthw.py

#实验一
#采用python语言获取操作系统信息；提示：使用Python内置platform工具包

import platform

def get_platform():
    '''获取操作系统名称及版本号'''
    return platform.platform()


def get_version():
    '''获取操作系统版本号'''
    return platform.version()


def get_architecture():
    '''获取操作系统的位数'''
    return platform.architecture()


def get_machine():
    '''计算机类型'''
    return platform.machine()


def get_node():
    '''计算机的网络名称'''
    return platform.node()


def get_processor():
    '''计算机处理器信息'''
    return platform.processor()


def get_system():
    '''获取操作系统类型'''
    return platform.system()


def get_uname():
    '''汇总信息'''
    return platform.uname()


def get_python_build():
    ''' 获取Python构建号和日期'''
    return platform.python_build()


def get_python_compiler():
    '''获取用于编译Python的编译器'''
    return platform.python_compiler()


def get_python_branch():
    '''获取Python实现SCM分支'''
    return platform.python_branch()


def get_python_implementation():
    '''获取Python实现的字符串'''
    return platform.python_implementation()


def get_python_version():
    '''获取Python版本'''
    return platform.python_version()


def get_python_revision():
    '''获取Python实现SCM修订'''
    return platform.python_revision()


def get_python_version_tuple():
    '''获取python实现的数组'''
    return platform.python_version_tuple()


def show_os_all_info():
    '''打印os的全部信息'''
    print('获取操作系统名称及版本号 : [{}]'.format(get_platform()))
    print('获取操作系统版本号 : [{}]'.format(get_version()))
    print('获取操作系统的位数 : [{}]'.format(get_architecture()))
    print('计算机类型 : [{}]'.format(get_machine()))
    print('计算机的网络名称 : [{}]'.format(get_node()))
    print('计算机处理器信息 : [{}]'.format(get_processor()))
    print('获取操作系统类型 : [{}]'.format(get_system()))
    print('汇总信息 : [{}]'.format(get_uname()))



def show_python_all_info():
    '''打印python的全部信息'''
    print('获取Python构建号和日期: [{}]'.format(get_python_build()))
    print('获取用于编译Python的编译器: [{}]'.format(get_python_compiler()))
    print('获取Python实现SCM分支: [{}]'.format(get_python_branch()))
    print('获取Python实现的字符串: [{}]'.format(get_python_implementation()))
    print('获取Python版本: [{}]'.format(get_python_version()))
    print('获取Python实现SCM修订: [{}]'.format(get_python_revision()))
    print('获取python实现的数组 : [{}]'.format(get_python_version_tuple()))


def main():
    print('操作系统信息:')
    show_os_all_info()
    print('计算机中的python信息：')
    show_python_all_info()


if __name__ == '__main__':
    main()