n = 0

def multiply(n):
    for i in range(0, 10):
        print("Number is: ", n)
        n+= 1
        if(n%2 == 0):
            print(f"{n} is even")
        else:
            print(f"{n} is Odd")    



r = multiply(n)