'''
Create a class with a class attribute a; create an object from it and set a directly using object a=0. 
Does this change the class attribute?  
'''

class sample:
    a = "Python"

obj = sample()
obj.a = "C++"  #This is an instance attribute and creates new object and does not change class attribute 
sample.a = "New" #This changes the class attribute
print("Class attribute is: ", sample.a)
print("New instance attribute assigned for a is : ", obj.a)    

