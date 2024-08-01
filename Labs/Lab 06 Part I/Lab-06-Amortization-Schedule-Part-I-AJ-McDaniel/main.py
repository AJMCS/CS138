'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): none
'''
""" This program can be used to create an amortization schedule for a loan.
"""

##### FUNCTION DEFINITIONS #####
def create_Schedule(loan, monthly_interest_rate, term):
  output = str.format(f"{'Payment Number:' :^15} {'Payment':>10} {'':5} {'Interest':>10} {'':5} {'Principle':>10} {'':5} {'Balance':>10}\n")
  num_of_payments = term * 12
  payment = loan * ((monthly_interest_rate * (1 + monthly_interest_rate) ** num_of_payments) / ((1 + monthly_interest_rate)**num_of_payments - 1))

  balance = loan

  for i in range(1, num_of_payments + 1):
    interest = balance * monthly_interest_rate
    principle = payment - interest
    balance -= principle

    output += str.format(f"{i:^15} (${payment:10,.2f}){'':5}(${interest:10,.2f}){'':5}(${principle:10,.2f}){'':5}${balance:10.2f}\n")
    
    
  return output


##### MAIN PROGRAM #####
def main():
  print(create_Schedule(20000,(0.05/12),2))




main()