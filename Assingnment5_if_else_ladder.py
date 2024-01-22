p = int(input("enter your Physics marks :"))
c = int(input("enter your Chemistry marks :"))
m = int(input("enter your maths marks :"))
if p<=35:
    print("You are failed in Physics Subject")
if c<=35:
    print("You are failed in Chemistry Subject")
if m<=35:
    print("You are failed in Maths Subject")

average_marks = int(p+c+m)/3
print("Your average Marks are :",average_marks)

if average_marks<=59:
    print("Your Grade is : C")
elif average_marks<=69:
    print("Your Grade is : B")
elif average_marks>69:
    print("Your Grade is : A")
