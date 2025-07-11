# This script will calculate the user’s monthly savings based on inputted monthly income and expenses.
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

# User Input for Financial Details:
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses =  float(input("Enter your monthly income: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% interest (compound interest not applied, just simple for 1 year)

rate = 0.05
annual_savings = monthly_savings * 12
projectSaving = annual_savings + (annual_savings * rate)

# Output Results:

print(f"Your monthly savings are ${monthly_savings:.2f}" )
print(f"Projected savings after one year, with interest, is: ${projectSaving:.2f}")
