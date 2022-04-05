def convert_lists(items):
    iter_var = iter(items)
    res_dict = dict(zip(iter_var, iter_var))
    return res_dict


list_item = ['Name', 'Rohan', 'Age', 28, 'Code', 165]
res = convert_lists(list_item)
print("Converted List into Dictionary")
print(res)

# Adding New Items to converted dictionary
res['Gender'] = 'Male'
res.update({'Phone': 7819173101})

print("After adding new elements", end="\n")
print(res)
