#!/usr/bin/env python
#-*-coding:utf-8-*-

import platform
os=platform.system()#操
# 作系统platform库使用方法
print(os)
#print('')
print('OS名称及版本号:')
print(platform.platform())#OS名称及版本号
print('OS版本号')
print (platform.version())#OS版本号
print('os位数')
print (platform.architecture())#os位数
print('计算机类型')
print(platform.machine())
print('计算机的网络名称')
print(platform.node())
print('计算机处理信息')
print(platform.processor())
print('计算机信息汇总')
print(platform.uname())
print('python相关信息')
platform.python_build()
print(platform.python_compiler())
print(platform.python_branch())
print(platform.python_implementation())
print(platform.python_revision())
print(platform.python_version())
print(platform.python_version_tuple())