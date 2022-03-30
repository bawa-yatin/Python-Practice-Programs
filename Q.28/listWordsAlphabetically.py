# Python Program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.

# Approach 1: Basic Approach using sort() function
data_items = ['Elle', 'Miles', 'Kratos', 'Joel', 'Peter', 'Nathan']
data_items.sort()
print(data_items)


# Approach 2: Using Function
def sortListItems(items):
    sorted_list = sorted(items)
    print(sorted_list)


fruit_items = ["Mango", "Apple", "Cherry", "Watermelon", "Grapes"]
sortListItems(fruit_items)


# Approach 3: Using Class
class itemsSort:
    def getSortedItems(self, list_items):
        items_sorted = sorted(list_items)
        return items_sorted


# Here words starting with uppercase letter will be given more preference
data = ['Elle', 'miles', 'kratos', 'Joel', 'peter', 'Nathan']
obj1 = itemsSort()
res = obj1.getSortedItems(data)
print(res)