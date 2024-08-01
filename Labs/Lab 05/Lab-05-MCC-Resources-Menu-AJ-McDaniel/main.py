'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" This program presents user with a menu of services and allows them to select one for additional information.
"""

##### CONSTANTS #####
# Do not change these! They are needed to produce the exact output expected.
LANGUAGE_LAB = "\nDid you know that MiraCosta has a Language Lab where you could schedule a one-on-one language coaching appointments through Zoom? \n\nCheck out their page: https://www.miracosta.edu/academics/degree-and-certificate-programs/languages-communication-and-humanities/international-languages/language-resource-center.html "
MLC="\nMLC is a great resource if you have questions regarding math topics! You can drop in for an appointment or schedule one at your convenience. \nMore information about the center is found here: https://www.miracosta.edu/student-services/math-learning-center/index.html"
STEM="\nIf you have questions concerning courses in Biology, Biotechnology, Chemistry, Computer Science, Physics, Astronomy, Oceanography, Earth Science, Geology, Horticulture, and Physical Science, don't be shy and go to:\nhttps://www.miracosta.edu/student-services/stem/index.html "
FOOD_PANTRY="\nExperiencing food insecurity? No problem, Food Pantry at MiraCosta College has your back! Food Pantry provides food assistance and referrals to students experiencing hunger\nhttps://www.miracosta.edu/student-services/care/food-pantry.html "
HEALTH_SERVICES="\nWe have amazing Student Health Services that are now open on campus! They offer a variety of health support for MiraCosta students including telehealth and teletherapy appointments. You can make an appointment here \nhttps://www.miracosta.edu/student-services/health-services/index.html"
MENTAL_HEALTH_SERVICES="\nFeeling anxious and/or stressed? MiraCosta Health Services offer Mental Health counseling. Free and confidential telehealth Counseling and Mental Health Services are available via Zoom or Phone to currently enrolled student. Simply follow the link \nhttps://www.miracosta.edu/student-services/health-services/counseling-and-mental-health-services.html"

main_options = [1,2,3]
options = ['a','b','c']
  
##### MAIN PROGRAM #####
def main():
    choice = 0
    sentinel = True

    
    #Main greeting
    print("\n***Welcome to MiraCosta College Student Resources*** \n")
    print("As you may already know we offer many services for our students.\n")

    
    while sentinel:
    
        #Display Menu
        print((str.format(f"""{main_options[0]}. Academic Support 
{main_options[1]}. Campus Services 
{main_options[2]}. Exit """)))
    
        choice = int(input("\nEnter your choice from the above options : "))
    
        
        #Data Validation
        while choice not in main_options:
            choice = int(input("\nError: Please enter a valid selection.\n"))

        
        #If one of the suboptions choice are selected
        if choice in [1, 2]:
            
            #1. Run correct suboptions menu
            if choice == 1:
                academic_support()
            else:
                campus_services()

            #2. Return to main menu
            input("Press enter to return to main menu. \n")

                
        #Else they chose option #3 - Exit        
        else:
            sentinel = False    




#Display suboptions of the Academic Support choice:
def academic_support():
    choice = ''
    
    #Display Menu
    print(str.format(f"""\n{options[0]})Language lab
{options[1]})Math Learning Center
{options[2]})STEM Learning Center"""))

    
    #Enter Selection
    choice = input("\nChoose from the options above : ").lower()

    
    #Data Validation
    while choice not in options:
        choice = input("Error: Please enter a valid selection.").lower()

    
    #Display Results
    if choice == options[0]:
        print(LANGUAGE_LAB + "\n")
    elif choice == options[1]:
        print(MLC + "\n")
    else:
        print(STEM + "\n")




#Display suboptions of the Campus Services choice:
def campus_services():

    #Display Menu
    print(str.format(f"""\n{options[0]})Food Pantry
{options[1]})Health Services
{options[2]})Mental Health Services"""))

    
    #Enter Selection
    choice = input("\nChoose from the options above : ").lower()

    
    #Data validation
    while choice not in options:
        choice = input("Error: Please enter a valid selection.\n").lower()

    
    #Display Results
    if choice == options[0]:
        print(FOOD_PANTRY + "\n")
    elif choice == options[1]:
        print(HEALTH_SERVICES + "\n")
    else:
        print(MENTAL_HEALTH_SERVICES + "\n")




main()
print("\nHappy studying, bye!!!")