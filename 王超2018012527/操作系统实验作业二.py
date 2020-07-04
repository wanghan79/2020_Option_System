import os
from threading import Thread


def execute_cmd_command():
    os.system("calc")  # 启动计算器
    os.system("cleanmgr")  # 打开磁盘清理工具
    os.system("CompMgmtLauncher")  # 计算机管理
    os.system("control")  # 控制面版
    os.system("diskmgmt.msc")  # 磁盘管理


for i in range(5):
    t = Thread(target=execute_cmd_command, args=("执行命令",))
    t.start()
