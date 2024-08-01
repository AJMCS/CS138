'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): none
'''
""" This program scales ingredients for a recipe.

TODO: Step 1 - Explain where you got the recipe from (Ex: aunt Jane, grandpa Mario, foodnetwork.com, etc.) and why you chose it. Also state what the original number of servings is.

For this lab, I will be using a recipe for making crepes. I got the recipe from https://www.allrecipes.com/recipe/16383/basic-crepes/ and the original number of servings is 4.
"""

#INPUT SECTION
#TODO: Step 2 - get user input for the number of servings they want to make.

num_of_servings = int(input("Please enter the number of servings: "))

#PROCESSING SECTION 
#TODO: Step 3 - calculate your scaling ratio

num_of_eggs = (1/2) * num_of_servings
cups_of_milk = (1/8) * num_of_servings
cups_of_water = (1/8) * num_of_servings
tsp_of_salt = (1/16) * num_of_servings
cups_of_flour = (1/4) * num_of_servings
tbsp_of_butter = (1/2) * num_of_servings

#OUTPUT SECTION
#TODO: Step 4 - output scaled ingredient list and recipe directions

print(f'Ingredients List for {num_of_servings} servings\n')
print(f'{num_of_eggs:.2f} eggs\n{cups_of_milk:.2f} cups of milk\n{cups_of_water:.2f} cups of water\n{tsp_of_salt:.2f} TSP of salt\n{cups_of_flour:.2f} cups of flour\n{tbsp_of_butter:.2f} TBSP of butter\n\n')

print(f'Step 1\nWhisk eggs, milk, water, and salt together in a large mixing bowl; add flour and butter and whisk vigorously until smooth.\n\nStep 2\nHeat a lightly oiled griddle or frying pan over medium-high heat. Pour or scoop the batter onto the pan, using approximately 1/4 cup for each crêpe. Tilt the pan with a circular motion so that the batter coats the surface evenly.\n\nStep 3\nCook until the top of the crêpe is no longer wet and the bottom has turned light brown, 1 to 2 minutes. Run a spatula around the edge of the skillet to loosen the crêpe; flip and cook until the other side has turned light brown, about 1 minute more. Serve hot.')