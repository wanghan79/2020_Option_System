import os
#import commands
import shutil
#1
pipeline = os.popen("ls")
print(pipeline.read())#类似于C中system函数，无法获取到运行命令的输出

os.system("mv ./test ./rename_test")


p=subprocess.Popen("ls",shell=True)
p.wait()

p=subprocess.Popen("ls",shell=True,stdout=subprocess.PIPE,universal_newlines=True)
p.wait()
result_lines=p.stdout.readlines()
for line in result_lines:
   print(line.strip())
   import sys
    #获取命令行参数

    print("脚本名：", sys.argv[0])
    for i in range(1, len(sys.argv)):
        print("参数", i, ":", sys.argv[i])
#2
import commands
(status,output)=commands.getstatusoutput("ls")
print status
print output
testSystem.py