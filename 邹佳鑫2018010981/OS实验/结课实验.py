#邹佳鑫结课实验

import os
def get_filelist(root_path):
for root, dirs, files in os.walk(root_path):  
        for file in files: 
            file_path = os.path.joile) 
            filepaths.append(file_path) 
        for dir in dirs: 
            dir_path = os.path.join(root, dir) 
            all_files_path(dir_path) 
if __name__ == '__main__':
    list = get_filelist
    print("共有文件：")
    print(len(list))
    for i in list:
        print(i)
