# Python program to check if one object is equal to another object

# Using "==" operator for comparing the values of both objects and "is" operator to
# check if both objects are identical in nature

# Approach 1: Basic Approach
list_1 = ["apple", "orange", "banana", "watermelon"]
list_2 = ["apple", "orange", "banana", "watermelon"]

# Checks the value of both objects
if list_1 == list_2:
    print("Yes both objects are equal")
else:
    print("No objects are not equal")

list_3 = list_2

if list_2 is list_3:
    print("Both objects are identical")
else:
    print("Both objects are different")


# Approach 2: Using Function
def objCompare(first, second):
    print("\nUsing Function")
    third = first
    if first == second and first is third:
        return True
    else:
        return False


list1 = [20, 40, 80, 90]
list2 = [20, 40, 80, 90, 105]
res = objCompare(list1, list2)
print(res)
