# Approach 1:

val_1 = input("Enter a string with some digits: ")
val_1 = val_1.split()
digit_list = []
word_list = []

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
    list_digit = []
    list_word = []
    for item in str_val:
        if item.isdigit():
            list_digit.append(item)
        else:
            list_word.append(item)

    print("Digits in string are:", list_digit)
    print("Words in string are:", list_word)


get_digits_only()
