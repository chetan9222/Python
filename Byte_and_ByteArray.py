#######V40###### bytes and bytearray
######1. Bytes :
# we can convert list in bytes by bytes function, the max value of bytes is 255.
# we can not perform element add or remove in bytes
# no Slicing and repeatation allowed in both bytes and bytearray

lst=[10,20,30,40,234]
b1=bytes(lst)  # convert list to bytes
print(type(b1))

# b1[3]=22 # TypeError: 'bytes' object does not support item assignment

#####2. Bytearray
# we can assign or perform element add or remove in bytearray
# no Slicing and repeatation allowed in both bytes and bytearray i.e b2*2 and b2[2:5]
b2=bytearray(lst)
print(type(b2))
b2[2]=22