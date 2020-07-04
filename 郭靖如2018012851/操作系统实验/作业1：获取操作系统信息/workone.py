"""
Author:Guojr
Purpose:获取操作系统信息
Time:
"""
import platform

'''
os名称和版本号
输出windows-10-10.0.18362-SP0
'''
def get_platform():
    return platform.platform()
print(get_platform())

'''
os版本号
输出10.0.18362
'''
def get_version():
    return platform.version()
print(get_version())

'''
os的位数
输出('64bit', 'WindowsPE')
'''
def get_architecture():
    return platform.architecture()
print(get_architecture())

'''
计算机类型
输出AMD64
'''
def get_machine():
    return platform.machine()
print(get_machine())

'''
计算机的网络名称
输出GJR
'''
def get_node():
    return platform.node()
print(get_node())

'''
计算机处理器信息
输出Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
'''
def get_processor():
    return platform.processor()
print(get_processor())

'''
获取操作系统类型
输出Windows
'''
def get_system():
    return platform.system()
print(get_system())

'''
汇总信息
输出uname_result(system='Windows', node='GJR', release='10', version='10.0.18362', 
machine='AMD64', processor='Intel64 Family 6 Model 142 Stepping 10, GenuineIntel')
'''
def get_uname():
    return platform.uname()
print(get_uname())