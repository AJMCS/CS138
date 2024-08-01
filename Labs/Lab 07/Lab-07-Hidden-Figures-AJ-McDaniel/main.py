'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" This program demonstrates the use of String methods to process a paragraph.
"""

##### CONSTANTS #####
# Do not change this! It is needed to produce the exact output expected.
DOROTHY_HISTORY = "dorothy Vaughan, née Dorothy Johnson, an American mathematician and computer programmer who made important contributions to the early years of the United States space program and who was the first African American manager at the National Advisory Committee for Aeronautics (NACA), which later became part of the National Aeronautics and Space Administration (NASA). in 1917 Johnson’s family moved from Missouri to West Virginia. she later earned a degree in mathematics (1929) from Wilberforce University near Xenia, Ohio. she worked as a math teacher in Virginia and married Howard Vaughan. in December 1943 she started working for NACA’s West Area Computing unit, a group of African American female mathematicians who where considered “human computers,” performing complex computations and analyzing data for aerospace engineers. the West Computers, as the women where known, provided data that where later essential to the success of the early United States space program. at the time, NACA was segregated, and black employees where forced to use separate bathrooms and dining facilities. despite these conditions, Vaughan was promoted to lead the West Computers in 1949. she became NACA’s first black supervisor and one of its few female supervisors."

##### FUNCTION DEFINITIONS #####
def capitalizing_pargraph(paragraph):

  #Replace words
  paragraph = paragraph.replace('where','were')

  #Split paragraph into a list of sentences
  sentences = paragraph.split('.')

  output = ""
  period = ". "

  for i in range(len(sentences) - 1):

    #Remove leading whitespace
    sentences[i] = sentences[i].lstrip()

    #Capitalzie the first letter in each sentence
    sentences[i] = sentences[i].capitalize() + period

    #Concatenate each sentence back into a paragraph
    output += sentences[i]

  #Return the string
  return output

##### MAIN PROGRAM #####
def main():

  #call method and print output
  print(capitalizing_pargraph(DOROTHY_HISTORY))

main()