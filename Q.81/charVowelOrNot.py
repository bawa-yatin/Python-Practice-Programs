
letter_val = input("Enter any letter: ")
if letter_val.isalpha():
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if letter_val in vowel_list:
        print(letter_val, "is a vowel!")
    else:
        print(letter_val, "is not a vowel!")
else:
    print("Value should be a letter only!")