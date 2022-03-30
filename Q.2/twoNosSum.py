# Python program to return sum of two numbers

# Approach 1

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

nosSum = num_1 + num_2
print("Sum of numbers is:", nosSum)


# Approach 2: Using Function

def addNos(num1, num2):
    print("\nUsing Functions")
    return f'Sum of Numbers is: {num1 + num2}'


result = addNos(12, 9)
print(result)


# Approach 3: Using Classes and objects

class calcSumofNos:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def nosAdd(self):
        print("\nUsing Classes")
        return f'Sum of numbers is {self.val1 + self.val2}'


cs1 = calcSumofNos(4, 13)
res1 = cs1.nosAdd()
print(res1)