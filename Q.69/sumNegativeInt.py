import re


def negative_nos_sum(val):
    total = 0
    for item in re.findall("-\d+", val):
        total += int(item)
    return total


str_val = input("Enter a string containing alphabets and numerics: ")
result = negative_nos_sum(str_val)
print("Sum of all negative integers:", result)
