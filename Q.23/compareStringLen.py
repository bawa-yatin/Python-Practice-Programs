# Python Program to compare strings by count of characters

# Approach 1: Using len() function
def str_compare(str1, str2):
    if len(str1) == len(str2):
        return True
    else:
        return False


str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")
res = str_compare(str_1, str_2)  # Variable holding the response returned from the
# function "str_compare()" after comparing length of both strings inputted
print("Result is", res)


# Approach 2: Using For Loop
def str_compare_2(string1, string2):
    total_1 = 0  # variable to keep track of the length of string1
    total_2 = 0  # variable to keep track of the length of string2
    for i in range(len(string1)):
        total_1 += + 1
    for j in range(len(string2)):
        total_2 += + 1
    if total_1 == total_2:
        return True
    else:
        return False


res = str_compare_2("Hello", "Adam")  # Variable holding the response returned from the
# function "str_compare_2()" after comparing length of both strings inputted
print("Result is", res)


# Approach 3: Using While Loop
def str_compare_3(val1, val2):
    sum_1 = 0  # variable to keep track of the length of first string
    sum_2 = 0  # variable to keep track of the length of second string
    for i in range(len(val1)):
        sum_1 += + 1
    for j in range(len(val2)):
        sum_2 += + 1
    if sum_1 == sum_2:
        return True
    else:
        return False


res = str_compare_3("Apple", "Mango")  # Variable holding the response returned from the
# function "str_compare_3()" after comparing length of both strings inputted
print("Result is", res)
