# Python program to check if an integer is completely divisible by 5 or not

# Approach 1: Using Function

def check_divisible():
    try:
        num_1 = int(input("Enter any positive number: "))
        if num_1 < 0:
            print("Invalid Value")
        else:
            if num_1 % 5 == 0:
                return True
            else:
                return False
    except ValueError:
        print("Provide numeric value only!")


result = check_divisible()
if result is not None:
    print(result)


# Approach 2: Using Class
class divCheck:
    def __init__(self, value):
        self.value = value

    def num_divisible(self):
        if self.value < 0:
            print("Invalid Value")
        else:
            if self.value % 5 == 0:
                return True
            else:
                return False


dc = divCheck(37)
res = dc.num_divisible()
if res is not None:
    print(res)
