'''
Author: Zhang yuxuan
purpose:  Get information
Date: 2020/6/30
'''


import platform
print("操作系统版本信息", platform.platform())
print('系统版本号', platform.version())
print('系统名称', platform.system())
print('系统位数', platform.architecture())
print('计算机类型', platform.machine())
print('网络名称', platform.node())
print("处理器名称", platform.processor())
print("python编译信息", platform.python_build())
print("python版本信息", platform.python_version())
