import multiprocessing as mp


def run1(a, L):
    L.acquire()
    for _ in range(5):
        a.value = a.value + 3
        print(a.value)
    L.release()


def run2(a, L):
    L.acquire()
    for _ in range(5):
        a.value = a.value + 5
        print(a.value)
    L.release()

if __name__ == '__main__':
    v = mp.Value('i', 0)
    L = mp.Lock()
    p1 = mp.Process(target=run1, args=(v, L))
    p2 = mp.Process(target=run2, args=(v, L))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

