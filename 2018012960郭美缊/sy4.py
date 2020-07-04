#给定文件夹我不知道在哪里，就用自己的文件夹了，序号代表几种方法
import os#1

for filename in os.listdir(r'D:\Googledownload\3DMGAME-CheatEnginev6.8.3CH\Cheat Engine 6.8.3'):

  print
  filename

import glob#2 可设置文件过滤
for filename in glob.glob(r'D:\Googledownload\3DMGAME-CheatEnginev6.8.3CH\Cheat Engine 6.8.3\*exe'):
    print
    filename

import os.path#3,有错误
def processDirectory(args,dirname,filename):
    print 'Directory',dirname
    for filename in filenames:
        print 'File',filename

os.path.walk(r'D:\Googledownload\3DMGAME-CheatEnginev6.8.3CH\Cheat Engine 6.8.3',processDirectory,None)

#4
for dirpath, dirnames, filenames in os.walk('D:\Googledownload\3DMGAME-CheatEnginev6.8.3CH\Cheat Engine 6.8.3'):
    print 'Directory', dirpath
    for filename in filenames:
        print ' File', filename