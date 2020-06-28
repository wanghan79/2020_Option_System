'''
Author: YixuanLiu
purpose: python实现windows命令调用
Data: 2020/6/28
'''

import os

print("Print exit to quit")
while (1):
    cmd = input('Enter command:   ')
    if cmd == 'exit':
        break
    else:
        try:
            os.system(cmd)
            print("—————————————————————————————————————————————————————")
        except Exception as e:
            print(e)
        else:
            continue