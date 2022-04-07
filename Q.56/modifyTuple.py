
# Python program to modify a tuple

tuple_items = (23, 18, 6, 12, 19)

# Appending an element to a tuple
print("Original Tuple:", tuple_items)
tuple_items += (90,)
print("After appending new element:", tuple_items)

# Appending an element at the start of tuple
print("Original Tuple:", tuple_items)
tuple_items = (81,) + tuple_items
print("After appending element at start:", tuple_items)

# Appending element at a specific position
print("Original Tuple is:", tuple_items)
tuple_1 = tuple_items[0:3]
tuple_2 = tuple_items[3:]

myTuple = tuple_1 + (66,) + tuple_2
print("Updated tuple is:", myTuple)

# Deleting an element from tuple(From Starting)
print("Original Tuple is:", tuple_items)
updated_tuple = tuple_items[1:]
print("Tuple after deleting first element:", updated_tuple)

# Deleting an element from tuple(From Last Position)
print("Original Tuple is:", tuple_items)
updated_tuple = tuple_items[:len(tuple_items) - 1]
print("Tuple after deleting last element:", updated_tuple)