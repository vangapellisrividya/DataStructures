''''
    Created on Nov 26, 2021

    @author:srividya
    @Date:  26/11/2021
    @Title: Substrings in string    
    '''

def count(sub, s): 
    M = len(sub) 
    N = len(s) 
    res = 0

    # A loop to slide sub[] one by one
    for i in range(N - M + 1): 

        # For current index i, check for the match
        j = 0
        while(j < M): 
            if (s[i + j] != sub[j]): 
                break
            j += 1

        if (j == M): 
            res += 1
            j = 0
    return res 

# Driver Code 
string = "abracadabra"
substring = "abr"
print("Count:", count(substring, string))