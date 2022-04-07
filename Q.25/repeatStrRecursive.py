
# Python program to create a recursive function that takes two parameters and repeats
# the string n number of times.

def str_repeat(str1, num):
    if num < 0:
        return ""
    elif num == 1:
        return str1

    return str1 + str_repeat(str1, num-1)


result = str_repeat("Hello", 6)  # Variable holding the response returned from the
# function "str_repeat()" after repeating the string number of times provided during
# function call
print(result)
