# Shatika Oliver
# April 27, 2025
# P3LAB
# This program calculates the minimum number of dollars, quarters, dimes, nickels, and pennies for a given amount

# Get user input
amount = float(input("Enter the amount of money as a float: $"))

# Convert dollars to cents (integer)
cents = int(round(amount * 100))

# If the amount is 0, print "No change"
if cents == 0:
    print("No change")
else:
    # Dictionary to store coins and their values
    coins = {
        'Dollar': 100,
        'Quarter': 25,
        'Dime': 10,
        'Nickel': 5,
        'Penny': 1
    }

    # Go through each coin type
    for coin, value in coins.items():
        count = cents // value
        cents -= count * value

        if count > 0:
            if count == 1:
                print(f"{count} {coin}")
            else:
                # Add 's' for plural form
                if coin == 'Penny':
                    print(f"{count} Pennies")
                else:
                    print(f"{count} {coin}s")
