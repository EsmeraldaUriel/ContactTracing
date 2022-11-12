#Display a menu of options
print("==========MENU==========")
print(" 1 -> Add on item")
print(" 2 -> Search")
print(" 2 -> Exit (y/n)")

#Dictionary
Dictionary = {}

Address = {}
PhoneNum = {}

#Option Function
while True:
    #Allow user to select item in the menu (check if valid)
    option = int(input("\nChoose in the menu 1-3: "))
    if option == 1:
        #Perform the selected option
        option_1keys = input("Full name: ")
        option_1address = input("Address: ")
        Address[option_1keys] = option_1address
        option_1number = int(input("Phone number: "))
        PhoneNum[option_1keys] = option_1number
        print("\nSaved!")

    elif option == 2:
        option_2 = input("\nEnter Full name: ")
        for key in Address:
            print("Full Name:", key,
                  "\nAddress:", Address[key])
        for key in PhoneNum:
            print("Phone Number:", PhoneNum[key])

    elif option == 3:
        option_3 = input("\nYou want to exit (y or n)? ")
        if option_3 == "n" or "N":
            continue
        elif option_3 == "y" or "Y":
            break

