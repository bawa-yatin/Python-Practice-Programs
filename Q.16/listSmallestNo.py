# Python Program to find the smallest number in a list

# Approach 1: Using For Loop in a Function
def smallest_no(list1):
    smallest_ele = list1[0]  # variable holding the first element of list and assuming
    # it to be the smallest element in list as of now
    for i in range(1, len(list1)):
        if list1[i] < smallest_ele:
            smallest_ele = list1[i]
    return smallest_ele


list_1 = [12, 5, 21, 19, 43, 37, 51, 28]
res = smallest_no(list_1)  # variable holding the response containing the smallest
# number in list
print("Smallest element in the list is", res)


# Approach 2: Using built-in function min() inside function
def no_smallest(list2):
    return min(list2)


list_2 = [22, 98, 25, 32, 6, 17, 87]
result = no_smallest(list_2)  # variable holding the response containing the smallest
# number in list
print("Smallest Element is", result)


# Approach 3: Sorting the list in ascending order and printing the first element
# in the list.
def smallest_no_using_sort(list3):
    list3.sort()
    return list_3[0]


list_3 = [10, 3, 21, 53, 18, 9]
res1 = smallest_no_using_sort(list_3)  # variable holding the response containing the smallest
# number in list
print("Smallest Element is", res1)
