'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" This program is to create a stack of flashcards then have the user test themselves.
"""
##### IMPORTS #####

##### CONSTANTS #####
FILE_NAME = "database.txt"
##### FUNCTION DEFINITIONS #####
def build_dict(fileName: str):
    dict = {}
    
    try:
        in_file = open(fileName, 'r')
        line = in_file.readline()
        while line != "":
            KVList = (line.split(","))
            dict[KVList[0]] = KVList[1]
            line = in_file.readline()
    except KeyError as err:
        print(err)

    return dict

def check_dict(key: str, dictionary):
    return dictionary.get(key, 'No Match Found')
    
##### MAIN PROGRAM #####
def main():
    sentinel = True
    choice = ""
    dictionary = build_dict(FILE_NAME)

    print("Let's review your flashcards!\n")

    while sentinel:
        for item in dictionary:
            print("Question:", item)
            input("Press Enter to see the answer:")
            print("Answer:", dictionary[item])

        choice = input("End of Deck. Redo all cards?(Y/N): ").upper()
        while choice != 'Y' and choice != 'N':
            choice = input("Invalid Input: Please try again. Redo all cards?(Y/N): ").upper()

        if choice == 'N': 
            sentinel = False

    print("\nQuestion Review time.")
    choice = input("Enter Question(stop to end): ")
    
    while choice != 'stop':
        print(check_dict(choice, dictionary))
        choice = input("Enter Question(stop to end): ")
    
    print("End of Program.")
        
main()
