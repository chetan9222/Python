items = ['onions','lettuse','tomato','olives','peppers','tomatoes'] # items list
print("Please enter the three toppings from the list ",items )

# Taking user choices
topping1 = input()
topping2 = input()
topping3 = input()

print("you are selected {},{},{}".format(topping1,topping2,topping3)) # display user choices

# Taking input, How many Sandwich wants of each choice
print("How many",topping1,"Sandwiches you want ? Please enter number") #
order1 =int(input())
print("How many",topping2,"Sandwiches you want ? Please enter number")
order2 =int(input())
print("How many",topping3,"Sandwiches you want ? Please enter number")
order3 =int(input())

# Display final bill
total =int((order1+order2+order3)*5)
print("Your final order total is : ",total)