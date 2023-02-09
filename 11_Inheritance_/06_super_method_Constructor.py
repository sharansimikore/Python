#Super method with Constructor

class person:
    country = "Australia"

    def __init__(self):
       print("Super Constuctor in Person ")

    def takebreath(self):
        print("Person is breathing...")

class Employee(person):
    company = "Jacobs & Co"

    def __init__(self):
        super().__init__()
        print("Super constuctor in Employee")

    def takebreath(self):
        super().takebreath()
        print("Employee gets higher salary so he is breathing")     

class Programmer(Employee):
    project = "ELO_AIBoat"

    def __init__(self):
        super().__init__()
        print("Super Constructor in Programmer")

    def takebreath(self):
        super().takebreath()
        print("Programmer: This is breathing inside Programmer")

              
# P = person()
# P.takebreath()

# E = Employee()
# E.takebreath()

Pr = Programmer()
# Pr.takebreath()