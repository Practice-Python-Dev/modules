#--------------------
#IMPORT RANDOM
#--------------------

import random

#RANDINT
# randint()
# Generates a random number - accepts two parameters (start, stop)
number_a = random.randint(1, 100)
print('Random from 1 to 100:')
print(number_a, '\n')



#RANDOM
# random.random()
# Use multiplication for a large number - Note, starts from zero and returns a float
# Example: Show it in a loop
number_b = random.random() *1000
print('Random from 1 to 1000:')
if (number_b <= 1000) and (number_b >= 0):
    print(str(number_b), 'is betweeen 1 and 1000\n')
else:
    print('There was an error\n')



#CHOICE
# random.choice()
# Grabs a random index within a list
my_list = [2, 109, 55, 'your momma', 'oh snap', 'he went there', 25, 44, 'prince', 101]
print('Random List Item:')
print(random.choice(my_list), '\n')



#SHUFFLE
# random.shuffle()
# Function randomly shuffles elements in a list - Permanent change (!)
new_list = list(range(11))
print('New List:')
print(new_list, '\n')
# Need to invoke outside print statement
# We are changing the list permanently
random.shuffle(new_list)
print('Shuffled List Permanently Changed:')
print(new_list)
print(new_list, '\n')



#SAMPLE
# random.sample(population, length)
# Returns a new list containing elements from the population (list), while leaving the original population unchanged
newer_list = random.sample(new_list, len(new_list))
print('Creates a Shuffled Copy:')
print(newer_list)
print(newer_list, '\n')
print('Note, the list we based this off is still the same:')
print(new_list, '\n')



#RANDRANGE
# random.randrange(start, stop, step)
# Generate a randomly selected element from the range
# Use step to only select divisibles of five ...
print('Random Nickels in 100:')
for i in range(3):
    print(random.randrange(0, 101, 5))
print('\n')
# Note, we used end='' to stop automatically printing on a new line



#SHUFFLE TUPLES
# Strings and tuples are immutable, so random.shuffle will raise an error
# Create a tuple to copy ...
my_tuple = tuple(range(10))
print('Here\'s a Tuple:')
print(my_tuple)
# Copy a shuffled version of the tuple into a new object
# Note, we're not changing (mutating) a tuple, we're creating a new one using info from the old one
shuffled_tuple = tuple(random.sample(my_tuple, len(my_tuple)))
print('Here\'s a Copy That\'s Shuffled:')
print(shuffled_tuple, '\n')



#SHUFFLE STRINGS
# Strings and tuples are immutable, so random.shuffle will raise an error
# For strings use the join() method to concatenate to a single string again ...
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('Here\'s a String:')
print(alphabet, '\n')
# Note, the join method takes takes iterable objects capable of returning it's members one at a time (lists, tuples, strings, dictionaries, sets, etc.)
# Syntax = string_name.join(iterable)
    # Here's a simpler example of join()
        # list1 = ['1', '2', '3', '4']
        # seperate = '-'
        # outcome = separate.join(list1)
    # This will  iterate through each item and concatenate ...
        # ouctome = 1-2-3-4
# Back to the alphabet. We're taking an empty string '' and .joining it with a random.sample of the alphabet
# Note, we need both (population, length) in random.sample()
shuffle_and_join = ''.join(random.sample(alphabet, len(alphabet)))
print(shuffle_and_join, '\n')



#PUZZLE - Coin Flips
# Use 'import itertools' and have some fun
import itertools
# Create a dictionary
    # The keys will be the sides of a coin
    # The value pairs will be the times occured
outcomes = {'heads': 0,
            'tails': 0,}
# This is our counter (for key-value pairs)
coin_sides = list(outcomes)
# Now let's iterate (flip) a million times
# Our counter increases the value-pair for the winning key
for i in range(1000000):
    # Each iteration (flip) adds to the respective key-value pair counter
    # coin_sides holds just the keys
        # coinsides = ['heads', 'tails']
    # dictionary[random.choice(heads, tails)] += 1
    # Looks something like this --> coin_sides = [500000, 500000]
    outcomes[random.choice(coin_sides)] += 1
# And print to the screen
print('One Million Coin Flips:')
print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'], '\n')
print(coin_sides)
# Note, this likely isn't the fastest way to do this ...
