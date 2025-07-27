# define a function that performs basic arithmetic operations.

def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error cannot divide by zero"
        return num1 / num2
    else:
        return "Error Invalid Operation"