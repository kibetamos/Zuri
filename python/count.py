# Python3 code to demonstrate 
# to count words in string 
# using sum() + strip() + split()
import string

word= input("Type y0ur text here:")
# initializing string  
  
# printing original string
print ("The original string is : " +  word)
  
# using sum() + strip() + split()
# to count words in string
res = sum([i.strip(string.punctuation).isalpha() for i in word.split()])
  
# printing result
print ("The number of words in string are : " +  str(res))