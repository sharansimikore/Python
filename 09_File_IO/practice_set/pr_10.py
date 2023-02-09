#WAP to rename a file to "renamed_file_by_python.txt"

import os

oldfile="D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\old.txt"
newfile="D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\new_python_file.txt"

with open(oldfile, "r") as f:
    content = f.read()

with open(newfile, "w") as f:
    content = f.write(content)

os.remove(oldfile)