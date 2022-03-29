# Python Program to find the largest number in a list

# Approach 1: Using For Loop in a Function
def largestNo(list1):
    largest_ele = list1[0]
    for i in range(1, len(list1)):
        if list1[i] > largest_ele:
            largest_ele = list1[i]
    print("Largest element in the list is", largest_ele)


list_1 = [12, 5, 21, 19, 43, 37, 51, 28]
largestNo(list_1)


# Approach 2: Using built-in function max() inside function
def noLargest(list2):
    print("\nUsing built-in function")
    print("Largest element is", max(list2))


list_2 = [22, 98, 5, 32, 17, 87]
noLargest(list_2)

# Approach 3: Sorting the list in ascending order and printing the last element
# in the list.

list_3 = [10, 3, 21, 53, 18, 9]
list_3.sort()
print("\nAfter sorting list")
print("Largest Element is", list_3[-1])
