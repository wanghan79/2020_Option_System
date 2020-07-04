import os

# 递归查询所有目录和文件
def get_all_files(dir):
    files_ = []
    list_ = os.listdir(dir)
    for i in range(0, len(list_)):
        path = os.path.join(dir, list_[i])
        if os.path.isdir(path):
            files_.append(path)
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_

filePath = get_all_files("e:\\python_project_local\\echart")
for i in filePath:
    print(i)