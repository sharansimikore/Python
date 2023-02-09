#Add a static method in problem 2 to greet a user with "Hello"

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

    @staticmethod
    def greet():
        print("Hello, This is a static method which does not contain self")    


a = calculator(4)
a.greet()
a.sqaure()    
a.cube()    
a.squareroot()