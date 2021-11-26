'''
    Created on Nov 25, 2021

    @author:srividya
    @Date:  25/11/2021
    @Title: Unique values in dictionary
    
    '''
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))