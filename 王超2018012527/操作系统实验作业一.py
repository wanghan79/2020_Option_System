import platform


def get_system_Platform():
    print('system and bit')
    print(platform.architecture())  # 系统位数

    print('system and deatial')
    print(platform.platform())  # 系统信息

    print('system')
    print(platform.system())  # 系统类型


def myPlatform():
    sysstr = platform.system()
    if sysstr == "Windows":
        print("my platform is:" + "Windows platform")
    elif sysstr == "Linux":
        print("my platform is:" + "Linux platform")
    else:
        print("my platform is:" + "Others platform")


get_system_Platform()
myPlatform()
