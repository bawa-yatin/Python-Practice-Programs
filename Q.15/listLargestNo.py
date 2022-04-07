# Python Program to find the largest number in a list

# Approach 1: Using For Loop in a Function
def largest_no(list1):
    largest_ele = list1[0]  # variable holding the first element of list and assuming
    # it to be the largest element in list as of now
    for i in range(1, len(list1)):
        if list1[i] > largest_ele:
            largest_ele = list1[i]
    return largest_ele


list_1 = [12, 5, 21, 19, 43, 37, 51, 28]
res1 = largest_no(list_1)  # variable holding the response containing the
# largest number in list
print("Largest element in the list is", res1)


# Approach 2: Using built-in function max() inside function
def no_largest(list2):
    return max(list2)


list_2 = [22, 98, 5, 32, 17, 87]
res2 = no_largest(list_2)  # variable holding the response containing the
# largest number in list
print("Largest element is", res2)


# Approach 3: Sorting the list in ascending order and printing the last element
# in the list using sort() method
def largest_no_using_sort(list3):
    list3.sort()
    return list_3[-1]


list_3 = [10, 3, 21, 53, 18, 9]
res1 = largest_no_using_sort(list_3)  # variable holding the response containing the
# largest number in list
print("Largest Element is", res1)
