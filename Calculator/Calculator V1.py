# print menu
print("Hello, what would you like to calculate")
print("Press 1 for Plus")
print("Press 2 for Minus")
print("Press 3 for Multiply")
print("Press 4 for Divide")
print("Press 5 for Exit")

# get user input
answer = int(input(""))

# continue until user chooses to exit
while answer != 5:
    # get user input for two numbers
    numb1 = float(input("First Number: "))
    numb2 = float(input("Second Number: "))
    
    # perform operation based on user choice
    if answer == 1:
        print("The answer is:", str(numb1 + numb2))
    elif answer == 2:
        print("The answer is:", str(numb1 - numb2))
    elif answer == 3:
        print("The answer is:", str(numb1 * numb2))
    elif answer == 4:
        if numb2 != 0:
            print("The answer is:", str(numb1 / numb2))
        else:
            print("You can't divide by zero!")
    else:
        print("Invalid choice. Please choose again.")

    # print menu and get user input again
    print("\nHello, what would you like to calculate")
    print("Press 1 for Plus")
    print("Press 2 for Minus")
    print("Press 3 for Multiply")
    print("Press 4 for Divide")
    print("Press 5 for Exit")
    answer = int(input(""))

# user chose to exit
print("Have a nice day")