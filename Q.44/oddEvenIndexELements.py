list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
odd_list = []
even_list = []

for i in range(1, len(list1), 2):
    odd_list.append(list1[i])
print("Odd Index Elements:", odd_list)

for j in range(0, len(list2), 2):
    even_list.append(list2[j])
print("Even Index Elements:", even_list)

print("After getting odd and even index elements:", odd_list + even_list)
