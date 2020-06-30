# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        test function of First OS experiment homework in spring semester, 2020
    
    Introduction:
        test function
        
    Created: 24/6/2020
    
    Last modified: 24/6/2020

"""

from OSInformationGetter import OSInformationGetter

def test():
    '''
    print all information of operating system
    '''
    os_info = OSInformationGetter()
    print('operation system type is : ' + os_info.get_system())
    print('operation system name is : ' + os_info.get_name())
    print('platform type is : ' + os_info.get_type())
    print('computer name in network is : ' + os_info.get_node())
    print('processor name is : ' + os_info.get_processor())
    print('operation system version is : ' + os_info.get_version())
    print('operation system architecture is : ' + os_info.get_arch()[0])
    print("Thanks for using my method!")

test()