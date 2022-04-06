
# Python program to check char is digit without using isdigit()
# take input from console

char_value = input("Enter the character: ")

# Condition to check if the input character lies between 0 and 9, if "Yes" it's a digit
if '0' <= char_value <= '9':
    print(char_value, "is a Number")
else:
    print(char_value, "is not a Number")