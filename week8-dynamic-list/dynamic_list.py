numList = []
number = int(input("Enter your a number [0 to exit]: "))
while number != 0:  
    numList.append(number)
    print("Minimum number:",min(numList)) #minimum number
    print("Index of Maximum number:",numList.index(max(numList))) #index of max
    numList.sort() #sorting
    print(numList)
    number = int(input("Enter your a number [0 to exit]: "))
