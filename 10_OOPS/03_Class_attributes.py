#An attribute that belongs to the class rather than a perticular an object

#eg.1

class Employee:
    company = "Microsoft"
    salary = 200
    exp = "10"

sharan = Employee()
Bhakti = Employee()

sharan.company = "Google" #Instance attribute
Employee.company = "Delloite" #Class attribute 

print(sharan.company, sharan.salary)
print(Bhakti.company, Bhakti.salary)
print(sharan.exp)
print("*******************")

#eg. 2

class Employee:
    company = "Google"  #specified to each class 

kavita = Employee()    #object installation
sharan.company 
kavita.company = "Tesla" 
Employee.company = "Meta" #Changing class attribute

print(Employee.company)
print(sharan.company)
print(kavita.company)

#Below line throws an error as address is not present in instance/class 
# print(sharan.address)