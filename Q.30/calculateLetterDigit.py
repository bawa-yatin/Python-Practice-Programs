# Python Program to calculate the number of letters, digits, uppercase and lowercase
# letters in a sentence

# Approach 1
str_value = input("Enter a string: ")
digits = letters = upper_letters = lower_letters = 0

for val in str_value:
    if val.isalpha():
        letters += 1
        if val.isupper():
            upper_letters += 1
        elif val.islower():
            lower_letters += 1
    elif val.isnumeric():
        digits += 1

print("Total Digits:", digits)
print("Total Letters:", letters)
print("Total Uppercase Letters:", upper_letters)
print("Total Lowercase Letters:", lower_letters)


# Approach 2: Using Function
def count_letter_digit(val):
    digit_count = letter_count = upper_letter_count = lower_letter_count = 0

    for i in val:
        if i.isalpha():
            letter_count += 1
            if i.isupper():
                upper_letter_count += 1
            elif i.islower():
                lower_letter_count += 1
        elif i.isnumeric():
            digit_count += 1

    print("Total Digits:", digit_count)
    print("Total Letters:", letter_count)
    print("Total Uppercase Letters:", upper_letter_count)
    print("Total Lowercase Letters:", lower_letter_count)


value = input("Enter a string: ")
count_letter_digit(value)


class letterDigitCount:
    def get_count(self, value):
        digit_count = letter_count = upper_letter_count = lower_letter_count = 0

        for i in value:
            if i.isalpha():
                letter_count += 1
                if i.isupper():
                    upper_letter_count += 1
                elif i.islower():
                    lower_letter_count += 1
            elif i.isnumeric():
                digit_count += 1

        print("Total Digits:", digit_count)
        print("Total Letters:", letter_count)
        print("Total Uppercase Letters:", upper_letter_count)
        print("Total Lowercase Letters:", lower_letter_count)


str1 = input("Enter a string: ")
ldc = letterDigitCount()
ldc.get_count(str1)
