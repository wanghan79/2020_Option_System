#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os

def lif(pa):
    gl = []
    lists = os.listdir(pa)
    for i in range(0, len(lists)):
        paths = os.pa.join(pa, lists[i])
        if os.pa.isdir(paths):
            gl.extend(lif(paths))
        if os.pa.isfile(paths):
            gl.append(paths)
    return gl
pa = input('path:')
gl = lif(pa)
print(gl)


# In[ ]:




