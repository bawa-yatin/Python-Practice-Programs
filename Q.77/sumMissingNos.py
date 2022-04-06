# Create a function that returns the sum of missing numbers.
# sumMissingNumbers([1, 3, 5, 7, 10]) ➞ 29(2 + 4 + 6 + 8 + 9)

# User-defined function to return the sum of all missing numbers in the provided input
def missing_nos_sum(items):
    # list variable to hold all the missing numbers from the input provided
    missing_items = []

    for val in range(items[0], items[-1] + 1):
        if val not in list_1:
            missing_items.append(val)

    total = 0  # Variable holding the sum of all missing numbers
    for item in missing_items:
        total += item

    return total


list_1 = [1, 3, 5, 7, 10]  # Input List
result = missing_nos_sum(list_1)
print("Sum of missing numbers:", result)