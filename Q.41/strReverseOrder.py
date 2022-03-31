# Approach 1: Using Loop

def reverseStr(val):
    rev_str = ""
    for i in val:
        rev_str = i + rev_str
    return rev_str


str_val = input("Enter a string: ")
print("Original String: ", str_val)
res_val = reverseStr(str_val)
print("Reversed String: ", res_val)


# Approach 2: Using built-in reversed function
def strReverse(val2):
    str_rev = "".join(reversed(val2))
    return str_rev


str_val_2 = input("Enter a string: ")
print("Original String: ", str_val_2)
res_val_2 = strReverse(str_val_2)
print("Reversed String: ", res_val_2)

# Approach 3: With Slicing

str_val_3 = input("Enter a string: ")
rev_str = str_val_3[::-1]
print(rev_str)