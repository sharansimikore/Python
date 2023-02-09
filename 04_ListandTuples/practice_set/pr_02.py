#Aaccept marks of the student and display in sorted manner

l1 = int(input("Enter marks of student 1: "))
l2 = int(input("Enter marks of student 2: "))
l3 = int(input("Enter marks of student 3: "))
l4 = int(input("Enter marks of student 4: "))
l5 = int(input("Enter marks of student 5: "))
l6 = int(input("Enter marks of student 6: "))

studentMarks = [l1, l2, l3, l4, l5, l6]
print(studentMarks)
studentMarks.sort() #Sorting elements
print(studentMarks)
