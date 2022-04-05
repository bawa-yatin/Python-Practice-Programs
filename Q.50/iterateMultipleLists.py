def iter_multiple_list(list1, list2):
    for i, j in zip(list1, list2):
        print(i, j)


list_1 = [15, 25, 35, 45]
list_2 = ["Apple", "Mango", "Cherry", "Strawberry"]
iter_multiple_list(list_1, list_2)
