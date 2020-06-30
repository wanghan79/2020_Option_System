import os

image_path = 'F://test//frames'


# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
def get_filelist(dir, Filelist):

    if os.path.isfile(dir):
        Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist


if __name__ == '__main__':
    list = get_filelist('F://test//frames', [])
    print(len(list))
    for e in list:
        print(e)
