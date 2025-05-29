# Prompt the user for their monthly income
# Convert the input to a float to handle potential decimal values
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
# Convert the input to a float
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate of 5% (0.05 as a decimal)
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest
# Simplified formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
# First, calculate savings over 12 months without interest
savings_without_interest = monthly_savings * 12
# Then, calculate the interest earned on those annual savings
interest_earned = savings_without_interest * annual_interest_rate
# Finally, add the interest earned to the annual savings
projected_annual_savings = savings_without_interest + interest_earned

# Output Results
# Display the user's monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places

# Display the projected annual savings after including interest
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
