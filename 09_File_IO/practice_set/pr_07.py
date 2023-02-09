#WAP to copy the text file "this.txt" 

#This program copies content of this.txt -> copy.txt 

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\this.txt",'r') as f:
    content = f.read()

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\copy.txt", 'w') as f:
    f.write(content)