'''
Operators in python can be overloaded using dunder method.
These method are called when given operator is used on the objects
Two overload operators using dunder method following operators are used:
n1 / n2 : __truediv__
n1 // n2 : __floordiv__

'''

class number:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        print("***Adding two numbers*********")
        return self.num1 + num2.num1

    def __sub__(self, num2):
        print("*****Subtraction of two numbers ******")
        return self.num1 - num2.num1

    def __mul__(self, num2):
        print("****Multiplication of two numbers****")
        return self.num1 * num2.num1    

n1 = number(10)
n2 = number(5)

sum = n1 + n2
sub = n1-n2
mul = n1 * n2

print("Addition of twp numbers is: ", sum)
print("Subtraction of two number is: ", sub)
print("Multiplication of two numbers is: ", mul)
        