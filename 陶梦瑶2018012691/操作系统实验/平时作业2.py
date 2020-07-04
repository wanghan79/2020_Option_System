import os

def test():
    os.system('cd /usr/local')
    os.mkdir('tmy')

    libs = {"numpy", "matplotlib",  "pandas"}
    try:
        for lib in libs:
            os.system("pip install " + lib)
        print("Successful")
    except:
        print("Failed Somehow")
test()




