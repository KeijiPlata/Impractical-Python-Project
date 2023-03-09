"""
This project generates funny sidekick names
"""

# import the packages needed
import sys
import random

# firstname inside of a tuple
firstName = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie­Weenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chewy', 'Chigger Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', 'Lunch Money',
        'Mergatroid', '"Mr Peabody"', 'Oil­Can', 'Oinks', 'Old Scratch',
        'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
        'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
        "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
        'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
        'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
        "Winston 'Jazz Hands'", 'Worms')

# This code split the first name and get the last element and store in middle
middleName = []
newfirstName = []
for character in firstName:
    if " " in character:
        # this code split the word in space (" ", 1) means to split when see
        # space. The positive 1 is number of split you want 
        # [-1] means only get the last element of that split
        middleName.append(character.rsplit(" ", 1)[-1])

        # get the first element
        newfirstName.append(character.rsplit(" ", 1)[0])

# lastname inside of a tuple
lastName = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley­Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar­Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

def main_loop():
    """ The main loop for the program """
    print("Welcome to the silly name Generator!")
    while True:
        print("Your name will be:")
        pick_name()
        message = "\nDo you want to try again? Press Enter else q to quit: "
        try_again = input(message)

        # if user type q, terminate the program
        if try_again.lower() == "q":
            print("Thank you for using the system!")
            break
def pick_name():
    """Pick the name"""
    first = random.choice(newfirstName)
    middle = random.choice(middleName)
    last = random.choice(lastName)

    # print the name
    # error message doen't work on my terminal
    print(f"{first} {middle} {last}", file=sys.stderr)

if __name__ == "__main__":
    main_loop()
