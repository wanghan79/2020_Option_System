#!/usr/bin/env python
# coding: utf-8

# In[1]:

from multiprocessing import Process

def pro(i):
    print('running',i)

if __name__ == '__main__':

    p1 = Process(target=func)
    p1.start()


# In[ ]:




