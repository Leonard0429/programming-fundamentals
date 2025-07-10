def findHypotenuse(length1, length2):
    squareOflength = length1 ** 2 + length2 ** 2
    hypo = squareOflength ** (1/2)
    return hypo

def main():
    length1 = float(input("Enter length 1 (cm): "))
    length2 = float(input("Enter length 2 (cm): "))
    hypotenuse = findHypotenuse(length1, length2)
    print("Length of hypotenuse: ", hypotenuse, "cm")

main()
