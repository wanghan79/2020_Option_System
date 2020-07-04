# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Second OS experiment homework in spring semester, 2020
    
    Introduction:
        a class for automatically ping website
        
    Special Tips:
        Using examples please look at Autoping_test.py
        
    Created: 25/6/2020
    
    Last modified: 25/6/2020

"""

import os


######################################################################################################################
class Autoping(object):
    '''
    Attentions:
        details can be checked below
    '''
    #--------------------------------------------------------------------------
    def __init__(self, filename, send_time):
        """
        Constructor
        
        Parameters
        ----------
        local_path: The name of input file
        send_time: number of ping times
        """
        self.filename = filename 
        self.send_time = send_time
        
    def pin(self):
        """
        ping all websites
        """
        f = open(self.filename,'r')
        for item in f:
            try:
                item = item.strip(' ')
                item = item.strip('\n')
                os.system('ping -n '+self.send_time +' '+ item + ' >>output.txt')
            except:
                print('website name error!')
        