# Python Program to find the difference between the biggest and smallest numbers
# of a list

# Approach 1: Using for loop inside a method defined in a class
class maxMinDiff:
    def diffLargeSmall(self, list2):
        large_element = list2[0]
        small_element = list2[0]

        for i in range(len(list2)):
            if list2[i] > large_element:
                large_element = list2[i]
            elif list2[i] < small_element:
                small_element = list2[i]
        nos_diff = large_element - small_element
        return f"Difference between {large_element} and {small_element} is {nos_diff}"


list_2 = [17, 7, 54, 26, 41, 13]
md = maxMinDiff()
print(md.diffLargeSmall(list_2))

# Approach 2: Sorting the list in ascending order and accessing the first and last
# element in the list to find out the difference.
list_elements = [10, 3, 21, 53, 18, 9]
list_elements.sort()
diffNos = list_elements[-1] - list_elements[0]
print("Difference is", diffNos)


# Approach 3: Using built-in function min() and max()
def largeSmallDiff(list1):
    largest_ele = max(list1)
    smallest_ele = min(list1)
    result = largest_ele - smallest_ele
    return f"Difference between {largest_ele} and {smallest_ele} is {result}"


list_1 = [8, 21, 11, 32, 5, 93, 57, 48]
print(largeSmallDiff(list_1))
