#self is kind of parameter which passes automatically

class Employee:
    age = 30
#Throws an error    
    # def getexper(): 
    def getexper(self):
        print(f"Salary of an employee with {self.age} is {self.salary}")


sharan = Employee()
sharan.salary = 1000

sharan.getexper()
Employee.getexper(sharan)
