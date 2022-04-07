# Python program to convert list into dictionary and add new item into dictionary

# User-defined function to convert list items into dictionary and return it
def convert_lists(items):
    iter_var = iter(items)
    res_dict = dict(zip(iter_var, iter_var))
    return res_dict


list_item = ['Name', 'Rohan', 'Age', 28, 'Code', 165]  # Input List
res = convert_lists(list_item)
print("Converted List into Dictionary")
print(res)  # Variable holding the response returned from the function "convert_lists()"

# Adding New Items to converted dictionary
res['Gender'] = 'Male'
res.update({'Phone': 7819173101})  # update function to update and new item in dictionary

print("After adding new elements", end="\n")
print(res)
