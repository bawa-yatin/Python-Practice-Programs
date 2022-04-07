
# Define a function that can accept two strings as input and print the string
# with maximum length in the console.
# If two strings have the same length, then the function should print all strings
# line by line.

# User-defined function to determine which string has the maximum length(str1 or str2)
# using len() function
def get_str_max_length(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    elif len(str1) == len(str2):
        print(str1, end='\n')
        print(str2)


str_val_1 = input('Enter first string: ')
str_val_2 = input('Enter second string: ')
get_str_max_length(str_val_1, str_val_2)
