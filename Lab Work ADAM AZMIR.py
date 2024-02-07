print("Choose a currency to convert")
print("1. USD")
print("2. EURO")
print("3. GBP")
print("4. SGD")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    RM = float(input("Enter the amount in Malaysian Ringgit (MYR): "))
    USD = 0.25 * RM
    print("Equivalent amount in US Dollar (USD) :", USD)
elif choice == 2:
    RM = float(input("Enter the amount in Malaysian Ringgit (MYR): "))
    EUR = 0.21 * RM
    print("Equivalent amount in Euro (EUR) :", EUR)
elif choice == 3:
    RM = float(input("Enter the amount in Malaysian Ringgit (MYR): "))
    GBP = 0.18 * RM
    print("Equivalent amount in Great Britain Pound (GBP) :", GBP)
elif choice == 4:
    RM = float(input("Enter the amount in Malaysian Ringgit (MYR): "))
    SGD = 0.33 * RM
    print("Equivalent amount in Singaporean Dollar (SGD) :", SGD)
else:
    print("Invalid choice. Please enter 1, 2, 3 or 4.")

