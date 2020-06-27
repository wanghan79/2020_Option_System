import os

def get_path(path):
    lists = []
    list = os.listdir(path)
    for i in range(0, len(list)):
        new_path = os.path.join(path, list[i])
        if os.path.isfile(new_path):
            lists.append(new_path)
        if os.path.isdir(new_path):
            lists.extend(get_path(new_path))
    return lists
path = input('输入目标路径')
lists = []
lists = get_path(path)
print(lists)