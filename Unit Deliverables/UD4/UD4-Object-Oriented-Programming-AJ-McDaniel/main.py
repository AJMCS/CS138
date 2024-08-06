'''
DEVELOPER: AJ McDaniel
COLLABORATORS: None
DATE: 8/2/2024
'''

"""This is a finance Manager GUI that allows you to deposit, withdraw, and add interest

There are a lot of people who want to improve on their fiscal responsibility. This simple finance manager can help you simulate how money works. It allows for three basic functions. 1 depositing money, withdrawing money, and adding interest to your savings account based on the interest rate. This way you can see how interest compounds over time and play with different scenarios to get a general understanding of personal finance basics.
"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
import tkinter as tk
from bank_account import BankAccount
from savings_account import SavingsAccount
from fin_manager import FinanceManagerGUI


##########################################
# FUNCTIONS:
##########################################
# NONE


##########################################
# MAIN PROGRAM:
##########################################
def main():
    root = tk.Tk()
    app = FinanceManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()