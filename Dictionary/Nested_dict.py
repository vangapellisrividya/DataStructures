'''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: nested dictionary of keys
'''

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)