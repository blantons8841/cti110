# Shatika Oliver
# April 27, 2025
# P3HW2
# This program calculates the gross pay for an employee, including overtime pay if worked over 40 hours.

# Pseudocode:
# 1. Ask user for employee's name
# 2. Ask for number of hours worked
# 3. Ask for employee's pay rate
# 4. If hours worked > 40:
#    a. Calculate overtime hours
#    b. Calculate overtime pay (1.5 times pay rate * overtime hours)
#    c. Calculate regular hours as 40 hours
# 5. Else:
#    a. No overtime hours
#    b. No overtime pay
#    c. Regular hours are total hours worked
# 6. Calculate regular pay (regular hours * pay rate)
# 7. Calculate gross pay (regular pay + overtime pay)
# 8. Display employee info in a formatted table

# Inputs
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Processing
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_hours = 40
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Outputs
print("-" * 60)
print(f"Employee name: {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("-" * 90)
print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")
