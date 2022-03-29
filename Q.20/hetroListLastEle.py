# Python program to return the last element of a list. List can be homogeneous or
# heterogeneous

# Approach 1: Reversing the list and printing the first element
new_list = [3, "John", 6.09, "Adam", True]
new_list.reverse()
print("Last element is", new_list[0])


# Approach 2: Using function

def lastElement(ele):
    print(f"Last element of the list is {ele[-1]}")


list_ele = ["Banana", 11, True, 23, 77, 4.87]
lastElement(list_ele)


# Approach 3: Using for loop in class
class endElement:
    def eleLast(self, list_2_ele):
        for i in range(len(list_2_ele)):
            if i == len(list_2_ele) - 1:
                print("Last element in list is", list_2_ele[i])


list_2 = [False, 8, "Hello", 8.09, "John"]
e1 = endElement()
e1.eleLast(list_2)
