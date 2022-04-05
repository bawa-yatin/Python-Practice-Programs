# Python Program to check if first number divides second number evenly
import math


# Approach One: Using modulus operator function
def evenly_divisible(num_1, num_2):
    if num_1 % num_2 == 0:
        return True
    else:
        return False


result = evenly_divisible(70, 7)
print("Result is", result)


def evely_divide_using_lib(val_1, val_2):
    if math.remainder(val_1, val_2) == 0:
        return True
    else:
        return False


res = evely_divide_using_lib(25, 4)
print("Result is", res)