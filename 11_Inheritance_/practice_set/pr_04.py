#Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them

'''
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return complex(self.real+c.real, self.imaginary+c.imaginary)

    def __mul__(self, c):
        return complex(self.real*c.real, self.imaginary*c.imaginary)

a = Complex(1,2)
a2 = Complex(2,4)
# a+a2
print("Adding of two complex nubers", a+a2)
print("Multiplication of two is: ", a*a2)

'''

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1=Complex(3, 2)
c2=Complex(1, 7)
print(c1+c2)
print(c1*c2)


'''
class complex:
    num1 = 1
    num2 = 2

    def __add__(self, num1, num2):
        return f"{self.num1} + {self.num1}"

    def __mul__(self, num1, num2):
        return f"{self.num1} * {self.num1}"    

n1 = 3
n2 = 2
summ = n1 + n2
print(summ)

mult= n1 * n2
print(mult)
'''