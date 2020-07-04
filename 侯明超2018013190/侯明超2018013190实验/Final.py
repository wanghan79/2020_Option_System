import os

path = r"C:\Users\似是而非\Desktop\数据结构"
dirs = os.listdir( path )

print('数据结构\n')
for file in dirs:
   print(file)