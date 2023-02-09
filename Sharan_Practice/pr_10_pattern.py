#Program----1

def pattern(n):
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print("")    
pattern(5)        

#Program----2


# n= int(input("Enter number:\n"))
# for i in range(n):
#     print("*" * (i*2))

#Program----3

for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")

    for k in range(i):
        print("*", end="")
    print("")
