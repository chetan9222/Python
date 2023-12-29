# Range type is define in simple bracket ()
# e.g 1. r=range(15) , single value --- range from 0 to 14
# e.g 2. s=range(1,15) , double value --- range from 1 to 14 always exclude the last rage parameter i.e 5
# e.g 3  t=range(1,15,3) , Triple value (step value)--- range from 1 to 14 but skips 2 values and print 3rd value
# range function is useful in for loop.

r=range(15)
for i in r:
    print(i)

s=range(1,15)
for i in s:
    print(i)

t=range(1,15,3)
for i in t:
    print(i)


