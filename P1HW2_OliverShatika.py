# Shatika Oliver
# April 5, 2025
# Assignment: P1HW2
# A Python program to calculate and display travel expenses based on user input.

# Pseudocode (Logic):
# Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Display results

# Ask user to enter their budget
print("This program calculated and displays travel expenses")
print() # Blank line for spacing
budget = float(input("Enter your budget: "))
print() # Blank line for spacing
# Ask user to enter travel destination
destination = input("Enter your travel destination: ")
print() # Blank line for spacing
# Ask user for amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas? "))
print() # Blank line for spacing
# Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
print() # Blank line for spacing
# Ask user for amount they will spend on food
food_expense = float(input("Last, how much do you need for food? "))

# Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_balance = budget - total_expenses
print() # Blank line for spacing
# Display results
print("----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)
print() # Blank line for spacing
print("Fuel:", gas_expense)
print("Accommodation:", accommodation_expense)
print("Food:", food_expense)
print() # Blank line for spacing
print("Remaining Balance:", remaining_balance)
