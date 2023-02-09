class person:
    country = "Australia"
    def takebreath(self):
        print("Person is breathing...")

class Employee(person):
    company = "Jacobs & Co"
    country = "USA"
    salary = 100

    def getsalary(self):
        print(f"Salary of Jacobs & Co employee is {self.salary}")     

    def takebreath(self):
        print("This employee gets higher salary so he is breathing")     

class Programmer(Employee):
    project = "ELO_AIBoat"

    def takebreath(self):
        print("This is breathing inside Programmer")

              
P = person()
P.takebreath()
# print(P.salary) # This throws an error since salary attribute is defined in class person

E = Employee()
E.getsalary()
E.takebreath()

Pr = Programmer()
print("Company:", Pr.company)
print("Contry: ", Pr.country)
Pr.takebreath()