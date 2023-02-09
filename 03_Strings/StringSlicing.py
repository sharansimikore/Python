a = "Python"
b = "Learning"
c=a+b

#String concatenating
print("String is",a+b) 
print(c)

#String Slicing
print(c[0])
print(c[1])
print(c[5])
# c[5] = 's' ---> does not support we cannot replace 'n' with 's'
print(c[0:3])
print(c[1:7])
print(c[:5]) #This is same as c[0:5]
print(c[:])
print(c[0:])
print(a[-6]) #Negative index starts from right(-1) and positive index start from left(0)
print(a[-1]) #Negative index starts from right(-1) and positive index start from left(0) 

#String Lenght
print(len(a))