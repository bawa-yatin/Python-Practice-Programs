def convertASCIItoHexa(ascii_val):
    hexa_val = []
    for i in range(len(ascii_val)):
        hexa_val.append(hex(ascii_val[i]).lstrip("0x").rstrip("L"))
    return hexa_val


asc_val = []
str_val = input("Enter a string: ")
for i in range(len(str_val)):
    asc_val.append(ord(str_val[i]))

print("ASCII Values:", asc_val)
res = convertASCIItoHexa(asc_val)
print("Hexadecimal Values:", res)
