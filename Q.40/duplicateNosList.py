# Approach 1: Using Traversal

def countDuplicateEle(items):
    repeat_elements = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in repeat_elements:
                repeat_elements.append(items[i])
    return repeat_elements


list1 = [10, 20, 30, 20, 20, 30, 40, 50, 20, 60, 60, 20, 20]
dup_ele = countDuplicateEle(list1)
print("Duplicate Elements are", dup_ele)


# Approach 2: Using count() function

def duplicateEleCount(items):
    repeat_elements = []
    for i in items:
        count = items.count(i)
        if count > 1:
            repeat_elements.append(items[i])
    return repeat_elements


list2 = [55, 35, 55, 45, 75, 35, 75, 45, 95]
rep_ele = countDuplicateEle(list2)
print("Duplicate Elements are", rep_ele)
