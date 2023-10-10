#Create a calculator capable of performing addition, subtraction, 
#multiplication and division operations on two numbers. 
#Your program should format the output in a readable manner!
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c= input("Enter the operator you want to perform")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print (a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)    
else:
    print("give another operator")                
