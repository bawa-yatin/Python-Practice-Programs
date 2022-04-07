# Python Program to sort the data in ascending and descending order

# Approach 1: Basic Approach
# Ascending sort
list1 = [87, 17, 11, 98, 21, 38]
len_list1 = len(list1)
for i in range(len_list1):
    for j in range(len_list1 - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print("Ascending Order", list1)

# Descending sort
for i in range(len_list1):
    for j in range(len_list1 - 1):
        if list1[j] < list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print("Descending Order", list1)


# Approach 2: Using Class and Function
class sortDataAscDesc:
    def __init__(self, items):
        self.items = items

    def ascending_sort(self):
        total_length = len(self.items)
        for i in range(total_length):
            for j in range(total_length - i - 1):
                if self.items[j] > self.items[j + 1]:
                    self.items[j], self.items[j + 1] = self.items[j + 1], self.items[j]

        return self.items

    def descending_sort(self):
        total_length = len(self.items)
        for i in range(total_length):
            for j in range(total_length - i - 1):
                if self.items[j] < self.items[j + 1]:
                    self.items[j], self.items[j + 1] = self.items[j + 1], self.items[j]

        return self.items


list2 = [25, 15, 45, 75, 35, 86, 65]
sd = sortDataAscDesc(list2)  # Creating object of class "sortDataAscDesc"
print(sd.ascending_sort())  # Using class object to access class method "ascending_sort()"
print(sd.descending_sort()) # Using class object to access class method "descending_sort()"

# Approach 3: Using sort() and sorted() methods
list3 = [17, 79, 56, 12, 51, 45]
list4 = [56, 75, 89, 12, 21, 99, 101]
list3.sort()
print("Ascending Order:", list3)

new_list = sorted(list4, reverse=True)
print("Descending Order", new_list)