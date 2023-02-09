
class sharan:
    name = "Kaka"

    def my_name(self):
        print(f"My name is: {self.name}")


class rahul(sharan):
    salary = 100

    def salary_rahul(self):
        print("*******Super method start*************")
        super().my_name()
        print(f"Rahul's salary is: {self.salary}")

        print(f"My name is {self.name}") 
        if((self.name) == "Kaka"):
            print("Its a Kaka")
        else:
            print("Its a Baba")

        print("********Super method end ***************")

s = sharan()
s.my_name() 

r =rahul()
r.salary_rahul()
