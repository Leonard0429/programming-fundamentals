def square(num):
    return num * num

def sumOfSquares(n):
    total = 0
    for i in range(1, n + 1):
        total += square(i)
    return total

def main():
    n = int(input("Enter a number: "))
    if n < 1:
        print("Please put a valid number or a number bigger than 1.")
        return 
    result = sumOfSquares(n)
    print("Sum of result between 1 to", n , "is", result)

main()
