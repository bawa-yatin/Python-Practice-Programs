def concatTwoLists(list1, list2):
    res = [i + j for i, j in zip(list1, list2)]
    print(res)


list_1 = ["M", "na", "i", "Aus"]
list_2 = ["y", "me", "s", "tin"]
concatTwoLists(list_1, list_2)
