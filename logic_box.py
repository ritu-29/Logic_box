print("Welocme to the pattern generator and number Analyzer!")
while True:
    print("Select an option:")
    print("1.Generate a pattern")
    print("2.Analyze a range of number")
    print("3.Exit")

    ch=int(input("Enter your choice:"))


    if ch == 1: 
        row=int(input("Enter a number of rows for the pattern:"))
        for i in range(0,row+1):
            for j in range(i):
                print("*",end=" ")
            print()
            i=i+1
           

    elif ch == 2:
        s=int(input("Enter the start of range -"))
        e=int(input("Enter the end of range -"))
        
        for i in range(s,e+1):
            if  i % 2 ==0:
                print(f"Number {i} is even")
            else:
                print(f"Number {i} is Odd")
        sum=0
        for i in range(s,e+1):
            sum=sum+i
        print(f"Sum of all numbers from {s} and {e} is {sum}")

    elif ch == 3:
        print("Exiting the program.....goodbyee!!")
        break
           

    else:
        print("Invalid  Choice")

        
        