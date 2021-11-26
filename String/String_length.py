''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: String length
    
    '''

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))