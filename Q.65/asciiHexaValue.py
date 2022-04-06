
# Create a function that takes a string's characters as ASCII and returns each
# character's hexadecimal value as a string.

# User-defined function to return the hexadecimal value of each character passed
def convert_ascii_to_hexa(ascii_val):
    hexa_val = []  # list variable for holding the hexadecimal values
    for i in range(len(ascii_val)):
        hexa_val.append(hex(ascii_val[i]).lstrip("0x").rstrip("L"))
    return hexa_val


asc_val = []  # list variable for holding the ascii values of the characters present
# in the input string

str_val = input("Enter a string: ")
for i in range(len(str_val)):
    asc_val.append(ord(str_val[i]))

print("ASCII Values:", asc_val)
res = convert_ascii_to_hexa(asc_val)  # Variable holding the response returned
# from the function
print("Hexadecimal Values:", res)
