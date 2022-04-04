# Python Program to define a class/function which has at least two methods

# Approach 1: Using Function
def twoMethods():
    def getString():
        user_name = input("Enter user name: ")
        if user_name.isalpha():
            printString(user_name)
        else:
            print("Invalid User Name!")

    def printString(name):
        print("Name of user is:", name.upper())

    getString()


twoMethods()


# Approach 2: Using Class
class userInfo:
    def __init__(self):
        self.uname = None

    def getString(self):
        self.uname = input("Enter a name: ")

    def printString(self):
        if self.uname.isalpha():
            print("Name of user is:", self.uname.upper())
        else:
            print("Invalid User Name!")


ui = userInfo()
ui.getString()
ui.printString()