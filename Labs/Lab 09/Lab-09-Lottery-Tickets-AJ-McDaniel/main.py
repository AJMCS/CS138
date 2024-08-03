'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" This program is to create lottery cards. The user can select their own numbers or have the numbers randomly selected for them.
"""
##### IMPORTS #####
import random

##### FUNCTION DEFINITIONS #####
def generate_ticket():
    unique_num = []
    mega_num = []
    result = []
    
    for i in range (1, 50):
        if i <= 19:
            unique_num.append(i)
            mega_num.append(i)
        else:
            unique_num.append(i)

    while len(result) < 5:
        num = random.sample(unique_num, 1)
        if num not in result:
            result.append(num[0])
    
    result.append(random.sample(mega_num,1)[0])

    return result

def create_ticket():
    numbers = []
    user_guess = 0
    
    for i in range(5):
        user_guess = int(input("Enter your lottery number between 1 and 49: "))
        
        while user_guess > 49 or user_guess < 1:
            user_guess = int(input("Invalid Entry: Please enter a number between 1 and 49: "))
        
        numbers.append(user_guess)
        
    user_guess = int(input("Enter your mega number between 1 and 19: "))

    while user_guess > 19 or user_guess < 1:
        user_guess = int(input("Invalid Entry: Please enter a number between 1 and 19: "))
    
    numbers.append(user_guess)

    return numbers
    

##### MAIN PROGRAM #####
def main():
    print('''Welcome to Python Lotto!
You have the option to choose your own lottery numbers or have them randomly selected for you.''')
    
    choice = input("Please enter C for custom or R for random: ").upper()

    while choice != 'C' and choice != 'R':
        choice = input("Invalid Entry: Please enter either C or R")
        
    result = generate_ticket() if choice == 'R' else create_ticket()

    print("Your lottery ticket is: ", str(result[0]), str(result[1]), str(result[2]), str(result[3]), str(result[4]), "(mega", str(result[5]) + ")")

main()
    