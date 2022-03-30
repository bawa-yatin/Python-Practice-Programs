# Python Program to concatenate two integer lists

# Approach 1: Using for loop to append elements of first list into second

list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]

for i in list2:
    list1.append(i)

print("Final list after concatenation:", list1)


# Approach 2: Using '+' operator inside function to concatenate lists
def listJoin(list_1_ele, list_2_ele):
    list_1_ele = list_1_ele + list_2_ele
    return list_1_ele


list_1 = [11, 17, 21, 56, 43]
list_2 = [9, 19, 23, 39, 67]
result = listJoin(list_1, list_2)
print("Concatenated list is", result)


# Approach 3: Using built-in function extend() to concatenate elements of two lists
# extend() takes a single parameter which is an iterable i.e. list, tuple or string

class concatLists:
    def joinLists(self, first_list_ele, sec_list_ele):
        first_list_ele.extend(sec_list_ele)
        return first_list_ele


first_list = [29, 19, 23, 39, 67, 3]
sec_list = [17, 7, 54, 26, 41, 13]
cl = concatLists()
res = cl.joinLists(first_list, sec_list)
print("Concatenated list is", res)
