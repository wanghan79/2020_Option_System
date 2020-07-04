import os
def print_list_dir(root_path):
    dir_files = os.listdir(root_path)
    for f in dir_files:
        file_path = os.path.join(root_path, f)
        if os.path.isfile(file_path):
            print(file_path)
        if os.path.isdir(file_path):
            print_list_dir(file_path)
if __name__ == '__main__':
    dir_path = ' your path'
    print_list_dir(dir_path)