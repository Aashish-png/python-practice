number= int(input("enter a number "))
diviser = number%2
diviser2= number%4

if (diviser==0):
    print("the number is even" )
elif(diviser2==0):
    print("the number is also diviser of 4")
else:    
    print("the number is odd")    
