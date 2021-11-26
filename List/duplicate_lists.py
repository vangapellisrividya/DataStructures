''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: duplicate lists in list
    
    '''
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)