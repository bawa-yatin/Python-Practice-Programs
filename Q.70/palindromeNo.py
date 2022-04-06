# Python program to identify if number is palindrome or not

# Approach 1: Basic Approach

# Using try-except block to check whether value provided is numeric in nature or not
try:
    num_val = int(input("Enter a number: "))
    temp = num_val  # temp variable used for holding the input value temporarily
    rev = 0  # variable for holding the reverse of the input number
    while num_val > 0:
        remainder = num_val % 10  # remainder variable holds the remainder after
        # dividing the input number by 10
        rev = (rev * 10) + remainder
        num_val = num_val // 10

    # Condition to check if reverse of input number is equal to the actual number
    if temp == rev:
        print("Number is palindrome!")
    else:
        print("Number is not palindrome!")

except ValueError as ve:
    print("Only numeric value allowed!")


# Approach 2: Using Slicing

# Using try-except block to check whether value provided is numeric in nature or not
try:
    num_val_2 = input("Enter a number: ")
    # Using slicing operation to get the reverse of a number and then comparing it
    # with the actual input
    if num_val_2 == num_val_2[::-1]:
        print("Number is palindrome!")
    else:
        print("Number is not palindrome!")

except ValueError as ve:
    print("Only numeric value allowed!")
