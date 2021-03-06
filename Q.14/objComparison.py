# Python program to check if one object is equal to another object

# Using "==" operator for comparing the values of both objects and "is" operator to
# check if both objects are identical in nature

# Approach 1: Basic Approach(Using == operator)
def compare_obj(list1, list2):
    # Checks the value of both objects
    if list1 == list2:
        return True
    else:
        return False


list_1 = ["apple", "orange", "banana", "watermelon"]
list_2 = ["apple", "orange", "banana", "watermelon"]
result = compare_obj(list_1, list_2)  # variable holding the response returned after
# comparing two objects
print(result)


# Approach 2: Using Function and "is" operator
def obj_compare(first, second):
    third = first  # Assigning value of "first" object to "third" object
    if first is third:
        return True
    else:
        return False


list1 = [20, 40, 80, 90]
list2 = [20, 40, 80, 90, 105]
res = obj_compare(list1, list2)  # variable holding the response returned after
# comparing two objects
print(res)
