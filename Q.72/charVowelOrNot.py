
# Python program to check if given char is vowel or consonant

letter_val = input("Enter any letter: ")

# Checking if the input value is a letter or not
if letter_val.isalpha():
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Condition to check if the provided letter is in the vowel list above or not
    if letter_val in vowel_list:
        print(letter_val, "is a vowel!")
    else:
        print(letter_val, "is not a vowel!")
else:
    print("Value should be a letter only!")