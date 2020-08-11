#------------------------------
# MY CUSTOM MODULES
#------------------------------

# Import random module for 'play_silo'
import random

#------------------------------
# PLAY SILO FUNCTION
#------------------------------

# app.py has a variable 'play' that will be passed here
# We will then pass the outcome back to app.py

def play_silo():
    # Define local variables
    play = input("Do you want to Play Silo? ")
    instant_win = [4, 5, 6]
    instant_loss = [1, 2, 3]

    # Roll if 'play' = "yes"
    while play == "yes" or play == "Yes" or play == "y" or play == "Y":

        # Roll the dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        outcome = [dice1, dice2, dice3]

        # Compare the 'outcome' to the 'instant win/loss' criteria
        compare_win  = all(elem in outcome for elem in instant_win)
        compare_loss = all(elem in outcome for elem in instant_loss)
        
        # Break at the end ...
        if compare_win:
            print("You got Silo!!!")
            outcome.sort()
            print(outcome)
            break
        # If 'compare_loss' = 'True'
        elif compare_loss:
            print("You crapped out:")
            outcome.sort()
            print(outcome)
            break
        # If trips ...
        elif dice1 == dice2 and dice2 == dice3:
            print("You Got Trips:")
            print(outcome)
            break
        # If doubles ...
        elif dice1 == dice2 or dice3 == dice1 or dice3 == dice2:
            outcome.sort()
            print("Your score is:", outcome)
            break
        # If no score keep rolling ...
        else:
            print("You rolled", outcome)
            play = input("Keep playing?")


#------------------------------
# OTHER USEFUL FUNCTIONS ...
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
