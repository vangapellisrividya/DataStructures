''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: common member in list
    
    '''

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))