def compute(annual_salary, portion_saved, total_cost):

    portion_down_payment = 0.25

    num_month = 0
    monthly_salary = (annual_salary/12.0)
    saving = 0
    current_savings = 0
    r = 0.04

    while current_savings < (total_cost * portion_down_payment):

        saving = monthly_salary * portion_saved
        current_savings = current_savings + current_savings * r / 12.0
        current_savings = current_savings + saving
        num_month += 1

    return num_month

def compute_geometrical(annual_salary, portion_saved, total_cost):

    portion_down_payment = 0.25

    num_month = 0
    monthly_salary = (annual_salary/12.0)
    saving = 0
    current_savings = 0
    r = 0.04

    while current_savings < (total_cost * portion_down_payment):

        """
        Formula for Compound Interest
        """
        saving = (annual_salary/12.0) * portion_saved

        current_savings = (saving/(r/12))*((1 + (r/12))**(num_month + 1) - 1)
        num_month += 1

    return num_month


"""
def main():

    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))

    print("Number of months: %d" % compute_geometrical(annual_salary, portion_saved, total_cost))


if __name__ == "__main__":

    main()
"""