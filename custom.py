#------------------------------
# MY CUSTOM MODULE
#------------------------------

# Creating my own custom module full of useful things ...
# Storing things here keeps code clean (within the app)

# Import random module for 'play_silo' function
import random

#------------------------------
# PLAY SILO FUNCTION
#------------------------------

# app.py has a variable 'play' that will be passed here
# We will then pass the outcome back to app.py

def play_silo(play):
    # Save outcomes in a list to manipulate later ...
    simulate = 0
    if play == "yes" or play == "Yes":
        while simulate <= 100:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)
            outcomes = [dice1, dice2, dice3]
            # Instant win
            instant_win = [4, 5, 6]
            compare_win  = all(elem in outcomes for elem in instant_win)
            # Instant loss
            instant_loss = [1, 2, 3]
            compare_loss = all(elem in outcomes for elem in instant_loss)
            simulate += 1
            if compare_win: 
                print("You got Silo!!!")
                outcomes.sort()
                print(outcomes, "\n----------")
                # break
            elif compare_loss:
                print("You crapped out:")
                outcomes.sort()
                print(outcomes, "\n----------")
                # break
            elif dice1 == dice2 and dice2 == dice3:
                print("You Got Trips:")
                print(outcomes, "\n----------")
                # break
            elif dice1 == dice2 or dice3 == dice1 or dice3 == dice2:
                print("You're score:")
                print(outcomes, "\n----------")
                # break
        print()
    # return dice1, dice2, dice3
    # return print(dice1, dice2, dice3)
        # Note, could expand upon this to include 1, 2, 3 instant loss and 4, 5, 6, instant win logic

#------------------------------
# OTHER USEFUL THINGS ...
#------------------------------

# ----- KM CONVERTOR -----

# Reference Only:
    # feet_in_mile = 5280
    # meters_in_kilometer = 1000

def km_to_miles(kilometers):
    miles = int(kilometers) * 0.621371
    return (kilometers, "is miles", miles)

# ----- FAMILY LIST -----

# Use for ....
family = ["James", "John", "Jamie", "Haru", "Brendan", "Jim"]


# ----- GET FILE EXTENSION -----

# This is from a tutorial ... Haven't used it ...
# Give it a fileneme, It will tell you the extension
def get_file_extension(filename):
    return filename[filename.index(".") + 1:]

