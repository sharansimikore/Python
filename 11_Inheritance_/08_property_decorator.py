class Employee:
    salary = 1200
    salBonus = 200


#This is a function but intentds(acts) as a property and returns value, it is also called as getter function 
    @property
    def totalSal(self):
        return self.salary + self.salBonus

#This is setter property where 2000 value is set
    @totalSal.setter
    def totalSal(self, val):
        self.salBonus = val - self.salary     

e = Employee()
print(e.totalSal)     
e.totalSal = 2000   
print(e.salary)
print(e.salBonus)
