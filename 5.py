
# Python program 
# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/  
import sys 
  
# A utility function to print a 
# substring str[low..high] 
def getStr(st,low,high) : 
    return st[low : high + 1] 
  
# This function prints the longest palindrome 
# substring of st[]. It also returns the length 
# of the longest palindrome 
def longestPalSubstr(st) : 
    n = len(st) # get length of input string 
  
    # table[i][j] will be false if substring  
    # str[i..j] is not palindrome. Else  
    # table[i][j] will be true 
    table = [[0 for x in range(n)] for y 
                          in range(n)]  
      
    # All substrings of length 1 are 
    # palindromes 
    maxLength = 1
    i = 0
    while (i < n) : 
        table[i][i] = True
        i = i + 1
      
    # check for sub-string of length 2. 
    start = 0
    i = 0
    while i < n - 1 : 
        if (st[i] == st[i + 1]) : 
            table[i][i + 1] = True
            start = i 
            maxLength = 2
        i = i + 1
      
    # Check for lengths greater than 2.  
    # k is length of substring 
    k = 3
    while k <= n : 
        # Fix the starting index 
        i = 0
        while i < (n - k + 1) : 
              
            # Get the ending index of  
            # substring from starting  
            # index i and length k 
            j = i + k - 1
      
            # checking for sub-string from 
            # ith index to jth index iff  
            # st[i+1] to st[(j-1)] is a  
            # palindrome 
            if (table[i + 1][j - 1] and 
                      st[i] == st[j]) : 
                table[i][j] = True
      
                if (k > maxLength) : 
                    start = i 
                    maxLength = k 
            i = i + 1
        k = k + 1
    return maxLength, getStr(st, start,  start + maxLength - 1)
  
    # return length of LPS 
  
  
# Driver program to test above functions 
#st = "forgeeksskeegfor"
# st = 'QWERTY'
st = input()
l, st = longestPalSubstr(st) 
print(l)
print(st)
# This code is contributed by Nikita Tiwari. 
