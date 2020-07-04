#邹佳鑫第一次实验

import platform


def TestPlatform():
        #获取操作系统类型
        print platform.system()
        #计算机的网络名称
        print platform.node()
        #获取操作系统名称及版本号
        print platform.platform()
        #获取操作系统的位数
        print platform.architecture()
        # 计算机处理器信息
        print platform.processor()
        #获取计算机类型
        print platform.machine()
        #获取计算机处理机信息
        print platform.processor()
        #获取操作系统中Python的构建日期
        print platform.python_build()
        #获取系统中python解释器的信息
        print platform.python_compiler()

        if platform.python_branch() == "":
        print platform.python_implementation()
        print platform.python_revision()
        print platform.release()
        print platform.system()
        #信息汇总
        print platform.uname()
        
def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print ("Call Windows tasks")
    elif (sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Other System tasks")

if __name__ == '__main__':
    main()
