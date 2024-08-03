"""A one line summary of the program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the program.
"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
import random


##########################################
# FUNCTIONS:
##########################################

def create_tuple(kanji: list, english: list) -> list:
    tupleList = []
    for i in range(len(kanji)):
        tupleList.append(tuple(kanji[i],english[i]))
    
    return tupleList


def pick_questions(questionsList):
    test = []
    while(len(test) <= 5):
        question = questionList[randrange(0,15)]
        #Check if the question already exists in the test
        if question not in test:
            test.append(question)


def ask_question(question: tuple):
    print("\n\n")
    answer = input("What is the meaning of the character", question[0], "in english?")

    if(answer == question[1]):
        print("\n\nCorrect! Good job")
        return 1
    else:
        print("\n\nIncorrect! the answer is", question[1])
        return 0


##########################################
# MAIN PROGRAM:
##########################################
def main():
    sentinel = True
    kanji = ["一","二","三","水","火","木","日","円","学","時","日本","東京","拉麺","先生","大学"]
    english = ["one","two","three","water","fire","tree","sun","yen","study","time","japan","tokyo","ramen","sensei","college"]
    questionsList = create_tuple(kanji, english)

    Print("Welcome to Kanji Quiz!\n\n")
    while(sentinel):

        play = input("Start a new game? (y/n): ").lower()

        while(play != 'y' or play != 'n'):
            play = input("Invalid Entry: Please enter (y/n): ")
        
            if(play == 'y'):
                correct = 0
                quiz = pick_questions(questionsList)

                for i in range(4):
                    correct += ask_question(quiz[i])

                print("Final Score:", correct + "/5")
            
            else:
                sentinel = False
        

    print("\n\nprogram ended.")

main()