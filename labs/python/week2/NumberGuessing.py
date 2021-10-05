import random

num = random.randint(1,100)
guess = int(input('Please enter your guess: '))
print('Number', num)

while guess != num:
    print('Your guess is too high') if guess > num else print('Your guess is too low')
    guess = int(input('Please enter your new guess: '))
else:
    print('You\'ve guessed correctly! Well Done!')