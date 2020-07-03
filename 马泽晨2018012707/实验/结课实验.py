import os



def get_file(path):

    path_list = []

    list = os.listdir(path)

    for i in range(0, len(list)):

        re_path = os.path.join(path, list[i])

        if os.path.isfile(re_path):

            path_list.append(re_path)

        if os.path.isdir(re_path):

            path_list.extend(get_file(re_path))

    return path_list



if __name__ == '__main__':

    scanf_path=('E:\mazc')

    print(get_file(scanf_path))