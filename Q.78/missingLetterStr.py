
# Given a string of letters in the English alphabet, return the letter that's missing
# from the string. The missing letter will make the string be in alphabetical order
# (from A to Z). If there are no missing letters in the string,
# return "No Missing Letter". missingLetter("abdefg") ➞ "c"

# User-defined function to return all the missing letters in the provided string
def missing_letters(value):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # list variable to hold all the missing letters from the string
    excluded_letters = []

    # Executing loop to get all the alphabets starting from index 0 of the input string
    # up to the last index of the input string
    for char in alphabets[alphabets.index(value[0]): alphabets.index(value[-1])]:
        if char not in value:
            excluded_letters.append(char)

    if excluded_letters:
        return excluded_letters
    else:
        return 'No Missing Letters!'


str_val = input('Enter a string: ')

# Checking if the input value is a string or not
if str_val.isalpha():
    print('Missing letters:', missing_letters(str_val))
else:
    print("Provide string input only!")
