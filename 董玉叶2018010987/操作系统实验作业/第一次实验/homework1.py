"""
Author: YY.Dong
Purpose: Using Python language to obtain operating system information
Created: 6/24/2020
"""
import platform
def apply():
        print('获取操作系统名称及版本号：',platform.platform() )       #获取操作系统名称及版本号，'Linux-3.13.0-46-generic-i686-with-Deepin-2014.2-trusty'
        print('获取操作系统版本号：',platform.version() )        #获取操作系统版本号，'#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015'
        print('获取操作系统的位数:', platform.architecture()  )   #获取操作系统的位数，('32bit', 'ELF')
        print('获取计算机类型：',platform.machine())         #计算机类型，'i686'
        print('获取计算机网络名称：',platform.node()  )          #计算机的网络名称，'XF654'
        print('获取计算机处理器信息：',platform.processor())       #计算机处理器信息，''i686'
        print('获取操作系统类型：',platform.system())
        print('以上信息汇总：',platform.uname())         #包含上面所有的信息汇总，('Linux', 'XF654', '3.13.0-46-generic', '#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015', 'i686', 'i686')


apply()
