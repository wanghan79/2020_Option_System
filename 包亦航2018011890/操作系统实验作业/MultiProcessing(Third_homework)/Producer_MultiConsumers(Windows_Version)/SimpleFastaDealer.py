# -*- coding:utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Third OS experiment homework in spring semester, 2020
    
    Introduction:
        A class for generate single fasta sequence from fasta file
        
    Special Tips:
        It's a decorative class
        
    Created: 27/5/2020
    
    Last modified: 27/5/2020
"""
from functools import wraps

######################################################################################################################
class SimpleFastaDealer(object):
    '''
    Attentions:
    This is a decorated class, you should using it by '@'
    
    Please check all the using details below
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self, filename):
        '''
        Introduction
        ------------
        constructor
        
        
        Parameters
        ----------
        filename: it's the absolute path or relative path of the fasta file
        ----------
        '''
        
        self.filename = filename
        
    #-------------------------------------------------------------------------------------------------------------------  
    def __call__(self, func, *args, **kwargs):
        '''
        Introduction
        ------------
        Rewrite __call__ function in order to make it a decorative class
        
        '''

        @wraps(func)  # To keep its own namespace
        def wrapper(*args, **kwargs):
            gener = self.extract()
            return func(gener, *args, **kwargs)
        return wrapper
    
    #-------------------------------------------------------------------------------------------------------------------  
    def extract(self):
        '''
        Introduction
        ------------
        extract single fasta sequence from the fasta file
        
        '''
        try:
            f = open(self.filename,'r')
            while True:
                name = f.readline()
                if not name:    #if no fasta left then break
                    break
                content = f.readline()
                yield(name + content)   # make it a generator
        except:
            print('Error occured when extracting!!!!')

