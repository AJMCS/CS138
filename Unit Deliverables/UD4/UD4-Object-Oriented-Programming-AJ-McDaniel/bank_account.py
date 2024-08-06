class BankAccount:
    def __init__(self, account_number="000000", balance=0.0, account_type="Checking"):
        self.__account_number = account_number
        self.__balance = balance
        self.__account_type = account_type

    def __str__(self):
        return f"Account {self.__account_number} ({self.__account_type}): ${self.__balance:.2f}"

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_account_type(self):
        return self.__account_type

    # Setters
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        self.__balance = balance

    def set_account_type(self, account_type):
        self.__account_type = account_type

    # Additional methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False