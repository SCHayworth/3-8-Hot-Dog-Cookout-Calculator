# Program 3-8 Hot Dog Cookout Calculator
# Shaun Hayworth
# CIS 2
# 10-16-2019
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

# Calculate the minimum number of hot dog packages needed
dog_minimum = dogs_needed // DOG_PACKAGE

# Calculate the total amount of hot dogs on hand
total_dogs = dog_minimum * DOG_PACKAGE

# Calculate the leftover hot dogs
leftover_dogs = dogs_needed - total_dogs

# Calculate the minimum number of bun packages needed
bun_minimum = dogs_needed // BUN_PACKAGE

# Calculate the total number of buns on hand
total_buns = bun_minimum * BUN_PACKAGE

# Calculate the number of leftover buns
leftover_buns = dogs_needed - total_buns

# Display the minimum packages of hot dogs and buns needed, and how many of each will be left over
print(f'Minimum packages of hot dogs needed: {dog_minimum}')
print(f'Minimum npackages of buns needed: {bun_minimum}')
print(f'Hot dogs left over: {leftover_dogs}')
print(f'Buns left over: {leftover_buns}')
