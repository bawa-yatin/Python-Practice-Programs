# Python Program to check if first number divides second number evenly
import math


# Approach One: Using modulus operator
def evenly_divisible(num_1, num_2):
    if num_1 % num_2 == 0:
        return True
    else:
        return False


result = evenly_divisible(70, 7)  # Variable holding the response returned from the
# function "evenly_divisible()"
print("Result is", result)


# Approach 2: Using math library: remainder()
def evely_divide_using_lib(val_1, val_2):
    if math.remainder(val_1, val_2) == 0:
        return True
    else:
        return False


res = evely_divide_using_lib(25, 4)  # Variable holding the response returned from the
# function "evely_divide_using_lib()"
print("Result is", res)
