import platform



print("操作系统及版本信息", platform.platform())
print('获取系统版本号', platform.version())
print('获取系统名称', platform.system())
print('系统位数', platform.architecture())
print('计算机类型', platform.machine())
print('计算机名称', platform.node())
print('处理器类型', platform.processor())
print('计算机相关信息', platform.uname())