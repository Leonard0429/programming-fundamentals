def checkCoord(x,y):
    if x >= 100 or x <= 250 and y >= 120 or y <= 220:
        print("True, coordinate is inside of the box")
    else:
        print("False, coordinate out of the box")

def main():
    x = int(input("Enter coordinates x: "))
    y = int(input("Enter coordinates y: "))
    result = checkCoord(x,y)
    print("For (", x, ",", y, ")")
    
main()
