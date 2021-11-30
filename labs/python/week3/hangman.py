import random

words = ('Python', 'Hockey', 'Cycling', 'PC', 'King', 'Out')
word = random.choice(words)

print('''

    WELCOME TO HANGMAN

THE AIM IS TO GUESS THE WORD
BY INPUTTING LETTERS TO SEE
IF THEY ARE IN THE WORD

YOU HAVE 5 CHANCES TO FIND
THE LETTERS IN THE WORD

AND THEN ONE FINAL GUESS FOR
THE WHOLE WORD

''')

print(f'There are {len(word)} letters in the word.')
print('GOOOOO!!!!')
print()

attempts = 0
while attempts < 5:
    guess = input('Please enter a letter: ')
    print('yes') if guess.lower() in word.lower() else print('no')
    attempts += 1

print('''

    NOW GUESS THE WORD
''')

final_guess = input('>>> ')

print('You guessed correctly well done!') if final_guess.lower() == word.lower() else print(f'Uh oh thats incorrect better luck next time \nThe word was {word}')