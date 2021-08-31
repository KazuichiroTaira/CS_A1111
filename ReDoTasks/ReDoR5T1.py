def main():
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days

    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")

    LIMIT = 300                  # euros
    NORMAL_COMMISSION = 7.5      #  %
    BONUS_COMMISSION = 14        #  %

    """
    Implement your own code here that goes through the list of
    sales and calculates and prints the Commissions based on those sales.
    Write then a command here that prints the total of Commissions.
    """
    list_cms = [0.0] * days
    for i in sales:

        if i >= LIMIT:
            cms = i * BONUS_COMMISSION * 1/100

        else:
            cms = i * NORMAL_COMMISSION * 1/100

        list_cms.append(cms)

        print(f"{cms:.2f} eur")

    ttl_cms = sum(list_cms)
    print(f"Total Commissions {ttl_cms:.2f} eur.")

main ()
