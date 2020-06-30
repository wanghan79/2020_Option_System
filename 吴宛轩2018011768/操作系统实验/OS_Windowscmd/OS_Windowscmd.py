# -*-coding:utf-8-*-
"""
    Author:W
    Purpose:
    Created:2020-6-24
"""
import os


class cmdTest:
    '''直接调用命令行'''
    def useCMD(self):
        os.system('cmd')

    '''一些命令的样例'''
    def get_javaInfo(self):
        '''获取java信息'''
        return os.system('java -version')

    def get_IP(self):
        '''IP信息'''
        return os.system('ipconfig')

    def get_dir(self):
        '''获取目录信息'''
        return os.system('dir')


def main():
    osTest = cmdTest()
    osTest.get_javaInfo()
    print("----------------------------------------------------------------------")
    osTest.get_IP()
    print("----------------------------------------------------------------------")
    osTest.get_dir()
    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    main()
