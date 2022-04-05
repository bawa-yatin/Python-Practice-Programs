# Python Program to find the remainder of two numbers

# Approach 1

try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))

    res = num_1 % num_2
    print("Remainder of", num_1, "and", num_2, "is", res)
except ValueError:
    print("Provide numeric value only!")
except ZeroDivisionError:
    print("Division by 0 not possible!")


# Approach 2: Using Functions
def rem_nos(val1, val2):
    print("\nUsing Functions")
    if val1 >= 1 and val2 >= 1:
        result = val1 % val2
        return result
    else:
        print("Invalid Value!")


res1 = rem_nos(15, 8)
print("Remainder is", res1)

# Approach 3: Using in-built divmod() function
# This function takes two numbers as parameters and returns a tuple containing
# both quotient and remainder. To access only the remainder part we can use indexing

funcRem = divmod(21, 9)
print("\nUsing built-in function")
print("Remainder is", funcRem[1])
