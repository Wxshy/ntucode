import random

while True:
    try:
        number = int(input('Please enter a number between 1-100: '))
    except Exception:
        print('Please enter a number between 1-100')
    else: 
        if number > 100:
            print('Please enter a number between 1-100')
        else:
            break

guess = random.randint(1,100)
print(f'Guess 1, number: {guess}')

i = 2
while guess != number:
    i += 1
    if guess < number:
        guess = random.randint(guess,100)
    else:
        guess = random.randint(1,guess)
        
    print(f'Guess {i}, number: {guess}')


print(f'The computer took {i} attempts to guess your number!')