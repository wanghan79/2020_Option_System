"""
Author: ShuMing.Bai
Purpose: Second: Implement Windows command line calls
Created: 6/24/2020
"""
import os

# 调用命令行
os.system('cmd') #可直接在控制台输入命令行命令
# 获取IP配置信息
os.system('ipconfig')
# 使用多条命令
os.system('cd ../ && mkdir test')
# 显示目录信息
os.system('dir')
# 创建目录
os.system('md movie music')
# 删除目录
os.system('rd movie')
