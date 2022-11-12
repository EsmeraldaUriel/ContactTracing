# Dictionary
Address = {}
PhoneNum = {}
Age = {}

# Option Function
while True:
    # Display a menu of options
    print("\n==========MENU==========")
    print(" 1 -> Add an item")
    print(" 2 -> Search")
    print(" 3 -> Exit (y/n)")
    print("=========================")

    # Allow user to select item in the menu (check if valid)
    option = int(input("\nChoose in the menu 1-3: "))
    if option == 1:
        # Perform the selected option
        option_1keys = input("Full name: ")
        option_1address = str(input("Address: "))
        Address[option_1keys] = option_1address
        option_1age = int(input("Age: "))
        Age[option_1keys] = option_1age
        option_1number = int(input("Phone number: "))
        PhoneNum[option_1keys] = option_1number
        print("\nSaved!")

    elif option == 2:
        option_2 = input("\nEnter Full name: ")
        if option_2 in Address:
            print("Full Name:", option_2,
                  "\nAddress:", Address[option_2])
            if option_2 in Age:
                print("Age: ", Age[option_2])
            elif option_2 in PhoneNum:
                print("Phone Number:", PhoneNum[option_2])
        else:
            print("The Contact is Not Existing")
    elif option == 3:
        option_3 = input("\nYou want to exit (y or n)? ")
        if option_3 == 'n' and 'N':
            continue
        elif option_3 == 'y' and 'Y':
            break
