# Power Calculator

# Approach 1: Using exponent operator(**)
num_1 = 3
num_2 = 4

power_result = num_1 ** num_2
print(power_result)


# Approach 2- Using Function
def calc_power_num(base, exponent):
    return base ** exponent


res = calc_power_num(4, 3)  # Variable holding the response returned from
# the function "calc_power_num()"
print(res)


# Approach 3: Using class and in-built pow() function
# pow() function takes 2 parameters i.e. base and exponent

class numPower:
    def __init__(self, num_base, num_exponent):
        self.base = num_base
        self.exponent = num_exponent

    def no_power(self):
        return pow(self.base, self.exponent)


# Object creation of "numPower" class and simultaneously assigning the value to
# class variable(base, exponent) through constructor method
np = numPower(5, 3)
num_power = np.no_power()  # Variable holding the response returned from the
# class method "no_power()"
print(num_power)
