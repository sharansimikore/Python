#WAP to find out whether a file is identical and matches the content of another file  copy.txt and this.txt

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\this.txt", 'r') as f:
    f1 = f.read()

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\copy.txt", 'r') as f:
    f2 = f.read()

if f1 == f2:
    print("Two files are identical")
else:
    print("Files are not identical")    
