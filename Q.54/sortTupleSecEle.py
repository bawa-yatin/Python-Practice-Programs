# Python programSort tuple by 2nd item
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

# User-defined function to sort the tuple items on the basis of 2 item in tuple
def sort_tuple(tup_items):
    return sorted(tup_items, key=lambda val: val[1])


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
res = sort_tuple(tuple1)  # Variable holding the response returned from the function
# sort_tuple()
print("Before Sorting", tuple1)
print("After Sorting", res)
