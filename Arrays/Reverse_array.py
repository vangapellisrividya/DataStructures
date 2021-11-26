
'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: Reverse of array

    '''
from array import *

class Array:
    integer = array('i',[])
    n = int(input("enter the length: "))
    for i in range(n):
        x = int(input("enter the element: "))
        integer.append(x)
    integer.reverse()
    print(integer)