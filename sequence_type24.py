#Simple data type holds a single value. But in real time project we needs hold on mutiple value or sequence off values at a time.
#Mutiple values comming from data base table and so on
# So we are use inbuilt collections or data structures in python. e.g List, Sets and Dictionary
# 1. List can store any number values or objects dynamically. IT maintains order of them.
# 2. Set is does not allows duplicates. we can use set to store any number of values dynamically.
# 3. Dictionary is map. It is stores key and value pair. It have diffrent methods than list and sets to deal with ky and values.

######v25####### Strings

s="python is awesome "
print(s)

# multiline string just like comment. we can use three single quotes also instead of the double quotes.
s1=""" phythoh is 
awesome"""
print(s1)

# to reach out first character of above s string and print it.
print(s[0])
print(s[2])

# to print string several times
print(s*2)

#to print length of string we use len function
print(len(s1))
print(len(s))

#to slicing string
print(s[0:5])
print(s[:8])
print(s[0:])

#we use negative number. -1 index is the last character of string then -2 index is second last and so on
print(s[-5:-1])

######v27##### steps in slicing
print(s[0:9:2])    # here the string getting print alternate character
print(s[15::-1])   # reverse string upto 15 index
print(s[::-1])     # reverse string

#######v28####### strip the spaces from string using strip function

r= "  this is  the  string   with extra   white spaces to  test  strip  function       "
print(r.strip())
print(r.lstrip()) # remove left hand side white spaces
print(r.rstrip()) # remove right hand side white spaces

#######v29####### few more string methods

# find function to find location of sub string

print(s.find("awe"))
print(s.find("some",0,8)) # we are giving index number 0 to 8 to find "some" sub string. o/p is -1 because no match found in 0 to 8
print(s.count("a")) # to print occrances of perticular sub string.
print(s.replace("python","bash script"))

print(s.upper())
print(s.lower())
print(s.title())