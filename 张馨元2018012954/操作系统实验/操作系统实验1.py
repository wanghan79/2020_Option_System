import platform

def Platform():

  print('计算机类型', platform.machine())

  print('计算机名称', platform.node())

  print('计算机相关信息', platform.uname())

  print("操作系统", platform.platform())

  print("版本信息", platform.platform())

  print('系统名称', platform.system())

  print('系统版本号', platform.version())

  print('系统位数', platform.architecture())

  print('处理器类型', platform.processor())

if __name__ == "__main__":

    Platform()