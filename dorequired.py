a=int(input("Enter a number") )
b=int(input("Enter a number") )
operation=input("enter operation(+,-,*,/):")
print(operation)
if(operation=="+"):
    print("Sum is:",a+b)
elif(operation=="-"):
    print("Difference is:",a-b)
elif(operation=="*"):
    print("Product is:",a*b)
elif(operation=="/"):
    print("Quotient  is:",a/b)
else:
    print("Wrong input \n\tPlease select +,-,*,/")
