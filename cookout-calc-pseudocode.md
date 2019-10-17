# Scope
Assume hot dogs come in packages of 10, and the hot dog buns come in package of 8. Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the number hot dogs each person will be given. The program should display the following details:

* The minimum number of package of hot dogs required
* The minimum number of package of hot dog buns required
* The number of hot dogs that will be left over
* The number of hot dog buns that will be left over

## Sample Run 1
    Enter the number of people attending the cookout:  33
    Enter the number of hot dogs for each person:  3
    Minimum packages of hot dogs needed: 10
    Minimum packages of hot dog buns needed: 13
    Hot dogs left over: 1
    Hot dog buns left over: 5
    
## Sample Run 2
    Number of people attending the cookout: 20
    Number of hot dogs per person: 2
    Minimum packages of hot dogs needed: 4
    Minimum packages of buns needed: 5
    Hot dogs left over: 0
    Buns left over: 0
    
# Pseudocode
    Prompt user for the number of people attending
    Prompt user for the number of hot dogs allocated to each person
    Calculate the total number of hot dogs needed
      dogs needed = people attending * dogs allocated
    Calculate the minimum number of hot dog packages required
      dog packages required = dogs needed / 10
    Calculate the amount of leftover hot dogs
      leftover dogs = dogs needed % 10
    Calculate the total number of bun packages required
      bun packages required = dogs needed / 8
    Calculate the leftover buns
      leftover buns = dogs needed % 8
    Print the minimum number of hot dog packages needed
    Print the minimum number of bun packages needed
    Print the number of leftover hot dogs
    Print the number of leftover buns
    
