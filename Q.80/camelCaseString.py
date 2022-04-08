
# Python program that takes a string and returns it back in camelCase.
# camelCasing("Hello World") ➞ "helloWorld"

# User-defined function to convert the provided input into a camel-case string
def str_camel_case(value):
    items = value.split()  # Splitting the value and storing it in 'item' variable
    camel_case_str = items[0].lower()  # converting the first letter of first item
    # to lowercase
    for val in range(1, len(items)):
        camel_case_str += items[val].capitalize()

    return camel_case_str


str_val = input("Enter a string: ")

# Checking if the input value is a string or not
if str_val.isdigit():
    print("Provide a string only!")
else:
    res_str = str_camel_case(str_val)
    print("Camel Case Conversion:", res_str)
