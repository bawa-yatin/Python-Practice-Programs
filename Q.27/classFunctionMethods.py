# Python Program to define a class/function which has at least two methods

# Approach 1: Using Function
def two_methods():
    def get_string():
        user_name = input("Enter user name: ")
        if user_name.isdigit():
            print("Invalid User Name!")
        else:
            print_string(user_name)

    def print_string(name):
        print("Name of user is:", name.upper())

    get_string()


two_methods()


# Approach 2: Using Class
class userInfo:
    def __init__(self):
        self.uname = None

    def get_string(self):
        self.uname = input("Enter a name: ")

    def print_string(self):
        if self.uname.isalpha():
            print("Name of user is:", self.uname.upper())
        else:
            print("Invalid User Name!")


ui = userInfo()
ui.get_string()
ui.print_string()