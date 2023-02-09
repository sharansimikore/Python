# An Instance attributes that belongs to the Instance(object)  
# Note: Instance attribute take preference over class attributes during assignment and retreival
class Employee:
    salary = 100
    company = "JCI"


Rajni = Employee()
Sharan = Employee()
Priyanka = Employee()

print("Priyanka salary before changing attribute: ", Priyanka.company)
print(Priyanka.company)

#Creating instance attribute salary for Rajni
Priyanka.company = "Microsoft" #Changing class attribute
Priyanka.salary = 999
Rajni.salary = 500

print(Rajni.salary)
print(Sharan.salary)
print(Sharan.company)
print(Priyanka.salary)
print("Priyanka salary after changing attribute: ", Priyanka.company)
