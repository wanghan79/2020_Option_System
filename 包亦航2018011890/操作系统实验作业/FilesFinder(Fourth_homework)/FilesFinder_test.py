# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Test class of fourth OS experiment homework in spring semester, 2020
    
    Introduction:
        Test class
        
    Created: 28/6/2020
    
    Last modified: 28/6/2020
"""

from FilesFinder import FilesFinder

def test():
    kk = FilesFinder(r'/Users/roarboil/desktop/somecodes')
    
    print('################ Test1 ######################')
    dic, fil = kk.find_file() #No parameters means list all 
    print('\n------We find these dictionaries------\n ')
    for i in dic:
        print(i + '   ' + dic[i])
    print('\n------We find these files------\n ')
    for i in fil:
        print(i + '   ' + fil[i])
    print('######################################\n')
    
    
    print('################ Test2 ######################')
    dic, fil = kk.find_file('.*d.*') #Find all files or dictionaries contain d
    print('\n------We find these dictionaries------\n ')
    for i in dic:
        print(i + '   ' + dic[i])
    print('\n------We find these files------\n ')
    for i in fil:
        print(i + '   ' + fil[i])
    print('######################################\n')
    
    print('################ Test3 ######################')
    dic, fil = kk.find_file('(.*protein.*)|(.*drug.*)') #Find all files or dictionaries contain protein or drug
    print('\n------We find these dictionaries------\n ')
    for i in dic:
        print(i + '   ' + dic[i])
    print('\n------We find these files------\n ')
    for i in fil:
        print(i + '   ' + fil[i])
    print('######################################')

test()
