# Python program to return the last element of a list. List can be homogeneous or
# heterogeneous

# Approach 1: Using for loop in class
class endElement:
    def ele_last(self, list_2_ele):
        for i in range(len(list_2_ele)):
            if i == len(list_2_ele) - 1:
                return list_2_ele[i]


list_2 = [False, 8, "Hello", 8.09, "John"]
e1 = endElement()
res = e1.ele_last(list_2)
print(res)


# Approach 2: Reversing the list and printing the first element
new_list = [3, "John", 6.09, "Adam", True]
new_list.reverse()
print("Last element is", new_list[0])


# Approach 3: Using function
def last_element(ele):
    return f"Last element of the list is {ele[-1]}"


list_ele = ["Banana", 11, True, 23, 77, 4.87]
print(last_element(list_ele))
