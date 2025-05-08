# Shatika Oliver
# April 12, 2025
# P2LAB2
# This program stores car models and their MPG in a dictionary, lets the user choose a car and input miles to drive, then calculates and displays the gas needed.

# Create the dictionary with vehicles and their MPG
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get and print all the keys
keys = vehicles.keys()
print(keys)
print()  # This adds the space before the prompt


# Ask the user to enter a vehicle name
vehicle = input("Enter a vehicle to see its mpg: ")

# Check if vehicle exists in dictionary
if vehicle in vehicles:
    mpg = vehicles[vehicle]
    print(f"\nThe {vehicle} gets {mpg} mpg.\n")

# Ask how many miles the user will drive
miles = float(input(f"How many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons_needed = miles / mpg

# Display result, rounded to two decimal places
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
