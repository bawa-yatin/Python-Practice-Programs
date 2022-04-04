def animalLegs(chickens, cows, pigs):
    chickenLegs = chickens * 2
    cowLegs = cows * 4
    pigLegs = pigs * 4
    total_legs = chickenLegs + cowLegs + pigLegs
    return total_legs


total_1 = animalLegs(2, 4, 4)
total_2 = animalLegs(5, 3, 1)
print("Total number of legs of all animals are", total_1)
print("Total number of legs of all animals are", total_2)
