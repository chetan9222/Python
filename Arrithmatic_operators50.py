####V50##### Arrithmatic operators
# There are some additional operators in python.
# Power of operator **  - ex a**b means a to the power of b
# Interger division operator or Floor division operator // - It perform the division and it will gives us integer quotiont from decimal number.

a,b=10,5     # this is the power of python we can also define variable like this, here a=10 and b=5 respectively.

print('addition : ', a+b)
print('Subtraction : ', a-b)
print('Multiplication : ', a*b)
print('Division : ', a/b)
print('Modulus : ', a%b)
print('Power of : ', a**b)
print('Floor Division : ', a//b)

#####V51########### Assignment operators
# a=10 means the 10 value assingn to a.
# Similarly a=x+y means x is added in y and resulting value is assign to a.
# compound assignment operator :
# 1. +=  :  a+=b means a=a+b
# 2. -=  :  a-=b means a=a-b
# 3. *=  :  a*=b means a=a*b
# 4. /=  :  a/=b means a=a/b
# 5. %=  :  a%=b means a=a%b
# 6. **= :  a**=b means a=a**b
# 7. //= :  a//=b means a=a//b

x=y=z=10
print(x,y,z)

p,q=10,5

p+=q
print(p) # here p=p+q p=10+5 so p=15

p*=q
print(p) # now p is holding value 15 so p=15*5 ,p=75

#####V52############## Comparison operators ex.  ==, !=, <, >,  <=, >=
# in this the final output is True or False.

d,e=77,88
print(d==e) # o/p is false
print(d!=e)
print(d>e)
print(d<e)
print(d>=e)
print(d<=e)

#####V53############## Logical Operators ex. and, or, not

f,g=10,12

print((f==g and f!=g)) # In "and" logical operator if both statements are true then o/p is true otherwise false.

print((f!=g and f<g)) # here both statements are true.

print((f==g or f!=g)) # In "or" logical operator if both statements are false then o/p is false otherwise true.

print((not f!=g)) # not statement is use to convert true statement to false vise versa

print(not(f==g or f!=g)) # we convert above true statement into false by not logical operator

#####V54############## Operator BMI(body mass index) usecase

weight = 72
height = 6.2

# BMI = Waight in kg /(height*height in meter)

heightInMeter = height*0.304800 # convert height into meter

bmi = weight/(heightInMeter**2)

print('your BMI is ',bmi)










