# coding=utf-8
"""
  Author:  XHH
  Purpose: 采用python语言实现windows命令行调用；提示：采用Python内置工具包os.system
  Created: 1/7/2020
"""

import os

# 例：查看系统信息
# cmd = 'winmsd'
# os.system('cmd')

while True:
    cmd = input('please input the correct cmd:\n')
    if cmd == 'exit':
        print('exit the process')
        break
    else:
        print('command is ', cmd)
        os.system(cmd)

#cmd命令举例
# 1. gpedit.msc-----组策略
# 2. sndrec32-------录音机
# 3. Nslookup-------IP地址侦测器使用
# 4. explorer-------打开资源管理器
# 5. logoff---------注销命令
# 6. shutdown-------60秒倒计时关机命令
# 7. lusrmgr.msc----本机用户和组
# 8. services.msc---本地服务设置
# 9. oobe/msoobe /a----检查XP是否激活
# 10. notepad--------打开记事本

