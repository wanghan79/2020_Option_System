import time
import multiprocessing


def do_somthing(senconds):
    '''
    description: This function's execution time is equal to senconds
    '''
    time.sleep(senconds)


def process_info(func):
    '''
    description: This is a decorator to require the inputs of execution time and outputs the summation of these times(t1)
    which is approxiamtely equal to the to total execution time in sync without multiprocessing
    '''
    def wrapper():
        num_of_processes = int(input("Please enter the number of processes\n"))
        exe_time = []
        print(f"please enter the time to execute for each of the {num_of_processes} processes")
        for _ in range(num_of_processes):
            t = int(input())
            exe_time.append(t)
        # calculate the total time to execute without multiprocessing
        t1 = 0
        for i in exe_time:
            t1 += i
        print('the total time without multiprogramming is', t1, 's')
        return func(exe_time)
    return wrapper


@process_info
def create_multiprocessing(exe_time):
    '''
    description；This function creates multiple processes and execute them concurrently, the number of processes to
    execute concurrently is depend on the loops for exe_time list, perf_couter function is used to get the start and the
    end time to calculate the total execution time(t2) in concurrency using multiprocessing.
    '''
    # calculate the total time using multiprocessing
    process = []
    start = time.perf_counter()
    for i in exe_time:
        p = multiprocessing.Process(target=do_somthing, args=[i])
        process.append(p)
        p.start()    # each process starts
    for p in process:
        p.join()     # the corresponding process ends
    finish = time.perf_counter()
    t2 = finish - start
    print('the total time using multiprocessing is', t2, 's')


@process_info
def create_multiprocessing_by_pool(exe_time):
    '''
    pool is another method to realize multiprocessing, the capacity of pool can be adjusted.
    '''
    capacity = int(input('''please enter pool capacity\n'''))
    with multiprocessing.Pool(capacity) as p:
        start = time.perf_counter()
        p.map(do_somthing, exe_time)
        finish = time.perf_counter()
        t2 = finish - start
        print('the total time using multiprocessing by pool is', t2, 's')

if __name__ == '__main__':
    '''print('test create_multiprocessing')
    create_multiprocessing()'''
    print('test create_multiprocessing_by_pool')
    create_multiprocessing_by_pool()

'''
test case for create_multiprocessing:
Please enter the number of processes
3
please enter the time to execute for each of the 5 processes
1
2
1

test case for create_multiprocessing_by_pool:
Please enter the number of processes
5
please enter the time to execute for each of the 5 processes
1
2
1
please enter pool capacity
3
'''