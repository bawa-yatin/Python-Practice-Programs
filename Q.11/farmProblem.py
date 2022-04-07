
# The Farm Problem
# In this challenge, a farmer is asking you to tell him how many legs can be counted
# among all his animals. The farmer breeds three species:

# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs


# User-defined function to calculate the total number of legs of all animals
def animal_legs(chickens, cows, pigs):
    chickenLegs = chickens * 2  # variable for holding the total number of legs of all the chicken present
    cowLegs = cows * 4  # variable for holding the total number of legs of all the cows present
    pigLegs = pigs * 4  # variable for holding the total number of legs of all the pigs present
    total_legs = chickenLegs + cowLegs + pigLegs  # variable for holding the total number of legs of all animals
    return total_legs


total_1 = animal_legs(2, 4, 4)
total_2 = animal_legs(5, 3, 1)
print("Total number of legs of all animals are", total_1)
print("Total number of legs of all animals are", total_2)
