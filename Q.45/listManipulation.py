
# Remove items from list
# list1 = [54, 44, 27, 79, 91, 41]
# Output:
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

# User-defined function to add, remove elements from "list_items" using append(),
# insert() and pop() function
def list_operations(list_items):
    print("Before Deleting Element:", list_items)
    list_items.pop(4)
    print("List After removing element at index 4", list_items)
    list_items.insert(2, 101)
    print("List after Adding element at index 2", list_items)
    list_items.append(28)
    print("List after Adding element at last", list_items)


list_1 = [34, 54, 67, 89, 43, 94, 13]
list_operations(list_1)
