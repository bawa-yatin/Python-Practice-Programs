
# Python program which accepts a sequence of words separated by whitespace as input
# to print the words composed of digits only.
# Example : 2 cats and 3 dogs.
# Output should be :
# ['2', '3']
# [‘cats’, ‘dogs’]

# Approach 1:
val_1 = input("Enter a string with some digits: ")
val_1 = val_1.split()  # Splitting the string provided to check which value is
# numeric and which value is a word
digit_list = []  # list variable for holding all the digits present inside the string
word_list = []  # list variable for holding all the words present inside the string

for val in val_1:
    if val.isdigit():
        digit_list.append(val)
    else:
        word_list.append(val)

print("Digits in string are:", digit_list)
print("Words in string are:", word_list)


# Approach 2: Using Function
def get_digits_only():
    str_val = input("Enter a string with some digits: ")
    str_val = str_val.split()
    list_digit = []  # list variable for holding all the digits present inside the string
    list_word = []  # list variable for holding all the words present inside the string
    for item in str_val:
        if item.isdigit():
            list_digit.append(item)
        else:
            list_word.append(item)

    print("Digits in string are:", list_digit)
    print("Words in string are:", list_word)


get_digits_only()
