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




print("Operations module loaded")
Operations().display()