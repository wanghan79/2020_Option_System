'''
Author: YixuanLiu
purpose:  python获取操作系统信息
Data: 2020/6/28
'''

import platform

def func(txt,info):
    print("{}:{}".format(txt,info))

func("操作系统及版本信息",platform.platform())
func("操作系统版本号",platform.version())
func("操作系统名称",platform.system())
func("系统位数",platform.architecture())
func("计算机类型",platform.machine())
func("计算机名称",platform.node())
func("处理器类型",platform.processor())
func("获取以上所有信息",platform.uname())
func("python编译信息",platform.python_build())
func("python版本信息",platform.python_version())
