import os

def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result

if __name__ == "__main__":
    allPath = all_path(r"D:\python-pycharm")
    print(allPath)
    
