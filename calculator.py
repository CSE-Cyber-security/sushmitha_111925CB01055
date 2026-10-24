print("----SIMPLE calculator----")
x=int(input("enter value for x:"))
y=int(input("enter value for y:"))
while True:
    print("1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.exit\n")
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
           print("calculating addition....")
           print("x+y=",x+y)

        case 2:
           print("calculating subtraction....") 
           print("x-y=",x-y)
        case 3:
           print("calculating multiplication....")
           print("x*y=",x*y)
        case 4:
           print("calculating division....")
           if y!=0:
            print("x/y=",x/y)
           else:
            print("error:division by zero not allowed")
        case 5:
           print("program exit")
           break
        case _:
           print("invalid choice!!")
          
