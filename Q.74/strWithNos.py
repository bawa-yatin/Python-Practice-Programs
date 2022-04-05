def get_str_with_nos(list_items):
    strings_numbers_list = []
    for val in list_items:
        for i in val:
            if i.isdigit():
                strings_numbers_list.append(val)
                break
    return strings_numbers_list


str_list = input('Enter a list of strings: ').split()
print('Strings containing numbers:', get_str_with_nos(str_list))
