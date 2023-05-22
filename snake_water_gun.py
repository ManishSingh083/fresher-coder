# importing modules
import random

# Logic of game winning
def gameWin(comp, you):
    if(comp == you):
        return None

    elif(comp == 's'):
        if(you == 'w'):
            return False
        elif(you == 'g'):
            return True

    elif(comp == 'w'):
        if(you == 'g'):
            return False
        elif(you == 's'):
            return True

    elif(comp == 'g'):
        if(you == 's'):
            return True
        elif(you == 'w'):
            return False

# Using Random Module for guessing s, w or g.
randNo = random.randint(1, 3)

print("Computer's Turn: Snake(s), Water(w), or Gun(g)?")

if (randNo == 1):
    comp = 's'
elif(randNo == 2):
    comp = 'w'
else:
    comp = 'g'
print(comp)

# Taking input from user.
user = input("Your Turn: Snake(s), Water(w) or Gun(g)?")

a = gameWin(comp, user)

if(a == None):
    print("The game is tie")
elif(a == False):
    print("Computer Win")
else:
    print("You Win")

# Showing the results.
print(f'''You Chose {user}.
Computer Chose {comp}.''')
