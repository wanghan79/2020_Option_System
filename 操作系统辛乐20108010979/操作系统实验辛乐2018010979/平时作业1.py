import platform

print("操作系统类型：" + platform.system()) #获取操作系统类型
print("操作系统名称及版本号:" + platform.platform())  #获取操作系统名称及版本号
print("操作系统的位数:" + str(platform.architecture())) #获取操作系统的位数
print("计算机类型：" + platform.machine()) #获取计算机类型
print("计算机网络名称：" + platform.node()) #获取计算机网络名称
print("计算机处理器名称：" + platform.processor()) #获取计算机处理器名称
print("汇总以上信息:" + str(platform.uname())) #汇总以上信息
