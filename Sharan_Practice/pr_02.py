class company:
    c_name = "Microsoft"

    def company_details(self):
            print("inside company details function")
         
        
class employee(company):
        name = "Sharan"
        
        def show_employee(self):
            print("This is inside show_employee method")

class increment(employee):
        bonus = 10

        def Inc(self):
            return print(f"Bonus os an employee is {self.bonus}") 
            

class salary(increment):
    salary = 200
    
    def total_salary(self):
        self.total = self.salary + self.bonus
        print(f"**********************************************************")
        print(f"company name is {self.c_name} ")
        print(f"Name of the employee is: {self.name}")
        print(f"salary of an employee is: {self.salary}")
        print(f"Bonus of an employee is: {self.bonus}")
        print(f"Total salary of an employee including bonus is: {self.total}")
        print("************************************************************")
             

c = company()
print(c.company_details())

e = employee()
print(e.company_details())
print(e.show_employee())

i = increment()
print(i.Inc())

s = salary()
print(s.total_salary())

