import multiprocessing


def fun(n):
    name = multiprocessing.current_process().name

    print(name, 'starting')

    print("worker ", n)

    return


if __name__ == '__main__':

    numList = []

    for i in range(5):
        p = multiprocessing.Process(target=fun, args=(i,))

        numList.append(p)

        p.start()

        p.join()

        print("Process end.")
