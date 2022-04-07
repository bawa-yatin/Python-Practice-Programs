
# Python program that takes two list and iterate both list simultaneously
# and print output

# User-defined function that prints elements of "list1" and "list2" simultaneously
# zip function is used here to combine the elements of both the lists

def iter_multiple_list(list1, list2):
    for i, j in zip(list1, list2):
        print(i, j)


list_1 = [15, 25, 35, 45]
list_2 = ["Apple", "Mango", "Cherry", "Strawberry"]
iter_multiple_list(list_1, list_2)
