def numLen(val1):
    str_val = str(val1)
    num_len = 0
    for i in str_val:
        num_len += 1
    return num_len


try:
    num_val = int(input("Enter any positive integer: "))
    result = numLen(num_val)
    print("Length of Number:", result)
except ValueError:
    print("Provide a numeric value only!")