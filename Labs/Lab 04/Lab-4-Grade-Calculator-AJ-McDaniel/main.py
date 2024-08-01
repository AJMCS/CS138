'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): none
'''
""" This program can be used to determine final course grade or to find the expected number of assignments for a given week of the semester.
"""
import math
##### FUNCTION DEFINITIONS #####
def determine_grade(uds, labs, eps):
  if(uds < 0 or labs < 0 or eps < 0):
    return "error"
  else:
    if(uds == 4 and labs >= 14 and eps >= 45):
      return "A"
    elif(uds >= 3 and labs >= 12 and eps >= 40):
      return "B"
    elif(uds >= 2 and labs >= 10 and eps >= 35):
      return "C"
    elif(uds >=1 and labs >= 8 and eps >= 30):
      return "D"
    else:
      return "F"


def progress_check_a(num_weeks_completed):
  num_UD = (num_weeks_completed - 1) // 4
  num_labs = math.floor((14/16) * num_weeks_completed)
  num_eps = math.floor((45/16) * num_weeks_completed)

  return num_UD, num_labs, num_eps


  
##### MAIN PROGRAM #####
def main():
  uds = int(input("Enter number of UDs: "))
  labs = int(input("Enter number of Labs: "))
  eps = int(input("Enter number of EPs: "))
  
  print("Determined grade is: " + determine_grade(uds, labs, eps) + "\n")

  num_weeks_completed = int(input("Enter number of weeks completed: "))

  num_uds, num_labs, num_eps = progress_check_a(num_weeks_completed)

  print(f"\nTo be on track for an A, after completing {num_weeks_completed} weeks of the semester you should have {num_uds} unit deliverables completed, {num_labs} labs completed, and earned {num_eps} engagement points.")

main()