def main():
    ref_interest = 1.3
    total_interest_rate = ref_interest + loan_interest

    housing_price = int(input("How much costs the house (euros)?\n"))
    savings = int(input("How much savings do you have (euros)?\n"))
    loan_period = int(input("What is the loan period (years)?\n"))

    a_opn_cst = int(input("What is the opening costs in bank A (eur)?"))
    a_loan_interest = int(input("What is the loan marginal in bank A (percentage)?"))

    r = amount_of_loan * ((1 + total_interest / 100)**period * total_interest/100) / ((1 + total_interest/100)**period - 1)

    b_opn_cst = int(input("What is the opening costs in bank B (eur)?"))
    b_loan_interest = int(input("What is the loan marginal in bank B (percentage)?"))

    c_opn_cst = int(input("What is the opening costs in bank A (eur)?"))
    a_loan_interest = int(input("What is the loan marginal in bank A (percentage)?"))

    amount_of_loan * ((1 + total_interest / 100) ** period * total_interest / 100) / (
                (1 + total_interest / 100) ** period - 1)


    print(f"The costs for {period:d} years loan are {cheapest:.2f} euros.")
    print(f"The total payment is {total:.2f} euros excluding own funding of {savings:.2f} euros.")