def letter_remove_str(val, items):
    rem_ele_list = []
    for i in range(len(val)):
        if val[i] in items:
            rem_ele_list.append(val[i])
            val = val.replace(val[i], " ")

    return val, rem_ele_list


str_val = input("Enter a string: ")
list_1 = ['a', 'e', 'i', 'o', 'u', 'b', 'd', 'm', 'o', 't', 'r', 's']
obj1, obj2 = letter_remove_str(str_val, list_1)
print("String after removal:", obj1.replace(' ', ''))
print("Removed Elements List:", obj2)
