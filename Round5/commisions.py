def main():
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days

    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    # Implement your own code here that goes through the list of
    # sales and calculates and prints the commissions based on those sales.
    # Write then a command here that prints the total of commissions.
    limit = 300  # euros
    normal_commission = 0.075  # %
    bonus_commission = 0.14
    total_commission = []

    print("Commissions")
    for v in sales:

        if v >= limit:
            commission = v * bonus_commission

        else:
            commission = v * normal_commission

        total_commission.append(commission)
        print(f"{commission:.2f} eur")

    print(f"Total Commissions {sum(total_commission):.2f} eur.")


main()