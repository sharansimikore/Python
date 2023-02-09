#This is extention of pr_04.py  repeat the pr_04.py for a list of such word to be censored


words = ["cat", "dog", "cow"]

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\demo.txt", "r") as f:
    content=f.read()

for word in words:
    content = content.replace(word, "###@@@###")

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\demo.txt", 'w') as f:
    f.write(content)
