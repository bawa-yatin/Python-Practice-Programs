def replaceWord(str_val, val1, val2):
    return str_val.replace(val1, val2)


def replaceChar(str_val, val1, val2):
    return str_val.replace(val1, val2)


str_1 = "My name is Akash"
str_2 = "i am 17 years old"

print("Original String:", str_1)
new_str_1 = replaceWord(str_1, "Akash", "Kabir")
print("Modified String:", new_str_1)

print("Before Replacing Char:", str_2)
new_str_2 = replaceWord(str_2, "i", "I")
print("After Replacing Char:", new_str_2)
