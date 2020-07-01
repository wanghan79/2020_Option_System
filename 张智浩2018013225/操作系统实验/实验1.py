import platform
print("操作系统类型：", platform.system())
print("操作系统名称及版本号：", platform.platform())
print("操作系统版本号:",platform.version())
print("操作系统位数", platform.architecture())
print("计算机类型:",platform.machine())
print("计算机名称", platform.node())
print("处理器信息:", platform.processor())
print("所有的信息汇总:",platform.uname())