# Python Program to square each odd number in a list

# Approach 1: Basic Approach(Traversing through each element of list)
list1 = [11, 52, 45, 82, 31, 7, 17, 98, 102, 151, 501, 56, 397, 652, 71, 199,
         218, 56, 6, 787]
squared_ele = []  # Initializing list variable for holding the squared values of all
# elements in "list1" list
for i in list1:
    # Checking condition if current element is not a giving a remainder of 0 after
    # dividing it by two, append the square of that particular element in the
    # "squared_ele" list
    if i % 2 != 0:
        squared_ele.append(i * i)

print(squared_ele)


# Approach 2: Using Function and exponent operator
def odd_no_square(items):
    new_list = []  # Initializing list variable for holding the squared values of all
    # elements in "items" list
    for j in items:
        if j % 2 != 0:
            new_list.append(j ** 2)
    return new_list


list2 = [11, 52, 45, 82, 31, 7, 17, 98, 102, 151, 501, 56, 397, 652, 71, 199,
         218, 56, 6, 787]
res = odd_no_square(list2)  # Variable holding the response returned
# from the function "odd_no_square" after calculating the square of each odd number
print(res)


# Approach 3: Using Class and pow() method
class squareOddItem:
    def get_odd_items_square(self, ele):
        new_list = []  # Initializing list variable for holding the squared values of all
        # elements in "items" list
        for j in ele:
            if j % 2 != 0:
                new_list.append(pow(j, 2))
        return new_list


list3 = [41, 52, 45, 82, 31, 17, 28, 98, 102, 151, 501, 56, 397, 652, 71, 199,
         218, 56, 16, 187]
obj1 = squareOddItem()  # Object creation of class "squareOddItem"
result = obj1.get_odd_items_square(list3)  # Variable holding the response returned
# from the class method after calculating the square of each odd number
print(result)
