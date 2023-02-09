import random

num = random.randint(1, 50)
# print(num)
userguess = None
counts = 0

while(num !=userguess):
    
    userguess = int(input("Enter a number:"))
    counts+=1
    if(userguess>num):
        print("Enter smaller number")
    elif(userguess<num):
        print("Enter a greater number")
    else:
        print("Number matches the entry")       

print("You have guessed in: ", counts)        

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
    print("HighScore is: ", hiscore)

if(counts<hiscore):
    print("You have just broken the record!!")
    with open("hiscore.txt", "w") as f:
        f.write(str(counts))
