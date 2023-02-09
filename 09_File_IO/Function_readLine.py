f = open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\demofile.txt", "r")
#read first line
data = f.readline()
print(data)

#read second line
data = f.readline()
print(data)

#read third line
data = f.readline()
print(data)
f.close