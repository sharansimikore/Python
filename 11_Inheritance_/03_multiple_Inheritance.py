#Multiple inheritance occurs when the child class inherits from more than one parent class


# class Freelancer:
#     level = 0
#     company = "JCI"

#     def upgradelevel(self):
#         self.level = self.level + 1

# class Employee:
#     comapany = "Volansys"

# class Programmer(Freelancer, Employee):
#         name = "Sharan"

# p = Programmer()        
# print(p.comapany)
# p.upgradelevel() 
# print(p.level)


class Mother:
    company = "JCI"

class Father:
    company = "JCI-Rupee"

class Child(Father, Mother):  #SInce Father is called first do "JCI-Rupee will print"
    name ="good"

c = Child()
print(c.company)