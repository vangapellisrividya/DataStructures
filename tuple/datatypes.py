''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Tuple in datatypes and unpacking variables

    '''
#create tuple
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#unpack variables:-
tuplex = 4, 8, 3 
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1 + n2 + n3) 
#the number of variables must be equal to the number of items of the tuple
#n1, n2, n3, n4= tuplex 