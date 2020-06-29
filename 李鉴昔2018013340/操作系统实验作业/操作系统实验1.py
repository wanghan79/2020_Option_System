"""
  Author:  jianxi.li
  Purpose: homework1:采用python语言获取操作系统信息；提示：使用Python内置platform工具包
  Created: 26/6/2020
"""
import platform
def showinfo(notes, output):
 print("{}:{}".format(notes, output))
showinfo("操作系统及版本信息", platform.platform())
showinfo('计算机名称', platform.node())
showinfo('计算机类型', platform.machine())
showinfo('获取系统版本号', platform.version())
showinfo('获取系统名称', platform.system())
showinfo('系统位数', platform.architecture())
showinfo('处理器类型', platform.processor())
showinfo('计算机相关信息', platform.uname())