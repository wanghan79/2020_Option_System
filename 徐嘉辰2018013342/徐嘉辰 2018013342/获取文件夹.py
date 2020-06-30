import os
result=[]
def search(path=".", name=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            search(item_path)
        elif os.path.isfile(item_path):
            global result
            result.append(item_path + ";")
            print (item_path + ";", end="")
search(path=r"D:\newfile")
