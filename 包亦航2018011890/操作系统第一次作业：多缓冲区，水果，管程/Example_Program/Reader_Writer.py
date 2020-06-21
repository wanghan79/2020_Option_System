# -*- coding:utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Example of 
    
    Introduction:
        A class for simulating Reader_Writer problem
        
    Special Tips:
        a fasta file is needed for using this(an example fasta file has been offered in the datas dic)
        
    Created: 27/5/2020
    
    Last modified: 27/5/2020
"""
from datas.SimpleFastaDealer import SimpleFastaDealer
import multiprocessing
import random
import time
import os

######################################################################################################################
class Reader_Writer(object):
    '''
    Attentions:
        using examples has been offered in OneProducer_MultiConsumer_test.py
        
        Please check all the using details below and in OneProducer_MultiConsumer_test.py
    '''
    
    #-------------------------------------------------------------------------------------------------------------------
    def __init__(self,reader_num=5,queue_length=6):
        '''
        Introduction
        ------------
        constructor
        
        
        Parameters
        ----------
        consumer_num: the number of consumers, if it's 6 if not offered
        queue_length: the capacity of the buffer queue
        ----------
        '''
        self.reader_num = reader_num
        self.queue_length = queue_length
        self.record = []
    
    #-------------------------------------------------------------------------------------------------------------------
    def start(self):
        '''
        Introduction
        ------------
        the control function or the entrance function
        
        '''
        
        lock  = multiprocessing.Lock()    # To prevent messy print
        queue = multiprocessing.Queue(self.queue_length)    #The buffer queue
        process1 = multiprocessing.Process(target=self.writer,args=(queue,lock))  #single producer
        process1.start()
        for i in range(self.reader_num):  #multi consumer
            process2 = multiprocessing.Process(target=self.read_and_print,args=(queue,lock))
            process2.start()
            self.record.append(process2)    #record every process for closing them later
        process1.join()
        for i in self.record:
            i.join()    #close them
        
    #-------------------------------------------------------------------------------------------------------------------
    def writer(self,queue,lock):
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
        @SimpleFastaDealer('datas/TestFasta.fasta')
        def run_p(gener):
            for seq in gener:
                time.sleep(random.random()*2)   #sleep for better impressions
                lock.acquire()
                print('Producing.........')
                lock.release()
                queue.put(seq)
        run_p()
    
    #-------------------------------------------------------------------------------------------------------------------
    def read_and_print(self,queue,lock):
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
            time.sleep(random.random()*11)
            lock.acquire()
            if queue.empty():   #if no resouce
                counter += 1
            else:
                counter = 0
                seq = queue.get()
                print('PID: ' + str(os.getpid()) + ' read a new sequence:')
                print(seq)
            lock.release()
            if counter == 10:   #producer has rest! so consumer rest too
                print('everyting of PID ' + str(os.getpid()) + ' is done!')
                break

if __name__ == '__main__':
    test = Reader_Writer()
    test.start()
