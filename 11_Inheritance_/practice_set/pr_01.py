# #Create a class C2-dvector and use it to create another class representing a 3-d vector
#This is incomplte program

class C2DVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
        

class C3DVector(C2DVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str_(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

C2D = C2DVector(1,2)
C3D = C3DVector(1,5,9)
print(C2D)
print(C3D)

