def listOperations(list_items):
    print("Before Deleting Element:", list_items)
    list_items.pop(4)
    print("List After removing element at index 4", list_items)
    list_items.insert(2, 101)
    print("List after Adding element at index 2", list_items)
    list_items.append(28)
    print("List after Adding element at last", list_items)


list_1 = [34, 54, 67, 89, 43, 94, 13]
listOperations(list_1)
