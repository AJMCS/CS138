'''
DEVELOPER: AJ McDaniel
COLLABORATORS: None
DATE: 8/3/2024
'''

"""This program calculates how much plastic bottle waste you make.

I didn't have much time to be very original and "inspired" for this UD so I just made a very practical program that has real world benefit to people who use it.
It is much better to use reusable cups for everyday consumption and looking at how much plastic you use on a daily basis can help reduce unnecessary waste.
"""

def calculate_plastic_saved(bottles_per_day):
    days_in_year = 365
    return bottles_per_day * days_in_year

def main():
    print("Welcome to the Plastic Bottle Reduction Calculator!")
    print("This program will help you see the impact of reducing the amount of plastic bottles you use.")

    # Input with error checking (repetition structure)
    while True:

        bottles_per_day = int(input("How many plastic water bottles do you use per day on average? "))

        while bottles_per_day < 0:
            bottles_per_day = int(input("Please enter a non-negative number."))   
        break

    bottles_per_year = calculate_plastic_saved(bottles_per_day)

    print(f"\nIf you use {bottles_per_day:.1f} bottles per day, that's about {bottles_per_year:.0f} bottles per year!")

    # Decision structure
    if bottles_per_year > 365:
        print("That's more than one bottle per day on average.")
    elif bottles_per_year > 0:
        print("Good job keeping it under one bottle per day, but there's still room for improvement!")
    else:
        print("Fantastic! You're not using any disposable water bottles.")

    # String manipulation
    reduction_goal = input("\nEnter a reduction goal (example: '10' for 10%): ").lower()

    if "%" in reduction_goal:
        percentage = float(reduction_goal.strip("%")) / 100
        reduced_bottles = bottles_per_year * (1 - percentage)
    else:
        print("Invalid reduction goal. Instead, lets see what a 10% reduction looks like.")
        reduced_bottles = bottles_per_year * 0.9

    bottles_saved = bottles_per_year - reduced_bottles

    print(f"\nIf you reduce your consumption by {reduction_goal}, you would save approximately {bottles_saved} bottles per year!")
    print("Remember, using a reusable water bottle is even better for the environment!")

if __name__ == "__main__":
    main()