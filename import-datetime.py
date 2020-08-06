#--------------------
# DATETIME MODULE
#--------------------

#The datetime module supplies classes for manipulating dates and times
#Date and time objects are categorized as either "aware" (unambiguous) or "naive"
#Documentation here: https://docs.python.org/3/library/datetime.html
#Import datetime module

import datetime

#--------------------
#DATE OUTPUT
#--------------------

#Create an object that points to raw datetime - classmethod.datetime.now()
my_time = datetime.datetime.now()
print("Local Machine Time:")
print(my_time, "\n")

#Extract the day of the week - Note, see python strftime to understand '%A' - https://strftime.org/
print("Today is", my_time.strftime('%A'))
#Extract the year ...
print('The year is', str(my_time.year))
#Print the hour
print("It's", my_time.hour, "o'clock", "\n")

#--------------------
#STORE DATES
#--------------------

#Datetime() class constructor requires three parameters (year, month, day)
my_birth = datetime.datetime(1983, 10, 31)
print("I was born on:")
print(my_birth, '\n')

#Replace a value of a stored date (not mutating the original)
my_birth = my_birth.replace(year=1984)
print("My mistake. Actually born on:")
print(my_birth, "\n")

#--------------------
#STRFTIME METHOD
#--------------------

#Method for formatting date objects into readable strings
#strftime() takes one parameter (format) to specify the format of the returned string
#There are a ton of format codes. Check the documentation, or here: https://strftime.org/

#Display the name of the month
print("What month is it:")
print(my_time.strftime("%B"), "\n")

#Display the time with am/pm
print("Morning or night:")
print("It's", my_time.strftime("%I:%p"), "\n")

#Display your timezone:
    #Note we need 'pytz' to do this
    #We need to install it via pip (we need pip too)
    #Run --> pip install pytz tzlocal

########################################################################
#HAVING ISSUES INSTALLING PIP
#WILL COME TO THIS LATER ...
# from pytz import reference
# localtime = reference.LocalTimezone()
# print(localtime.tzname(now))

#https://www.tutorialspoint.com/How-do-I-print-a-Python-datetime-in-the-local-timezone
#https://stackoverflow.com/questions/31299580/python-print-the-time-zone-from-strftime#

# print("Your Timezone:")
# print(now.strftime("%Z"))

########################################################################

#--------------------
#PUZZLE
#--------------------

#Print days left till your birthday
# https://docs.python.org/3/library/datetime.html
# >>> import time
# >>> from datetime import date
# >>> today = date.today()
# >>> today
# datetime.date(2007, 12, 5)
# >>> today == date.fromtimestamp(time.time())
# True
# >>> my_birthday = date(today.year, 6, 24)
# >>> if my_birthday < today:
# ...     my_birthday = my_birthday.replace(year=today.year + 1)
# >>> my_birthday
# datetime.date(2008, 6, 24)
# >>> time_to_birthday = abs(my_birthday - today)
# >>> time_to_birthday.days
# 202








#classmethod.date.today()
# raw_date = datetime.date.today()
# print('Local Date:')
# print(raw_date, '\n')




#Padding on bottom ...
print('\n' *1)
