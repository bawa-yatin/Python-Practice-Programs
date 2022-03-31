# Approach 1: Using Traversal

def countEleOccur(items):
    elements_occur = {}
    for i in items:
        if i not in elements_occur:
            elements_occur[i] = 1
        else:
            elements_occur[i] += 1
    return elements_occur


list1 = [10, 20, 30, 20, 20, 30, 40, 50, 20, 60, 60, 20, 20]
ele_occur = countEleOccur(list1)
print(ele_occur)


# Approach 2: Using count() function

def eleCountOccur(items):
    elements_occur = {}
    for i in items:
        count = items.count(i)
        elements_occur[i] = count
    return elements_occur


list2 = [55, 35, 55, 45, 75, 35, 75, 45, 95]
occur_ele = eleCountOccur(list2)
print(occur_ele)
