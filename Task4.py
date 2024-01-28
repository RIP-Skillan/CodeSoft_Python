import random
l1=['Rock','Paper','Scissors']
l2=['R','P','S']
l3=['You Win','You Lose',"It's a Tie"]
while(1):
    a=input("\nEnter the first letter of your choice: \nR:Rock\nP:Paper\nS:Scissors\n")
    if a.upper() in l2:
        b=random.randint(0,2)
        c=l2.index(a.upper())
        if((b==0 and c==2)|(not(b==2 and c==0)and(b>c))):
            w=1
        elif(b==c):
            w=2
        else:
            w=0
        print("\nYour Choice:"+l1[c])
        print("Computer's Choice:"+l1[b])
        print(l3[w])
    else:
        print("Invalid Choice")
    d=input("Do you want to continue: Y or N: ")
    if(d=="N" or d=="n"):
        break