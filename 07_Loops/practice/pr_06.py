'''
WAP to print the following start pattern

   *
 * * *       n=3
* * * * 

'''

n = int(input("Enter a number:\n"))
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))

    

          