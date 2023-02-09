'''
WAP to generate multiplication tables from 2 to 20 and write it to the different files. 
Place these files in a folder for a 13 year old  

'''

for i in range(2, 21):
    with open(f"D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\tables/multiplication_of_{i}.txt", 'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")
