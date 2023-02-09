#Set is a collection of non repeatative element

a = {1, 4, 5}
print(a)

a.add(10)
a.add(7)
a.add(4)
a.add(4)

print(a) #As set does not add repeatative elements

#List is not hashable so it cannot be added in sets as contents of List can be changed(mutable)
# a.add([1,2,3])
# print(a)

#Dictonary is not hashable so it cannot be added in sets as contents of List can be changed(mutable)
# a.add({1,2})
# print(a)

#Tuples is hashable so it can be added in sets
a.add((11,12,13))
print(a)

#prints lenght of the set
print(len(a))

#removal of an item
a.remove(1) #removes 1 from set a
print(a)

# a.remove(20) #throw an error while removing as 20 is not present in the list
# print(a)

a.pop() # removes an arbitary elemet from the set and returns the element removed 
print(a)

a.clear() #Empties the set
print(a)

#union
#intersection