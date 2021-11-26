'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: input in given range of dictionary
'''
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)