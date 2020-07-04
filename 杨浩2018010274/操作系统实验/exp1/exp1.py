import platform


def show_os_info():
    print('hardware info:')
    print('machine type:', platform.machine())
    print('processor info:', platform.processor())

    print('software info:')
    print('outline of OS:', platform.platform())
    print('bit architecture and linkage format:', platform.architecture())
    print('system’s network name:', platform.node())
    print('\n')


show_os_info()
#full info of OS
print(platform.uname())