class marks():
    
    def total(self, m1, m2, m3):
        t = m1 + m2 + m3
        print("Inside total:", t)
        if(t>0):
            print(f"{t} is positive number")
        else:
            print("f{t} is negetive number")  

    def character(self, c1):
        if((c1>='a') & (c1<='z')):
            print(f"{c1} is LowerCase")
        elif((c1 >='A') & (c1<='Z')):
            print(f"{c1} is UpperCase")
        # elif((c1 >= int(0)) & (c1 <= int(9))):
        #     print(f"{c1} is a number")    
        else:
            print(f"{c1} is special character")

class average(marks):

    def calculation(self):
        print("********START OF SUPER METHOD***********")
        super().character('a')
        print("This is inside calculation method")
        print(f"The number is")
        print("********END OF SUPER METHOD***********")

m = marks()
m.total(1, 2, 3)
m.character('B')

a = average()
a.calculation()