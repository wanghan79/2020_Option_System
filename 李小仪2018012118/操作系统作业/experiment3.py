##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:Create multiple processes
      Created:1/7/2020
"""
import os
from multiprocessing import Process,Pool
import os,time

def run_proc(name):
    for i in range(5):
        time.sleep(0.2)
        print('Run child process %s (%s)' %(name, os.getpid()))

if __name__ =='__main__':
      print('Run the main process (%s).' %(os.getpid()))
      mainStart = time.time()
      p = Pool(8)
      for i in range(16):
          p.apply_async(run_proc,args=('Process'+str(i),))
      print("Waiting for all subprocesses done ...")
      p.close()
      p.join()
      print("All subprocesses done")
      mainEnd = time.time()
      print('All process ran %0.2f seconds.' %(mainEnd-mainStart))
