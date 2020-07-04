"""
    Author: Dd.Li
    Purpose: 采用python语言获取操作系统信息
    Created: 2/7/2020
"""

import platform

def os_info():
    print('操作系统及版本信息：[{}]'.format(platform.platform()))
    print('操作系统版本号：[{}]'.format(platform.version()))
    print('操作系统类型：[{}]'.format(platform.system()))
    print('操作系统位数：[{}]'.format(platform.architecture()))
    print('计算机类型：[{}]'.format(platform.machine()))
    print('计算机的网络名称：[{}]'.format(platform.node()))
    print('计算机处理器信息：[{}]'.format(platform.processor()))
    print('汇总信息：[{}]'.format(platform.uname()))


def main():
    print("操作系统信息：")
    os_info()   # 获取操作系统信息


if __name__ == '__main__':
    main()