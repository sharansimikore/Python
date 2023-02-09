#Maximum number of 3

def maximum(n1, n2, n3):
    if(n1 > n2) and (n1 > n3):  
        return n1
    elif(n2 > n3):
        return n2
    else:
        return n3            

max = maximum(112, 500, 1900)
print("Maximum number is: ", max)