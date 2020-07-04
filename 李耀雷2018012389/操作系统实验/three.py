from multiprocessing import Process
import time


class apply(Process):
    def __init__(self, arg):
        super(apply, self).__init__()
        self.arg = arg

    def run(self):
        print('print', self.arg)
        time.sleep(2)


if __name__ == '__main__':
    for i in range(100):
        p = apply(i)
        p.start()

