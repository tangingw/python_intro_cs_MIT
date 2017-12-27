def compute(annual_salary, portion_saved, total_cost, semi_annual_raise):

    portion_down_payment = 0.25

    num_month = 0
    increment_cycle = 0
    monthly_salary = (annual_salary/12.0)
    saving = 0
    current_savings = 0
    r = 0.04

    while current_savings < (total_cost * portion_down_payment):

        if (num_month + 1) % 6 == 0:

            increment_cycle += 1

        if (num_month + 1) == 7 + ((increment_cycle - 1)*6) and increment_cycle >= 1:

            monthly_salary = monthly_salary +  monthly_salary * semi_annual_raise

        saving = monthly_salary * portion_saved

        current_savings = current_savings + current_savings * (r / 12.0)
        current_savings = current_savings + saving
        num_month += 1

    return num_month

"""
def main():

    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual rase, as a decimal: "))

    num_month = compute(annual_salary, semi_annual_raise, portion_saved, total_cost)

    print("Number of months: %d" % num_month)


if __name__ == "__main__":

    main()
"""