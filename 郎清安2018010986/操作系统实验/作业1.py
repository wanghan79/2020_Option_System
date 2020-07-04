import platform
#借鉴于维基百科
print("获取操作系统名称及版本号:", platform.platform())
print('获取操作系统版本号:', platform.version())
print('获取操作系统的位数:', platform.architecture())
print('计算机类型:', platform.machine())
print('计算机的网络名称:', platform.node())
print('计算机处理器信息:', platform.processor())
print('包含上面所有的信息汇总:', platform.uname())