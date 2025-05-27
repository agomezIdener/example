from multiply import multiply
from factorial import factorial
import hello
import goodmorning

class Operations:
    def __init__(self):
        self.a = 5
        self.b = 4
    def display(self):
        print(f"a = {self.a}, b = {self.b}")

    def subtract(self):
        return self.a - self.b

    def add(self):
        return self.a + self.b
    
    def multiply(self):
        return multiply(self.a, self.b)
    
    def factorial(self):
        return factorial(self.a)




print("Operations module loaded")
Operations().display()
print((Operations().add()))
print((Operations().subtract()))
print((Operations().multiply()))
print((Operations().factorial()))

hello.hello()
goodmorning.good()

print("Example test")