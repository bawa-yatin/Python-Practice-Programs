# Python Program to return the next number from the integer passed

# Approach 1
num_1 = int(input("Enter a number: "))
if num_1 >= 0:
    num_1 += 1
else:
    print("Please enter a valid number")

print("Next number in the sequence is", num_1)


# Approach 2: Using Functions
def nextNumber(num1):
    if num1 >= 0:
        result = num1 + 1
        return result
    else:
        return "Please enter a valid number"


res = nextNumber(9)
print("\nUsing Functions")
print("Next number is", res)


# Approach 3: Using class and objects

class nextNo:
    def __init__(self, val1):
        self.val1 = val1

    def sequenceNextNo(self):
        if self.val1 >= 0:
            result = self.val1 + 1
            return result
        else:
            return "Please enter a valid number"


n1 = nextNo(61)
res1 = n1.sequenceNextNo()

print("\nUsing Classes")
print("Next number is", res1)