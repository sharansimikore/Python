myDict = {
    "name" : "Sharanbasappa",
    "LastName" : "SImikore",
    "Marks" : [45, 56, 67],
    1 : 2
}

#Dictonary methods
# print(myDict.keys())
print(list(myDict.keys())) #prints the key of a dictoanry
print(list(myDict.values())) #prints the value of a dictoanary
# print(myDict.values())
print(list(myDict.items())) #prints (key, value) of the dictonary

print(myDict)
updateDict = {
    "company" : "JCI",
    "role" : "QA Engineer",
    "Exp" : "5"
}
# print(updateDict)
myDict.update(updateDict) #update the dictonary by adding (key, value) pairs to the updateDict
print(myDict)


# print(myDict["Marks"])

print(myDict["name"]) #prints the value associated with key "name"
print(myDict.get("name")) #prints the value associated with key "name"

#The difference between the .get and [] syntax in dictonaries?
# print(myDict["name2"]) #throws an error as name2 is not present in the dictonary
# print(myDict.get("name2")) #Returs None as name2 is not present in the dictonary\
