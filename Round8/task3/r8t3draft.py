def gen_payment_dict(payment_file):
    payment_dict = {}

    for numid_and_payment in payment_file:
        numid_and_payment = numid_and_payment.strip()

        if numid_and_payment == "":
            continue

        try:
            num_id, payment = numid_and_payment.split(" ")
            num_id = num_id[:-1]

            num_id = int(num_id)
            payment = float(payment)

            payment_dict[num_id] = payment

        except:

            if ' ' not in numid_and_payment:
                print(f"Invalid line in payment file: {numid_and_payment}")

            else:
                num_id, payment = numid_and_payment.split(" ")
                print(f"Invalid payment amount: {payment}")

    return payment_dict


def gen_membership_dict(membership_file):
    membership_dict = {}

    for numid_name_address_phonenum_roll in membership_file:
        numid_name_address_phonenum_roll = numid_name_address_phonenum_roll.strip()

        numid_and_name_address_phonenum_roll = numid_name_address_phonenum_roll.split(";")

        try:
            numid = int(numid_and_name_address_phonenum_roll[0])

        except:
            continue

        name = numid_and_name_address_phonenum_roll[1]

        membership_dict[numid] = name

    return membership_dict


def cross_referencing_dicts(payment_dict, membership_dict):
    for m_num_id in membership_dict:
        found = False

        for p_num_id in payment_dict:
            # print(m_num_id, p_num_id)
            if m_num_id == p_num_id:
                found = True
                referred_payment = p_num_id, membership_dict[m_num_id], payment_dict[p_num_id]
                compute_payed_amount(referred_payment)
                break

        if not found:
            print(f"Membership fee missing: {m_num_id} {membership_dict[m_num_id]}")

    return


def compute_payed_amount(referred_payment):
    num_id, name, amount_paid = referred_payment

    fees = 10.00
    difference = amount_paid - fees

    # print(num_id, name, amount_paid, difference)

    if difference < 0.0:
        print(f"Membership fee partially missing: {num_id} {name}, {amount_paid:.2f} / 10.00 paid")

    elif difference > 0.0:
        print(f"Warning, excess amount paid:: {num_id} {name}, {amount_paid:.2f} / 10.00 paid")

    else:
        pass

    return


def main():
    # payment_filename = input("Enter the name of the payment file:\n")
    payment_filename = "payments_3.txt"
    with open(payment_filename, "r") as f:
        payment_file = f.readlines()

    payment_dict = gen_payment_dict(payment_file)
    print(f"\nPayment file {payment_filename} read!\n")


    # membership_filename = input("Enter the name of the membership file:\n")
    membership_filename = "member_list_3.txt"
    with open(membership_filename, "r") as f:
        membership_file = f.readlines()

    membership_dict = gen_membership_dict(membership_file)

    cross_referencing_dicts(payment_dict, membership_dict)

    print()
    print(f"All members listed in {membership_filename} have been checked.")


main()
