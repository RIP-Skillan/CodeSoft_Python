l=[]

while(1):
    print("------------Menu----------\n1) Create\n2) Update\n3) View Tasks\n4) Exit\n--------------------------")
    c=int(input("Enter your Choice: "))
    match(c):
        case 1:
            l.append([input("Enter Task: "),input("Enter Deadline: ")])
        case 2:
            p=int(input("Enter the Task Number to be updated: "))
            if(p>0 and p<=len(l)):
                ch=int(input("Enter Update mode:\n1:Task\t2:Deadline\t3:Both Task and Deadline\n"))
                match(ch):
                    case 1:
                        l[p-1][0]=input("Enter the updated Task name: ")
                    case 2:
                        l[p-1][1]=input("Enter updated Deadline: ")
                    case 3:
                        l[p-1][0]=input("Enter the updated Task name: ")
                        l[p-1][1]=input("Enter updated Deadline: ")
                    case _:
                        print("Invalid Mode")
            else:
                print("Invalid Task Number")
        case 3:
            if(len(l)>0):
                print("_______TO-Do List______")
                for i in range(len(l)):
                    print("Task",i+1,":\nTask:",l[i][0],"\tDeadline:",l[i][1])
                    print("_______________________")
                print("__________End__________")
            else:
                print("To-Do List is empty")
        case 4:
            break
        case _:
            print("Invalid Choice")
                        
    