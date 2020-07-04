import os

os.getcwd()  # 获取当前路径

os.chdir("C:\\Users\\Administrator\\Desktop\\图片")  # 设置文件夹所在的位置

os.listdir(".")
os.chdir("C:\\Users\\Administrator\\Desktop\\图片")
filename=os.listdir(".")
name=[]
for i in filename:
      portion = os.path.splitext(i)
      if portion[1] == ".zip":
       name.append(portion[0])
      if portion[1] == ".png":
       name.append(portion[0])
