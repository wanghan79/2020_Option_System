"""
Author:Chenjiaying
Purpose:用python语言获取操作系统信息
Created:30/6/2020
"""
import platform

def os():
    print("操作系统名称及版本信息：", platform.platform())
    print("获取操作系统名称：", platform.system())
    print("获取操作系统的发行号：", platform.release())
    print("获取操作系统版本号：", platform.version())
    print("操作系统的位数：", platform.architecture())
    print("计算机类型：", platform.machine())
    print("计算机名称：", platform.node())
    print("计算机处理器信息：", platform.processor())
    print("计算机信息汇总：", platform.uname())

os()
