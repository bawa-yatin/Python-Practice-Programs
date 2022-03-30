# Python Program to square each odd number in a list

# Approach 1: Basic Approach
list1 = [11, 52, 45, 82, 31, 7, 17, 98, 102, 151, 501, 56, 397, 652, 71, 199,
         218, 56, 6, 787]
squared_ele = []
for i in list1:
    if i % 2 != 0:
        squared_ele.append(i * i)

print(squared_ele)


# Approach 2: Using Function and exponent operator
def oddNoSquare(items):
    new_list = []
    for j in items:
        if j % 2 != 0:
            new_list.append(j ** 2)
    return new_list


list2 = [11, 52, 45, 82, 31, 7, 17, 98, 102, 151, 501, 56, 397, 652, 71, 199,
         218, 56, 6, 787]
res = oddNoSquare(list2)
print(res)


# Approach 3: Using Class and pow() method
class squareOddItem:
    def getOddItemsSquare(self, ele):
        new_list = []
        for j in ele:
            if j % 2 != 0:
                new_list.append(pow(j, 2))
        return new_list


list3 = [41, 52, 45, 82, 31, 17, 28, 98, 102, 151, 501, 56, 397, 652, 71, 199,
         218, 56, 16, 187]
obj1 = squareOddItem()
result = obj1.getOddItemsSquare(list3)
print(result)
