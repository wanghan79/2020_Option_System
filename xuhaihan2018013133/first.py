# coding=utf-8
"""
  Author:  XHH
  Purpose: 采用python语言获取操作系统信息；提示：使用Python内置platform工具包
  Created: 1/7/2020
"""

import platform

#platform模块用来访问平台相关属性

# 获取操作系统名称及版本号
print('操作系统名称及版本号: ', platform.platform())

# 获取操作系统名称
print('获取操作系统名称: ', platform.system())

# 获取操作系统版本号
print('获取操作系统版本号: ', platform.version())

# 获取操作系统的位数
print('获取操作系统的位数: ', platform.architecture())

# 计算机类型
print('计算机类型: ', platform.machine())

# 计算机的网络名称
print('计算机的网络名称: ', platform.node())

# 计算机处理器信息
print('计算机处理器信息: ', platform.processor())

# 包含上面所有的信息汇总
print('包含上面所有的信息汇总:')
print(platform.uname())

