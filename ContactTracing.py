#Display a menu of options
print("==========MENU==========")
print(" 1 -> Add on item")
print(" 2 -> Search")
print(" 2 -> Exit (y/n)")

#Dictionary
Dictionary = {}

#Option Function
while True:
    #Allow user to select item in the menu (check if valid)
    option = int(input("Choose in the menu 1-3: "))
    if option == 1:
        #Perform the selected option
        option_1keys = float(input("Full name: "))
        option_1values = int(input("Phone number: "))

    elif option == 2:
        option_2 = float(input("Enter Full name: "))

    elif option == 3:
        option_3 = float(input("You want to exit or retry? "))

