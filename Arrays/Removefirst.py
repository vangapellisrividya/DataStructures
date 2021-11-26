'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: Removing first ocuurrence of selected element

    '''

import numpy as np

from array import *
class Array:
    integer = array('i',[])
    n = int(input("enter the length: "))
    for i in range(n):
        x = int(input("enter the element: "))
        integer.append(x)
    f=0
    ele=int(input("enter the element"))
    for e in integer:
        if ele==integer[i]:
            integer.remove(ele)
            f=1
            break
    if f==0:
        print("not found")
    else:
        print("element removed")
        print(integer)     