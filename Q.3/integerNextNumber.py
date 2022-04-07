# Python Program to return the next number from the integer passed

# Approach 1

# Using try-except block to verify whether the input provided is in numeric form or not
try:
    num_1 = int(input("Enter a number: "))
    # Condition to check if number provided is greater than or equal to 0 or not
    if num_1 >= 0:
        num_1 += 1
        print("Next number in the sequence is", num_1)
    else:
        print("Please enter a valid number")
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Functions
def next_number(num1):
    if num1 >= 0:
        result = num1 + 1
        return result
    else:
        return "Please enter a valid number"


# Calling the user-defined function defined above to return the next number after
# the integer passed and storing it in variable "res"
res = next_number(9)  # Variable holding the response returned from the function
print("\nUsing Functions")
print("Next number is", res)


# Approach 3: Using class and objects

class nextNo:
    def __init__(self, val1):
        self.val1 = val1

    def sequence_next_no(self):
        if self.val1 >= 0:
            result = self.val1 + 1
            return result
        else:
            return "Please enter a valid number"


# Object creation of "nextNo" class and simultaneously assigning the value to
# class variable(val1) through constructor method
n1 = nextNo(61)
res1 = n1.sequence_next_no()  # Variable holding the response returned from the function

print("\nUsing Classes")
print("Next number is", res1)
