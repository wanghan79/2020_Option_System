# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Fourth OS experiment homework in spring semester, 2020
    
    Introduction:
        a class for listing files or finding the specific file
        
    Special Tips:
        Using examples please look at FilesFinder_test.py
        
    Created: 28/6/2020
    
    Last modified: 28/6/2020

"""

import os
import re

######################################################################################################################
class FilesFinder(object):
    '''
    Attentions:
        details can be checked below
    '''
    #--------------------------------------------------------------------------
    def __init__(self,base_path):
        """
        Introduction
        ----------
        Constructor
        
        Parameters
        ----------
        base_path: The basic path
        """
        self.base_path = base_path
        self.dic_list = dict() #store all dictionaies
        self.file_list = dict() #store all files
        self.get_list() #get all files after construction
        
    def get_list(self):
        """
        Introduction
        ----------
        get all files, dictionaries and store them into the dict
        """
        for base, dirs, files in os.walk(self.base_path):
            for d in dirs:
                fullname = os.path.join(base, d) #The whole path
                self.dic_list.update({d:fullname})
            for f in files:
                fullname = os.path.join(base, f) #The whole path
                self.file_list.update({f:fullname})
    
    def find_file(self,file_name = '.*'):
        """
        Introduction
        ----------
        find the files and dictionaries meet the requirement
        
        Parameters
        ----------
        file_name: it should be regular expression, default we matches all
        """
        d_result = dict() #dictionaries meet your need
        f_result = dict() #files meet your need
        for d in self.dic_list:
            if re.search(file_name,d): #if successfully match then put it in
                d_result.update({d:self.dic_list[d]})
        for f in self.file_list:
            if re.search(file_name,f):
                f_result.update({f:self.file_list[f]})
        return d_result, f_result  
        