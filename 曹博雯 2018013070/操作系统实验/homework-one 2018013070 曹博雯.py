"""
    Author:
        BowenCao
        2018013070

    Purpose:
        用python语言获取操作系统信息

    Created: 24/6/2020
"""
import platform


def get_platform():
    '''
     :Description: 获取操作系统名称及版本号
    '''
    return platform.platform()


def get_version():
    '''
    :Description: 获取操作系统版本号
    '''
    return platform.version()


def get_architecture():
    '''
    :Description: 获取操作系统的位数
    '''
    return platform.architecture()


def get_machine():
    '''
    :Description: 计算机类型
    '''
    return platform.machine()


def get_node():
    '''
    :Description: 计算机的网络名称
    '''
    return platform.node()


def get_processor():
    '''
    :Description: 计算机处理器信息
    '''
    return platform.processor()


def get_system():
    '''
    :Description: 获取操作系统类型
    '''
    return platform.system()


def get_uname():
    '''
    :Description: 汇总信息
    '''
    return platform.uname()


def show_os_all_info():
    '''
    :Description: 打印os的全部信息
    '''
    print('获取操作系统名称及版本号 : [{}]'.format(get_platform()))
    print('获取操作系统版本号 : [{}]'.format(get_version()))
    print('获取操作系统的位数 : [{}]'.format(get_architecture()))
    print('计算机类型 : [{}]'.format(get_machine()))
    print('计算机的网络名称 : [{}]'.format(get_node()))
    print('计算机处理器信息 : [{}]'.format(get_processor()))
    print('获取操作系统类型 : [{}]'.format(get_system()))
    print('汇总信息 : [{}]'.format(get_uname()))


def test():
    show_os_all_info()


if __name__ == '__main__':
    test()