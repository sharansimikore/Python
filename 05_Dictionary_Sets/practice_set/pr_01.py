#WAP to create a dictonary  of hindi words with values as their english translation provide user with an option to look it up

myDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Items"
}

print("Options are", list(myDict.keys())) #prints only the Keys

a= input("Enter the hindi word\n")
print("the meaning of your word is:", myDict[a]) #If key is present in the dictonary then this (.get) method will not throw error
print("the meaning of your word is:", myDict.get(a)) #If key is not present in the dictonary then this (.get) method will throw error