#1. Dictonary is unordered
#2. It is mutable meaning values can be changed
#3. Key cannot be duplicate
#4. It is indexed

myDict = {
    "name" : "Sharan",
    "Ages" : [12, 22, 33] #list
}

print(myDict["name"])
print(myDict["Ages"])

#Changing the values of Ages
myDict["Ages"] = {10, 20}
print(myDict["Ages"])