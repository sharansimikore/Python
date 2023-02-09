#with file statement no need to close this file
with open("sample.txt", 'r') as f:
    a=f.read()
with open("sample.txt", 'w') as f:
    a = f.write("I am DON and I will be")
print(a)    