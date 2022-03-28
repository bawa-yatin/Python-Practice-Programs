numList = [11, 43, 23, 77, 51, 78]

# Approach 1: By simply providing index of first element in square brackets
print("First element is", numList[0])

# Approach 2: By using slicing syntax, where slicing starts at 0th index and ends at index 1
firstElement = numList[:1]
print("First element is", firstElement)

# Approach 3: Using list comprehension
first = 0
res = [numList[i] for i in range(len(numList)) if i == first]
print("First element of list is", res)

# Approach 4: Using For Loop
for i in range(len(numList)):
    if i == first:
        print("First element of list is", numList[i])
