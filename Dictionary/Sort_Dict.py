'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: sort dictionary in ascending and descending order by value

    '''

my_dict = {'red': '# FF0000', 'green': '# 008000',
            'black': '# 000000', 'white': '# FFFFFF'}
def ascend():
    print("\nSort (ascending) the dictionary elements by value:")
    print("Sorted dictionary is :")
    for w in sorted((my_dict), key = my_dict.get,reverse = False):
        print(w, my_dict[w])
def descend():
    print("\nSort (descending) dictionary elements by value:")
    print("Sorted dictionary is :")
    for w in sorted(my_dict, key = my_dict.get, reverse = True):
        print(w, my_dict[w])

if __name__=='__main__':
    ascend()
    descend()