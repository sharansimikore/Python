'''
Create a class Employee and add salary and increment property of it.
Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes 
the value of increment based on the salary 

'''

class Employee:
    salary = 100
    increment = 20

    #This is a function but intentds(acts) as a property and returns value, it is also called as getter function 
    @property
    def SalaryAfterIncrement(self):
        return self.salary + self.increment

#This is setter property where 2000 value is set
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, val):
        self.totalSalary2 =val + self.salary       


e = Employee()
print("increment", e.increment)
print("Total Salary", e.SalaryAfterIncrement)     
e.SalaryAfterIncrement = 200
print("salary after settin", e.totalSalary2)


 