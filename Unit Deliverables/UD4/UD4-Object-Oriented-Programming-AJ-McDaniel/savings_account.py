from bank_account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number="000000", balance=0.0, interest_rate=0.01):
        super().__init__(account_number, balance, "Savings")
        self.__interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + f" (Interest Rate: {self.__interest_rate:.2%})"

    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, rate):
        self.__interest_rate = rate

    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        return interest