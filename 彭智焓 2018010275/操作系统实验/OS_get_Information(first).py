# encoding:utf-8
'''
@name    :   OS_get_Information
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/7/1          ZH.Peng    2018010275
'''
import platform
class OS_get_Information(object):
    def __init__(self):
        self.platform = "操作系统及版本信息"
        self.version = "操作系统版本号"
        self.system = "操作系统名称"
        self.architecture = "系统位数"
        self.machine = "计算机类型"
        self.node = "计算机名称"
        self.processor = "处理器类型"
        self.uname = "获取以上所有信息"
    
    def get_platform(self):
        print("{}:{}".format(self.platform, platform.platform()))

    def get_version(self):
        print("{}:{}".format(self.version, platform.version()))

    def get_system(self):
        print("{}:{}".format(self.system, platform.system()))

    def get_architecture(self):
        print("{}:{}".format(self.architecture, platform.architecture()))

    def get_machine(self):
        print("{}:{}".format(self.machine, platform.machine()))

    def get_node(self):
        print("{}:{}".format(self.node, platform.node()))

    def get_processor(self):
        print("{}:{}".format(self.processor, platform.processor()))

    def get_uname(self):
        print("{}:{}".format(self.uname, platform.uname()))

    def get_informations(self):
        print(self.platform)
        self.get_platform()
        self.get_version()
        self.get_system()
        self.get_architecture()
        self.get_machine()
        self.get_node()
        self.get_processor()
        self.get_uname()
if __name__ == "__main__":
    os_info = OS_get_Information()
    os_info.get_informations()