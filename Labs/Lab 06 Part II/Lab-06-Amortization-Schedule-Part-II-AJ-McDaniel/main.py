'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" This program can be used to create an amortization schedule for a loan.
"""

##### FUNCTION DEFINITIONS #####

def find_loan():
  loan = float(input("Please enter the initial loan amount: $"))

  while loan <= 0:
    loan = float(input("Invalid input. Please enter the initial loan amount: $"))

  return loan



def find_interest():
  interest = float(input("Please enter the annual interest rate in percentages: "))

  while interest > 100 or interest <= 0:
    interest = float(input("Invalid input. Please enter the annual interest rate in percentages: "))

  return interest / 1200



def find_term():
  term = int(input("Please enter the number of years to pay off the loan within: "))

  while term <= 0:
    term = int(input("Invalid input. Please enter the number of years to pay off the loan within: "))

  return term


def create_Schedule(loan, monthly_interest_rate, term):
  output = str.format(f"{'Payment Number    ' :^15} {'Payment  ':>10} {'':5} {' Interest ':>10} {'':5} {'Principle':>10} {'':5} {'Balance':>10}\n")
  num_of_payments = term * 12
  payment = loan * ((monthly_interest_rate * (1 + monthly_interest_rate) ** num_of_payments) / ((1 + monthly_interest_rate)**num_of_payments - 1))

  balance = loan

  for i in range(1, num_of_payments + 1):
    interest = balance * monthly_interest_rate
    principle = payment - interest
    balance -= principle

    output += str.format(f"{i:^15}(${payment:10,.2f}){'':5}(${interest:10,.2f}){'':5}(${principle:10,.2f}){'':5}${balance:10,.2f}\n")


  return output
  



##### MAIN PROGRAM #####
def main():
  print("Welcome to the Amortization Calculator! With its help we can calculate and display the complete Amortization Schedule for a loan.\n")

  print(create_Schedule(find_loan(), find_interest(), find_term()))


main()