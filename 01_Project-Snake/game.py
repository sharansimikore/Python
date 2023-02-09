#This is snake, water and gun game

import random
def gamewin(comp, you):
    if comp == you:
        None
    elif(comp == 's'):
        if(you == 'w'):
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if(you=='g'):
            return False
        elif(you=='s'):
            return True
    elif(comp == 'g'):
        if(you == 's'):
            return False
        else:
            return True





print("Comp turn : snake(s) water(w) gun(g)")
randNum = random.randint(1,3)
if randNum == 1:
    comp = 's'
elif randNum == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Enter your choice snake(s) water (w) gun(g)")        
a = gamewin(comp, you)

print(f"Your choice is {you}")
print(f"Comp choice is {comp}")

if(a == None):
    print("game is Tie!!")
elif(a == True):
    print("You Win!!!!!")
else:
    print("You lost!!!")        