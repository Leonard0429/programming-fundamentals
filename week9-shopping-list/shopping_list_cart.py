def shopping_list_cart():
    shopList = []
    while True:
        print("\n--Shopping List--")
        print("1. Add item")
        print("2. Remove item")
        print("3. Count item in list")
        print("4. End")
        choice = (input("Enter your choice:"))
        if choice == '1':
            item = input("Enter item name (add): ")
            if item in shopList:
                print("Item already in list, Choose another product.")
                print("Current shopList:",shopList)
            else:
                shopList.append(item)
                print(item,"added.")
                print("Current shopList:",shopList)
        elif choice == '2':
            item = (input("Enter item name (remove): "))
            if item in shopList:
                shopList.remove(item)
                print(item,"removed.")
                print("Current shopList:",shopList)
            else:
                print("Item not in list.")
        elif choice == '3':
            count = len(shopList)
            print("Item in list:",count)
            print("Current shopList:",shopList)
        elif choice == '4':
            print("Thank you for using the shopping list!.")
            break
        else:
            print("Invalid input. Please type number from 1-4.")
            
shopping_list_cart()
