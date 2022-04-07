
# Python Program to reverse a tuple

# Approach 1: Using slicing method inside a function

# User-defined function to reverse a tuple using slicing method
def tuple_rev(tup_items):
    rev_tup = tup_items[::-1]
    return rev_tup


tup_1 = ("A", "B", "C", "D")
res = tuple_rev(tup_1)  # Variable holding the response returned from the function
print("Before Reversing:", tup_1)
print("After Reversing:", res)


# Approach 2: Using reversed() method
class reversedTuple:
    def __init__(self, items):
        self.items = items

    def get_reverse_tuple(self):
        new_tuple = ()  # Variable for holding the reversed tuple
        for i in reversed(self.items):
            new_tuple += (i,)
        return new_tuple


tup_2 = (10, 20, 30, 40, 50)
rt = reversedTuple(tup_2)
result = rt.get_reverse_tuple()  # Variable holding the response returned from the function
print("Before Reversing:", tup_2)
print("After Reversing:", result)
