import platform

def Platform():
    print('计算机类型：',platform.machine())
    print('计算机网络名称：',platform.node())
    print('计算机信息：',platform.uname())
    print("操作系统名称：",platform.platform())
    print("操作系统版本信息：",platform.platform())
    print('操作系统系统版本号：',platform.version())
    print('操作系统位数：',platform.architecture())
    print('处理器信息：',platform.processor())

if __name__ == "__main__":

    Platform()