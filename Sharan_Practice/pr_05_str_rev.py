#String reverve 

s = input("Enter a string:\n")
print("String is: ", s)

def reverse_string(s):
    return s[::-1]

r = reverse_string(s)
print(r)

# method-1------------------------------------------------

# def strposition(st):
#     for i in range(len(st)):
#         print("character '{}' is at index {}". format(st[i], i))

# st = "sharan"
# strposition(st)

# method-2 -------------------------------------------------

# st = input("Enter a string: ")

# def strposition(stri):
#     for i in range(len(st)):
#         print("character '{}' and its position is '{}' ".format(stri[i], i))

# strposition(st)        
