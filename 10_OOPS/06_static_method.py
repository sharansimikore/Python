#sometimes we does need a function that does not use the self parameter. We can define a static method
import time

class Employee:
    sharan = 30

    def getsalary(self, signature):
        print(f"Salary of Sharan is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("This is a tatic function without self parameter\n")

    @staticmethod
    def time():
        print(f"This is 9AM in the morning")    

sharan = Employee()
sharan.salary = 1000
print(sharan.salary)
sharan.getsalary("Thanks!")

sharan.greet()        
sharan.time()

