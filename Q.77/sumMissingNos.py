def missing_nos_sum(items):
    missing_items = []
    for val in range(items[0], items[-1] + 1):
        if val not in list_1:
            missing_items.append(val)

    total = 0
    for item in missing_items:
        total += item

    return total


list_1 = [1, 3, 5, 7, 10]
result = missing_nos_sum(list_1)
print("Sum of missing numbers:", result)