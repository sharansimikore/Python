class number:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        print("In SUM Function")
        return self.num1 + num2.num1

    def __str__(self):
        return f"number is {self.num1}"    

    def __len__(self):
        return 5    

n1 = number(2)
print(n1)
print(len(n1))