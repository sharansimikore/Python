#WAP to find out the line number where python is present from question pr_05.py

content=True
i=1

with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\log.txt", 'r') as f:
    while content:
        content = f.readline()
     

        if "python" in content.lower():
            print(content)
            print(f"Yes Python is present at :{i}")
        i=i+1
        
    