# Python Program to return the sum of all numbers in the list

# Approach 1: Using for loop inside function
def ele_add_1(list_ele):
    total = 0  # variable holding the total sum of all elements in the list passed
    for i in range(len(list_ele)):
        total += list_ele[i]
    return total


list1 = [3, 13, 23, 11]
res = ele_add_1(list1)  # Variable holding the total sum of all elements
# returned from the function "ele_add_1()"
print("Result using for loop is", res)


# Approach 2: Using while loop inside function
def ele_add_2(list_ele_2):
    total1 = 0  # variable holding the total sum of all elements in the list passed
    j = 0
    while j < len(list_ele_2):
        total1 += list_ele_2[j]
        j += 1
    return total1


list2 = [13, 7, 21, 31]
res2 = ele_add_2(list2)  # Variable holding the total sum of all elements
# returned from the function "ele_add23()"
print("Result using while loop is", res2)


# Approach 3: Using built-in function sum()
def ele_add_3(list_ele_3):
    return sum(list_ele_3)


list3 = [2, 4, 6, 12, 14]
res3 = ele_add_3(list3)  # Variable holding the total sum of all elements
# returned from the function "ele_add_3()"
print("Result using sum() function is", res3)
