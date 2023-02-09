'''
Can we change the self parameter inside a class to something else (say-sharan). Try changing self to sel, slf, sharan or
 anything and see the effect
'''

class sample:
    def __init__(sel, name, age) :
        sel.name = name
        sel.age = age

obj=sample("Sharan", 29)        
print(obj.name, obj.age)