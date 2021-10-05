import random

while True:
    try:
        number = int(input('Please enter a number between 1-100: '))
    except ValueError:
        print('Please enter a number between 1-100')
    if number > 100:
        print('Please enter a number between 1-100')
    else:
        break

guess = random.randint(1,100)

i = 1
while guess != number:
    print(f'Guess {i}, number: {guess}')
    i += 1
    if guess < number:
        guess = random.randint(guess,100)
    else:
        guess = random.randint(1,guess)

print(f'The computer took {i} attempts to guess your number!')