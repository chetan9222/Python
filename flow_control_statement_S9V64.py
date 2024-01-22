######V64#### Flow control statements
# Flow control determine the order in which the statements are executed in run time.
# There are 3 types of flow control statements

# 1. Conditional Statements : It allows execute our code conditionally.
# E.g if, if....else, if...elif...else(ladder)

# 2. Looping Statements (Iterative Statements ) : It allows us to execute same set of statement or logic multiple time
# E.g while, for

# 3. Transfer Statements : It allows us to transfer control from one place to another place.
# E.g break, continue, pass, return

######V64#### if else syntax
"""
if syntax -
if condition :            # if condition is "true" then and then only statements are execute
    statements
___________________________________________________________________________
if....else syntax -
if condition :            # if condition is "true" then and then only statements are execute
    statements
else :                    # if condition is "false" then control comes at else part and execute else statements.
    statements
---------------------------------------------------------------------------
if..elif..else syntax -  # here note that only one condition is executed only. if first condition is gets TRUE the remaining elif are not executed
if condition1:            # if condition is "true" then and then only statements are execute and exit
    statements

elif condition2:         # we can use multiple elif for multiple conditions.
    statements           # If statement is false then only elif conditions sre execute until TRUE. and exit
elif condition3:
    statements

else :                    # if condition is "false" then control comes at else part and execute else statements.
    statements
"""

######V65#### find even and odd number by if else
"""
x = int(input("Enter the Number to test the number is Even or Odd"))

if x%2 == 0:
    print(x,"is Even number")
else:
    print(x,"is Odd number")
"""
######V65#### Handle zero by using if... elif...else ladder
# in above example if we type 0 it will show us 0 is even number to handle this we use if....elif...else (ladder)
# if we have multiple conditions then we use if else ladder
# In which we use multiple elif blocks statements for multiple conditions. 

x = int(input("Enter the Number to test the number is Even or Odd"))
if x==0:
    print(x,"is not Even nor Odd")
elif x%2 == 0:
    print(x,"is Even number")
else:
    print(x,"is Odd number")