import tkinter as tk
from tkinter import messagebox
from bank_account import BankAccount
from savings_account import SavingsAccount

class FinanceManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Finance Manager")
        self.checking = BankAccount("12345", 1000, "Checking")
        self.savings = SavingsAccount("67890", 5000, 0.02)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=0, column=1)

        tk.Button(self.master, text="Deposit to Checking", command=self.deposit_checking).grid(row=1, column=0)
        tk.Button(self.master, text="Withdraw from Checking", command=self.withdraw_checking).grid(row=1, column=1)
        tk.Button(self.master, text="Deposit to Savings", command=self.deposit_savings).grid(row=2, column=0)
        tk.Button(self.master, text="Withdraw from Savings", command=self.withdraw_savings).grid(row=2, column=1)
        tk.Button(self.master, text="Apply Interest", command=self.apply_interest).grid(row=3, column=0, columnspan=2)

        self.status_text = tk.Text(self.master, height=5, width=40)
        self.status_text.grid(row=4, column=0, columnspan=2)
        self.update_status()

    def deposit_checking(self):
        self.perform_transaction(self.checking.deposit, "Deposit")

    def withdraw_checking(self):
        self.perform_transaction(self.checking.withdraw, "Withdrawal")

    def deposit_savings(self):
        self.perform_transaction(self.savings.deposit, "Deposit")

    def withdraw_savings(self):
        self.perform_transaction(self.savings.withdraw, "Withdrawal")

    def apply_interest(self):
        interest = self.savings.apply_interest()
        messagebox.showinfo("Interest Applied", f"Interest of ${interest:.2f} applied to savings account.")
        self.update_status()

    def perform_transaction(self, transaction_func, transaction_type):
        try:
            amount = float(self.amount_entry.get())
            if transaction_func(amount):
                messagebox.showinfo("Success", f"{transaction_type} of ${amount:.2f} successful.")
            else:
                messagebox.showerror("Error", f"{transaction_type} failed. Please check the amount.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
        self.update_status()

    def update_status(self):
        status = f"{self.checking}\n{self.savings}"
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, status)