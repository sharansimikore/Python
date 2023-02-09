#WAP to read the text from given file "test.txt" and find out whether it conatins the word "sharan"

f = open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\test.txt", 'r')
d = f.read()
if "sharan" in d:
    print("Yes Sharan is present")
else:
    print("No Sharan is not present")


f.close()
