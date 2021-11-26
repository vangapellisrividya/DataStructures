''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Split word based on firstt character
    
    '''

from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)