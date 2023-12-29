######V41####### Dictionary Type
# Dictionary type is define in Curly braces {}
# Dictionary type element contains the KEY and VALUE saparated by colan :
# we can also use String as a key in dictionary type but we use numbers here
# e.g

dict1={1:"Chetan",2:"Prashant",3:"Raj"}
print(type(dict1))
print(dict1)

# there are different methods of dict type like print(dict1.     ---- type this and you will get suggessions try the all

print(dict1.items())
print(dict1.keys())

# we can access value by passing KEY
print(dict1[2])

# we can delete the element by using del function that are available in language

del dict1[3]
print(dict1)

# dictionary type using for loop
k=dict1.values()
for i in k:
    print(i)