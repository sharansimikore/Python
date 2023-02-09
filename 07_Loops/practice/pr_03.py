#WAP to find whethergiven number is prime or not

num = int(input("Enter a number: \n"))
prime = True

for i in range(2, num):
    if(num%i==0):
        prime = False
        break

if(prime):
    print("Number is prime")
else:
    print("Number is not prime")

