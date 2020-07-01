import platform

#获取操作系统名称及版本号
def get_platform():
    return platform.platform()

#获取操作系统版本号
def get_version():
    return platform.version()

#获取操作系统的位数
def get_architecture():
    return platform.architecture()

#计算机类型
def get_machine():
    return platform.machine()

#计算机网络名称
def get_node():
    return platform.node()

#计算机处理信息
def get_processor():
    return platform.processor()

#获取操作系统类型
def get_system():
    return platform.system()

#汇总信息
def get_uname():
    return platform.uname()


def show_os_all_info():
    '''打印os的全部信息'''

    print('操作系统名称及版本号：%s' % get_platform())
    print('操作系统版本号：%s' % get_version())
    print('操作系统的位数：%s' % str(get_architecture()))
    print('计算机类型：%s' % get_machine())
    print('计算机网络名称：%s' % get_node())
    print('计算机处理信息：%s' % get_processor())
    print('获取操作系统类型：%s' % get_system())
    print('汇总信息：%s' % str(get_uname()))

if __name__ == '__main__':
    show_os_all_info()