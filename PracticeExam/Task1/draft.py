RIR = 1.3     #reference interest rate


def main():

    # line = input("How much costs the house (euros)?\n")
    line = 150000
    cost_house = int(line)
    # a_list.append(amount_of_loan)

    # line = input("How much savings do you have (euros)?\n")
    line = 10000
    saving = int(line)
    # a_list.append(saving)

    # line = input("What is the loan period (years)?\n")
    line = 15
    loan_period = int(line)
    # a_list.append(loan_period)

    amount_of_loan = cost_house - saving


### banks ###
    banks = {}
    bank = "a"

    # line = input("What is the opening costs in bank A (eur)?\n")
    line = 356
    opening_cost_a = int(line)
    # line = input("What is the loan margin in bank A (percentage)?\n")
    line = 0.7
    loan_margin_a = float(line)

    total_interest_a = loan_margin_a + RIR

    r_a = amount_of_loan * ((1 + total_interest_a / 100) ** loan_period * total_interest_a / 100) / (
            (1 + total_interest_a / 100) ** loan_period - 1)

    total_payment_a = r_a * loan_period + opening_cost_a
    cost_a = total_payment_a - amount_of_loan

    banks[bank] = cost_a, total_payment_a

    bank = "b"
    # line = input("What is the opening costs in bank B (eur)?\n")
    line = 459       # 280
    opening_cost_b = int(line)
    # line = input("What is the loan margin in bank B (percentage)?\n")
    line = 0.65      # 0.8
    loan_margin_b = float(line)

    total_interest_b = loan_margin_b + RIR

    r_b = amount_of_loan * ((1 + total_interest_b / 100) ** loan_period * total_interest_b / 100) / (
            (1 + total_interest_b / 100) ** loan_period - 1)

    total_payment_b = r_b * loan_period + opening_cost_b
    cost_b = total_payment_b - amount_of_loan

    banks[bank] = cost_b, total_payment_b

    bank = "c"

    # line = input("What is the opening costs in bank C (eur)?\n")
    line = 459 #356
    opening_cost_c = int(line)
    # line = input("What is the loan margin in bank C (percentage)?\n")
    line = 0.65   #0.7
    loan_margin_c = float(line)

    total_interest_c = loan_margin_c + RIR

    r_c = amount_of_loan * ((1 + total_interest_c / 100) ** loan_period * total_interest_c / 100) / (
            (1 + total_interest_c / 100) ** loan_period - 1)

    total_payment_c = r_c * loan_period + opening_cost_c
    cost_c = total_payment_c - amount_of_loan

    banks[bank] = cost_c, total_payment_c
    print(banks)
    min_val = min(banks.values())  # minimum values
    min_keys_list = [k for k, v in banks.items() if v == min_val]
    min_key = min_keys_list[0]
    # print(min_key, min_val)   # <- this is the cheapest!!

    cost, cheapest_total_payment = min_val

    print(f"The bank {min_key.upper()} is the cheapest.")
    print(f"The costs for {loan_period} years loan are {cost:.2f} euros.")
    print(f"The total payment is {cheapest_total_payment:.2f} euros excluding own funding of {saving:.2f} euros.")

    ### think if there were two lowest values? meaning two loans are same

main()
