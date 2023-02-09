#Supermethod

class sharan:
    company = "JCI"

    def employer(self):
        print(f"Name of the company is: {self.company}")

class salary(sharan):
    salary = 100

    def paisa(self):
        print("***************Super Method***************")
        super().employer()
        print(f"The salary of an employee is: {self.salary}")
        print("************End of Super Method**************")


s = sharan()
s.employer()

p = salary()
p.paisa()