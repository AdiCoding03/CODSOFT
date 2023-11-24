print("CALCULATOR \n\n")
print("Enter + for Addition")
print("Enter - for Subtraction")
print("Enter x for Multiplication")
print("Enter / for Division")
print("Enter % for P\n")

while(1):
    o=input("Enter the arithmetic operation: ")

    if(o=="+"):
        a=int(input("Enter the 1st number: "))
        b=int(input("Enter the 2nd number: "))
        r=a+b
    elif(o=="-"):
        a=int(input("Enter the 1st number: "))
        b=int(input("Enter the 2nd number: "))
        r=a-b
    elif(o=="x"):
        a=int(input("Enter the 1st number: "))
        b=int(input("Enter the 2nd number: "))
        r=a*b
    elif(o=="/"):
        a=int(input("Enter the 1st number: "))
        b=int(input("Enter the 2nd number: "))
        r=a/b
    elif(o=="%"):
        a=int(input("Enter the 1st number: "))
        b=int(input("Enter the 2nd number: "))
        r=a%b
    else:
        print("Invalid Operation\n")
        continue
              
    print("\n")
    print("Result")
    print(a,o,b,"=",r,"\n")
    
    print("Enter = to Continue")
    print("Enter # to Exit")
    ch=input("Enter your choice: ")
    print("\n")
    if(ch=="#"):
        break
    if(ch=="="):
        continue
    

