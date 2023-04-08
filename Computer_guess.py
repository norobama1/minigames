import random

def computer_guess(x):
    low =1
    high =x
    feedback = ''
    guessess =0
    while feedback != 'c':
        if low!=high:
         guess = random.randint(low,high)
        else:
           guess = low
        feedback = input(f"Is {guess} too high(H),too low(L),or correct(C)")
        guessess +=1
        if feedback =='h':
         high = guess -1
        elif feedback == 'l':
           low = guess+1
    
    print(f"Computer has guessed our number,{guess},correctly in {guessess} guessess")

computer_guess(100)