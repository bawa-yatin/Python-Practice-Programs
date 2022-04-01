initial_list = [['George', 'Mary'], ['Peter', 'Harry']]
sub_list = ['Smith', 'Paul']
index_pos = int(input("Enter the position where you want to add the sublist: "))

print("Original List:", initial_list)
initial_list.insert(index_pos, sub_list)
print("After modification", initial_list)