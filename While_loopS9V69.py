#####V69##### While loop
# Syntax -
# While (Condition):
#       statements
# we are going to print 1 to 20 numbers using while loop
"""x = 1
while (x <= 20):
    print(x)
    x+=1
"""
#####V71##### odd number from given number
"""
x = int(input("Please enter Min number : "))
y = int(input("Please enter Max number : "))
i = x              #
if x%2 == 0: i=x+1  # if we enter as even number the we need to add 1 to display odd number
while (i <= y):
    print(i)
    i+=2
"""
#####V72##### for loop
# for loop is use to iterate over the element of the sequence. Like String,lists,Tuple,Set,Range etc.
# the for loop is executed until the sequence has values.
# Syntax -
# at the very first time when for loop executes the first value is stored in "Var" here. see in syntax
# and we van use that "Var" in the Statements in a for loop until the last element of sequence execute.
# for Var as sequence :      # there very first for loop is execute
#       Statements :

######V73#### using for loop print numbers from 50 to 70
"""
for i in range(50,71): # range exclude the last number so we define last number as 71
    print(i)
"""
# increment the value of x by 2
"""
for x in range(50,71,2):
    print(x)
"""
########V74#### Product of Nubmers in list
"""
lst=[1,2,3,4,5]
prod=1    # we are define variable to stire product

for i in lst:
    prod*=i
    #print("product is ", prod)           # this is execute with in the for loop so it will print every time
print("product is ",prod)                 # this is out side the foe loop so it will execute one time.
"""
########75##### Multiplication Table of given number
"""
num=int(input("enter a number for create table"))

for i in range(1,11):    # we are given range 1 to 11 because last num in range is exclude always. 
    print(num,'X',i,'=',i*num)
"""
#########V76#### break
"""
# we use break statement to exit from loop
lst=[3,2,9,4,5,3,7]

for i in lst:
    if (i==5): # == means value of i in list
        break
    print(i)
"""
####V77#### Continue
# we use continue statement to skip the specific condition.
# print 1 to 20 skip multiple of 3
"""
for i in range(1,20):
    if (i%3==0):
        continue
    print(i)
"""
######V78##### assert
# we use assert statement to validate the input
# ask the end user to enter number which is grater than 10
"""
x=int(input("Please enter number Greater than 10"))
assert x>10, "You Entered wrong number"
print("You are entered",x)
"""
######V79##### Remove Duplicate numbers in list by eval function
# eval function is use to remove duplicate function from lst
# method 1 :
"""
l1=eval(input("Enter list numbers"))
print(l1)                     # in terminal elements type in a [] bracket
l2 = []                       # new empty list for add non-duplicate element.

for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)
"""
#Method 2 : by using set function because set is avoids duplicates.
"""
l1=eval(input("Enter list numbers"))
print(l1)
s1 = set(l1)
print(s1)
"""
########V80###### more programs : Count Vowels in a word
"""
word = input("enter word")
vowels = {'a', 'e', 'i', 'o', 'u'}  # set of vowels
result = {}                         # to store result in empty dictionary type

for c in word:
    if c in vowels:
        result[c] = result.get(c, 0)+1   # here result[c] is key and result.get(c, 0) is initial value of result dictionary.
                                         # if any vowel found first time in word it will counted as 1
for k , v in result.items():             # we consider k as key and v as value of dictionary and to invoke the k and v we use item() func.
    print(k, "is present", v, "times")
"""

#######V81######### more programs : handle employee details

n = int(input("Please Enter Number of employees in your company"))
employee = {}                                   # employee empty dictionary to store key and value
for i in range(n):
    name = input("please enter name of Employee : ")
    salary = int(input("Please enter Salary of Employee :"))
    employee[name] = salary             # stored employee[name] as key and salary as value in employee dictionary.
while True:
    name = input(" Please enter name of employee to check salary : ")
    salary = employee.get(name, -1)     # to invoke the employee name and salary from employee dictionary . we use get func.
                                        # if the employee name is match then get salary if not match then retun -1
    if salary == -1:
        print("you enter wrong employee name or Employee does not exist")
    else:
        print("the salary details of employee is :", salary)

    choice = input(" You want to continue to check another employee salary details please [Y|N]")
    if choice == 'N':         # if user type N then break the if loop
        break

