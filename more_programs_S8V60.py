######V60##### Student information
"""student_id = int(input("enter student id"))
name = input("Enter name")
marks = float(input("Enter marks"))

print("ID :", student_id, "Name of student :", name, "Marks :", marks)
"""
#######V61##### Average of three numbers
"""a, b, c = [int(x) for x in input("Please enters 3 numbers to calculate average").split()]

average = float(a+b+c)/3

print("The average of 3 numbers is ", average)
"""
#####V62####### Area of circle
"""
r = float(input("Please enter Radius of \"Circle\" to find out area of Circle"))
pi = 22/7
area_of_circle = pi*r**2

print("The area of circle is : ",area_of_circle)
"""
######V63###### Area of circle using inbuild module "math"
# There are some inbuilt module in python. we can use it in our programs. like,
# we are importing math module and it contains pi value so we need not declare it separately like above program.
import math
r = float(input("Please enter Radius of \"Circle\" to find out area of Circle"))
area_of_cicle = math.pi*r**2                          # we are use math.pi witch is inbuilt in math module
print("The area of circle is : ",area_of_cicle)
