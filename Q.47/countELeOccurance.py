
# Python program to count occurrence of each element from list

# Approach 1: Using Traversal

# User-defined function to return the occurrence of every element in list via traversing
def count_ele_occur(items):
    elements_occur = {}  # Dictionary variable to hold the occurrences of every element
    for i in items:
        if i not in elements_occur:
            elements_occur[i] = 1
        else:
            elements_occur[i] += 1
    return elements_occur


list1 = [10, 20, 30, 20, 20, 30, 40, 50, 20, 60, 60, 20, 20]
ele_occur = count_ele_occur(list1)  # Variable holding the response returned from the function
print(ele_occur)


# Approach 2: Using count() function
def ele_count_occur(items):
    elements_occur = {}
    for i in items:
        count = items.count(i)
        elements_occur[i] = count
    return elements_occur


list2 = [55, 35, 55, 45, 75, 35, 75, 45, 95]
occur_ele = ele_count_occur(list2)
print(occur_ele)
