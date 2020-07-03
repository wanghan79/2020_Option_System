"""
Author   :  Yihang.Gao  高艺航
StuNumber: 2018012950
Purpose  : Get OS Imformation
Created  : 1/7/2020
"""
import platform

print("操作系统版本信息：", platform.platform())
print('系统名称        ：', platform.system())
print('系统版本号      ：', platform.version())
print('系统位数        ：', platform.architecture())
print('计算机类型      ：', platform.machine())
print('计算机名称      ：', platform.node())
print('处理器类型      ：', platform.processor())
print('计算机相关信息  ：', platform.uname())