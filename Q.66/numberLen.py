
# Create a function that takes a number and returns its length
# (use of the len() function is prohibited)

# User-defined function to return the length of input number
def num_len(val1):
    str_val = str(val1)  # Variable holding the string form of input value

    # Variable holding the length of the input value
    num_len = 0
    for i in str_val:
        num_len += 1
    return num_len


# Using try-except block to verify whether the value entered is in numeric form or not
try:
    num_val = int(input("Enter any positive integer: "))
    result = num_len(num_val)  # Variable holding the response returned from the function
    print("Length of Number:", result)
except ValueError:
    print("Provide a numeric value only!")