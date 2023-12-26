#######v30######## Create list
# in list we can store multiple values. we can give any name to list. we are using lst here.
lst=[10,True,30.5,3+5j,"this is string"]
print(lst)            # same as string we can use same functions in a list e.g
print(lst[3])
print(lst[2:5])
print(lst*4)
print(len(lst))

#######v31######## Adding and removing list elements
lst.append(40) #to add one element at the last here we add 40
print(lst)
lst.remove("this is string") # we are remove "this is string" element. also we can use delete function.
del(lst[2])  # delete is the in-built function in python.
print(lst)

#######v32########Few more list function

lst.insert(2,99)
print(lst)

lst1=[10.2,15,33,11,22,8]
lst1.sort()  # without parameter python print Ascending order. For Descending order "lst1.sort(reverse=True)"
print(lst1)

print(max(lst1))  # to print Largest number of list
print(min(lst1))  # to print Smallest number of list

