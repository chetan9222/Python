#####V82##### Reverse string
"""
# Method : 1 by Slicing
s = input("Please enter string")
print(s[::-1])  # by slicing we can print the string in reverse form
"""
# Method : 2 by
"""
s = input("Please enter string")
i = len(s) - 1              # length index is start with 0 so we decrease with 1
result = ' '
while i >=0:
    result = result + s[i]
    i = i -1
print(result)
"""
######V83###### Reverse string using split and join
"""
s = '-'.join(['a','b','c'])   # join method is joins the elements given in itterable. - is use as delimiter
print(s)
"""
"""
s = input("Please enter String")
#print(reversed(s))   # the reverse function is reverse the object but we need to convert in string
print(''.join(reversed(s)))
"""
######V84###### Reverse the words in the string
# input - All the power is with in you
# output - you in with is power the All
"""
s = "All the power is with in you"
temp = s.split() # split method is use to split the string by default space is the delimiter
print(temp)
result = []    # empty list tom store a result
i = len(temp) - 1    # length index is start with 0 so we decrease with 1
while i >= 0:
    result.append(temp[i])
    i = i-1
print(result)    # it will print reverse but it is list type we need to convert in to string by join
output = ' '.join(result)  # new variable output is stored the string
print(output)
"""
######V85###### Reverse character in the words
# Input : super cool python
# output : repus looc nhtyp
"""
s = 'super cool python'
temp = s.split()  # by default split method is consider space as a delimiter
print(temp)
result = []
i = 0
while i<len(temp):
    result.append(temp[i][::-1]) # this will append the word in result in reverse formate.
    i=i+1
print(result)
output = ' '.join(result)
print(output)
"""
######V86###### Remove duplicate char in list
"""
s = 'aaaabbbbcccXXXXZZZZZZZ'
temp = []

for c in s:
    if c not in temp:
        temp.append(c)
print(temp)
output = ' '.join(temp)
print(output)
"""
#####V87##### count of character in the string
"""
s = 'aaaabbbbcccXXXXZZZZZZZ'
d = {}

for c in s:
    if c in d.keys():
        d[c] = d[c]+1  # if character is already present then add 1
    else:
        d[c] = 1  # If the character is occur first time print 1

for k,v in d.items():
    print('{}={} times'.format(k,v))
"""
######V88#### Print Right angle triangle

# the logic is print right angle triangle
"""
r = int(input("how many rows you want"))

for i in range(1, r+1):
    for j in range(1, i+1):
        print("* ", end="")  # if we not end parameter here then it will print star in new line so we use end parameter here.
    print()  # the outer for loop is finishes we want to print so we use print here
"""
#or

"""
r = int(input("how many rows you want"))

for i in range(1, r+1):
    print("* "*i)     # it will print * a i times for each row
"""
######V89##### Print pyramid pattern
# logic print spaces first and then *
"""
r = int(input("how many rows you want"))

for i in range(1,r+1):
    print(" "*(r-i),end="")
    print("* "*i)
"""
######V90#### Find substring in the given string

s = "take up one idea and make that idea your life." \
    "think and dream that idea. leave every other idea alone."
subs = "idea"
found = False
pos = -1
length = len(s)

while True:
    pos = s.find(subs,pos+1,length) # we use find function we find sub string and if
    if pos == -1:
        break
    print("found substring at position",pos)
    found = True
if found == False:
    print("string is not found")


