''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Characers count
    
    '''

test_str = "GeeksforGeeks"
  
# using naive method to get count 
# of each element in string 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print ("Count of all characters in GeeksforGeeks is :\n "+  str(all_freq)) 