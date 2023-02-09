'''
PasacalCase
EmployeeName -->PasacalCase

camelCase
isNumeric, isFloat --> camelCase

'''

class Employee:
    company = "Google"

    # def __init__(self):
    #     print("This is a constructor")

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = 100
        self.subunit = subunit
        print("This is a Constructor with parameters")        

    def getDetails(self):
        print(f"Name of the company is {self.company} and salary is {self.salary}")    
        print(f"Subunit of employee is {self.subunit}")

    def getsalary(self, signature):
        print(f"Salary of Sharan is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("This is a tatic function without self parameter\n")

    @staticmethod
    def time():
        print(f"This is 10AM in the morning")    


# sharan=Employee() #This throws an error (missing 3 required positional arguments:)
sharan= Employee("Kavita", 100, "YouTube")
sharan.getDetails()
