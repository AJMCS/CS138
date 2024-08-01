"""This program will read a string of military time from a list and convert each digit into its corresponding binary value. It'll then display this time to the console where 1s and 0s are denoted by "*" and "." respectively. Each column is a single digit represented in binary where the place values are read from bottom to top.

This program will read a string of military time from a list and convert each digit into its corresponding binary value. It'll then display this time to the console where 1s and 0s are denoted by "*" and "." respectively. Each column represents a single binary digit. Since it's military time, there will be four columns. each row of the colum represents a binary place value, where the bottom row is the 1s place up to the top of row which represents the 8ths place. 

Place values of each column:
(*bottom* 1 -> 2 -> 4 -> 8 *top*)
"""

##########################################
# IMPORTS:
#   N/A
##########################################
#None


##########################################
# FUNCTIONS:
##########################################
def digit_to_binary(digit):
  """Takes a one digit time as input and stores its corresponding binary value in a list and returns the list."""
  list = []

  binary_string = bin(digit)
  binary_string = binary_string [2:].rjust(4, '0') #[2:] removes first two characters of the binary string. These first two characters are notation denoting the number is writen in binary and not the number itself.
#rjust() fills left side  number with '0' as needed. 
#ex: input 1(decimal) becomes output 1(binary) we want to represent this with four digits so we add three '0's to the left so it becomes '0001'

  for i in range (0,len(binary_string)): #loops through list
    if(binary_string[i] == '0'): 
      list.append(".") # all 0s -> "."
    else:
      list.append("*") # all 1s -> "*"

  return list



def print_to_console(list):

  for i in range(0, 4):
    string = ""
    for j in range(0, 4):
      string = string + " " + list[j][i]

    print(string)


##########################################
# MAIN PROGRAM:
##########################################
def main():
  main_list = []
  time = input("enter a value in military time\n")
  
  while time != "":
    for i in range(0,4):
      digit = int(time[i])
      main_list.append(digit_to_binary(digit))
  
    #print(time.strip())
    print_to_console(main_list)
    print()
    main_list.clear()

    time = input("Enter a new value in military time\n(enter nothing to quit)\n")

  if time == "":
    print("\n\nprogram ended.")

main()