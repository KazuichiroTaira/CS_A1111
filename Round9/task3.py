# Y1 SUMMER 2021
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Main program for exercise 9.3 - Student Loan

import random
from student_loan import StudentLoan


def print_loan(loan):
    print("Loan left to pay: {:10.2f} eur".format(loan.get_amount_left()))
    print("Loan paid:        {:10.2f} eur".format(loan.get_amount_paid()))
    print()


def start_and_take_loan():
    name = input("Enter your name:\n")
    years = int(input("For how many years are you taking student loan?\n"))
    while years <= 0:
        years = int(input("Enter a positive number!\n"))
    months = int(input("How many months per year?\n"))
    while not 1 <= months <= 12:
        months = int(input("The months must be between 1 and 12!\n"))
    print("You take the loan for {:d} months per year for {:d} years.".format(
        months, years))

    loan_id = str(random.randint(1000, 9999)) + "-" + str(
        random.randint(1000, 9999))
    loan = StudentLoan(loan_id, name, months)
    print()
    print("The loan at the beginning:")
    print(loan)

    loan.grow_yearly_interest()
    print(
        "You continue to take the loan for {:d} more years.".format(years - 1))
    print()
    for i in range(years - 1):
        loan.take_more_loan(months)
        loan.grow_yearly_interest()

    print("After {:d} years:".format(years))
    print_loan(loan)
    return loan


def graduate(loan):
    support = input(
        "You have graduated. Did you complete your degree within target time? (y/n)?\n")
    if support.lower() == "y":
        creds = int(input("How many credits is your degree?\n"))
        loan.pay_loan_compensation(creds)
        print("Loan after Kela's possible payment:")
        print_loan(loan)


def wait_and_grow_interest(loan):
    years_until_paying_back = int(
        input("How many years until you start paying the loan back?\n"))
    while years_until_paying_back < 0:
        years_until_paying_back = int(input("Enter a positive number or 0!\n"))
    if years_until_paying_back > 0:
        print("The loan continues to grow yearly interest.")
        for i in range(years_until_paying_back):
            loan.grow_yearly_interest()

        print("After {:d} more years:".format(years_until_paying_back))
        print_loan(loan)


def pay_back_loan(loan):
    print("You start paying the loan back.")

    monthly_payment = float(input(
        "What is the amount of monthly payment you want to make (eur)?\n"))

    while monthly_payment * 12 < loan.get_amount_left() * loan.get_interest():
        if monthly_payment <= 0:
            monthly_payment = float(input("Enter a positive number!\n"))
        else:
            print(
                "With that amount the interest grows faster than you can pay it back.")
            monthly_payment = float(input("Enter a larger amount:\n"))

    years_to_pay_back = 0
    months_to_pay_back = 0
    while loan.get_amount_left() > monthly_payment * 12:
        loan.pay_loan(monthly_payment * 12)
        loan.grow_yearly_interest()
        years_to_pay_back += 1
    while loan.get_amount_left() != 0:
        loan.pay_loan(monthly_payment)
        months_to_pay_back += 1
    print(
        "It took you {:d} years and {:d} months to pay back the loan.".format(
            years_to_pay_back, months_to_pay_back))


def terminate_loan(loan):
    print("The loan info at the end:")
    print(loan)

    print("Now the loan can be terminated.")
    print("Press enter to terminate loan.")
    input()
    if loan.terminate():
        print("Loan terminated.")
        print()
        print("Loan info after termination:")
        print(loan)
    else:
        print("For some reason the termination didn't work.")


def main():
    seed = int(input("Enter a seed for the random generator:\n"))
    random.seed(seed)

    loan = start_and_take_loan()
    graduate(loan)
    wait_and_grow_interest(loan)
    pay_back_loan(loan)
    print()
    terminate_loan(loan)

    print("Program ends.")


main()