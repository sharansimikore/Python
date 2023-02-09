#Write __str__ to print the vector as follows 1i+2j+3k . Assume a vector should be 3D

class Vector:

    def __init__(self, vec):
        self.vec = vec 

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = Vector([1,2,3])
v2 = Vector([4, 5, 6])

print(v1) 
print(v2)       
            
        
