# Python Program to compare strings by count of characters

# Approach 1: Using len() function
def strCompare(str1, str2):
    if len(str1) == len(str2):
        return True
    else:
        return False


str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")
res = strCompare(str_1, str_2)
print("Result is", res)


# Approach 2: Using For Loop
def strCompare2(string1, string2):
    total_1 = 0
    total_2 = 0
    for i in range(len(string1)):
        total_1 += + 1
    for j in range(len(string2)):
        total_2 += + 1
    if total_1 == total_2:
        return True
    else:
        return False


res = strCompare("Hello", "Adam")
print("Result is", res)


# Approach 3: Using While Loop
def strCompare3(val1, val2):
    sum_1 = 0
    sum_2 = 0
    for i in range(len(val1)):
        sum_1 += + 1
    for j in range(len(val2)):
        sum_2 += + 1
    if sum_1 == sum_2:
        return True
    else:
        return False


res = strCompare("Apple", "Mango")
print("Result is", res)
