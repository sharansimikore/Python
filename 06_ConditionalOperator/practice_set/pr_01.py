#Find the greatest of 4 entered by user
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))
num4 = int(input("Enter num4"))

if (num1 > num4):
    f1 = num1
else:
    f1 = num4

if (num2 > num3):
    f2 = num2
else:
    f2 = num3

if (f1>f2):
    print("Greatest num is: ", f1)
else:
    print("Greatest num is: ", f2)    