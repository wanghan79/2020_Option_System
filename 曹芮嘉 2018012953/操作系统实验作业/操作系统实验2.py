# !/usr/bin/python3
"""
  Author:  RuiJia. Cao
  Purpose: Using Python language to realize windows command line calling.
  Created: 28/6/2020
"""

import os

while True:
    cmd = input('Please enter the command!')
    os.system(cmd)