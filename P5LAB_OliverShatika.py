# Shatika Oliver
# May 2, 2025
# P5LAB
# This program simulates a self-checkout machine by calculating change owed to a customer,
# and breaking it down into dollars, quarters, dimes, nickels, and pennies.

import random

def disperse_change(change):
    # Convert to cents to avoid floating point issues
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    cash_paid = float(input("How much cash will you put in the self-checkout? "))
    if cash_paid < amount_owed:
        print("Insufficient payment. Transaction cancelled.")
        return

    change = round(cash_paid - amount_owed, 2)
    print(f"Change is: ${change:.2f}\n")
    disperse_change(change)

main()










