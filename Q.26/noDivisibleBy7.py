# Python program to find all numbers which are divisible by 7 and not by 5

# Approach 1:
lower_limit = int(input("Enter a lower limit: "))
upper_limit = int(input("Enter a upper limit: "))
final_items = []

for i in range(lower_limit, upper_limit + 1):
    if i % 7 == 0 and i % 5 != 0:
        final_items.append(i)
print(final_items)


# Approach 2: Using Function
def eleDivBy7(start, end):
    return [j for j in range(start, end + 1) if j % 7 == 0 and j % 5 != 0]


start_val = int(input("Enter the starting value: "))
end_val = int(input("Enter the ending value: "))
res = eleDivBy7(start_val, end_val)
print(res)


# Approach 3: Using Class
class divisibleNum:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getNoDivisibleBy7(self):
        return [j for j in range(self.start, self.end + 1) if j % 7 == 0 and j % 5 != 0]


start_limit = int(input("Enter the starting limit: "))
end_limit = int(input("Enter the ending limit: "))
dn = divisibleNum(start_limit, end_limit)
result = dn.getNoDivisibleBy7()
print(result)
