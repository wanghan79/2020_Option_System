# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: platform
  Created: 24/6/2020
"""
# 作业1. 采用python语言获取操作系统信息；提示：使用Python内置platform工具包

import platform

print(platform.platform())      # 获取操作系统名称及版本号，Windows-10-10.0.18362-SP0
print(platform.system())        # 获取操作系统名称，Windows
print(platform.version())       # 获取操作系统版本号，10.0.18362
print(platform.architecture())  # 获取操作系统的位数，('64bit', 'WindowsPE')
print(platform.machine())       # 计算机类型，AMD64
print(platform.node())          # 计算机的网络名称，DESKTOP-1OBE4SD
print(platform.processor())     # 计算机处理器信息，'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
print(platform.uname())         # 包含上面所有的信息汇总，uname_result(system='Windows', node='DESKTOP-1OBE4SD', release='10', version='10.0.18362', machine='AMD64', processor='Intel64 Family 6 Model 142 Stepping 10, GenuineIntel')
