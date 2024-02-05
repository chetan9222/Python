# enter any number
# print number up to given number
# skip multiple of 10
# break if number is grater than 100
n = int(input("Please enter number to print the number up to that number"))
x = 0
while (x <= n):
    x += 1
    if x%10 == 0:
        continue
    if x >= 100:
        break
    print(x)

