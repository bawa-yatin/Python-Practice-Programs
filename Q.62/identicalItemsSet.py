# Approach 1: Using intersection method

set_1 = {10, 25, 45, 55, 75}
set_2 = {15, 10, 96, 45, 25}
iden_items = set_1.intersection(set_2)
print(iden_items)

# Approach Two: Using nested loops

set_items = []
set_3 = {1, 3, 5, 7, 9}
set_4 = {2, 3, 5, 7, 11}
for i in set_3:
    for j in set_4:
        if i == j:
            set_items.append(j)
print(set(set_items))
