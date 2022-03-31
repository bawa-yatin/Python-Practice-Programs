class MathOperations:
    def __init__(self):
        self.val_1 = int(input("Enter first value: "))
        self.val_2 = int(input("Enter second value: "))

    def addition(self):
        return self.val_1 + self.val_2

    def subtract(self):
        return self.val_1 - self.val_2

    def multiply(self):
        return self.val_1 * self.val_2

    def divide(self):
        return self.val_1 / self.val_2

    def modulus(self):
        return self.val_1 % self.val_2

    def floor_division(self):
        return self.val_1 // self.val_2

    def exponent(self):
        return pow(self.val_1, self.val_2)


obj1 = MathOperations()
print("Sum is", obj1.addition())
print("Difference is", obj1.subtract())
print("Product is", obj1.multiply())
print("Division is", obj1.divide())
print("Modulus is", obj1.modulus())
print("Floor Division is", obj1.floor_division())
print("Exponent is", obj1.exponent())