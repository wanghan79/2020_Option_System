import os
def get_name(path):

    file_list = []

    list = os.listdir(path)
    for i in range(0, len(list)):
        path_2 = os.path.join(path, list[i])
        if os.path.isfile(path_2):
            file_list.append(path_2)
        if os.path.isdir(path_2):
            file_list.extend(get_name(path_2))
    return file_list
path=input("请输入路径：")
ans=get_name(path)
print(ans)