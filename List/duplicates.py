''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Remove duplicates
    
    '''

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using naive method
# to remove duplicated 
# from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))
