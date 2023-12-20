#In python we convert the value from float to int
a=30.33
print(a)

h=int(a) # this will convert a floating variable to integer
print(h)

#instead of passing number we are passing a string and print floating point

i=float("22.55")
print(i)
print(type(i))

#the bin function will give us binary conversion of any numeric value.
#similar for hex function
#Similar for oct
print(bin(15))
print(hex(255))
print(oct(12))

#integer to hexadecimal conversion function
b=255
print(hex(b))

#integer to binary conversion function
c=10
print(bin(c))

#integer to octal conversion function
d=15
print(oct(d))

#hexadecimal to int
e=0xfa
print(int(e))

#binary to int
f=0b1011
print(int(f))

#Octal to int
g=0o101
print(int(g))
