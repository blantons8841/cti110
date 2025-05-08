# Shatika Oliver
# April 12, 2025
# P2HW2
# This program prompts the user to input grades for six modules, stores them in a list, and displays the lowest, highest, total, and average grade.

# Pseudocode:
# Prompt the user to input grades for Module 1 through Module 6.
# Store each input in a variable.
# Add all the grade variables to a list called module_grades.
# Get the lowest grade using min()
# Get the highest grade using max()
# Calculate the sum using sum()
# Calculate the average using sum() / len()
# Display the results.

# Collect grades from user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
module_grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Perform calculations
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Display results
print("\n------------Results------------")
print("Lowest Grade:      {:.1f}".format(lowest))
print("Highest Grade:     {:.1f}".format(highest))
print("Sum of Grades:     {:.1f}".format(total))
print("Average:           {:.2f}".format(average))
print("---------------------------------------")

