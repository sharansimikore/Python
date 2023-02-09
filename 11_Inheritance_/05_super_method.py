#Super method is used to access the methods of super class in the derived class

class person:
    country = "Australia"

    def takebreath(self):
        print("Person is breathing...")

class Employee(person):
    company = "Jacobs & Co"

    def takebreath(self):
        super().takebreath()
        print("Employee gets higher salary so he is breathing")     

class Programmer(Employee):
    project = "ELO_AIBoat"

    def takebreath(self):
        super().takebreath()
        print("Programmer: This is breathing inside Programmer")

              
P = person()
P.takebreath()

E = Employee()
E.takebreath()

Pr = Programmer()
Pr.takebreath()