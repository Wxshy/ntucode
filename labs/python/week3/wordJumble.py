import random 

words = ('Python', 'Hockey', 'Cycling', 'PC', 'King', 'Out')
hints = ('A snake', 'A sport with stick and ball', 'Kings of the roads', 'The MasterRace', 'Kai', 'Opposite of In')
i = random.randint(0, len(words))

word = words[i]
hint = hints[i]


correct = word
jumble = ''

while word:
    p = random.randrange(len(word))
    jumble += word[p]
    word = word[:p] + word[p + 1:]

print('''
    HELLO THERE

WELCOME TO WORD JUMBLE
UNSCRAMBLE THE LETTERS
    TO WIN A PRIZE!

Enter !hint to get a hint
''')

print(f'The scrambled word is {jumble}')
guess = input('Please enter your guess: ')

hintUsed = False

if guess.title() == correct: print('Well done you\'ve guessed it on your first attempt')
elif guess == '!hint': 
    hintUsed = True
    print(hint)


while guess.title() != correct and guess:
    print('Unlucky thats not correct. Try again')
    guess = input('Please enter your guess: ')
    if guess == '!hint': 
        hintUsed = False
        print(hint)


if hintUsed: points = 1
else: points = 10

print(f'Well done you guessed the word! You earned {points}') if guess.title() == correct else print('Unfortunately you did not guess the word.')

