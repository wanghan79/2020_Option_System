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

######################################################################################################################
class OneProducer_MultiConsumer(object):
    '''
    Attentions:
        using examples has been offered in OneProducer_MultiConsumer_test.py
        
        Please check all the using details below and in OneProducer_MultiConsumer_test.py
    '''
    
    #-------------------------------------------------------------------------------------------------------------------
    def __init__(self,consumer_num=6,queue_length=6):
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
        self.consumer_num = consumer_num
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
        process1 = multiprocessing.Process(target=self.Producer,args=(queue,lock))  #single producer
        process1.start()
        for i in range(self.consumer_num):  #multi consumer
            process2 = multiprocessing.Process(target=self.Consumer,args=(queue,lock))
            process2.start()
            self.record.append(process2)    #record every process for closing them later
        process1.join()
        for i in self.record:
            i.join()    #close them
        
    #-------------------------------------------------------------------------------------------------------------------
    def Producer(self,queue,lock):
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
    def Consumer(self,queue,lock):
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

# test = OneProducer_MultiConsumer()
# test.start()
