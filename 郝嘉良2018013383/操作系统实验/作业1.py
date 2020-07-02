import platform

pf = platform.platform()        #获取操作系统名称及版本号
sys = platform.system()          #获取操作系统名称
ver = platform.version()         #获取操作系统版本号
at = platform.architecture()    #获取操作系统的位数
machine = platform.machine()         #计算机类型
node = platform.node()            #计算机的网络名称
pro = platform.processor()       #计算机处理器信息
uname = platform.uname()           #包含上面所有的信息汇总

print(pf)
print(sys)
print(ver)
print(at)
print(machine)
print(node)
print(pro)
print(uname)