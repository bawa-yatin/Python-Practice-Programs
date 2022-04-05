import string


def str_camel_case(value):
    items = value.split()
    camel_case_str = items[0].lower()
    for val in range(1, len(items)):
        camel_case_str += items[val].capitalize()

    return camel_case_str


str_val = input("Enter a string: ")
if str_val.isdigit():
    print("Provide a string only!")
else:
    res_str = str_camel_case(str_val)
    print("Camel Case Conversion:", res_str)
