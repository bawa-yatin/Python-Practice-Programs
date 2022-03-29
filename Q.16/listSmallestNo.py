# Python Program to find the smallest number in a list

# Approach 1: Using For Loop in a Function
def smallestNo(list1):
    largest_ele = list1[0]
    for i in range(1, len(list1)):
        if list1[i] < largest_ele:
            largest_ele = list1[i]
    print("Smallest element in the list is", largest_ele)


list_1 = [12, 5, 21, 19, 43, 37, 51, 28]
smallestNo(list_1)


# Approach 2: Using built-in function min() inside function
def noSmallest(list2):
    print("\nUsing built-in function")
    print("Smallest element is", min(list2))


list_2 = [22, 98, 25, 32, 6, 17, 87]
noSmallest(list_2)

# Approach 3: Sorting the list in ascending order and printing the first element
# in the list.

list_3 = [10, 3, 21, 53, 18, 9]
list_3.sort()
print("\nAfter sorting list")
print("Smallest Element is", list_3[0])