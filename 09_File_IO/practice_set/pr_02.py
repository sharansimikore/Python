def game():
    return 199

score = game()
with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\hiscore.txt") as f:
    hiscore = (f.read())
    # print("Hiscore is:", hiscore)
    # print("Score is: ", score)

    if hiscore == '':
        with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\hiscore.txt", 'w') as f:
            f.write(str(score))
            
    if int(hiscore) < score:
        print("Score is greater", score)
        with open("D:\\PythonCoursewithNotes\\1.Chapter1\\09_File_IO\\practice_set\\hiscore.txt", 'w') as f:
            f.write(str(score))
    
