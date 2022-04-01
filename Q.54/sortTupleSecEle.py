def sortTuple(tup_items):
    return sorted(tup_items, key=lambda val: val[1])


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
res = sortTuple(tuple1)
print("Before Sorting", tuple1)
print("After Sorting", res)
