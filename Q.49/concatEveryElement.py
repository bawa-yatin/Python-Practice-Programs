
# Concatenate two list in following
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# User-defined function to combine first element of "list_1" with every element of
# "list_2" and so on.
def concat_elements(list_1, list_2):
    new_list = []  # list variable for holding the concatenated elements
    for i in list_1:
        for j in list_2:
            new_list.append(i + j)
    print(new_list)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concat_elements(list1, list2)
