''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Comparing String 
    
    '''

match_words=['abc', 'xyz', 'aba', 'mom','1221']
counter = 0

for word in match_words:
    if len(word) > 1 and word[0] == word[-1]:
      counter += 1
print(counter)