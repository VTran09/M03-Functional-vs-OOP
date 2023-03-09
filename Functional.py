class do_math:
    def __init__ (self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    def add(self):
        return self.val1 + self.val2
    
    def multiply(self):
        return self.val1 * self.val2
    
    def substract(self):
        return self.val1 - self.val2
    
    def divide(self):
        return self.val1 / self.val2
    
math_instance = do_math(10,6)
print("Addition of two numbers:", math_instance.add())
print("Substraction of two numbers:", math_instance.substract())
print("Multiplication of two numbers:", math_instance.multiply())
print("Division of two numbers:", round(math_instance.divide(), 2))