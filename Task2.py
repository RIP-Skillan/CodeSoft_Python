def read():
    a=int(input("Enter 1st operand: "))
    b=int(input("Enter 2nd operand: "))
    return a,b

while(1):
    print("-----------Menu-----------\n1) Add\n2) Subtract\n3) Multipy\n4) Divide\n5) Exit\n------------End-----------")
    c=int(input("Enter your choice: "))
    match c:
        case 1:
            a,b=read()
            print(a,"+",b,"=",(a+b))
        case 2:
            a,b=read()
            print(a,"-",b,"=",(a-b))
        case 3:
            a,b=read()
            print(a,"*",b,"=",(a*b))
        case 4:
            a,b=read()
            print(a,"/",b,"=",round((a/b),2))
        case 5:
            break
        case _:
            print("Invalid Choice")
        
