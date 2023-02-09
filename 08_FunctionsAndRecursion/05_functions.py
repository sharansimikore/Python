#Average of marks of a student

# marks = [56, 76, 79, 91]
# per = (sum(marks)/400)*100

# marks1 = [66, 86, 79, 91]
# per1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100
# print(per, per1)

def funper(mark):
    pert = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100
    return pert

def fun2(marks):
    p2 = (sum(marks)/400)*100
    return p2

marks1 = [66, 86, 79, 91]
per1=funper(marks1)
print(per1)

marks2=[89, 99, 91, 92]
per2=fun2(marks2)
print(per2)