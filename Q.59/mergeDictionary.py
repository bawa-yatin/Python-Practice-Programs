# Approach 1: Using Pipe(|) Operator
def mergeDict(first_dict, second_dict):
    res = first_dict | second_dict
    return res


dict_1 = {'Apple': 10, 'Mango': 20}
dict_2 = {'Banana': 12, 'Cherry': 7}
obj1 = mergeDict(dict_1, dict_2)
print("After merging dictionaries:", obj1)


# Approach 2: Using Update Method

dict1 = {'Bike': 15, 'Cars': 20}
dict2 = {'Trucks': 7, 'Scooters': 17}
dict1.update(dict2)
print("After merging dictionaries:", dict1)
