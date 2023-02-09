#WAP to calculate the grade of a student from his marks from
# the following scheme
#90-100-> Ext, 80-90-> A, 70-80-> B, 60-70->C, 
# 50-60->D, 40-50->E, 30-40->F

marks = int(input("Enter marks of student\n"))

if(marks>=90 and marks<=100):
    print("Ext")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks>=50 and marks<60):
    print("D")
elif(marks>=40 and marks<50):
    print("E")
else:
    print("Fail")