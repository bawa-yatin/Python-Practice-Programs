dict_values = [
    {'Name': 'Tom', 'Age': '57'},
    {'Name': 'Bob', 'Age': '57'},
    {'Name': 'Tom', 'Age': '29'},
]

res = list(set(val for item in dict_values for val in item.items()))
print(str(res))

dict_2 = {
    'Gender': 'Male',
    'Location': 'Pune',
    'Locality': 'Baner',
    'Gender': 'Male',
    'Location': 'Pune',
    'Locality': 'Hadapsar'
}

print(set(dict_2.items()))

