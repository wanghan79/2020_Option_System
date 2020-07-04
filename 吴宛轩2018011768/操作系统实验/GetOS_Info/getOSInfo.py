"""
    Author:W
    Purpose:
    Created:2020-6-24
"""
import platform


class OSInfo:

    def get_OS(self):
        '''获取操作系统类型'''
        return platform.system()

    def get_platform(self):
        '''获取操作系统名称及版本号'''
        return platform.platform()

    def get_version(self):
        '''获取操作系统版本号'''
        return platform.version()

    def get_architecture(self):
        '''获取操作系统的位数'''
        return platform.architecture()

    def get_machine(self):
        '''获取计算机类型'''
        return platform.machine()

    def get_node(self):
        '''获取计算机网络名称'''
        return platform.node()

    def get_processor(self):
        '''获取计算机处理机信息'''
        return platform.processor()

    def get_allInfo(self):
        '''获取所有信息'''
        print("操作系统类型: " + self.get_OS())
        print("操作系统名称及版本号: " + self.get_platform())
        print("操作系统版本号: " + self.get_version())
        print("操作系统的位数: " + str(self.get_architecture()))
        print("计算机类型: " + self.get_machine())
        print("计算机网络名称: " + self.get_node())
        print("计算机处理机信息: " + self.get_processor())

class OSPythonInfo:

    def get_pythonBuildInfo(self):
        '''获取Python构建号和日期'''
        return platform.python_build()

    def get_pythonCompiler(self):
        '''获取用于编译Python的编译器'''
        return platform.python_compiler()

    def get_pythonBranch(self):
        '''获取Python实现SCM分支'''
        return platform.python_branch()

    def get_pythonImplementation(self):
        '''获取Python实现的字符串'''
        return platform.python_implementation()

    def get_pythonVersion(self):
        '''获取Python版本'''
        return platform.python_version()

    def get_pythonReversion(self):
        '''获取Python实现SCM修订'''
        return platform.python_revision()

    def get_pythonAllInfo(self):
        '''获取所有python信息'''
        print("Python构建号和日期: " + str(self.get_pythonBuildInfo()))
        print("Python的编译器: " + self.get_pythonCompiler())
        print("Python实现的SCM分支: " + self.get_pythonBranch())
        print("Python实现的字符串: " + self.get_pythonImplementation())
        print("Python版本: " + self.get_pythonVersion())
        print("Python实现的SCM修订: " + self.get_pythonReversion())


def main():
    print("-----------------------------------------------------------------------------------")
    os = OSInfo()
    os.get_allInfo()
    print("-----------------------------------------------------------------------------------")
    os_py = OSPythonInfo()
    os_py.get_pythonAllInfo()
    print("-----------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
