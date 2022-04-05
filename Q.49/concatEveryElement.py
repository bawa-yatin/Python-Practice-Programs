def concat_elements(list_1, list_2):
    new_list = []
    for i in list_1:
        for j in list_2:
            new_list.append(i + j)
    print(new_list)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concat_elements(list1, list2)
