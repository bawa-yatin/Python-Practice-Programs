# Python Program to return a string as an integer

# Approach 1:
# Using try-except block to verify whether the input provided is in numeric form or not
try:
    input_val = input("Enter any numeric value: ")
    print(type(input_val))
    new_type = int(input_val)  # variable holding the integer conversion of number in
    # string format
    print(type(new_type))
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Function
def str_convert(val):
    print("\nUsing Functions")
    print("Original type is", type(val))
    updated_type = int(val)  # variable holding the integer conversion of number in
    # string format
    return updated_type


sc = str_convert("76")  # Variable holding the response returned from the function
# "str_convert()"
print(sc)
print("New Type is", type(sc))


# Approach 3: Using Class
class convertStr:
    def __init__(self, value):
        self.value = value

    def get_int_val(self):
        print("\nUsing Class")
        print(self.value)
        print(type(self.value))
        modified_type = int(self.value)  # variable holding the integer conversion
        # of number in string format
        return modified_type


# Object creation of "convertStr" class and simultaneously assigning the value to
# class variable(value) through constructor method
cs = convertStr("27")
result = cs.get_int_val()
print(result)
print("New Type is", type(result))
