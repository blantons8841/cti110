# Shatika Oliver
# April 11, 2025
# P2LAB1
# This program asks the user to input the radius of a circle and then calculates and displays the diameter, circumference, and area.

import math

# Ask the user for the radius
radius = float(input("What is the radius of the circle? "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")

