# Python program to convert boolean value to string

boolVal1 = True
print(type(boolVal1))

# Approach 1: Using built-in str() method
str_convert = str(boolVal1)
print(type(str_convert))

# Approach 2: Using built-in format() method
str_convert_format = format(boolVal1)
print(type(str_convert_format))

# Approach 3: Using if condition
print(type(boolVal1))

if boolVal1:
    boolVal1 = "True"
    print(type(boolVal1))
elif not boolVal1:
    boolVal1 = "False"
    print(type(boolVal1))
