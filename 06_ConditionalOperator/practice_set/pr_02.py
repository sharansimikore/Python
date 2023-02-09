#Student pass or fail, average should be 40 and 33 marks
#in each subject


s1 = int(input("Enter marks of s1"))
s2 = int(input("Enter marks of s2"))
s3 = int(input("Enter marks of s3"))

sum = (s1+s2+s3)/3

if(s1 <33 or s2<33 or s3<33):
    print("You are fail")
elif(sum<40):
    print("You are fail")
else:
    print("You are Pass")        