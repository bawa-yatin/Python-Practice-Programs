# Approach 1
num_1 = 3
num_2 = 4

power_result = num_1 ** num_2
print(power_result)


# Approach 2- Using Function
def calcPowerNum(base, exponent):
    return base ** exponent


res = calcPowerNum(4, 3)
print(res)


# Approach 3: Using class and in-built pow() function
# pow() function takes 2 parameters i.e. base and exponent

class numPower:
    def __init__(self, num_base, num_exponent):
        self.base = num_base
        self.exponent = num_exponent

    def noPower(self):
        return pow(self.base, self.exponent)


np = numPower(5, 3)
num_power = np.noPower()
print(num_power)
