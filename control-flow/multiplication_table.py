# This script will ask the user to enter a number,
# then use a for loop to print the multiplication table for that number from 1 to 10.

# Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
    