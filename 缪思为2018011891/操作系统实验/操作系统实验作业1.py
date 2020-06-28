import platform as p

print("操作系统类型：",p.system())
print("操作系统名称及版本号：",p.platform())
print("操作系统版本号:",p.version())
print("操作系统的位数",p.architecture())
print("计算机类型:",p.machine())
print("计算机的网络名称",p.node())
print("计算机处理器信息:",p.processor())
print("所有的信息汇总:",p.uname())