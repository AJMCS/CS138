'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): none

This program implements the projectile formula to a function.

'''
#### CONSTANTS SECTION ####
# Step 1: Defining a constant global variable
ACCELERATION = -9.8


#### FUNCTIONS SECTION ####
# Step 2: Defining a function to find the time of the maximum height
# name the function calc_time_max_height
def calc_time_max_height(velocity):
  '''This function calculates at wha time the max height of the projectile was reached.'''
  result = -(velocity / ACCELERATION)
  return result


# Step 3: Defining a function to find the height of the maximum height
# name the function calc_max_height
def calc_max_height(velocity, initial_height, time):
  '''This function calculates the max height of the projectile'''
  result = (1.0/2.0)*ACCELERATION*(time**2) + velocity*time + initial_height
  return result


# Step 6: Combining two functions into one and returning two outputs
# name the function find_peak
def find_peak(velocity, initial_height):
  peak_height_time = calc_time_max_height(velocity)
  peak_height = calc_max_height(velocity, initial_height, peak_height_time)
  return peak_height, peak_height_time


#### MAIN PROGRAM ####
# Step 4: Using the calc_time_max_height to find the time of the maximum height
# passed values to a variable. Using the calc_max_height to find the maximum height and
# passed values to a variable.
max_height_time = calc_time_max_height(39.2)
max_height = calc_max_height(39.2,3,max_height_time)


# Step 5: Printing the results using calc_time_max_height and calc_max_height output.
print(f'The maximum height of the ball with velocity 39.2 m/s and initial velocity 3m is {max_height_time:.2f} sec, with maxim height {max_height:.2f} meters using the two functions.\n\n')


# Step 7: Using the find_peak to find the maximum height and time
# passed values to two different variables
peak_height, peak_time = find_peak(39.2, 3)


# Step 8: Printing the results using the find_peak output
print(f'The maximum height of the ball with velocity 39.2 m/s and initial velocity 3 m is {peak_time:.2f} sec, with maxim height {peak_height:.2f} meters using the two functions"')