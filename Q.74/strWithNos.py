
# Python program that takes an array of strings and returns an array with only the
# strings that have numbers in them.
# If there are no strings containing numbers, return an empty array.

def get_str_with_nos(list_items):
    strings_numbers_list = []  # list variable containing strings that have numbers
    # in them
    for val in list_items:
        for i in val:
            if i.isdigit():
                strings_numbers_list.append(val)
                break
    return strings_numbers_list


# Splitting input string into a list of strings and passing it to user-defined function
str_list = input('Enter a list of strings: ').split()
print('Strings containing numbers:', get_str_with_nos(str_list))
