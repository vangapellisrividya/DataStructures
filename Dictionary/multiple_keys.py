'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: multiple keys in dictionary
'''

sports = {"games" : 1, "practice" : 2, "contribute" :3}
  
# using if, all statement 
if all(key in sports for key in ('games', 'practice')):
    print("keys are present")
else:
    print("keys are not present")
  
# using if, all statement 
if all(key in sports for key in ('games', 'ide')):
    print("keys are present")
else:
    print("keys are not present")