#作业1. 采用python语言获取操作系统信息；提示：使用Python内置platform工具包;
"""
  Author:  Jiaza.Xin
  Purpose: Get operating system information in python language.
  Created: 28/6/2020
"""

import platform
def show_osinfo(tip, info):
    print("{}:{}".format(tip,info))#--------------Python format 格式化函数：不设置指定位置，按默认顺序


def apply():
    show_osinfo("操作系统及版本信息",platform.platform())
    show_osinfo('获取系统版本号',platform.version())
    show_osinfo('获取系统名称', platform.system())
    show_osinfo('系统位数', platform.architecture())
    show_osinfo('计算机类型', platform.machine())
    show_osinfo('计算机名称', platform.node())
    show_osinfo('处理器类型', platform.processor())
    show_osinfo('计算机相关信息', platform.uname())