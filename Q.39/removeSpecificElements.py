
# Python program to print the list after removing the 0th,4th,5th numbers from list

# Approach 1: Traversal of List
def remove_items(items, index_value):
    updated_list = []  # list variable for holding the remaining elements after
    # deleting 0th, 4th, 5th numbers
    for x in range(len(items)):
        if x != 0 and x != 4 and x != 5:
            updated_list.append(items[x])
    print("New List:", end="\n")
    print(updated_list)


list_items_1 = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
pos = [0, 4, 5]  # list variable containing the list of indexes from which the elements
# have to be removed
remove_items(list_items_1, pos)


# Approach 2: Using Pop Method
# User-defined function for removing 0th, 4th, 5th numbers from the "list2" list
# using pop() method
def remove_items_using_pop(list2, index):
    for x in range(len(list2)):
        for y in index:
            if x == y:
                list2.pop(x)
    print(list2)


list_items_2 = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
pos = [0, 4, 5]  # list variable containing the list of indexes from which the elements
# have to be removed
remove_items_using_pop(list_items_2, pos)


# Approach 3: Using del function
# User-defined function for removing 0th, 4th, 5th numbers from the "list3" list
# using del keyword
def remove_items_using_del(list3, new_pos):
    for i in new_pos:
        del list3[i]
    print(list3)


list_items_3 = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
pos = [0, 4, 5]  # list variable containing the list of indexes from which the elements
# have to be removed
remove_items_using_del(list_items_3, pos)
