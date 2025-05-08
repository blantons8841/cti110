# Shatika Oliver
# April 26, 2025
# P4LAB2
# A program that asks the user to enter an integer.

def get_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")

def display_multiplication_table(num):
    for i in range(1, 13):
        print(f"{num} * {i} = {num * i}")

def main():
    while True:
        num = get_integer()
        if num is None:
            print("\nCannot accept negative values.")
        elif num >= 0:
            display_multiplication_table(num)
        else:
            print("\nThis program does not handle negative numbers.")

        while True:
            repeat = input("\nWould you like to run the program again? ").lower()
            if repeat == "yes":
                break
            elif repeat == "no":
                print("\nExiting program.")
                return
            else:
                print("\nInvalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
