#n! = 1 * 2 * 3 * 4 * ....n
#n! = 1 * 2 * 3 * 4 *.....(n-1) * n
#n! = (n-1)! * n

#This is normal factorial function
n= 5 
fact = 1
for i in range(n):
    fact = fact * (i+1)
print("Factorial using normal ", fact)

#This is factorial using function
def fact(num):
     
    fact = 1
    for i in range(num):
        fact = fact * (i+1)
    return (fact)

#This is factorial using recursive function
def factrecursive(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * factrecursive(num-1)


f = fact(5)
r= factrecursive(5)
print("Factorial using function", f)
print("Factorial using recursive:", r)