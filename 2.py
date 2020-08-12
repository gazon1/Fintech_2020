import re 
# https://www.geeksforgeeks.org/python-program-to-count-words-in-a-sentence/
  
  
doc = input()
res = len(re.findall(r'\w+(?:(-)*\w+)+', doc)) 
  
# printing result 
print(str(res)) 


# ho-ho-ho my merry - merry
