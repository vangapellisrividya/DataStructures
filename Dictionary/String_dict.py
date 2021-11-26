'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: Unique values in dictionary
'''

string = input( "Enter a String :-" )
dic = {}

for i in string :
    dic [i] = string.count(i)
print("Dictionary :-",dic)