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

# Check whether the amount of hot dogs needed is evenly divisible by the number of dogs in a package
# if yes, floor divide by the number of hotdogs in the package
if dogs_needed % DOG_PACKAGE == 0:
    minimum_dogs = dogs_needed // DOG_PACKAGE

# If not, floor divide by the number in a package of hot dogs and add 1
else:
    minimum_dogs = (dogs_needed // DOG_PACKAGE) + 1

# Check whether the amount of buns needed is evenly divisible by the number of buns in a packages
# If yes, floor divide by the number of buns in a package
if dogs_needed % BUN_PACKAGE == 0:
    minimum_buns = dogs_needed // BUN_PACKAGE

# If not, floor divide by the number of buns in a package and add 1
else:
    minimum_buns = (dogs_needed // BUN_PACKAGE) + 1

# Calculate the total number of hot dogs
total_dogs = minimum_dogs * DOG_PACKAGE

# Calculate the total number of Buns
total_buns = minimum_buns * BUN_PACKAGE

# Calculate how many hot dogs and buns will be left over.
leftover_dogs = total_dogs - dogs_needed
leftover_buns = total_buns - dogs_needed

# Display the minimum number of hot dog packages, bun packages, and how many of each will be left leftover
print(f'Minimum packages of hot dogs needed: {minimum_dogs}')
print(f'Minimum packages of buns needed: {minimum_buns}')
print(f'Hot dogs left over: {leftover_dogs}')
print(f'Buns left over: {leftover_buns}')
