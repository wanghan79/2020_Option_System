# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        First OS experiment homework in spring semester, 2020
    
    Introduction:
        A class to get basic information of operating system
        
    Special Tips:
        Using examples please look at OSInformationGetter_test.py
        
    Created: 24/6/2020
    
    Last modified: 24/6/2020

"""
import platform


######################################################################################################################
class OSInformationGetter(object):
    '''
    Attentions:
        details can be checked below
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self):
        pass
    
    def get_type(self):
        '''
        Returns
        -------
        platform type
        
        Example output on my computer
        -------
        x86_64
        '''
        return platform.machine()
    
    def get_node(self):
        '''
        Returns
        -------
        computer name in network
        
        Example output on my computer
        -------
        boildeAir.lan
        '''
        return platform.node()
        
    def get_name(self):
        '''
        Returns
        -------
        operation system name
        
        Example output on my computer
        -------
        Darwin-18.7.0-x86_64-i386-64bit
        '''
        return platform.platform()
    
    def get_processor(self):
        '''
        Returns
        -------
        processor name
        
        Example output on my computer
        -------
        i386
        '''
        return platform.processor()
    
    def get_version(self):
        '''
        Returns
        -------
        operation system version
        
        Example output on my computer
        -------
        Darwin Kernel Version 18.7.0: Thu Jan 23 06:52:12 PST 2020; root:xnu-4903.278.25~1/RELEASE_X86_64
        '''
        return platform.version()
        
    def get_system(self):
        '''
        Returns
        -------
        operation system type
        
        Example output on my computer
        -------
        Darwin
        '''
        return platform.system()
    
    def get_arch(self):
        '''
        Returns
        -------
        operation system architecture
        
        Example output on my computer
        -------
        ('64bit', '')
        '''
        return platform.architecture()
    def get_combine_tuple(self):
        '''
        Returns
        -------
        a tuple with combined imformation
        
        Example output on my computer
        -------
        uname_result(system='Darwin', node='boildeAir.lan', release='18.7.0', version='Darwin Kernel Version 18.7.0: Thu Jan 23 06:52:12 PST 2020; root:xnu-4903.278.25~1/RELEASE_X86_64', machine='x86_64', processor='i386')
        '''
        return platform.uname()
    
