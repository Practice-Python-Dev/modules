#------------------------------
# IMPORT MODULES & USE THEM
#------------------------------

# Importing functionality from external python files is a core concept
# Write something once in a module, then import it into any files it is useful

# This file 'app.py' draws on the other files (modules) in the repository

#------ CUSTOM MODULE (BY ME) -----

import custom

#------------------------------
# PLAY SILO GAME 
#------------------------------

# Ask the user if they want to play silo
    # Pass 'play' parameter to our function
    # Function runs, Passes back the result
    # Print it - Syntax = module.function(parameter)

play = input("Want to Play Silo? ")
print(custom.play_silo(play))

#------------------------------
# KILOMETERS TO MILES
#------------------------------

# Ask the user for kilometers to convert
    # Pass 'kilometers', run the function
    # Pass back results, print ...

# kilometers = input("Convert Kilometers to Miles: ")


