'''
A file contains a word "donkey" multiple times you need to replace this word with "######" by updating the same file

'''

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\demo.txt", "r") as f:
    content=f.read()

content = content.replace("donkey", "###@@@###")

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\demo.txt", 'w') as f:
    f.write(content)
