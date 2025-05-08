# Shatika Oliver
# April 26,2025
# P4HW2
# This program asks for employee name, pay rate, and hours worked,
# calculates regular pay and overtime pay, and shows totals after 
# all employees are entered.

# Pseudocode:
# 1. Initialize totals for overtime pay, regular pay, gross pay, and employee count
# 2. Ask user for employee name
# 3. While employee name is not "Done":
#     a. Ask for hours worked
#     b. Ask for pay rate
#     c. If hours worked > 40:
#         - Calculate overtime hours
#         - Calculate overtime pay
#         - Calculate regular pay (40 * pay rate)
#     d. Else:
#         - No overtime
#         - Regular pay = hours worked * pay rate
#     e. Calculate gross pay (regular pay + overtime pay)
#     f. Add values to totals
#     g. Display employee information
#     h. Ask for next employee name
# 4. When done, display totals

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Ask for first employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name != "Done":
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))
    
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display employee pay details
    print()
    print(f'Employee name:   {employee_name}')
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"OverTime":<15}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<15}')
    print('-' * 94)
    print(f'{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<19.2f}${regular_pay:<19.2f}${gross_pay:<14.2f}')
    print()

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# After all employees entered
print()
print(f'Total number of employees entered:  {employee_count}')
print(f'Total amount paid for overtime:  ${total_overtime_pay:.2f}')
print(f'Total amount paid for regular hours:  ${total_regular_pay:.2f}')
print(f'Total amount paid in gross:  ${total_gross_pay:.2f}')
