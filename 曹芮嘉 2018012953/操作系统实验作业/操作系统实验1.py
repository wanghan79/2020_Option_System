# !/usr/bin/python3
"""
  Author:  RuiJia. Cao
  Purpose: Get operating system information.
  Created: 27/6/2020
"""
import platform
def showinfo(tips, result):
    print("{}:{}".format(tips, result))

showinfo("操作系统及版本信息", platform.platform())
showinfo('获取系统版本号', platform.version())
showinfo('获取系统名称', platform.system())
showinfo('系统位数', platform.architecture())
showinfo('计算机类型', platform.machine())
showinfo('计算机名称', platform.node())
showinfo('处理器类型', platform.processor())
showinfo('计算机相关信息', platform.uname())
