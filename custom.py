#------------------------------
# MY CUSTOM MODULE
#------------------------------

# Creating my own custom module full of useful things ...
# Storing things here keeps code clean (within the app)

#----- IMPORT MODULES -----

# Random module for 'play_silo' function
import random

#------------------------------
# SILO GAME FUNCTION
#------------------------------

# app.py has a variable 'play' that will be passed here
# We will then pass the outcome back to app.py

def play_silo(play):
    while play == "yes" or play == "Yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        if dice1 == dice2 and dice2 == dice3:
            print("You Got Trips:")
            print(dice1, dice2, dice3)
            break
        if dice1 == dice2 or dice3 == dice1 or dice3 == dice2:
            print("You're score:")
            print(dice1, dice2, dice3)
            break
        # Note, could expand upon this to include 1, 2, 3 instant loss and 4, 5, 6, instant win logic

#------------------------------
# OTHER USEFUL THINGS ...
#------------------------------

#----- KM CONVERTOR -----
# kilometers = 0

def km_to_miles():
    print("Convert Kilometers to Miles:")
    kilometers = int(input("How Many Kilometers: "))
    miles = kilometers * 0.621371
    return ("That's", miles, "miles!\n")


# feet_in_mile = 5280
# meters_in_kilometer = 1000

#----- FAMILY LIST -----

# Use for ....
family = ["James", "John", "Jamie", "Haru", "Brendan", "Jim"]


#----- GET FILE EXTENSION -----

# This is from a tutorial ... Haven't used it ...
# Give it a fileneme, It will tell you the extension
def get_file_extension(filename):
    return filename[filename.index(".") + 1:]

