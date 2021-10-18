import random

words = ['Hockey', 'Banana', 'Yellow', 'Sky', 'Dog', 'Moon']

for _ in range(len(words)):
    w = random.choice(words)
    print(w)
    words.remove(w)