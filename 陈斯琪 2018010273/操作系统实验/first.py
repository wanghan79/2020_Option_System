##!/usr/bin/python3
# """
#   Author:  Sq.Chen
#   Purpose: Get information of OS
#   Created: 25/6/2020
# """

import platform

def show(name, info):
    print("{}:{}".format(name, info))


show("操作系统及版本信息", platform.platform())
show('获取系统名称', platform.system())
show('获取系统版本号', platform.version())
show('系统位数', platform.architecture())
show('计算机名称', platform.node())
show('计算机类型', platform.machine())
show('处理器类型', platform.processor())
show('计算机相关信息', platform.uname())
