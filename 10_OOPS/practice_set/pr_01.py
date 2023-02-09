#Create a class programmer for storing information of few programmers working at microsoft

#1. Method
class programmer:
    company = "Microsoft"

    def __init__(self,name, salary, project):
        print("This will print the details\n")
        self.name = name
        self.salary = salary
        self.project = project
        

    def details(self):
        print(f"Name of the Employee is {self.name}\n")
        print(f"Salary of an {self.name} is {self.salary}\n")
        print(f"Project of {self.name} is {self.project}\n")

sharan = programmer("Meghana", 500, "ELO")
Rocky = programmer("Priya", 600, "GitHub")
sharan.details()        
Rocky.details()