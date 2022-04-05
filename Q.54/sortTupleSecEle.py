def sort_tuple(tup_items):
    return sorted(tup_items, key=lambda val: val[1])


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
res = sort_tuple(tuple1)
print("Before Sorting", tuple1)
print("After Sorting", res)
