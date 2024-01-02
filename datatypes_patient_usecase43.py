id= 1
First_name= 'Bob'
Last_name= 'White'
ssn= '123-56-6789'
Has_Insurance= True
Billing_Ammount= "10000"  # This is string type Billing_Ammount so we un able to perform mathematical calculation on it so we need to conver it into float.
print(type(Billing_Ammount))
Billing_Ammount=float(Billing_Ammount) # we convert the billing amount into float for calculation
print(type(Billing_Ammount))  # to check Billing_Ammount converted into float or not
print(id,First_name,Last_name,ssn,Has_Insurance,Billing_Ammount)

# now we wants only last four digit of ssn so we use slicing here.
print(id,First_name,Last_name,ssn[7:len(ssn)],Has_Insurance,Billing_Ammount)

