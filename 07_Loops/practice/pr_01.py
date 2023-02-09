#WAP to print multiplication table of a given number using for loop

# i=1
num = int(input("enter a number:\n"))
 
for i in range(1,11):
    # print(str(num) + "X" + str(i) + "=" + str(num*i))
    #f string
    print(f"{num}X{i}={num*i}")
 