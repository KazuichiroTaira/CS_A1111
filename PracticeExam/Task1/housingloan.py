def loan_calculator(a_list, total_interest):

    amount_of_loan, saving, loan_period = a_list

    result = amount_of_loan * ((1 + total_interest / 100) ** loan_period * total_interest / 100) / (
                (1 + total_interest / 100) ** loan_period - 1)

    return result


def main():
    # flag = True

    a_list = []
    # line = input("How much costs the house (euros)?\n")
    line = 150000
    amount_of_loan = int(line)
    a_list.append(amount_of_loan)

    # line = input("How much savings do you have (euros)?\n")
    line = 10000
    saving = int(line)
    a_list.append(saving)

    # line = input("What is the loan period (years)?\n")
    line = 15
    period = int(line)
    a_list.append(period)

    bank_and_interest = {}

    bank = 'a'
    # line = input("What is the opening costs in bank A (eur)?\n")
    line = 459
    opening_cost_a = int(line)
    # line = input("What is the loan margin in bank A (percentage)?\n")
    line = 0.65
    total_interest_a = float(line)

    r_a = loan_calculator(a_list, total_interest_a)

    bank_and_interest[bank] = r_a, opening_cost_a

    bank = 'b'
    # line = input("What is the opening costs in bank B (eur)?\n")
    line = 280
    opening_cost_b = int(line)
    # line = input("What is the loan margin in bank B (percentage)?\n")
    line = 0.8
    total_interest_b = float(line)

    r_b = loan_calculator(a_list, total_interest_b)
    bank_and_interest[bank] = r_b, opening_cost_b

    bank = 'c'
    # line = input("What is the opening costs in bank C (eur)?\n")
    line = 356
    opening_cost_c = int(line)
    # line = input("What is the loan margin in bank C (percentage)?\n")
    line = 0.7
    total_interest_c = float(line)

    r_c = loan_calculator(a_list, total_interest_c)
    bank_and_interest[bank] = r_c, opening_cost_c

    print(bank_and_interest)

    for i in bank_and_interest:
        print(i)
        r, opening_cost = bank_and_interest[i]
        result = (r * 15) + opening_cost
        print(result)
        # r = bank_and_interest[i] * 15
        # print(f"{r:.2f}")

    # min_val = min(bank_and_interest.values())    #minimum values
    # min_key = [k for k, v in bank_and_interest.items() if v == min_val]
    # print(min_key, min_val)   # <- this is the cheapest!!

    # total = min_val * 15

    # print(f"The bank {min_key} is the cheapest.")
    # print(f"The costs for {period: d} years loan are {cheapest:.2f} euros.")
    # print(f"The total payment is {total: .2f} euros excluding own funding of {savings: .2f} euros.")


main()
