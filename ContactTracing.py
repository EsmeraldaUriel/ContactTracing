#Display a menu of options
print("==========MENU==========")
print(" 1 -> Add on item")
print(" 2 -> Search")
print(" 2 -> Exit (y/n)")

#Dictionary
Dictionary = {
    "Uriel Esmeralda": "09321313211",
    "Juan Luna": "0912312141",
    "Jeriko Rosales": "093122234"
}

#Option Function
while True:
    #Allow user to select item in the menu (check if valid)
    option = int(input("Choose in the menu 1-3: "))
    if option == 1:
        #Perform the selected option
        option_1keys = float(input("Full name: "))
        option_1values = int(input("Phone number: "))
        Dictionary.append(option_1keys, ":", option_1values)
        print("This is the new Contact List: ", Dictionary)

    elif option == 2:
        option_2 = float(input("Enter Full name: "))

    elif option == 3:
        option_3 = float(input("You want to exit or retry? "))

