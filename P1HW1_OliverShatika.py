# Shatika Oliver
# April 5, 2025
# Assignment: P1HW1
# A Python program that collects user input and performs exponentiation, addition, and subtraction.

# -----Calculating Exponents-----
print("-----Calculating Exponents-----")
print() # blank line spacing

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print ()# blank line before output
print(base, "raised to the power of", exponent, "is", result, "!!")
print() # another blank line

print("-----Addition and Subtraction-----")
print()

start = int(input("Enter a starting integer: "))
to_add = int(input("Enter an integer to add: "))
to_subtract = int(input("Enter an integer to subtract: "))

final = start + to_add - to_subtract

print()
print(start, "+", to_add, "-", to_subtract, "is equal to", final)
