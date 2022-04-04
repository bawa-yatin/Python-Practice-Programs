# Approach 1: Basic Approach

try:
    num_val = int(input("Enter a number: "))
    temp = num_val
    rev = 0
    while num_val > 0:
        remainder = num_val % 10
        rev = (rev * 10) + remainder
        num_val = num_val // 10

    if temp == rev:
        print("Number is palindrome!")
    else:
        print("Number is not palindrome!")

except ValueError as ve:
    print("Only numeric value allowed!")

# Approach 2: Using Slicing
try:
    num_val_2 = input("Enter a number: ")
    if num_val_2 == num_val_2[::-1]:
        print("Number is palindrome!")
    else:
        print("Number is not palindrome!")

except ValueError as ve:
    print("Only numeric value allowed!")
