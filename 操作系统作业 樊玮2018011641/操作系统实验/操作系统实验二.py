'''
Author: WeiFan 2018011641
Aim:  python实现windows命令调用
Data: 2020/6/28
'''
import os
#cmd1='cmd.exe'
#os.system(cmd1)

#cmd2='D:\python'
#os.system(cmd2)

while True:
    cmd = input('[CMD]# ')
    if cmd:
        if cmd == 'exit' :
            print('logout')
            break
        else:
            print('Command is %s' %(cmd))
            os.system(cmd)
    else:
        print('You must enter true Command')
        continue