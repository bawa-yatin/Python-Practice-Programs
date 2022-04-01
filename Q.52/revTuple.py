def tupleRev(tup_items):
    rev_tup = tup_items[::-1]
    return rev_tup


tup_1 = ("A", "B", "C", "D")
res = tupleRev(tup_1)
print("Before Reversing:", tup_1)
print("After Reversing:", res)


class reversedTuple:
    def __init__(self, items):
        self.items = items

    def getReverseTuple(self):
        new_tuple = ()
        for i in reversed(self.items):
            new_tuple += (i,)
        return new_tuple


tup_2 = (10, 20, 30, 40, 50)
rt = reversedTuple(tup_2)
result = rt.getReverseTuple()
print("Before Reversing:", tup_2)
print("After Reversing:", result)
