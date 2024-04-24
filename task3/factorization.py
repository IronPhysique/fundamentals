
# FV = Future Value
# PV = Present Value (Initial Investment)
# r = Interest Rate (as a decimal)
# t = Time in years

def calculate_years(initial_investment, target_value, interest_rate):
    years = 0
    while initial_investment < target_value:
        initial_investment *= (1 + interest_rate)
        years += 1
    return years

initial_investment = float(input("Enter the initial investment amount (£): "))
target_value = float(input("Enter the target value (£): "))
interest_rate = float(input("Enter the interest rate (as a decimal): "))

years_to_target = calculate_years(initial_investment, target_value, interest_rate)
print(f"It will take {years_to_target} years for an initial investment of £{initial_investment} to grow to £{target_value} at an interest rate of {interest_rate * 100}%.")

