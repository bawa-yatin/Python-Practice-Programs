# Python Program to return a string as an integer

# Approach 1:

try:
    input_val = input("Enter any numeric value: ")
    print(type(input_val))
    new_type = int(input_val)
    print(type(new_type))
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Function
def strConvert(val):
    print("\nUsing Functions")
    print("Original type is", type(val))
    updated_type = int(val)
    return updated_type


sc = strConvert("76")
print(sc)
print("New Type is", type(sc))


# Approach 3: Using Class
class convertStr:
    def __init__(self, value):
        self.value = value

    def getIntVal(self):
        print("\nUsing Class")
        print(self.value)
        print(type(self.value))
        modified_type = int(self.value)
        return modified_type


cs = convertStr("27")
result = cs.getIntVal()
print(result)
print("New Type is", type(result))
