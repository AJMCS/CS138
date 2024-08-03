'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" File input and output, exception handling
"""
##### IMPORTS #####


##### FUNCTION DEFINITIONS #####
def encypt_or_decrypt():
    choice = input("Encrypt or Decrypt? ").lower()
    
    while choice != "encrypt" and choice != "decrypt":
        choice = input("Invalid Entry: Please enter either encrypt or decrypt: ").lower()

    return choice


def read_file():
    in_file = input("Please enter the name of a text file you wish to be read into the program (exclude the extension in your response): ")
    
    try:
        in_file = open(in_file + ".txt", 'r')
        data = in_file.read()
        in_file.close()
    except IOError as err:
        print(err)
        data = input("Enter data manually: ")

    return data


def write_file(data):
    out_file = input("Please enter the name of a text file you wish to be write to the program (exclude the extension in your response): ")

    choice = input("Enter '1' if you would like to rewrite to the file, otherwise enter nothing to append: ")
    
    out_file = open(out_file + ".txt", "w") if choice else open(out_file + ".txt", "a")
    out_file.write(data)
    out_file.close()

##### MAIN PROGRAM #####
def main():
    data = ""
    result = ""
    choice = encypt_or_decrypt()
    data = read_file()

    if choice == 'encrypt':
        key = int(input("Enter the shift amount for encryption: "))
        for i in range(len(data)):
            result += (chr(ord(data[i]) + key))
    else:
        key = int(input("Enter the shift amount for decryption: "))
        for i in range(len(data)):
            result += (chr(ord(data[i]) - key))

    write_file(result)
main()