'''
Author: WeiFan 2018011641
Aim:  python获取操作系统信息
Data: 2020/6/28
'''
import platform

os=platform.platform()
print(os)
version=platform.version()
print(version)
bit=platform.architecture()
print(bit)
ctype=platform.machine()
print(ctype)
netname=platform.node()
print(netname)
processor=platform.processor()
print(processor)
uname=platform.uname()
print(uname)


build=platform.python_build()
print(build)
compiler=platform.python_compiler()
print(compiler)
branch=platform.python_branch()
print(compiler)
implementation=platform.python_implementation()
print(implementation)
revision=platform.python_revision()
print(revision)
version=platform.python_version()
print(version)
v_tuple=platform.python_version_tuple()
print(v_tuple)

