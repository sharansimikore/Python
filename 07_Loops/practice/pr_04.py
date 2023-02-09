#WAP to calculate the factorial of a given number by using for loop

fact=1
num = int(input("Enter a number:\n"))
for i in range(1, num+1):
    fact=fact*i
print(f"fact of {num} is {fact}")    