"""
This program creates a text based bar chart like to determine
how many character in a word occurs in a user input
"""
# This import is used to print well formatted json or dictionary
import pprint

def main_loop():
    """The main loop for the program"""
    # declaration of alphabet to compare later
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # declare a empty dictionary
    barchart = {}
    flag = True

    while flag:
        text=input("Enter the text you want: ")
        check_characters(text, barchart, alphabet)
        pprint.pprint(barchart, width=110)
        flag, barchart = loop_break(flag, barchart)

def check_characters(text, barchart, alphabet):
    """Checks the character in the text and store it in dictionary"""
    for character in text:
        character = character.lower()
        if character in alphabet:
            barchart.setdefault(character, [])
            barchart[character].append(character)

def loop_break(flag, barchart):
    """Asks the user if he/she wants to continue"""
    message = "Do you want to try again? Press enter if yes, q to quit: "
    validation = input(message)

    if validation == 'q':
        print("Thank you for using the program")
        flag = False
    else:
        # clear the dictionary to reset the program
        barchart.clear()

    return flag, barchart

if __name__ == '__main__':
    main_loop()
