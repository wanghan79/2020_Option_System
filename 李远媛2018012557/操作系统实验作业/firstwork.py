'''
    Author: Yy.Li
    Purpose:The Python language is used to obtain operating system information
    Created:30/6/2020
'''

import platform
os = platform.system()

def show_os_info():
    print("操作系统名称及版本号：{}".format(platform.platform()))
    print("操作系统版本号：{}".format(platform.version()))
    print("操作系统的位数：{}".format(platform.architecture()))
    print("操作系统类型：{}".format(platform.system()))
    print("计算机类型：{}".format(platform.machine()))
    print("计算机的网络名称：{}".format(platform.node()))
    print("计算机处理器信息：{}".format(platform.processor()))
    print("所有的信息汇总：{}".format(platform.uname()))

def show_python_info():
    print("the Python build number and date as strings: {}".format(platform.python_build()))
    print("Returns a string identifying the compiler used for compiling Python: {}".format(platform.python_compiler()))
    print("Returns a string identifying the Python implementation SCM branch: {}".format(platform.python_branch()))
    print("Returns a string identifying the Python implementation: {}".format(platform.python_implementation()))  #Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’
    print("Returns the Python version as string 'major.minor.patchlevel': {}".format(platform.python_version()))
    print("Returns a string identifying the Python implementation SCM revision: {}".format(platform.python_revision()))
    print("Returns the Python version as tuple (major, minor, patchlevel) of strings: {}".format(platform.python_version_tuple()))

def main():
    print("操作系统信息：")
    show_os_info()
    print("#" * 50)
    print("计算机中的python信息：")
    show_python_info()

if __name__ == '__main__':
    main()
