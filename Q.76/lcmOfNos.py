# Python program that returns the least common multiple (LCM) of two integers

# Approach 1: Basic Approach
# User-defined function to calculate LCM of the numbers provided
def get_lcm(val1, val2):
    if val1 > val2:
        max_val = val1
    else:
        max_val = val2
    while True:
        if (max_val % val1 == 0) and (max_val % val2 == 0):
            lcm = max_val
            break
        max_val += 1
    return lcm


# Executed try-except block to check whether the values provided are numeric in nature
# or not. Also using an if-else condition to check whether the values provided are
# greater than 0 or not
try:
    num_1 = int(input("Enter first positive integer: "))
    num_2 = int(input("Enter second positive integer: "))

    if num_1 > 0 and num_2 > 0:
        result = get_lcm(num_1, num_2)
        print(f"LCM of {num_1} and {num_2} is {result}")
    else:
        print("Invalid Value!")
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using GCD
# User-defined function to calculate GCD of the numbers provided
def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


# User-defined function to calculate LCM of the numbers provided
def calculate_lcm(num1, num2):
    lcm = (num1 * num2) // calculate_gcd(num1, num2)
    return lcm


# Executed try-except block to check whether the values provided are numeric in nature
# or not. Also using an if-else condition to check whether the values provided are
# greater than 0 or not
try:
    val_1 = int(input("Enter first positive integer: "))
    val_2 = int(input("Enter second positive integer: "))

    if val_1 > 0 and val_2 > 0:
        res = calculate_lcm(val_1, val_2)
        print(f"LCM of {val_1} and {val_2} is {res}")
    else:
        print("Invalid Value!")
except ValueError:
    print("Provide numeric value only!")
