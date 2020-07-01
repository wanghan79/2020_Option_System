
import os

def get_all_path(path):
    rootdir = path
    lists = []
    list = os.listdir(path)
    for i in range(0, len(list)):
        new_path = os.path.join(path, list[i])
        if os.path.isfile(new_path):
            lists.append(new_path)
        if os.path.isdir(new_path):
            lists.extend(get_all_path(new_path))
    return lists
