######V37####### Type Set
# Set is define in curly braces {}.
# if we update the set it
# Set does not allow duplicates. it cannot print duplicates.
# Set does not perform repeatation i.e (s*3), indexing i.e s[0], slicing i.e s[0:5]
# set does not follow sequence or order of element.

s={10,20,30,40,10,10,50,60,20,20,20}

print(type(s))
print(s)

s.update([66,77])
print(s)

s.remove(40)
print(s)

# print(s*3) # TypeError: unsupported operand type(s) for *: 'set' and 'int'

# print(s[5])  # TypeError: 'set' object is not subscriptable

# print(s[0:5]) # TypeError: 'set' object is not subscriptable

######V38####### Frozen Set

# we can convert Set in to frozen set by frozen set function. once we convert set into Frozen Set then we can not perform update and remove operation.

f=frozenset(s)

print(f)
print(type(f))

# f.update([100]) # AttributeError: 'frozenset' object has no attribute 'update'
# f.remove(30) # AttributeError: 'frozenset' object has no attribute 'remove'
