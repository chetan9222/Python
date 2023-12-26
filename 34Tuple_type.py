########V33######## Tuple Type

# It is just like List data Structure. But once we create tuple element, we cannot modify it (Immutable).
# we can not insert any element in the tuple once it create.
# we use it, if we want read only list.
# we can add duplicates elements in tuple.
# Tuple can supports different types of elements e.g string, float,string so on
# Syntax :  t1 = (1,2,3) If we have single element in tuple then it should be and with comma e.g. t1 = (1,)
# Because if we not give comma there then python treated as single element variable.

tpl=(100,) # Single element tuple ended with comma
print(tpl)
print(type(tpl))  # this is check for type. tpl=(100) this will consider as single value variable (int type).

tpl1=(20,30,40,20,50,'xyz')
print(tpl1)
# we cant insert or modify tuple. This is difference between list and tuple.
#tpl1.insert[3]= 123              ---error 'tuple' object has no attribute 'insert'

#tpl1[3]= 123                     ----TypeError: 'tuple' object does not support item assignment

print(tpl1*3)
print(tpl1.count(20)) #  How much times 20 number occurse in tuple.

print(tpl1.index('xyz'))








