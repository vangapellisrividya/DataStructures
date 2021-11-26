''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: remove in Tuple

    '''

my_tuple = (10, 20, 30, 40, 50)

# converting the tuple to the list
my_list = list(my_tuple)
print(my_list)  # output: [10, 20, 30, 40, 50]

# Here i wanna delete second element "20"
my_list.pop(1) # output: [10, 30, 40, 50]
# As you aware that pop(1) indicates second position

# Here i wanna remove the element "50"
my_list.remove(50) # output: [10, 30, 40]

# again converting the my_list back to my_tuple
my_tuple = tuple(my_list)

print("After removing")
print(my_tuple )# output: (10, 30, 40)