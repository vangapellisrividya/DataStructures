'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: Count of elements occurrence

    '''

import numpy as np

from array import *
class Array:
    integer = array('i',[])
    n = int(input("enter the length: "))
    for i in range(n):
        x = int(input("enter the element: "))
        integer.append(x)
    k=0
    for e in integer:
        if integer.index(e)==k :
            print(e," comes ",integer.count(e),"times")
        k+=1
        

