import random
nouns = ('Table', 'Sam', 'Cat', 'Tree', 'Dog', 'Sand')
verbs = ('ran', 'yawned', 'protested', 'fell', 'layed', 'persued')
adjectives = ('lazy', 'red', 'large', 'tiny', 'round', 'loud')

n_random = random.randint(0,5)
v_random = random.randint(0,5)
a_random = random.randint(0,5)

print(nouns[n_random], verbs[v_random], adjectives[a_random])

#--------------------------------------------------------------------------

while True:
    try: 
        n = int(input('Please enter a number for that timestables: '))
    except ValueError:
        print('Please enter a number')
    else:
        break

print([i * n for i in range(1,11)])

#-----------------------------------------------------------------------------

import calendar

while True:
    try: 
        year = int(input('Please enter a year to check: '))
    except ValueError:
        print('Please enter a valid year')
    else:
        break


print(f'{year} is a leap year') if calendar.isleap(year) else print(f'{year} is not a leap year')

#----------------------------------------------------------------------------------------------------

def interest(P, R, T):
    return P * R * T

print('Loan Calculator')

P = float(input('Amount Borrowed: $'))
R = float(input('Interest Rate: '))
T = int(input('Term (years): '))

print(interest(P, R, T))
