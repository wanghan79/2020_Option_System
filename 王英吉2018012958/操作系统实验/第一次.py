import platform
def Platform():
    print(platform.machine())
    print(platform.node())
    print(platform.uname())
    print(platform.platform())
    print(platform.platform())
    print(platform.system())
    print(platform.version())
    print(platform.architecture())
    print(platform.processor())

if __name__ == "__main__":
    Platform()