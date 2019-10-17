# Program 3-8 Hot Dog Cookout Calculator
# Shaun Hayworth
# CIS 2
# 10-17-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/3-8-Hot-Dog-Cookout-Calculator

# Program calculates the minimum number of packages of hot dogs and buns required for a cookout, given a number of people
# attending a cookout, and the number of hot dogs per person.

# Initialize DOG_PACKAGE constant.
# Change this if buying a different number of hot dogs per package
DOG_PACKAGE = 10

# Initialize BUN_PACKAGE constant
# Change this if buying a different number of buns per package
BUN_PACKAGE = 8

# Prompt user for the number of people attending the cookout
attending = int(input('Number of people attending the cookout: '))

# Prompt user for the number of hot dogs per person
dogs_per_person = int(input('Number of hot dogs per person: '))

# Calculate the total hot dogs needed
dogs_needed = attending * dogs_per_person

# Check whether the amount of hot dogs needed is evenly divisible by 10
if dogs_needed % DOG_PACKAGE = 0:

    # if yes, divide by the number of hotdogs in the package
    minimum_dogs = dogs_needed / DOG_PACKAGE
else:

    # If not, floor divide by the number of packages and add 1
    minimum_dogs = (dogs_needed // DOG_PACKAGE) + 1
