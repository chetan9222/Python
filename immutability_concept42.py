######V42##### Imutable
# immutability term is applicable for all data types in python.
# immutability :- if we define a=10 and b=10 then python assign same memory location to store the value of a and b.
# i.e python not assign different memory location to store same value of variables.
# python PVM(python Virtual Machine) not waste the memory location for same value in a program.
# e.g

a=10
b=10
print(a is b) # It will print "True" because we check memory location here.
# To further memory location detail we can use "id" function
print(id(a))
print(id(b)) # the output will show same memory loacation for value of a and b this is the immutability concept of python.

c=True
d=True
print(id(c))
print(id(d)) # the output will show same memory loacation for value of c and d this is the immutability concept of python.

# if some how we change the value of d=False then it will allocate different memory location.
# d=False
# print(id(d)) # the output will show different memory loacation for value of d

e='chetan'
f='chetan'
print(e is f) # It will print "True" because we check memory location here.
# To find out further memory location details, we can use "id" function.
print(id(e))
print(id(f))