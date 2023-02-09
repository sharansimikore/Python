# A Class method is a method which is bound to the class and not the object of the class 


class Employee:
    salary = 100  #Class attribute 
    company = "Tesla"

    # def getSalary(self, sal):
    #     self.__class__.salary= sal #tender class
    #     self.salary = sal   #Instance attribute

#This method is used to change the class attribute value(salary)   
    @classmethod
    def getSalary(cs, sal):
        cs.salary= sal #tender class    

e= Employee()
print(e.salary)
e.getSalary(455)
print(e.salary)
print(Employee.salary)