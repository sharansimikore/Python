# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizz_buzz(50)

def number(n):
    for i in range(1, n+1):
        # print("n=:", i)
        i+=1
        if(i%2 ==0):
            print("EVEN")
        elif(i%3 == 0):
            print("ODD")
        else:
            print("NONE")        

number(10)
