''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: List of words longer than n
    
    '''

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))