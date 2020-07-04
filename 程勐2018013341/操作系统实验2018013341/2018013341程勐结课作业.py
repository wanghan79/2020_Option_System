import os

def show_files(path,n):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            for i in range(n):
                print(end='\t')
            print(cur_path)
            show_files(cur_path,n+1)
        else:
            for i in range(n):
                print(end='\t')
            print(file)

contents = show_files("C:desktop\杂\",0)
