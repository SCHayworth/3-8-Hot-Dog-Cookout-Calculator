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
    DOG_PACKAGE = 10
    BUN_PACKAGE = 8
    Prompt user for the number of people attending
    Prompt user for the number of hot dogs for each person
    Calculate the total number of hot dogs and buns needed
        dogs needed = people attending * dogs per person
    IF dogs needed % DOG_PACKAGE = 0
        minimum dog packages = dogs needed / DOG_PACKAGE
    ELSE minimum dog packages = (dogs needed // DOG_PACKAGE) + 1
    IF dogs needed % BUN_PACKAGE = 0
        minimum bun packages = dogs needed / BUN_PACKAGE
    ELSE minimum bun packages = (dogs needed // BUN_PACKAGE) + 1
    Calculate how many hot dogs there are in total
        total dogs = minimum dog packages * DOG_PACKAGE
    Calculate how many hot dogs will be left over
        leftover dogs = total dogs - dogs needed
    Calculate how many buns there are in total
        total buns = minimum bun packages * BUN_PACKAGE
    Calculate how many buns will be left over
        leftover buns = total buns - dogs needed
    print minimum dog packages
    print minimum bun packages
    print leftover dogs
    print leftover buns
