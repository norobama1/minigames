import random
import time
from words import words
import string

name = input("Hey! Enter your name:")
print(name+' Ready to play Hangman!!!')
time.sleep(1)
print('Start Guessing....\n')
time.sleep(0.5)

def get_valid_word(words):
   word = random.choice(words)
   while '-' in word or ' ' in word:
      word = random.choice(words)

   return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6
#getting user input
    while len(word_letters)>0 and lives>0:
        #used letters
        print('You have used these letters:', ' '.join(used_letters))
        print(f'You have {lives} left')

        #current word
        word_used = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word:', ' '.join(word_used))

        user_letter = input('Guess the word: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
              word_letters.remove(user_letter)
            else:
             lives = lives -1
             print("Letter is not in the word")

        elif user_letter in used_letters:
            print('You already guessed the letter')
        else:
            print('Invalid')
    
    if lives ==0:
       print('You lost the word was:',word)
    else:
       print('You guessed the word',word)
hangman()