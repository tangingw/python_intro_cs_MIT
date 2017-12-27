PORTION_DOWN_PAYMENT = 0.25


def compute(annual_salary, portion_saved, total_cost, semi_annual_raise):

    saving = 0
    num_month = 0
    increment_cycle = 0
    current_savings = 0

    monthly_salary = (annual_salary/12.0)

    investment_return = 0.04

    while current_savings < (total_cost * PORTION_DOWN_PAYMENT) and num_month < 36:

        """
        Divide the months into a cycle of 6 months
        """

        if (num_month + 1) % 6 == 0:

            increment_cycle += 1

        """
        The adjustment of the salary will only happen after 6th, 12th, 18th and so on
        meaning the adjustment can only take place on 7th, 13th, 19th and so on months
        """

        if (num_month + 1) == 7 + ((increment_cycle - 1)*6) and increment_cycle >= 1:

            monthly_salary = monthly_salary +  monthly_salary * semi_annual_raise

        saving = monthly_salary * portion_saved

        current_savings = current_savings + current_savings * (investment_return / 12.0)
        current_savings = current_savings + saving
        num_month += 1

    return current_savings


def bisection_compute(annual_salary):

    steps = 0
    semi_annual_raise = 0.07
    total_cost = 1000000
    down_payment = PORTION_DOWN_PAYMENT * total_cost

    minimum = 0
    maximum = 10000
    mid = (minimum + maximum)/2
    portion_saved = mid/10000

    current_savings = compute(annual_salary, portion_saved, total_cost, semi_annual_raise)
    epsilon = 1

    while abs(current_savings - down_payment) >= epsilon:

        if steps == 100:

            print("It is not possible to pay the down payment in three years.")
            exit(1)

        if current_savings > down_payment:

            maximum = mid

        else:

            minimum = mid

        mid = (minimum + maximum)/2
        portion_saved = mid/10000
        current_savings = compute(annual_salary, portion_saved, total_cost, semi_annual_raise)

        steps += 1

    print("Best savings rate: %f" % portion_saved)
    print("Steps in Bisection search: %d" % steps)


def main():

    annual_salary = 120000
    bisection_compute(annual_salary)


if __name__ == "__main__":

    main()
