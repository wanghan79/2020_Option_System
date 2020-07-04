# -*- coding:utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Third OS experiment homework in spring semester, 2020
    
    Introduction:
        To simulating OneProducer_MultiConsumer problem
        
    Special Tips:
        It's a decorative class
        a fasta file is needed for using this(an example fasta file has been offered in the same dic)
        
    Created: 27/5/2020
    
    Last modified: 27/5/2020
"""
from SimpleFastaDealer import SimpleFastaDealer
import multiprocessing
import random
import time
import os

    

    
#-------------------------------------------------------------------------------------------------------------------
def Producer(queue,lock):
    '''
    Introduction
    ------------
    Producer, it's a decorative class that produce one fasta sequence from the fasta file
    
    
    Parameters
    ----------
    gener: the generator of fasta seq, details please look at SimpleFastaDealer.py
    queue: the buffer queue
    lock: this lock is not for buffer mutual exclusion as queue has its own way to do that,
    here it's used to avoid messy print
    ----------
    '''
    @SimpleFastaDealer('TestFasta.fasta')
    def run_p(gener):
        for seq in gener:
            time.sleep(random.random()*2)   #sleep for better impressions
            lock.acquire()
            print('Producing.........')
            lock.release()
            queue.put(seq)
    run_p()

#-------------------------------------------------------------------------------------------------------------------
def Consumer(queue,lock):
    '''
    Introduction
    ------------
    Consumer, multi consumer may run at the same time 
    
    Parameters
    ----------
    see above
    ----------
    '''
    counter = 0 #if counter is more than 10 than we regard the producer has rest
    while True:
        time.sleep(random.random()*10)
        lock.acquire()
        if queue.empty():   #if noe resouce
            counter += 1
        else:
            counter = 0
            seq = queue.get()
            print('PID: ' + str(os.getpid()) + ' get a new sequence:')
            print(seq)
        lock.release()
        if counter == 10:   #producer has rest! so consumer rest too
            print('everyting of PID ' + str(os.getpid()) + ' is done!')
            break
        
if __name__ == '__main__':
    consumer_num=6
    queue_length=6
    record = []
    lock  = multiprocessing.Lock()    # To prevent messy print
    queue = multiprocessing.Queue(queue_length)    #The buffer queue
    process1 = multiprocessing.Process(target=Producer,args=(queue,lock))  #single producer
    process1.start()
    for i in range(consumer_num):  #multi consumer
        process2 = multiprocessing.Process(target=Consumer,args=(queue,lock))
        process2.start()
        record.append(process2)    #record every process for closing them later
    process1.join()
    for i in record:
        i.join()    #close them
