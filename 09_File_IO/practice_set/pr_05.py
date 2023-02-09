#WAP to mine a log file and find whether it contains python

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\log.txt", 'r') as f:
    content = f.read()


if "python" in content.lower(): #As Python (P) is present in log.txt
    print("Yes Python is present")
else:
    print("No pythin is not present")