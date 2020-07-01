__author__ = '2018013343'
"""
Author: sun hejian
Purpose: create multiprocess
Created: 30/6/2020
"""

import multiprocessing
def do(n) :
  name = multiprocessing.current_process().name
  print(name,'starting')
  print("worker ", n)
  return

if __name__ == '__main__' :
  List = []
  for i in range(7) :
    m = multiprocessing.Process(target=do, args=(i,))
    List.append(m)
    m.start()#就绪
    print("Process end.")
  for i in List:
    i.join()
  print(List)
