# Approach 1: Using set() method

list1 = []


def list_ele():
    for i in range(25):
        item = input("Enter the element: ")
        list1.append(item)
    return list(set(list1))


obj = list_ele()
print(obj)

# Approach 2: Using Dict Method
list2 = []


def unique_ele():
    for i in range(0, 25):
        num = input("Enter an element: ")
        list2.append(num)
    return list(dict.fromkeys(list2))


obj2 = unique_ele()
print(obj2)
