#Write a class calculator capable of finding square, cube and squareroot of a number

class calculator:
    number = 2 

    def __init__(self, num) :
        self.number=num

    def sqaure(self):
        print(f"Square of {self.number} is: {self.number **2}\n")
       
    def cube(self):
        print(f"Cube of {self.number} is {self.number **3}\n")

    def squareroot(self):
        print(f"squareroot of {self.number} is {self.number **0.5}\n")

a = calculator(4)
a.sqaure()    
a.cube()    
a.squareroot()


