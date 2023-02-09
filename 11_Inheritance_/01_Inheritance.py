#Inheritance is the way of creating a new class from an existing class

class Employee():
    company = "Google"

    def showdetails(self):
        print("This is an employee")

class Company(Employee):
    language = "Python"
    # company = "JCI"

    def getlanguage(self):
        print(f"The language is {self.language}")

    def showdetails(self):
        print("This is an company(employee)")    

e=Employee()
# print(e.company)
print(e.showdetails())

c=Company()
print(c.language)
print(c.getlanguage())
print(c.company)

# print(c.showdetails())