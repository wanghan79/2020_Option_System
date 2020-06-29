"""
  Author:  jianxi.li
  Purpose: homework4:采用Python语言获取操作系统下给定文件目录下的所有文件及文件夹（包括子文件夹），并输出到屏幕；提示：采用Python内置工具包os.path
  Created: 28/6/2020
"""
import os
def print_list_dir(dir):
 files = os.listdir(dir)
 for file in files:
  file = os.path.join(dir, file)
  if os.path.isfile(file):
   print(file)
  if os.path.isdir(file):
   print_list_dir(file)
if __name__ == '__main__':
 dir_paths = 'D:\学习\C  program\小程序'#在这里更改文件位置
 print_list_dir(dir_paths)