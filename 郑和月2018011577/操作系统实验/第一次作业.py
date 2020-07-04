import platform

def showinfo(tip, info):
    print("{}:{}".format(tip, info))

showinfo("操作系统名称及版本号", platform.platform())
showinfo("获取操作系统名称", platform.system())
showinfo("获取操作系统版本号", platform.version())
showinfo("获取操作系统的位数", platform.architecture())
showinfo("计算机类型", platform.machine())
showinfo("计算机的网络名称", platform.node())
showinfo("计算机处理器信息", platform.processor())
showinfo("包含上面所有的信息汇总", platform.uname())      
