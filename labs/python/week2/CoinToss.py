from random import randint

#heads = 1 | tails = 0

guess = input('Please guess either heads or tails: ')
if guess == 'heads': guess = 1 
else: guess = 0
wins = 0

for _ in range(10):
    flip = randint(0,1)
    print(f'Flip: {flip}')
    if flip == guess: wins += 1

print(f'You guess correctly {wins}/10!')
