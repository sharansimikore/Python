# #User Open function to read the content of a file !!!

f = open('sample.txt', 'r')
# data=f.read()
data =  f.read(5)  #Prints 5 characters
print(data)
f.close()

f = open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\demofile.txt", "r")
print(f.read())
f.close

#By default open in read mode(r)
f = open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\demofile.txt")
print(f.read())
f.close
