'''
Description:Implement windows command line call
Author:li tong

'''
import os
def call():

    os.system('ipconfig') #查询IP
    os.system('dir ') #查看当前目录下所有子文件
    os.system('cd c:/users &&mkdir aaa.txt')#执行多条语句
    os.system('start ping www.nenu.edu.cn -t')  #向百度不间断发送数据包测试网络连通性
call()