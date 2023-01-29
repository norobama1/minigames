import random

def game(comp,b):
    if b==comp:
      return 0
    elif comp =='s' and b =='w':
        return -1
    elif comp =='s' and b =='g':
        return 1
    elif comp =='w' and b =='s':
        return 1
    elif comp =='w' and b =='g':
        return -1
    elif comp =='g' and b =='s':
        return -1
    elif comp =='g' and b =='w':
        return 1

print("Snake(s) Water(w) or Gun(g)\n")
randNo = random.randint(1,3)
if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
elif randNo==3:
    comp = 'g'
b = input("Player 2 turn: Snake(s) Water(w) or Gun(g): ")
result = game(comp,b)

print("you choosed",b,'\ncompuer choosed',comp)
if result==0:
    print("Draw")
elif result==1:
    print("You Won")
else:
    print("You Lose")
    