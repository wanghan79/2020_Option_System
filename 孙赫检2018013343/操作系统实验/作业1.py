__author__ = '2018013343'
"""
Author: sun hejian
Purpose: get os information
Created: 28/6/2020
"""
import platform
os = platform.system()
print(os)
def get_platform():
    return platform.platform()
def get_version():
    return platform.version()
def get_architecture():
    return platform.architecture()
def get_machine():
    return platform.machine()
def get_node():
    return platform.node()
def get_processor():
    return platform.processor()
def get_system():
    return platform.system()
def get_uname():
    return platform.uname()

def show_os_all_info():
    print('操作系统名称及版本号 : [{}]'.format(get_platform()))
    print('操作系统版本号 : [{}]'.format(get_version()))
    print('操作系统的位数 : [{}]'.format(get_architecture()))
    print('计算机类型 : [{}]'.format(get_machine()))
    print('计算机的网络名称 : [{}]'.format(get_node()))
    print('计算机处理器信息 : [{}]'.format(get_processor()))
    print('操作系统类型 : [{}]'.format(get_system()))
    print('汇总信息 : [{}]'.format(get_uname()))

def main():
    print('操作系统信息:')
    show_os_all_info()

main()
