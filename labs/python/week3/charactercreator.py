class Character:
    def __init__(self):
        self.Strength = 0
        self.Health = 0
        self.Wisdom = 0
        self.Dexterity = 0
    def add_to_character(self, n):
        if n == 1:
            self.Strength += 1
        elif n == 2:
            self.Health += 1
        elif n == 3:
            self.Wisdom += 1
        elif n == 4:
            self.Dexterity += 1

print('''

    WELCOME TO CREATE YOUR CHARACTER

    YOU HAVE 30 POINTS TO ADD TO EITHER:

    1. Strength
    2. Health
    3. Wisdom
    4. Dexterity

''')

points = 30

player = Character()

for i in range(30):
    print(f'You have {points} points left')
    choice = int(input('Please enter the category you would like to add to (1-4): '))
    player.add_to_character(choice)
    points -= 1

print('Here is your character')
print(f'''

    Strength: {player.Strength}
    Health: {player.Health}
    Wisdom: {player.Wisdom}
    Dexterity: {player.Dexterity}

''')