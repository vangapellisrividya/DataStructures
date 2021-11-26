
''''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: table of dictionary

    '''
dict ={}
dict1 = {1: ["Samuel", 21, 'Data Structures'],
     2: ["Richie", 20, 'Machine Learning'],
     3: ["Lauren", 21, 'OOPS with java'],
     }
 
# Print the names of the columns.
print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
for key, value in dict1.items():
    name, age, course = value
    print ("{:<10} {:<10} {:\10}".format(name, age, course))