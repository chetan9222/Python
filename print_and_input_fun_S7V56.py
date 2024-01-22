"""#####V56###### print and input function
# we use input function to take input from user
# we use print function to display output.
a = 1
b = 2
print(a,b)
print("The value of a and b is : ", a,b)
print('this is the \n print function test')

print('hello'*3)

print(a,b,sep=',') # Separator between two printing value
print(a,b,sep='&') # Separator
print(a,b,end='.') # end

#####V56###### print and string formating

name = 'chetan'
marks = 97.5612
# There are different methods to print the string and value togather.

# 1st method (simple)
print("The Marks of",name,"is",marks)

# 2nd method ( by using % place holder ex. %s - string, %i - Integer, %f - float )
print("The marks of %s is %f" %(name,marks))
print("The marks of %s is %.2f" %(name,marks)) # to restrict the floating number after decimal point we use %.2f

#3rd method (by using format method ) we cant restrict decimal point in this method
print("The marks of {} is {}".format(name,marks))

print("The marks of {1} is {0}".format(marks,name)) # we use index in braces accordingly it will prints the value

#####V57###### Input (we gather the input from console or keyboard or user)

s = input() # If you enter any num or string on console. it will sore it in variable s and prints it.
print(s)
print(type(s)) # by default the input type is str

p = int(input("enter your name")) # we can convert the type of variable by type casting
print(p)
print(type(p))

#####V58###### Reading multiple inputs from user by split() function

u=input("enter 3 numbers separated by space").split()# split fun by default understand space between two numbers
print(u)
print(type(u))  # by default input is consider as string. see in output the elements are in ''
"""
# we use , (comma) as number separator in split function
lst = [int(x) for x in input("enter two numbers separated by comma").split(",")]
# we store input in x and pass it in lst using for loop
# we use int(x) for type casting here because by default python consider input as a string
print(lst)

