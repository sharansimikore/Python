'''
WAP to print the following start pattern

*
* *       for n=3
* * *
'''

n= int(input("Enter number:\n"))
for i in range(n):
    print("*" * (i+1))
    