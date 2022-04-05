def concat_two_lists(list1, list2):
    res = [i + j for i, j in zip(list1, list2)]
    print(res)


list_1 = ["M", "na", "i", "Aus"]
list_2 = ["y", "me", "s", "tin"]
concat_two_lists(list_1, list_2)
