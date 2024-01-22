####V45##### None data type
# If we don't have any value to assign any variable so we can assign the 'None' data type in python.
d = None
print(d)

####V46##### Escape characters e.g \"    \" or \\  \\,   \n , \t

# we use the escape character to print some special character as follows
# we wants "good" word is in double quotes then we use \"    \" this escape character.
print(" Chetan is a \"good\" student ")

# we wants \good\ word is in back slash then we use \\   \\ this escape character.
print(" Chetan is a \\good\\ student ")

print(" Chetan is a \ngood student ") # for new line

print(" Chetan is a \tgood student ") # for tab

# there are different types of escape character depending on as per use. please google it.

###V47#### Constants
# In java we define constant like "final pi = 3.14"
# But in python, we use convention. We define constant in a capital letter "PI = 3.14" without any keyword. so other python developer can understand this is a constant.

PI = 3.14
INTEREST_RATE = 7

####V48### del keyword
# In list we use "del function" to delete the perticular list element
# Also there is a "del keyword" in python to delete the objects within our program.
#a = 10
#print(a)

#a = 10
#del a
#print(a) # It will print error NameError: name 'a' is not defined because del keyword is deleted the value of a.
# we can use del keyword in program when our work is done and we want to clean up some variable value.

####V49#### Data type summary
# in this we are practice all the data types
x = 10 # int
y = 10
o = 20
print(id(x),id(y),id(o)) # the value of x and y is saved on same memory location known as immutablity.

f = 20.15 # float
print(type(f))

g = 3+5j # Complex, here 3 is real part and 5j is the imaginary part number
print(type(g))
print(g.imag) # print imaginary part
print(g.real) # print real part

s = 'chetan'
print(type(s))

lst = [1,2,3,4,5,6] # we use lists type to ordered collection of list
print(type(lst))

t = bytes(lst) # bytes
print(t)
print(type(t))

ba = bytearray(lst) # bytearray , the difference between byte and bytearray is, in bytearray we can make changes (mutable) in byte we cant.
print(ba)           # byte array assign new memory location.
print(type(ba))

r1 = range(20)  # range is use to spacify range and it is immutable
r2 = range(1,10) # start and end range
r3 = range(1,20,30) # steps

t = (1,2,3,4,5,6,7,8) # tuple, immutable. (new memory location will allocated)
print(type(t))

set = {1,3,4,5,7,1,5} # set , un-ordered list with unique keys or elements avoid duplicates It is mutable
print(type(set))
print(set)

fs = frozenset(set)  # frozenset, immutable
print(type(fs))
print(fs)

v = {'chetan':100,'vijay': 101,'rajesh':500,'prashant':555} # dictionary type

print(type(v))
print(v)




