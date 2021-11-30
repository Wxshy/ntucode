from random import choice

h = 0
t = 0

for _ in range(100):
    flip = choice(['heads', 'tails'])
    if flip == 'tails': t += 1
    else: h += 1

print(f'There were {h} heads and {t} tails')
