import os

def print_files(path):
    root=path
    path_list=[]
    list=os.listdir(root)
    for i in range(0,len(list)):
        com_path=os.path.join(root,list[i])
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(path(com_path))

    return path_list

path=input("你想查看的路径信息：")
ans=print_files(path)
print(ans)
