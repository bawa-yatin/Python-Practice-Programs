# Create a function that takes a string containing integers as well as other
# characters and return the sum of the negative integers only.
# Ex negative_sum("22 13%14&-11-22 13 12") => -11 + -22 = -33

# Using re(Regular expressions) module to extract the negative integers
import re


# User-defined function to return the sum of all negative integers
def negative_nos_sum(val):
    total = 0  # Variable holding the sum of all negative integers

    # Making use of findall() method in "re" module to get all negative integers
    # and add them
    for item in re.findall("-\d+", val):
        total += int(item)
    return total


str_val = input("Enter a string containing alphabets and numerics: ")
result = negative_nos_sum(str_val)
print("Sum of all negative integers:", result)
