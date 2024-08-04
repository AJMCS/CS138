'''
DEVELOPER: AJ McDaniel
COLLABORATORS: None
DATE: 8/3/2024
'''

"""A flash card language learner game for Japanese kanji characters.

This program is to help those looking to improve on their reading skill in the Japanese language. There are typically about 3000 different kanji characters in the typical Japanese newpaper - so to facilitate your learning and memorization, this program will quiz you on some of the most common kanji characters encountered in daily life.
"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
import random


##########################################
# FUNCTIONS:
##########################################

def create_dict(kanji: list, english: list) -> list:
    dictionary = {}
    for i in range(len(kanji)):
        dictionary[kanji[i]] = english[i]

    return dictionary


def pick_questions(questionsList: dict):
    quiz = {}
    keys = list(questionsList.keys())
    
    while(len(quiz) < 5):
        random_key = random.choice(keys)
        #Check if the question already exists in the test
        if random_key not in quiz:
            quiz[random_key] = questionsList[random_key]

    return quiz

def ask_questions(quiz: dict):
    print("\n\n")
    score = 0
    
    for items in quiz:
        answer = input(f"What is the meaning of the character {items} in english? ")

        if(answer == quiz[items]):
            print("\n\nCorrect! Good job")
            score += 1
        else:
            print(f"\n\nIncorrect! the answer is {quiz[items]}.")
    
    return score


##########################################
# MAIN PROGRAM:
##########################################
def main():
    sentinel = True
    kanji = ["一","二","三","水","火","木","日","円","学","時","日本","東京","拉麺","先生","大学"]
    english = ["one","two","three","water","fire","tree","sun","yen","study","time","japan","tokyo","ramen","sensei","college"]
    questionsList = create_dict(kanji, english)

    print("Welcome to Kanji Quiz!\n\n")
    
    while(sentinel):

        play = input("Start a new game? (y/n): ").lower()

        while(play != 'y' and play != 'n'):
            play = input("Invalid Entry: Please enter (y/n): ")

        if(play == 'y'):
            correct = 0
            quiz = pick_questions(questionsList)

            correct += ask_questions(quiz)

            print("Final Score:", str(correct) + "/5")

        else:
            sentinel = False


    print("\n\nprogram ended.")

main()