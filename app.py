#------------------------------
# IMPORT MODULES & USE THEM
#------------------------------

# Importing functionality from external python files is a core concept
# Write something once in a module, then import it into any files it is useful

# This file 'app.py' draws on the other files (modules) in the repository

#------------------------------
# CUSTOM MODULE (BY ME)
#------------------------------

import custom

#------ PLAY SILO -----


# Ask the user if they want to play silo
play = input("Do you want to play Silo? ")

# Pass 'play' parameter to our function, Function runs, Passes back the result, Then we print
# Syntax = module.function(parameter)
print(custom.play_silo(play))

#------ CONVERT KILOMETERS TO MILES -----


########## BUGGGGGGSSSS ##############
# Call the function
custom.km_to_miles()


#------------------------------
# RANDOM MODULE
#------------------------------