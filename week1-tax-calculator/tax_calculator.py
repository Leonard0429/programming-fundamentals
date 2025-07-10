def calculate_tax(income, tax_rate): 
    tax_owed = round(income * tax_rate,2)
    return tax_owed

def total_tax(tax_rate):
    total = 0
    while True:
        income_str = input("Enter income amount (or type 'done' to finish): ")
        if income_str.lower() == "done": # remember lower / isdigit must put ()
            break
        if income_str.isdigit():
            income = float(income_str)
            tax = calculate_tax(income, tax_rate)
            print("Tax for this income: ",tax,"SGD")
            total += tax
        else: 
             print("Error , Please type a number or 'Done'.")
    print("Total owed income tax is: ",total,"SGD")
    return

tax_rate = float(input("Enter tax rate (as a decimal, e.g., 0.20 for 20%): "))
total_tax(tax_rate)
