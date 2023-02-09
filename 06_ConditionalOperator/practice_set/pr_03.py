#WAP to find whether a given username contains less than 
# 10 character or not

username = input("Enter a username: ")

l = len(username)
print(l)
if(l<10):
    print("Yes username contains less than 10 chars")
else:
    print("username does not contain")    
