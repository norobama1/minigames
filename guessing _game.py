import random

num = random.randint(1,100)
guessess =0
guess =0
#print(num)
while num!= guess:
   guess = int(input("guess the number btw 1 to 100"))
   guessess +=1  
   if guess>num:
    print("enter a lower number pl! \n")
   elif guess<num:
    print("enter a higher number pl! \n")
   else:
    print("You guessed the number in",guessess,'attempt')


