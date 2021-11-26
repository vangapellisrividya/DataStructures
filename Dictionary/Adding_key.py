'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: sort dictionary in ascending and descending order by value

    '''
class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
        print([key,value])
  
if __name__=='__main__':
    dict_obj = my_dictionary()
    
    dict_obj.add(1, 'Geeks')
    dict_obj.add(2, 'forGeeks')
    