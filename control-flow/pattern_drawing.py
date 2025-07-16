# Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer,
# then use nested loops to print a square pattern of that size made of asterisks (*).


# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
