# !/usr/bin/python3
"""
  Author:  RuiJia. Cao
  Purpose: Using Python language to realize windows command line calling.
  Created: 28/6/2020
"""

import os

os.system('dir')
os.system('java -version')
os.system('ipconfig')
os.system("calc")
os.system("cmd.exe")
os.system("appwiz.cpl")
os.system("certmgr.msc")
os.system('control')
os.system("cleanmgr")
os.system("iexpress")
os.system("cmstp")

order = input('Please enter your command:')

os.system(order)