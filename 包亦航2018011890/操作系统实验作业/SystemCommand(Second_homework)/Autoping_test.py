# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Test class of second OS experiment homework in spring semester, 2020
    
    Introduction:
        Test class
        
    Created: 25/6/2020
    
    Last modified: 25/6/2020
"""

from Autoping import Autoping

def test():
    test1 = Autoping('sample_input.txt','4')
    print('Processing')
    test1.pin()
    print('Done!')
    print('datas have been written into output.txt')
test()
