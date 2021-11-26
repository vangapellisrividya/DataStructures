''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: existed element in Tuple

    '''
tup=(1,3,4,32,1,1,1) 
for i in tup:
    if tup.count(i) > 1:
        print(i)

tup1=(1,2,3,4)
f=0
k=int(input("enter the value"))
for value in tup1:
    if value==k:
        print("existed")
        break
    else:
        print("not existed")
        
    