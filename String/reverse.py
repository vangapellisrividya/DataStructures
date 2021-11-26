''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Reverse of string
    
    '''

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))