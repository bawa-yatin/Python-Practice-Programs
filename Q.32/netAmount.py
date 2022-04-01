# Approach 1

trans_log = input("Enter the transaction log: ")
items = trans_log.split(" ")
amount = 0
for i in range(len(items)):
    if items[i] == 'D':
        amount += int(items[i + 1])
    elif items[i] == 'W':
        amount -= int(items[i + 1])

print("Total Amount is", amount)


# Approach 2: Using Function
def calcAmount(ele):
    amt = 0
    for j in range(len(ele)):
        if ele[j] == 'D':
            amt += int(ele[j + 1])
        elif ele[j] == 'W':
            amt -= int(ele[j + 1])

    return amt


trans_log_2 = input("Enter the transaction log: ")
item = trans_log_2.split(" ")
obj1 = calcAmount(item)
print("Total Amount is", obj1)


# Approach 3: Using Class
class countAmt:
    def __init__(self, log):
        self.log = log

    def getAmt(self):
        amt = 0
        for j in range(len(self.log)):
            if self.log[j] == 'D':
                amt += int(self.log[j + 1])
            elif self.log[j] == 'W':
                amt -= int(self.log[j + 1])
        return amt


trans_log_3 = input("Enter the transaction log: ")
item2 = trans_log_3.split(" ")

ca = countAmt(item2)
obj2 = ca.getAmt()
print("Total Amount is", obj2)
