
# Python program to check if key exists in dictionary and delete that key
# value from dictionary

# Approach 1: Using In Operator

dict_1 = {"Books": 15, "Chocolates": 25, "Games": 20}
print("Before removing element:", dict_1)
if "Chocolates" in dict_1:
    dict_1.pop("Chocolates")

print("After removing element:", dict_1)


# Approach 2: Using del keyword

# User-defined function to check if key exists in dictionary and deleting that key
def remove_dict_key(dict_ele):
    if dict_ele.get("Fruits") is not None:
        del dict_ele["Fruits"]
    return dict_ele


dict_2 = {"Fruits": 15, "Eggs": 25, "Bread": 20}
print("Before removing element:", dict_2)
res = remove_dict_key(dict_2)  # Variable holding the response returned from the
# function after deleting the key
print("After removing element:", dict_2)