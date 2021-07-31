class StudentLoan:
    INTEREST = 0.01
    LOAN_PER_MONTH = 650

    def __init__(self, loan_id, holder, start_months):
        self.__id = loan_id
        self.__holder = holder
        self.__amount_left = start_months*self.LOAN_PER_MONTH
        self.__amount_paid = 0
        self.__in_effect = True
        self.__interest = self.INTEREST

    def get_id(self):
        return self.__id

    def get_holder(self):
        return self.__holder

    def get_amount_left(self):
        return self.__amount_left

    def get_amount_paid(self):
        return self.__amount_paid

    def get_interest(self):
        return self.__interest

    def is_in_effect(self):
        return self.__in_effect

    def take_more_loan(self, months):
        if self.__in_effect:
            self.__amount_left += months*self.LOAN_PER_MONTH

    def pay_loan(self, amount):
        if self.__in_effect:
            if amount > self.__amount_left:
                amount = self.__amount_left
            self.__amount_left -= amount
            self.__amount_paid += amount

    def pay_loan_compensation(self, credit):
        if self.__amount_left > 2500 and credit > 0:
            years = credit / 60
            max_amount = 1240 * years
            exceeding = self.__amount_left - 2500
            to_pay = 0.4 * exceeding
            if to_pay >= max_amount:
                to_pay = max_amount
            self.pay_loan(to_pay)

    def grow_yearly_interest(self):
        if self.__in_effect:
            self.__amount_left *= (1 + self.__interest)

    def terminate(self):
        if self.__in_effect and self.__amount_left == 0:
            self.__in_effect = False
            return True
        else:
            return False

    def __str__(self):
        info = ""

        if self.__in_effect:
            label = "in effect"
        else:
            label = "outdated"
        info += f'Student loan ({label}), loan id: {self.__id}\n'
        info += f"Loan holder: {self.__holder}\n"
        info += f"Amount left to pay: {self.__amount_left:.2f} eur\n"
        info += f"Amount paid: {self.__amount_paid:.2f} eur"

        return info
