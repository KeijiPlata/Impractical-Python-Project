"""
This project convert the word into a piglatin word
The program only accepts a word
"""

def main_loop():
    """The main loop of the program"""
    # declaration of variable
    vowels = 'aeiou'
    flag = True

    print("Hi this is the pig latin word converter!")
    while flag:
        userinput = input("Enter the word to convert: ")
        print(f"The conversion of the word is: {check_word(userinput, vowels)}")
        flag = end_loop(flag)

def check_word(userinput, vowels):
    """check if the firstword is in consonant or vowels"""
    if userinput[0] in vowels:
        word = userinput + "way"
    else:
        word = userinput[1:] + userinput[0] + "ay"
    return word

def end_loop(flag):
    """check if the user want to try again or not"""
    message = "Do you want to try again?" + \
                " press enter to continue, q to quit: "
    validation = input(message)
    if validation == "q":
        print("Thank you for using the program")
        flag = False
    return flag

if __name__ == "__main__":
    main_loop()
