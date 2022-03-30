# Python Program to check if first number divides second number evenly
import math


# Approach One: Using modulus operator function
def evenlyDivisible(num_1, num_2):
    if num_1 % num_2 == 0:
        return True
    else:
        return False


result = evenlyDivisible(70, 7)
print("Result is", result)


def evelyDivideUsingLib(val_1, val_2):
    if math.remainder(val_1, val_2) == 0:
        return True
    else:
        return False


res = evelyDivideUsingLib(25, 4)
print("Result is", res)