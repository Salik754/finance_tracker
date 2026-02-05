"""
Finance tracker
A simple finance tracker application to manage personal expenses and income.
"""

# Ask user for monthly allowance
allowance = float(input("Enter your monthly allowance($): "))
# Ask for expenses
clothes = float(input("Enter your clothing expenses($): "))
food = float(input("Enter your food expenses($): "))
tranport = float(input("Enter your transport expenses($): "))
# Calculate total expenses
total_expenses = clothes + food + tranport

# CAlculate remaining balance
remaining_balance = allowance - total_expenses

##Display summary
print(f"Monthly allowance: ${allowance}")
print(f"Total expenses: ${total_expenses}")
print(f"Remaining balance: ${remaining_balance}")

# Display message based on remaining balance
if remaining_balance > 0:
    print("You are within budget.")
elif remaining_balance == 0:
    print("You have used your entire allowance.")
else:
    print("You are over budget.")
# End of the program
