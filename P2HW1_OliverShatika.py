# Shatika Oliver
# April 12, 2025
# Assignment: P2HW1
# A Python program to calculate and display travel expenses based on user input.

# Pseudocode (Logic):
# Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Calculate remaining balance
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

# Calculate remaining balance
remaining = budget - (gas_expense + accommodation_expense + food_expense)

# Display results
print("\n----------Travel Expenses----------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Gas:':20}${gas_expense:.2f}")
print(f"{'Accommodation:':20}${accommodation_expense:.2f}")
print(f"{'Food:':20}${food_expense:.2f}")
print("-----------------------------------")
print() # Blank line for spacing
print(f"{'Remaining Balance:':20}${remaining:.2f}")

