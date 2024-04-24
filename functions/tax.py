

def getIncomeTax(salary):

    personal_allowance = 11850
    taxable_salary = max(0, salary - personal_allowance)
    
    tax_brackets = [
        (34500, 0.2),
        (150000, 0.4),
        (float("inf"), 0.45)
    ]

    tax = 0
    previous_limit = 0
    for limit, rate in tax_brackets:
        if taxable_salary > previous_limit:
            taxable_income = min(taxable_salary - previous_limit, limit - previous_limit)
            tax += taxable_income * rate
            previous_limit = limit
        else:
            break

    return tax


if __name__ == "__main__":
    try:
        salary = int(input("enter income: "))
        tax = getIncomeTax(salary)
        print(f"The tax for £{salary} is £{tax:.2f}")
    except ValueError:
        print("Invalid input.(numbers only)")

