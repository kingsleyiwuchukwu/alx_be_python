# Objective: Solidify your understanding of class methods 
# and static methods in Python by implementing examples of each in a class,
# demonstrating their usage and differences.

# Task Description:
# Create a Python script named class_static_methods_demo.py. 
# In this script, define a class Calculator that includes both a class method 
# and a static method to perform calculations. T
# his task aims to illustrate when and how to use @classmethod and @staticmethod decorators, 
# highlighting their differences and practical applications.

# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
