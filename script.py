#!/usr/bin/env python3
INCH_TO_CM = 2.54
CM_TO_INCH = 1 / INCH_TO_CM

# Display the menu
print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

# Get the user's choice
choice = input("Make your selection (1, 2): ")

if choice == "1":
    inches = float(input("Enter inches: "))
    cm = inches * INCH_TO_CM
    print(f"Number of cm: {cm}")
elif choice == "2":
    cm = float(input("Enter cm: "))
    inches = cm * CM_TO_INCH
    print(f"Number of inches: {inches}")
else:
    print("Invalid entry")
