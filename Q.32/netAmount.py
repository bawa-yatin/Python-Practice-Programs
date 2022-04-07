
# Python program that computes the net amount of a bank account based on a transaction
# log from console input.
# Log format is :  D 100 W 200

# Approach 1
trans_log = input("Enter the transaction log: ")
# Splitting the transaction log in the input string into a list
items = trans_log.split(" ")
amount = 0  # variable to keep track of the amount present in the bank
for i in range(len(items)):
    if items[i] == 'D':
        amount += int(items[i + 1])
    elif items[i] == 'W':
        amount -= int(items[i + 1])

print("Total Amount is", amount)


# Approach 2: Using Function
def calc_amount(ele):
    amt = 0  # variable to keep track of the amount present in the bank
    for j in range(len(ele)):
        if ele[j] == 'D':
            amt += int(ele[j + 1])
        elif ele[j] == 'W':
            amt -= int(ele[j + 1])

    return amt


trans_log_2 = input("Enter the transaction log: ")
# Splitting the transaction log in the input string into a list
item = trans_log_2.split(" ")
obj1 = calc_amount(item)  # Variable holding the response returned from the function
# after calculating the total amount
print("Total Amount is", obj1)


# Approach 3: Using Class
class countAmt:
    def __init__(self, log):
        self.log = log

    def get_amt(self):
        amt = 0  # variable to keep track of the amount present in the bank
        for j in range(len(self.log)):
            if self.log[j] == 'D':
                amt += int(self.log[j + 1])
            elif self.log[j] == 'W':
                amt -= int(self.log[j + 1])
        return amt


trans_log_3 = input("Enter the transaction log: ")
# Splitting the transaction log in the input string into a list
item2 = trans_log_3.split(" ")

ca = countAmt(item2)  # Object creation of class "countAmt"
obj2 = ca.get_amt()  # Variable holding the response returned from the class method
# after calculating the total amount
print("Total Amount is", obj2)
