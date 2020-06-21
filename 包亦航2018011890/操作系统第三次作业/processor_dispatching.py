# -*- coding:utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        processor dispatching algorithm compare
             
    Created: 20/6/2020
    
    Last modified: 20/6/2020
"""

import random
import queue

######################################################################################################################
class processor_dispatching(object):
    '''
    Attentions:
    
    Please check all the using details below
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self,num,bline,tline,last_time):
        '''
        Introduction
        ------------
        constructor
        
        Parameters
        ----------
        num: number of random tasks
        bline: min arriving time
        tline: max arriving time
        last_time: max process time of single task
        ----------

        '''
        
        self.num = num
        self.bline = bline
        self.tline = tline
        self.last_time = last_time
        task_list = []
        for i in range(self.num): #generate taskes
            a = random.randint(self.bline, self.tline)
            b = random.randint(1, self.last_time)
            task_list.append((a,b))
        self.task_list = task_list
        
        
    #------------------------------------------------------------------------------------------------------------------- 
    def FCFS(self):
        '''
        Introduction
        ------------
        First Come First Serve algorithm

        '''
        finish_time = []
        turnaround_time = []
        righted_turnaround_time = []
        wait_time = []
        f_list = sorted(self.task_list,key= lambda x:x[0])
        f_q = queue.PriorityQueue()
        co = 0
        t = 0
        while True:
            if f_q.empty() and f_list[co][0] > t:
                t = f_list[co][0]
            while co < self.num:
                if f_list[co][0]<=t:
                    f_q.put(f_list[co])
                    co += 1
                else:
                    break
            if f_q.empty() and co >= self.num:
                break
            kk = f_q.get()
            t += kk[1]
            finish_time.append(t)
            wait_time.append(t-kk[0]-kk[1])
            turnaround_time.append(t-kk[0])
            righted_turnaround_time.append((t-kk[0])/kk[1])
            if f_q.empty() and co >= self.num:
                break
            
        ave_finish_time =0 
        ave_turnaround_time = 0
        ave_righted_turnaround_time = 0
        for i in finish_time:
            ave_finish_time += i
        ave_finish_time /= self.num
        for i in turnaround_time:
            ave_turnaround_time += i
        ave_turnaround_time /= self.num
        for i in righted_turnaround_time:
            ave_righted_turnaround_time += i
        ave_righted_turnaround_time /= self.num
        wait_time = sorted(wait_time)
        print("top 3 wait time: ")
        for i in range(self.num-3,self.num):
            print(wait_time[i],end=' ')
        print(' ')
        print("average finish time is: ",end='')
        print(ave_finish_time)
        print("average turnaround time is: ",end='')
        print(ave_turnaround_time)
        print("average righted_turnaround_time time is: ",end='')
        print(ave_righted_turnaround_time)
    
    #-------------------------------------------------------------------------------------------------------------------  
    def SJF(self):
        '''
        Introduction
        ------------
        Shortest Job First algorithm

        '''
        finish_time = []
        turnaround_time = []
        wait_time = []
        righted_turnaround_time = []
        f_list = sorted(self.task_list,key= lambda x:x[0])
        f_q = queue.PriorityQueue()
        co = 0
        t = 0
        while True:
            if f_q.empty() and f_list[co][0] > t:
                t = f_list[co][0]
            while co < self.num:
                if f_list[co][0]<=t:
                    f_q.put((f_list[co][1],f_list[co][0]))
                    co += 1
                else:
                    break
            if f_q.empty() and co >= self.num:
                break
            kk = f_q.get()
            t += kk[0]
            finish_time.append(t)
            wait_time.append(t-kk[0]-kk[1])
            turnaround_time.append(t-kk[1])
            righted_turnaround_time.append((t-kk[1])/kk[0])
            if f_q.empty() and co >= self.num:
                break
            
        ave_finish_time =0 
        ave_turnaround_time = 0
        ave_righted_turnaround_time = 0
        for i in finish_time:
            ave_finish_time += i
        ave_finish_time /= self.num
        for i in turnaround_time:
            ave_turnaround_time += i
        ave_turnaround_time /= self.num
        for i in righted_turnaround_time:
            ave_righted_turnaround_time += i
        ave_righted_turnaround_time /= self.num
        wait_time = sorted(wait_time)
        print("top 3 wait time: ")
        for i in range(self.num-3,self.num):
            print(wait_time[i],end=' ')
        print(' ')
        print("average finish time is: ",end='')
        print(ave_finish_time)
        print("average turnaround time is: ",end='')
        print(ave_turnaround_time)
        print("average righted_turnaround_time time is: ",end='')
        print(ave_righted_turnaround_time)

    #-------------------------------------------------------------------------------------------------------------------  
    def HRRN(self):
        '''
        Introduction
        ------------
        Highest Response Ratio Next algorithm

        '''
        finish_time = []
        turnaround_time = []
        wait_time = []
        righted_turnaround_time = []
        f_list = sorted(self.task_list,key= lambda x:x[0])
        f_q = queue.PriorityQueue()
        co = 0
        t = 0
        while True:
            if f_q.empty() and f_list[co][0] > t:
                t = f_list[co][0]
                tmp_rev = []
                while(not f_q.empty()):
                    tmp = f_q.get()
                    resp = (t - tmp[1] + tmp[2])/ tmp[2]
                    tmp_rev.append((-resp,tmp[1],tmp[2])) #negative makes high response first
                for item in tmp_rev:
                    f_q.put((item[0],item[1],item[2]))
            while co < self.num:
                if f_list[co][0]<=t:
                    resp = (t - f_list[co][0] + f_list[co][1])/ f_list[co][1]
                    f_q.put((-resp,f_list[co][0],f_list[co][1]))
                    co += 1
                else:
                    break
            if f_q.empty() and co >= self.num:
                break
            kk = f_q.get()
            t += kk[2]
            tmp_rev = []
            while(not f_q.empty()):
                tmp = f_q.get()
                resp = (t - tmp[1] + tmp[2])/ tmp[2]
                tmp_rev.append((-resp,tmp[1],tmp[2]))
            for item in tmp_rev:
                f_q.put((item[0],item[1],item[2]))
            finish_time.append(t)
            wait_time.append(t-kk[2]-kk[1])
            turnaround_time.append(t-kk[1])
            righted_turnaround_time.append((t-kk[1])/kk[2])
            if f_q.empty() and co >= self.num:
                break
            
        ave_finish_time =0 
        ave_turnaround_time = 0
        ave_righted_turnaround_time = 0
        for i in finish_time:
            ave_finish_time += i
        ave_finish_time /= self.num
        for i in turnaround_time:
            ave_turnaround_time += i
        ave_turnaround_time /= self.num
        for i in righted_turnaround_time:
            ave_righted_turnaround_time += i
        ave_righted_turnaround_time /= self.num
        wait_time = sorted(wait_time)
        print("top 3 wait time: ")
        for i in range(self.num-3,self.num):
            print(wait_time[i],end=' ')
        print(' ')
        print("average finish time is: ",end='')
        print(ave_finish_time)
        print("average turnaround time is: ",end='')
        print(ave_turnaround_time)
        print("average righted_turnaround_time time is: ",end='')
        print(ave_righted_turnaround_time)


if __name__  == '__main__':
    
    print("==================exp1==================\n")
    kk = processor_dispatching(1000,100,100,100)
    kk.FCFS()
    print("<--------------------------------->")
    kk.SJF()
    print("<--------------------------------->")
    kk.HRRN()
    print("\n")
    
    print("==================exp2==================\n")
    kk = processor_dispatching(10,0,10,5)
    kk.FCFS()
    print("<--------------------------------->")
    kk.SJF()
    print("<--------------------------------->")
    kk.HRRN()
    print("\n")
    
    print("==================exp3==================\n")
    kk = processor_dispatching(1000,0,1000,5)
    kk.FCFS()
    print("<--------------------------------->")
    kk.SJF()
    print("<--------------------------------->")
    kk.HRRN()
    print("\n")
    
    print("==================exp4==================\n")
    kk = processor_dispatching(1000,0,1000,500)
    kk.FCFS()
    print("<--------------------------------->")
    kk.SJF()
    print("<--------------------------------->")
    kk.HRRN()
    print("\n")
    
    print("==================exp5==================\n")
    kk = processor_dispatching(1000,0,10000,5)
    kk.FCFS()
    print("<--------------------------------->")
    kk.SJF()
    print("<--------------------------------->")
    kk.HRRN()
    print("\n")
    
    print("==================exp6==================\n")
    kk = processor_dispatching(1000,0,50000,1000)
    kk.FCFS()
    print("<--------------------------------->")
    kk.SJF()
    print("<--------------------------------->")
    kk.HRRN()
    print("\n")